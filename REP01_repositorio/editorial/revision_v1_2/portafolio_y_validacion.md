# Portafolio jerarquizado y pruebas futuras

El usuario decidió conservar los tres candidatos. Esta prioridad de desarrollo editorial no sustituye la prioridad local de N01 ni modifica T01. Primero expediente territorial; después memoria cultural; tercero cuaderno de contraste. Se ponderan proximidad al encargo, decisión destinataria y dependencias, sin fingir costo, aceptación o factibilidad comprobados.

## Expediente de revisión: qué cambió en el lugar y con qué respaldo

**ID:** T01-P001. **Estado heredado:** PROPUESTA_NO_IMPLEMENTADA.

**Función y decisión:** Recuperar una revisión concreta por identificador/nombre, comparar descripción y fundamento y mostrar la duda que condiciona su reutilización. El mapa es auxiliar si persiste una pregunta espacial; el resultado central es una explicación acotada. Conservar identificador/punto, modificar solo lo sustentado o detener una modificación; al retomar, decidir si el respaldo responde a la tarea o hace falta nueva aclaración.

**Valor público condicional:** Explicabilidad y responsabilidad de revisiones usadas en decisiones públicas; relación directa con el encargo territorial.

**Historias:** HU01-H001, HU01-H002, HU01-H003. **Necesidades:** N01-N001, N01-N002, N01-N003, N01-N004.

**Alcance:** Una relación/revisión autorizada de lugares y sus fuentes pertinentes; iniciar con el último cambio que afecte identificación y no con catálogo urbano.; Búsqueda por identificador/nombre, comparación antes/después y estado de duda con referencia espacial opcional.; Extensión separable de auditoría de asignaciones a dos unidades, únicamente si aparecen registros operativos y particiones justificadas. No es condición del expediente básico.

**Exclusiones:** Organizar visitas, verificar puertas en campo, garantizar ingreso o certificar precisión de un acceso.; Actualizar automáticamente todas las bases, registrar toda conversación o todos los desconocimientos.; Declarar una geometría SSC correcta, inferir error por límites distintos o hacer ranking territorial desde entrevistas.

**Recursos por obtener:** T01-D001: Petición, tabla/copia revisada y finalidad de revisión; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato. T01-D002: Nota de último cambio, fundamento, croquis/aclaración y duda pertinente; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato. T01-D003: Referencias espaciales y particiones operativas si se activa auditoría; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato. T01-D004: Marco Geoestadístico como referencia contextual opcional; estado CANDIDATO_DOCUMENTADO. Solo referencia documental consultada; autorización y obtención del contenido por comprobar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.

**Operaciones:** Recepción autorizada y huella; delimitar encargo antes de unir datos. Unión semántica por identidad justificada, no por calle/nombre parecido. Versionar diferencias de significado: sitio, acceso, descripción, traslado. No convertir CRS por defecto. Si se aporta geometría necesaria, validar referencia/ejes/unidad y transformar a CRS adecuado a operación documentada; conservar origen. No se ejecuta ahora. Construir C007 y lectura C009; seleccionar respaldo pertinente y mantener conversación nueva como actividad humana. Si se activa resumen: fijar C004 y comparar particiones sobre mismos registros/periodo, conciliar asignaciones y exclusiones C005; tasas solo con marco de revisiones compatible. No promediar tasas sin pesos ni transferir población por área sin justificar.

**Funciones propuestas y pendientes de aceptación:** Custodia de fuente, revisión técnica, coordinación y autoridad de cambio por acreditar.

**Responsabilidades todavía desconocidas:** Responsable técnico y custodio de registro por confirmar con institución/alcance exactos. Aportante de croquis/aclaración y mantenimiento de nota; aceptación de compañera no recabada. Responsable de permisos/retención y, si hay auditoría, emisor de particiones y revisor de asignaciones.

**Cargas y beneficios:** Podría reducir reconstrucciones de sentido al retomar una revisión; beneficio no medido. Quien revisa asumiría escribir una explicación pertinente, quien conserva respaldos gestionaría acceso/versiones y quien observa aclararía solo preguntas dentro de su experiencia. Evitar que el coste de llenar historial supere notas que ya funcionan.

