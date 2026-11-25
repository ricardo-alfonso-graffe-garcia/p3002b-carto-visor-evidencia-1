# Contratos propuestos, sin instancias operativas

No son esquemas de las capas SSC. Cada campo conserva tipo, significado, origen, unidad y nulabilidad. Los controles se diseñan aquí; la validación semántica con datos reales es futura.

## Recepción y referencia al original (T01-C001)

**id**: T01-C001

**nombre**: Recepción y referencia al original

**proposito**: Registrar qué se recibió y qué puede utilizarse antes de preparar un derivado.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: referencia_original
  
  **tipo**: string
  
  **significado**: Ruta/URI autorizada al original o referencia física; no promesa de acceso universal.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente aportante

- **nombre**: naturaleza
  
  **tipo**: enum
  
  **significado**: DIGITAL/TEXTO/OBJETO_FISICO/REFERENCIA_EXTERNA. Un objeto físico conserva referencia y custodia, no sustituto digital.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción

- **nombre**: sha256_archivo
  
  **tipo**: string
  
  **significado**: Huella del archivo recibido; null para objeto físico o recurso no materializado, con motivo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Cálculo de integridad

- **nombre**: emisor_y_custodia
  
  **tipo**: object
  
  **significado**: Emisor funcional, receptor y ubicación autorizada de custodia por confirmar.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente/recepción

- **nombre**: ocasion_fuente
  
  **tipo**: object
  
  **significado**: Descripción de ocasión y fecha si consta; fecha desconocida no se completa con fecha de descarga.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Fuente

- **nombre**: acceso_licencia
  
  **tipo**: object
  
  **significado**: Separar permiso de lectura, usos permitidos, licencia y ámbito de difusión; desconocido restringe reutilización.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Aportante o emisor

- **nombre**: uso_solicitado
  
  **tipo**: string
  
  **significado**: Pregunta, finalidad y alcance autorizado para este objeto.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de la tarea

**controles**: - ACEPTAR registro con identidad, fuente y finalidad; acceso autorizado para tarea.

- ADVERTIR licencia o fecha desconocida, conservando motivo.

- DETENER lectura/transformación del contenido si no está autorizado; no interpretar catálogo como payload ni objeto físico como imagen.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. No contiene credenciales, datos de capas SSC ni muestras realmente recibidas.

## Afirmación o referencia unificada (T01-C002)

**id**: T01-C002

**nombre**: Afirmación o referencia unificada

**proposito**: Hacer comparables significados mínimos sin fusionar entidades diferentes.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: sujeto_id
  
  **tipo**: string
  
  **significado**: Entidad sobre la que se afirma; identificador de espacio distinto de acceso, artículo u ocasión.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Original/adaptador

- **nombre**: tipo_entidad
  
  **tipo**: enum
  
  **significado**: SITIO/ACCESO/OCASION/ACTIVIDAD/ACUERDO/OTRO con significado documentado.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Adaptador semántico

- **nombre**: afirmacion
  
  **tipo**: string
  
  **significado**: Contenido original o paráfrasis explícitamente marcada, con localizador.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Original/revisor

- **nombre**: modalidad
  
  **tipo**: enum
  
  **significado**: OBSERVADO/RELATADO/INTERPRETADO/DESEADO/HIPOTETICO; no intercambiables.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente y revisión

- **nombre**: autor_funcional
  
  **tipo**: string
  
  **significado**: Quién afirma y quién interpreta, sin dar a mediador condición de observador.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Original

- **nombre**: tiempo_y_vigencia
  
  **tipo**: object
  
  **significado**: Contexto, fecha con granularidad conocida y vigencia si está respaldada, sin rellenar resolución.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Fuente

- **nombre**: correspondencias
  
  **tipo**: array<object>
  
  **significado**: Entidad origen/destino, criterio, evidencia, estado CONFIRMADA/PROPUESTA/DISPUTADA y versión. Puede estar vacía si no hay unión.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Revisión semántica

**controles**: - ACEPTAR si identidad y significado corresponden a fuente versionada.

- ADVERTIR nombre coincidente sin identidad acreditada: conservar dos candidatos.

- DETENER unión que confunda sitio/acceso o observado/relatado; devolver duda con referencias.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. No transforma desconocimiento o desacuerdo en error. No geocodificar automáticamente por nombre.

## Referencia espacial opcional (T01-C003)

**id**: T01-C003

**nombre**: Referencia espacial opcional

**proposito**: Representar una entidad o partición solo cuando la decisión lo requiere.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: entidad_ref
  
  **tipo**: string
  
  **significado**: Entidad C002 o partición a la que se refiere la geometría.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Revisión

