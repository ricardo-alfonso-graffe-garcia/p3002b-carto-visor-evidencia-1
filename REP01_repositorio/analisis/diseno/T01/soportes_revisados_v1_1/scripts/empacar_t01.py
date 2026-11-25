"""Exportación y comprobaciones documentales reales. No implementa productos."""
from pathlib import Path
import json,csv,hashlib,zipfile,shutil,subprocess,datetime,re,sys,os
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'insumos/T01_insumos_v1'; OUT=ROOT/'entrega'; SUP=OUT/'T01_soportes_v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,o):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def text(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
def read(p):return json.loads(p.read_text())
R=read(OUT/'T01_diseno_v1.json');H=read(BASE/'historias_revisadas.json');N=read(BASE/'necesidades_revisadas.json')
for folder in ['tablas','matrices','fuentes','esquemas','desarrollo','registro','controles','diagramas','scripts']: (SUP/folder).mkdir(parents=True,exist_ok=True)
checks=[]
def check(name,ok,details):
 checks.append(dict(control=name,estado='CONFORME' if ok else 'INCIDENCIA',detalle=details))
 if not ok:print('INCIDENCIA:',name,details)
# Integridad y referencias de fuentes de entrada.
manifest=read(BASE/'manifest.json');rows=[]
for a in manifest['archivos']:
 p=BASE/a['ruta']; b=p.read_bytes();rows.append(dict(ruta=a['ruta'],bytes=len(b),sha256=sha(p),coincide=len(b)==a['bytes'] and sha(p)==a['sha256'],tipo='PAQUETE_ENTRADA',incluido_en_salida=False))
check('manifest_entrada',all(x['coincide'] for x in rows),dict(archivos=len(rows),errores=[x['ruta'] for x in rows if not x['coincide']]))
reg=read(BASE/'registro_entradas.json');pref=[dict(archivo=a['archivo'],coincide=sha(BASE/a['archivo'])==a['sha256']) for a in reg['preferidas']]
check('preferidas',all(a['coincide'] for a in pref),pref)
check('instrucciones_identicas',(ROOT/'upload/90_instrucciones_T01(1).md').read_bytes()==(BASE/'instrucciones_T01.md').read_bytes(),'Cotejo byte a byte del adjunto con la copia del paquete.')
# Seguridad de ZIP leído: rutas relativas sin symlinks; CRC y procedencia.
zchecks=[]
for p in [ROOT/'upload/91_insumos_T01(1).zip',BASE/'referencia_geoinsights/GeoInsights_snapshot.zip']:
 with zipfile.ZipFile(p) as z:
  bad=[a.filename for a in z.infolist() if Path(a.filename).is_absolute() or '..' in Path(a.filename).parts or (a.external_attr>>16)&0o170000==0o120000]
  zchecks.append(dict(archivo=p.name,entradas=len(z.infolist()),sha256=sha(p),rutas_inseguras=bad,crc_error=z.testzip()))
check('zip_entrada_seguro_crc',all(not x['rutas_inseguras'] and x['crc_error'] is None for x in zchecks),zchecks)
geo=read(BASE/'referencia_geoinsights/procedencia_snapshot.json')
check('procedencia_snapshot',geo['sha256_zip']==sha(BASE/'referencia_geoinsights/GeoInsights_snapshot.zip') and geo['commit']==R['arquitectura']['adaptacion_geoinsights']['commit'],dict(commit=geo['commit'],bytes=(BASE/'referencia_geoinsights/GeoInsights_snapshot.zip').stat().st_size))
save(SUP/'controles/integridad_entradas.json',dict(manifest=rows,preferidas=pref,zip=zchecks,alcance='Integridad byte a byte y lectura segura; no verdad, calidad o auditoría de seguridad del contenido.'))
# Referencias de originales que no se redistribuyen.
inventory=[dict(tipo='PAQUETE_ENTRADA',ruta='T01_insumos_v1/manifest.json',sha256=sha(BASE/'manifest.json'),bytes=(BASE/'manifest.json').stat().st_size,incluido_en_salida=False)]+[{k:v for k,v in x.items() if k!='coincide'} for x in rows]
save(SUP/'fuentes/entradas_referenciadas.json',inventory)
# Cotejo mecánico de citas canónicas; no implica lectura completa o revisión interpretativa.
corpora={e:read(BASE/f'corpus/{e}_corpus_analisis_v1.json') for e in ['E01','E02','E03','E04','E05']}
pars={x['id']:x for c in corpora.values() for x in c['parrafos']}
ev={x['id']:x for x in N['evidencias']}; quotes=[]; skipped=[]
for x in N['evidencias']:
 if x.get('tipo')!='CANONICA': skipped.append(dict(id=x['id'],tipo=x.get('tipo'),razon='No cita canónica de párrafo; referencia documental no comprobada aquí como testimonio.'));continue
 p=pars.get(x.get('referencia'));start=x.get('inicio');end=x.get('fin');q=x.get('cita','')
 good=p is not None and p['texto'][start:end]==q and p.get('voz')==x.get('voz') and p.get('turno')==x.get('turno_id')
 quotes.append(dict(id=x['id'],referencia=x['referencia'],coincide=good))
