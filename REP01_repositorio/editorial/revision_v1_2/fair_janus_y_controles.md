# FAIR JANUS y controles reales

Esta nota retrospectiva reúne controles existentes y comprobaciones nuevas de la revisión 1.2. No acredita controles anteriores a la generación o codificación ni revisión por personas que no participaron.

## Procedimiento ordinario y adaptación del ejercicio

| Requisito ordinario | Material disponible y alcance adaptado |

|---|---|

| Cinco entrevistas y dos tipos de actor | Cinco diálogos canónicos generados con IA; funciones distintas y dos perfiles no especializados, sin ADIP entrevistado |

| Fecha y perfil | Perfiles funcionales conservados; fecha de entrevista no consignada, sin completarla con fecha de edición |

| Guion validado | Instrumentos y preguntas localizables; no se atribuye validación de guion no documentada |

| Audio y consentimiento de personas | No audios ni firmas aportados; acuerdos dentro de los diálogos no se convierten en consentimientos reales |

| Citas verificadas | Cotejo literal contra texto canónico, conservando párrafo y contexto; no cotejo acústico |

| Uso de IA | Generación, codificación, síntesis y escritura declaradas; parámetros desconocidos siguen desconocidos |

| Validación humana | Pendiente; los controles estructurales y revisión asistida no la reemplazan |

La excepción docente es comunicada por el usuario; no se inventa un documento de autorización independiente ni se transforma el ejercicio en evidencia empírica de campo.

## Evidencia FAIR por principio

| Principio | Evidencia local | Estado y pendiente |

|---|---|---|

| F1 | Ids locales estables y separados por clase en registro. | PARCIAL: Persistencia, unicidad global y resolución externa con gobernanza. |

| F2 | Cada registro describe entidad, versión, procedencia, acceso y relaciones; perfiles de información con 21 campos. | PARCIAL: Revisar adecuación con usuarios y responsables; completar desconocidos cuando se aporten. |

| F3 | Cada registro explicita entidad y ruta del payload; cotejo real con contenido individual. | ATENDIDO_LOCALMENTE: Conservar vinculación y evaluar interoperabilidad si se despliega externamente. |

| F4 | Registro consultable dentro del ZIP. | PENDIENTE: Registro o indexación en recurso de búsqueda con acceso y gobernanza adecuados. |

| A1 | Id se resuelve localmente a una ruta incluida y cotejada. | PARCIAL: Servicio y protocolo estandarizado de recuperación por identificador si se autoriza despliegue. |

| A1.1 | JSON, CSV y SVG son legibles localmente; no se desplegó acceso remoto. | PENDIENTE: Definir y comprobar protocolo abierto, gratuito e implementable. |

| A1.2 | Se documenta acceso y ausencia de autorización de publicación. | PENDIENTE: Establecer autenticación/autorización y reglas de acceso si se crea servicio. |

| A2 | Metadatos y payloads están separados en paquete. | PENDIENTE: Política de preservación y continuidad de metadatos aun si falta dato. |

| I1 | JSON estructurado, ids tipados y estados enumerados bajo contrato local. | PARCIAL: Evaluar representación semántica formal compartida y correspondencias. |

| I2 | Vocabulario y clases locales documentados sin registro. | PENDIENTE: Evaluar vocabularios FAIR pertinentes, términos y mapeo con comunidad. |

| I3 | Relaciones tipadas a entidades y evidencias existentes verificadas. | PARCIAL: Referencias interoperables persistentes si se autoriza exteriorización. |

| R1 | Contexto, restricciones, incertidumbres y procedencia en historias y perfiles. | PARCIAL: Revisión sustantiva y documentación de usos apropiados. |

| R1.1 | Licencia valor null y fundamento por objeto; NO_CONSTA publicación. | PENDIENTE: Resolver derechos y licencia aplicable a cada recurso antes de reutilización ampliada. |

| R1.2 | Trazas a necesidades y evidencias, versiones, catálogo de entrada y huellas. | PARCIAL: Revisión humana, autorías de artefactos y responsables futuros si se conocen. |

| R1.3 | Contrato metodológico HU01 comprobado localmente. | PENDIENTE: Contrastar estándares pertinentes con comunidad y finalidad, sin atribuir manual a los casos. |

## Una misma entidad en ficha y objeto

La ficha de Retomar el sentido del último cambio (HU01-H003) en [historias](fichas_historias.md) reproduce formulación, modalidad y criterios del [objeto JSON](../../analisis/historias/HU01/soportes_revisados_v1_1/objetos/historias/HU01-H003.json). El registro conserva versión propia de historia 1.0, perfil de metadatos 1.1 y necesidad 1.1, sin forzar una versión única a entidades distintas. Los 76 objetos locales se conservan en HU01 y el control de esta revisión comprueba payloads y relaciones existentes. Un ID local no es PID externo y un archivo JSON no certifica FAIR.

## JANUS aplicado y pendiente

Se aplican separación entre afirmación y respaldo, rastreo de procedencia, revisión asistida, límites y registros de cambios. No se acredita revisión adversarial por dos personas, concordancia, saturación o exportaciones completas de prompts. Los prompts y respuestas conservados permanecen con su procedencia real; la ausencia de parámetros no se corrige inventándolos. PROV-O, RO-Crate, DataCite y nanopublicaciones siguen evaluaciones de empaquetado futuro, no implementación actual.

## Acceso y reutilización por familia

| Familia | Consulta académica actual | Difusión y cambios |

|---|---|---|

| Corpus y análisis asociados | Copia entregada para este ejercicio, sin abrir una licencia nueva | Antes de difusión verificar permisos y riesgos de inferencia; no crear autorizaciones ni contactos ficticios |

| Fuentes documentales públicas | Referencias y copias aportadas según alcance registrado | Condiciones de cada fuente; su publicidad no autoriza cualquier contenido derivado |

| Código GeoInsights | Licencia MIT del snapshot, atribución preservada | No extender MIT al corpus, datos de terceros o imágenes |

| Datos de producto no aportados | No existe acceso de contenido acreditado | Obtención y permiso previos a procesamiento o publicación |

| Figuras y reporte editorial | Material del ejercicio para evaluación | Derechos y atribuciones por aclarar antes de reutilización pública; no heredan licencias de insumos ajenos |

La política operativa de solicitud o retirada requiere un custodio y canal reales por designar. Se propone registrar solicitud, alcance, autorización o rechazo y versiones afectadas. No se publica dirección de contacto inventada. CARE se reconsiderará si se incorpora conocimiento indígena o comunitario con gobernanza pertinente; el solo rol cultural no acredita esa condición.

## Controles de alcance y referencias

Las huellas comprueban integridad. Los recuentos de 545 párrafos, 713 fragmentos y 971 asignaciones son controles de cobertura, no acuerdo ni calidad. La revisión 1.1 conserva controles, incidencias, instrucciones y resultados en [editorial controles](../controles/LEEME.md). Los nuevos resultados se guardan junto con el validador 1.2 después de ejecutarlo. La revisión semántica de todo el análisis por una persona sigue pendiente.

El informe bibliográfico previo [bibliografía consultada](../registros/bibliografia_consultada.json) conserva alcance de lectura y fuentes. La fuente Capybara nueva fue abierta en esta revisión; el blog no se usa para validar fenómenos ni capas de CDMX. Los demás originales no se declaran releídos por completo: se conserva su registro documental y se verifican atribuciones utilizadas.
