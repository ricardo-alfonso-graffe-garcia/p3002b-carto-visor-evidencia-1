# Protocolo exploratorio futuro de vegetación y equipamientos culturales

## Pregunta propósito y naturaleza

¿Dónde coinciden menor fracción de cobertura vegetal y mayor separación respecto de equipamientos culturales, y qué zonas conservarían prioridad de verificación al cambiar la unidad espacial? La decisión propuesta es seleccionar lugares para comprobar condiciones y acceso con las funciones públicas y comunitarias pertinentes. No se atribuye esta pregunta a las entrevistas ni se identifica con alguno de los tres productos heredados. Es la extensión editorial EX01, propuesta y no ejecutada.

Una coincidencia descriptiva no demuestra desigualdad causada por vegetación, ausencia de oferta cultural, disposición a asistir ni acceso efectivo. La posible utilidad pública depende de que una función con capacidad de actuar acuerde pregunta, recursos y criterio de verificación. La cobertura vegetal no equivale a sombra, arbolado accesible o confort.

## Recursos candidatos y condiciones

| Recurso por obtener | Información necesaria | Condición que bloquea |
|---|---|---|
| Ráster de cobertura vegetal o clasificación validada | Productor, versión, bandas, unidad, método, periodo, CRS, tamaño de celda, máscara y precisión de clasificación | Sin significado o validación, no publicar «área vegetal»; NDVI solo no demuestra fracción de área |
| Directorio de equipamientos culturales | Tipo de servicio, identificador, geometría de sitio, fuente, fecha y alcance de cobertura | Sin actualización y cobertura, no interpretar falta de registro como falta de servicio |
| Particiones y límites | Fuente, edición, vigencia, significado y licencia | Sin equivalencia jurídica, no asignar competencia por una coincidencia espacial |
| Red o información de accesibilidad, sólo para extender | Caminabilidad, entradas, restricciones y fecha | Sin red comprobada, la distancia recta no se etiqueta tiempo de viaje ni acceso |
| Población, sólo para una extensión distributiva | Universo, periodo, geografía, resolución y compatibilidad | No dividir por población de otro universo ni imponer una tasa a la fracción de área |

No se da por adquirido, vigente ni autorizado ninguno de estos recursos. La selección del producto concreto, fechas y licencia pertenece a la siguiente etapa. Earth Engine es una alternativa de procesamiento, no una fuente universal ni una integración operativa actual. Su ficha deberá fijar identificador de colección o asset, filtros temporales/espaciales, bandas, máscara, CRS, escala, reductor, región, salida y límites de cuota/permisos; no se inventan esos valores antes de seleccionar datos.

## Unidad variables y denominadores

La observación base será una celda o fragmento válido del ráster y cada equipamiento deduplicado. Para una unidad U, la fracción vegetal propuesta es suma de área vegetal válida dentro de U dividida entre área válida observada dentro de U. Se conserva además área válida/área total de U para mostrar cobertura. NoData queda fuera del denominador válido y nunca se convierte en cero vegetación. Sólo procede esta operación si el insumo representa una fracción o una clase defendible; otro índice exige otra interpretación.

La separación se estimaría inicialmente por distancia recta desde centros de celdas válidas a equipamientos pertinentes, expresada en metros tras una proyección justificada, y se resumiría con ponderación por área válida. No se empleará el centroide de una jurisdicción como ubicación de toda su población. La distancia aproxima separación geométrica; el acceso exige otra prueba. Las fechas de funcionamiento de equipamientos y de observación vegetal deben ser compatibles con la pregunta; se registran estación, desfase y fuentes. No se utiliza la fecha de descarga como fecha de observación.

## Pasos y contrato

