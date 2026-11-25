# R03 · Recodificación completa de E03

Protocolo de recodificación 1.0 · Corpus 1.0 · Libro operativo 1.2 · 24 de noviembre de 2026

## Encargo y límites

Recodifica los 124 párrafos del participante de E03 con el libro común 1.2. Lee los 196 párrafos canónicos y los 140 turnos para recuperar contexto. No se exige un segmento por párrafo ni conservar cantidades de la primera lectura. Los ejemplos del libro ilustran alcance; no sustituyen releer ni son respuestas esperadas para cada caso.

La entrevista pertenece a una persona que coordina proyectos en una organización de la sociedad civil. No infieras institución exacta, jerarquía, identidad ni información posterior que no declare. El texto canónico es la autoridad y permanece intacto.

Esta tarea continúa la recodificación común con la versión operativa 1.2. Tras revisar R02 se añadió formular y orientar una pregunta de indagación (C063), distinguida de preguntar para aclarar un encargo, nombrar fases o variar método según finalidad. La aplicación E01 fue reabierta para ese cambio y no requirió nuevas asignaciones. Los resultados anteriores no se incluyen en este paquete.

El libro no está congelado. La revisión humana independiente permanece pendiente; esta tarea no la sustituye ni mide concordancia. No adoptes un código por el sector de sus ejemplos: exige la operación definida y conserva los atributos concretos del caso. Tampoco excluyas un código solo por provenir de otro sector.

## Entradas y control de contexto

Descomprime 50_insumos_R03.zip. En R03_insumos_v1 lee LEEME.md, manifest.json, instrucciones_R03.md, libro_comun.json y su vista legible, corpus, objetivos.json, config_validacion.json, validador y nota de pruebas técnicas. El instructivo externo debe coincidir con el interno. Recalcula las huellas si puedes ejecutar Python y registra el control real; si no, indica NO_EJECUTADO.

La fuente es E03_corpus_analisis_v1.json; la vista de texto ayuda a leer. Los ejemplos de otros perfiles dentro del libro son antecedentes del instrumento: no amplían el corpus a analizar ni autorizan atribuir sus necesidades a E03. No se incluyen asignaciones anteriores, correspondencias, salidas del piloto, encargo del cliente, productos deseados o rúbrica. No uses otros chats, recuerdos ni navegación externa.

Si falta un archivo necesario, identifica el faltante y detén las conclusiones dependientes. No inventes ejecución, metadatos o aprobaciones. Modelo y parámetros quedan null si no constan.

## Aplicación y revisión

1. Lee el libro completo, las 18 reglas y las 20 fronteras. Después lee toda E03 antes de segmentar. Revisa también párrafos nominales, cortesías y cierres; pueden contener explicación, límites o valoraciones.
2. Selecciona unidades de significado continuas dentro de un párrafo. Recupera el turno completo, la última intervención entrevistadora y referentes. No unas citas entre párrafos ni normalices el texto.
3. Aplica los códigos por significado y justifica cada uno. No traduzcas una codificación previa ni asignes por palabras compartidas. La forma de una metáfora no determina su sentido. No hay cuota de códigos o fragmentos.
4. Distingue decisiones, actores mencionados, condiciones y alcance sin convertir cada enunciado en necesidad. Conserva recursos suficientes y decisiones de no cambiar. No presupongas fallas o demanda tecnológica.
5. Registra modalidad, atribución y elicitación. Una intención recordada no acredita ejecución. El mismo significado puede presentarse como relato o deseo; su modalidad no decide por sí sola qué código corresponde. Las opciones ofrecidas por el entrevistador siguen siendo sugeridas aunque se rechacen.
6. Cubre los 124 párrafos participantes exactamente una vez con estado y razón. CODIFICADO no implica haber interpretado toda cláusula: si una parte sustantiva queda sin encaje, registra incidencia parcial. PENDIENTE_REVISION es admisible y no se oculta para obtener una aprobación estructural.
7. Revisa lecturas alternativas, doble codificación justificada, negaciones, casos de suficiencia y material sin encaje. Un caso nuevo puede exigir cambiar el libro, pero en esta salida solo propones el cambio y sus casos afectados; no añadas C064 ni alteres definiciones.
8. Ejecuta el validador y revisa el sentido de las decisiones. Las pruebas incluidas son documentación técnica, no esta recodificación. Un resultado sin errores no cierra incidencias interpretativas ni equivale a validación humana.

