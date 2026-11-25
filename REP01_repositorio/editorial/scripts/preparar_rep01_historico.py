from pathlib import Path
import json, hashlib, re, shutil, subprocess, datetime, html

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'trabajo/REP01_insumos_v1'
OUT=ROOT/'entrega'
REPO=OUT/'REP01_repositorio'
def read(p): return json.loads(p.read_text())
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(rel,s):
 p=REPO/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.strip()+'\n')

sources={k:read(REPO/v) for k,v in {
 'C':'55_libro_comun_v1_3.json','S':'63_sintesis_transversal_v1_1.json',
 'P':'67_procesos_descritos_v1_1.json','D':'72_contraste_documental_v1_1.json',
 'A':'76_actores_y_preferencias_v1_1.json','N':'82_necesidades_v1_1.json',
 'H':'88_historias_y_objetos_v1_1.json','T':'93_diseno_y_fundamentos_v1_1.json'}.items()}
canon={}
for p in sorted((REPO/'analisis/insumos').glob('E0*_corpus_analisis_v1.json')):
 canon.update({x['id']:x for x in read(p)['parrafos']})

# Cotejo de las entradas; no equivale a lectura semántica.
manifest=read(BASE/'manifest.json')
integridad=[]
for x in manifest['archivos']:
 p=BASE/x['ruta'];integridad.append({'ruta':x['ruta'],'bytes_ok':p.stat().st_size==x['bytes'],'sha256_ok':sha(p)==x['sha256']})
assert all(x['bytes_ok'] and x['sha256_ok'] for x in integridad)
dump(REPO/'editorial/controles/integridad_insumos.json',{'archivos':len(integridad),'resultado':'COINCIDEN','detalle':integridad,'limite':'Lectura de bytes y cotejo, sin acreditar comprensión del contenido.'})