**Pruebas de contenido heredadas:** T01-K001: Dado Una revisión autorizada con sitio/punto y nueva descripción de acceso, cuando Se comparan respaldo y diferencia de calle, entonces La explicación permite conservar sitio/punto sin inferir traslado, puerta única o cancelación de acceso. Ensayo futuro de tarea con respaldos reales; cotejo con responsable técnico y evidencia de alcance T01-K002: Dado Una consulta se refiere a una copia/version concreta, cuando Otra persona retoma el último cambio pertinente, entonces Puede explicar qué cambió, por qué y qué duda importa, o detectar necesidad de nueva aclaración. Comparación futura entre consulta con notas actuales y expediente propuesto, conservando interpretación y esfuerzo; sin umbral de ahorro predefinido T01-K003: Dado Se activa extensión espacial con datos autorizados y dos particiones, cuando Se comparan asignaciones y resumen en ambas, entonces Se concilian registros únicos, ambigüedades y exclusiones; denominador desconocido impide tasa y salida igual no certifica equivalencia. Prueba futura de conservación de entidades y revisión de muestra de bordes/solapes; contrastar informe de parámetros con fuentes T01-K004: Dado Falta CRS, respaldo de identidad o permiso necesario, cuando Se intenta transformación afectada, entonces Operación se detiene con pregunta localizada y el original permanece; lectura textual autorizada puede continuar. Pruebas futuras de contrato y control de versiones/acceso, sin datos personales de ejemplo en T01

**Condición de descarte:** Descartar software nuevo si las notas actuales ya permiten retomar con esfuerzo aceptable; reformular como pauta documental si no hay responsable o permiso de mantenimiento. Retirar extensión espacial si no cambia una decisión o si carece de unidades/fuentes compatibles.

## Cuaderno de contraste de ocasiones: decidir qué se puede comparar y afirmar

**ID:** T01-P002. **Estado heredado:** PROPUESTA_NO_IMPLEMENTADA.

**Función y decisión:** Colocar dos ocasiones del mismo caso junto a sus palabras, secuencias y procedencias para decidir unidad de comparación y alcance de una afirmación; puede adoptar documentos existentes, sin programa nuevo obligatorio. Comparar salidas completas o decisiones puntuales, reducir una explicación de elección a descripción respaldada y decidir si pedir otra ocasión aporta o conviene detener seguimiento.

**Valor público condicional:** Calidad del conocimiento territorial y límites de afirmaciones. Su uso público requiere todavía una decisión y destinatario público concretos; no se presupone por ser académico.

**Historias:** HU01-H004, HU01-H005, HU01-H006. **Necesidades:** N01-N006, N01-N007, N01-N008, N01-N009.

**Alcance:** Contraste interno de un caso y una segunda ocasión que la persona considere distinta, si existe interés/disponibilidad y se acuerda periodo pertinente.; Enlazar afirmación, nota de observación, relato posterior y desconocimiento; permitir esquema y referencias espaciales solo cuando ayuden.; Exploración TDA únicamente como extensión independiente si una matriz multivariable comparable y volumen justifican su coste después de validar cuaderno básico.

**Exclusiones:** Recopilar cada movimiento o un periodo entero por defecto, publicar ubicaciones identificadoras o GPS.; Ordenar personas por rapidez, hallar causa única, reconstruir todas las opciones por catálogo o representar dos zonas/ciudad.; Imponer aprobación académica total a participantes o sustituir conversación con un modelo.

**Recursos por obtener:** T01-D005: Notas y relatos autorizados de primera ocasión y versiones de afirmación; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato. T01-D006: Segunda ocasión contrastante y contexto que se acepte compartir; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato. T01-D007: Secuencias/esquemas de actividades, opciones recordadas y referencias espaciales opcionales; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.