Una valoración sobre el modo de conversar o recordar durante la entrevista puede conservarse como CONTEXTO y memo reflexivo cuando no informa procesos, actores o necesidades de la actividad estudiada. Si sí informa sustantivamente la actividad, selecciónala por su significado; el cierre por sí solo no determina el estado.

Distingue resolver un encaje de codificación de resolver una incógnita factual. La ambigüedad conservada y la viabilidad futura no verificada pueden seguir abiertas como límites de evidencia, sin fabricar respuestas para cerrar cobertura. Una parte sustantiva sin encaje requiere incidencia y razón concreta.

No produzcas todavía mapas finales, necesidades priorizadas, historias de usuario, arquetipos, recomendaciones de producto ni texto del reporte. Los memos pueden señalar material candidato y límites para su etapa posterior.

## Estructura JSON obligatoria

Objeto con metadatos, segmentos, cobertura, memos, incidencias y balance. Las listas pueden ser vacías cuando corresponda; nunca omitas campos para acortar.

metadatos:
- tarea: R03; resultado_version: 1.0; protocolo_version: 1.0; corpus_version: 1.0; libro_version: 1.2.
- estado: APLICACION_PARA_REVISION.
- tipo_revision: ASISTIDA_POR_LLM; revision_humana_independiente: PENDIENTE.
- modelo y parametros: null cuando no consten; fuente_modelo: explicación de disponibilidad.

segmentos: un objeto por fragmento, con estos campos:
- id: R03-S001 y sucesivos únicos; entrevista; parrafo_id; turno_id.
- cita: texto literal continuo del párrafo participante, sin normalizar espacios ni agregar puntos suspensivos. Puede omitir el prefijo de voz si los offsets lo reflejan.
- inicio y fin: índices Unicode, inicio incluido y fin excluido, de la cadena original texto. Debe cumplirse texto[inicio:fin] == cita. Calcula con Python; no cuentes bytes ni posiciones UTF-16. No uses valores aproximados.
- codigos: lista no vacía de identificadores C001 a C063 existentes.
- justificaciones_codigo: lista de {codigo, justificacion}, una entrada por código, explicando qué significa aquí y por qué no basta una categoría vecina cuando hay frontera.
- estatus: lista no vacía con RELATO_EPISODIO, PRACTICA_GENERAL_DECLARADA, INTERPRETACION_PARTICIPANTE, PREFERENCIA_DESEADA, HIPOTETICO o DESCONOCIMIENTO_EXPLICITO.
- subtipos_hipotetico: lista con CONTRAFACTUAL, POSIBILIDAD o ILUSTRACION cuando estatus incluye HIPOTETICO; vacía en otro caso.
- nota_estatus: razón contextual y cláusulas si hay mezcla inseparable. Prefiere separar fragmentos cuando se pueda.
- atribuciones: lista no vacía de {sujeto_referido, tipo, justificacion}; tipo DECLARACION_PROPIA, TERCERO_RELATADO o INFERENCIA_ANALITICA. Describe la relación con esta voz sin atribuir necesidades no dichas a terceros.
- elicitacion: objeto con forma, funciones, influencia, marco, respuesta, movimiento, apertura_turno_parrafos, intervencion_inmediata_parrafos y justificacion.
- contexto_parrafos: lista de referencias canónicas útiles; motivo_contexto: explicación o cadena vacía si no hace falta otro contexto.

