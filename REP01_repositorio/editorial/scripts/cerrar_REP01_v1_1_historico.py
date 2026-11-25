from pathlib import Path
import json,hashlib,re,shutil,zipfile,subprocess,sys,csv,collections,datetime,html
import fitz
ROOT=Path.cwd();W=ROOT/'tmp/review/REP01_revision_v1_1';R=W/'REP01_repositorio';BASE=ROOT/'tmp/review/REP01_insumos_v1'
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(p.read_text())
def dump(p,j):p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
pdf=W/'P3002B_Evidencia1_Ricardo_Graffe.pdf';shutil.copy2(ROOT/'tmp/review/REP01_render_cierre'/pdf.name,pdf)
word=W/'P3002B_Evidencia1_Ricardo_Graffe.docx';md=W/'REP01_reporte_v1_1.md';trace=W/'REP01_trazabilidad_v1_1.json';j=rd(trace)
pages=fitz.open(pdf);body=[];alltext='';links=[];bounds=[]
for i,p in enumerate(pages):
    t=p.get_text();alltext+=t
    m=re.search(r'Cuerpo\s*·\s*(\d+)',t)
    if m:body.append({'pagina_pdf':i+1,'pagina_cuerpo':int(m.group(1))})
    for l in p.get_links():
        if l.get('file'):
            q=l['file'];assert not Path(q).is_absolute()and'..'not in Path(q).parts and(W/q).is_file(),q
            links.append({'pagina_pdf':i+1,'tipo':'ARCHIVO_RELATIVO','destino':q})
        elif l.get('uri'):
            assert l['uri'].startswith(('https://','http://')),l
            links.append({'pagina_pdf':i+1,'tipo':'URL','destino':l['uri']})
    for b in p.get_text('blocks'):
        assert b[0]>=0 and b[1]>=0 and b[2]<=p.rect.width+1 and b[3]<=p.rect.height+1
    bounds.append({'pagina_pdf':i+1,'contenido_dentro_pagina':True})
assert 0<len(body)<=10 and [x['pagina_cuerpo']for x in body]==list(range(1,len(body)+1))
norm=lambda x:re.sub(r'\s+',' ',x).strip()
for q in j['citas']:assert norm(q['cita'])in norm(alltext),q['id']
assert '\ufffd'not in alltext
map_sections=[]
for s in j['secciones']:
    # La búsqueda normalizada admite los saltos de línea del título.
    hits=[i+1 for i,p in enumerate(pages)if norm(s['titulo'])in norm(p.get_text())]
    assert len(hits)==1,(s['id'],hits);s['pagina_pdf_inicio']=hits[0];s['pagina_cuerpo_inicio']=hits[0]-1
    map_sections.append({'id':s['id'],'pagina_pdf_inicio':hits[0],'pagina_cuerpo_inicio':hits[0]-1})
for k,fig in enumerate(j['figuras'],1):
    hits=[i+1 for i,p in enumerate(pages)if f'Figura {k}.'in p.get_text()]
    assert len(hits)==1,(k,hits);fig['pagina_pdf']=hits[0]
    if k==1:
        fig['tamano_propuesto']='Ancho efectivo 6.65 pulgadas; composición en dos filas, PNG 240 dpi de Graphviz, revisión visual en página PDF 3.'
        fig['simplificacion']+=' En 1.1 se conserva la misma secuencia en dos filas; no se añade una transferencia. El límite conserva línea sin flecha.'
    fig['alcance_revision']='Inspección visual asistida del gráfico y de su página en el PDF final; fuentes y simplificaciones cotejadas. No revisión humana independiente.'
