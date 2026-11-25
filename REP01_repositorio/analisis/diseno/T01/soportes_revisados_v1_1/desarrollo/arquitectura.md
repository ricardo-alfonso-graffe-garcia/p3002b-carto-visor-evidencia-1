# Arquitectura propuesta · Lectura técnica completa

**contratos**: - **id**: T01-C001
  
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

- **id**: T01-C002
  
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

- **id**: T01-C003
  
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

- **id**: T01-C004
  
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

- **id**: T01-C005
  
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

- **id**: T01-C006
  
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

- **id**: T01-C007
  
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

- **id**: T01-C008
  
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

- **id**: T01-C009
  
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

- **id**: T01-C010
  
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

- **id**: T01-C011
  
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

**modulos**: - **id**: T01-M001
  
  **responsabilidad**: EXTRACCION
  
  **nombre**: Recibir y delimitar uso
  
  **funcion**: Recibir fuentes autorizadas o registrar su falta, conservar original y acceso; adaptador por fuente/soporte, no descarga universal.
  
  **entradas**: - T01-C001
  
  **salidas**: - T01-C001
  
  - T01-C011
  
  **control calidad**: Validar archivo íntegro, tipo real, permisos y procedencia, distinguir catálogo y contenido.
  
  **faltantes**: Fuente ausente queda REQUERIDO_NO_DISPONIBLE; no crear coordenadas ni notas testimoniales.
  
  **procedencia**: La actividad de recibir no es observar el fenómeno; preservar emisor y fecha real de fuente.
  
  **versionado**: Identidad de paquete/archivo/versión y huella separadas.
  
  **retorno**: Duda a aportante solo mediante función y autorización futura; no se contacta a nadie ahora.
  
  **limites**: Responsabilidad modular PROPUESTA; no describe una unidad organizativa observada ni un servicio ya implementado. Fuentes externas, actividad humana e interfaz no se confunden con cálculo de backend.

- **id**: T01-M002
  
  **responsabilidad**: UNIFICACION
  
  **nombre**: Aclarar identidades y significados
  
  **funcion**: Mapear campos con diccionario explícito; separar sitio/acceso, observado/relatado y ocasión/resolución. Uniones solo con correspondencias justificadas.
  
  **entradas**: - T01-C001
  
  - T01-C011
  
  **salidas**: - T01-C002
  
  - T01-C003
  
  - T01-C011
  
  **control calidad**: Validar significado, tipo, cardinalidad de joins y unidades; no imponer coincidencia geométrica.
  
  **faltantes**: Null con motivo; referencia verbal válida sin geometría; CRS desconocido bloquea operación espacial.
  
  **procedencia**: Mapa campo origen→destino con transformaciones y fuente, sin borrar texto o versiones.
  
  **versionado**: Versionar adaptador y vocabulario, conservar campos originales.
  
  **retorno**: Errores a EXTRACCION; desacuerdos conservados con alternativa en C011.
  
  **limites**: Responsabilidad modular PROPUESTA; no describe una unidad organizativa observada ni un servicio ya implementado. Fuentes externas, actividad humana e interfaz no se confunden con cálculo de backend.

- **id**: T01-M003
  
  **responsabilidad**: AGREGACION
  
  **nombre**: Seleccionar unidades y conservar exclusiones
  
  **funcion**: Rama optativa para asignación/resumen espacial o conteo pertinente; aplicar C004 manteniendo miembros y denominador, no paso obligatorio para notas.
  
  **entradas**: - T01-C002
  
  - T01-C003
  
  - T01-C004
  
  - T01-C011
  
  **salidas**: - T01-C005
  
  - T01-C011
  
  **control calidad**: Reconciliar recibidos únicos/asignados/ambiguos/excluidos, periodos, borde y peso; no media simple de tasas.
  
  **faltantes**: No asignar nulos a celda cero ni reemplazar población faltante; descripción sin tasa cuando proceda.
  
  **procedencia**: Salida enlaza cada miembro, configuración y partición exactas.
  
  **versionado**: Cambiar tamaño/origen/periodo genera escenario/versiones, nunca reemplaza referencia.
  
  **retorno**: Ambigüedad geométrica o semántica a UNIFICACION; revisar configuración por duda de ANALISIS.
  
  **limites**: Responsabilidad modular PROPUESTA; no describe una unidad organizativa observada ni un servicio ya implementado. Fuentes externas, actividad humana e interfaz no se confunden con cálculo de backend.

