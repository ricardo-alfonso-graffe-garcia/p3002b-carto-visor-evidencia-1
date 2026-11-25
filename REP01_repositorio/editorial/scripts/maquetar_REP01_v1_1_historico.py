from pathlib import Path
import re,json
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.section import WD_SECTION_START
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT=Path.cwd();WORK=ROOT/'tmp/review/REP01_revision_v1_1';md=(WORK/'REP01_reporte_v1_1.md').read_text()
doc=Document();doc.core_properties.author='Ricardo Alfonso Graffe Garcia';doc.core_properties.title='Procesos actores y necesidades de información territorial en cinco relatos';doc.core_properties.subject='P3002B Evidencia 1';doc.core_properties.comments=''
styles=doc.styles
for name in ['Normal','Title','Heading 1','Heading 2','Caption','List Bullet']:
    s=styles[name];s.font.name='Liberation Serif';s.font.color.rgb=RGBColor(0,0,0)
normal=styles['Normal'];normal.font.size=Pt(11.5);normal.paragraph_format.line_spacing=1.10;normal.paragraph_format.space_after=Pt(5)
for n,size in [('Heading 1',13),('Heading 2',12)]:
    s=styles[n];s.font.size=Pt(size);s.font.bold=True;s.paragraph_format.space_before=Pt(9);s.paragraph_format.space_after=Pt(5);s.paragraph_format.keep_with_next=True
styles['Title'].font.size=Pt(23);styles['Title'].font.bold=True
styles['Caption'].font.size=Pt(9.5);styles['Caption'].font.italic=True;styles['Caption'].font.bold=False;styles['Caption'].paragraph_format.space_after=Pt(7)

def layout(sec):
    sec.page_width=Inches(8.5);sec.page_height=Inches(11);sec.top_margin=sec.bottom_margin=Inches(.78);sec.left_margin=sec.right_margin=Inches(.8);sec.header_distance=sec.footer_distance=Inches(.3)
for sec in doc.sections:layout(sec)

def field(p,name):
    r=p.add_run();el=OxmlElement('w:fldSimple');el.set(qn('w:instr'),name);r._r.addnext(el)
def newsection(label):
    sec=doc.add_section(WD_SECTION_START.NEW_PAGE);layout(sec)
    sec.header.is_linked_to_previous=False;sec.footer.is_linked_to_previous=False
    h=sec.header.paragraphs[0];h.text='P3002B  ·  Evidencia 1';h.style='Normal'
    for r in h.runs:r.font.size=Pt(9);r.font.color.rgb=RGBColor(0,0,0)
    f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.RIGHT;f.add_run(label+'  ·  ');field(f,'PAGE')
    for r in f.runs:r.font.size=Pt(9)
    pnum=OxmlElement('w:pgNumType');pnum.set(qn('w:start'),'1');sec._sectPr.append(pnum)
    return sec

token=re.compile(r'(\[[^\]]+\]\([^)]+\)|\*\*[^*]+\*\*|`[^`]+`|\*[^*]+\*)')
def hyperlink(p,label,target):
    h=OxmlElement('w:hyperlink');h.set(qn('r:id'),p.part.relate_to(target,RT.HYPERLINK,is_external=True))
    rr=OxmlElement('w:r');rp=OxmlElement('w:rPr');color=OxmlElement('w:color');color.set(qn('w:val'),'205476');rp.append(color);rr.append(rp)
    t=OxmlElement('w:t');t.text=label;rr.append(t);h.append(rr);p._p.append(h)
def inline(p,text):
    for t in token.split(text):
        if not t:continue
        if t.startswith('[')and']('in t:
            label,target=re.match(r'\[([^\]]+)\]\(([^)]+)\)',t).groups();hyperlink(p,label,target)
        elif t.startswith('**'):p.add_run(t[2:-2]).bold=True
        elif t.startswith('*'):p.add_run(t[1:-1]).italic=True
        elif t.startswith('`'):
            r=p.add_run(t[1:-1]);r.font.name='Liberation Mono';r.font.size=Pt(9)
        else:p.add_run(t)

