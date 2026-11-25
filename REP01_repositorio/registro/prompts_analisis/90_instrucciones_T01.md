# T01 · Fundamentos, arquitectura y productos candidatos

Encargo 1.0 · 25 de noviembre de 2026 · P3002B, Evidencia 1.

Lee estas instrucciones y 91_insumos_T01.zip. Desarrolla una propuesta de diseño fundamentada para el reporte; la implementación del producto pertenece a la fase siguiente. No ejecutes GeoInsights, modelos territoriales o servicios en la nube. Los scripts de validación de documentos y los diagramas de diseño sí pueden ejecutarse. No publiques, registres PIDs ni contactes a terceros.

## Punto de partida y lectura

Comprueba manifest.json y registro_entradas.json. Se incluyen el expediente maestro y los 208 requisitos, Canvas/rúbrica/feedback, cinco corpus, libro 1.3 y resultados preferidos S01/P01/D01/ACT01/N01/HU01. S01, P01, D01, ACT01 y N01 están revisadas 1.1, al igual que HU01; los corpus son 1.0. El control estructural no demuestra verdad externa o revisión humana independiente.

Lee primero el alcance de esta tarea, las secciones 10–16 del maestro y las categorías GCR/LEN/DAT de la matriz. Lee las 21 historias completas, sus condiciones, prácticas a preservar, criterios y perfiles de información; después las 29 necesidades y las cinco fichas funcionales/procesos. Consulta las evidencias y vuelve a los párrafos canónicos, preguntas y correcciones cuando uses un episodio o cita. La consulta dirigida es válida si registras su alcance; no declares lectura exhaustiva de archivos que solo consultaste parcialmente. No repitas todo el corpus duplicado de cada JSON como si fuera evidencia independiente.

HU01 conserva cinco perfiles funcionales, 21 historias, 28 criterios, 90 pasos propuestos, seis deseos ideales explícitos y N005 como condición pendiente sin historia. En su revisión 1.1 se separaron 21 contextos temporales y dos contextos espaciales: describir una ocasión, orden o vigencia no acredita resolución temporal o escala de representación. El diseño puede proponer una granularidad requerida, identificada como propuesta y justificada por decisión; no modifica lo que la persona expresó ni afirma la resolución de datos no inspeccionados. Los 21 perfiles siguen con sus 21 campos; contexto_temporal/contexto_espacial conservan las descripciones.

Los cinco casos no constituyen una cadena institucional entre sí. D01 conserva cero episodios con fuente formal directamente atribuible, diez preguntas pendientes y cero divergencias formalmente demostradas. ACT01 mantiene posturas frente a homologación NO_RECABADA; poder e interés dependen del ámbito. N01 distingue actuales atendidas, parcial, carencia específica, ideal y condición. El encargo del cliente es una propuesta institucional, no el diagnóstico demostrado.

Las dos capas SSC no están en las entradas; no se requiere poseerlas para proponer esta arquitectura. No describas sus atributos, CRS, calidad o disponibilidad como si los hubieras inspeccionado. La propuesta puede pensar más allá de esas capas sin prometer acceso a cualquier dato.

## Resultado intelectual esperado

Construye una argumentación que explique cómo las decisiones observadas y deseadas justifican determinadas capacidades de información, qué alternativas son razonables y qué falta comprobar. Elabora dos o tres productos candidatos concretos para la fase siguiente. No son un backlog aprobado o una promesa de implementación.

Cada producto debe expresar función, personas usuarias, decisión, alcance y exclusiones, necesidad/historia de origen, información requerida, transformaciones, representación de salida, interacción, responsables por confirmar, dependencias, incertidumbres, pruebas propuestas y condiciones para descartarlo o reformularlo. Un título como «dashboard», «visor» o «pipeline» no basta. No transformes la legitimidad de una necesidad en obligación de resolverla con software público. Puedes conservar historias fuera del portafolio con una razón explícita. No necesitas diseñar un producto por perfil, digitalizar las muestras físicas o sustituir la conversación.

La trazabilidad de una propuesta a una historia acredita su relación analítica, no que la persona haya pedido esa solución. Distingue DEMANDA_EXPRESADA, CAPACIDAD_DERIVADA y OPORTUNIDAD_PROPUESTA en el argumento. Los productos son siempre PROPUESTA_NO_IMPLEMENTADA, con pertinencia, factibilidad y aceptación pendientes.

## Geografía crítica, unidades e incertidumbre

