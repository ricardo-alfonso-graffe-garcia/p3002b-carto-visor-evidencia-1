#!/usr/bin/env python3
"""HU01: contrato, procedencia y payloads locales; no certifica FAIR/FDO o utilidad."""
from pathlib import Path
import json,re,hashlib,argparse,sys,datetime
FAIR=['F1','F2','F3','F4','A1','A1.1','A1.2','A2','I1','I2','I3','R1','R1.1','R1.2','R1.3']
CAMPOS=['variables_significados','fuente_responsable','unidad','cobertura_geografica','escala_espacial','resolucion_espacial','representacion','referencia_espacial','periodo','resolucion_temporal','actualizacion','calidad','incertidumbre','agregacion','denominador','acceso','licencia','procedencia','versiones','transformaciones','vocabulario']
def validar(base,r,soportes=None):
 b=Path(base);errors=[];warnings=[]
 def err(at,msg):errors.append({'ruta':at,'mensaje':msg})
 def txt(x,at):
  if not isinstance(x,str) or not x.strip():err(at,'Texto no vacío requerido.')
 def arr(x,at,nonempty=False):
  if not isinstance(x,list):err(at,'Lista requerida.');return []
  if nonempty and not x:err(at,'Lista no vacía requerida.')
  return x
 def refs(x,valid,at,nonempty=False):
  aa=arr(x,at,nonempty)
  if any(not isinstance(v,str) for v in aa):err(at,'Ids de texto requeridos.');return []
  if len(set(aa))!=len(aa):err(at,'Ids repetidos.')
  for v in aa:
   if v not in valid:err(at,'Id desconocido: '+v)
  return aa
 def idx(xs,prefix,at,nonempty=False):
  out={}
  for x in arr(xs,at,nonempty):
   if not isinstance(x,dict):err(at,'Objeto requerido.');continue
   i=x.get('id')
   if not isinstance(i,str) or not re.fullmatch(prefix+r'\d{3,}',i):err(at,'Id inválido.');continue
   if i in out:err(at,'Id repetido.')
   out[i]=x
  return out
 n=json.loads((b/'necesidades_revisadas.json').read_text());a=json.loads((b/'actores_revisados.json').read_text());needs={x['id']:x for x in n['necesidades']};ev={x['id']:x for x in n['evidencias']};acts={x['id'] for x in a['actores']};cases={'E01','E02','E03','E04','E05'};nk={k['id'] for x in n['necesidades'] for k in x['verificacion']}
 meta=r.get('metadatos',{})
 for k,v in {'tarea':'HU01','resultado_version':'1.1','corpus_version':'1.0','libro_version':'1.3','sintesis_version':'1.1','procesos_version':'1.1','documental_version':'1.1','actores_version':'1.1','necesidades_version':'1.1','estado':'HISTORIAS_REVISADAS_EN_COORDINACION','tipo_revision':'ASISTIDA_POR_LLM','revision_humana_independiente':'PENDIENTE'}.items():
  if meta.get(k)!=v:err('metadatos.'+k,'Se requiere '+v)
 for k in ['modelo','parametros']:
  if k not in meta:err('metadatos.'+k,'Campo requerido; null si no consta.')
 txt(meta.get('fuente_modelo'),'metadatos.fuente_modelo')
 for x in arr(r.get('lectura_entradas'),'lectura_entradas',True):
  for k in ['archivo','alcance','comprobacion']:txt(x.get(k),'lectura_entradas.'+k)
 for x in arr(r.get('decisiones_metodologicas'),'decisiones_metodologicas',True):
  for k in ['decision','fundamento']:txt(x.get(k),'decisiones_metodologicas.'+k)
 for x in arr(r.get('citas_ilustrativas'),'citas_ilustrativas'):
  ref=x.get('referencia');quote=x.get('cita');txt(x.get('uso'),'citas_ilustrativas.uso')
  if ref not in ev or ev[ref]['tipo']!='CANONICA' or not isinstance(quote,str) or not quote or quote not in ev[ref]['cita']:err('citas_ilustrativas','Fragmento literal canónico N01 requerido.')
 profiles=idx(r.get('perfiles_analiticos'),'HU01-P','perfiles_analiticos',True);stories=idx(r.get('historias'),'HU01-H','historias',True);mds=idx(r.get('perfiles_metadatos'),'HU01-M','perfiles_metadatos',True);allcases=set();kidset=set();opset=set()
 def sourcecheck(x,ident):
  es=refs(x.get('entrevistas'),cases,ident+'.entrevistas',True);vs=refs(x.get('evidencias'),set(ev),ident+'.evidencias',True);backed={ev[v]['entrevista'] for v in vs if v in ev and ev[v]['tipo']=='CANONICA'}
  if not set(es)<=backed:err(ident,'Cada caso exige evidencia participante propia.')
  refs(x.get('actores'),acts,ident+'.actores',True);refs(x.get('necesidades'),set(needs),ident+'.necesidades',True)
  return es
 for ident,x in profiles.items():
  es=sourcecheck(x,ident);allcases.update(es)
  for k in ['nombre','descripcion','patron','contraejemplo_y_limite']:txt(x.get(k),ident+'.'+k)
  for k in ['capacidades','restricciones']:
   for v in arr(x.get(k),ident+'.'+k,True):txt(v,ident+'.'+k)
  if x.get('tipo') not in {'PERFIL_FUNCIONAL','ARQUETIPO_CANDIDATO'}:err(ident,'Tipo de perfil inválido.')
  if x.get('tipo')=='ARQUETIPO_CANDIDATO' and len(es)<2:err(ident,'Arquetipo candidato requiere al menos dos casos.')
 if allcases!=cases:err('perfiles_analiticos','Cubrir las cinco voces.')
 for ident,x in stories.items():
  sourcecheck(x,ident)
  for k in ['titulo','formulacion','contexto','objetivo','beneficio_o_decision','limites']:txt(x.get(k),ident+'.'+k)
  if x.get('perfil') is not None and x.get('perfil') not in profiles:err(ident,'Perfil desconocido.')
  if 'perfil' not in x:err(ident,'Perfil requerido; null si no aplica.')
  if x.get('tipo') not in {'ACTUAL_A_PRESERVAR','IDEAL_A_CONTRASTAR','CONDICIONAL'}:err(ident,'Modalidad de historia inválida.')
  for k in ['restricciones','preservar']:
   for y in arr(x.get(k),ident+'.'+k):txt(y,ident+'.'+k)
  for y in arr(x.get('criterios'),ident+'.criterios',True):
   kid=y.get('id')
   if not isinstance(kid,str) or not re.fullmatch(r'HU01-K\d{3,}',kid) or kid in kidset:err(ident,'Id de criterio inválido/repetido.')
   kidset.add(kid)
   for k in ['dado','cuando','entonces','limites']:txt(y.get(k),str(kid)+'.'+k)
   if y.get('origen') not in {'PROPUESTA_ANALITICA','ADAPTADO_DE_CRITERIO_N01'} or y.get('estado')!='PROPUESTO_NO_EJECUTADO':err(str(kid),'Origen/estado inválido; no afirmar prueba o aceptación.')
   refs(y.get('criterios_n01'),nk,str(kid)+'.criterios_n01',y.get('origen')=='ADAPTADO_DE_CRITERIO_N01')
  pr=x.get('prioridad',{})
  for k in ['ambito','razon','limites']:txt(pr.get(k),ident+'.prioridad.'+k)
  if pr.get('nivel') not in {'ALTA','MEDIA','BAJA','PENDIENTE'} or pr.get('origen')!='ANALISIS_CONDICIONAL':err(ident,'Prioridad inválida.')
  if x.get('perfil_metadatos') not in mds:err(ident,'Perfil de metadatos desconocido.')
  for y in arr(x.get('metaalgoritmo'),ident+'.metaalgoritmo',True):
   oid=y.get('id')
   if not isinstance(oid,str) or not re.fullmatch(r'HU01-OP\d{3,}',oid) or oid in opset:err(ident,'Id de operación inválido/repetido.')
   opset.add(oid)
   for k in ['nombre','entrada','operacion','salida','precondicion','limite']:txt(y.get(k),str(oid)+'.'+k)
   if y.get('intervencion') not in {'HUMANA','AUTOMATIZABLE_POR_VALIDAR','MIXTA_POR_VALIDAR'}:err(str(oid),'Intervención inválida.')
 for ident,x in mds.items():
  for k in ['nombre','descripcion']:txt(x.get(k),ident+'.'+k)
  hs=refs(x.get('historias'),set(stories),ident+'.historias',True);fields=[]
  for y in arr(x.get('campos'),ident+'.campos',True):
   name=y.get('campo');fields.append(name);txt(y.get('justificacion'),ident+'.'+str(name)+'.justificacion');vs=refs(y.get('evidencias'),set(ev),ident+'.campo.evidencias',y.get('estado')=='RESPALDADO')
   if y.get('estado') not in {'RESPALDADO','PROPUESTO','DESCONOCIDO','NO_APLICA'}:err(ident,'Estado de campo inválido.')
   if 'valor' not in y or (y.get('estado') in {'DESCONOCIDO','NO_APLICA'} and y.get('valor') is not None):err(ident,'Desconocido/no aplicable: valor null con razón.')
  if sorted(str(y) for y in fields)!=sorted(CAMPOS):err(ident,'Cubrir los 21 campos exactamente una vez.')
  for hid in hs:
   if hid in stories and stories[hid].get('perfil_metadatos')!=ident:err(ident,'Relación inversa de metadatos inconsistente.')
 coverage=[];linked=set()
 for x in arr(r.get('cobertura_necesidades'),'cobertura_necesidades',True):
  nid=x.get('necesidad');coverage.append(nid);hs=refs(x.get('historias'),set(stories),'cobertura_necesidades.historias');txt(x.get('razon'),'cobertura_necesidades.razon')
  if x.get('tratamiento') not in {'DESARROLLADA','INTEGRADA_CON_OTRA','CONSERVADA_COMO_CONDICION','FUERA_DE_ALCANCE_DE_PRODUCTO','PENDIENTE_DE_VALIDACION'}:err(str(nid),'Tratamiento inválido.')
  if x.get('tratamiento') in {'DESARROLLADA','INTEGRADA_CON_OTRA'} and not hs:err(str(nid),'Se requiere historia de destino.')
  for hid in hs:
   if hid in stories and nid not in stories[hid].get('necesidades',[]):err(str(nid),'La historia no incluye la necesidad.')
 for hid,x in stories.items():linked.update(x.get('necesidades',[]))
 if sorted(str(x) for x in coverage)!=sorted(needs):err('cobertura_necesidades','Cubrir las 29 necesidades exactamente una vez.')
 ideals={x['id'] for x in needs.values() if x['tipo']=='DESEO_IDEAL'}
 if not ideals<=linked:err('historias','Dar desarrollo explícito a los seis deseos ideales.')
 local=r.get('perfil_objeto_local',{})
 for k in ['nombre','version','limites']:txt(local.get(k),'perfil_objeto_local.'+k)
 arr(local.get('campos'),'perfil_objeto_local.campos',True)
 if local.get('estado')!='PROPUESTA_LOCAL_NO_REGISTRADA':err('perfil_objeto_local','No declarar registro externo.')
 objs=idx(r.get('objetos_digitales'),'HU01-OD','objetos_digitales',True);entities={**needs,**profiles,**stories,**mds};types={**{k:'NECESIDAD' for k in needs},**{k:'PERFIL_ANALITICO' for k in profiles},**{k:'HISTORIA' for k in stories},**{k:'PERFIL_METADATOS' for k in mds}};seen=[];paths=[];fileschecked=0
 for ident,x in objs.items():
  ent=x.get('entidad');seen.append(ent)
  for k in ['titulo','descripcion']:txt(x.get(k),ident+'.'+k)
  if ent not in entities or x.get('tipo')!=types.get(ent):err(ident,'Entidad/tipo inexistente o incorrecto.')
  if x.get('version')!=('1.1' if ent in needs or ent in mds else '1.0') or x.get('estado')!='PROTOTIPO_LOCAL_NO_REGISTRADO':err(ident,'Versión/estado de objeto inválidos.')
  for k in ['pid_externo','tipo_registrado_externo','perfil_registrado_externo']:
   if k not in x or x[k] is not None:err(ident,'Mantener '+k+' null; no hay registro externo autorizado.')
  path=x.get('ruta_payload');safe=isinstance(path,str) and path and not Path(path).is_absolute() and '..' not in Path(path).parts
  if not safe:err(ident,'Ruta relativa segura requerida.')
  else:paths.append(path)
  if not isinstance(x.get('sha256'),str) or not re.fullmatch('[0-9a-f]{64}',x['sha256']):err(ident,'SHA-256 requerido.')
  for k in ['actividad','revision']:txt(x.get('procedencia',{}).get(k),ident+'.procedencia.'+k)
  refs(x.get('procedencia',{}).get('fuentes'),set(entities)|set(ev),ident+'.procedencia.fuentes',True)
  acc=x.get('acceso',{})
  for k in ['condicion','fundamento']:txt(acc.get(k),ident+'.acceso.'+k)
  if acc.get('autorizacion_publicacion')!='NO_CONSTA':err(ident,'No hay autorización de publicación aportada.')
  lic=x.get('licencia',{});txt(lic.get('fundamento'),ident+'.licencia.fundamento')
  if 'valor' not in lic:err(ident,'Licencia valor: null si no consta.')
  if lic.get('valor') is not None:warnings.append({'ruta':ident+'.licencia','mensaje':'Revisar evidencia de licencia de este artefacto, sin extender licencia ajena.'})
  for y in arr(x.get('relaciones'),ident+'.relaciones'):
   if y.get('tipo') not in {'DERIVA_DE','DESCRITO_POR','REPRESENTA','RELACIONADO_CON'} or y.get('destino_entidad') not in set(entities)|set(ev):err(ident,'Relación de procedencia inválida.')
  if soportes and safe:
   f=Path(soportes)/path
   if not f.is_file():err(ident,'Payload no encontrado.')
   else:
    fileschecked+=1
    if hashlib.sha256(f.read_bytes()).hexdigest()!=x.get('sha256'):err(ident,'SHA-256 no coincide con bytes.')
    if ent in entities and json.loads(f.read_text())!=entities[ent]:err(ident,'Payload no coincide con entidad fuente.')
 if sorted(str(x) for x in seen)!=sorted(entities):err('objetos_digitales','Un objeto por necesidad/perfil/historia/metadatos, sin duplicados.')
 if len(paths)!=len(set(paths)):err('objetos_digitales','Rutas de payload repetidas.')
 if not soportes:warnings.append({'ruta':'objetos_digitales','mensaje':'Falta --soportes: payloads y huellas aún no cotejados; repetir para entrega final.'})
 ff=[]
 for x in arr(r.get('estado_fair'),'estado_fair',True):
  ff.append(x.get('principio'))
  for k in ['evidencia_local','pendiente','limites']:txt(x.get(k),'estado_fair.'+k)
  if x.get('estado') not in {'PARCIAL','PENDIENTE','ATENDIDO_LOCALMENTE'}:err('estado_fair','Estado inválido.')
  if x.get('principio') in {'F1','F4'} and x.get('estado')=='ATENDIDO_LOCALMENTE':err('estado_fair','Id local/ZIP no acredita persistencia global o indización externa.')
 if sorted(str(x) for x in ff)!=sorted(FAIR):err('estado_fair','Cubrir los 15 principios exactamente una vez.')
 pack=[]
 for x in arr(r.get('evaluacion_empaquetado'),'evaluacion_empaquetado',True):
  pack.append(x.get('opcion'))
  for k in ['utilidad','dependencias','limites']:txt(x.get(k),'evaluacion_empaquetado.'+k)
  if x.get('estado') not in {'USO_PROPUESTO','NO_IMPLEMENTADO','NO_PERTINENTE_CON_RAZON'}:err('evaluacion_empaquetado','Estado inválido.')
 if sorted(str(x) for x in pack)!=sorted(['RO_CRATE','DATACITE','PROV','NANOPUBLICACIONES']):err('evaluacion_empaquetado','Evaluar cuatro opciones una vez.')
 for x in arr(r.get('agenda_validacion'),'agenda_validacion',True):
  if 'objeto' not in x or (x['objeto'] is not None and x['objeto'] not in entities):err('agenda_validacion','Objeto inexistente.')
  for k in ['pendiente','comprobacion']:txt(x.get(k),'agenda_validacion.'+k)
 for x in arr(r.get('limites'),'limites',True):
  for k in ['descripcion','consecuencia']:txt(x.get(k),'limites.'+k)
 return {'validador':'Historias HU01 revisadas 1.1','estado':'SIN_ERRORES_ESTRUCTURALES' if not errors else 'ERROR','errores':errors,'advertencias':warnings,'conteos':{'perfiles':len(profiles),'historias':len(stories),'perfiles_metadatos':len(mds),'criterios':len(kidset),'pasos_propuestos':len(opset),'necesidades_cubiertas':len(coverage),'objetos_digitales':len(objs),'payloads_comprobados':fileschecked},'alcance':'Control técnico local. No certifica interpretación, aceptación, metadatos adecuados, utilidad, PID externo, FAIR/FDO integral, fuentes web, figuras o revisión humana.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('base');ap.add_argument('resultado');ap.add_argument('--soportes');ap.add_argument('--salida',required=True);a=ap.parse_args();f=Path(a.resultado)
 try:out=validar(a.base,json.loads(f.read_text()),a.soportes)
 except (ValueError,TypeError,KeyError,AttributeError,OSError) as ex:out={'validador':'Historias HU01 revisadas 1.1','estado':'ERROR','errores':[{'ruta':'$','mensaje':'Control incompleto: '+str(ex)}],'advertencias':[]}
 out['ejecucion']={'estado':'EJECUTADO','fecha_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'comando_argumentos':sys.argv,'sha256_resultado_evaluado':hashlib.sha256(f.read_bytes()).hexdigest() if f.exists() else None,'sha256_validador':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'codigo_salida':0 if not out['errores'] else 1};Path(a.salida).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'estado':out['estado'],'errores':len(out['errores']),'salida':a.salida},ensure_ascii=False));sys.exit(out['ejecucion']['codigo_salida'])
