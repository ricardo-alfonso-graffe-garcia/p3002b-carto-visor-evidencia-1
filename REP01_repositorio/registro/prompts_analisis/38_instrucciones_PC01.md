# PC01 · Pilotaje operativo del libro común

Versión 1.0 · Corpus 1.0 · Propuesta C01 1.0 · 24 de noviembre de 2026

## Tarea y alcance

Aplica el libro común propuesto en C01 a los 22 párrafos objetivo del archivo casos_PC01_v1.json. El objetivo es comprobar si definiciones, fronteras y reglas se pueden usar de forma consistente antes de recodificar las cinco entrevistas. No se solicita recodificación completa, síntesis transversal, mapas, historias de usuario ni redacción del reporte.

Esta es una aplicación piloto asistida por LLM. No la presentes como revisión humana independiente, medición de fiabilidad, validación externa o aplicación integral de JANUS. Registra revisión humana independiente PENDIENTE. No inventes modelo, parámetros, fechas de entrevistas, firmas ni verificaciones. El libro sigue en propuesta durante este ejercicio.

## Entradas y autoridad

Descomprime 39_insumos_PC01.zip. Dentro de PC01_insumos_v1 están este instructivo, LEEME.md, manifest.json, el libro común C01 1.0, los 22 casos, las cinco fuentes canónicas y sus vistas de lectura, el validador y su nota de pruebas. El JSON canónico determina texto, voz, párrafo y turno. La vista de texto facilita lectura y no reemplaza la fuente.

El libro es una extracción sin cambios de los 60 códigos, sus ejemplos, 18 reglas y 18 fronteras de C01. Las correspondencias locales y asignaciones previas se excluyen deliberadamente: aplica las definiciones al texto, no traduzcas automáticamente códigos anteriores. El paquete no contiene el encargo del cliente, los productos buscados o la rúbrica como categorías esperadas. No utilices otros chats, recuerdos ni navegación externa.

Comprueba primero inventario y huellas. Si una entrada necesaria no se puede leer, informa el archivo exacto y no emitas conclusiones dependientes de él. Si no puedes ejecutar Python, registra NO_EJECUTADO y no declares controles aprobados.

## Secuencia de lectura y aplicación

1. Lee los 60 códigos completos, las reglas y fronteras. Distingue ejemplos de definiciones: no codifiques por palabra coincidente o por compartir una metáfora.
2. Lee las cinco fuentes completas para contexto. Después vuelve a cada caso, al turno completo, a la intervención que lo abrió y a los antecedentes de pronombres. Puedes citar otros párrafos en memos o contexto; solo los 22 objetivos reciben segmentos en esta salida.
3. Decide si hay contenido codificable. Un nombre de metáfora puede necesitar contexto y no código; un cierre puede incluir contenido sustantivo. No fuerces todos los casos al mismo estado.
4. Selecciona fragmentos continuos suficientes dentro de un párrafo. El mismo párrafo puede necesitar varios. Evita fragmentar para reproducir el inventario local; tampoco unas modalidades distintas solo para ahorrar registros.
5. Aplica cero, uno o varios códigos según significado, justificando por separado cada asignación. No hay cuota ni número esperado. No es necesario utilizar los 60 códigos y su ausencia del piloto no los invalida.
6. Distingue episodio, práctica general, interpretación, preferencia, posibilidad o desconocimiento. Una afirmación sobre otras personas sigue teniendo esta voz como fuente, no equivale a entrevistarlas. Un ejercicio ideal no demuestra una falla actual ni un beneficio medido.
7. Registra elicitación, respuesta y movimiento con los ejes separados de C01. Una pregunta cerrada puede ser neutral; una opción rechazada sigue habiendo sido sugerida. Una aclaración propia dentro del turno no borra la pregunta que lo abrió.
8. Revisa alternativas y escribe memos sobre fronteras realmente encontradas. Si falta un código o una regla no resuelve el caso, documenta la incidencia y propuesta; no cambies el libro ni inventes un C061 en esta salida. PENDIENTE_REVISION es válido y requiere razón concreta.
9. Ejecuta el validador y revisa el sentido de cada decisión aunque pase. Entrega la salida íntegra y conserva incidencias. No redactes un resultado esperado para aparentar que el piloto fue exitoso.

