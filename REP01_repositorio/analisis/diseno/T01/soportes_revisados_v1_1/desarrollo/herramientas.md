# Herramientas · Diseño para revisión

## SaTScan (T01-B001)

**id**: T01-B001

**nombre**: SaTScan

**lente**: SCAN

**lenguaje**: Núcleo C/C++; interfaz Java; ejecutable autónomo con modo batch.

**version documentacion**: Sitio/README rama b_10_3_3; guía efectivamente leída 10.1 (julio 2022).

**funcion**: Escaneo espacial/temporal con modelos explícitos y contraste de ventanas.

**requisitos**: Archivos de casos/coordenadas y controles o población según modelo. README de compilación menciona Boost 1.81.0 y JDK17; preferir evaluar binario correspondiente al sistema y licencia antes de decidir, sin compilar ahora.

**compatibilidad**: COMPATIBILIDAD_NO_PROBADA

**fuentes**: - T01-F004

- T01-F005

**limites**: Ningún paquete instalado ni ejecución. No integra automáticamente el snapshot ni elimina MAUP.

## powerlaw (T01-B002)

**id**: T01-B002

**nombre**: powerlaw

**lente**: POTENCIA_ESCALAMIENTO

**lenguaje**: Python

**version documentacion**: null — motivo explicado en el campo/contrato correspondiente.

**funcion**: Ajustar y comparar distribuciones de cola pesada; no resuelve por sí sola regresión de Y sobre N.

**requisitos**: Según README master: NumPy, SciPy, matplotlib, mpmath, dill, h5py, tqdm; fijar release y verificar sus requisitos y dominio discreto/continuo después.

**compatibilidad**: COMPATIBILIDAD_NO_PROBADA

**fuentes**: - T01-F008

- T01-F006

**limites**: Candidata para rama distributiva, no prueba de bondad automática ni recomendación de desplegar con una muestra insuficiente. Web de documentación alternativa falló.

## KeplerMapper (kmapper) (T01-B003)

**id**: T01-B003

**nombre**: KeplerMapper (kmapper)

**lente**: TDA

**lenguaje**: Python

**version documentacion**: 2.1.0

**funcion**: Construir/visualizar Mapper mediante filtros, cobertura y agrupamiento compatibles con scikit-learn.

**requisitos**: Documentación Setup menciona NumPy/scikit-learn y requisitos Python antiguos; verificar manifiesto de release antes de instalar. Visualización declara recursos web externos: revisar exportación autónoma y permisos para datos restringidos.

**compatibilidad**: COMPATIBILIDAD_NO_PROBADA

**fuentes**: - T01-F009

**limites**: No homología persistente universal ni equivalencia con mapperKD R del snapshot. No se promete ejecución offline del HTML sin prueba.

## Mesa (T01-B004)

**id**: T01-B004

**nombre**: Mesa

**lente**: ABM

**lenguaje**: Python

**version documentacion**: Overview stable sin versión completa legible; pyproject main consultado (Alpha).

**funcion**: Definir agentes/modelos, activación, espacio y recolectar resultados y corridas por parámetros.

**requisitos**: Main declara Python >=3.12; no se atribuye ese requisito a todos los releases. Seleccionar versión estable y revisar su manifiesto, dependencias de análisis e interfaz; definir fuentes de reglas/calibración antes.

**compatibilidad**: COMPATIBILIDAD_NO_PROBADA

**fuentes**: - T01-F010

- T01-F011

- T01-F012

**limites**: Sin instalación o simulación; herramienta no valida reglas ni pertinencia de modelar personas como agentes.