- **nombre**: representacion
  
  **tipo**: enum
  
  **significado**: PUNTO/LINEA/POLIGONO/RASTER/RED o REFERENCIA_VERBAL.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Adaptador fuente

- **nombre**: geometria_o_recurso
  
  **tipo**: object
  
  **significado**: Geometría con tipo/orden de ejes o referencia a archivo raster/red. Null permitido para referencia verbal sin coordenadas.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Fuente

- **nombre**: crs_origen
  
  **tipo**: string
  
  **significado**: Sistema de referencia documentado; no asignar EPSG por parecido o ciudad.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Metadatos de origen

- **nombre**: detalle_calidad
  
  **tipo**: object
  
  **significado**: Resolución, precisión, unidad, método y escala de representación si constan, separados.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Fuente

- **nombre**: cobertura_edicion
  
  **tipo**: object
  
  **significado**: Extensión, emisor, versión/edición y vigencia de la referencia, no prueba de competencia.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente

- **nombre**: papel_y_limites
  
  **tipo**: string
  
  **significado**: Qué representa y para qué se puede usar; sitio no es puerta ni centroide es entrada.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente/revisión

**controles**: - ACEPTAR referencia verbal para consulta textual; coordenadas solo con procedencia.

- ADVERTIR precisión desconocida y límites de representación.

- DETENER distancia/área/intersección si CRS o semántica no acreditados; conservar original antes de conversión, validar ejes, unidad y geometría.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. La unidad de coordenadas depende del CRS documentado. No hay geometrías reales en T01.

## Configuración de selección y agregación (T01-C004)

**id**: T01-C004

**nombre**: Configuración de selección y agregación

**proposito**: Definir una operación después de la pregunta y permitir comparaciones reproducibles.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: pregunta_variable
  
  **tipo**: object
  
  **significado**: Decisión, variable, significado, tipo de medida y unidad.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Diseño acordado

- **nombre**: universo_ids
  
  **tipo**: array<string>
  
  **significado**: Entidades/versiones elegibles y marco de recepción; no población implícita.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C001/C002

- **nombre**: particion_ref
  
  **tipo**: object
  
  **significado**: Identidad y versión de unidad, autoría y finalidad; null si no procede agregación areal.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: C003/revisor

- **nombre**: periodo_alineacion
  
  **tipo**: object
  
  **significado**: Cobertura temporal requerida y tolerancia/regla de comparación; no rellenar fechas ausentes.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Diseño

- **nombre**: operacion_y_parametros
  
  **tipo**: object
  
  **significado**: Regla de suma/media/conteo o comparación, unidades, pesos, bordes/solapes y selección.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Diseño metodológico

- **nombre**: denominador_definicion
  
  **tipo**: object
  
  **significado**: Universo/exposición, numerador compatible, fuente, unidad y periodo; null si solo hay descripción.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Pregunta/fuente

- **nombre**: alternativa_y_cambio
  
  **tipo**: object
  
  **significado**: Configuración contraparte y factor que se cambia; null para operación sin escenario.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Revisión

**controles**: - ACEPTAR operación definida sobre entidades y unidades pertinentes.

- ADVERTIR cambios de cobertura y compatibilidad parcial; no producir comparación silenciosa.

- DETENER suma de tasas, media de porcentajes sin pesos, denominador incompatible o doble conteo de solapes; devolver C011.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. No se fijan radios, tamaños de celda o frecuencias por conveniencia tecnológica.

## Asignaciones y resumen con exclusiones (T01-C005)

**id**: T01-C005

**nombre**: Asignaciones y resumen con exclusiones

**proposito**: Conservar pertenencias y denominadores de un resumen opcional.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: config_ref
  
  **tipo**: string
  
  **significado**: Versión exacta de C004 utilizada.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Agregación

- **nombre**: asignaciones
  
  **tipo**: array<object>
  
  **significado**: Entidad→unidad, peso si justificado, estado ASIGNADA/AMBIGUA/FUERA y motivo; no duplicar como dos personas.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C002/C003/C004

- **nombre**: numerador
  
  **tipo**: number
  
  **significado**: Conteo/medida y unidad indicados en configuración; null si no calculable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Transformación

- **nombre**: denominador
  
  **tipo**: number
  
  **significado**: Valor solo si marco pertinente y conocido; cero distinto de desconocido.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Fuente y transformación

- **nombre**: valor_y_unidad
  
  **tipo**: object
  
  **significado**: Resultado con unidad, método de incertidumbre y sus límites; tasa null si denominador falta o es cero.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Transformación