- **id**: T01-M004
  
  **responsabilidad**: CONSTRUCCION
  
  **nombre**: Enlazar episodios, revisiones y acuerdos
  
  **funcion**: Construir expediente de cambios, ocasión/afirmación o memoria de acuerdos. Puede recibir directamente referencias unificadas y saltar agregación.
  
  **entradas**: - T01-C001
  
  - T01-C002
  
  - T01-C003
  
  - T01-C005
  
  - T01-C011
  
  **salidas**: - T01-C006
  
  - T01-C007
  
  - T01-C008
  
  - T01-C011
  
  **control calidad**: Cotejar identidad y apoyos, modalidad y orden; no transformar hipótesis en evento.
  
  **faltantes**: Un expediente puede conservar pregunta pendiente; segunda ocasión o confirmación no aportada no se simula.
  
  **procedencia**: Enlaces a fuente por afirmación/actividad, sin considerar duplicados de JSON como voces independientes.
  
  **versionado**: Versionar objeto construido y decisión interpretativa; conservar versión anterior.
  
  **retorno**: Contradicción o pregunta pertinente a UNIFICACION y, si falta original, EXTRACCION.
  
  **limites**: Responsabilidad modular PROPUESTA; no describe una unidad organizativa observada ni un servicio ya implementado. Fuentes externas, actividad humana e interfaz no se confunden con cálculo de backend.

- **id**: T01-M005
  
  **responsabilidad**: ANALISIS
  
  **nombre**: Examinar comparabilidad y suficiencia
  
  **funcion**: Preparar lectura estructurada con intervención humana; evaluar alcance de afirmaciones o sensibilidad si se justifica en fase siguiente. Cuatro lentes son evaluados, sin ejecución obligatoria.
  
  **entradas**: - T01-C004
  
  - T01-C005
  
  - T01-C006
  
  - T01-C007
  
  - T01-C008
  
  - T01-C011
  
  **salidas**: - T01-C009
  
  - T01-C011
  
  **control calidad**: Verificar nivel de inferencia, denominadores, muestra y método; acotar, no concluir causalidad por mapa.
  
  **faltantes**: Sin insumo suficiente, salida pendiente/reducida; falta de datos no dispara un modelo para rellenar.
  
  **procedencia**: Relacionar objeto, método, configuración, autor de interpretación y evidencia que limita.
  
  **versionado**: Versionar memo y configuración/semilla si futura ejecución; ninguna semilla inventada ahora.
  
  **retorno**: Duda de unidad a AGREGACION; de significado/soporte a CONSTRUCCION/UNIFICACION.
  
  **limites**: Responsabilidad modular PROPUESTA; no describe una unidad organizativa observada ni un servicio ya implementado. Fuentes externas, actividad humana e interfaz no se confunden con cálculo de backend.

- **id**: T01-M006
  
  **responsabilidad**: PRODUCTOS
  
  **nombre**: Preparar consulta y devolución
  
  **funcion**: Producir vistas mínimas y artefacto para revisión de P001/P002/P003; backend prepara y controla datos, interfaz permite consultar, personas deciden y conversan.
  
  **entradas**: - T01-C006
  
  - T01-C007
  
  - T01-C008
  
  - T01-C009
  
  - T01-C011
  
  **salidas**: - T01-C010
  
  - T01-C011
  
  **control calidad**: Cotejar tabla/texto/mapa con lectura autorizada, leyenda, versión y permisos; no difundir por defecto.
  
  **faltantes**: Mostrar pendiente y límite, no esconderlos tras pantalla vacía o colores de magnitud.
  
  **procedencia**: Salida vuelve a fuentes y revisiones; metadato del artefacto distinto de conocimiento representado.
  
  **versionado**: Salida identifica versión del diseño, objetos y configuración; retirar/advertir salida afectada, no cambiar pasado.
  
  **retorno**: Persona puede cuestionar representación o respaldo mediante C011 a ANALISIS/CONSTRUCCION. Ninguna aprobación implicada por consultar.
  
  **limites**: Responsabilidad modular PROPUESTA; no describe una unidad organizativa observada ni un servicio ya implementado. Fuentes externas, actividad humana e interfaz no se confunden con cálculo de backend.