Usa los conceptos atribuidos a Andrea en los apuntes según la síntesis del expediente, sin inventar apellido, biografía o una publicación de esa persona. Los PDFs originales de clase no están redistribuidos; la matriz conserva páginas y requisitos. No declares haberlos leído desde este paquete. Para afirmaciones técnicas usa literatura o documentación primaria comprobada y separa esa fundamentación de la atribución docente.

Desarrolla la retórica visual, verbal y metodológica de la cartografía: qué pregunta cuenta la representación, quién decide qué observar, qué títulos, leyendas, colores y operaciones guían la interpretación. Examina autoría y posibilidad de cuestionar límites, cobertura y subregistro, jurisdicción y capacidad de actuar. Ausencia de observaciones no es ausencia del fenómeno; no cuantifiques exclusiones que no puedas calcular con datos existentes.

Distingue escala de representación, resolución, unidad de análisis, cobertura, efectos de escala y zonificación del MAUP, y falacia ecológica cuando sea pertinente. Homologar puede significar correspondencias e interoperabilidad, sin una geometría universal. No sostengas que escaneo, hexágonos o más datos eliminan automáticamente el MAUP o sesgo.

Evalúa explícitamente estas ocho familias de agregación: ADMINISTRATIVA, REJILLA_HEXAGONOS, NATURAL, TENENCIA_CONCESION, COMUNITARIA, REDES, INFLUENCIA y REFERENCIA. La familia REFERENCIA abarca particiones analíticas de referencia justificables, no un límite verdadero por defecto. Para cada una explica pregunta pertinente, proceso generador, denominador, límites/jurisdicción, parámetros, estabilidad temporal, autoría, exclusiones, comparabilidad y razón para adoptar, condicionar o descartar. No es necesario aplicarlas todas a todos los productos.

Concreta cuatro prácticas de diseño: INCERTIDUMBRE_DENOMINADORES; COMPARAR_UNIDADES; ESCENARIOS_METODOLOGICOS; EXCLUSIONES. Di qué vería o podría cuestionar la persona, qué datos/configuración se necesitarían y cómo se comprobaría después. Un escenario de interfaz o análisis de sensibilidad es una propuesta; no un resultado calculado. Una salida igual entre dos unidades no demuestra identidad de capas o equivalencia jurídica.

## Cuatro lentes, con condiciones de uso

Evalúa exactamente SCAN, POTENCIA_ESCALAMIENTO, TDA y ABM. Cada ficha debe vincular una pregunta y decisión posible con historias/productos pertinentes, insumos requeridos, unidad, supuestos, parámetros, salidas interpretables, incertidumbres, sensibilidad, verificación futura y límites. Puede concluir no pertinencia para los productos actuales, siempre con razón y una condición de reconsideración. Cubrir el temario no exige asignar cuatro métodos a una misma necesidad.

- SCAN: especificar eventos/medidas y referencia o población en riesgo, hipótesis nula, ventanas y dimensión temporal cuando corresponda. Diferenciar concentración detectada de causa y de capacidad de intervenir. Revisar sensibilidad y multiplicidad conforme al método elegido.
- POTENCIA_ESCALAMIENTO: distinguir una relación de escala entre magnitudes de una distribución de cola pesada. Explicar estimación y dominio, comparación con alternativas, diagnóstico y requisitos de muestra. Una recta log–log no prueba ley de potencia.
- TDA: distinguir Mapper y otras construcciones si se mencionan. Explicar variables, normalización, métrica, filtro/cobertura/agrupamiento cuando aplique, y cómo interpretar conexiones. Cercanía de perfiles o formas no equivale a cercanía geográfica. No asumir que el script del repositorio implementa cualquier variante TDA.
- ABM: definir agentes, ambiente, reglas/interacciones, decisiones, parámetros, fuentes de calibración, comparación con observaciones, incertidumbre y sensibilidad. Escenarios condicionales no son predicciones ciertas ni efectos causales demostrados.

Investiga al menos una herramienta candidata por lente en documentación oficial o repositorio de sus autores. Registra versión/documentación consultada, lenguaje, función, requisitos y compatibilidad no probada. No instales versiones antiguas del repositorio por inercia ni digas que corre en el entorno sin probarlo. Una herramienta descartada puede formar parte de la evaluación, sin recomendación de despliegue.

## GeoInsights como referencia estática

Se incluye referencia_geoinsights/GeoInsights_snapshot.zip: copia pública del repositorio data-lama/covid_geoinsights_pipeline, commit ab60b86a6a87bca0dd370c7c4af3ada4185d187e. Comprueba procedencia_snapshot.json y descomprime de forma segura para leer, sin ejecutar sus scripts. El snapshot público no se declara idéntico al ZIP originalmente aportado en clase. Conserva licencia MIT y atribución DataLama Team, 2020–2021. El README deja la cita del artículo pendiente; no inventes esa referencia.

