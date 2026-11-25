# Cierre del corpus y protocolo de primera lectura

Corpus de referencia 1.0 · Protocolo de análisis 1.0 · 24 de noviembre de 2026

Ya se recibieron y revisaron cinco transcripciones. La cobertura está documentada en 24_cobertura_corpus.csv y el inventario de versiones en 24_registro_corpus.json. E01 aporta operación pública de registros territoriales; E02 investigación; E03 coordinación civil; E04 actividad económica cotidiana y E05 uso personal de la ciudad. E04 y E05 son los dos perfiles finales no especializados. Ninguna persona pertenece al perfil excluido por el usuario.

Este cierre permite comenzar primeras lecturas locales. No declara saturación, representatividad, cumplimiento integral de la rúbrica ni finalización de los registros administrativos. Se conservan los originales y se separan los campos disponibles de los desconocidos. No se reabrirán diálogos para producir evidencia que falte a una conclusión futura.

## Qué se conserva y cómo se localiza

Los originales permanecen en corpus/E01 a corpus/E05. En analisis/insumos hay un JSON canónico por entrevista, versión 1.0. Conserva cada párrafo no vacío del documento y su posición original, incluso los saltos de numeración por párrafos vacíos. No corrige ortografía, espacios ni voz. Los párrafos de continuación se vinculan con la intervención en que aparecen.

El prefijo E01-P007, por ejemplo, identifica el párrafo 7 del documento E01. La unidad de registro es el párrafo; no se confunde con una unidad de significado autosuficiente. El análisis selecciona fragmentos sustantivos dentro de párrafos y recupera el turno y la pregunta anterior para interpretarlos. Una idea que atraviesa varios párrafos puede recibir varios segmentos relacionados mediante un memo; no se inventa una cita unificada.

Las citas serán subcadenas literales de un único párrafo fuente. No se sustituye una cita por una paráfrasis, se añaden puntos suspensivos como si estuvieran en el original ni se unen frases separadas. Las citas que se utilicen en el reporte deberán conservar ese vínculo y pasar revisión de sentido además de comprobación textual.

## Secuencia de análisis

1. A01: primera lectura de E01, propuesta de segmentos y códigos locales, lectura del proceso, actores y necesidades candidatas.
2. Comprobar citas, identificadores y cobertura de A01; revisar las interpretaciones y registrar correcciones.
3. Preparar A02 a A05 por separado con el mismo protocolo y únicamente su entrevista. No transferir códigos, hallazgos o síntesis de A01 como respuestas deseadas. Una modificación del método se documentará y aplicará consistentemente.
4. Consolidar los cinco libros locales con el corpus completo. Unir equivalencias, conservar diferencias y justificar los cambios en un registro. Los códigos locales se mantendrán como antecedentes; el libro común tendrá una nueva versión y referencias cruzadas.
5. Pilotear el libro propuesto, revisar incidencias y versionar ajustes; después recodificar las cinco entrevistas bajo criterios comunes. Solo entonces comparar temas, arquetipos, preferencias, procesos y necesidades.
6. Construir mapas por perfil y conexiones de extremo a extremo únicamente cuando haya sustento. Investigar por separado el proceso documentado pertinente y explicar vacíos o diferencias de alcance.
7. Formular y priorizar necesidades e historias de usuario con objetos y metadatos trazables. Las historias no equivalen a una por entrevista. Justificar después propuestas técnicas, cuatro lentes y productos concretos cuando correspondan a las decisiones.
8. Redactar el reporte con narrativa, citas y rutas a soportes, dentro del límite acordado, y revisar rúbrica y matriz de requisitos.

Una primera lectura local por LLM es una etapa delimitada, no una codificación independiente humana ni una validación del conjunto. El carácter provisional debe permanecer visible en el registro de análisis, sin convertirlo en una carga de identificadores en la prosa.

## Análisis local y clasificación de evidencia

Los códigos se proponen desde el significado del texto. Cada uno tendrá nombre comprensible, definición, criterios de inclusión y exclusión y al menos un ejemplo literal. No se exige una cuota de códigos; se evita fragmentar sin utilidad o unir asuntos distintos para simplificar. Se admite codificación múltiple con justificación.

Se distinguirán relato del episodio, práctica general declarada, interpretación de la persona, preferencia deseada, posibilidad hipotética y desconocimiento explícito. Son condiciones del enunciado, no certificaciones de verdad externa. Una preferencia ideal no se redactará como una falla ocurrida. Un contrafactual no se tratará como un paso del proceso real.

La pregunta del entrevistador aporta contexto, no prueba de una necesidad del participante. Se distinguirá una iniciativa propia de una respuesta a pregunta abierta, ejercicio ideal, opción sugerida, recapitulación o corrección. Si no puede determinarse, se dejará registrado. No se borrará el efecto del guion común para presentar coincidencias como hallazgos espontáneos.

Todo párrafo del participante tendrá un registro de cobertura: codificado, contextual o administrativo. Los contextuales explican el diálogo sin recibir un código sustantivo; los administrativos se reservan para apertura o cierre sin contenido analítico. Si un párrafo mezcla contenidos, se selecciona el fragmento sustantivo y se explica su contexto. No se asigna un código a un simple asentimiento sin leer la pregunta y el turno.

