import argparse,pathlib,json,hashlib,csv,re,datetime,xml.etree.ElementTree as ET
from PIL import Image
ap=argparse.ArgumentParser();ap.add_argument('--resultado',required=True);ap.add_argument('--base',required=True);ap.add_argument('--soportes',required=True);a=ap.parse_args()
F=pathlib.Path(a.resultado);S=pathlib.Path(a.soportes);B=pathlib.Path(a.base);R=json.loads(F.read_text());N=json.loads((B/'necesidades_revisadas.json').read_text());nds={n['id']:n for n in N['necesidades']};entities={x['id']:x for group in [list(nds.values()),R['perfiles_analiticos'],R['historias'],R['perfiles_metadatos']] for x in group};errors=[];checked=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(ok,msg):
 if not ok:errors.append(msg)
def file(p,role):checked.append(dict(archivo=str(p.relative_to(S)),bytes=p.stat().st_size,sha256=sha(p),comprobacion=role))
check(json.loads((S/'objetos/registro_objetos.json').read_text())==R['objetos_digitales'],'Registro no coincide')
for od in R['objetos_digitales']:
 p=S/od['ruta_payload'];check(p.is_file(),'Payload faltante '+str(p))
 if not p.exists():continue
 check(sha(p)==od['sha256'],'Huella distinta '+od['entidad']);check(json.loads(p.read_text())==entities[od['entidad']],'Entidad distinta '+od['entidad']);file(p,'JSON idéntico a entidad canónica y SHA-256 conforme a registro')
cover={x['necesidad']:set(x['historias']) for x in R['cobertura_necesidades']}
for h in R['historias']:
 for n in h['necesidades']:check(h['id'] in cover[n],'Cobertura inversa '+h['id']+n)
 check(all(any(x in nds[n]['evidencias']+nds[n]['evidencia_que_limita'] for n in h['necesidades']) for x in h['evidencias']),'Evidencias fuera de necesidades '+h['id'])
 check(h['tipo']==('IDEAL_A_CONTRASTAR' if any(nds[n]['tipo']=='DESEO_IDEAL' for n in h['necesidades']) else 'ACTUAL_A_PRESERVAR'),'Modalidad '+h['id'])
for m in R['perfiles_metadatos']:
 check(len(m['campos'])==21,'Campos '+m['id'])
 for h in m['historias']:check(next(x for x in R['historias'] if x['id']==h)['perfil_metadatos']==m['id'],'Metadatos inversos')
def csvformat(x):return json.dumps(x,ensure_ascii=False) if isinstance(x,(list,dict)) else ('' if x is None else str(x))
expected={
'historias.csv':[{k:v for k,v in h.items() if k!='metaalgoritmo'} for h in R['historias']],
'cobertura_necesidades.csv':[dict(titulo=nds[x['necesidad']]['titulo'],tipo_n01=nds[x['necesidad']]['tipo'],estado_actual=nds[x['necesidad']]['estado_actual'],**x) for x in R['cobertura_necesidades']],
'perfiles.csv':R['perfiles_analiticos'],
'criterios.csv':[dict(historia=h['id'],**k) for h in R['historias'] for k in h['criterios']],
'metadatos.csv':[dict(perfil=m['id'],historias=m['historias'],**f) for m in R['perfiles_metadatos'] for f in m['campos']],
'estado_fair.csv':R['estado_fair'],
'operaciones.csv':[dict(historia=h['id'],**op) for h in R['historias'] for op in h['metaalgoritmo']],
'registro_objetos.csv':R['objetos_digitales']}
tables=[]
for name,rows in expected.items():
 p=S/'tablas'/name
 with p.open(encoding='utf-8-sig',newline='') as f:actual=list(csv.DictReader(f))
 check(actual==[{k:csvformat(v) for k,v in x.items()} for x in rows],'Tabla distinta '+name);tables.append(dict(archivo=name,filas=len(actual),coincide_con_resultado=len(actual)==len(rows) and actual==[{k:csvformat(v) for k,v in x.items()} for x in rows]));file(p,'CSV cotejado completo con proyección del resultado final')
allids=set(entities)|{k['id'] for h in R['historias'] for k in h['criterios']}
for name in ['perfiles','recorrido']:
 p=S/'figuras'/(name+'.svg');tree=ET.parse(p);txt=' '.join(tree.getroot().itertext())
 for ref in re.findall(r'(?:HU01-[PHMK]|N01-N)\d{3}',txt):check(ref in allids,'Id en figura inexistente '+ref)
 for case in ['E01','E02','E03','E04','E05']:check(case in txt,'Caso ausente en figura '+name+case)
 if name=='recorrido':
  for num in [4,9,16,17,23,29]:check(f'N01-N{num:03}' in txt,'Ideal ausente figura')
 file(p,'XML válido, ids y cobertura de cinco casos; seis ideales en recorrido')
 p=S/'figuras'/(name+'.png')
 with Image.open(p) as im:im.verify()
 file(p,'PNG decodificado; inspección visual separada con huellas')
for p,role in [(S/'objetos/registro_objetos.json','Copia exacta del registro principal'),(S/'procedencia/evidencias_N01.json','Copia exacta de las 351 referencias N01')]:file(p,role)
check(json.loads((S/'procedencia/evidencias_N01.json').read_text())==N['evidencias'],'Evidencias heredadas distintas')
# Fuentes originales siguen intactas.
manifest=json.loads((B/'manifest.json').read_text())
for x in manifest['archivos']:
 p=B/x['ruta'];check(p.stat().st_size==x['bytes'] and sha(p)==x['sha256'],'Entrada modificada '+x['ruta'])
# Todo subdirectorio existente dispone de LEEME; no directorios técnicos vacíos.
for p in [S]+[x for x in S.rglob('*') if x.is_dir()]:check((p/'LEEME.md').exists(),'LEEME faltante '+str(p))
out=dict(estado='SIN_ERRORES' if not errors else 'ERROR',fecha_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),errores=errors,sha256_resultado=sha(F),sha256_script=sha(pathlib.Path(__file__)),conteos=dict(payloads=len(R['objetos_digitales']),tablas=len(tables),figuras_svg=2,exportaciones_png=2,necesidades=len(cover),historias=len(R['historias'])),tablas=tables,archivos_comprobados=checked,alcance='Cotejos técnicos efectivamente ejecutados. No prueba criterios de producto, utilidad, comprensión, interpretación, accesibilidad externa ni revisión humana independiente.')
(S/'control/verificacion_soportes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(estado=out['estado'],errores=errors,archivos=len(checked)),ensure_ascii=False));raise SystemExit(1 if errors else 0)