check('citas_canonicas_n01',all(q['coincide'] for q in quotes),dict(cotejadas=len(quotes),incidencias=[q for q in quotes if not q['coincide']],otras_referencias=skipped))
illustrations=[]
for x in H['citas_ilustrativas']:
 v=ev[x['referencia']];p=pars[v['referencia']];i=corpora[v['entrevista']]['parrafos'].index(p)
 good=x['cita'] in p['texto'] and p['voz']=='Participante'
 illustrations.append(dict(cita=x['cita'],evidencia=x['referencia'],parrafo=p['id'],voz=p['voz'],coincide=good,contexto_pregunta=v.get('contexto_pregunta'),nota_contextual=x['uso']))
check('cinco_citas_explicacion',all(q['coincide'] and q['cita'] in (OUT/'T01_explicacion_v1.md').read_text() for q in illustrations),illustrations)
save(SUP/'controles/cotejo_citas.json',dict(canonicas=quotes,referencias_no_testimoniales=skipped,ilustrativas=illustrations,limite='Coincidencia textual/voz/turno, no revisión independiente de la interpretación.'))
# Registro exacto de consulta humana asistida realizada en esta tarea.
sel=read(ROOT/'seleccion_parrafos.json');sel['E03']=sorted(set(sel['E03']+list(range(28,90))))
for e,nums in {'E01':[156,157,158],'E02':[147,148,149],'E03':[181,182,183],'E04':[151,152,153],'E05':[172,173,174]}.items():sel[e]=sorted(set(sel[e]+nums))
consult=[dict(entrevista=e,archivo=f'PAQUETE_ENTRADA:T01_insumos_v1/corpus/{e}_corpus_analisis_v1.json',parrafos=[f'{e}-P{i:03}' for i in nums],alcance='Lectura dirigida de estos párrafos con preguntas/correcciones para argumentar; no transcripción completa.',sha256=sha(BASE/f'corpus/{e}_corpus_analisis_v1.json')) for e,nums in sel.items()]
save(SUP/'fuentes/consulta_corpus.json',consult)
save(SUP/'fuentes/citas_utilizadas.json',illustrations)
save(SUP/'fuentes/registro_fuentes.json',R['fuentes'])
text(SUP/'fuentes/bibliografia.md','# Fuentes consultadas y alcance real\n\nConsulta: 25 de noviembre de 2026. Las rutas del código refieren al snapshot dentro del paquete de entrada, no a archivos redistribuidos aquí.\n\n'+'\n\n'.join(f"## {x['id']} · {x['titulo']}\n\n{x['emisor']}. Versión: {x['version'] or 'no consta'}. [Fuente]({x['url']}). Estado: **{x['estado']}**.\n\nLocalizador: {x['localizador']}\n\nLectura: {x['lectura_efectiva']}\n\nLímites: {x['limites']}"+(f"\n\nPAQUETE_ENTRADA: `referencia_geoinsights/GeoInsights_snapshot.zip!/{x['archivo_snapshot']}`; SHA-256 del archivo: `{x['sha256_archivo_snapshot']}`." if x.get('archivo_snapshot') else '') for x in R['fuentes']))
# No se copia código del snapshot. Se conserva licencia como atribución documental.
shutil.copyfile(BASE/'referencia_geoinsights/LICENSE',SUP/'fuentes/LICENSE_GeoInsights')
# Tablas completas, sin recortes de texto ni de objetos anidados.
tablechecks=[]
def cell(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def table(name,items,folder='tablas'):
 if not items:return
 keys=list(dict.fromkeys(k for r in items for k in r))
 p=SUP/folder/(name+'.csv')
 with p.open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=keys);wr.writeheader();wr.writerows({k:cell(x.get(k)) for k in keys} for x in items)
 with p.open(newline='') as f:back=[{k:json.loads(v) for k,v in row.items()} for row in csv.DictReader(f)]
 expected=[{k:x.get(k) for k in keys} for x in items]
 tablechecks.append(dict(archivo=str(p.relative_to(SUP)),filas=len(items),columnas=len(keys),igualdad_celda_a_celda=back==expected,sha256=sha(p)))
for k,v in R.items():
 if isinstance(v,list) and v and all(isinstance(x,dict) for x in v):table(k,v)
for k,v in R['arquitectura'].items():
 if isinstance(v,list):table('arquitectura_'+k,v)