- **nombre**: exclusiones
  
  **tipo**: array<object>
  
  **significado**: Entidades y motivos de exclusión; resumen numérico solo con marco verificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Agregación

- **nombre**: conciliacion
  
  **tipo**: object
  
  **significado**: Recibidos únicos, asignados, ambiguos y excluidos; motivos pueden solaparse, estados de destino no.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Agregación

**controles**: - ACEPTAR cuando trazas de asignación reconcilian con universo único y configuración.

- ADVERTIR cambios de denominador/periodo frente a otra configuración.

- DETENER tasa con denominador nulo/cero, pérdida silenciosa en join o doble asignación no declarada.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. No incluye resultados estadísticos calculados; igualdad de resumen no demuestra equivalencia de particiones.

## Ocasión, secuencia y afirmación enlazada (T01-C006)

**id**: T01-C006

**nombre**: Ocasión, secuencia y afirmación enlazada

**proposito**: Construir un objeto consultable de P002 sin forzar geometría ni precisión temporal.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: caso_ocasion
  
  **tipo**: object
  
  **significado**: Identidades seudónimas del caso y ocasión y periodo acordado; segunda ocasión solo si se produce voluntariamente.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente autorizada

- **nombre**: contexto_proposito
  
  **tipo**: string
  
  **significado**: Qué se intentaba hacer, desde dónde conceptualmente y qué actividades considera conectadas.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Narración/revisión

- **nombre**: actividades_relaciones
  
  **tipo**: array<object>
  
  **significado**: Actividad con id, relato y enlaces por tipo SECUENCIA/SOLAPAMIENTO/RELACION_NARRADA; orden desconocido sigue marcado.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C002

- **nombre**: tiempos
  
  **tipo**: array<object>
  
  **significado**: Valor o rango, unidad y origen medido/aproximado/relatado; lista vacía si desconocidos. No tratar aproximación como medición exacta.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente

- **nombre**: afirmaciones_respaldo
  
  **tipo**: array<object>
  
  **significado**: Qué se pretende sostener y qué fragmentos lo apoyan o limitan.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Equipo de análisis

- **nombre**: alternativas_no_reconstruidas
  
  **tipo**: array<object>
  
  **significado**: Opciones desconocidas, no recordadas o no abordadas sin afirmar inexistencia.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente/revisión

- **nombre**: unidad_comparacion
  
  **tipo**: object
  
  **significado**: Salida completa/actividad puntual, criterio y condiciones que limitan comparación.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Decisión analítica

**controles**: - ACEPTAR reconstrucción con procedencia y unidad explícita incluso sin mapa o fecha exacta.

- ADVERTIR comparabilidad parcial y diferencias observado/relatado.

- DETENER comparación numérica de tiempos con orígenes/unidades incompatibles; no borrar relato para resolver incompatibilidad.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. No datos de seguimiento producidos; la responsabilidad académica permanece en equipo.

## Revisión explicable de un registro (T01-C007)

**id**: T01-C007

**nombre**: Revisión explicable de un registro

**proposito**: Construir el expediente P001 con cambio, respaldo y duda sin sustituir la decisión técnica.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: registro_revision
  
  **tipo**: object
  
  **significado**: Registro de sitio y versiones antes/después pertinentes; no inventar que dos copias causaron incidente.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C001/C002

- **nombre**: alcance_encargo
  
  **tipo**: string
  
  **significado**: Qué se revisa y qué no se está verificando en campo o decidiendo sobre visitas.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Petición

- **nombre**: diferencias
  
  **tipo**: array<object>
  
  **significado**: Campo o sentido antes/después; distingue identidad, descripción, acceso, ubicación y conservación sin cambio.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Revisor

- **nombre**: fundamento
  
  **tipo**: array<object>
  
  **significado**: Referencias al respaldo y qué parte de decisión sostiene cada una, con quién observó/relató.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Revisor

- **nombre**: decision_humana
  
  **tipo**: enum
  
  **significado**: CONSERVAR/MODIFICAR/DETENER/PENDIENTE con responsable y razón en objeto asociado.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable técnico

- **nombre**: duda_pertinente
  
  **tipo**: object
  
  **significado**: Pregunta surgida en revisión que afecta interpretar entrega; no lista infinita de todo desconocido.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Revisor

- **nombre**: referencias_espaciales
  
  **tipo**: array<string>
  
  **significado**: Referencias C003 opcionales; vacío cuando el texto basta.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C003

**controles**: - ACEPTAR conservar sin cambio con fundamento; no exigir movimiento visible para acreditar revisión.

- ADVERTIR nota anterior para nuevo encargo: revalidar alcance.