**conexiones**: - **desde**: T01-M001
  
  **hacia**: T01-M002
  
  **tipo**: FLUJO
  
  **objeto**: Original autorizado y contexto C001
  
  **condicion**: Solo tras comprobar recepción y permiso.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M002
  
  **hacia**: T01-M003
  
  **tipo**: FLUJO
  
  **objeto**: Referencias C002/C003 y configuración C004
  
  **condicion**: Solo si la pregunta requiere resumen/asignación; P001 opcional.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M002
  
  **hacia**: T01-M004
  
  **tipo**: FLUJO
  
  **objeto**: Referencias y notas C001/C002/C003
  
  **condicion**: Rama directa para revisiones, ocasiones y acuerdos; no polígonos obligatorios.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M003
  
  **hacia**: T01-M004
  
  **tipo**: FLUJO
  
  **objeto**: Asignaciones, resumen y exclusiones C005
  
  **condicion**: Si el resumen aporta a construir la lectura.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M003
  
  **hacia**: T01-M005
  
  **tipo**: FLUJO
  
  **objeto**: Resumen y escenario C004/C005
  
  **condicion**: Comparación de unidades puede saltar construcción adicional de episodio.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M004
  
  **hacia**: T01-M005
  
  **tipo**: FLUJO
  
  **objeto**: Ocasiones/revisiones/acuerdos C006–C008
  
  **condicion**: Lectura de comparabilidad, suficiencia o vigencia.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M004
  
  **hacia**: T01-M006
  
  **tipo**: FLUJO
  
  **objeto**: Ocasiones/revisiones/acuerdos C006–C008
  
  **condicion**: Consulta descriptiva puede saltar análisis numérico; requiere revisión de límites y procedencia.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M005
  
  **hacia**: T01-M006
  
  **tipo**: FLUJO
  
  **objeto**: Lectura con límites C009
  
  **condicion**: Solo si es comprensible y sus fuentes/estado están identificados.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M006
  
  **hacia**: T01-M005
  
  **tipo**: RETORNO
  
  **objeto**: Duda de lectura o representación C011
  
  **condicion**: Cuando una persona o control cuestione salida.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M006
  
  **hacia**: T01-M004
  
  **tipo**: RETORNO
  
  **objeto**: Duda de contenido de nota C011
  
  **condicion**: Si falta distinguir cambio/ocasión/acuerdo.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M005
  
  **hacia**: T01-M003
  
  **tipo**: RETORNO
  
  **objeto**: Duda de unidad/denominador C011
  
  **condicion**: Reformular configuración, conservar alternativas.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M005
  
  **hacia**: T01-M004
  
  **tipo**: RETORNO
  
  **objeto**: Duda de afirmación C011
  
  **condicion**: Volver a evidencia y acotar.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M004
  
  **hacia**: T01-M002
  
  **tipo**: RETORNO
  
  **objeto**: Identidad o significado disputado C011
  
  **condicion**: Conservar dos versiones hasta aclaración.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M003
  
  **hacia**: T01-M002
  
  **tipo**: RETORNO
  
  **objeto**: Pertenencia ambigua o CRS faltante C011
  
  **condicion**: No asignar por fuerza.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

- **desde**: T01-M002
  
  **hacia**: T01-M001
  
  **tipo**: RETORNO
  
  **objeto**: Fuente/permiso no resuelto C011
  
  **condicion**: Buscar aclaración pertinente futura sin sobrescribir original.
  
  **limites**: Flecha de arquitectura propuesta; no transferencia institucional observada entre personas entrevistadas.

**adaptacion geoinsights**: **commit**: ab60b86a6a87bca0dd370c7c4af3ada4185d187e

**atribucion**: COVID-19 GeoInsights Mobility Pipeline, DataLama Team, 2020–2021.

