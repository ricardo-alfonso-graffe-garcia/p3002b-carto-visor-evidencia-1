from pathlib import Path
import json,re,shutil,csv,html
ROOT=Path.cwd();W=ROOT/'tmp/review/REP01_revision_v1_1';R=W/'REP01_repositorio'
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
j=json.loads((W/'REP01_trazabilidad_v1_1.json').read_text())
# Guías editoriales activas; las fuentes analíticas de la base permanecen intactas.
for p in [R/'LEEME.md']+list((R/'editorial').rglob('*.md')):
    s=p.read_text().replace('REP01_reporte_v1.md','REP01_reporte_v1_1.md').replace('REP01_trazabilidad_v1.json','REP01_trazabilidad_v1_1.json').replace('REP01_control_editorial.json','REP01_control_editorial_v1_1.json')
    s=s.replace('La revisión humana independiente y la comprobación efectiva de diez páginas permanecen pendientes.','La revisión humana independiente permanece pendiente. La paginación efectiva y los controles de Word/PDF se documentan en `editorial/controles/maquetacion_v1_1.json`.')
    if p==R/'LEEME.md':
        s=s.replace('# REP01 · Decidir con información suficiente','# REP01 Procesos actores y necesidades de información territorial')
        s=s.replace('Versión para revisión editorial, sin publicación ni licencia abierta del corpus.','Versión 1.1 revisada en coordinación y maquetada, sin publicación ni licencia abierta del corpus.')
        a=s.index('El manuscrito editable es');b=s.index('\n1.',a)
        s=s[:a]+'''El paquete de entrega contiene el Word y PDF `P3002B_Evidencia1_Ricardo_Graffe`, el texto `REP01_reporte_v1_1.md`, la trazabilidad y el control editorial 1.1. Estos archivos deben permanecer al mismo nivel que `REP01_repositorio/` después de extraer el ZIP. La trazabilidad y el control son externos al inventario de esta carpeta para evitar ciclos.

Para una entrada visual, abre [indice.html](indice.html). La [revisión de coordinación](editorial/registros/revision_coordinacion_v1_1.md) explica los cambios y los límites persistentes. La matriz CSV de cobertura está en `editorial/registros/cobertura_requisitos.csv`.
'''+s[b:]
        s=s.replace('ejecutar el validador suministrado','ejecutar `editorial/scripts/validar_reporte_v1_1.py`')
        s += '\n## Entrega y verificación\n\nLos scripts originales 1.0 se conservan como antecedente y no sustituyen los controles 1.1. La comprobación actual usa el validador 1.1 con las mismas entradas originales y la carpeta final real. Word/PDF se cotejan en el control de maquetación. Los archivos DOCX pueden repaginarse en otro editor; el conteo certificado corresponde al PDF suministrado y al render de ese DOCX.\n'
    p.write_text(s)
(R/'editorial/figuras/LEEME.md').write_text('''# Figuras del reporte

Tres diagramas con fuente DOT y exportaciones SVG/PNG. La figura 1 conserva recepción, contraste, aclaración mediada, decisión/copia, devolución y límite; en 1.1 se recompone en dos filas y se exporta a mayor resolución para mejorar su lectura en página. La figura 2 conserva dos derivaciones analíticas independientes. La figura 3 resume arquitectura con agregación opcional y revisión de incidencias. Las simplificaciones y fuentes se registran en la trazabilidad externa.

Los mapas completos de cinco procesos permanecen en `analisis/procesos/P01/figuras_revisadas_v1_1/` desde la raíz del repositorio. Los cuatro modelos documentales se conservan en `analisis/documental/D01/soportes_recibidos/figuras/`. Los SVG permiten ampliar sus etiquetas. El registro de inspección 1.1 y la maquetación distinguen revisión asistida de revisión humana independiente.
''')
with(R/'editorial/registros/cobertura_requisitos.csv').open('w',newline='',encoding='utf-8-sig')as f:
    fields=['requisito','enunciado_original','estado','secciones','soportes','evidencia_cumplimiento','limite'];cw=csv.DictWriter(f,fieldnames=fields);cw.writeheader()
    for x in j['cobertura_requisitos']:cw.writerow({k:(' | '.join(x[k])if isinstance(x.get(k),list)else x.get(k,''))for k in fields})