table('datos_productos',[dict(producto=p['id'],**d) for p in R['productos'] for d in p['datos']])
table('criterios_productos',[dict(producto=p['id'],**c) for p in R['productos'] for c in p['criterios']])
table('trazabilidad_productos',[dict(producto=p['id'],**t) for p in R['productos'] for t in p['trazabilidad_argumental']])
table('campos_contratos',[dict(contrato=c['id'],**f) for c in R['arquitectura']['contratos'] for f in c['campos']])
coverage=[dict(**x,titulo=next(h['titulo'] for h in H['historias'] if h['id']==x['historia']),tipo_origen=next(h['tipo'] for h in H['historias'] if h['id']==x['historia']),restricciones_origen=next(h['restricciones'] for h in H['historias'] if h['id']==x['historia'])) for x in R['cobertura_historias']]
table('historias_21',coverage,'matrices')
qmap={q['id']:q for q in read(BASE/'requisitos_T01.json')}
table('requisitos_39',[dict(**q,requisito_texto=qmap[q['requisito']]['requisito'],comprobacion_encargo=qmap[q['requisito']]['comprobacion']) for q in R['cobertura_requisitos']],'matrices')
check('tablas_derivadas',all(t['igualdad_celda_a_celda'] for t in tablechecks),dict(tablas=len(tablechecks),filas=sum(t['filas'] for t in tablechecks)))
save(SUP/'controles/cotejo_tablas.json',tablechecks)
# Desarrollo legible completo de los objetos, además de CSV/JSON.
def mdvalue(v,level=0):
 if isinstance(v,str):return v
 if v is None:return 'null — motivo explicado en el campo/contrato correspondiente.'
 if isinstance(v,(int,float,bool)):return str(v)
 if isinstance(v,list):return '\n\n'.join('- '+mdvalue(x,level+1).replace('\n','\n  ') for x in v) if v else 'Lista vacía justificada por los límites/decisión del objeto.'
 return '\n\n'.join('**'+str(k).replace('_',' ')+'**: '+mdvalue(w,level+1) for k,w in v.items())
for name in ['fundamentos_criticos','alternativas_agregacion','practicas_diseno','lentes','herramientas','productos','seleccion_portafolio','extension_fair_janus','agenda_validacion']:
 val=R[name];s='# '+name.replace('_',' ').capitalize()+' · Diseño para revisión\n\n'
 if isinstance(val,list):
  for x in val:s+='## '+(x.get('concepto') or x.get('nombre') or x.get('familia') or x.get('lente') or x.get('practica') or x.get('objeto') or x.get('id'))+' ('+x.get('id','agenda')+')\n\n'+mdvalue(x)+'\n\n'
 else:s+=mdvalue(val)
 text(SUP/'desarrollo'/(name+'.md'),s)
text(SUP/'desarrollo/arquitectura.md','# Arquitectura propuesta · Lectura técnica completa\n\n'+mdvalue(R['arquitectura']))
save(SUP/'esquemas/contratos_propuestos.json',R['arquitectura']['contratos'])
text(SUP/'esquemas/contratos_propuestos.md','# Contratos propuestos, sin instancias operativas\n\nNo son esquemas de las capas SSC. Cada campo conserva tipo, significado, origen, unidad y nulabilidad. Los controles se diseñan aquí; la validación semántica con datos reales es futura.\n\n'+'\n\n'.join('## '+c['nombre']+' ('+c['id']+')\n\n'+mdvalue(c) for c in R['arquitectura']['contratos']))
# Cadena de necesidad/historia a evidencia/código sin duplicar corpus completo.
traces=[]
for p in R['productos']:
 for hid in p['historias']:
  h=next(x for x in H['historias'] if x['id']==hid)
  for nid in h['necesidades']:
   n=next(x for x in N['necesidades'] if x['id']==nid)
   traces.append(dict(producto=p['id'],historia=hid,necesidad=nid,titulo_necesidad=n['titulo'],estado_original=n['estado_actual'],tipo=n['tipo'],codigos=n['codigos_comunes'],evidencias=n['evidencias'],evidencia_que_limita=n['evidencia_que_limita'],limites=n['condiciones_y_limites'],localizadores=[dict(evidencia=v,referencia=ev[v].get('referencia'),preguntas=ev[v].get('contexto_pregunta'),voz=ev[v].get('voz')) for v in n['evidencias'] if v in ev],alcance='Relación analítica; referencias canónicas del mismo corpus no son corroboraciones independientes.'))
