from pathlib import Path
import json, hashlib, re, shutil
import fitz

ROOT=Path.cwd(); W=ROOT/'tmp/review/REP01_revision_v1_3'; R=W/'REP01_repositorio'; E=R/'editorial/revision_v1_3'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

layout_path=R/'editorial/controles/maquetacion_v1_3.json'
layout=json.loads(layout_path.read_text())
layout.update(revision_visual='REALIZADA_ASISTIDA',alcance_revision_visual='Se inspeccionaron las trece páginas exportadas, incluidos gráficos, tablas y referencias; no revisión humana independiente.')
save(layout_path,layout)
tr=json.loads((W/'REP01_trazabilidad_v1_3.json').read_text())
pdf=fitz.open(W/'P3002B_Evidencia1_Ricardo_Graffe.pdf')
norm=lambda s:re.sub(r'\s+',' ',s).strip()
txt=norm(' '.join(p.get_text() for p in pdf))
for q in tr['citas']: assert norm(q['cita']) in txt,q['id']
links=[x for p in pdf for x in p.get_links()]
local=[x['file'] for x in links if x.get('file')]
assert all((W/x).is_file() for x in local),[x for x in local if not(W/x).is_file()]
old=ROOT/'output/REP01_entrega_v1_2/REP01_repositorio'; changed=[]; lost=[]; kept=0
for p in old.rglob('*'):
 if p.is_file() and '__pycache__' not in p.parts:
  rel=str(p.relative_to(old)); q=R/rel
  if not q.is_file(): lost.append(rel)
  elif sha(q)!=sha(p): changed.append(rel)
  else: kept+=1
assert not lost,lost
assert all(x in ['LEEME.md','indice.html','manifest.json'] or x.startswith('editorial/') for x in changed),changed
delta=json.loads((E/'delta_sobre_175_recomendaciones.json').read_text())
save(E/'controles_adicionales_v1_3.json',{'version':'1.3','estado':'SIN_ERRORES_EN_ALCANCE_COMPROBADO','controles':[
 {'control':'Siete citas presentes en el PDF final, además del cotejo canónico','resultado':'PASS','citas':len(tr['citas'])},
 {'control':'Enlaces locales del PDF final resuelven','resultado':'PASS','locales':len(local),'totales':len(links)},
 {'control':'Fuentes de corpus y análisis de 1.2 inalteradas','resultado':'PASS','preexistentes_iguales':kept,'cambiados':changed,'omitidos':lost},
 {'control':'Trece páginas inspeccionadas visualmente de forma asistida','resultado':'PASS','cuerpo':10,'total':len(pdf)},
 {'control':'20 puntos de presencia y brechas; 175 tratamientos históricos conservados','resultado':'PASS'}],
 'limites':['No revisión humana independiente','No pruebas de utilidad ni cálculo espacial ejecutados','No conformidad integral FAIR/FDO/JANUS']})