j['metadatos']['estado']='MAQUETADO_COMPROBADO';j['metadatos']['paginacion_estado']='COMPROBADA'
j['paginacion_efectiva']={'total_pdf':len(pages),'cuerpo':len(body),'paginas_pdf_cuerpo':[x['pagina_pdf']for x in body],'portada':[1],'referencias':[len(pages)-1],'anexo_metodologico':[len(pages)],'maximo_cuerpo':10,'estado':'COMPROBADA','limite':'Conteo del PDF suministrado y render del Word; otro editor puede repaginar el DOCX.'}
j['pendientes_maquetacion']=[]
j['limites']=[x for x in j['limites']if 'PENDIENTE_MAQUETACION'not in x]
j['limites'].append('PDF final con nueve páginas de cuerpo; la edición posterior del Word exige recontar páginas.')
j['metadatos']['limites']=[x for x in j['metadatos']['limites']if 'Paginación estimada'not in x]
render=ROOT/'tmp/review/REP01_render_cierre'
layout={'control':'Maquetación REP01 1.1','estado':'COMPROBADA_ASISTIDA','pdf':pdf.name,'pdf_sha256':sh(pdf),'docx':word.name,'docx_sha256':sh(word),'paginas_totales':len(pages),'paginas_cuerpo':len(body),'detalle_cuerpo':body,'secciones':map_sections,'figuras':[{ 'id':f['id'],'pagina_pdf':f['pagina_pdf']}for f in j['figuras']],'revision_visual':{'estado':'REALIZADA_ASISTIDA','paginas_pdf':list(range(1,len(pages)+1)),'resultado':'Sin cortes, superposiciones, glifos ausentes o filas truncadas visibles; tablas repetidas con encabezado. Se corrigieron regla de título y espacio provocado por figura vertical.','renderes':[{'pagina':int(p.stem.split('-')[-1]),'sha256':sh(p)}for p in sorted(render.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))]},'citas_pdf':{'total':len(j['citas']),'literalidad_normalizando_solo_espacios':'COINCIDE'},'enlaces_pdf':links,'limites':['La inspección es asistida, no humana independiente.','El PDF congela la paginación comprobada; DOCX puede repaginarse en otro equipo.','Los enlaces locales pueden requerir autorización del visor PDF y extracción completa del ZIP.']}
dump(R/'editorial/controles/maquetacion_v1_1.json',layout)
# Cerrar solo los requisitos de producción efectivamente completados.
for x in j['cobertura_requisitos']:
    if x['requisito']in ['ALC05','PRO12','RED08','RED15']:
        prev=x['estado'];x['estado']='ATENDIDO_EN_SOPORTE';x['evidencia_cumplimiento']='Word y PDF producidos; PDF de doce páginas totales con nueve de cuerpo. Tres figuras y cinco tablas inspeccionadas en página; fuentes completas preservadas en repositorio.'
        x['limite']='Cumplimiento de formato/legibilidad y extensión del archivo final; no acredita divergencias documentales, revisión humana independiente o pruebas de producto.'
        if 'editorial/controles/maquetacion_v1_1.json'not in x['soportes']:x['soportes'].append('editorial/controles/maquetacion_v1_1.json')
        adjust=rd(R/'editorial/registros/ajustes_cobertura_v1_1.json');adjust.append({'requisito':x['requisito'],'antes':prev,'despues':x['estado'],'razon':x['evidencia_cumplimiento']});dump(R/'editorial/registros/ajustes_cobertura_v1_1.json',adjust)
dump(R/'editorial/registros/cobertura_requisitos.json',j['cobertura_requisitos'])
with(R/'editorial/registros/cobertura_requisitos.csv').open('w',newline='',encoding='utf-8-sig')as f:
    fields=['requisito','enunciado_original','estado','secciones','soportes','evidencia_cumplimiento','limite'];cw=csv.DictWriter(f,fieldnames=fields);cw.writeheader()
    for x in j['cobertura_requisitos']:cw.writerow({k:(' | '.join(x[k])if isinstance(x.get(k),list)else x.get(k,''))for k in fields})