save(SUP/'matrices/trazabilidad_necesidades.json',traces);table('trazabilidad_necesidades',traces,'matrices')
# Comprobaciones que el validador original no asegura por sí solo.
check('cobertura_inversa_historias',len(R['cobertura_historias'])==21 and all(set(x['productos'])=={p['id'] for p in R['productos'] if x['historia'] in p['historias']} for x in R['cobertura_historias']),'21 filas únicas y correspondencia bidireccional producto↔historia.')
full=read(BASE/'requisitos/02_matriz_requisitos.json');sub=[x for x in full if x['categoria'] in ['GCR','LEN','DAT']]
check('subconjunto_39',len(sub)==39 and {x['id'] for x in sub}=={x['requisito'] for x in R['cobertura_requisitos']} and all(qmap[x['id']]['requisito']==x['requisito'] for x in sub),'Subconjunto exacto de matriz con 208 requisitos; sin cierre de otros 169.')
check('estados_propuesta',all(p['estado']=='PROPUESTA_NO_IMPLEMENTADA' for p in R['productos']) and all(k['estado']=='PROPUESTO_NO_EJECUTADO' for p in R['productos'] for k in p['criterios']) and all(t['compatibilidad']=='COMPATIBILIDAD_NO_PROBADA' for t in R['herramientas']),'3 productos/12 criterios/4 herramientas con estados pendientes correctos.')
check('referencias_fuentes_afirmaciones',all(all(next(s for s in R['fuentes'] if s['id']==f)['estado']=='VERIFICADA' for f in a['fuentes']) for a in R['afirmaciones_tecnicas']),'Cada afirmación tiene fuente primaria verificada; pertinencia interpretativa sigue revisión humana.')
check('campos_perfiles_origen',len(H['perfiles_metadatos'])==21 and all(len(m['campos'])==21 for m in H['perfiles_metadatos']),'441 campos de HU01, 21 contextos temporales y dos espaciales; no se cambian originales.')
# Exportar diagramas de diseño, sin cifras territoriales o simulación.
arch=r'''digraph Arquitectura {
 graph [rankdir=TB,bgcolor="white",pad="0.35",nodesep="0.65",ranksep="0.8",label="ARQUITECTURA PROPUESTA · T01\nRamas por pregunta y soporte; retornos sin sobrescribir originales",labelloc=t,fontname="DejaVu Sans",fontsize=22];
 node [shape=box,style="rounded,filled",fillcolor="#EDF3F7",color="#42657D",fontname="DejaVu Sans",fontsize=17,margin="0.18,0.13"];
 edge [fontname="DejaVu Sans",fontsize=12,color="#315E78",arrowsize=0.8];
 fuente [label="Fuente externa o soporte aportado\nPermiso y custodia por confirmar",fillcolor="#F2EFE8"];
 recep [label="Recepción · M001\nOriginal, finalidad y procedencia\nContrato de recepción C001"];
 unify [label="Unificación · M002\nIdentidad, significado y referencia\nC002 / C003"];
 agg [label="Agregación optativa · M003\nUnidad, miembros y denominador\nConfiguración C004 / resumen C005"];
 build [label="Construcción · M004\nOcasión / revisión / acuerdo\nC006 / C007 / C008"];
 ana [label="Análisis · M005\nComparabilidad y alcance\nLectura con límites C009"];
 prod [label="Productos · M006\nConsulta o documento mínimo\nSalida con trazas C010"];
 humano [label="Actividad humana\nInterpretar, conversar, revalidar\ny decidir; responsable por confirmar",fillcolor="#F4EBD9"];
 fuente -> recep [label="aporte autorizado"];
 recep -> unify [label="original y contexto"];
 {rank=same;agg;build;}
 unify -> agg [label="si requiere resumen"];
 unify -> build [label="notas sin agregación"];
 agg -> build [label="asignaciones útiles"];
 agg -> ana [label="contraste de unidades"];
 build -> ana [label="examinar suficiencia"];
 build -> prod [label="consulta descriptiva"];
 ana -> prod [label="lectura revisable"];
 prod -> humano [label="vista y pregunta"];
 humano -> prod [style=dashed,color="#A45D27",label="duda C011",constraint=false];
 prod -> ana [style=dashed,color="#A45D27",label="cuestionar lectura",constraint=false];
 ana -> build [style=dashed,color="#A45D27",label="volver al respaldo",constraint=false];
 ana -> agg [style=dashed,color="#A45D27",label="revisar unidad",constraint=false];
 build -> unify [style=dashed,color="#A45D27",label="aclarar identidad",constraint=false];
 agg -> unify [style=dashed,color="#A45D27",label="pertenencia dudosa",constraint=false];
 unify -> recep [style=dashed,color="#A45D27",label="fuente o permiso",constraint=false];
 leyenda [shape=note,fillcolor="white",color="#A8ADB2",fontsize=13,label="Continuas: flujos propuestos y condicionales.\nDiscontinuas: retorno de dudas/correcciones (C011).\nM = módulo; C = contrato; prefijo T01 omitido para lectura.\nNo son procesos institucionales observados entre E01–E05.\nNingún servicio o producto se ejecutó."];
 humano -> leyenda [style=invis];
}'''
prod=r'''digraph Productos {
 graph [rankdir=TB,bgcolor="white",pad="0.4",nodesep="0.55",ranksep="0.65",label="TRES PRODUCTOS CANDIDATOS · PROPUESTA NO IMPLEMENTADA\nFuentes requeridas → apoyo propuesto → decisión → comprobación futura",labelloc=t,fontname="DejaVu Sans",fontsize=22];
 node [shape=box,style="rounded,filled",fontname="DejaVu Sans",fontsize=16,color="#42657D",margin="0.18,0.14",width=3.7];
 edge [fontname="DejaVu Sans",fontsize=12,color="#315E78",arrowsize=0.8];
 s1 [label="Fuentes funcionales E01\nPetición, copia, croquis y aclaración\nOriginales no aportados",fillcolor="#F2EFE8"];
 s2 [label="Fuentes funcionales E02\nNotas y relatos de ocasiones\nSegunda ocasión por acordar",fillcolor="#F2EFE8"];
 s3 [label="Fuentes funcionales E03\nAcuerdos, calendario y notas\nOriginales no aportados",fillcolor="#F2EFE8"];
 p1 [label="Expediente de revisión · P001\nÚltimo cambio, respaldo y duda\nHistorias H001–H003",fillcolor="#E5EFF6"];
 p2 [label="Cuaderno de contraste · P002\nOcasiones, unidad y afirmaciones\nHistorias H004–H006",fillcolor="#E5EFF6"];
 p3 [label="Memoria cultural · P003\nAcuerdos y qué volver a preguntar\nH007–H008; H010–H012",fillcolor="#E5EFF6"];
 d1 [label="Decisión técnica\nConservar / modificar / detener\no pedir nueva aclaración",fillcolor="#E8F1E8"];
 d2 [label="Decisión de análisis\nQué comparar y hasta dónde afirmar\no detener seguimiento",fillcolor="#E8F1E8"];
 d3 [label="Decisión de coordinación\nQué retomar, confirmar y anunciar\no conservar como idea",fillcolor="#E8F1E8"];
 c1 [label="Comprobar en fase siguiente\nRetomar cambio y explicar límite\nCriterios K001–K004",fillcolor="#F4EBD9"];
 c2 [label="Comprobar en fase siguiente\nQué cambia con otra ocasión\nCriterios K005–K008",fillcolor="#F4EBD9"];
 c3 [label="Comprobar en fase siguiente\nRelevo, vigencia y comunicación\nCriterios K009–K012",fillcolor="#F4EBD9"];
 {rank=same;s1;s2;s3;}{rank=same;p1;p2;p3;}{rank=same;d1;d2;d3;}{rank=same;c1;c2;c3;}
 s1 -> p1 [label="evidencia autorizada"];s2 -> p2 [label="contraste voluntario"];s3 -> p3 [label="fuente y ocasión"];
 p1 -> d1 [label="explicar revisión"];p2 -> d2 [label="examinar respaldo"];p3 -> d3 [label="preparar preguntas"];
 d1 -> c1 [label="ensayo de tarea"];d2 -> c2 [label="comparar alcance"];d3 -> c3 [label="retomar y revalidar"];
 c1 -> p1 [style=dashed,color="#A45D27",label="reformular",constraint=false];c2 -> p2 [style=dashed,color="#A45D27",label="reformular",constraint=false];c3 -> p3 [style=dashed,color="#A45D27",label="reformular",constraint=false];
 legend [shape=note,fontsize=13,fillcolor="white",label="Cada columna es una relación de diseño, sin cadena entre casos.\nFlechas continuas: fundamento/uso/comprobación propuestos; discontinuas: reformulación.\nP y K usan prefijo T01; H usa HU01. Fuentes concretas y permisos por confirmar.\nTodas las pruebas son propuestas, sin adopción, desempeño o aceptación acreditados."];
 c2 -> legend [style=invis];
}'''
exports=[]
for name,code in [('arquitectura',arch),('productos',prod)]:
 dotpath=SUP/'diagramas'/(name+'.dot');text(dotpath,code)
 for fmt in ['svg','png','pdf','plain']:
  out=dotpath.with_suffix('.'+fmt);proc=subprocess.run(['dot','-Gdpi=140','-T'+fmt,str(dotpath),'-o',str(out)],capture_output=True,text=True)
  exports.append(dict(archivo=str(out.relative_to(SUP)),formato=fmt,retorno=proc.returncode,stderr=proc.stderr,bytes=out.stat().st_size if out.exists() else 0))