Valores de elicitacion:
- forma: ABIERTA, CERRADA, MIXTA, NO_INTERROGATIVA o NO_DETERMINABLE.
- funciones: una o varias de EXPLORACION, FOCALIZACION, SEGUIMIENTO, OPCIONES, RECAPITULACION, CIERRE, OTRA.
- influencia: SIN_CONTENIDO_SUGERIDO, CONTENIDO_SUGERIDO o NO_DETERMINABLE.
- marco: RELATO, METAFORA, IDEAL u OTRO.
- respuesta: CONFIRMA, RECHAZA, MATIZA, CORRIGE, DESARROLLA, ASIENTE_SIN_DESARROLLO o NO_APLICA.
- movimiento: RESPUESTA, CONTINUACION, ACLARACION_PROPIA, AUTOCORRECCION_PROPIA o NUEVO_ASUNTO_PROPIO.
- apertura_turno_parrafos: párrafos del último turno entrevistador anterior al turno participante. intervencion_inmediata_parrafos: párrafos de la intervención entrevistadora más reciente antes del párrafo objetivo. Pueden coincidir, especialmente en continuaciones; no se inventa una nueva pregunta entre párrafos. Las referencias son contexto, nunca evidencia participante.

cobertura: exactamente 124 objetos, uno por párrafo objetivo. Campos parrafo_id, estado (CODIFICADO, CONTEXTO, ADMINISTRATIVO o PENDIENTE_REVISION), segmentos (ids de este párrafo) y justificacion. CODIFICADO exige al menos un segmento; otros estados exigen lista vacía. Si una parte pudo codificarse pero otra sigue ambigua, deja CODIFICADO y registra la duda parcial en incidencias sin fingir que se resolvió.

memos: objetos con id R03-M001, tema, parrafos, segmentos, codigos, interpretacion, alternativa y efecto_para_recodificacion. Las referencias pueden incluir párrafos de contexto no objetivo, pero los segmentos deben existir en la salida. Expón diferencias entre códigos cercanos, evidencia insuficiente y lecturas alternativas. No hay cuota de memos.

incidencias: objetos con id R03-I001, tipo, descripcion, parrafos, codigos, propuesta, estado (ABIERTA o RESUELTA_EN_APLICACION). No se puede declarar resuelto un cambio del libro que todavía no se aplicó y revisó. Una lista vacía es posible si está justificada en el balance.

balance: objeto con reglas_probadas (ids R001–R018 efectivamente examinados), reglas_no_probadas, fronteras_observadas (ids F existentes cuando corresponda), cambios_propuestos (lista explicada), pendientes y recomendacion. Expresa alcance y límites; no declares libro congelado, el conjunto de cinco entrevistas recodificado o validación humana.

## Salida legible y archivos

Entrega:
1. R03_recodificacion_E03_v1.json con el objeto completo.
2. R03_explicacion_v1.md con explicación completa y tablas.
3. R03_control_validacion.json con el control realmente ejecutado o estado NO_EJECUTADO y motivo.

Puedes añadir compilado Word sin sustituir JSON y Markdown. No es necesario duplicar todo el JSON en la respuesta si los archivos están completos y descargables. Si no puedes crear archivos, presenta bloques completos sin truncamiento y señala lo que falta.

En la explicación identifica entradas, versiones y alcance; desarrolla las decisiones y fronteras encontradas con citas verificables, y presenta tabla de códigos utilizados con nombres, fragmentos, párrafos y ejemplos. Los conteos describen esta entrevista y esta versión: no son menciones, prevalencia, importancia o personas. Incluye resumen de cobertura y todas las incidencias. Expón conceptos completos en la prosa y los identificadores después entre paréntesis.

Si incluyes memos sobre procesos, actores o necesidades, conserva quién lo afirma, qué episodio o deseo sostiene la lectura y qué falta verificar. No conviertas terceros relatados en entrevistas adicionales ni esquemas del analista en categorías de la persona.

Para ejecutar desde el directorio del paquete:

```bash
python3 validar_recodificacion.py . /ruta/R03_recodificacion_E03_v1.json --salida /ruta/R03_control_validacion.json
```

La coordinación revisará la salida antes de preparar R04. Si se modifica después el libro, se registrarán versión y reapertura de los casos afectados, también de entrevistas ya recodificadas. No se supone estabilidad definitiva tras un piloto.
