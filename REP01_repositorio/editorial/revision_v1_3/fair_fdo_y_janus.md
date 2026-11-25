# FAIR FDO y JANUS en la versión 1.3

## Qué se incorpora al cuerpo

La sección 2 explica una adaptación de JANUS y añade el esquema de relaciones entre evidencia y diseño. La sección 5 muestra el registro local HU01-OD037 para la historia HU01-H003. La sección 9 presenta aplicación y pendientes por cada dimensión FAIR. Se hace explícito un trabajo existente, sin recodificar o registrar objetos externamente.

## Principios y objeto concreto

| Dimensión | Evidencia local existente | Qué falta |
|---|---|---|
| Localización | Identificadores, catálogo de 76 objetos y rutas | Identificadores globales persistentes y resolución externa |
| Accesibilidad | Archivos recuperables en la entrega y condición académica declarada | Gobernanza de acceso, permisos y preservación de metadatos |
| Interoperabilidad | Campos y relaciones tipados localmente, con cotejo de referencias | Vocabularios y tipos compartidos y registrados |
| Reutilización | Versiones, procedencia y huellas, con límites | Derechos y licencias efectivos por artefacto y estándares comunitarios pertinentes |

La [matriz detallada de los quince principios](../revision_v1_2/fair_janus_y_controles.md) se conserva. FAIR orienta el tratamiento de recursos; no es una única serialización ni se obtiene por tener un JSON. Fuente: GO FAIR Foundation, The FAIR Guiding Principles, secciones F, A, I y R, consultadas el 25 de noviembre de 2026: https://www.gofair.foundation/fair-principles.

## Ejemplo legible de prototipo local orientado a FDO

| Atributo del registro conservado | Valor |
|---|---|
| Registro | HU01-OD037 |
| Entidad representada | HU01-H003, Retomar el sentido del último cambio de un lugar |
| Versión de entidad | 1.0 |
| Estado | PROTOTIPO_LOCAL_NO_REGISTRADO |
| Payload | objetos/historias/HU01-H003.json, dentro del subpaquete HU01 |
| Necesidad | N01-N004, registro HU01-OD004, versión de necesidad 1.1 |
| Perfil funcional | HU01-P001 |
| Perfil de metadatos | HU01-M003, versión propia 1.1 |
| Procedencia | Necesidad y evidencias N01-V0028 a V0043, según registro original |
| Huella | SHA-256 del payload, cotejable con el registro |
| Acceso y derechos | Consulta académica; publicación y licencia no acreditadas |
| PID, tipo y perfil externos | Nulos, no registrados |

El [JSON de esta vista editorial](ejemplo_objeto_local_orientado_a_fdo.json) conserva el registro original y la necesidad vinculada. La [historia fuente](../../analisis/historias/HU01/soportes_revisados_v1_1/objetos/historias/HU01-H003.json) mantiene formulación, contexto, criterio K004 y operaciones OP009–OP013. Su vínculo con el proceso E01 es contextual: el ideal propone retomar revisiones futuras; no demuestra que el producto se usara en aquel episodio.

Un FDO vincula una representación digital con identidad persistente, perfil, tipo y referencias interpretables por máquinas. Los registros locales permiten preparar esa transición, sin sustituir el registro externo. La denominación FDO del cuerpo significa FAIR Digital Object; no se traslada la acepción Forecasting and Decision Objects usada en algunos ejemplos del blog. Fuente primaria de delimitación: FDO Forum, What is an FDO?, apartados An FDO is y What are Core FDOs, consultados el 25 de noviembre de 2026: https://fairdo.org/about/what_is_an_fdo/.

## JANUS y alcance real

El texto metodológico del marco organiza preparación, codificación, síntesis, revisión, escritura y empaquetado con trazabilidad. La sección 2 resume esa lógica y distingue los componentes conservados de las condiciones pendientes. No se acredita revisión humana independiente, concordancia, controles históricos ausentes o empaquetado completo. Fuente primaria: Feged Rivadeneira (2025), The JANUS Framework, Methods, secciones 1 a 9, páginas PDF 9 a 11: https://doi.org/10.21203/rs.3.rs-7580516/v1.

Las entrevistas y su análisis se organizan mediante la adaptación de JANUS descrita en el reporte. Su aplicación se limita a organización, trazabilidad y revisión; no acredita conformidad integral.
