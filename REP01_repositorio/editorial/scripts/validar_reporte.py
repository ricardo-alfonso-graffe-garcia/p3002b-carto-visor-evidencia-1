from pathlib import Path
import json,re,hashlib,argparse,datetime
MARKERS=['PORTADA','CUERPO','REFERENCIAS','DECLARACION_IA']
def validar(base,md,j,repo):
 errors=[];warnings=[]
 def ck(ok,path,msg):
  if not ok:errors.append({'ruta':path,'mensaje':msg})
 def pathok(v):
  if not isinstance(v,str)or not v:return False
  q=Path(v)
  return not q.is_absolute()and '..'not in q.parts and (repo/q).resolve().is_relative_to(repo.resolve())and(repo/q).is_file()
 m=j.get('metadatos',{});ck(m.get('tarea')=='REP01'and m.get('version')=='1.0'and m.get('estado')=='MANUSCRITO_PARA_REVISION','metadatos','Tarea/versión/estado incorrectos.');ck(m.get('autor')=='Ricardo Alfonso Graffe Garcia'and m.get('matricula')=='A01664904','metadatos.autor','Autor/matrícula no coinciden con indicación expresa.');ck(m.get('revision_humana_independiente')=='PENDIENTE'and m.get('paginacion_estado')=='PENDIENTE_MAQUETACION','metadatos','No se acredita revisión humana o paginación final en esta etapa.')
 for label in MARKERS:
  ck(md.count('<!-- '+label+'_INICIO -->')==1 and md.count('<!-- '+label+'_FIN -->')==1,label,'Delimitadores únicos requeridos.')
  ck(md.find('<!-- '+label+'_INICIO -->')<md.find('<!-- '+label+'_FIN -->'),label,'Orden de delimitadores incorrecto.')
 body=md.split('<!-- CUERPO_INICIO -->')[-1].split('<!-- CUERPO_FIN -->')[0];words=len(re.findall(r'\b[\wÁÉÍÓÚÑáéíóúñ]+\b',body))
 if words>3800:warnings.append({'ruta':'cuerpo','mensaje':'Extensión de '+str(words)+' palabras: revisar presupuesto de figuras; conteo no equivale a páginas.'})
 ck('Ricardo Alfonso Graffe Garcia'in md and 'A01664904'in md,'portada','Falta autor o matrícula.')
 sections={x['id']:x for x in j.get('secciones',[])};ck(bool(sections)and len(sections)==len(j.get('secciones',[])),'secciones','Secciones requeridas sin ids duplicados.')
 for id,x in sections.items():
  ck(bool(re.fullmatch(r'REP01-S\d{3}',id))and x.get('ancla')in md and x.get('funcion_argumental'),id,'Id/ancla o función argumental no resuelven.')
  for f in x.get('soportes',[]):ck(pathok(f),id+'.soportes','Archivo de soporte inexistente/inseguro.')
 canon={}
 for f in(base/'base_repositorio/analisis/insumos').glob('E0*_corpus_analisis_v1.json'):canon.update({p['id']:p for p in json.loads(f.read_text())['parrafos']})
 voices=set();qs=j.get('citas',[]);seen=set()
 for q in qs:
  id=q.get('id','');ck(bool(re.fullmatch(r'REP01-Q\d{3}',id))and id not in seen,id,'Id de cita inválido/duplicado.');seen.add(id);p=canon.get(q.get('parrafo'),{})
  ck(q.get('voz')==p.get('voz')=='Participante'and q.get('cita')and q['cita']in p.get('texto',''),id,'Cita no continua/literal o voz incorrecta.');ck(q.get('cita','__NO__')in body,id,'Cita no presente en cuerpo.');ck(q.get('entrevista')==str(q.get('parrafo','')).split('-')[0],id,'Entrevista/párrafo incompatibles.');voices.add(q.get('entrevista'));ck(q.get('seccion')in sections and pathok(q.get('ruta_fuente')),id,'Sección o ruta fuente inexistente.')
  for c in q.get('contexto_pregunta',[]):ck(c in canon,id,'Párrafo contextual inexistente.')
 ck(voices=={'E01','E02','E03','E04','E05'},'citas','Se requieren cinco voces en citas verificables del cuerpo.')
 # Todos los ids definidos por fuentes preferidas, sin tratar menciones como definiciones.
 ids={'MET-JANUS'}
 def collect(v):
  if isinstance(v,dict):
   if isinstance(v.get('id'),str):ids.add(v['id'])
   for x in v.values():collect(x)
  elif isinstance(v,list):
   for x in v:collect(x)
 for rel in json.loads((base/'registro_entradas.json').read_text())['json_preferidos']:collect(json.loads((base/'base_repositorio'/rel).read_text()))
 ids.update(canon)
 for a in j.get('afirmaciones',[]):
  ck(a.get('seccion')in sections and a.get('tipo')in ['RELATO','DOCUMENTAL','INTERPRETACION','PROPUESTA'],'afirmaciones','Tipo o sección incorrectos.');ck(pathok(a.get('soporte'))and bool(a.get('localizador'))and bool(a.get('limite')),'afirmaciones','Soporte/localizador/límite requerido.')
  ck(bool(a.get('objetos_fuente'))and all(x in ids for x in a.get('objetos_fuente',[])),'afirmaciones','Objeto fuente no definido.')
 ck(bool(j.get('afirmaciones')),'afirmaciones','Falta registro de afirmaciones centrales.')
 for f in j.get('figuras',[]):ck(pathok(f.get('archivo'))and f.get('seccion')in sections,'figuras','Ruta o sección inexistente.');ck(f.get('estado_revision')in ['REALIZADA','PENDIENTE']and bool(f.get('alcance_revision')),'figuras','Revisión de figura sin alcance.')
 req={x['id']for x in json.loads((base/'requisitos/02_matriz_requisitos.json').read_text())};coverage=j.get('cobertura_requisitos',[])
 ck(len(coverage)==208 and {x.get('requisito')for x in coverage}==req,'cobertura_requisitos','Se requieren exactamente 208 requisitos distintos.')
 for x in coverage:
  ck(x.get('estado')in ['ATENDIDO_EN_MANUSCRITO','ATENDIDO_EN_SOPORTE','PARCIAL','PENDIENTE','NO_APLICA_JUSTIFICADO']and bool(x.get('evidencia_cumplimiento'))and bool(x.get('limite')),'cobertura_requisitos','Estado/prueba/límite requeridos.')
  ck(all(k in sections for k in x.get('secciones',[]))and all(pathok(f)for f in x.get('soportes',[])),'cobertura_requisitos','Referencia editorial no resuelve.')
  if x.get('estado')=='ATENDIDO_EN_MANUSCRITO':ck(bool(x.get('secciones')),'cobertura_requisitos','Falta sección del manuscrito.')
  if x.get('estado')=='ATENDIDO_EN_SOPORTE':ck(bool(x.get('soportes')),'cobertura_requisitos','Falta soporte.')
 inv=j.get('repositorio',{}).get('inventario',[]);paths=[x.get('ruta')for x in inv];actual={str(f.relative_to(repo))for f in repo.rglob('*')if f.is_file()and str(f.relative_to(repo))!='manifest.json'and '__pycache__'not in f.parts}
 ck(len(paths)==len(set(paths))and set(paths)==actual,'repositorio.inventario','Inventario no cubre exactamente archivos finales, salvo manifest.json raíz.')
 for x in inv:
  if pathok(x.get('ruta')):
   f=repo/x['ruta'];ck(f.stat().st_size==x.get('bytes')and hashlib.sha256(f.read_bytes()).hexdigest()==x.get('sha256'),'inventario','Tamaño/huella distinta: '+x['ruta'])
  else:ck(False,'inventario','Ruta inválida/faltante.')
 # Comprobar originales canónicos que el diseño editorial no puede alterar.
 for x in json.loads((base/'registro_entradas.json').read_text())['fuentes_inmutables']:
  ck(pathok(x['ruta'])and hashlib.sha256((repo/x['ruta']).read_bytes()).hexdigest()==x['sha256'],'fuentes_inmutables','Fuente alterada/omitida: '+x['ruta'])
 for dir in [repo]+[x for x in repo.rglob('*')if x.is_dir()and '__pycache__'not in x.parts]:ck((dir/'LEEME.md').is_file()or(dir/'README.md').is_file(),'navegacion','Carpeta sin guía: '+str(dir.relative_to(repo)))
 for k in ['lectura_entradas','tesis_y_estructura','referencias','incidencias','pendientes_maquetacion','limites']:ck(bool(j.get(k)),k,'Registro requerido, sin completar por apariencia.')
 for ref in j.get('referencias',[]):ck(ref.get('estado')in ['VERIFICADA','PENDIENTE']and ref.get('referencia_completa')and ref.get('localizador_consultado'),'referencias','Referencia incompleta o estado inválido.')
 return {'validador':'REP01 editorial 1.0','estado':'SIN_ERRORES_ESTRUCTURALES'if not errors else 'ERROR','errores':errors,'advertencias':warnings,'conteos':{'palabras_cuerpo':words,'secciones':len(sections),'citas':len(qs),'voces':len(voices),'afirmaciones':len(j.get('afirmaciones',[])),'figuras':len(j.get('figuras',[])),'requisitos':len(coverage),'archivos_inventariados':len(inv)},'paginacion':'PENDIENTE_MAQUETACION','alcance':'Cotejo documental estructural y literal. No certifica calidad narrativa, pertinencia semántica, fuentes externas, inspección real de figuras, veracidad de metadatos declarados, validación humana o diez páginas maquetadas.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('base');ap.add_argument('manuscrito');ap.add_argument('trazabilidad');ap.add_argument('--repositorio',required=True);ap.add_argument('--salida');a=ap.parse_args()
 try:out=validar(Path(a.base),Path(a.manuscrito).read_text(),json.loads(Path(a.trazabilidad).read_text()),Path(a.repositorio))
 except(ValueError,KeyError,AttributeError,TypeError,OSError)as e:out={'validador':'REP01 editorial 1.0','estado':'ERROR','errores':[{'ruta':'$','mensaje':'Control incompleto: '+str(e)}],'advertencias':[]}
 out['ejecucion']={'fecha_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argumentos':__import__('sys').argv,'sha256_manuscrito':hashlib.sha256(Path(a.manuscrito).read_bytes()).hexdigest(),'sha256_trazabilidad':hashlib.sha256(Path(a.trazabilidad).read_bytes()).hexdigest(),'sha256_validador':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 if a.salida:Path(a.salida).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'estado':out['estado'],'errores':len(out['errores'])},ensure_ascii=False));raise SystemExit(bool(out['errores']))
