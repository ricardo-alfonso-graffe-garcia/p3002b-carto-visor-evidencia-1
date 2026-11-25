#!/usr/bin/env python3
"""N01: estructura, trazabilidad y propuestas de verificación; no acredita prioridad o interpretación."""
from pathlib import Path
import json,re,hashlib,argparse,datetime,sys
def validar(base,r):
 b=Path(base);errors=[];warnings=[]
 def err(at,msg):errors.append({'ruta':at,'mensaje':msg})
 def txt(x,at):
  if not isinstance(x,str) or not x.strip():err(at,'Texto no vacío requerido.')
 def arr(x,at,nonempty=False):
  if not isinstance(x,list):err(at,'Lista requerida.');return []
  if nonempty and not x:err(at,'Lista no vacía requerida.')
  return x
 def refs(x,valid,at,nonempty=False):
  a=arr(x,at,nonempty)
  if any(not isinstance(y,str) for y in a):err(at,'Ids de texto requeridos.');return []
  if len(a)!=len(set(a)):err(at,'Ids repetidos.')
  for y in a:
   if y not in valid:err(at,'Referencia desconocida: '+y)
  return a
 def idx(xs,prefix,at,nonempty=False):
  out={}
  for x in arr(xs,at,nonempty):
   if not isinstance(x,dict):err(at,'Objeto requerido.');continue
   ident=x.get('id')
   if not isinstance(ident,str) or not re.fullmatch(prefix+r'\d{3,}',ident):err(at,'Id inválido.');continue
   if ident in out:err(at,'Id repetido: '+ident)
   out[ident]=x
  return out
 if not isinstance(r,dict):return {'estado':'ERROR','errores':[{'ruta':'$','mensaje':'Objeto requerido.'}],'advertencias':[]}
 p=json.loads((b/'procesos_revisados.json').read_text());d=json.loads((b/'documental_revisado.json').read_text());a=json.loads((b/'actores_revisados.json').read_text());s=json.loads((b/'sintesis_revisada.json').read_text());book=json.loads((b/'libro_comun_v1_3.json').read_text())
 pvs={x['id']:x for x in p['evidencias']};dvs={x['id']:x for x in d['evidencias_documentales']};avs={x['id']:x for x in a['evidencias']};aids={x['id'] for x in a['actores']};prids={x['id'] for actor in a['actores'] for x in actor['preferencias']};hids={x['id'] for x in s['hallazgos']};cids={x['id'] for x in book['codigos_comunes']};comps={x['id'] for pr in p['procesos'] for k in ['nodos','relaciones'] for x in pr[k]};cases={x['entrevista'] for x in p['procesos']};pars={}
 for f in sorted((b/'corpus').glob('*_corpus_analisis_v1.json')):pars.update({x['id']:x for x in json.loads(f.read_text())['parrafos']})
 meta=r.get('metadatos',{})
 for k,v in {'tarea':'N01','resultado_version':'1.1','corpus_version':'1.0','libro_version':'1.3','sintesis_version':'1.1','procesos_version':'1.1','documental_version':'1.1','actores_version':'1.1','estado':'NECESIDADES_REVISADAS_EN_COORDINACION','tipo_revision':'ASISTIDA_POR_LLM','revision_humana_independiente':'PENDIENTE'}.items():
  if meta.get(k)!=v:err('metadatos.'+k,'Se requiere '+v)
 for k in ['modelo','parametros']:
  if k not in meta:err('metadatos.'+k,'Campo requerido; null si no consta.')
 txt(meta.get('fuente_modelo'),'metadatos.fuente_modelo')
 for x in arr(r.get('lectura_entradas'),'lectura_entradas',True):
  for k in ['archivo','alcance','comprobacion']:txt(x.get(k),'lectura_entradas.'+k)
 for x in arr(r.get('criterios_analisis'),'criterios_analisis',True):
  for k in ['criterio','fundamento']:txt(x.get(k),'criterios_analisis.'+k)
 cp=idx(r.get('criterios_priorizacion'),'N01-CP','criterios_priorizacion',True)
 for ident,x in cp.items():
  for k in ['nombre','definicion','regla_uso','limite']:txt(x.get(k),ident+'.'+k)
 ev=idx(r.get('evidencias'),'N01-V','evidencias',True);evcase={};primary=set();sourcesseen=set()
 for ident,x in ev.items():
  for k in ['lectura','limite']:txt(x.get(k),ident+'.'+k)
  kind=x.get('tipo');ref=x.get('referencia');key=(kind,ref)
  if key in sourcesseen:warnings.append({'ruta':ident,'mensaje':'Misma referencia registrada otra vez; revisar independencia y duplicación.'})
  sourcesseen.add(key)
  if kind=='P01':
   if ref not in pvs:err(ident,'Evidencia P01 desconocida.')
   else:
    primary.add(ident);evcase[ident]=pvs[ref]['entrevista']
    if 'cita' in x and x['cita']!=pvs[ref]['cita']:err(ident,'Cita P01 alterada.')
  elif kind=='D01':
   if ref not in dvs:err(ident,'Evidencia D01 desconocida.')
  elif kind=='ACT01':
   if ref not in avs:err(ident,'Evidencia ACT01 desconocida.')
   else:
    if avs[ref]['tipo']=='CANONICA':primary.add(ident);evcase[ident]=avs[ref]['entrevista']
    if 'cita' in x and x['cita']!=avs[ref].get('cita'):err(ident,'Cita ACT01 alterada.')
  elif kind=='CANONICA':
   if ref not in pars:err(ident,'Párrafo desconocido.');continue
   par=pars[ref];start=x.get('inicio');end=x.get('fin')
   if x.get('entrevista')!=ref[:3] or x.get('turno_id')!=par['turno']:err(ident,'Entrevista/turno incorrectos.')
   if x.get('voz')!=par['voz'] or par['voz']!='Participante':err(ident,'Conservar voz participante.')
   if type(start)!=int or type(end)!=int or not (0<=start<end<=len(par['texto'])) or par['texto'][start:end]!=x.get('cita'):err(ident,'Cita u offsets no coinciden literalmente.')
   primary.add(ident);evcase[ident]=ref[:3]
  else:err(ident,'Tipo de evidencia inválido.')
 ns=idx(r.get('necesidades'),'N01-N','necesidades',True);kids=set()
 for ident,x in ns.items():
  for k in ['titulo','enunciado','contexto','decision','objeto_informacion','informacion_actual','faltante_o_deseada','condiciones_y_limites','contexto_elicitacion']:txt(x.get(k),ident+'.'+k)
  aa=refs(x.get('actores'),aids,ident+'.actores',True);ee=refs(x.get('entrevistas'),cases,ident+'.entrevistas',True);vv=refs(x.get('evidencias'),set(ev),ident+'.evidencias',True)
  if not set(vv)&primary:err(ident,'La necesidad atribuida requiere evidencia directa de participante, no solo documento.')
  if not set(ee)<={evcase[v] for v in vv if v in evcase}:err(ident,'Cada caso requiere evidencia propia de participante.')
  if x.get('tipo') not in {'NECESIDAD_ACTUAL','DESEO_IDEAL','INFERENCIA_ANALITICA_CONDICIONAL'}:err(ident,'Tipo de necesidad inválido.')
  if x.get('estado_actual') not in {'ATENDIDA_EN_EPISODIO','PARCIAL_DECLARADA','CARENCIA_DECLARADA','NO_APLICA_AL_IDEAL','NO_DETERMINABLE'}:err(ident,'Estado actual inválido.')
  contrary=refs(x.get('evidencia_que_limita'),set(ev),ident+'.evidencia_que_limita')
  if not contrary:txt(x.get('razon_sin_contraevidencia'),ident+'.razon_sin_contraevidencia')
  elif 'razon_sin_contraevidencia' not in x:err(ident,'Declarar razon_sin_contraevidencia, null si no aplica.')
  for k in ['soportes_mencionados','conservar','incognitas']:
   for y in arr(x.get(k),ident+'.'+k):txt(y,ident+'.'+k)
  refs(x.get('codigos_comunes'),cids,ident+'.codigos_comunes');refs(x.get('hallazgos_s01'),hids,ident+'.hallazgos_s01');refs(x.get('componentes_p01'),comps,ident+'.componentes_p01');refs(x.get('preferencias_act01'),prids,ident+'.preferencias_act01')
  variants=[]
  for y in arr(x.get('variantes_por_caso'),ident+'.variantes_por_caso'):
   variants.append(y.get('entrevista'));refs(y.get('actores'),aids,ident+'.variante.actores',True);vs=refs(y.get('evidencias'),set(ev),ident+'.variante.evidencias',True)
   for k in ['particularidad','limites']:txt(y.get(k),ident+'.variante.'+k)
   if y.get('entrevista') not in ee or y.get('entrevista') not in {evcase[v] for v in vs if v in evcase}:err(ident,'Variante sin respaldo propio de ese caso.')
  if len(ee)>1 and sorted(str(y) for y in variants)!=sorted(ee):err(ident,'Necesidad compartida exige una variante por caso.')
  geo=x.get('vinculo_territorial',{})
  if geo.get('tipo') not in {'ESPACIAL_DIRECTO','REFERENCIA_DE_LUGAR','RELACION_CONTEXTUAL','NO_CARTOGRAFICO_DIRECTO','NO_DETERMINABLE'}:err(ident,'Tipo territorial inválido.')
  for k in ['razon','limites']:txt(geo.get(k),ident+'.vinculo_territorial.'+k)
  refs(geo.get('evidencias'),set(ev),ident+'.vinculo_territorial.evidencias',True)
  for y in arr(x.get('vinculos_sectoriales'),ident+'.vinculos_sectoriales',True):
   for k in ['actividad','razon','limites']:txt(y.get(k),ident+'.sector.'+k)
   if y.get('sector') not in {'PUBLICO','ACADEMICO','SOCIEDAD_CIVIL','PRIVADO','CIUDADANIA','MIXTO'}:err(ident,'Sector inválido.')
   if y.get('estatus_iniciativa') not in {'IDENTIFICADA_DOCUMENTALMENTE','ACTIVIDAD_RELATADA_SIN_NOMBRE_FORMAL','NO_IDENTIFICADA'}:err(ident,'Estatus de iniciativa inválido.')
   if 'iniciativa' not in y or (y['iniciativa'] is not None and not isinstance(y['iniciativa'],str)):err(ident,'Iniciativa: texto o null requerido.')
   if y.get('estatus_iniciativa')=='IDENTIFICADA_DOCUMENTALMENTE':txt(y.get('iniciativa'),ident+'.sector.iniciativa')
   if y.get('nexo') not in {'PUBLICO_DIRECTO','RELEVANCIA_PUBLICA_POR_VALIDAR','USO_PRIVADO','REFERENCIA_CONTEXTUAL'}:err(ident,'Nexo inválido.')
   refs(y.get('evidencias'),set(ev),ident+'.sector.evidencias',True)
  for y in arr(x.get('verificacion'),ident+'.verificacion',True):
   kid=y.get('id')
   if not isinstance(kid,str) or not re.fullmatch(r'N01-K\d{3,}',kid) or kid in kids:err(ident,'Id de criterio inválido/repetido.')
   kids.add(kid)
   for k in ['observable','metodo','limites']:txt(y.get(k),str(kid)+'.'+k)
   if y.get('origen') not in {'DECLARADO','PROPUESTA_ANALITICA'} or y.get('estado')!='PROPUESTA_NO_EJECUTADA':err(str(kid),'Origen/estado de comprobación inválido; no declarar pruebas realizadas.')
   refs(y.get('evidencias'),set(ev),str(kid)+'.evidencias',True)
  pr=x.get('prioridad',{})
  for k in ['razon','limites']:txt(pr.get(k),ident+'.prioridad.'+k)
  if pr.get('ambito') not in set(ee)|{'PORTAFOLIO_EXPLORATORIO'}:err(ident,'Ámbito de prioridad no corresponde a sus casos.')
  if pr.get('nivel') not in {'ALTA','MEDIA','BAJA','PENDIENTE'} or pr.get('origen') not in {'ANALISIS_CONDICIONAL','DECLARADA_POR_PARTICIPANTE'}:err(ident,'Nivel/origen de prioridad inválido.')
  refs(pr.get('criterios'),set(cp),ident+'.prioridad.criterios',True);cmp=refs(pr.get('comparables'),set(ns),ident+'.prioridad.comparables')
  if ident in cmp:err(ident,'No compararse consigo misma.')
  for other in cmp:
   if other in ns and pr.get('ambito') in cases and pr['ambito'] not in ns[other].get('entrevistas',[]):err(ident,'Comparación fuera de la misma actividad.')
 cov=[]
 for x in arr(r.get('cobertura_casos'),'cobertura_casos',True):
  case=x.get('entrevista');cov.append(case);nn=refs(x.get('necesidades'),set(ns),'cobertura_casos.necesidades',True)
  for k in ['lectura_actual','lectura_ideal','decisiones_y_suficiencia']:txt(x.get(k),'cobertura_casos.'+k)
  for y in arr(x.get('omisiones_justificadas'),'cobertura_casos.omisiones_justificadas'):txt(y,'cobertura_casos.omisiones_justificadas')
  if set(nn)!={nid for nid,n in ns.items() if case in n.get('entrevistas',[])}:err(str(case),'Cobertura de necesidades inconsistente con sus casos.')
 if sorted(str(x) for x in cov)!=sorted(cases):err('cobertura_casos','Cubrir los cinco casos exactamente una vez.')
 cov=[]
 for x in arr(r.get('cobertura_hallazgos'),'cobertura_hallazgos',True):
  hid=x.get('hallazgo');cov.append(hid);nn=refs(x.get('necesidades'),set(ns),'cobertura_hallazgos.necesidades');txt(x.get('justificacion'),'cobertura_hallazgos.justificacion')
  if x.get('tratamiento') not in {'INTEGRADO','CONTEXTO','NO_GENERA_NECESIDAD_NUEVA'}:err(str(hid),'Tratamiento inválido.')
  if x.get('tratamiento')=='INTEGRADO' and not nn:err(str(hid),'Hallazgo integrado requiere necesidad de destino.')
 if sorted(str(x) for x in cov)!=sorted(hids):err('cobertura_hallazgos','Cubrir los 22 hallazgos exactamente una vez.')
 decisions=idx(r.get('decisiones_de_consolidacion'),'N01-D','decisiones_de_consolidacion',True)
 for ident,x in decisions.items():
  for k in ['formulacion_revisada','razon']:txt(x.get(k),ident+'.'+k)
  if x.get('origen') not in {'PROPUESTA_ANALITICA','PARAFRASIS_DE_PASAJE','SOLICITUD_DOCUMENTAL'} or x.get('decision') not in {'DIVIDIDA','FUSIONADA','DESCARTADA_COMO_SOLUCION','SOLO_CONTEXTO','PENDIENTE'}:err(ident,'Origen/decisión inválidos.')
  refs(x.get('evidencias'),set(ev),ident+'.evidencias',True);refs(x.get('necesidades_destino'),set(ns),ident+'.necesidades_destino')
 for x in arr(r.get('agenda_validacion'),'agenda_validacion',True):
  if 'necesidad' not in x or (x['necesidad'] is not None and x['necesidad'] not in ns):err('agenda_validacion','Necesidad válida o null requerido.')
  for k in ['pendiente','por_que_importa','proxima_comprobacion']:txt(x.get(k),'agenda_validacion.'+k)
 for x in arr(r.get('limites'),'limites',True):
  for k in ['descripcion','consecuencia']:txt(x.get(k),'limites.'+k)
 return {'validador':'Necesidades N01 revisada 1.1','estado':'SIN_ERRORES_ESTRUCTURALES' if not errors else 'ERROR','errores':errors,'advertencias':warnings,'conteos':{'necesidades':len(ns),'evidencias':len(ev),'criterios_priorizacion':len(cp),'criterios_verificacion':len(kids),'casos':len(r.get('cobertura_casos',[])),'hallazgos_cubiertos':len(r.get('cobertura_hallazgos',[])),'decisiones_consolidacion':len(decisions)},'alcance':'Control técnico de estructura, referencias, cobertura y citas. No valida interpretación, prioridad, aceptación, independencia, contenido web, figuras, aplicación normativa o revisión humana.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('base');ap.add_argument('resultado');ap.add_argument('--salida',required=True);a=ap.parse_args();f=Path(a.resultado)
 try:out=validar(a.base,json.loads(f.read_text()))
 except (ValueError,TypeError,KeyError,AttributeError,OSError) as ex:out={'validador':'Necesidades N01 revisada 1.1','estado':'ERROR','errores':[{'ruta':'$','mensaje':'Control incompleto: '+str(ex)}],'advertencias':[]}
 out['ejecucion']={'estado':'EJECUTADO','fecha_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'comando_argumentos':sys.argv,'sha256_resultado_evaluado':hashlib.sha256(f.read_bytes()).hexdigest() if f.exists() else None,'sha256_validador':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'codigo_salida':0 if not out['errores'] else 1};Path(a.salida).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'estado':out['estado'],'errores':len(out['errores']),'salida':a.salida},ensure_ascii=False));sys.exit(out['ejecucion']['codigo_salida'])