dump(R/'editorial/controles/revision_figuras_v1_1.json',{'estado':'REALIZADA_ASISTIDA','figuras':j['figuras'],'revision_humana_independiente':'PENDIENTE','control_maquetacion':'maquetacion_v1_1.json'})
review={'version':'1.1','estado':'REVISION_ASISTIDA_COMPLETADA','metodo':['Lectura completa del manuscrito recibido y revisado','Siete citas cotejadas con texto canónico y contexto próximo','Tablas nuevas derivadas de cuatro modelos, cinco actores y cinco necesidades','Fuentes de conteos y procedencia localizadas','Inspección visual de tres figuras y doce páginas finales','Controles repetidos sobre originales y copia revisada'],'originales':'Conservados sin alteración en coordinación; copia revisada con cambios editoriales identificados.','pendientes_sustantivos':['Revisión humana independiente','Documentos directamente aplicables a episodios; cero divergencias formalmente demostradas','Posturas de homologación no recabadas','Pruebas de utilidad y factibilidad de productos, pendientes de etapa posterior'],'no_calificacion_automatica':True}
dump(R/'editorial/controles/revision_editorial_asistida_v1_1.json',review)
note=R/'editorial/registros/revision_coordinacion_v1_1.md'
with note.open('a')as f:f.write('\n## Maquetación comprobada\n\nEl PDF final tiene doce páginas: portada 1, cuerpo 2 a 10 (nueve páginas), referencias 11 y anexo metodológico 12. Las doce páginas y las tres figuras se inspeccionaron visualmente. Se conservan cinco tablas, siete citas y las cinco voces. La figura 1 se recompuso en dos filas sin cambiar su sentido. Los enlaces locales del PDF se verificaron como rutas relativas existentes. El control de maquetación guarda huellas de DOCX/PDF y renderes.\n')
# Localizadores de formulaciones solicitados por el usuario.
method=[]
for i,line in enumerate(md.read_text().splitlines(),1):
    if re.search('generad[ao]s? con IA|generaron con IA|grabacion|grabación|consentimientos firmados',line,re.I):method.append({'linea_md':i,'texto':line})
