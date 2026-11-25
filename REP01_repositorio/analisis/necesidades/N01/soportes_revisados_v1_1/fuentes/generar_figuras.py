from pathlib import Path
import json,html,textwrap
ROOT=Path(__file__).resolve().parent.parent
DATA=json.loads((ROOT/'fuentes/figuras_datos.json').read_text())
OUT=ROOT/'figuras';OUT.mkdir(exist_ok=True)
W=1500;M=44;PAD=24;LH=27
C={'NECESIDAD_ACTUAL':'#126b73','DESEO_IDEAL':'#6b4ca5','INFERENCIA_ANALITICA_CONDICIONAL':'#9a6015'}
def esc(t):return html.escape(str(t))
def lines(t,width):
 return [l for p in str(t).split('\n') for l in (textwrap.wrap(p,width=width,break_long_words=False,break_on_hyphens=False) or [''])]
def render(case):
 parts=[]
 def text(x,y,t,size=21,color='#203340',weight='400'):
  parts.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{esc(t)}</text>')
 def block(x,y,width,label,t,color='#edf3f6'):
  ls=lines(t,max(15,int((width-2*PAD)/11.9)))
  height=61+LH*len(ls)+PAD
  parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="12" fill="{color}"/>')
  text(x+PAD,y+33,label,18,'#365166','700')
  for i,l in enumerate(ls):text(x+PAD,y+68+LH*i,l)
  return height
 text(M,52,case['entrevista']+' · '+case['titulo'],29,'#142f43','700')
 text(M,89,'De la decisión y lo disponible al conocimiento necesario · N01 1.0',20)
 y=119
 y+=block(M,y,W-2*M,'SUFICIENCIA Y LÍMITE DEL CASO',case['suficiencia'],'#e7f2ed')+36
 for n in case['necesidades']:
  color=C[n['tipo']]
  heading=lines(n['id']+' · '+n['titulo'],95)
  for i,l in enumerate(heading):text(M,y+28+i*34,l,25,color,'700')
  y+=len(heading)*34+16
  text(M,y+20,n['tipo']+' · '+n['estado_actual'],17,color,'700');y+=40
  y+=block(M,y,W-2*M,'DECISIÓN',n['decision'])+16
  col=(W-2*M-24)/2
  ha=block(M,y,col,'INFORMACIÓN ACTUAL',n['informacion_actual'])
  hb=block(M+col+24,y,col,'FALTA / DESEO Y CONDICIONES',n['faltante_o_deseada'],'#f4eff9')
  y+=max(ha,hb)+12
  # Las dos referencias alimentan la formulación, sin imponer una secuencia temporal.
  text(M+20,y+23,'↓',26,color,'700');text(M+col+44,y+23,'↓',26,color,'700');y+=40
  y+=block(M,y,W-2*M,'NECESIDAD DE INFORMACIÓN FORMULADA',n['objeto_informacion'],'#e9f4f5')+16
  y+=block(M,y,W-2*M,'COMPROBACIÓN PROPUESTA · '+n['verificacion'][0]['id'],n['verificacion'][0]['observable'],'#f4f6f8')+18
  p=n['prioridad']
  ls=lines('Prioridad '+p['nivel']+' · ámbito '+p['ambito']+' · '+p['razon'],117)
  for i,l in enumerate(ls):text(M,y+22+i*25,l,18,color)
  y+=len(ls)*25+16
  ids=', '.join(n['evidencias'])
  for l in lines('Evidencias: '+ids,126):text(M,y+19,l,17);y+=23
  y+=28
  parts.append(f'<path d="M{M} {y} H{W-M}" stroke="#c9d5dd"/>');y+=35
 text(M,y+10,'Fuente: N01_necesidades_v1.json. Selección de decisiones; detalle y contraevidencia en JSON/CSV.',17)
 text(M,y+38,'Flechas = relación analítica. No son flujo de producto. Prioridad local; utilidad y aceptación no comprobadas.',17)
 H=int(y+70)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img"><title>{esc(case["titulo"])}</title><desc>{esc(case["suficiencia"])}</desc><rect width="{W}" height="{H}" fill="#ffffff"/>'+''.join(parts)+'</svg>'
 (OUT/(case['entrevista']+'_decisiones_necesidades.svg')).write_text(svg)
 return {'entrevista':case['entrevista'],'ancho':W,'alto':H,'necesidades':[n['id'] for n in case['necesidades']]}
if __name__=='__main__':
 print(json.dumps([render(c) for c in DATA],ensure_ascii=False))
