from pathlib import Path
import json,re,argparse,hashlib,datetime
LENTES={'SCAN','POTENCIA_ESCALAMIENTO','TDA','ABM'}
FAMILIAS={'ADMINISTRATIVA','REJILLA_HEXAGONOS','NATURAL','TENENCIA_CONCESION','COMUNITARIA','REDES','INFLUENCIA','REFERENCIA'}
PRACTICAS={'INCERTIDUMBRE_DENOMINADORES','COMPARAR_UNIDADES','ESCENARIOS_METODOLOGICOS','EXCLUSIONES'}
ROLES={'EXTRACCION','UNIFICACION','AGREGACION','CONSTRUCCION','ANALISIS','PRODUCTOS'}
REPS={'PUNTOS','LINEAS','POLIGONOS','RASTER','REDES','TEXTO_TABLAS','MUESTRAS_FISICAS','TRES_DIMENSIONES'}
COMMIT='ab60b86a6a87bca0dd370c7c4af3ada4185d187e'
def validar(base,r):
 errors=[];warnings=[];ids={}
 def err(path,msg):errors.append({'ruta':path,'mensaje':msg})
 def text(x,path):
  if not isinstance(x,str)or not x.strip():err(path,'Texto explicativo requerido.')
 def req(x,keys,path):
  if not isinstance(x,dict):err(path,'Objeto requerido.');return
  for k in keys:
   if k not in x:err(path+'.'+k,'Campo requerido.')
   elif x[k]is None or x[k]=='' or x[k]==[]:err(path+'.'+k,'Contenido requerido.')
 def arr(x,path,minn=0):
  if not isinstance(x,list):err(path,'Lista requerida.');return []
  if len(x)<minn:err(path,'Lista incompleta.')
  return x
 def index(rows,prefix,path):
  out={}
  for i,x in enumerate(arr(rows,path,1)):
   if not isinstance(x,dict):err(path,'Elemento no objeto.');continue
   k=x.get('id','')
   if not re.fullmatch(prefix+r'\d{3}',str(k))or k in ids:err(path+'['+str(i)+'].id','Id inválido o duplicado.')
   else:ids[k]=x;out[k]=x
  return out
 def refs(v,allowed,path,minn=0):
  for i,k in enumerate(arr(v,path,minn)):
   if not isinstance(k,str)or k not in allowed:err(path+'['+str(i)+']','Referencia no existente.')
 def enumeration(rows,key,values,path):
  actual=[x.get(key)for x in rows];
  if len(actual)!=len(values)or set(actual)!=values:err(path,'Cobertura enumerada exacta requerida.')
 hu=json.loads((base/'historias_revisadas.json').read_text());n=json.loads((base/'necesidades_revisadas.json').read_text());a=json.loads((base/'actores_revisados.json').read_text());rq=json.loads((base/'requisitos_T01.json').read_text());story={x['id']:x for x in hu['historias']};needs={x['id']for x in n['necesidades']};actors={x['id']for x in a['actores']}
 meta=r.get('metadatos',{});req(meta,['tarea','resultado_version','estado','historias_version','necesidades_version','libro_version','tipo_revision','revision_humana_independiente','implementacion','fuente_modelo'],'metadatos')
 for k,v in {'tarea':'T01','resultado_version':'1.1','estado':'DISENO_REVISADO_EN_COORDINACION','historias_version':'1.1','necesidades_version':'1.1','libro_version':'1.3','tipo_revision':'ASISTIDA_POR_LLM','revision_humana_independiente':'PENDIENTE','implementacion':'NO_EJECUTADA'}.items():
  if meta.get(k)!=v:err('metadatos.'+k,'Versión o estado inválido.')
 for k in ['lectura_entradas','decisiones_metodologicas','agenda_validacion','limites']:arr(r.get(k),k,1)
 src=index(r.get('fuentes'),'T01-F','fuentes');claims=index(r.get('afirmaciones_tecnicas'),'T01-A','afirmaciones_tecnicas');critical=index(r.get('fundamentos_criticos'),'T01-G','fundamentos_criticos');units=index(r.get('alternativas_agregacion'),'T01-U','alternativas_agregacion');practices=index(r.get('practicas_diseno'),'T01-V','practicas_diseno');lenses=index(r.get('lentes'),'T01-L','lentes');tools=index(r.get('herramientas'),'T01-B','herramientas');products=index(r.get('productos'),'T01-P','productos')
 ar=r.get('arquitectura',{});req(ar,['adaptacion_geoinsights','modulos','conexiones','contratos','representaciones','google_earth_engine'],'arquitectura');modules=index(ar.get('modulos'),'T01-M','arquitectura.modulos');contracts=index(ar.get('contratos'),'T01-C','arquitectura.contratos')
 if len(products)not in [2,3]:err('productos','Se requieren dos o tres productos.')
 for x in src.values():
  req(x,['titulo','emisor','url','consulta','localizador','lectura_efectiva','tipo','estado','limites'],x['id'])
  if x.get('tipo')not in ['PRIMARIA','REFERENCIA_METODOLOGICA']or x.get('estado')not in ['VERIFICADA','NO_RECUPERADA']:err(x['id'],'Tipo/estado de fuente inválidos.')
  if not re.match(r'https?://',str(x.get('url',''))):err(x['id']+'.url','URL de fuente requerida.')
 def sources(x,minn=1,primary=False):
  refs(x.get('fuentes'),src,x['id']+'.fuentes',minn)
  for k in x.get('fuentes',[]):
   if k in src and (src[k].get('estado')!='VERIFICADA'or(primary and src[k].get('tipo')!='PRIMARIA')):err(x['id']+'.fuentes','La afirmación requiere fuente primaria verificada.')
 for x in claims.values():req(x,['afirmacion','fuentes','localizadores','alcance','aplicacion_local','limites'],x['id']);sources(x,primary=True)
 for x in critical.values():req(x,['concepto','argumento','fuentes','consecuencia_diseno','limites'],x['id']);sources(x);refs(x.get('historias'),story,x['id']+'.historias')
 enumeration(list(units.values()),'familia',FAMILIAS,'alternativas_agregacion')
 for x in units.values():req(x,['pregunta','denominador','proceso_generador','jurisdiccion','parametros','estabilidad_temporal','autoria_limites','exclusiones','decision','fuentes','limites'],x['id']);sources(x);refs(x.get('productos'),products,x['id']+'.productos')
 enumeration(list(practices.values()),'practica',PRACTICAS,'practicas_diseno')
 for x in practices.values():req(x,['accion_visible','insumos','comprobacion_propuesta','limites'],x['id']);refs(x.get('productos'),products,x['id']+'.productos')
 enumeration(list(lenses.values()),'lente',LENTES,'lentes')
 for x in lenses.values():
  req(x,['pregunta','datos_requeridos','supuestos','parametros','salida_interpretable','sensibilidad','validacion_futura','estado','reconsideracion','herramientas','fuentes','limites'],x['id']);sources(x,primary=True);refs(x.get('historias'),story,x['id']+'.historias');refs(x.get('productos'),products,x['id']+'.productos');refs(x.get('herramientas'),tools,x['id']+'.herramientas',1)
  if x.get('estado')not in ['CONDICIONAL','NO_PERTINENTE_EN_PRODUCTOS_ACTUALES']:err(x['id']+'.estado','No se declara ejecución de lente.')
  if not any(k in tools and tools[k].get('lente')==x.get('lente')for k in x.get('herramientas',[])):err(x['id'],'Falta candidata del lente correspondiente.')
 for x in tools.values():
  req(x,['nombre','lente','lenguaje','funcion','requisitos','compatibilidad','fuentes','limites'],x['id']);sources(x,primary=True)
  if x.get('lente')not in LENTES or x.get('compatibilidad')!='COMPATIBILIDAD_NO_PROBADA':err(x['id'],'Lente o compatibilidad inválidos.')
 if ar.get('adaptacion_geoinsights',{}).get('commit')!=COMMIT:err('arquitectura.adaptacion_geoinsights.commit','No coincide snapshot de entrada.')
 req(ar.get('adaptacion_geoinsights'),['atribucion','licencia','archivos_examinados','se_retoma','se_modifica','no_se_transfiere','limites'],'arquitectura.adaptacion_geoinsights')
 if {x.get('responsabilidad')for x in modules.values()}!=ROLES:err('arquitectura.modulos','Faltan responsabilidades o hay roles ajenos.')
 for x in modules.values():req(x,['nombre','funcion','control_calidad','faltantes','procedencia','versionado','retorno','limites'],x['id']);refs(x.get('entradas'),contracts,x['id']+'.entradas',1);refs(x.get('salidas'),contracts,x['id']+'.salidas',1)
 for x in arr(ar.get('conexiones'),'conexiones',1):
  if x.get('desde')not in modules or x.get('hacia')not in modules or x.get('tipo')not in ['FLUJO','RETORNO']:err('conexiones','Módulo o tipo inexistente.')
  req(x,['objeto','condicion','limites'],'conexion')
 for x in contracts.values():
  req(x,['nombre','proposito','campos','controles','procedencia_versiones','limites'],x['id'])
  for c in arr(x.get('campos'),x['id']+'.campos',1):
   req(c,['nombre','tipo','significado','origen'],x['id']+'.campo')
   if 'unidad'not in c or not isinstance(c.get('nullable'),bool):err(x['id']+'.campo','Unidad y nullable explícitos requeridos.')
 enumeration(arr(ar.get('representaciones'),'representaciones'),'tipo',REPS,'representaciones')
 for x in ar.get('representaciones',[]):
  req(x,['adaptacion','limites'],'representacion');refs(x.get('productos'),products,'representacion.productos')
  if x.get('estado')not in ['CONSIDERADA','NO_NECESARIA_EN_PRODUCTOS_ACTUALES']:err('representacion.estado','Estado inválido.')
 gee=ar.get('google_earth_engine',{});req(gee,['decision','finalidad','dependencias','limites'],'google_earth_engine');refs(gee.get('productos'),products,'google_earth_engine.productos');refs(gee.get('fuentes'),src,'google_earth_engine.fuentes')
 for x in products.values():
  req(x,['nombre','funcion','usuarios','historias','necesidades','decision','argumento','alcance','exclusiones','datos','operaciones','modulos','salida_e_interaccion','actividad_humana','responsables_pendientes','incertidumbres','cargas_y_beneficios','criterios','condicion_descarte','limites'],x['id'])
  if x.get('origen')!='OPORTUNIDAD_PROPUESTA'or x.get('estado')!='PROPUESTA_NO_IMPLEMENTADA':err(x['id'],'Producto debe ser propuesta no implementada.')
  refs(x.get('usuarios'),actors,x['id']+'.usuarios',1);refs(x.get('historias'),story,x['id']+'.historias',1);refs(x.get('necesidades'),needs,x['id']+'.necesidades',1);refs(x.get('modulos'),modules,x['id']+'.modulos',1)
  if any(n not in {n for h in x.get('historias',[])if h in story for n in story[h]['necesidades']} for n in x.get('necesidades',[])):err(x['id'],'Necesidad no vinculada por historias del producto.')
  for da in index(x.get('datos'),'T01-D',x['id']+'.datos').values():
   req(da,['variable','acceso','licencia','resolucion_requerida','limites'],da['id'])
   if da.get('estado')not in ['CANDIDATO_DOCUMENTADO','REQUERIDO_NO_DISPONIBLE']:err(da['id'],'Estado de datos inválido.')
   source=da.get('fuente')
   if source is not None and source not in src:err(da['id'],'Fuente de dato inexistente.')
   if da.get('estado')=='CANDIDATO_DOCUMENTADO'and(source not in src or src[source].get('estado')!='VERIFICADA'):err(da['id'],'Candidato documentado requiere fuente consultada.')
  for k in index(x.get('criterios'),'T01-K',x['id']+'.criterios').values():
   req(k,['dado','cuando','entonces','metodo','limites'],k['id'])
   if k.get('estado')!='PROPUESTO_NO_EJECUTADO':err(k['id'],'No se declara comprobación de producto ejecutada.')
 cov=arr(r.get('cobertura_historias'),'cobertura_historias');hc=[x.get('historia')for x in cov]
 if len(hc)!=len(story)or set(hc)!=set(story):err('cobertura_historias','Se requieren exactamente las 21 historias.')
 for x in cov:
  text(x.get('razon'),'cobertura_historias.razon');refs(x.get('productos'),products,'cobertura_historias.productos')
  if x.get('disposicion')not in ['VINCULADA_A_PRODUCTO','PRACTICA_A_PRESERVAR','FUERA_DE_ALCANCE_CON_RAZON','PENDIENTE_DE_VALIDACION']:err('cobertura_historias','Disposición inválida.')
  declared={p['id']for p in products.values()if x.get('historia')in p.get('historias',[])}
  if set(x.get('productos',[]))!=declared:err('cobertura_historias','Cobertura inversa no coincide.')
  if x.get('disposicion')=='VINCULADA_A_PRODUCTO'and not declared:err('cobertura_historias','Vínculo a producto vacío.')
 req(r.get('seleccion_portafolio'),['criterios','argumento','comparacion_condicional','pendientes'],'seleccion_portafolio');req(r.get('extension_fair_janus'),['medidas','objetos_afectados','controles_propuestos','estados_pendientes','limites'],'extension_fair_janus')
 cr=arr(r.get('cobertura_requisitos'),'cobertura_requisitos');want={x['id']for x in rq};actual=[x.get('requisito')for x in cr]
 if len(actual)!=39 or set(actual)!=want:err('cobertura_requisitos','Se requieren exactamente los 39 requisitos GCR/LEN/DAT.')
 for x in cr:
  text(x.get('razon'),'cobertura_requisitos.razon');refs(x.get('objetos'),ids,'cobertura_requisitos.objetos')
  if x.get('estado')not in ['DESARROLLADO_EN_DISENO','PENDIENTE_CON_RAZON','NO_APLICA_CON_RAZON']:err('cobertura_requisitos','Estado inválido.')
  if x.get('estado')=='DESARROLLADO_EN_DISENO'and not x.get('objetos'):err('cobertura_requisitos','Requiere objeto de diseño existente.')
 return {'validador':'T01 revisado 1.1','estado':'SIN_ERRORES_ESTRUCTURALES'if not errors else 'ERROR','errores':errors,'advertencias':warnings,'conteos':{'fuentes':len(src),'afirmaciones_tecnicas':len(claims),'fundamentos':len(critical),'familias_agregacion':len(units),'practicas':len(practices),'lentes':len(lenses),'herramientas':len(tools),'modulos':len(modules),'contratos':len(contracts),'productos':len(products),'historias_cubiertas':len(hc),'requisitos_cubiertos':len(cr)},'alcance':'Control estructural y referencial. No certifica lectura externa, corrección técnica, adecuación semántica de contratos, fidelidad, utilidad, adopción, implementación, figuras, FAIR/FDO o revisión humana independiente.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('base');ap.add_argument('resultado');ap.add_argument('--salida');a=ap.parse_args();f=Path(a.resultado)
 try:out=validar(Path(a.base),json.loads(f.read_text()))
 except(ValueError,KeyError,TypeError,AttributeError,OSError)as e:out={'validador':'T01 revisado 1.1','estado':'ERROR','errores':[{'ruta':'$','mensaje':'Control incompleto: '+str(e)}],'advertencias':[]}
 out['ejecucion']={'fecha_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argumentos':__import__('sys').argv,'sha256_resultado':hashlib.sha256(f.read_bytes()).hexdigest(),'sha256_validador':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 if a.salida:Path(a.salida).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'estado':out['estado'],'errores':len(out['errores'])},ensure_ascii=False));raise SystemExit(bool(out['errores']))