def table(lines,number):
    rows=[[c.strip()for c in line.strip().strip('|').split('|')]for line in lines]
    rows=[rows[0]]+rows[2:];t=doc.add_table(rows=1,cols=len(rows[0]));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
    widths={1:[1.8,2.8,2.3],2:[1.15,2.85,2.9],3:[1.7,2.7,2.5],4:[1.55,2.1,3.25],5:[1.45,2.75,2.7]}[number]
    # Total width is 6.9 inches, matching Letter minus two .8-inch margins.
    for col,w in zip(t.columns,widths):col.width=Inches(w)
    for ri,row in enumerate(rows):
        cells=t.rows[0].cells if ri==0 else t.add_row().cells
        for ci,(cell,txt)in enumerate(zip(cells,row)):
            cell.width=Inches(widths[ci]);cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            p=cell.paragraphs[0];inline(p,txt);p.paragraph_format.space_after=Pt(2);p.paragraph_format.space_before=Pt(2);p.paragraph_format.line_spacing=1.05
            for r in p.runs:r.font.name='Liberation Sans';r.font.size=Pt(9.7);r.font.bold=ri==0
            pr=cell._tc.get_or_add_tcPr();borders=OxmlElement('w:tcBorders')
            for edge in ['top','left','bottom','right']:
                el=OxmlElement('w:'+edge);el.set(qn('w:val'),'single');el.set(qn('w:sz'),'4');el.set(qn('w:color'),'D9D9D9');borders.append(el)
            pr.append(borders);m=OxmlElement('w:tcMar')
            for edge in ['top','bottom','left','right']:
                el=OxmlElement('w:'+edge);el.set(qn('w:w'),'65'if edge in ['top','bottom']else'85');el.set(qn('w:type'),'dxa');m.append(el)
            pr.append(m)
            if ri==0:
                shading=OxmlElement('w:shd');shading.set(qn('w:fill'),'E4ECF1');pr.append(shading)
        trpr=t.rows[ri]._tr.get_or_add_trPr();no=OxmlElement('w:cantSplit');trpr.append(no)
        if ri==0:trpr.append(OxmlElement('w:tblHeader'))

def addblocks(text):
    lines=text.splitlines();i=0;table_no=0
    while i<len(lines):
        line=lines[i].strip()
        if not line or line.startswith('<!--')or line.startswith('<a '):i+=1;continue
        if line.startswith('|'):
            arr=[]
            while i<len(lines)and lines[i].strip().startswith('|'):arr.append(lines[i]);i+=1
            table_no+=1;table(arr,table_no);continue
        if line.startswith('!['):
            alt,target=re.match(r'!\[([^\]]+)\]\(([^)]+)\)',line).groups();p=doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.keep_with_next=True
            width=6.65 if 'F001'in target or 'F002'in target else 5.1
            run=p.add_run();run.add_picture(str(WORK/target),width=Inches(width));run._r.xpath('.//wp:docPr')[0].set('descr',alt)
            i+=1;continue
        if line.startswith('## '):
            doc.add_paragraph(line[3:],style='Heading 1');i+=1;continue
        if line.startswith('# '):
            doc.add_paragraph(line[2:],style='Title');i+=1;continue
        if line.startswith('*Figura')or line.startswith('*Tabla'):
            p=doc.add_paragraph(style='Caption');inline(p,line.strip('*'));i+=1;continue
        isbullet=line.startswith('- ')
        p=doc.add_paragraph();inline(p,line[2:]if isbullet else line)
        if isbullet:
            p.paragraph_format.left_indent=Inches(.15);p.paragraph_format.first_line_indent=Inches(-.15)
        i+=1

cover=md.split('<!-- PORTADA_INICIO -->')[1].split('<!-- PORTADA_FIN -->')[0]
for line in cover.splitlines():
    if not line.strip():continue
    p=doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.LEFT
    if line.startswith('# '):
        p.style='Title';p.paragraph_format.space_before=Pt(90);p.paragraph_format.space_after=Pt(35);p.add_run(line[2:])
    else:
        inline(p,line.strip());p.paragraph_format.space_after=Pt(9)
newsection('Cuerpo')
body=md.split('<!-- CUERPO_INICIO -->')[1].split('<!-- CUERPO_FIN -->')[0];addblocks(body)
newsection('Referencias');addblocks(md.split('<!-- REFERENCIAS_INICIO -->')[1].split('<!-- REFERENCIAS_FIN -->')[0])
newsection('Anexo metodológico');addblocks(md.split('<!-- DECLARACION_IA_INICIO -->')[1].split('<!-- DECLARACION_IA_FIN -->')[0])

# Quitar bordes de párrafo heredados de la plantilla, incluida la regla azul del título.
for style in doc.styles:
    if style.element.pPr is not None:
        for border in list(style.element.pPr.findall(qn('w:pBdr'))):style.element.pPr.remove(border)
for p in doc.paragraphs:
    if p._p.pPr is not None:
        for border in list(p._p.pPr.findall(qn('w:pBdr'))):p._p.pPr.remove(border)
out=WORK/'P3002B_Evidencia1_Ricardo_Graffe.docx';doc.save(out)
print(out)
