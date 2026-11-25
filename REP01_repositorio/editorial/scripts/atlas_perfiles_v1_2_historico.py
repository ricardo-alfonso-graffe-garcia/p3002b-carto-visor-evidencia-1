from pathlib import Path
import json,subprocess
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
W=Path('tmp/review/REP01_revision_v1_2');R=W/'REP01_repositorio';E=R/'editorial/revision_v1_2'
h=json.loads((R/'88_historias_y_objetos_v1_1.json').read_text());tr=json.loads(Path('output/REP01_entrega/REP01_trazabilidad_v1_1.json').read_text())
dot='''digraph G {
graph [rankdir=TB, bgcolor="white",pad=.2,nodesep=.4,ranksep=.5];
node [shape=box,fontname="Liberation Sans",fontsize=12,margin=".14,.10",color="#777777"];
edge [fontname="Liberation Sans",fontsize=10,color="#666666",style=dashed];
src [label="Producción o custodia SSC\nUnidad, captura y edición por acreditar"];
coord [label="Coordinación ADIP\nAcordar significado y responsabilidades"];
dev [label="Desarrollo propuesto\nValidar y preparar derivado versionado"];
user [label="Función usuaria por confirmar\nConsultar, decidir o señalar incidencia"];
auth [label="Revisión y autoridad de cambio\nCompetencia y procedimiento por acreditar"];
{rank=same;src;coord;}
src -> dev [label="Original y metadatos\ncon permiso"];
coord -> dev [label="Contrato y criterio\npor acordar"];
dev -> user [label="Vista, respaldo y límites"];
user -> auth [label="Incidencia con evidencia"];
auth -> src [label="Consulta o cambio autorizado\ncon versión nueva",constraint=false];
auth -> dev [label="Decisión e impacto\nen derivados",constraint=false];
}'''
(E/'recorrido_institucional_propuesto.dot').write_text(dot)
for typ in ['svg','png']:subprocess.run(['dot','-T'+typ,str(E/'recorrido_institucional_propuesto.dot'),'-o',str(E/f'recorrido_institucional_propuesto.{typ}')],check=True)
doc=Document();sec=doc.sections[0];sec.page_width=Inches(8.5);sec.page_height=Inches(11);sec.top_margin=sec.bottom_margin=Inches(.8);sec.left_margin=sec.right_margin=Inches(.85)
for name in ['Normal','Title','Heading 1','Heading 2']:
 s=doc.styles[name];s.font.name='Liberation Sans';s.font.color.rgb=RGBColor(0,0,0)
 if s.element.pPr is not None:
  for x in list(s.element.pPr.findall(qn('w:pBdr'))):s.element.pPr.remove(x)
doc.styles['Normal'].font.size=Pt(11);doc.styles['Normal'].paragraph_format.line_spacing=1.12;doc.styles['Normal'].paragraph_format.space_after=Pt(7)
doc.styles['Title'].font.size=Pt(22);doc.styles['Heading 1'].font.size=Pt(15);doc.styles['Heading 2'].font.size=Pt(12)
doc.core_properties.author='Ricardo Alfonso Graffe Garcia';doc.core_properties.title='Perfiles funcionales e historias de información'
ideals=['HU01-H003','HU01-H006','HU01-H011','HU01-H017','HU01-H021']
for i,(a,ideal)in enumerate(zip(h['perfiles_analiticos'],ideals)):
 if i:doc.add_page_break()
 doc.add_paragraph('Perfiles funcionales e historias de información' if i==0 else 'Perfiles funcionales',style='Title')
 doc.add_paragraph('Anexo visual de Evidencia 1 · Ricardo Alfonso Graffe Garcia · Revisión 1.2')
 doc.add_paragraph(a['nombre'],style='Heading 1')
 doc.add_paragraph(f"Voz {a['entrevistas'][0]} · Perfil {a['id']} · Actor {a['actores'][0]}")
 quote=next(q for q in tr['citas']if q['entrevista']==a['entrevistas'][0])
 p=doc.add_paragraph();r=p.add_run('«'+quote['cita']+'»');r.italic=True;p.add_run(' ('+quote['parrafo']+').')
 doc.add_paragraph('Qué hace y qué permite decidir',style='Heading 2');doc.add_paragraph(a['patron'])
 doc.add_paragraph('Capacidades que el diseño debe preservar',style='Heading 2');doc.add_paragraph(' '.join(a['capacidades']))
 st=next(x for x in h['historias']if x['id']==ideal)
 doc.add_paragraph('Historia ideal por contrastar',style='Heading 2');doc.add_paragraph(st['formulacion']);doc.add_paragraph(f"{st['id']} · {st['perfil_metadatos']} · Necesidad "+', '.join(st['necesidades']))
 doc.add_paragraph('Qué comprobar antes de avanzar',style='Heading 2');k=st['criterios'][0];doc.add_paragraph('Dado que '+k['dado']+', cuando '+k['cuando']+', entonces '+k['entonces']+'.')
 doc.add_paragraph('Límite y caso contrario',style='Heading 2');doc.add_paragraph(a['contraejemplo_y_limite']);doc.add_paragraph(' '.join(st['restricciones']))
 doc.add_paragraph('Fuente: HU01 1.1 y corpus 1.0. Síntesis funcional de una voz, sin biografía añadida, aceptación de producto o representatividad. Ficha completa y evidencias en perfiles_y_sintesis.md y fichas_historias.md.')
doc.add_page_break();doc.add_paragraph('Recorrido institucional por acreditar',style='Title');doc.add_paragraph('Propuesta de organización del encargo · No describe una cadena observada entre las entrevistas')
doc.add_picture(str(E/'recorrido_institucional_propuesto.png'),width=Inches(6.65))
doc.add_paragraph('Todas las flechas son conexiones propuestas. El origen SSC y la competencia para autorizar cambios requieren documentación. La coordinación de significados no confiere automáticamente autoridad sobre cada fuente.')
doc.add_paragraph('Cómo leerlo',style='Heading 2');doc.add_paragraph('El productor conserva el original; coordinación acuerda criterios; desarrollo prepara derivados; la persona usuaria decide y señala dudas. La revisión de una incidencia puede terminar en aclaración, rechazo, pendiente o incorporación autorizada. Una corrección genera nueva versión y revisión de salidas afectadas. No se atribuye a una unidad concreta una competencia no acreditada.')
doc.add_paragraph('El relato E01 sólo reconstruye la petición, revisión de una copia, aclaración y devolución. No comprueba captura SSC, transferencia a ADIP ni actualización de la fuente. Los cinco mapas y cuatro modelos documentales permanecen en P01 y D01.')
doc.save(E/'Anexo_visual_perfiles_y_recorrido_v1_2.docx')
p=E/'perfiles_y_sintesis.md';p.write_text(p.read_text()+'\n## Consulta visual\n\nEl [anexo visual](Anexo_visual_perfiles_y_recorrido_v1_2.pdf) presenta cinco perfiles, sus voces, capacidades, historias y pruebas futuras.\n')
p=E/'procesos_y_gobernanza.md';p.write_text(p.read_text()+'\n## Diagrama de responsabilidades propuestas\n\n![Recorrido institucional propuesto con origen y autoridad por acreditar](recorrido_institucional_propuesto.png)\n\n[Versión vectorial](recorrido_institucional_propuesto.svg). Todas las relaciones del diagrama son propuestas, sin confundirlas con evidencia del proceso institucional vigente.\n')
print('Atlas y diagrama creados')