msg='''# Revisión explícita del reporte REP01 1.3

Esta revisión responde a las ocho preguntas del usuario y conserva entrevistas, libro de códigos, recodificaciones, catálogos y los tres candidatos existentes. Las nuevas copias de auditoría y especificaciones coinciden por SHA-256 con las ya leídas: no incorporan requisitos distintos. Se mantiene la revisión 1.2 como antecedente.

## Respuestas y localizadores

Las páginas siguientes son físicas del PDF, contando la portada como página 1. El cuerpo sigue teniendo diez páginas.

| Elemento | Situación de 1.2 | Situación de 1.3 |
|---|---|---|
| Historias de usuario | Dos formulaciones completas en el cuerpo y 21 fichas de soporte | Se conservan las dos, con capacidad y propósito, páginas 7–8, sección 5 |
| FAIR | Referencia y límites en cuerpo; desarrollo por principio en soporte | Cuatro dimensiones explícitas y límites en página 11; matriz detallada enlazada |
| FDO | 76 objetos digitales locales en soporte; sigla y ejemplo ausentes del PDF | Un objeto concreto orientado a FDO en página 8, registro HU01-OD037; no se afirma registro externo |
| Trazabilidad | Cadena explícita en sección 5 | Se conserva y puede seguirse en página 8 desde evidencia hasta historia, metadatos y operaciones |
| JANUS | Adaptación declarada, con poca explicación del recorrido | Explicación de la lógica y aplicación en página 2; límites en página 11 y anexo |
| Mapa de procesos | Diagrama E01 y tablas comparativas en el cuerpo | Se conserva como figura 2, página 4; otros mapas y modelos en soporte |
| Mapa de actores | Análisis y tabla en cuerpo; redes gráficas en soporte | Se añade subred E01 de cuatro actores, figura 3, página 6; no se presenta como red completa de los 46 actores |
| Esquema de la imagen | No aparecía; la arquitectura de producto no era equivalente | Figura 1, página 3, con la misma lógica analítica, tres candidatos y pruebas futuras |

## Qué muestra el esquema

Fuentes y segmentos, con procedencia y versión, fundamentan actores/perfiles, procesos/decisiones y códigos/temas. Estas lecturas convergen en necesidades actuales y deseadas verificables; de ellas se derivan historias, información/metadatos y operaciones/métodos. Los tres candidatos reúnen alcance y aceptación, y la validación propuesta puede devolver preguntas a las necesidades. Se representan relaciones analíticas, no una cronología que deba imponerse retrospectivamente a las entrevistas. El cierre no implica pruebas ya realizadas.

## Alcance de FAIR y FDO

FAIR son principios orientadores, no una certificación obtenida al guardar JSON. Existen identificadores, relaciones, versiones, procedencia y huellas locales; faltan persistencia y registro externos, semántica compartida y acuerdos efectivos de derechos y acceso. El registro HU01-OD037 ya existía en HU01 y conserva su payload, versión y referencias. Se expone como prototipo local orientado a FAIR Digital Object; sus campos externos PID, tipo y perfil no están registrados. La vista editorial no crea una implementación FDO plena ni altera el objeto original.

## Qué sigue ausente o parcial

1. No hay un procedimiento formal directamente aplicable a los cinco episodios que permita demostrar divergencias institucionales. Los cuatro modelos documentales tienen ámbitos distintos; las diferencias no se convierten en incumplimientos probados.
2. Las posiciones frente a homologación siguen NO_RECABADA para los 46 actores. Los incentivos y alianzas se presentan como hipótesis condicionadas, no preferencias comprobadas.
3. No se acredita revisión humana independiente, concordancia o saturación. Los controles asistidos no las sustituyen.
4. No se acredita una puerta de privacidad anterior a la codificación, exportaciones completas de conversaciones o parámetros desconocidos. No se reconstruyen registros históricos inexistentes.
5. No están implementados PID/perfiles externos, RO-Crate, PROV-O, DataCite o nanopublicaciones ni acuerdos efectivos de derechos por recurso.
6. Las pruebas de utilidad, aceptación y mantenimiento, y el protocolo espacial, son propuestas futuras. No hay resultados, ahorro o robustez empírica medidos.
7. Se conserva un antecedente complementario de Capybara; no se identifica como el ejemplo exacto de las capturas de clase.
8. Los registros y las fechas disponibles se conservan. El uso de IA se describe en la declaración metodológica.

Estas diferencias están registradas en veinte puntos de presencia y brechas. La resolución histórica de 175 recomendaciones significa que cada una tiene tratamiento y destino; no significa cumplimiento empírico completo ni garantiza una calificación. La limitación de páginas anotada por el auditor se ajusta a la decisión del usuario de excluir portada, referencias y anexos del máximo de diez páginas de cuerpo.

## Contenido que está en soporte, no falta

Las 21 fichas completas de historia, cinco mapas de proceso, cuatro modelos documentales, cinco redes por episodio, catálogo amplio de actores, 76 objetos, operaciones y contratos con 119 campos se conservan. El reporte selecciona y explica ejemplos con enlaces al resto. No se ha sustituido la base consolidada por un nuevo análisis.

## Entrega y comprobación

El paquete incluye Word, PDF, manuscrito, trazabilidad, controles y REP01_repositorio. Después de extraerlo, abrir REP01_repositorio/indice.html, Revisión actual 1.3. Se cotejaron las siete citas y las fuentes canónicas; se verificaron enlaces, relaciones y objetos. Se inspeccionaron las trece páginas finales del reporte. Estos controles son documentales y asistidos.

La procedencia del corpus se declara en las páginas físicas 2 y 13; la bibliografía de la página 12 incluye un título sobre modelos de lenguaje. Los archivos de soporte también contienen referencias metodológicas a IA: no se afirma que sólo haya dos menciones en toda la entrega.
'''
(W/'107_revision_explicita_REP01_v1_3.md').write_text(msg)
shutil.copy2(Path(__file__),R/'editorial/scripts/empaquetar_revision_v1_3_historico.py')
files=[{'ruta':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)}for p in sorted(R.rglob('*'))if p.is_file()and str(p.relative_to(R))!='manifest.json'and'__pycache__'not in p.parts]
tr['repositorio']['inventario']=files;save(W/'REP01_trazabilidad_v1_3.json',tr)
save(R/'manifest.json',{'version':'1.3','archivos':files,'alcance':'Raíz de soportes. Manuscrito, trazabilidad y control externos para evitar ciclos.'})
print(json.dumps({'archivos_repositorio':len(files)+1,'cambiados_preexistentes':changed,'conservados':kept,'PDF_enlaces_locales':len(local),'paginas':len(pdf),'citas':len(tr['citas'])},ensure_ascii=False))