Lee el README completo, LICENSE, el orquestador, la configuración de ejecución y los módulos pertinentes. Se incluye una guía de lectura con rutas y alcance de la inspección preparatoria, no una certificación de funcionamiento. Examina los adaptadores/unificadores, agregadores por geometría/radio/comunidad, constructores, análisis y generación de productos. Los datos viven fuera del repo y algunas dependencias/configuraciones son externas. La copia contiene código de depuración en universal_generic_unifier.py al construir casos y dependencias históricas; no es un producto listo para ejecutar en CDMX.

Explica qué retomas, qué cambias y qué descartas, con archivo y localizador. Separa patrón arquitectónico de decisiones epidemiológicas. No traslades casos, movilidad, Rt, ventanas o población como supuestos del proyecto. No publiques ni reproduzcas credenciales o claves de configuración.

Diseña seis responsabilidades modulares: EXTRACCION, UNIFICACION, AGREGACION, CONSTRUCCION, ANALISIS y PRODUCTOS. Incluye entradas/salidas con contratos, controles de calidad, procedencia, manejo de faltantes, versiones y retornos de dudas/correcciones. Los datos pueden seguir ramas o saltar operaciones no pertinentes; no obligues a una nota o muestra a convertirse en polígono agregado. Las conexiones propuestas son de arquitectura, no procesos institucionales observados.

Evalúa representaciones PUNTOS, LINEAS, POLIGONOS, RASTER, REDES, TEXTO_TABLAS, MUESTRAS_FISICAS y TRES_DIMENSIONES; justifica qué sí necesita adaptador, qué requiere referencia a un objeto físico y qué no procede en los productos actuales. Considerar 3D no obliga a usarlo. No prometas lectura universal sin contratos y adaptación.

Distingue backend de preparación/análisis, interfaz, actividad humana y fuente externa. Evalúa Google Earth Engine según finalidad y datos, consultando documentación primaria si lo propones. Sin pertinencia suficiente, explica su descarte. No presupongas cuenta, cuotas, credenciales o autorización.

## Datos, contratos, metadatos y selección

Para cada producto documenta datos requeridos y fuentes candidatas. Una página de catálogo comprobada no demuestra descarga, integridad, vigencia, resolución, permiso o acceso operativo a su contenido. Usa estados CANDIDATO_DOCUMENTADO o REQUERIDO_NO_DISPONIBLE. No descargues datos masivos o personales ni produzcas análisis territoriales para llenar resultados. Las fuentes pueden ser institucionales, comunitarias, conocimiento situado o soportes no digitales con condiciones explícitas.

Los contratos indican campos, significado, tipos, unidades, nulos, procedencia, identidad/versiones, referencia espacial y semántica/tiempo pertinentes. Incluye reglas para aceptar, advertir o detener una transformación y devolver dudas sin sobrescribir originales. No rellenes atributos de capas no aportadas. La información requerida por un producto puede precisar metadatos de HU01 como propuesta de diseño, sin cambiar sus fuentes.

Justifica las transformaciones: conversiones de unidad/CRS, uniones semánticas, alineación espacial y temporal, agregaciones y denominadores, según proceda. Elige parámetros después de la pregunta; conserva alternativas y sensibilidad. No confundir error, incertidumbre, desconocimiento y desacuerdo legítimo.

La selección de dos o tres productos será razonada y condicional: relevancia de la decisión, beneficio potencial, restricciones, disponibilidad/producción de información, coste de mantenimiento, carga para quienes aportan y verificabilidad. No inventes pesos, presupuesto, impacto medido o demanda de ciudad. Puede haber prioridad parcial, empates y reformulación. Explica qué gana/pierde o qué esfuerzo asume cada función sin inventar posturas de terceros.

Cada historia HU01 tendrá disposición explícita: VINCULADA_A_PRODUCTO, PRACTICA_A_PRESERVAR, FUERA_DE_ALCANCE_CON_RAZON o PENDIENTE_DE_VALIDACION. No borrar historias de prácticas suficientes o de necesidades minoritarias por no entrar al portafolio.

## FAIR, JANUS y fuentes

Reutiliza la trazabilidad ya conseguida. Evalúa la extensión a datos/productos, sin reiniciar la codificación o fabricar una implementación FAIR/FDO. Separa metadatos de conocimiento y del artefacto, permisos, licencia y acceso. RO-Crate, DataCite, PROV o nanopublicaciones pueden seguir propuestos; cualquier implementación declarada requiere archivo y control reales. El alcance T01 no exige publicarlos.

