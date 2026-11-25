# Lentes · Diseño para revisión

## SCAN (T01-L001)

**id**: T01-L001

**lente**: SCAN

**pregunta**: Extensión hipotética de P001: ¿se concentran registros con discrepancias de identificación entre los registros realmente revisados, para decidir dónde ampliar la comprobación humana? No equivale a riesgo delictivo ni acceso inseguro.

**historias**: - HU01-H001

- HU01-H003

**productos**: - T01-P001

**datos requeridos**: Evento: registro revisado con discrepancia definida por protocolo común; control: registro revisado comparable sin discrepancia. Marco de todos los revisados, coordenadas o unidades con pertenencia conocida y periodos de revisión. Bernoulli si hay casos/controles; Poisson solo con conteos y exposición pertinente justificada. Nada de esto está aportado como conjunto operativo.

**supuestos**: Unidad: revisión de registro en un periodo, deduplicada según protocolo. Nula Bernoulli: probabilidad de discrepancia constante entre revisados, condicionado al total y ajustes predefinidos. La selección de revisiones debe ser conocida: concentración de comprobaciones no es incidencia territorial del fenómeno.

**parametros**: Declarar ventanas circulares/alternativa justificada, centros y máximo de población revisada, búsqueda alta/baja, covariables y réplica/semilla. Empezar con análisis puramente espacial en periodo fijo; si se justifica espacio-tiempo, fijar intervalo y ventana temporal según disponibilidad real, sin heredar días epidemiológicos.

**salida interpretable**: Ventana candidata, observados/esperados y evidencia bajo modelo para orientar revisión. Responsable debe decidir si tiene capacidad/competencia para actuar; no inferir causa.

**sensibilidad**: Comparar ventanas máximas y unidad base, exposición, localizaciones dudosas, exclusiones y fechas. Usar contraste de máximos Monte Carlo para la búsqueda elegida; registrar todas las configuraciones y controlar adicionalmente análisis sucesivos/múltiples hipótesis, sin escoger el p menor.

**validacion futura**: Primero auditar marco, selección y clasificación de eventos; probar con casos de referencia del método y calcular desempeño/potencia con diseño acordado; luego contrastar hallazgos con revisión independiente. Pruebas aún no ejecutadas.

**estado**: NO_PERTINENTE_EN_PRODUCTOS_ACTUALES

**reconsideracion**: Solo si existe conjunto de revisiones con controles/exposición, una decisión de priorización territorial y responsable que pueda actuar; la tarea actual se resuelve por evidencia del caso.

**herramientas**: - T01-B001

**fuentes**: - T01-F004

- T01-F005

- T01-F001

**limites**: Detectar concentración no explica mecanismo, corrige subregistro o elimina MAUP; no escanear los cinco perfiles como puntos.

## POTENCIA_ESCALAMIENTO (T01-L002)

**id**: T01-L002

**lente**: POTENCIA_ESCALAMIENTO

**pregunta**: Extensión de mantenimiento de P001: ¿cómo cambia el esfuerzo verificable al crecer el número de registros que se revisan? Otra pregunta distinta sería si las duraciones de revisión muestran una cola pesada. Ninguna fue demandada como estudio por E01.

**historias**: - HU01-H002

- HU01-H003

**productos**: - T01-P001

**datos requeridos**: Para relación Y=a·N^beta: conjuntos comparables con tamaño N, esfuerzo Y y condiciones de revisión registradas; para distribución p(x) proporcional a x^-alpha: observaciones positivas de duración con censura, dependencia y proceso de selección conocidos. El corpus no proporciona esa muestra.

**supuestos**: Unidad relacional: lote/periodo comparable, sin confundir dificultad con tamaño; distributiva: duración por tarea con dominio x>=xmin y soporte discreto/continuo adecuado. No asumir independencia cuando tareas comparten responsable o material.

**parametros**: Relación: dominio de tamaños, modelo de error y estimación beta/a con incertidumbre; comparar relación lineal y alternativas no potenciales. Distribución: estimar alpha/xmin por máxima verosimilitud y criterio de ajuste, evaluar tamaño efectivo de cola, truncamiento y rango de observación.

**salida interpretable**: Estimación e intervalo y diagnóstico para evaluar si la forma resumida es defendible; no coeficiente normativo de productividad ni presupuesto inventado.

**sensibilidad**: Comparar lognormal, exponencial y potencial truncada cuando proceda; KS con remuestreo paramétrico para ajuste y razones de verosimilitud para alternativas. Revisar dominio, ceros, censura, dependencia, heterogeneidad y residuos en regresión; recta log–log no basta.

**validacion futura**: Antes de estimar, justificar muestra mediante precisión/potencia y suficiente variación, sin mínimo mágico; separar ajuste y evaluación, revisar tareas extremas con fuentes y mostrar qué cambia bajo unidades de lote distintas.

**estado**: NO_PERTINENTE_EN_PRODUCTOS_ACTUALES

**reconsideracion**: Pregunta explícita de mantenimiento, registros de esfuerzo autorizados y comparables y cantidad efectiva de observaciones que permita distinguir modelos. No extender exponentes de ciudades a estos casos.

**herramientas**: - T01-B002

**fuentes**: - T01-F006

- T01-F007

- T01-F008

**limites**: 21 historias no son una muestra de duraciones ni ciudades. powerlaw cubre distribuciones; una relación entre magnitudes requiere análisis estadístico separado y diagnóstico de error.