**Operaciones:** Recibir soportes con permiso y mantener seudonimización y detalle mínimo. Las entrevistas de entrada justifican diseño pero no son los originales de seguimiento que se requieren. Unificar vocabulario de actividad/ocasión y marcar modalidad de cada fragmento. No reducir habitual contado a hecho observado. Construir C006: relaciones de secuencia/solapamiento y opciones desconocidas; no inferir ruta mínima ni rellenar tiempos. Alinear ocasiones por finalidad/unidad conceptual antes de comparar, conservar diferencias de contexto temporal. Convertir unidades solo cuando significado y valor estén documentados; no exigir CRS a esquema conceptual. Preparar comparación C009 de qué se puede sostener con una ocasión y con ambas, admitiendo reducción. Sin agregación areal, denominador de habitantes o estadística de población.

**Funciones propuestas y pendientes de aceptación:** Responsable de investigación, aportante voluntario y custodia de notas por acordar.

**Responsabilidades todavía desconocidas:** Responsable académica y custodia del ejercicio concreto no identificados institucionalmente. Personas que aportarían segunda ocasión: interés/disponibilidad y esfuerzo por recabar, sin asumir rechazo. Quien mantenga cuaderno y controle acceso a notas/versiones; aceptación de herramienta pendiente.

**Cargas y beneficios:** Puede ayudar a modificar una afirmación con evidencia y evitar comparación impropia; no ahorro medido. Participante asumiría reconstrucción voluntaria, analistas revisarían notas/relaciones y custodio protegería detalles. Un cuaderno ya existente puede ser suficiente y reduce coste de migración.

**Pruebas de contenido heredadas:** T01-K005: Dado Dos reconstrucciones con distinto origen/propósito o actividades, cuando Se intenta comparar tiempos o decisiones, entonces Se explica por qué no son equivalentes y qué comparación acotada sí procede, manteniendo papel situado de tiempo/cercanía. Revisión futura de tarea con textos reales, cotejando unidad y fuentes; comparar contra interpretación de equipo T01-K006: Dado Se dispone voluntariamente de segunda ocasión contrastante, cuando Se compara qué puede decirse con una y con dos, entonces Se precisa o reduce afirmación o se justifica que seguimiento no aporta; no se exige periodo entero. Ensayo futuro de contraste con acuerdos y material autorizado, registrar decisión y esfuerzo sin umbral de éxito inventado T01-K007: Dado Una afirmación pretende explicar elección entre opciones no reconstruidas, cuando Se revisa el vínculo con respaldo, entonces Opciones desconocidas siguen visibles y analista acota explicación, sin imputarlas desde catálogo o casos ajenos. Auditoría futura de afirmación→fragmento→modalidad, con revisión humana de explicaciones alternativas T01-K008: Dado Una nota observada y relato posterior difieren en énfasis, cuando Se prepara la vista de contraste, entonces Ambas procedencias se conservan y se puede expresar desacuerdo sin reemplazarlas por una única versión. Prueba futura de trazabilidad, acceso y regeneración de vista tras una corrección autorizada

**Condición de descarte:** Mantener solo pauta documental si herramientas actuales bastan. Suspender segunda ocasión si no hay interés/disponibilidad o no modifica lectura con esfuerzo aceptable; descartar TDA si reduce contexto o carece de matriz comparable. No imponer investigación extensa para justificar software.

## Memoria de acuerdos culturales: preparar qué retomar y qué volver a preguntar

**ID:** T01-P003. **Estado heredado:** PROPUESTA_NO_IMPLEMENTADA.

**Función y decisión:** Recuperar por espacio los acuerdos prácticos, fuente/ocasión, notas propias y preguntas de revalidación para que otra persona del equipo prepare el acercamiento; conservar nota/calendario/mensajes que ya funcionan. Qué se puede retomar antes de proponer fechas/formato, qué debe confirmarse con anfitriones/equipo y qué puede anunciarse o permanecer como idea sin fecha.

**Valor público condicional:** Continuidad de un servicio cultural compartido y claridad de compromisos; no se declara un programa público formal ni presupuesto comprobado.

**Historias:** HU01-H007, HU01-H008, HU01-H010, HU01-H011, HU01-H012. **Necesidades:** N01-N010, N01-N011, N01-N012, N01-N013, N01-N015, N01-N016, N01-N017.