check('exportacion_diagramas',all(x['retorno']==0 and x['bytes']>0 for x in exports),exports)
# Validar texto de nodos dentro de bounding box desde plain; inspección visual se documenta aparte.
figurechecks=[]
for name in ['arquitectura','productos']:
 p=SUP/'diagramas'/(name+'.plain');lines=p.read_text().splitlines();head=lines[0].split();w,h=float(head[2]),float(head[3]);nodes=[]
 import shlex
 for line in lines:
  if line.startswith('node '):
   a=line.split();x,y,nw,nh=map(float,a[2:6]);nodes.append(dict(nodo=a[1],dentro= x-nw/2>=-0.01 and y-nh/2>=-0.01 and x+nw/2<=w+0.01 and y+nh/2<=h+0.01))
 figurechecks.append(dict(figura=name,ancho_pulgadas=w,alto_pulgadas=h,nodos=nodes,todos_dentro=all(x['dentro'] for x in nodes),alcance='Contención de cajas, no juicio automático de legibilidad.'))
check('cajas_diagramas',all(x['todos_dentro'] for x in figurechecks),figurechecks)
save(SUP/'controles/figuras_exportacion.json',dict(exportaciones=exports,geometria=figurechecks))
# Las huellas fijan las dos imágenes efectivamente observadas por el asistente.
# La comprobación PDF es complementaria y no equivale a revisión humana.
import fitz
from PIL import Image
reviewed_png={'arquitectura':'7232190fc6a3b2579de25f385791779888fca92835d1709d5706360666bada55','productos':'9b0e588e2758fb106d06c8a341e3604a86297dfe099a97a17369a5a2dd2d91fe'}
visual=[]
for name in ['arquitectura','productos']:
 png=SUP/'diagramas'/(name+'.png');pdf=SUP/'diagramas'/(name+'.pdf')
 with Image.open(png) as im:im.verify()
 with Image.open(png) as im:dimensions=list(im.size)
 with fitz.open(pdf) as doc:
  pages=len(doc);page=doc[0];words=page.get_text('words');body=page.get_text()
  contained=all(page.rect.contains(fitz.Rect(*w[:4])) for w in words)
  labels=['Recepción','Unificación','Agregación','Construcción','Análisis','Productos'] if name=='arquitectura' else ['Expediente','Cuaderno','Memoria','Decisión','Comprobar']
  visible_labels=all(x.casefold() in body.casefold() for x in labels)
 visual.append(dict(figura=name,png_sha256=sha(png),png_efectivamente_inspeccionado=sha(png)==reviewed_png[name],dimensiones_png=dimensions,pdf_sha256=sha(pdf),paginas_pdf=pages,textos_pdf_dentro_pagina=contained,rotulos_pdf_presentes=visible_labels,revision_visual_asistida='Observados ambos PNG: rótulos legibles, conceptos antes de identificadores, contraste suficiente, flechas y leyenda visibles, sin recorte aparente. Arquitectura con ramas/retornos; productos con tres relaciones independientes.',limite='Inspección del mismo asistente, no humana independiente. El PDF se abrió y comprobó por texto/geometría; no se atribuye inspección visual independiente del PDF.'))