dump(R/'editorial/registros/localizadores_metodologicos_v1_1.json',{'manuscrito':md.name,'pdf_paginas':[2,12],'ubicaciones':method,'alcance':'Localización para revisión del usuario; se conserva una declaración fiel a modalidad autorizada y registros disponibles.'})
# Actualizar el índice legible de secciones y figuras.
guide=['# Guía por sección del reporte\n','Archivo principal: [manuscrito revisado](../../../REP01_reporte_v1_1.md). Word y PDF están junto a ese archivo.\n','| Sección | Inicio en cuerpo | Soportes |','|---|---|---|']
for s in j['secciones']:guide.append('| '+s['titulo']+' | '+str(s['pagina_cuerpo_inicio'])+' | '+', '.join(s['soportes'])+' |')
(R/'editorial/registros/guia_por_seccion.md').write_text('\n'.join(guide)+'\n')
shutil.copy2(Path(__file__),R/'editorial/scripts/cerrar_REP01_v1_1_historico.py')
# No incluir scripts activos con afirmaciones de regeneración portátil: son registro histórico.
with(R/'editorial/scripts/LEEME.md').open('a')as f:f.write('\n## Revisión 1.1\n\nEl control activo es validar_reporte_v1_1.py y recibe base original, Markdown 1.1, trazabilidad 1.1 y --repositorio. Comprueba también el PDF hermano y la huella del control de maquetación. Los scripts cuyo nombre termina en historico.py documentan una ejecución con rutas locales; no prometen reconstrucción portátil del documento.\n')
# Manifiesto se escribe después de controles internos y antes del control externo.
dump(trace,j)
comp=R/'editorial/controles/complementarios_v1_1.json'
subprocess.run([sys.executable,str(R/'editorial/scripts/controles_complementarios.py'),str(R),str(md),str(trace),str(BASE),'--salida',str(comp)],check=True)
inventory=[{'ruta':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sh(p)}for p in sorted(R.rglob('*'))if p.is_file()and p!=R/'manifest.json'and'__pycache__'not in p.parts]
j['repositorio']['inventario']=inventory;j['repositorio']['instrucciones_verificacion']=['Extraer paquete completo y conservar documentos junto a REP01_repositorio/.','Cotejar inventario y ejecutar editorial/scripts/validar_reporte_v1_1.py con insumos originales, manuscrito/trazabilidad 1.1 y --repositorio.','Consultar control de maquetación para huellas DOCX/PDF, páginas y revisión asistida.','Los scripts históricos no son instaladores portátiles.'];j['repositorio']['adaptaciones']+=['Coordinación 1.1 actualiza guías editoriales y figura 1, añade tablas/controles/registros sin cambiar fuentes canónicas.']
dump(R/'manifest.json',{'paquete':'REP01_repositorio','version':'1.1','estado':'MAQUETADO_COMPROBADO','inventario':inventory,'exclusion':'Solo manifest.json raíz; manuscrito/trazabilidad/control/Word/PDF externos para evitar ciclos.'})
dump(trace,j)
control=W/'REP01_control_editorial_v1_1.json'
subprocess.run([sys.executable,str(R/'editorial/scripts/validar_reporte_v1_1.py'),str(BASE),str(md),str(trace),'--repositorio',str(R),'--salida',str(control)],check=True)
c=rd(control);c['controles_complementarios']={'estado':rd(comp)['estado'],'errores':rd(comp)['errores'],'archivo':'REP01_repositorio/editorial/controles/complementarios_v1_1.json','sha256':sh(comp)};c['paginacion_efectiva']=j['paginacion_efectiva'];c['maquetacion']={'archivo':'REP01_repositorio/editorial/controles/maquetacion_v1_1.json','sha256':sh(R/'editorial/controles/maquetacion_v1_1.json')};c['revision_humana_independiente']='PENDIENTE';c['sin_publicacion']=True;c['sin_implementacion']=True;dump(control,c)
# Índice HTML y enlaces del reporte: sin rutas faltantes.
for raw in re.findall(r'href="([^"]+)"',(R/'indice.html').read_text()):assert(R/raw).is_file(),raw
output=ROOT/'output/REP01_entrega';output.mkdir(parents=True,exist_ok=True)
for name in [md.name,trace.name,control.name,word.name,pdf.name]:shutil.copy2(W/name,output/name)
zpath=output/'P3002B_Evidencia1_entrega.zip'
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=8)as z:
    for name in [md.name,trace.name,control.name,word.name,pdf.name]:z.write(W/name,'P3002B_Evidencia1/'+name)
    for p in sorted(R.rglob('*')):
        if p.is_file()and'__pycache__'not in p.parts:z.write(p,'P3002B_Evidencia1/REP01_repositorio/'+str(p.relative_to(R)))
with zipfile.ZipFile(zpath)as z:
    assert z.testzip()is None
    assert len(z.namelist())==len(set(z.namelist()))==len(inventory)+6
    for p in inventory:assert hashlib.sha256(z.read('P3002B_Evidencia1/REP01_repositorio/'+p['ruta'])).hexdigest()==p['sha256']
    for name in [md.name,trace.name,control.name,word.name,pdf.name]:assert hashlib.sha256(z.read('P3002B_Evidencia1/'+name)).hexdigest()==sh(W/name)
out={'version':'1.1','estado':c['estado'],'paginas_pdf':len(pages),'paginas_cuerpo':len(body),'requisitos':len(j['cobertura_requisitos']),'cobertura':dict(collections.Counter(x['estado']for x in j['cobertura_requisitos'])),'archivos_repositorio':len(inventory)+1,'archivo_entrega':zpath.name,'bytes_zip':zpath.stat().st_size,'sha256_zip':sh(zpath),'controles':'SIN_ERRORES_EN_ALCANCE_COMPROBADO','fuentes_canonicas':'PRESERVADAS'}
dump(ROOT/'tmp/review/REP01_cierre_v1_1.json',out);print(json.dumps(out,ensure_ascii=False))