**Alcance:** Una página por relación con espacio, con interlocución funcional, acuerdos/pendientes y enlaces a calendario/notas autorizados. No agenda central para toda CDMX.; Distinguir lo dicho antes de notas propias después y confirmar vigencia por ocasión; descripciones de ritmos sirven para preguntar y proponer formato.; Vista de preparación y borrador revisable de qué comunicar sobre fechas/entrada/participación autónoma; ideas de futuro y cierre permanecen diferenciados.

**Exclusiones:** Sustituir negociación cultural, visita o mediación emergente; digitalizar cada conversación o exigir perfiles de asistentes y trayectos.; Comprometer salón/equipo unilateralmente, predecir asistencia, fijar horario comunitario óptimo o medir impacto cultural total.; Recomendación acústica, aforo técnico, modelo 3D, apertura automática de espacios o reservas en tiempo real.

**Recursos por obtener:** T01-D008: Notas, interlocución funcional y acuerdos con equipo/anfitriones; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato. T01-D009: Referencias de entrada y borradores de invitación/recepción; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato. T01-D010: Descripciones situadas de ritmos y notas propias posteriores; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato. T01-D011: Calendario de posibilidades/confirmaciones y estado de cierre/ideas; estado REQUERIDO_NO_DISPONIBLE. Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar. No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.

**Operaciones:** Recepción autorizada, identificación del espacio y referencias funcionales sin inventar contactos. Unificar estados posibilidad/confirmado/idea/pendiente/cerrado; separar fecha de visita, de confirmación, de actividad y de escritura de la nota. Construir C008 con fuente/ocasión y pregunta de vigencia; no copiar nota antigua como atributo permanente del lugar. Relacionar confirmación con fecha/función sin unir agendas por coincidencia de nombre ni interpretar silencio. Sin agregación areal ni tasa de participación. Preparar lectura C009 y vista C010. Validación del contenido de invitación es humana; otra voz debe poder matizar la referencia antes de tomarla como actual.

**Funciones propuestas y pendientes de aceptación:** Coordinación cultural, mediación y anfitriones, con confirmaciones independientes.

**Responsabilidades todavía desconocidas:** Quien mantendría notas entre personas del equipo y custodiaría respaldos, por confirmar. Anfitriones y programación/mediación tendrían que revisar pertinencia de referencias/fechas; no hay aceptación directa de carpeta. Responsabilidad de acceso y versión de calendario y de autorizar una eventual difusión.

**Cargas y beneficios:** Podría facilitar relevo sin pedir toda memoria oral y mejorar preguntas; no rapidez o ahorro demostrados. Coordinación seleccionaría notas mínimas, equipo sostendría versiones y anfitriones solo confirmarían lo pertinente a ocasión nueva. Se evita migrar toda comunicación que ya funciona o cargar a asistentes con registro continuo.

**Pruebas de contenido heredadas:** T01-K009: Dado Otra persona del equipo retoma una relación con notas autorizadas, cuando Prepara un nuevo acercamiento, entonces Distingue acuerdos prácticos y qué confirmar, fuente anterior y notas propias sin necesitar memoria oral completa ni tratar la nota como mandato. Ensayo futuro de preparación con material real y revisión de coordinación; valorar esfuerzo de dejar notas y calidad de preguntas T01-K010: Dado Se considera anunciar una serie con fechas posibles y confirmadas, cuando Se revisa el contenido comunicable, entonces Se separa posibilidad de confirmación por fecha/equipo/uso y quedan pendientes que impidan cumplir lo ofrecido. Cotejo futuro de calendario, mensajes y borrador, sin envío; revisión con funciones pertinentes T01-K011: Dado Se revisa invitación/recepción de otra convocatoria, cuando Se comunica entrada y participación, entonces La indicación de puerta tiene respaldo y se entiende que escuchar basta, escritura es optativa y no se exige asistencia previa. Prueba futura de comprensión voluntaria y cotejo con confirmación del espacio; no inventar respuestas T01-K012: Dado La serie terminó y hay interés o ideas futuras, cuando Se retoma memoria del espacio, entonces Se distingue cierre de compromiso futuro; no se atribuye opinión colectiva ni fecha inexistente y descripción de ritmos se revalida. Revisión futura de estados y procedencia con nota/calendario; ensayo de preguntar por vigencia

