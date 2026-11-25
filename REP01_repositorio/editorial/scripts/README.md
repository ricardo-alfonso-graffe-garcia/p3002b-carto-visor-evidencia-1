# Scripts de esta etapa
`validar_reporte.py` es copia idéntica del control suministrado. Requiere la raíz de insumos original, manuscrito y trazabilidad externos y la carpeta final. `controles_complementarios.py` comprueba la navegación editorial, literalidad de segmentos/ejemplos y resolución de payloads de historias. No implementan Carto-Visor ni ejecutan lentes territoriales. Los scripts de etapas previas conservan carácter histórico y dependencias originales.

Los tres archivos `*_historico.py` conservan el código efectivo de preparación, figuras y trazabilidad usado en esta integración. Sus rutas dependen del layout de trabajo (insumos en trabajo/ y entrega/ al lado de los scripts); no se ejecutan desde esta ubicación sin adaptar esa raíz. No contienen una exportación de chats ni regeneran por sí solos la redacción del manuscrito, que fue escrita con asistencia y se entrega completa fuera del ZIP. Para los controles, use los dos scripts sin sufijo histórico con argumentos explícitos.

## Revisión 1.1

El control activo es validar_reporte_v1_1.py y recibe base original, Markdown 1.1, trazabilidad 1.1 y --repositorio. Comprueba también el PDF hermano y la huella del control de maquetación. Los scripts cuyo nombre termina en historico.py documentan una ejecución con rutas locales; no prometen reconstrucción portátil del documento.