- DETENER modificación que solo obedece a diferencia de calle sin resolver identidad; requerir revisión humana antes de producir nueva versión.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. No sincroniza automáticamente otras bases ni ofrece ingreso seguro por cualquier acceso.

## Acuerdo cultural y memoria situada (T01-C008)

**id**: T01-C008

**nombre**: Acuerdo cultural y memoria situada

**proposito**: Construir P003 para preparar qué retomar y qué confirmar.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: espacio_y_propuesta
  
  **tipo**: object
  
  **significado**: Referencia funcional al espacio y propósito cultural; identidad no exige coordenadas.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Fuente/revisión

- **nombre**: interlocucion_funcional
  
  **tipo**: object
  
  **significado**: Con qué rol se habló y vía autorizada, sin inventar nombre/contacto ni atribuir propiedad.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Acuerdo

- **nombre**: hecho_y_ocasion
  
  **tipo**: object
  
  **significado**: Contenido, contexto temporal y fuente; separa dicho antes de notas propias después.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C002

- **nombre**: estado_acuerdo
  
  **tipo**: enum
  
  **significado**: POSIBILIDAD/CONFIRMADO/IDEA/PENDIENTE/CERRADO, con alcance por fecha y función.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Personas que confirman

- **nombre**: fecha_franja_vigencia
  
  **tipo**: object
  
  **significado**: Fecha concreta solo si aportada y necesaria para anunciar; franjas descriptivas y fecha de confirmación distintas.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Fuente

- **nombre**: preguntas_revalidacion
  
  **tipo**: array<object>
  
  **significado**: Qué confirmar con quién antes de otra propuesta; pregunta abierta no se vuelve compromiso.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Coordinación

- **nombre**: comunicacion_participacion
  
  **tipo**: object
  
  **significado**: Qué puede decir invitación/recepción: escuchar basta, escribir optativo, sesión autónoma; requiere cotejo humano.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Mediación/coordinación

**controles**: - ACEPTAR nota situada con fuente y alcance y una idea sin fecha como IDEA.

- ADVERTIR descripción antigua y vigencia no confirmada.

- DETENER anuncio propuesto si fecha/uso/equipo pertinentes no están confirmados; no traducir interés parcial en asistencia o disposición colectiva.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. Escribir notas no sustituye construir sentido cultural, escuchar anfitriones o visitar cuando haga falta.

## Comparación o lectura analítica con límites (T01-C009)

**id**: T01-C009

**nombre**: Comparación o lectura analítica con límites

**proposito**: Relacionar material preparado con la decisión posible, sin ejecutar métodos innecesarios.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: pregunta_y_unidad
  
  **tipo**: object
  
  **significado**: Pregunta y nivel de afirmación, evitando inferencia individual desde áreas.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C004/C006/C007/C008

- **nombre**: objetos_comparados
  
  **tipo**: array<string>
  
  **significado**: Identidades/versiones, regla de comparabilidad y enlaces; puede ser una sola revisión a interpretar.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Construcción

- **nombre**: metodo_config
  
  **tipo**: object
  
  **significado**: Lectura humana estructurada o método numérico si en futuro se autoriza y justifica; distinguir estado.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Análisis

- **nombre**: hallazgo_o_pendiente
  
  **tipo**: string
  
  **significado**: Afirmación acotada o razón por la que no puede formularse; ningún resultado territorial en este diseño.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Análisis/revisión

- **nombre**: incertidumbres_exclusiones
  
  **tipo**: array<object>
  
  **significado**: Tipo y origen: error/incertidumbre/desconocimiento/desacuerdo; no confianza porcentual sin método.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Todas las etapas

- **nombre**: sensibilidad
  
  **tipo**: object
  
  **significado**: Configuraciones y diferencias/estabilidad si se calculan en fase futura; null si no ejecutado.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Análisis

- **nombre**: decision_por_tomar
  
  **tipo**: string
  
  **significado**: Quién debería interpretar para conservar, acotar, revalidar o descartar; responsabilidad por confirmar.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Actividad humana

**controles**: - ACEPTAR lectura acotada y estado pendiente explícito.

- ADVERTIR cambio de unidad o selección; no esconderlo en nota técnica.

- DETENER causalidad, equivalencia jurídica o recomendación de despliegue no sostenida por respaldo.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. Objeto de lectura humana de backend; no es aprobación ni un dashboard implementado.

## Salida de consulta y devolución (T01-C010)

**id**: T01-C010

**nombre**: Salida de consulta y devolución

**proposito**: Preparar el mínimo que una interfaz o documento debe comunicar, con trazas a respaldos.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: producto_audiencia
  
  **tipo**: object
  
  **significado**: Identidad del producto, personas/roles y ámbito de acceso.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Diseño