Conserva prompts/instrucciones, entradas/salidas, versiones, decisiones, incertidumbres y fuentes verificadas como adaptación JANUS. Revisión humana independiente pendiente; no declarar concordancia o saturación. Los prompts de desarrollo de entrevistas se excluirán del repositorio final, los de análisis e integración se conservarán.

Busca y lee fuentes primarias para cada afirmación técnica sustantiva: artículo original, documentación oficial, repositorio de autores o norma aplicable. Registra título, emisor/autores, versión/fecha si constan, URL, consulta, sección y alcance efectivamente leído. No conviertas búsquedas o índices en lectura del artículo completo. Si un recurso falla, registra el intento y usa otra fuente pertinente; no inventes contenido. No transfieras hechos de otra ciudad al corpus. El blog Capybara sirve como ejemplo de articulación argumento–fuente–procedencia, no como evidencia territorial de CDMX o validez de todos sus resultados.

## Contrato de salida JSON

Entrega T01_diseno_v1.json con estas claves. Las listas deben contener objetos completos y explicados; no basta un esqueleto. Los identificadores son estables y únicos dentro de su clase.

- metadatos: tarea T01, resultado_version 1.0, estado DISENO_PARA_REVISION, historias_version 1.1, necesidades_version 1.1, libro_version 1.3, tipo_revision ASISTIDA_POR_LLM, revision_humana_independiente PENDIENTE, implementacion NO_EJECUTADA, modelo/parametros null si no se exponen y explicación de su fuente.
- lectura_entradas: archivo, alcance, comprobacion. decisiones_metodologicas: decision, fundamento, limites.
- fuentes: id T01-Fnnn, titulo, emisor, url, version (null si no consta), consulta, localizador, lectura_efectiva, tipo PRIMARIA o REFERENCIA_METODOLOGICA, estado VERIFICADA o NO_RECUPERADA, limites. Fuentes locales de código usan url pública y archivo_snapshot con ruta real dentro del ZIP. No afirmar revisión por pares por el nombre de un archivo.
- afirmaciones_tecnicas: id T01-Annn, afirmacion, fuentes (ids), localizadores, alcance, aplicacion_local, limites. Cada afirmación debe tener fuente VERIFICADA pertinente, no solo un enlace existente.
- fundamentos_criticos: id T01-Gnnn, concepto, argumento, historias (ids), fuentes (ids), consecuencia_diseno, limites. Desarrolla el conjunto de conceptos de la sección crítica.
- alternativas_agregacion: id T01-Unnn, familia (ocho valores enumerados), pregunta, productos (ids; puede estar vacío con razón), denominador, proceso_generador, jurisdiccion, parametros, estabilidad_temporal, autoria_limites, exclusiones, decision, fuentes (ids), limites.
- practicas_diseno: id T01-Vnnn, practica (cuatro valores enumerados), productos (ids), accion_visible, insumos, comprobacion_propuesta, limites.
- lentes: id T01-Lnnn, lente (cuatro valores), pregunta, historias (ids), productos (ids), datos_requeridos, supuestos, parametros, salida_interpretable, sensibilidad, validacion_futura, estado CONDICIONAL o NO_PERTINENTE_EN_PRODUCTOS_ACTUALES, reconsideracion, herramientas (ids T01-B), fuentes (ids), limites. No declarar método ejecutado.
- herramientas: id T01-Bnnn, nombre, lente (uno de los cuatro), lenguaje, version_documentacion (null si no consta), funcion, requisitos, compatibilidad COMPATIBILIDAD_NO_PROBADA, fuentes (ids), limites. Al menos una candidata documentada por lente; no significa recomendar su despliegue.
- arquitectura: adaptacion_geoinsights (commit exacto, atribucion, licencia, archivos_examinados, se_retoma, se_modifica, no_se_transfiere, limites); modulos (id T01-Mnnn, responsabilidad de las seis enumeradas, nombre, funcion, entradas y salidas como listas de contratos T01-C, control_calidad, faltantes, procedencia, versionado, retorno, limites); conexiones (desde/hacia ids de módulo, tipo FLUJO o RETORNO, objeto, condicion, limites); contratos (id T01-Cnnn, nombre, proposito, campos [{nombre,tipo,significado,unidad,nullable,origen}], controles, procedencia_versiones, limites); representaciones (tipo de las ocho enumeradas, estado CONSIDERADA o NO_NECESARIA_EN_PRODUCTOS_ACTUALES, productos, adaptacion, limites); google_earth_engine (decision, finalidad, productos, fuentes, dependencias, limites). Unidad null significa no pertinente o desconocida con explicación, no campo vacío sin razón.
- productos: id T01-Pnnn, nombre, origen OPORTUNIDAD_PROPUESTA, estado PROPUESTA_NO_IMPLEMENTADA, funcion, usuarios (ids ACT01), historias (ids), necesidades (ids N01), decision, argumento, alcance, exclusiones, datos [{id T01-Dnnn,variable,estado CANDIDATO_DOCUMENTADO o REQUERIDO_NO_DISPONIBLE,fuente (id T01-F o null),acceso,licencia,resolucion_requerida (propuesta explicada o desconocida),limites}], operaciones, modulos (ids), salida_e_interaccion, actividad_humana, responsables_pendientes, incertidumbres, cargas_y_beneficios, criterios [{id T01-Knnn,dado,cuando,entonces,metodo,estado PROPUESTO_NO_EJECUTADO,limites}], condicion_descarte, limites. Dos o tres productos completos.
- cobertura_historias: exactamente 21 objetos {historia,disposicion de las cuatro enumeradas,productos,razon}. Coherencia inversa con los productos y no adjudicar una solución a la persona.
- seleccion_portafolio: criterios, argumento, comparacion_condicional, pendientes. Sin fingir autorización o selección empírica de toda la ciudad.
- extension_fair_janus: medidas, objetos_afectados, controles_propuestos, estados_pendientes, limites. No declara conformidad integral.
- cobertura_requisitos: requisito (id de matriz), estado DESARROLLADO_EN_DISENO o PENDIENTE_CON_RAZON o NO_APLICA_CON_RAZON, objetos (ids T01), razon. Debe cubrir exactamente los 39 requisitos GCR/LEN/DAT; otros requisitos se discuten en prosa sin fabricar cierre de los 208.
- agenda_validacion y limites: listas explicadas; cada agenda incluye objeto, pendiente, comprobacion y alcance. Conserva límites documentales, de muestra, posturas y revisión humana.