**licencia**: MIT para código/documentación de referencia; licencia preservada en fuentes/LICENSE_GeoInsights. No se copió código ejecutable al diseño.

**archivos examinados**: - **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/README.md
  
  **alcance**: Completo; Architecture, Configuration, External data, Citation, Credits.
  
  **sha256**: 06ac7a3d941695f3e4ae9e32f9efb432c15290f5e0ef25e1e2e7c9291a433fc3

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/excecute_all.py
  
  **alcance**: Completo, líneas 1–141; etapas 16, CSV 21, PRE 24–55, bucle 75–100, POS 121–128.
  
  **sha256**: 8596f9e8e988179ab4605300a8704470df159ba3da062af56e5a6fba7ce5ca4a

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/unifiers/universal_generic_unifier.py
  
  **alcance**: Completo, 1–178; selección 44 y DEBUG 82–84.
  
  **sha256**: 1b468e9f313086f990106029ee7686348184ad805dc4b06eb6233647da30a4c8

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/agglomerators/universal_geometry_agglomerate.py
  
  **alcance**: Completo, 1–206; within/inner 105, 126–130; population mock 144–146.
  
  **sha256**: 5a1c35725f590354e6d323b6e7d54a5391f533a50d978a7ba33acb23a5fd2ff6

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/agglomerators/universal_radius_agglomerate.py
  
  **alcance**: Completo, 1–151; radio 25/47, función delegada 73, agrupación diaria 115–118.
  
  **sha256**: fafa3f532b2bd01cc7bc47ac9df4d661ba2a13cc0104149e68d41628cb280e22

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/agglomerators/universal_community_agglomerate.py
  
  **alcance**: Completo, 1–252; llamada R 58–69; mapa 95; atributo/esquema 108–155; population 170–173 comentado.
  
  **sha256**: 17c1591f4c3642d839fda0b22545b12c9fcb2c3de2730d127e68ad6248b995e3

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/constructors/universal_daily_graphs_constructor.py
  
  **alcance**: Completo, 1–131; build_graphs 86, matriz de distancias comentada 99–101.
  
  **sha256**: 125677ae1a45dda9867bc2bbe9050405652a2051646710ac33b1bfb7265c3d70

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/analysis/tda_script.R
  
  **alcance**: Completo, 1–228; mapper externo 16–24, matriz 102, filtros y parámetros 123–208.
  
  **sha256**: deb24a2f57d37f1208901d6028588c8997a7c196f4157f07fdf69ad929361ce1

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/wrappers/report_bogota.py
  
  **alcance**: Completo, 1–82; ejecución de análisis 18–44 y exportación 47–82.
  
  **sha256**: c2cbd44e00c995a2a7c4c0e1d8e262b7534348af4dc1cc9f84a11cb6bdf590fd

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/functions/generic_unifier_class.py
  
  **alcance**: Completo, 1–152; árbol 31–64; contrato 76–108; esquema 119–123.
  
  **sha256**: 90c76daebdad83123b508ceb25fc759550ee1d293b3b1063d2ac68a6e0fd562e

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/extractors/universal_git_single_extractor.py
  
  **alcance**: Completo, 1–82; descripción 31, actualización/copia 44–79.
  
  **sha256**: 3dcde609f2ecb11bccae7c7da1433017e200eb785cea370b88594d85dbc3bbf2

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/POS/generate_website_files.py
  
  **alcance**: Consulta dirigida 1–160; save_pandas 17–28 y rutas de productos 42–159. Resto no leído.
  
  **sha256**: 89a5f6265e19efe064a34c51197a2e090304c46be4349adedb5e937c1f7f6d3f

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/requirements_excecution.txt
  
  **alcance**: Completo, 1–24; dependencias fijadas históricas.
  
  **sha256**: a2b02a5d590509482e19b8fb11ec032036a210d95058da1408a6f51ab48b0f1a

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/LICENSE
  
  **alcance**: Completo; MIT, copyright DataLama Team 2020–2021.
  
  **sha256**: 345a001f3a97e86a0a7cd1f1c52815c063b1e372fb565460d18c3b438ccfc201

