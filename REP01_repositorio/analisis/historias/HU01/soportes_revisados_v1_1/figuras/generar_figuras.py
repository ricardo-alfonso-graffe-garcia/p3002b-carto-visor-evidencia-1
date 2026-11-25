import argparse,json,pathlib,textwrap,html
ap=argparse.ArgumentParser();ap.add_argument('--resultado',required=True);ap.add_argument('--salida',required=True);a=ap.parse_args();R=json.loads(pathlib.Path(a.resultado).read_text());D=pathlib.Path(a.salida);D.mkdir(parents=True,exist_ok=True)
def esc(s):return html.escape(str(s))
def start(w,h,title,desc):return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{esc(title)}</title><desc>{esc(desc)}</desc><rect width="100%" height="100%" fill="#f3f5f7"/><style>text{{font-family:DejaVu Sans,sans-serif;fill:#142a3b}}.title{{font-weight:bold}}.muted{{fill:#42596a}}</style>']
def text(out,x,y,s,size=18,width=100,fill=None,bold=False):
 lines=textwrap.wrap(s,width=width,break_long_words=False,break_on_hyphens=False) or ['']
 for j,l in enumerate(lines):out.append(f'<text x="{x}" y="{y+j*(size+7)}" font-size="{size}"'+(' class="title"' if bold else '')+(f' style="fill:{fill}"' if fill else '')+f'>{esc(l)}</text>')
 return y+len(lines)*(size+7)
def rect(out,x,y,w,h,fill='#fff',stroke='#cfdae1'):out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}"/>')
o=start(1320,1800,'Cinco perfiles funcionales de HU01','Síntesis de actividad, capacidades y límites. Sin arquetipos representativos ni rostros inventados.')
text(o,45,56,'Perfiles para comprender decisiones',32,bold=True);text(o,45,94,'Cinco voces conservadas · perfiles funcionales · revisión humana independiente pendiente',19)
shorts=[('Revisar antes de cambiar','Distinguir el espacio, su acceso y un posible traslado.','No estuvo en campo ni organiza visitas; otra lectura no es autorización.','Comparación, pregunta concreta y explicación breve; carpeta ideal no obliga a mapa.'),('Comparar sin borrar diferencias','La unidad y el alcance dependen de la afirmación.','Pocos casos; alternativas incompletas; sin representación de zonas o causa única.','Conversación posterior, esquemas modificables y desconocidos; segunda ocasión por acordar.'),('Construir encuentros con otras personas','Fechas estables permiten participación y sesiones autónomas.','Consulta parcial; no compromete sola espacio/equipo; no conoce impacto total.','Visita pertinente, mediación y comunicación sencilla; acuerdos se revalidan.'),('Reponer con criterio del mostrador','Reponer conocido es distinto de consultar alternativa.','Sin especialización cartográfica; tacto no prueba uso; cantidad sigue limitando.','Muestras en mano, revisión física y relevo autónomo; no inventario digital obligatorio.'),('Acordar y explorar con margen','Ir a mirar y compartir puede funcionar sin compra.','Sin especialización cartográfica; no decide por amistad ni garantiza mesa futura.','Lectura en destino, preguntar y decidir si siguen; notas futuras son opcionales.')]
for i,(p,s) in enumerate(zip(R['perfiles_analiticos'],shorts)):
 y=130+i*315;rect(o,35,y,1250,290);rect(o,52,y+18,96,46,'#dcebf2');text(o,67,y+49,f'E{i+1:02}',23,bold=True)
 text(o,174,y+42,s[0],25,bold=True);text(o,174,y+79,f"{p['id']} · {p['actores'][0]} · PERFIL FUNCIONAL",17)
 yy=text(o,174,y+120,'Decisión: '+s[1],19,width=96)
 yy=text(o,174,yy+8,'Límite: '+s[2],18,width=105)
 text(o,174,yy+8,'Preservar: '+s[3],18,width=105)
text(o,45,1740,'Fuente: cinco conversaciones completas y procesos revisados; entidades HU01 para revisión.',17)
text(o,45,1770,'Las coincidencias entre soportes no convierten las funciones en un usuario representativo.',17)
o.append('</svg>');(D/'perfiles.svg').write_text('\n'.join(o))
o=start(1520,2130,'Del conocimiento necesario a historias y criterios','Cinco casos, prácticas actuales y seis deseos ideales. Las flechas expresan trazabilidad analítica, no cadena de trabajo entre casos.')
text(o,40,55,'Necesidad → historia → criterio e información',30,bold=True)
text(o,40,91,'Ejemplos de los cinco casos y desarrollo de los seis deseos ideales · propuestas de comprobación',18)
sel=[(1,[1,3]),(2,[5,6]),(3,[8,11,12]),(4,[13,17]),(5,[19,21])]
labels={1:'Registro territorial',2:'Investigación de compras',3:'Encuentros culturales',4:'Mercería de barrio',5:'Salida personal'}
for ix,(case,hs) in enumerate(sel):
 y=125+ix*385;rect(o,25,y,1470,365);text(o,45,y+32,f'E{case:02} · {labels[case]}',22,bold=True)
 for j,hn in enumerate(hs):
  h=R['historias'][hn-1];yy=y+55+j*(92 if len(hs)==3 else 137)
  ideal=h['tipo']=='IDEAL_A_CONTRASTAR';bg='#e9f0fb' if ideal else '#e8f3ee';kind='IDEAL' if ideal else 'ACTUAL'
  rect(o,43,yy,335,78,bg);text(o,57,yy+25,kind+' · '+', '.join(h['necesidades']),16,bold=True);text(o,57,yy+50,('Deseo por contrastar' if ideal else 'Práctica a preservar / revisar'),15,width=35)
  o.append(f'<path d="M382 {yy+38} L422 {yy+38}" stroke="#42596a" stroke-width="2"/><path d="M414 {yy+32} L424 {yy+38} L414 {yy+44}" fill="none" stroke="#42596a" stroke-width="2"/>')
  rect(o,430,yy,505,78);text(o,444,yy+24,h['id'],16,bold=True);text(o,444,yy+49,h['titulo'],16,width=49)
  o.append(f'<path d="M940 {yy+38} L974 {yy+38}" stroke="#42596a" stroke-width="2"/><path d="M966 {yy+32} L976 {yy+38} L966 {yy+44}" fill="none" stroke="#42596a" stroke-width="2"/>')
  rect(o,982,yy,490,78,'#f8f3e8');text(o,995,yy+24,'Comprobar: '+', '.join(k['id'] for k in h['criterios']),15,width=52);text(o,995,yy+60,'Información: '+h['perfil_metadatos']+' · 21 campos',15)
 text(o,45,y+347,'Todas las necesidades e historias: tablas/cobertura_necesidades.csv e historias.csv.',15)
text(o,40,2076,'Las flechas son relaciones de derivación. Criterios no ejecutados; no aceptación ni publicación.',17)
text(o,40,2106,'N01-N005 permanece como condición de una petición futura; no fue carencia del episodio.',17)
o.append('</svg>');(D/'recorrido.svg').write_text('\n'.join(o))
