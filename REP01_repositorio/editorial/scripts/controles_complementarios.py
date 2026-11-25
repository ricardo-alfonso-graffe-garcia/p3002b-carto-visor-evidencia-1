"""Cotejos locales REP01; sin acreditar validez semántica o revisión humana."""
from pathlib import Path
import argparse,json,re,hashlib,urllib.parse,xml.etree.ElementTree as ET
from collections import Counter

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def run(repo,md,trace,base):
 errors=[];info={}
 def check(test,where,msg):
  if not test:errors.append({'ruta':where,'mensaje':msg})
 canon={}
 for f in (repo/'analisis/insumos').glob('E0*_corpus_analisis_v1.json'):
  canon.update({x['id']:x for x in read(f)['parrafos']})
 allids=set(canon)|{'MET-JANUS'}
 def ids(v):
  if isinstance(v,dict):
   if isinstance(v.get('id'),str):allids.add(v['id'])
   for y in v.values():ids(y)
  elif isinstance(v,list):
   for y in v:ids(y)
 reg=read(repo/'editorial/fuentes/registro_entradas.json')
 for rel in reg['json_preferidos']:ids(read(repo/rel))
 segments=assignments=coverage=0;codestats=[]
 for i in range(1,6):
  f=next((repo/f'analisis/recodificacion/R0{i}').glob('*.json'));d=read(f)
  for seg in d['segmentos']:
   p=canon.get(seg['parrafo_id'],{});q=seg['cita']
   check(p.get('voz')=='Participante',seg['id'],'Voz no participante.')
   check(p.get('texto','')[seg['inicio']:seg['fin']]==q,seg['id'],'Cita/offset distinto al corpus.')
   check(all(x in allids for x in seg['codigos']),seg['id'],'Código no definido.')
   segments+=1;assignments+=len(seg['codigos'])
  coverage+=len(d['cobertura'])
  codestats.append({'archivo':str(f.relative_to(repo)),'version':d['metadatos']['resultado_version'],'fragmentos':len(d['segmentos']),'parrafos_cobertura':len(d['cobertura'])})
 check((coverage,segments,assignments)==(545,713,971),'recodificacion','Conteos distintos del cierre de referencia.')
 info['recodificacion']={'parrafos_participantes':coverage,'fragmentos':segments,'asignaciones':assignments,'detalle':codestats,'alcance':'Literalidad/offsets/códigos definidos; no nueva recodificación semántica ni medición de concordancia.'}
 book=read(repo/'55_libro_comun_v1_3.json');nexamples=0
 for code in book['codigos_comunes']:
  for e in code['ejemplos']:
   check(e['cita']in canon[e['parrafo_id']]['texto'],code['id'],'Ejemplo no literal continuo.');nexamples+=1
 check((len(book['codigos_comunes']),nexamples)==(64,123),'libro','Cardinalidad de libro distinta.')
 info['libro']={'codigos':len(book['codigos_comunes']),'ejemplos_cotejados':nexamples,'alcance':'Cotejo textual, no pilotaje humano.'}
 need=read(repo/'82_necesidades_v1_1.json');cnt=0
 for ev in need['evidencias']:
  pid=ev.get('referencia');q=ev.get('cita')
  if pid in canon and q:
   check(q in canon[pid]['texto'],ev['id'],'Evidencia N01 no coincide con párrafo.');cnt+=1
 info['evidencias_N01']={'cotejos_literales':cnt,'total':len(need['evidencias']),'alcance':'No evaluación automática de interpretación.'}
 hu=read(repo/'88_historias_y_objetos_v1_1.json')
 sub=repo/'analisis/historias/HU01/soportes_revisados_v1_1'
 objects=read(sub/'objetos/registro_objetos.json')
 if isinstance(objects,dict):
  objects=objects.get('objetos',objects.get('objetos_digitales',objects.get('registros',[])))
 check(objects==hu['objetos_digitales'],'objetos/registro_objetos.json','Registro no coincide con JSON principal.')
 for ob in objects:
  p=sub/ob['ruta_payload']
  check(p.is_file(),ob['id'],'Payload inexistente.')
  if p.is_file():
   check(sha(p)==ob['sha256'],ob['id'],'Huella de payload distinta.')
   content=read(p);check(content.get('id')==ob['entidad'],ob['id'],'Entidad del payload distinta.')
  for rel in ob['relaciones']:check(rel['destino_entidad']in allids,ob['id'],'Relación a entidad desconocida.')
 info['objetos_HU01']={'registros':len(objects),'payloads_cotejados':len(objects),'base_resolucion':str(sub.relative_to(repo)),'alcance':'Relaciones/archivos locales y huellas; no conformidad FDO/FAIR ni registro externo.'}
 # Solo enlaces de lectura editorial: las rutas de prompts históricos son evidencia, no interfaz actual.
 links=[];externals=[]
 paths=[md,repo/'LEEME.md']+list((repo/'editorial').rglob('*.md'))
 for p in paths:
  for target in re.findall(r'!?\[[^\]]*\]\(([^\n]+?)\)',p.read_text()):
   target=target.strip('<>')
   if re.match(r'^[a-zA-Z]+:',target):externals.append(target);continue
   raw,_,anchor=target.partition('#')
   f=(p.parent/urllib.parse.unquote(raw)).resolve() if raw else p
   check(f.is_file(),str(p),'Enlace local no resuelve: '+target)
   if f.is_file() and anchor and f.suffix=='.md':
    check(anchor in f.read_text(),str(p),'Ancla explícita no encontrada: '+target)
   links.append({'origen':str(p.relative_to(repo)) if p.is_relative_to(repo)else p.name,'destino':target,'existe':f.is_file()})
 info['navegacion_editorial']={'enlaces_comprobados':len(links),'detalle':links,'enlaces_externos_distintos':len(set(externals)),'alcance':'Existencia de archivos y anclas editoriales. No se comprueban en masa URLs ni rutas históricas de prompts como interfaz actual.'}
 inv=read(repo/'editorial/registros/indice_inverso.json')['parrafos']
 check(set(inv)==set(canon),'indice_inverso','No cubre exactamente todos los párrafos.')
 mapped=set(n for v in inv.values()for n in v['necesidades'])
 check(mapped=={x['id']for x in need['necesidades']},'indice_inverso','No enlaza todas las necesidades desde los párrafos.')
 check(all(q['id']in [x['id']for x in inv[q['parrafo']]['citas_reporte']]for q in trace['citas']),'indice_inverso','Cita editorial sin vínculo inverso.')
 info['indice_inverso']={'parrafos':len(inv),'parrafos_con_necesidades':sum(bool(x['necesidades'])for x in inv.values()),'necesidades_distintas':len(mapped)}
 old=base/'base_repositorio';changed=[];missing=[]
 for f in old.rglob('*'):
  if f.is_file():
   dst=repo/f.relative_to(old)
   if not dst.is_file():missing.append(str(f.relative_to(old)))
   elif sha(f)!=sha(dst):changed.append(str(f.relative_to(old)))
 check(not missing and changed==['LEEME.md'],'base_curada','Fuentes omitidas o alteradas fuera del LEEME editorial: '+str(changed+missing))
 info['originales']={'archivos_base':sum(p.is_file()for p in old.rglob('*')),'faltantes':missing,'modificados':changed,'excepcion':'LEEME.md raíz sustituido por guía final, sin tocar fuentes canónicas.'}
 png=[]
 from PIL import Image
 for fig in trace['figuras']:
  for key in ['archivo','editable','vector']:check((repo/fig[key]).is_file(),fig['id'],'Falta exportación/fuente '+key)
  p=repo/fig['archivo']
  with Image.open(p)as im:im.verify()
  with Image.open(p)as im:png.append({'id':fig['id'],'pixeles':list(im.size),'sha256':sha(p)})
  svg=ET.parse(repo/fig['vector']).getroot();check('viewBox'in svg.attrib,fig['id'],'SVG sin viewBox.')
 info['figuras']={'archivos_decodificados':png,'inspeccion_visual':'Registrada aparte en revision_figuras.json; efectuada por asistente, no inferida de decodificación.','maquetacion':'PENDIENTE_MAQUETACION'}
 info['cobertura_requisitos']=dict(Counter(x['estado']for x in trace['cobertura_requisitos']))
 return {'control':'REP01 complementario 1.0','estado':'SIN_ERRORES_EN_ALCANCE_COMPROBADO'if not errors else'ERROR','errores':errors,'resultados':info,'limites':['No verifica verdad externa, calidad narrativa integral, acuerdos humanos, ejecución de productos o diez páginas.','No reejecuta todos los controles históricos; examina los artefactos indicados.']}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('repositorio');ap.add_argument('manuscrito');ap.add_argument('trazabilidad');ap.add_argument('base');ap.add_argument('--salida',required=True);a=ap.parse_args()
 repo=Path(a.repositorio).resolve();md=Path(a.manuscrito).resolve();tr=Path(a.trazabilidad).resolve();base=Path(a.base).resolve()
 result=run(repo,md,read(tr),base)
 result['ejecucion']={'fecha_utc':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'sha256_script':sha(Path(__file__)),'sha256_manuscrito':sha(md),'nota':'No se incluye huella del JSON externo en control interno para evitar ciclos al completar inventario.'}
 Path(a.salida).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'estado':result['estado'],'errores':result['errores'],'resultados':{k:v for k,v in result['resultados'].items()if k in ['indice_inverso','cobertura_requisitos']}},ensure_ascii=False))
 raise SystemExit(bool(result['errores']))