## TDA (T01-L003)

**id**: T01-L003

**lente**: TDA

**pregunta**: En una extensión de P002 con muchas ocasiones comparables: ¿aparecen formas de similitud entre perfiles que ayuden a formular contrastes y volver a los relatos? La primera comparación de dos ocasiones no necesita Mapper.

**historias**: - HU01-H004

- HU01-H005

- HU01-H006

**productos**: - T01-P002

**datos requeridos**: Matriz por ocasión, variables acordadas: actividades, secuencia representable, tiempo disponible/carga solo si realmente medidos o categorías explícitas, fuente y desconocidos. No convertir relatos íntegros en embeddings sin justificar pérdida de significado. Sin matriz aportada.

**supuestos**: Unidad: ocasión descrita bajo pauta común. Normalizar variables cuantitativas para evitar dominio por unidades; categorías requieren codificación/métrica justificada (p.ej. distancia mixta a evaluar). No imputar desconocido como 0. Mapper es una construcción, distinta de homología persistente con filtraciones; esta última no se propone para portafolio actual.

**parametros**: Definir métrica y normalización con equipo, filtro interpretable (p.ej. dimensión de actividades cuando sea válida), cobertura por intervalos superpuestos y agrupamiento en preimágenes (algoritmo y parámetros). No heredar 8 intervalos, 40% o altura 70 del código epidemiológico.

**salida interpretable**: Nodos contienen ocasiones; aristas señalan miembros compartidos por solapamiento de cobertura. Explorar miembros y palabras de origen. Cercanía de perfiles o del dibujo no es proximidad geográfica, desplazamiento o relación causal.

**sensibilidad**: Variables/codificación, normalización, métrica, filtro, intervalos, solapamiento y agrupamiento; contrastar estabilidad de miembros y estructura bajo variaciones y remuestreo adecuado por caso; no contar pertenencias repetidas como observaciones nuevas.

**validacion futura**: Comenzar por comparación de tablas y relatos; si hay volumen y pregunta que lo justifiquen, verificar cada pertenencia y arista, comparar con agrupamiento simple y revisar interpretaciones con equipo sin exigir acuerdo académico total a participantes.

**estado**: CONDICIONAL

**reconsideracion**: Solo tras validar utilidad del cuaderno básico, producir voluntariamente matriz comparable y justificar necesidad de exploración multivariable. Si codificar aplana contexto o añade carga desproporcionada, descartar.

**herramientas**: - T01-B003

**fuentes**: - T01-F009

- T01-F027

- T01-F026

**limites**: No TDA ejecutado; documentación no garantiza inmunidad a ruido, nulos o métrica. mapperKD externo no ha sido recuperado ni reemplazado por kmapper.

## ABM (T01-L004)

**id**: T01-L004

**lente**: ABM

**pregunta**: Extensión hipotética de coordinación cultural: ¿qué condiciones de agenda permitirían sostener una serie bajo distintas reglas de confirmación? No predecir preferencias o asistencia de una comunidad a partir de una coordinadora.

**historias**: - HU01-H007

- HU01-H011

- HU01-H012

**productos**: - T01-P003

**datos requeridos**: Agentes funcionales: coordinación, mediación y gestión del espacio; participantes solo si se justifica pregunta y datos consentidos. Ambiente: espacios y calendarios; recursos/capacidades, reglas y registros de decisiones repetidas para calibrar/contrastar. No aportados; voces de terceros no entrevistadas.

**supuestos**: Regla candidata a discutir: una fecha pasa de posibilidad a confirmada cuando cada función pertinente confirma disponibilidad/uso y sentido de propuesta. Interacción por intercambio de confirmaciones; cancelar o reformular si no se sostienen condiciones. No convertir silencio en rechazo ni disponibilidad en voluntad.

**parametros**: Unidad: ocasión de concertación, con paso por evento y orden de actualización declarados; tiempos de respuesta, cambios de agenda y capacidad por documentar, distribuciones solo con fuente. Semillas/réplicas, inicialización y horizonte; no números tomados del corpus como calibración.

**salida interpretable**: Escenarios condicionales de fechas sostenibles, pendientes y carga de revalidación bajo reglas explícitas, sin pronóstico cierto ni efectos causales de política. Primero comparar si una tabla de acuerdos ya responde.

**sensibilidad**: Reglas alternativas, orden de activación, tiempos de respuesta, heterogeneidad, información faltante y condiciones iniciales; separar variación aleatoria de incertidumbre estructural y de parámetros, sin ocultarlas con una única trayectoria.

**validacion futura**: Descripción ODD, revisión de reglas con funciones pertinentes, verificación de estados y eventos, casos límite, calibración con registros autorizados y evaluación con ocasiones separadas/no usadas para ajustar. Si no existen observaciones suficientes, no validar por parecido visual.

**estado**: NO_PERTINENTE_EN_PRODUCTOS_ACTUALES

**reconsideracion**: Decisión de escenarios que no resuelva el expediente de acuerdos y disponibilidad de reglas/observaciones de varias ocasiones, con pertinencia y participación acordadas. Puede descartarse por coste y reducción excesiva del sentido cultural.

**herramientas**: - T01-B004

**fuentes**: - T01-F010

- T01-F011

- T01-F012

**limites**: No agentes ni simulaciones ejecutados. No se infiere una cadena entre casos, ni el poder de la coordinadora para comprometer a otros.