write('LEEME.md','''
# REP01 · Decidir con información suficiente

Versión para revisión editorial, sin publicación ni licencia abierta del corpus.

Pregunta: ¿qué debe conservar una organización de información territorial para ayudar a decidir sin borrar diferencias de significado, responsabilidad y ocasión?

El manuscrito argumenta que hacer recuperables significado, respaldo y límites de una decisión antecede a elegir una plataforma. Compara cinco relatos: revisión pública, investigación, coordinación cultural, mercería y salida personal. Los deseos ideales coexisten con prácticas suficientes. El contraste documental tiene cuatro modelos parciales, sin fuentes directamente atribuibles a los episodios ni divergencias formalmente demostradas.

## Empezar a leer

El manuscrito editable es `../REP01_reporte_v1.md`. Junto al ZIP se entregan `REP01_trazabilidad_v1.json` y `REP01_control_editorial.json`. Manténgalos al mismo nivel que esta carpeta al extraer. La trazabilidad y el control quedan fuera del inventario para evitar ciclos de huellas.

1. Leer el manuscrito y volver a la [guía por sección](editorial/registros/guia_por_seccion.md).
2. Para un literal, abrir `corpus/E0x/E0x_texto_con_localizadores.txt`; el párrafo conserva su numeración. La pregunta y las correcciones están en la misma entrevista. Para auditoría de voz y offsets usar `analisis/insumos/` y `analisis/recodificacion/`.
3. Para derivaciones, seguir necesidad → historia → metadatos/objeto en los documentos 82 y 88; el [índice inverso](editorial/registros/indice_inverso.json) permite ir del párrafo al reporte y a las necesidades/propuestas.
4. Para límites administrativos, metodológicos y de diseño, consultar [incidencias](editorial/registros/incidencias_metodologicas.md) y [agenda](editorial/registros/agenda_pendientes.md).

## Mapa de carpetas

| Ruta | Función |
|---|---|
| `corpus/` | Cinco transcripciones DOCX y vistas canónicas TXT/JSON sin modificar. |
| `analisis/insumos/` | Párrafos, voces, turnos y localizadores fuente. |
| `analisis/libro_comun/`, `analisis/recodificacion/` | Linaje del libro y aplicaciones preferidas, segmentos y memos. |
| `analisis/sintesis/`, `analisis/procesos/`, `analisis/documental/` | Síntesis, cinco procesos completos y cuatro modelos documentales parciales. |
| `analisis/actores/`, `analisis/necesidades/`, `analisis/historias/` | Mapa ampliado, necesidades, historias, metadatos y payloads de objetos locales. |
| `analisis/diseno/`, `analisis/referencias/` | Fundamentos, arquitectura, contratos, representaciones, candidatos y referencia GeoInsights. |
| `registro/` | Prompts/entradas de análisis y salidas iniciales con función de linaje. No prompts de desarrollo de entrevistas. |
| `editorial/` | Fuentes de encargo, figuras nuevas, controles y registro efectivo de esta integración. |
| Archivos 11, 24, 55, 63, 67, 72, 76, 82, 88, 93 | Lectura humana e instrumentos; las versiones preferidas se conservan explícitas. |

## Versiones y conservación

Corpus 1.0; libro 1.3; R01/R02 1.3, R03 1.2, R04/R05 1.1; S01/P01/D01/ACT01/N01/HU01/T01 revisadas 1.1. Los objetos internos pueden conservar sus propias versiones: no se cambian todos a la versión de su paquete. La base curada se copió: contiene 482 archivos; el catálogo describe 446 registros de procedencia. Los archivos permanecen idénticos salvo este LEEME de entrada, sustituido por la guía final. El catálogo original conserva la procedencia de sus siete adaptaciones históricas de rutas humanas. No se reescriben objetos ni sus payloads.

`manifest.json` inventaría todos los archivos de esta raíz salvo sí mismo. No incluye huellas del manuscrito, trazabilidad o control externos. Para cotejar: leer bytes y SHA-256 de cada ruta; ejecutar el validador suministrado con el directorio original de insumos, manuscrito y trazabilidad externos y `--repositorio` apuntando aquí. El script editorial adicional comprueba navegación local, citas/offsets, objetos y archivos. Los scripts históricos requieren sus entradas y rutas originales: no se promete regeneración idéntica de revisiones.

## Acceso y límites

El corpus se distribuye para revisión del ejercicio; no se otorga permiso abierto de reutilización. MIT corresponde al código GeoInsights, no a entrevistas o registros personales. Los acuerdos textuales de participación no acreditan firmas, audio ni trabajo de campo; fechas de entrevista NO_CONSIGNADA. Las transcripciones se generaron con IA; se preservan y se declara su alcance en el manuscrito. La revisión humana independiente y la comprobación efectiva de diez páginas permanecen pendientes.
''')
write('editorial/LEEME.md','''# Integración editorial REP01
Fuentes registra las entradas de encargo y sus procedencias; figuras contiene DOT editable y SVG/PNG exportados; controles contiene comprobaciones efectivamente ejecutadas; registros explica lectura, tesis, decisiones, incidencias y pendientes; scripts conserva los controles de esta etapa. Ninguna carpeta acredita ejecución de los productos candidatos.
''')
write('editorial/fuentes/LEEME.md','''# Fuentes de la integración
Copias del registro de entradas preferidas, catálogo de la base, instrucciones, matriz completa de 208 requisitos y transcripción operativa de Canvas/rúbrica/feedback. La nota JANUS conserva el alcance de la consulta previa; las reconsultas REP01 se registran aparte. No se han traído archivos de otras conversaciones ni prompts de desarrollo de entrevistas. El catálogo describe la base recibida y no constituye inventario final.
''')
write('editorial/figuras/LEEME.md','''# Figuras sintéticas de REP01
Cada figura se entrega en DOT editable, SVG y PNG. El manuscrito usa PNG para facilitar la maquetación; SVG permite redimensionar sin perder texto. La trazabilidad identifica nodos comprimidos y relaciones conservadas. Revisión asistida visual y de contenido registrada en controles; legibilidad efectiva en el documento maquetado permanece pendiente. Los cinco mapas completos y modelos documentales originales se conservan en sus carpetas de análisis.
''')
write('editorial/controles/LEEME.md','''# Controles ejecutados
Integridad de las 495 entradas, literalidad/offsets de recodificación y ejemplos, navegación editorial y objetos locales se comprueban por separado. El control editorial principal se entrega fuera del ZIP y registra las huellas del manuscrito/trazabilidad y del validador. Ningún resultado equivale a revisión humana independiente, validación de utilidad, bibliografía exhaustiva o diez páginas. Los controles históricos no se presentan como reejecutados en esta etapa.
''')
write('editorial/registros/LEEME.md','''# Registros de análisis e integración
La guía por sección y el índice inverso permiten pasar del manuscrito al párrafo y del párrafo a necesidades e historias. La lectura identifica alcances reales, separando consulta de contenido y cotejo de integridad. Las incidencias no modifican las fuentes. El registro de integración es un memo de lo realizado; no una exportación completa de chats ni un consentimiento.
''')
write('editorial/scripts/LEEME.md','''# Scripts de esta etapa
`validar_reporte.py` es copia idéntica del control suministrado. Requiere la raíz de insumos original, manuscrito y trazabilidad externos y la carpeta final. `controles_complementarios.py` comprueba la navegación editorial, literalidad de segmentos/ejemplos y resolución de payloads de historias. No implementan Carto-Visor ni ejecutan lentes territoriales. Los scripts de etapas previas conservan carácter histórico y dependencias originales.
''')