**Condición de descarte:** Si no hay relevo real o la nota/calendario/mensajes bastan, mantenerlos y usar una pauta mínima sin nuevo sistema. Reformular si sostener notas pesa más que su utilidad o si anfitriones/equipo no encuentran pertinente documentar; retirar descripciones que se conviertan en etiquetas rígidas.

## Protocolo comparativo de utilidad y esfuerzo

Participantes futuros: una persona de la función usuaria pertinente y una revisora de contenido con competencia acreditada; no se registra aquí aceptación ni ejecución. El caso debe ser el mismo y estar autorizado para ambas condiciones. Se compara la práctica actual con el apoyo propuesto, conservando insumos equivalentes; si no es posible, se explicita que la comparación no aísla el apoyo. El orden debe controlarse o registrarse para no atribuir aprendizaje al producto.

| Producto | Tarea y respuesta correcta | Ayuda y registro | Avanzar o detener |

|---|---|---|---|

| Expediente territorial | Explicar qué cambió, por qué, con qué respaldo y duda; decidir consultar si no alcanza | Fuentes autorizadas iguales; registrar enlaces usados, ayudas solicitadas, errores de identidad, decisión, duración y esfuerzo sólo si se medirán | Avanzar si mejora comprensión con carga aceptable acordada; detener ante falsa certeza de puerta o modificación no autorizada |

| Memoria cultural | Distinguir confirmado, posible y pendiente, y formular qué revalidar con anfitriones | Notas y calendario permitidos; registrar compromisos atribuidos erróneamente, aclaraciones y esfuerzo de mantener | Avanzar si facilita relevo sin convertir nota antigua en mandato; simplificar si soportes actuales bastan |

| Cuaderno de ocasiones | Comparar qué puede afirmarse con una ocasión y con ambas; reducir afirmación o justificar no seguir | Relatos autorizados, sin opciones imputadas; registrar cambio de afirmación, procedencia, ayuda y carga | Avanzar si aporta distinción útil con participación voluntaria; detener si requiere registro que no se acepta |

## Qué mide cada comprobación

Calidad del dato: identidad, fuente, campos indispensables, unidades, nulos y permisos. Contenido: interpretación defendible y límite de afirmación según revisora pertinente. Utilidad: tarea y decisión correctamente resueltas. Esfuerzo: trabajo de consulta y de mantenimiento que las personas acepten evaluar. No se mezclan estos cuatro planos en una puntuación única. La línea de base se medirá con la práctica actual, no se inventa retrospectivamente un ahorro o umbral.

## Continuidad y actualización

Cada producto necesita una función custodio, quien revise contenido y autoridad de acceso/cambio, nombradas antes de operar. Una observación, uso nuevo o acuerdo modificado puede activar revisión; no se inventa frecuencia semanal. Versionar entradas, notas y salidas; preservar historia de cambios y retirar salidas afectadas, sin borrar evidencia. Transferir requiere que otra persona pueda explicar contenido, límites y pendientes con permisos iguales.

## Plan secuencial sin fechas ficticias

| Puerta | Dependencia | Función propuesta | Evidencia de cierre |

|---|---|---|---|

| Revisión interpretativa | Corpus y formulaciones disponibles | Autor y revisora humana independiente por acordar | Observaciones, resolución y desacuerdos conservados |

| Fuente y autoridad | Decisión territorial delimitada | Custodio/productor y coordinación | Conjunto, edición, permiso, diccionario y procedimiento aplicable |

| Prototipo proporcional | Fuentes compatibles y aceptación de mantenimiento | Diseño y desarrollo | Contrato, ejemplo autorizado y pruebas técnicas, sin despliegue implícito |

| Comparación con práctica actual | Caso equivalente y participación acordada | Función usuaria y revisora de contenido | Tarea, respuesta, ayudas, errores, decisión y esfuerzo |

| Continuidad o descarte | Resultado de prueba y recursos | Custodia y coordinación | Decisión explícita de conservar, simplificar, detener o implementar con responsable |