links=[('Libro común de códigos','55_libro_comun_v1_3.md'),('Síntesis de hallazgos','63_sintesis_transversal_v1_1.md'),('Cinco procesos relatados','67_procesos_descritos_v1_1.md'),('Contraste documental','72_contraste_documental_v1_1.md'),('Actores y preferencias','76_actores_y_preferencias_v1_1.md'),('Necesidades de información','82_necesidades_v1_1.md'),('Historias y objetos digitales','88_historias_y_objetos_v1_1.md'),('Fundamentos y diseño','93_diseno_y_fundamentos_v1_1.md'),('Cobertura de 208 requisitos','editorial/registros/cobertura_requisitos.csv'),('Cambios de coordinación','editorial/registros/revision_coordinacion_v1_1.md')]
lis=''.join('<li><a href="'+html.escape(url,quote=True)+'">'+html.escape(label)+'</a></li>'for label,url in links)
corpus=''.join('<li>Entrevista '+str(i)+': <a href="corpus/E0'+str(i)+'/E0'+str(i)+'_transcripcion_v1.docx">Word</a> · <a href="corpus/E0'+str(i)+'/E0'+str(i)+'_texto_con_localizadores.txt">texto con localizadores</a></li>'for i in range(1,6))
(R/'indice.html').write_text('''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Soportes de Evidencia 1</title><style>body{font-family:Arial,sans-serif;max-width:900px;margin:48px auto;padding:0 24px;line-height:1.6;color:#171717}a{color:#205476}h1{line-height:1.2}li{margin:6px 0}</style><h1>Soportes de Evidencia 1</h1><p>Ricardo Alfonso Graffe Garcia · A01664904 · P3002B</p><p>El reporte compara cinco relatos y sus decisiones de información. Este índice permite consultar las fuentes completas, los mapas, las derivaciones y los controles. Los vínculos son archivos locales; extrae el paquete completo antes de abrirlos.</p><h2>Documentos de análisis</h2><ul>'''+lis+'''</ul><h2>Corpus</h2><ul>'''+corpus+'''</ul><h2>Figuras del cuerpo</h2><ul>'''+''.join('<li><a href="editorial/figuras/REP01-F00'+str(i)+'.svg">Figura '+str(i)+' ampliable</a></li>'for i in range(1,4))+'''</ul><h2>Alcance</h2><p>La revisión de coordinación y de maquetación es asistida. Las prioridades son locales y los productos son propuestas pendientes de prueba. El contraste documental conserva las correspondencias que no pudieron acreditarse. La declaración metodológica está en el reporte y sus registros.</p></html>''')
for src,name in [('tmp/review/maquetar_REP01.py','maquetar_REP01_v1_1_historico.py'),('tmp/review/preparar_cierre_REP01.py','preparar_cierre_REP01_v1_1_historico.py')]:shutil.copy2(ROOT/src,R/'editorial/scripts'/name)
# Validador derivado con versión 1.1, procedencia local identificada y comprobación efectiva del PDF.
s=(R/'editorial/scripts/validar_reporte.py').read_text()
s=s.replace("m.get('version')=='1.0'and m.get('estado')=='MANUSCRITO_PARA_REVISION'","m.get('version')=='1.1'and m.get('estado')=='MAQUETADO_COMPROBADO'")
s=s.replace("m.get('paginacion_estado')=='PENDIENTE_MAQUETACION'","m.get('paginacion_estado')=='COMPROBADA'")
s=s.replace("if words>3800:","if words>3800 and m.get('paginacion_estado')!='COMPROBADA':")
s=s.replace("ids.update(canon)","ids.update(canon)\n collect(json.loads((repo/'editorial/registros/procedencia_REP01.json').read_text()))")
s=s.replace("return {'validador':'REP01 editorial 1.0'",'''# Conteo físico del PDF suministrado, no estimación por palabras.
 import fitz
 pdf=repo.parent/'P3002B_Evidencia1_Ricardo_Graffe.pdf'
 with fitz.open(pdf) as pag:
  body_pages=[]
  for i,page in enumerate(pag):
   match=re.search(r'Cuerpo\\s*·\\s*(\\d+)',page.get_text())
   if match:body_pages.append((i+1,int(match.group(1))))
 ck(bool(body_pages) and len(body_pages)<=10 and [n for i,n in body_pages]==list(range(1,len(body_pages)+1)),'paginacion','PDF sin cuerpo contado o sobre máximo de diez páginas.')
 layout=json.loads((repo/'editorial/controles/maquetacion_v1_1.json').read_text())
 ck(layout['pdf_sha256']==hashlib.sha256(pdf.read_bytes()).hexdigest() and layout['paginas_cuerpo']==len(body_pages),'paginacion','Control de maquetación no corresponde al PDF final.')
 return {'validador':'REP01 editorial 1.1' ''')
s=s.replace("'paginacion':'PENDIENTE_MAQUETACION'","'paginacion':'COMPROBADA'")
# El texto de alcance distingue validación programática de inspección visual aparte.
s=s.replace('No certifica calidad narrativa, pertinencia semántica, fuentes externas, inspección real de figuras, veracidad de metadatos declarados, validación humana o diez páginas maquetadas.','Incluye conteo del PDF y su huella; no certifica calidad narrativa, pertinencia semántica, fuentes externas, inspección visual o validación humana. La inspección visual asistida se registra aparte.')
(R/'editorial/scripts/validar_reporte_v1_1.py').write_text(s)
print(json.dumps({'guia_html':True,'csv_filas':len(j['cobertura_requisitos']),'validador_derivado':'1.1'},ensure_ascii=False))