check('revision_figuras_asistida',all(x['png_efectivamente_inspeccionado'] and x['paginas_pdf']==1 and x['textos_pdf_dentro_pagina'] and x['rotulos_pdf_presentes'] for x in visual),visual)
save(SUP/'controles/revision_visual.json',dict(fecha='2026-11-25',tipo='ASISTIDA_POR_LLM',figuras=visual,revision_humana_independiente='PENDIENTE'))
# Registro de trabajo y límites interpretativos.
shutil.copyfile(BASE/'instrucciones_T01.md',SUP/'registro/instrucciones_T01.md')
text(SUP/'registro/prompt_analisis_integracion.txt','Petición de la persona usuaria, 25 de noviembre de 2026:\n\nLee íntegramente las instrucciones adjuntas y comprueba el paquete de insumos. Desarrolla T01 con la profundidad solicitada: fundamentos críticos, MAUP, incertidumbre, alternativas de agregación, evaluación de los cuatro lentes, arquitectura adaptada de GeoInsights y dos o tres productos candidatos concretos. Justifica las propuestas mediante las historias y necesidades revisadas, conservando sus condiciones y límites. Contrasta las afirmaciones técnicas con fuentes primarias y documenta qué consultaste. Explica los conceptos en lenguaje comprensible, con identificadores como apoyo. Ejecuta el validador sobre el resultado final, realiza las comprobaciones complementarias y entrega los cuatro archivos completos indicados.\n\nEstrategia de contexto aplicada: lectura de instrucciones completas y maestro 10–16; 21 historias y perfiles; necesidades/fichas/procesos; regreso dirigido a párrafos canónicos y preguntas. Lectura estática del snapshot y consulta primaria técnica; composición por secciones, sin nuevos registros de campo.\n\nNo se incluyen prompts de desarrollo de entrevistas ni se exportan instrucciones internas del servicio. Los archivos preparar_t01.py y empacar_t01.py conservan el texto de especificaciones, las transformaciones documentales y las comprobaciones utilizadas. Modelo exacto y parámetros no expuestos: null; revisión asistida, humana independiente pendiente.\n')
text(SUP/'registro/revision_asistida.md','# Registro de revisión asistida · 25 noviembre 2026\n\nSe revisó el diseño con el expediente vigente y los pasajes registrados en consulta_corpus.json. Esta revisión la realizó el mismo asistente que produjo el diseño; no es independiente ni humana.\n\n- Se preservó la corrección sitio/acceso y la ausencia de movimiento ejecutado de punto en E01.\n- Se mantuvo el papel de tiempo/cercanía y valor del relato posterior en E02, además de la corrección «explicar menos».\n- Se separó visita/confirmación, consulta parcial/comunidad, posibilidad/compromiso y mediación emergente de E03.\n- Se conservaron el par tangible y restricción de cantidad de E04 y el margen de explorar/no comprar de E05. H017 y H021 quedan pendientes explícitas.\n- Se distinguieron DEMANDA_EXPRESADA, CAPACIDAD_DERIVADA y OPORTUNIDAD_PROPUESTA; no aprobación de terceros o necesidad de software público atribuida.\n- Se revisaron ocho familias, cuatro prácticas, cuatro lentes, seis responsabilidades y ocho representaciones, sin ejecución territorial.\n- Se conservó fuente indexada de MG con alcance restringido y fallos de recuperación; no payload, escala o licencia de capas SSC inventados.\n- Se localizaron DEBUG, población vacía y dependencia Mapper externa en código; no certificación de funcionamiento, identidad con ZIP de clase o cita de artículo inventada.\n\nLos controles mecánicos adjuntos verifican sus propios objetos. Las pruebas de utilidad de productos, contratos con datos operativos, pertinencia institucional, fuentes situadas y revisión humana independiente permanecen pendientes. No se declara saturación, concordancia o conformidad FAIR/FDO/JANUS.\n')
# Copias de scripts realmente utilizados: sin configuración del snapshot.
for src,dst in [(ROOT/'preparar_t01.py',SUP/'scripts/preparar_t01.py'),(Path(__file__),SUP/'scripts/empacar_t01.py'),(BASE/'validar_diseno.py',SUP/'scripts/validar_diseno.py')]:shutil.copyfile(src,dst)
# Enlaces de figuras de MD requieren extracción y están declarados.
md=(OUT/'T01_explicacion_v1.md').read_text();links=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',md)
check('rutas_figuras_explicacion',len(links)==2 and all((OUT/l).is_file() for l in links),links)
# Reglas de esquema no ejecutadas se mantienen como propuestas en datos.
readmes={
 'tablas':'Tablas completas derivadas del JSON. Cada celda es JSON válido, también los textos y nulos: así se conserva la estructura anidada sin recortar. cotejo_tablas.json comprueba igualdad celda a celda. Son diseño, no datos estadísticos territoriales.',
 'matrices':'historias_21.csv conserva disposición, restricciones de origen y productos. requisitos_39.csv conserva criterio del encargo y ubicación del desarrollo. trazabilidad_necesidades enlaza producto/historia/necesidad/códigos/evidencias al PAQUETE_ENTRADA; no duplica todo el corpus ni añade voces.',
 'fuentes':'registro_fuentes.json y bibliografia.md indican qué se consultó y qué falló. consulta_corpus.json registra lectura dirigida. entradas_referenciadas.json identifica originales como PAQUETE_ENTRADA por ruta/huella: no están redistribuidos en este ZIP. LICENSE_GeoInsights conserva atribución MIT, sin licenciar corpus o datos externos.',
 'esquemas':'Once contratos propuestos con campos y controles de aceptar/advertir/detener. No son esquemas inspeccionados de SSC ni instancias operativas. Validador estructural T01 no acredita adecuación semántica de contratos.',
 'desarrollo':'Fichas completas legibles derivadas del JSON para revisar fundamentos, unidades, prácticas, lentes, herramientas, productos, arquitectura, selección, agenda y FAIR/JANUS. No es el cuerpo final del reporte. La prosa principal está en T01_explicacion_v1.md fuera del ZIP.',
 'registro':'Instrucciones T01 y petición de análisis/integración, estrategia de contexto y revisión asistida. No prompts de desarrollo de entrevistas ni instrucciones internas del servicio. No revisión humana independiente.',
 'controles':'Controles reales de integridad, citas/localizadores, tablas, figuras y esquema. comprobaciones_complementarias.json es cotejo de esta entrega; el validador original tiene alcance propio. La inspección visual asistida se registra con sus límites; las pruebas de productos siguen pendientes.',
 'diagramas':'Arquitectura y productos son PROPUESTAS. DOT y SVG editables; PNG/PDF exportados mediante Graphviz; plain conserva posiciones para comprobar cajas. Continuas indican flujos/relaciones condicionados; discontinuas, retornos o reformulación. No flechas institucionales observadas entre casos.',
 'scripts':'Scripts usados para componer diseño, exportar soportes/comprobarlos y validador original preservado. Reproducción: disponer del PAQUETE_ENTRADA extraído en insumos/T01_insumos_v1 y snapshot seguro en geoinsights/<carpeta commit>. Copiar preparar_t01.py y empacar_t01.py al directorio de trabajo; copiar registro/seleccion_parrafos.json a ese mismo directorio y la explicación entregada a entrega/T01_explicacion_v1.md. Ejecutar preparar_t01.py; luego python3 insumos/T01_insumos_v1/validar_diseno.py insumos/T01_insumos_v1 entrega/T01_diseno_v1.json --salida entrega/T01_control_validacion.json; finalmente empacar_t01.py. Requiere Python 3, Graphviz, Pillow y PyMuPDF. No ejecuta código del snapshot. Las huellas de PNG verifican las figuras observadas en esta revisión; si otra versión de Graphviz cambia su exportación, ese control exigirá nueva inspección, sin heredar automáticamente conformidad visual.'}
