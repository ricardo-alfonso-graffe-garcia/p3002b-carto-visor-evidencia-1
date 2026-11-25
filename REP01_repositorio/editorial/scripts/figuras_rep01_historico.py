from pathlib import Path
import subprocess,json
root=Path(__file__).resolve().parent/'entrega/REP01_repositorio/editorial/figuras'
head='''digraph G {
graph [bgcolor="white", pad="0.25", nodesep="0.30", ranksep="0.42", fontname="DejaVu Sans", fontsize=16];
node [shape=box, style="rounded,filled", fillcolor="#edf4f6", color="#507084", penwidth=1.3, fontname="DejaVu Sans", fontsize=15, margin="0.18,0.12"];
edge [color="#435a69", fontname="DejaVu Sans", fontsize=12, arrowsize=0.8];
'''
figs={
'REP01-F001':head+'''
rankdir=TB;
a [label="1 · Recibir y delimitar\\nTres registros para preparar visitas"];
b [label="2 · Contrastar referencias\\nTabla, antecedentes, mapa y croquis"];
c [label="3 · Aclarar el tercer sitio\\nPregunta por la solicitante;\\nrespuesta del equipo del recorrido"];
d [label="4 · Decidir y preparar la copia\\nMismo espacio: conservar identificador y punto;\\nprecisar el acceso utilizado"];
e [label="5 · Devolver y explicar\\nResponder por qué cambió la calle;\\nfin de la revisión de esta voz"];
f [label="Límite\\nOtro acceso y uso posterior no comprobados", fillcolor="#fff4dd", color="#ad8747"];
a -> b -> c -> d -> e;
e -> f [style=dashed, arrowhead=none, label="alcance"];
}
''',
'REP01-F002':head+'''
rankdir=TB;
a [label="Registro territorial\\nEntender el último cambio\\nE01-P137 · N01-N004"];
b [label="Historia de retomar\\nLugar, revisión, respaldo y duda\\nHU01-H003 · M003"];
c [label="Comprobación futura\\nExplicar y decidir si consultar\\nHU01-K004",fillcolor="#fff4dd"];
d [label="Investigación de compras\\nSegunda ocasión contrastante\\nE02-P143 · N01-N009"];
e [label="Historia de contrastar\\nOcasión, propósito y procedencia\\nHU01-H006 · M006"];
f [label="Comprobación futura\\nPrecisar o reducir una afirmación\\nHU01-K008",fillcolor="#fff4dd"];
{rank=same; a; d;}
{rank=same; b; e;}
{rank=same; c; f;}
a -> b -> c;
d -> e -> f;
}
''',
'REP01-F003':head+'''
rankdir=TB;
a [label="Extracción autorizada\\nOriginal, permiso y procedencia"];
b [label="Unificación por contrato\\nEntidad, significado y desconocidos"];
c [label="Agregación optativa\\nPartición, pertenencia y denominador"];
d [label="Construcción\\nRelaciones y vistas derivadas"];
e [label="Análisis interpretativo\\nCasos, respaldo y límites"];
f [label="Productos candidatos\\nExpediente · Cuaderno · Memoria"];
g [label="Revisión de incidencia\\nConservar fuente y motivo",fillcolor="#fff4dd"];
a -> b;
b -> c [label="si la pregunta lo requiere"];
b -> d [label="por caso", color="#246c80"];
c -> d;
d -> e -> f;
e -> g [style=dashed,label="revisar contrato o insumo"];
g -> b [style=dashed,label="nueva versión propuesta"];
}
'''}
for name,txt in figs.items():
 (root/(name+'.dot')).write_text(txt)
 for fmt in ['svg','png']:
  subprocess.run(['dot','-T'+fmt,'-Gdpi=150',str(root/(name+'.dot')),'-o',str(root/(name+'.'+fmt))],check=True)
print('Tres fuentes DOT y seis exportaciones generadas.')