- **nombre**: contenido_versionado
  
  **tipo**: object
  
  **significado**: Vista textual, tabla o mapa opcional con título, leyenda y versión, preparado desde lectura analítica.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C009

- **nombre**: interacciones
  
  **tipo**: array<object>
  
  **significado**: Acciones pertinentes: buscar, comparar, abrir respaldo autorizado y formular duda; no modificación directa de original.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Diseño

- **nombre**: limites_visibles
  
  **tipo**: array<string>
  
  **significado**: Dudas, denominadores y cobertura cuando apliquen, más propósito y exclusiones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: C009

- **nombre**: traza_salida
  
  **tipo**: array<object>
  
  **significado**: Ruta de cada afirmación a contratos/entradas/configuración, con permisos separados.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Procedencia

- **nombre**: revision_y_devolucion
  
  **tipo**: object
  
  **significado**: Revisión humana por realizar, destinatario por confirmar y canal; no envío automático.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable pendiente

**controles**: - ACEPTAR vista con significado comprensible sin conocer ids.

- ADVERTIR referencia cuyo respaldo requiere autorización; mostrar metadato permitido y motivo.

- DETENER difusión si excede permisos o si presenta propuesta como observación/implementación.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. Puede ser documento sencillo; la interfaz no ejecuta decisiones humanas ni garantiza condiciones actuales.

## Duda, incidencia o corrección sin sobrescritura (T01-C011)

**id**: T01-C011

**nombre**: Duda, incidencia o corrección sin sobrescritura

**proposito**: Permitir retornos entre responsabilidades y revisión humana.

**campos**: - **nombre**: objeto_id
  
  **tipo**: string
  
  **significado**: Identidad local estable de esta entidad; no PID externo.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: version
  
  **tipo**: string
  
  **significado**: Versión inmutable; cambio crea versión con padre identificable.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Registro propuesto

- **nombre**: fuentes_versionadas
  
  **tipo**: array<object>
  
  **significado**: Identidades, versiones, localizadores y huellas de fuentes utilizadas, sin duplicar como corroboraciones.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Recepción y transformaciones

- **nombre**: nulos_motivos
  
  **tipo**: object
  
  **significado**: Mapa campo→DESCONOCIDO/NO_APLICA/NO_APORTADO/RESTRINGIDO y explicación; vacío solo cuando no hay nulos.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Responsable de recepción/revisión

- **nombre**: objeto_cuestionado
  
  **tipo**: object
  
  **significado**: Identidad, versión y campo afectado; fuente original permanece.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Cualquier etapa

- **nombre**: tipo_y_motivo
  
  **tipo**: object
  
  **significado**: Error verificable, incertidumbre, desconocimiento o desacuerdo y evidencia de por qué importa.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Control/persona

- **nombre**: destino_funcional
  
  **tipo**: string
  
  **significado**: Responsabilidad pertinente para aclarar, por confirmar; no canal público indiscriminado.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Revisión

- **nombre**: propuesta_correccion
  
  **tipo**: object
  
  **significado**: Cambio o pregunta propuesta con fundamento, sin aprobación automática.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: True
  
  **origen**: Revisor

- **nombre**: estado_resolucion
  
  **tipo**: enum
  
  **significado**: ABIERTA/RESPONDIDA/NO_RESUELTA/RETIRADA_CON_RAZON, con historial y explicación.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Revisión

- **nombre**: derivados_afectados
  
  **tipo**: array<string>
  
  **significado**: Identidades de salidas que deben advertirse o reconstruirse al cambiar una fuente.
  
  **unidad**: null — motivo explicado en el campo/contrato correspondiente.
  
  **nullable**: False
  
  **origen**: Procedencia

**controles**: - ACEPTAR objeción localizada aunque no esté resuelta.

- ADVERTIR salidas afectadas por duda nueva.

- DETENER propagación de corrección sin respaldo y autoría; crear versión y repetir solo operaciones afectadas después de revisar.

**procedencia versiones**: Cada salida conserva identidad/versiones de entradas, actividad, configuración, responsable funcional por confirmar, fecha de transformación y huella de archivo cuando exista. No sobrescribir originales. Unidad null en identificadores/textos/estados significa no pertinente; en geometría/tiempo/calidad significa desconocida o expresada en subcampo explícito y exige motivo.

**limites**: CONTRATO_PROPUESTO, sin instancia de datos de producto ni conformidad normativa ejecutada. El retorno solicita aclaración pertinente; no obliga a recabar toda información faltante ni acredita respuesta de terceros.