for folder,description in readmes.items():text(SUP/folder/'LEEME.md','# '+folder.capitalize()+'\n\n'+description+'\n')
text(SUP/'LEEME.md','# T01 · Soportes de diseño para revisión\n\nEste ZIP acompaña T01_diseno_v1.json, T01_explicacion_v1.md y T01_control_validacion.json. Extraer T01_soportes_v1 junto a los otros tres archivos para que resuelvan las imágenes relativas.\n\nComenzar por la explicación, luego diagramas/productos y las matrices. Usar desarrollo para contrastar alternativas y contratos, fuentes para revisar qué se leyó y controles para delimitar lo comprobado.\n\nNingún producto o método territorial se ejecutó. Aceptación, compatibilidad, revisión humana independiente y conformidad integral FAIR/FDO siguen pendientes. Inventario y SHA-256 excluyen el propio manifiesto; los originales del paquete de entrada se referencian, sin declararlos disponibles aquí.\n\nLas flechas son arquitectura/diseño propuesto, no conexiones institucionales observadas. El patrón GeoInsights se atribuye a DataLama Team 2020–2021 (MIT), commit ab60b86a6a87bca0dd370c7c4af3ada4185d187e; no copia de credenciales o código ejecutable del snapshot.\n')
# Guardar selección usada para poder reproducir la bitácora de consulta.
shutil.copyfile(ROOT/'seleccion_parrafos.json',SUP/'registro/seleccion_parrafos.json')
check('sin_directorios_vacios',all(any(p.iterdir()) for p in SUP.rglob('*') if p.is_dir()),'Todas las carpetas tienen contenido y LEEME.')
# Copiar control de esquema que corresponde al JSON actual, sin modificarlo.
validation=read(OUT/'T01_control_validacion.json')
check('validador_sobre_final',validation['estado']=='SIN_ERRORES_ESTRUCTURALES' and validation['ejecucion']['sha256_resultado']==sha(OUT/'T01_diseno_v1.json') and validation['ejecucion']['sha256_validador']==sha(BASE/'validar_diseno.py'),dict(estado=validation['estado'],sha256_resultado=sha(OUT/'T01_diseno_v1.json')))
shutil.copyfile(OUT/'T01_control_validacion.json',SUP/'controles/T01_control_validacion.json')
save(SUP/'registro/salidas_principales.json',dict(alcance='Tres archivos principales externos al ZIP; su huella permite cotejarlos con los soportes. El ZIP no se incluye en sí mismo.',archivos=[dict(nombre=p.name,bytes=p.stat().st_size,sha256=sha(p)) for p in [OUT/'T01_diseno_v1.json',OUT/'T01_explicacion_v1.md',OUT/'T01_control_validacion.json']]))
# Decisión editorial de comprobación cualitativa: independiente del validador.
save(SUP/'controles/comprobaciones_complementarias.json',dict(fecha_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),tipo_revision='ASISTIDA_POR_LLM',revision_humana_independiente='PENDIENTE',controles=checks,estado='CONFORME_EN_ALCANCE_DOCUMENTAL' if all(x['estado']=='CONFORME' for x in checks) else 'INCIDENCIAS',limites='No certifica fuentes situadas, interpretación, adopción, compatibilidad o implementación. Las pruebas de productos se conservan propuestas, no ejecutadas.'))
# Lista exacta de archivos, tamaños y hashes; manifiesto se excluye a sí mismo.
files=sorted(p for p in SUP.rglob('*') if p.is_file() and p.name!='manifest_sha256.json')
manifest_out=dict(version='1.0',alcance='Integridad de soportes; manifiesto excluido de sí mismo.',archivos=[dict(ruta=str(p.relative_to(SUP)),bytes=p.stat().st_size,sha256=sha(p)) for p in files])
save(SUP/'manifest_sha256.json',manifest_out)
for a in manifest_out['archivos']:
 p=SUP/a['ruta'];assert p.stat().st_size==a['bytes'] and sha(p)==a['sha256']
zipout=OUT/'T01_soportes_v1.zip'
with zipfile.ZipFile(zipout,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(SUP.rglob('*')):
  if p.is_file():z.write(p,str(p.relative_to(OUT)))
with zipfile.ZipFile(zipout) as z:
 assert z.testzip() is None
 for a in manifest_out['archivos']:assert hashlib.sha256(z.read('T01_soportes_v1/'+a['ruta'])).hexdigest()==a['sha256']
print(json.dumps(dict(estado='COMPLETO' if all(x['estado']=='CONFORME' for x in checks) else 'REVISAR',tablas=len(tablechecks),archivos_soportes=len(manifest_out['archivos'])+1,zip_bytes=zipout.stat().st_size,sha256_zip=sha(zipout)),ensure_ascii=False))
if not all(x['estado']=='CONFORME' for x in checks):raise SystemExit(1)