agenda=['Precisar límites, usuarios, instituciones y operaciones cubiertos por la ausencia de plataforma afirmada.',
 'Recibir las dos capas e identificar versión, linaje, responsable, frecuencia y acceso.',
 'Completar vigencia de disposiciones locales y régimen temporal aplicable, sin extender el control nacional a los casos.',
 'Cotejar conjunto, tabla, croquis, copia y aclaración de E01 si se aportan.',
 'Cotejar pauta, acuerdos, notas, unidades comparadas y versiones de E02.',
 'Cotejar acuerdos de fechas, invitación, notas y cierre de E03.',
 'Establecer si se conservan soportes y acuerdos propios de compra/orden de E04.',
 'Cotejar mensajes y horario histórico de E05 solo si son aportados.',
 'Distinguir falta de capa, semántica, coordinación y vigencia como explicaciones posibles.',
 'Revisión humana independiente de paráfrasis, aplicabilidad y explicaciones alternativas.']
write('editorial/registros/agenda_pendientes.md','# Agenda documental y de diseño\n\nLas diez cuestiones D01 siguen pendientes; se presentan en el mismo orden del registro `72_contraste_documental_v1_1.json#/cuestiones_pendientes`.\n\n'+'\n'.join(f'{i+1}. {s}'for i,s in enumerate(agenda))+'''

La posición de los 46 actores ante homologación permanece NO_RECABADA; las capacidades operativas no la sustituyen. Ningún contacto, nueva entrevista o comprobación de utilidad se ejecutó en REP01.

Antes de seleccionar implementación: acordar pertinencia y mantenimiento, disponer de soportes/permiso y ensayar criterios con roles pertinentes. Si bastan las prácticas actuales, conservarlas. SCAN, potencia/escalamiento y ABM no se aplican a productos básicos; TDA requiere condiciones adicionales. Las propuestas no se convierten en resultados al pasar un validador.

Maquetación: definir Word/PDF, ubicar figuras sin reducir tipografía, comprobar tamaño y saltos, separar portada/referencias/declaración y contar páginas reales del cuerpo. Estado PENDIENTE_MAQUETACION.
''')
write('editorial/registros/incidencias_metodologicas.md','''
# Incidencias metodológicas para revisión

1. **Generación y grabación. ABIERTA para revisión del usuario.** Las instrucciones REP01 exigen declarar generación de transcripciones con IA. Los corpus contienen invitación a grabar y aceptación: E01-P004/P005; E02-P005/P006; E03-P004/P005; E04-P005/P006; E05-P004/P005. No se recibieron audios ni registros firmados; las frases se conservan como contenido textual y no como acreditación externa. Ubicación editorial: S001 y declaración de IA.
2. **Fecha y guion. ABIERTA administrativa.** `24_registro_corpus.json#/entrevistas` consigna fechas NO_CONSIGNADA; solo E01 muestra guion 1.0 en encabezado. `11_guiones_entrevistas.json#/estado` conserva la fórmula histórica «aplicación pendiente». Se consulta como diseño del instrumento, no como certificación de aplicación humana o estado actual del corpus. No se reescribe.
3. **Secuencia y validación humana. ABIERTA.** Libro R018 pide revisión/pilotaje humano antes de congelar; se continuó mediante adopción operativa asistida con revisión independiente pendiente. Ubicaciones: `55_libro_comun_v1_3.json#/reglas_recodificacion/17`, `24_protocolo_analisis.md`, metadatos de R01–R05. El manuscrito relata la secuencia efectiva sin declararla validación humana ni conformidad JANUS integral.
4. **Rótulos históricos dentro de versiones preferidas. RESUELTA editorialmente.** R01 balance y M012–M018 retienen libro 1.1; R02 balance/M017 conserva referencias a 1.2 y tareas siguientes; R03-M017 refiere copia 1.1; R04-M015 conserva un título histórico de laguna. Se priorizan metadatos y linaje actuales; el contenido histórico se preserva, conforme S01-D012. No son contradicciones entre participantes.
5. **Aplicabilidad documental. ABIERTA.** D01 tiene cuatro modelos parciales, cero fuentes atribuibles directamente a los episodios y cero divergencias demostradas. La cobertura de PRO01/PRO02/PRO08 es parcial; semejanza con PAOT no identifica E01. Las diez preguntas no se cierran por presencia de diagramas.
6. **Fundamento geoestadístico. RESUELTA editorialmente.** T01-G007 conserva referencia a F014 como texto indexado. REP01 usa F041, §6.2 del documento INEGI de 2021, leído de nuevo, para función censal y límites convencionales. No se cambia T01 ni se atribuye inspección vectorial.
7. **Registros de chats/contexto. ABIERTA.** Prompts de análisis y salidas recibidas se conservan; faltan exportaciones completas de todos los intercambios, registros verificables de configuración y algunos archivos internos citados por las etapas. El memo REP01 no los reconstruye. CTX02–CTX05 y JAN04 son parciales o pendientes según alcance.
8. **Licencia y privacidad. ABIERTA.** Anonimización funcional observable; no certificación de anonimato irreversible, examen jurídico ni permiso abierto del corpus. Datos del autor son los autorizados. No se inventa registro anterior de revisión de privacidad; el examen editorial de esta etapa tiene alcance acotado.
''')
write('editorial/registros/memo_integracion.md','''
# Memo efectivo de integración REP01

Tesis fijada antes de redactar: la utilidad depende de poder recuperar significado, respaldo, responsabilidad y ocasión de una decisión; la centralización es una posibilidad a contrastar. Evidencias: conservación deliberada E01; comparabilidad E02; confirmación distribuida E03. Contraejemplos: reposición satisfecha E04, apertura deliberada E05 y herramientas suficientes en E02/E03. Límites: corpus generado con IA, muestra funcional, ausencia de documentos de episodios y aceptación de productos.

Se leyó la instrucción externa completa y se extrajo el ZIP. Se cotejaron 495 entradas por tamaño/huella, además del catálogo de 446 archivos curados. Se leyeron las cinco entrevistas completas en sus vistas de párrafos, preguntas y correcciones; se volvió a los pasajes citados. Se consultaron todos los requisitos y sus pruebas, versiones preferidas y desarrollo técnico. No se atribuye lectura semántica a cada byte cotejado: ver `lectura_efectiva.json`.

Se trabajó en copia de la base. El manuscrito integra análisis existente sin recodificar ni crear intervenciones de entrevista. Se crearon tres figuras de síntesis, navegación por sección, índice inverso y registros editoriales. Los scripts nuevos verifican objetos; los históricos se preservan con sus limitaciones. No se implementó Carto-Visor ni se publicó repositorio.

Las consultas externas de esta etapa se limitaron a fuentes metodológicas primarias ya registradas: Openshaw, Harley, INEGI, FAIR, JANUS, Mapper y ODD. Se registraron pasajes consultados y fallo inicial del DOI JANUS antes de recuperar PDF. No se investigaron nuevas necesidades ni se añadieron voces.

Herramientas efectivas: Codex/LLM para integración y escritura; Python para JSON, cotejo, inventario y ZIP; Graphviz para DOT→SVG/PNG; lector de imágenes para inspección asistida. Modelo de ejecución identificable y parámetros no disponibles: null. No se conservaron ni reconstruyeron razonamientos internos o chats como si fueran exportaciones originales.

Revisión futura: usuario y revisores humanos independientes deben valorar las formulaciones señaladas y pertinencia semántica; maquetar y medir diez páginas efectivas. La estimación de páginas es presupuesto editorial, no medida de PDF.
''')

# Sustituir localizadores breves por enlaces exactos al corpus, conservando los literales.
mdp=OUT/'REP01_reporte_v1.md';md=mdp.read_text()
for e,p in [('E01','065'),('E03','182'),('E02','083'),('E01','137'),('E02','148'),('E04','152'),('E05','119')]:
 md=md.replace(f'({e}-P{p})',f'([{e}-P{p}](REP01_repositorio/corpus/{e}/{e}_texto_con_localizadores.txt))')
md=md.replace('Coordinación del ejercicio, asistida por LLM. (s. f.). *D01: Contraste documental y revisión del encargo*','*D01: Contraste documental y revisión del encargo*. (s. f.)')
mdp.write_text(md)

print('Preparada base editorial',len(list(REPO.rglob('*'))),'objetos de archivo/carpeta')