Las propuestas locales de necesidades deberán explicar quién necesita saber qué, para qué decisión, en qué contexto y qué evidencia lo permite. Los criterios no expresados se marcarán como propuestas del análisis pendientes de validar, sin inventar tiempos, porcentajes, umbrales, costos o capacidades institucionales.

## Revisión inspirada en JANUS

Se conservan entrada canónica y huellas, prompt, salida completa, versión, esquema de códigos, segmentos, memos, incidencias y resoluciones. El modelo y los parámetros se registrarán cuando la interfaz los informe; en otro caso permanecen no disponibles. El paquete no autoriza a inventar esos valores.

El validador local comprobará identificadores, referencias, literalidad y cobertura. Emitirá errores y advertencias, con posiciones de las citas cuando coincidan. Una validación estructural correcta no demuestra que un código esté bien interpretado. Después se revisarán alcance de afirmaciones, contexto de citas, lectura alternativa y discrepancias.

JANUS contempla revisión adversarial humana con experiencia complementaria. Su estado se conservará como pendiente mientras no se realice y documente. No se declarará revisión humana por una respuesta del modelo o por estas comprobaciones automáticas. Tampoco se calcularán concordancias entre observadores sin codificaciones independientes de las mismas unidades y un instrumento compartido. No se reutilizarán métricas publicadas como si correspondieran al proyecto.

El reporte describirá las herramientas y usos de IA efectivamente realizados. Una firma, fecha, revisión externa o verificación de un soporte no se acredita por aparecer mencionada en el diálogo. Los metadatos conservan los valores disponibles y sus límites.

## FAIR y objetos digitales

Esta etapa prepara identificadores locales estables, archivos legibles por máquina, versiones, procedencia y relaciones. Los objetos futuros de códigos, necesidades e historias enlazarán sus fuentes y condiciones de acceso. Los metadatos todavía no conocidos seguirán vacíos o pendientes.

No se declarará un depósito FAIR completo por usar JSON, una carpeta o GitHub. No se inventarán DOI, licencias, repositorios publicados o identificadores persistentes externos. Los prompts de análisis e integración sí forman parte de los soportes previstos; los prompts de desarrollo de entrevistas se conservan en el expediente de preparación y se excluyen del repositorio final conforme al alcance acordado.

## Qué no se infiere del corpus

Cinco perfiles no describen toda la ciudad. Los registros relatados no son manuales institucionales. Las relaciones entre perfiles no forman automáticamente una sola cadena operativa. Las personas mencionadas no tienen preferencias conocidas por el solo hecho de aparecer en un relato. La ausencia de una necesidad expresada no prueba su inexistencia.

Las necesidades sin alcance cartográfico directo se conservan para el juicio crítico. Las capacidades de los cuatro lentes y la arquitectura de referencia se examinarán en su etapa, sin convertirlas en códigos o necesidades predeterminadas de las primeras lecturas.

## Estado operativo después del cierre de HU01

N01 y HU01 están revisadas operativamente 1.1 con sus cuatro originales por tarea preservados. En HU01 no cambian cinco perfiles funcionales, 21 historias, 28 criterios, 90 operaciones o prioridades; N005 sigue como condición sin actividad nueva. Se cotejaron las 67 entradas, 76 payloads, 29 necesidades, 351 evidencias y las referencias a los criterios fuente. 348 citas, voz, turnos y posiciones y cinco citas ilustrativas coinciden con los cinco corpus. Dos figuras inspeccionadas y reutilizadas; no se declara nueva exportación.

La revisión precisa 23 campos: 21 contextos temporales y dos contextos espaciales se conservan con sus evidencias, separados de resolución_temporal o escala_espacial desconocidas. Referencia de significado: W3C DCAT 3, 6.6.7; no conformidad DCAT. El diseño posterior puede proponer granularidad requerida con su razón y estado sin atribuirla al relato. No se inventan fechas, escalas, disponibilidad o licencias.

Los perfiles de metadatos revisados tienen versión 1.1; perfiles funcionales e historias conservan 1.0 porque su contenido no cambia, necesidades heredadas conservan 1.1. El registro explicita entidad, ruta, huella y versión por objeto. Los 76 objetos locales no son PIDs/tipos/perfiles registrados. Control revisado y cotejo complementario ejecutados; novena tabla preserva contextos. Las auditorías técnicas no prueban semántica, utilidad, aceptación o revisión humana independiente.

T01 está preparada con 39 requisitos GCR/LEN/DAT y cobertura de las 21 historias. Fundamentos, cuatro lentes, arquitectura y dos o tres productos serán propuestas con validación futura. Fuente de código: snapshot público GeoInsights identificado por commit, distinto como objeto del ZIP original del curso, con lectura estática y licencia MIT. No se ejecuta ni se trasladan datos/resultados epidemiológicos. Los requisitos de Andrea se conservan como apuntes, sin inventar identidad o fuente autoral.

Corpus, libro 1.3 y S01/P01/D01/ACT01/N01 permanecen intactos; siguen límites de contraste documental y posturas no recabadas. Los 208 requisitos se revisarán integralmente antes de entregar. Revisión humana independiente pendiente; no declarar concordancia, saturación, firmas o registros no disponibles.
