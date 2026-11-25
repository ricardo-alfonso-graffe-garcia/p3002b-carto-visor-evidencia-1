# Entrega preferida REP01 1.3

Esta versión hace explícitos esquema, mapa de actores, metodología JANUS y preparación de objetos hacia FDO. [Revisión actual](editorial/revision_v1_3/LEEME.md). [Volver al PDF](../P3002B_Evidencia1_Ricardo_Graffe.pdf). El cuerpo tiene diez páginas; la revisión humana y la implementación integral FAIR/FDO siguen pendientes. Los antecedentes 1.1 y 1.2 que se conservan debajo no sustituyen esta indicación de versión preferida. El manuscrito actual es REP01_reporte_v1_3.md y el control es REP01_control_editorial_v1_3.json.

# REP01 Procesos actores y necesidades de información territorial

Versión 1.2 revisada a partir de auditoría y maquetada, sin publicación ni licencia abierta del corpus.

Pregunta: ¿qué debe conservar una organización de información territorial para ayudar a decidir sin borrar diferencias de significado, responsabilidad y ocasión?

El manuscrito argumenta que hacer recuperables significado, respaldo y límites de una decisión antecede a elegir una plataforma. Compara cinco relatos: revisión pública, investigación, coordinación cultural, mercería y salida personal. Los deseos ideales coexisten con prácticas suficientes. El contraste documental tiene cuatro modelos parciales, sin fuentes directamente atribuibles a los episodios ni divergencias formalmente demostradas.

## Revisión actual

El [registro de revisión 1.2](editorial/revision_v1_2/LEEME.md) reúne fichas humanas, contratos, protocolo futuro y resolución de 175 recomendaciones. [Volver al PDF](../P3002B_Evidencia1_Ricardo_Graffe.pdf). Los controles y la matriz 1.1 conservados debajo son históricos; la verificación actual es `editorial/scripts/validar_reporte_v1_2.py`, con control externo 1.2 y maquetación `editorial/controles/maquetacion_v1_2.json`.

## Empezar a leer

El paquete de entrega contiene el Word y PDF `P3002B_Evidencia1_Ricardo_Graffe`, el texto `REP01_reporte_v1_3.md`, la trazabilidad y el control editorial 1.2. Estos archivos deben permanecer al mismo nivel que `REP01_repositorio/` después de extraer el ZIP. La trazabilidad y el control son externos al inventario de esta carpeta para evitar ciclos.

Para una entrada visual, abre [indice.html](indice.html). La [revisión de coordinación](editorial/registros/revision_coordinacion_v1_1.md) explica los cambios y los límites persistentes. La matriz CSV de cobertura está en `editorial/registros/cobertura_requisitos.csv`.

1. Leer el manuscrito y volver a la [guía por sección](editorial/registros/guia_por_seccion.md).
2. Para un literal, abrir `corpus/E0x/E0x_texto_con_localizadores.txt`; el párrafo conserva su numeración. La pregunta y las correcciones están en la misma entrevista. Para auditoría de voz y offsets usar `analisis/insumos/` y `analisis/recodificacion/`.
3. Para derivaciones, seguir necesidad → historia → metadatos/objeto en los documentos 82 y 88; el [índice inverso](editorial/registros/indice_inverso.json) permite ir del párrafo al reporte y a las necesidades/propuestas.
4. Para límites administrativos, metodológicos y de diseño, consultar [incidencias](editorial/registros/incidencias_metodologicas.md) y [agenda](editorial/registros/agenda_pendientes.md).

## Mapa de carpetas

| Ruta | Función |
|---|---|
| `corpus/` | Cinco transcripciones DOCX y vistas canónicas TXT/JSON sin modificar. |
| `analisis/insumos/` | Párrafos, voces, turnos y localizadores fuente. |
| `analisis/libro_comun/`, `analisis/recodificacion/` | Linaje del libro y aplicaciones preferidas, segmentos y memos. |
| `analisis/sintesis/`, `analisis/procesos/`, `analisis/documental/` | Síntesis, cinco procesos completos y cuatro modelos documentales parciales. |
| `analisis/actores/`, `analisis/necesidades/`, `analisis/historias/` | Mapa ampliado, necesidades, historias, metadatos y payloads de objetos locales. |
| `analisis/diseno/`, `analisis/referencias/` | Fundamentos, arquitectura, contratos, representaciones, candidatos y referencia GeoInsights. |
| `registro/` | Prompts/entradas de análisis y salidas iniciales con función de linaje. No prompts de desarrollo de entrevistas. |
| `editorial/` | Fuentes de encargo, figuras nuevas, controles y registro efectivo de esta integración. |
| Archivos 11, 24, 55, 63, 67, 72, 76, 82, 88, 93 | Lectura humana e instrumentos; las versiones preferidas se conservan explícitas. |

## Versiones y conservación

Corpus 1.0; libro 1.3; R01/R02 1.3, R03 1.2, R04/R05 1.1; S01/P01/D01/ACT01/N01/HU01/T01 revisadas 1.1. Los objetos internos pueden conservar sus propias versiones: no se cambian todos a la versión de su paquete. La base curada se copió: contiene 482 archivos; el catálogo describe 446 registros de procedencia. Los archivos permanecen idénticos salvo este LEEME de entrada, sustituido por la guía final. El catálogo original conserva la procedencia de sus siete adaptaciones históricas de rutas humanas. No se reescriben objetos ni sus payloads.

`manifest.json` inventaría todos los archivos de esta raíz salvo sí mismo. No incluye huellas del manuscrito, trazabilidad o control externos. Para cotejar: leer bytes y SHA-256 de cada ruta; ejecutar `editorial/scripts/validar_reporte_v1_1.py` con el directorio original de insumos, manuscrito y trazabilidad externos y `--repositorio` apuntando aquí. El script editorial adicional comprueba navegación local, citas/offsets, objetos y archivos. Los scripts históricos requieren sus entradas y rutas originales: no se promete regeneración idéntica de revisiones.

## Acceso y límites

El corpus se distribuye para revisión del ejercicio; no se otorga permiso abierto de reutilización. MIT corresponde al código GeoInsights, no a entrevistas o registros personales. Las aperturas conservan los acuerdos de participación; fechas de entrevista NO_CONSIGNADA. Las transcripciones se preservan y su alcance se declara en el manuscrito. La revisión humana independiente permanece pendiente. La paginación efectiva y los controles de Word/PDF se documentan en `editorial/controles/maquetacion_v1_1.json`.

## Entrega y verificación

Los scripts originales 1.0 se conservan como antecedente y no sustituyen los controles 1.1. La comprobación actual usa el validador 1.1 con las mismas entradas originales y la carpeta final real. Word/PDF se cotejan en el control de maquetación. Los archivos DOCX pueden repaginarse en otro editor; el conteo certificado corresponde al PDF suministrado y al render de ese DOCX.