## Estructura JSON obligatoria

Objeto con metadatos, segmentos, cobertura, memos, incidencias y balance_piloto. Las listas pueden ser vacías cuando corresponda; nunca omitas campos para acortar.

metadatos:
- tarea: PC01; piloto_version: 1.0; corpus_version: 1.0; libro_version: 1.0.
- estado: APLICACION_PILOTO_PARA_REVISION.
- tipo_revision: ASISTIDA_POR_LLM; revision_humana_independiente: PENDIENTE.
- modelo y parametros: null cuando no consten; fuente_modelo: explicación de disponibilidad.

segmentos: un objeto por fragmento, con estos campos:
- id: PC01-S001 y sucesivos únicos; entrevista; parrafo_id; turno_id.
- cita: texto literal continuo del párrafo participante, sin normalizar espacios ni agregar puntos suspensivos. Puede omitir el prefijo de voz si los offsets lo reflejan.
- inicio y fin: índices Unicode, inicio incluido y fin excluido, de la cadena original texto. Debe cumplirse texto[inicio:fin] == cita. Calcula con Python; no cuentes bytes ni posiciones UTF-16. No uses valores aproximados.
- codigos: lista no vacía de identificadores C001 a C060 existentes.
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

cobertura: exactamente 22 objetos, uno por párrafo objetivo. Campos parrafo_id, estado (CODIFICADO, CONTEXTO, ADMINISTRATIVO o PENDIENTE_REVISION), segmentos (ids de este párrafo) y justificacion. CODIFICADO exige al menos un segmento; otros estados exigen lista vacía. Si una parte pudo codificarse pero otra sigue ambigua, deja CODIFICADO y registra la duda parcial en incidencias sin fingir que se resolvió.

memos: objetos con id PC01-M001, tema, parrafos, segmentos, codigos, interpretacion, alternativa y efecto_para_recodificacion. Las referencias pueden incluir párrafos de contexto no objetivo, pero los segmentos deben existir en la salida. Expón diferencias entre códigos cercanos, evidencia insuficiente y lecturas alternativas. No hay cuota de memos.

incidencias: objetos con id PC01-I001, tipo, descripcion, parrafos, codigos, propuesta, estado (ABIERTA o RESUELTA_EN_PILOTO). No se puede declarar resuelto un cambio del libro que todavía no se aplicó y revisó. Una lista vacía es posible si está justificada en el balance.

balance_piloto: objeto con reglas_probadas (ids R001–R018 efectivamente examinados), reglas_no_probadas, fronteras_observadas (ids F existentes cuando corresponda), cambios_propuestos (lista explicada), pendientes y recomendacion. Expresa alcance y límites; no declares libro congelado, corpus recodificado o validación humana.

## Explicación legible y entregables

La explicación debe permitir entender qué se probó, qué se pudo aplicar y qué requiere ajuste. Usa conceptos en prosa y localizadores después entre paréntesis: no hagas del texto una secuencia de identificadores. Incluye una tabla de los 22 casos, con decisión, códigos por nombre y motivo breve; después desarrolla las fronteras e incidencias relevantes con citas verificables. No son hallazgos finales ni una jerarquía de necesidades.

Entrega tres archivos descargables:
1. PC01_pilotaje_v1.json con el objeto completo.
2. PC01_explicacion_v1.md con explicación íntegra y tablas, sin truncamiento.
3. PC01_control_validacion.json con salida real del validador; si no se ejecutó, estado NO_EJECUTADO y motivo. No imites una salida exitosa.

Puedes añadir PC01_pilotaje_v1.docx como compilado íntegro, sin sustituir JSON o Markdown. Si la interfaz no permite crear archivos, presenta todo el contenido con límites claros, sin omitir campos por extensión ni dar por guardado lo que no se guardó. La coordinación revisará las salidas antes de ajustar el libro y preparar la recodificación.

Para ejecutar desde el directorio del paquete:

```bash
python3 validar_PC01.py . /ruta/PC01_pilotaje_v1.json --salida /ruta/PC01_control_validacion.json
```

El validador comprueba estructura, referencias, offsets, literalidad, cobertura y valores permitidos. No determina si una interpretación es correcta, si se revisó todo el material ni si la entrevista acredita hechos externos. Toda modificación posterior conserva original, antes y después y motivo.