- **archivo**: covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/pipeline_scripts/configuration/selected_excecutions.csv
  
  **alcance**: Completo, 12 líneas; columnas y YES/NO leídos; solo configuración de referencia.
  
  **sha256**: 022ef53ccdc5b3492f898a29b2a6fa1f7cd836609be3bc537864c97681bf8401

**se retoma**: - **archivo**: pipeline_scripts/excecute_all.py
  
  **localizador**: 16–21,75–100
  
  **patron**: Separar etapas y plan explícito de operaciones; configurar pregunta, fuente y versión en vez de ejecución implícita.

- **archivo**: pipeline_scripts/functions/generic_unifier_class.py
  
  **localizador**: 31–64,76–108,119–123
  
  **patron**: Separar originales, unificados y derivados; contratos por adaptador y reglas de atributos.

- **archivo**: pipeline_scripts/agglomerators/universal_radius_agglomerate.py; universal_geometry_agglomerate.py; universal_community_agglomerate.py
  
  **localizador**: radius:25,73; geometry:105–109; community:58–95,108–155
  
  **patron**: Intercambiar estrategia de agrupación y conservar miembros/configuración; comunidad del código es agrupación de red, no voz comunitaria.

- **archivo**: pipeline_scripts/wrappers/report_bogota.py; POS/generate_website_files.py
  
  **localizador**: wrapper:18–44,47–82; POS:17–28,42–59
  
  **patron**: Separar análisis de preparación de artefactos; no identificar pipeline con interfaz.

**se modifica**: - **archivo**: pipeline_scripts/excecute_all.py
  
  **localizador**: 12–13,16,84–100
  
  **cambio**: Diseñar grafo con ramas y retornos, bitácoras inmutables por ejecución futura; no reiniciar log ni exigir todas las etapas.

- **archivo**: pipeline_scripts/unifiers/universal_generic_unifier.py
  
  **localizador**: 82–84
  
  **cambio**: No reutilizar salida DEBUG como casos; construir adaptadores nuevos de evidencia/espacio/acuerdo con pruebas de contrato.

- **archivo**: pipeline_scripts/agglomerators/universal_geometry_agglomerate.py
  
  **localizador**: 105,126–130,144–146
  
  **cambio**: Sustituir joins que pueden omitir puntos por asignaciones conciliadas con bordes/exclusiones; población ausente no se llena ni se usa como tasa.

- **archivo**: pipeline_scripts/constructors/universal_daily_graphs_constructor.py; analysis/tda_script.R
  
  **localizador**: constructor:86,99–101; TDA:16–24,102,123–208
  
  **cambio**: Contratos de objetos derivados explícitos; verificar dependencias externas y construcción de matriz, no asumir TDA universal.

- **archivo**: requirements_excecution.txt
  
  **localizador**: 1–24
  
  **cambio**: Reevaluar herramientas y versiones en entorno futuro aislado; no instalar por inercia dependencias de 2020–2021.

**no se transfiere**: - Casos, población Facebook, movilidad, Rt, incidencia, alertas, ventanas temporales, parámetros de Mapper, rutinas de Bogotá o pronósticos como supuestos del proyecto.

- Esquema universal de polígonos ni creación obligatoria de árboles de datos; una nota puede ir de unificación a construcción/consulta.

- Configuración de cuentas, claves, rutas personales o automatización de descarga/publicación. No se leyó ni empaquetó archivo con valores de credenciales.

- Artículo asociado: README mantiene Citation pending; no se inventa referencia ni identidad con ZIP de clase.

**limites**: Referencia pública estática; procedencia y huella cotejadas, no auditoría completa ni funcionamiento acreditado. Datos fuera del repositorio y mapper externo no aportados; no se ejecutó GeoInsights, R o dependencias. Configuración de ejecución sin credenciales leída, valores secretos no copiados.

**representaciones**: - **tipo**: PUNTOS
  
  **estado**: CONSIDERADA
  
  **productos**: - T01-P001
  
  **adaptacion**: Adaptador opcional C003 con significado de sitio/acceso y CRS documentado; el mapa se abre solo si la duda sigue siendo espacial.
  
  **limites**: Un punto no acredita puerta o exactitud métrica.