1. Acordar pregunta, función destinataria y criterio de prioridad de verificación, antes de observar rankings; no se fijan umbrales políticos en este documento.
2. Recibir originales autorizados y metadatos; comprobar tipo, duplicados, geometrías, ejes, unidades, fechas y cobertura. Conservar insumos y descartes.
3. Preparar derivados con CRS, máscara y resolución documentados. El remuestreo de categorías conserva significado; el de cantidades requiere regla de conservación apropiada. No mejorar resolución nominal para simular detalle.
4. Calcular variables con unidades y denominadores; mantener registros de asignados, ambiguos y excluidos y motivos. La contabilidad debe reconciliar recibidos únicos con estados terminales.
5. Resumir primero por jurisdicciones pertinentes y luego por rejillas propuestas de 500 m y 1 km, sólo si el insumo soporta ese detalle y extensión. Desplazar el origen medio ancho de celda para evaluar zonificación a escala semejante; cambiar ancho evalúa escala. Conservar periodo, datos y reglas.
6. Presentar fracción vegetal, distancia, cobertura y faltantes por separado. Evitar un índice compuesto sin ponderación justificada. Contrastar las zonas seleccionadas bajo el criterio previamente acordado, y mostrar cuáles cambian de selección o posición por configuración.
7. Revisar interpretación con especialistas de dato y funciones territoriales; una verificación en sitio sería futura, con permiso y registro propio. Decidir continuar, pedir información o detener, dejando constancia.

## Sensibilidad y prueba controlada

Se compararán cambios de unidad, origen, periodo admisible, fuente equivalente y regla de exclusión. Se registrará la intersección y diferencia entre conjuntos de zonas seleccionadas y el sentido de cambio de las variables; no se escogerá la configuración que confirme una expectativa. Si la prioridad depende de unidades o coberturas inestables, el resultado se comunicará como exploratorio y no sustentará por sí solo una intervención.

Antes de datos territoriales se diseñará una prueba con superficies y puntos controlados de verdad conocida, incluyendo celda parcialmente enmascarada, punto sobre borde, duplicado y unidad sin observación. Se comprobarán área válida, ponderación, pertenencia, conservación del total y nulos contra resultados esperados definidos antes de ejecutar. Son datos de prueba futuros, no observaciones creadas del territorio ni nuevas entrevistas. No se ejecutó esta prueba.

## Comparación de capas y límites

Si dos capas pretenden representar la misma entidad, primero se acreditan significado, periodo, autoridad y correspondencias; después se aplica a ambas una misma operación y universo para comparar resultado, entidades sin pareja y ambigüedades. Igualdad de conteos o de un resumen no demuestra identidad jurídica ni intercambiabilidad para otro uso. Una discrepancia puede provenir de edición, cobertura o definición; su explicación requiere evidencia, no corrección automática.

Extender fuera de CDMX sólo tiene sentido si el fenómeno y cobertura cruzan la frontera y existe documentación comparable y coordinación competente. No se recorta una actividad metropolitana por conveniencia del mapa ni se atribuyen competencias extraterritoriales.

## Salidas incertidumbre y abstención

Cada corrida futura entregará tabla de variables y calidad, mapa con leyenda, ficha metodológica y registro de exclusiones, todos enlazados al manifiesto de versiones y parámetros. La vista simple dirá «Zonas para verificación exploratoria; separación geométrica y vegetación registrada». El detalle mostrará fuentes, fechas, denominadores, áreas sin datos, sensibilidad y límites de uso.

Sin permiso se detiene el uso; sin CRS se detiene la medición espacial; sin compatibilidad temporal se detiene la comparación afectada; sin denominador válido se omite la fracción; sin validación de clasificación no se publica área vegetal; sin cobertura del directorio no se afirma ausencia de servicio. Las salidas afectadas se marcan retiradas o no interpretables, conservando bitácora. No se fabrican intervalos de confianza. La incertidumbre de clasificación, posición y cobertura acompaña cada transformación; no se reduce a un porcentaje sin modelo.

## Ocho preguntas de control

Qué se agrega: área válida y separación, no personas. Unidad: jurisdicción y rejilla con edición/origen. Denominador: área observada válida, separado de cobertura total. Autoridad: custodio de cada fuente y competencia por verificar. Límites: administrativos para responsabilidad, rejillas para sensibilidad. Parámetros: CRS, escala, máscara, fechas, distancia y criterio de selección versionados. Exclusiones: motivos y contabilidad explícitos. Decisión: verificar antes de intervenir, o abstenerse si falta sustento.