Los ids de datos, criterios y módulos no se reutilizan para otra entidad. Las listas de referencias solo usan ids existentes; una referencia no sustituye la explicación. No agregues citas de entrevista no verificadas o registros nuevos. Los originales del corpus y resultados de entrada son inmutables.

## Explicación y soportes

T01_explicacion_v1.md debe desarrollar el argumento con prosa legible, comparaciones y casos concretos. El cuerpo del reporte final no se escribe aún. Incluye una síntesis apta para adaptarse después a diez páginas, y desarrollo técnico amplio en soportes; no intentes insertar todo el esquema en ese cuerpo. Explica cómo cada soporte permite revisar una decisión, sin narrar un checklist.

En T01_soportes_v1.zip incluye LEEME por carpeta; tablas completas derivadas del JSON; fuentes/registro y bibliografía; esquemas/contratos propuestos; matriz de las 21 historias y 39 requisitos; inventario y SHA-256 (excluyendo el propio manifiesto); scripts usados; controles reales; diagramas editables y PNG/PDF exportados. Al menos un diagrama debe explicar la arquitectura con ramas y retornos, y otro vincular los dos/tres productos con decisiones, fuentes y comprobaciones. Marca como propuesta y explica las flechas; no dibujar conexiones institucionales observadas inexistentes. Usa conceptos en los rótulos, ids como apoyo, y comprueba legibilidad. No crear datos estadísticos, mocks presentados como resultados o carpetas vacías.

Las fuentes originales no incluidas se referencian como PAQUETE_ENTRADA con ruta y huella, no se declaran accesibles dentro del ZIP de salida. Si copias código MIT, conserva su licencia. No atribuyas al corpus licencias de fuentes externas. No empaquetes credenciales.

Ejecuta validar_diseno.py con el JSON final. Su control comprueba estructura, cobertura y referencias; no verifica interpretación, bibliografía, contratos semánticos, figuras, adopción o pertinencia técnica. Acompaña cotejos complementarios reales de tablas/figuras/huellas y registro de revisión. No rellenes un control con PASS si no se ejecutó.

```bash
python3 validar_diseno.py . /ruta/T01_diseno_v1.json --salida /ruta/T01_control_validacion.json
```

Entrega cuatro archivos completos: T01_diseno_v1.json; T01_explicacion_v1.md; T01_control_validacion.json; T01_soportes_v1.zip. Conserva respuesta completa. Después se traerán a coordinación para revisión antes de planificar la redacción y el repositorio final. No solicitar aprobación intermedia para trabajo ya autorizado; si falta un dato, avanza con lo que no depende de él y registra la limitación concreta.