- **tipo**: LINEAS
  
  **estado**: CONSIDERADA
  
  **productos**: - T01-P002
  
  **adaptacion**: Adaptador opcional para esquema de secuencia o trazado aportado, distinguiendo relación narrada de geometría de recorrido.
  
  **limites**: No inferir ruta GPS ni trayecto mínimo desde líneas dibujadas.

- **tipo**: POLIGONOS
  
  **estado**: CONSIDERADA
  
  **productos**: - T01-P001
  
  **adaptacion**: Adaptador de partición con emisor/edición/propósito, reglas de solapamiento y correspondencias; solo extensión de contraste territorial.
  
  **limites**: SSC no aportadas, identidad/CRS/atributos desconocidos.

- **tipo**: RASTER
  
  **estado**: NO_NECESARIA_EN_PRODUCTOS_ACTUALES
  
  **productos**: Lista vacía justificada por los límites/decisión del objeto.
  
  **adaptacion**: Considerar contrato C003 para futuras preguntas ambientales: archivo, bandas, unidad, máscara, CRS, resolución y periodo deberían documentarse.
  
  **limites**: NO_NECESARIA_EN_PRODUCTOS_ACTUALES: imágenes no resuelven identidad, alternativas narradas ni confirmaciones culturales.

- **tipo**: REDES
  
  **estado**: CONSIDERADA
  
  **productos**: - T01-P002
  
  **adaptacion**: Adaptador de nodos/aristas tipadas C006 con ocasión y procedencia. Red relacional de actividades distinta de red vial y de Mapper.
  
  **limites**: Sin vínculos institucionales entre casos ni grafo de movilidad digital.

- **tipo**: TEXTO_TABLAS
  
  **estado**: CONSIDERADA
  
  **productos**: - T01-P001
  
  - T01-P002
  
  - T01-P003
  
  **adaptacion**: Adaptador principal C001/C002/C006–C010: conservar modalidad, nulos y enlaces con esquema y vocabulario propios de la decisión.
  
  **limites**: OCR o normalización futura requieren cotejo; no promesa de leer cualquier formato.

- **tipo**: MUESTRAS_FISICAS
  
  **estado**: NO_NECESARIA_EN_PRODUCTOS_ACTUALES
  
  **productos**: Lista vacía justificada por los límites/decisión del objeto.
  
  **adaptacion**: Si se reconsidera H017, referencia C001 a objeto, custodia y contexto de ensayo, con material en mano; foto solo complementa.
  
  **limites**: NO_NECESARIA_EN_PRODUCTOS_ACTUALES: fuera del portafolio; no muestras digitalizadas, compradas ni recibidas. Se preserva práctica de E04.

- **tipo**: TRES_DIMENSIONES
  
  **estado**: NO_NECESARIA_EN_PRODUCTOS_ACTUALES
  
  **productos**: Lista vacía justificada por los límites/decisión del objeto.
  
  **adaptacion**: No adaptar ahora. Solo reconsiderar con decisión que necesite altura/volumen, referencias verticales/unidades y medición pertinente.
  
  **limites**: NO_NECESARIA_EN_PRODUCTOS_ACTUALES: escucha situada de E03/E05 no exige modelo acústico/3D; no se aportó levantamiento.

**google earth engine**: **decision**: DESCARTADO_EN_PRODUCTOS_ACTUALES

**finalidad**: Se evaluó capacidad para cómputo ambiental/raster y datos geoespaciales; ninguna decisión seleccionada requiere ese procesamiento. Un acuerdo o el sentido de una nota no se obtiene de imagen satelital.

**productos**: Lista vacía justificada por los límites/decisión del objeto.

**fuentes**: - T01-F016

**dependencias**: Si cambia la pregunta: datos adecuados, registro/proyecto, autorización, cuotas y condiciones de uso por comprobar; adaptador con contratos, referencias temporales, máscaras y resolución. Ninguna cuenta asumida.

**limites**: No integración, servicio, exportación o nube ejecutados; descarte por pertinencia actual, no afirmación de incapacidad general.