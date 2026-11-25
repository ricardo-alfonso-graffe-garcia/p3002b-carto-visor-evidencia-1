# Productos candidatos · revisión 1.1

## Expediente de revisión: qué cambió en el lugar y con qué respaldo (T01-P001)

**id**: T01-P001

**nombre**: Expediente de revisión: qué cambió en el lugar y con qué respaldo

**origen**: OPORTUNIDAD_PROPUESTA

**estado**: PROPUESTA_NO_IMPLEMENTADA

**funcion**: Recuperar una revisión concreta por identificador/nombre, comparar descripción y fundamento y mostrar la duda que condiciona su reutilización. El mapa es auxiliar si persiste una pregunta espacial; el resultado central es una explicación acotada.

**usuarios**: - ACT01-A001

**historias**: - HU01-H001

- HU01-H002

- HU01-H003

**necesidades**: - N01-N001

- N01-N002

- N01-N003

- N01-N004

**decision**: Conservar identificador/punto, modificar solo lo sustentado o detener una modificación; al retomar, decidir si el respaldo responde a la tarea o hace falta nueva aclaración.

**argumento**: El caso de tres registros se atendió con tabla, croquis y conversación. La técnica conservó sitio/punto y cambió descripción de acceso, con aclaración mediada. El ideal pide recuperar el sentido del último cambio, no corregir toda base ni demostrar que faltó una plataforma. Por eso la propuesta organiza fundamento y versiones y preserva la pregunta a quien conoce el sitio.

**alcance**: - Una relación/revisión autorizada de lugares y sus fuentes pertinentes; iniciar con el último cambio que afecte identificación y no con catálogo urbano.

- Búsqueda por identificador/nombre, comparación antes/después y estado de duda con referencia espacial opcional.

- Extensión separable de auditoría de asignaciones a dos unidades, únicamente si aparecen registros operativos y particiones justificadas. No es condición del expediente básico.

**exclusiones**: - Organizar visitas, verificar puertas en campo, garantizar ingreso o certificar precisión de un acceso.

- Actualizar automáticamente todas las bases, registrar toda conversación o todos los desconocimientos.

- Declarar una geometría SSC correcta, inferir error por límites distintos o hacer ranking territorial desde entrevistas.

**datos**: - **id**: T01-D001
  
  **variable**: Petición, tabla/copia revisada y finalidad de revisión
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: por registro y versión documental; granularidad de revisión para responder a la copia concreta. Fechas de registro/observación separadas; resolución real desconocida.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

- **id**: T01-D002
  
  **variable**: Nota de último cambio, fundamento, croquis/aclaración y duda pertinente
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: una afirmación por cambio y respaldo; distinguir sitio y acceso. Sin precisión métrica mínima inventada; mapa solo si ayuda a reconocer entidad.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

- **id**: T01-D003
  
  **variable**: Referencias espaciales y particiones operativas si se activa auditoría
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: identidad/versiones de referencia y asignación por registro; escala/resolución/CRS deberán conocerse antes de medir. Sin valores de capas SSC.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

- **id**: T01-D004
  
  **variable**: Marco Geoestadístico como referencia contextual opcional
  
  **estado**: CANDIDATO_DOCUMENTADO
  
  **fuente**: T01-F014
  
  **acceso**: Solo referencia documental consultada; autorización y obtención del contenido por comprobar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: edición/partición coherente con periodo y finalidad de comparación; no seleccionada aún. Resolución real no inspeccionada.
  
  **limites**: Solo descripción oficial indexada. No contenido descargado, atributo, CRS o geometría verificados. No reemplaza autoridad operativa ni jurídica. Coordinación corroboró el fundamento metodológico general en F041, sin adquirir contenido vectorial o permiso de uso operativo.
  
  **fuentes_contexto**: - T01-F041

**operaciones**: - Recepción autorizada y huella; delimitar encargo antes de unir datos.

- Unión semántica por identidad justificada, no por calle/nombre parecido. Versionar diferencias de significado: sitio, acceso, descripción, traslado.

- No convertir CRS por defecto. Si se aporta geometría necesaria, validar referencia/ejes/unidad y transformar a CRS adecuado a operación documentada; conservar origen. No se ejecuta ahora.

- Construir C007 y lectura C009; seleccionar respaldo pertinente y mantener conversación nueva como actividad humana.

- Si se activa resumen: fijar C004 y comparar particiones sobre mismos registros/periodo, conciliar asignaciones y exclusiones C005; tasas solo con marco de revisiones compatible. No promediar tasas sin pesos ni transferir población por área sin justificar.

**modulos**: - T01-M001

- T01-M002

- T01-M003

- T01-M004

- T01-M005

- T01-M006

**salida_e_interaccion**: Ficha textual de revisión con qué se conservó/modificó, por qué y qué no se comprobó, línea de versiones y enlaces a respaldos autorizados. Buscar, poner revisiones lado a lado y formular duda localizada. Mapa/croquis abre bajo petición; si se habilita auditoría, panel A/B de unidad/denominador/exclusiones rotulado como sensibilidad. No mapa inicial obligatorio.

**actividad_humana**: La técnica interpreta correspondencia y explicita el alcance de su revisión. Colega aporta otra lectura sin autorizar toda decisión; fuente mediada debe mantenerse atribuida al equipo. Conversar cuando aparece información nueva. No ejecutar contacto o cambio en bases desde T01.

**responsables_pendientes**: - Responsable técnico y custodio de registro por confirmar con institución/alcance exactos.

- Aportante de croquis/aclaración y mantenimiento de nota; aceptación de compañera no recabada.

- Responsable de permisos/retención y, si hay auditoría, emisor de particiones y revisor de asignaciones.

**incertidumbres**: - No están los originales de tabla/croquis/copia ni las capas SSC. No hay precisión o CRS acreditados.

- Persisten dudas del otro acceso; no son carencia que bloquee esta revisión ya atendida ni prueban uso futuro.

- Consistencia de notas entre registros y carga de mantenerlas no medidas; quién confirma condiciones de otra solicitud sigue pendiente.

**cargas_y_beneficios**: Podría reducir reconstrucciones de sentido al retomar una revisión; beneficio no medido. Quien revisa asumiría escribir una explicación pertinente, quien conserva respaldos gestionaría acceso/versiones y quien observa aclararía solo preguntas dentro de su experiencia. Evitar que el coste de llenar historial supere notas que ya funcionan.

**criterios**: - **id**: T01-K001
  
  **dado**: Una revisión autorizada con sitio/punto y nueva descripción de acceso
  
  **cuando**: Se comparan respaldo y diferencia de calle
  
  **entonces**: La explicación permite conservar sitio/punto sin inferir traslado, puerta única o cancelación de acceso
  
  **metodo**: Ensayo futuro de tarea con respaldos reales; cotejo con responsable técnico y evidencia de alcance
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: Depende de soportes no aportados; no simular episodio nuevo. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K002
  
  **dado**: Una consulta se refiere a una copia/version concreta
  
  **cuando**: Otra persona retoma el último cambio pertinente
  
  **entonces**: Puede explicar qué cambió, por qué y qué duda importa, o detectar necesidad de nueva aclaración
  
  **metodo**: Comparación futura entre consulta con notas actuales y expediente propuesto, conservando interpretación y esfuerzo; sin umbral de ahorro predefinido
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: No crear confusión de versiones como incidente histórico. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K003
  
  **dado**: Se activa extensión espacial con datos autorizados y dos particiones
  
  **cuando**: Se comparan asignaciones y resumen en ambas
  
  **entonces**: Se concilian registros únicos, ambigüedades y exclusiones; denominador desconocido impide tasa y salida igual no certifica equivalencia
  
  **metodo**: Prueba futura de conservación de entidades y revisión de muestra de bordes/solapes; contrastar informe de parámetros con fuentes
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: Extensión opcional; sin capas ni análisis territorial en T01. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K004
  
  **dado**: Falta CRS, respaldo de identidad o permiso necesario
  
  **cuando**: Se intenta transformación afectada
  
  **entonces**: Operación se detiene con pregunta localizada y el original permanece; lectura textual autorizada puede continuar
  
  **metodo**: Pruebas futuras de contrato y control de versiones/acceso, sin datos personales de ejemplo en T01
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: Detener solo rama dependiente; no convertir todo desconocimiento en bloqueo general. Sin ensayo de producto, aceptación o desempeño medido en T01.

**condicion_descarte**: Descartar software nuevo si las notas actuales ya permiten retomar con esfuerzo aceptable; reformular como pauta documental si no hay responsable o permiso de mantenimiento. Retirar extensión espacial si no cambia una decisión o si carece de unidades/fuentes compatibles.

**limites**: Propuesta situada, no obligación de alcaldía ni demanda de toda CDMX. N005 queda condición sin historia y sin convertirla en dato de acceso confirmado.

**trazabilidad_argumental**: - **tipo**: DEMANDA_EXPRESADA
  
  **contenido**: Recuperar sentido del último cambio, respaldo y duda pertinente, mediante ideal elicitado; el episodio sí se atendió.
  
  **fuentes_entrada**: - E01-P120–P137
  
  - E01-P155–P157
  
  - N01-N004
  
  - HU01-H003

- **tipo**: CAPACIDAD_DERIVADA
  
  **contenido**: Distinguir entidad, revisión, fuente y alcance antes de cambiar; conservar pregunta y acceso a respaldo.
  
  **fuentes_entrada**: - E01-P029
  
  - E01-P049–P065
  
  - HU01-H001
  
  - HU01-H002
  
  - C002
  
  - C004
  
  - C009
  
  - C016

- **tipo**: OPORTUNIDAD_PROPUESTA
  
  **contenido**: Expediente consultable versionado y mapa auxiliar; auditoría por unidades opcional es ampliación del equipo, no solicitud de participante.
  
  **fuentes_entrada**: - HU01-M001
  
  - HU01-M002
  
  - HU01-M003

## Cuaderno de contraste de ocasiones: decidir qué se puede comparar y afirmar (T01-P002)

**id**: T01-P002

**nombre**: Cuaderno de contraste de ocasiones: decidir qué se puede comparar y afirmar

**origen**: OPORTUNIDAD_PROPUESTA

**estado**: PROPUESTA_NO_IMPLEMENTADA

**funcion**: Colocar dos ocasiones del mismo caso junto a sus palabras, secuencias y procedencias para decidir unidad de comparación y alcance de una afirmación; puede adoptar documentos existentes, sin programa nuevo obligatorio.

**usuarios**: - ACT01-A005

**historias**: - HU01-H004

- HU01-H005

- HU01-H006

**necesidades**: - N01-N006

- N01-N007

- N01-N008

- N01-N009

**decision**: Comparar salidas completas o decisiones puntuales, reducir una explicación de elección a descripción respaldada y decidir si pedir otra ocasión aporta o conviene detener seguimiento.

**argumento**: La investigadora corrigió tiempos no equivalentes al reconocer orígenes y actividades diferentes, y admite que no reconstruyó todas las alternativas. Una segunda ocasión es deseo ideal prioritario dentro de su pregunta, no repetición semanal ya observada. Un cuaderno conserva secuencias y relatos sin inventar causa o convertir narración posterior en registro defectuoso.

**alcance**: - Contraste interno de un caso y una segunda ocasión que la persona considere distinta, si existe interés/disponibilidad y se acuerda periodo pertinente.

- Enlazar afirmación, nota de observación, relato posterior y desconocimiento; permitir esquema y referencias espaciales solo cuando ayuden.

- Exploración TDA únicamente como extensión independiente si una matriz multivariable comparable y volumen justifican su coste después de validar cuaderno básico.

**exclusiones**: - Recopilar cada movimiento o un periodo entero por defecto, publicar ubicaciones identificadoras o GPS.

- Ordenar personas por rapidez, hallar causa única, reconstruir todas las opciones por catálogo o representar dos zonas/ciudad.

- Imponer aprobación académica total a participantes o sustituir conversación con un modelo.

**datos**: - **id**: T01-D005
  
  **variable**: Notas y relatos autorizados de primera ocasión y versiones de afirmación
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: por ocasión y por afirmación/fragmento; separar visto/dicho/interpretado y aproximación temporal. No exige minuto exacto ni fecha inventada.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

- **id**: T01-D006
  
  **variable**: Segunda ocasión contrastante y contexto que se acepte compartir
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: contraste dentro del caso, periodo a acordar; puede bastar secuencia ordinal con contexto. No intervalo fijo semanal.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

- **id**: T01-D007
  
  **variable**: Secuencias/esquemas de actividades, opciones recordadas y referencias espaciales opcionales
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: relaciones tipadas por ocasión, con origen y propósito; tiempo/distancia solo si aportados y comparables. CRS/resolución real desconocidos.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

**operaciones**: - Recibir soportes con permiso y mantener seudonimización y detalle mínimo. Las entrevistas de entrada justifican diseño pero no son los originales de seguimiento que se requieren.

- Unificar vocabulario de actividad/ocasión y marcar modalidad de cada fragmento. No reducir habitual contado a hecho observado.

- Construir C006: relaciones de secuencia/solapamiento y opciones desconocidas; no inferir ruta mínima ni rellenar tiempos.

- Alinear ocasiones por finalidad/unidad conceptual antes de comparar, conservar diferencias de contexto temporal. Convertir unidades solo cuando significado y valor estén documentados; no exigir CRS a esquema conceptual.

- Preparar comparación C009 de qué se puede sostener con una ocasión y con ambas, admitiendo reducción. Sin agregación areal, denominador de habitantes o estadística de población.

**modulos**: - T01-M001

- T01-M002

- T01-M004

- T01-M005

- T01-M006

**salida_e_interaccion**: Dos columnas de ocasiones con narración, actividades, fuente, palabra original y afirmación en revisión. Alternar unidad salida/decisión, abrir fragmento autorizado, conservar desacuerdo y cambiar alcance del argumento. Esquema relacional editable sin presentarse como red vial real; mapa bajo decisión del equipo si aporta.

**actividad_humana**: Equipo y persona participante acuerdan qué compartir; analistas interpretan y deciden qué pueden afirmar, con crítica de colega y retorno parcial cuando sea pertinente. Dejar de investigar una pregunta o explicar menos puede ser resultado suficiente.

**responsables_pendientes**: - Responsable académica y custodia del ejercicio concreto no identificados institucionalmente.

- Personas que aportarían segunda ocasión: interés/disponibilidad y esfuerzo por recabar, sin asumir rechazo.

- Quien mantenga cuaderno y controle acceso a notas/versiones; aceptación de herramienta pendiente.

**incertidumbres**: - No notas originales, nuevas ocasiones, alternativas exhaustivas o versiones de texto aportadas.

- Tiempos aproximados y lo que no se recuerda no tienen por qué convertirse en medición.

- Efecto del contraste y carga del seguimiento desconocidos; un ideal no obliga a producir nuevos registros.

**cargas_y_beneficios**: Puede ayudar a modificar una afirmación con evidencia y evitar comparación impropia; no ahorro medido. Participante asumiría reconstrucción voluntaria, analistas revisarían notas/relaciones y custodio protegería detalles. Un cuaderno ya existente puede ser suficiente y reduce coste de migración.

**criterios**: - **id**: T01-K005
  
  **dado**: Dos reconstrucciones con distinto origen/propósito o actividades
  
  **cuando**: Se intenta comparar tiempos o decisiones
  
  **entonces**: Se explica por qué no son equivalentes y qué comparación acotada sí procede, manteniendo papel situado de tiempo/cercanía
  
  **metodo**: Revisión futura de tarea con textos reales, cotejando unidad y fuentes; comparar contra interpretación de equipo
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: No basta ver dos líneas próximas en mapa. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K006
  
  **dado**: Se dispone voluntariamente de segunda ocasión contrastante
  
  **cuando**: Se compara qué puede decirse con una y con dos
  
  **entonces**: Se precisa o reduce afirmación o se justifica que seguimiento no aporta; no se exige periodo entero
  
  **metodo**: Ensayo futuro de contraste con acuerdos y material autorizado, registrar decisión y esfuerzo sin umbral de éxito inventado
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: No se atribuye aceptación o seguimiento nuevo. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K007
  
  **dado**: Una afirmación pretende explicar elección entre opciones no reconstruidas
  
  **cuando**: Se revisa el vínculo con respaldo
  
  **entonces**: Opciones desconocidas siguen visibles y analista acota explicación, sin imputarlas desde catálogo o casos ajenos
  
  **metodo**: Auditoría futura de afirmación→fragmento→modalidad, con revisión humana de explicaciones alternativas
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: Crítica externa no aprueba interpretación total. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K008
  
  **dado**: Una nota observada y relato posterior difieren en énfasis
  
  **cuando**: Se prepara la vista de contraste
  
  **entonces**: Ambas procedencias se conservan y se puede expresar desacuerdo sin reemplazarlas por una única versión
  
  **metodo**: Prueba futura de trazabilidad, acceso y regeneración de vista tras una corrección autorizada
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: No equiparar desacuerdo con error de captura ni conversión de relato en observación. Sin ensayo de producto, aceptación o desempeño medido en T01.

**condicion_descarte**: Mantener solo pauta documental si herramientas actuales bastan. Suspender segunda ocasión si no hay interés/disponibilidad o no modifica lectura con esfuerzo aceptable; descartar TDA si reduce contexto o carece de matriz comparable. No imponer investigación extensa para justificar software.

**limites**: No se implementa seguimiento ni se generalizan preferencias. Las tres historias contienen necesidades atendidas, carencia específica e ideal: conservan sus estados distintos.

**trazabilidad_argumental**: - **tipo**: DEMANDA_EXPRESADA
  
  **contenido**: Desea variación entre ocasiones y primero segundo contraste voluntario, con secuencia, palabras y desconocidos.
  
  **fuentes_entrada**: - E02-P128–P145
  
  - E02-P148
  
  - E02-P162
  
  - N01-N009
  
  - HU01-H006

- **tipo**: CAPACIDAD_DERIVADA
  
  **contenido**: Separar unidad de comparación, ocasión y nivel de afirmación; enlazar evidencia y opciones no reconstruidas sin borrar diferencias.
  
  **fuentes_entrada**: - E02-P058–P065
  
  - E02-P070–P097
  
  - HU01-H004
  
  - HU01-H005
  
  - C009
  
  - C023
  
  - C024
  
  - C029

- **tipo**: OPORTUNIDAD_PROPUESTA
  
  **contenido**: Cuaderno estructurado de contraste, preferentemente sobre soportes actuales; TDA sería otra propuesta a reconsiderar, no solicitud ni método observado.
  
  **fuentes_entrada**: - HU01-M004
  
  - HU01-M005
  
  - HU01-M006

## Memoria de acuerdos culturales: preparar qué retomar y qué volver a preguntar (T01-P003)

**id**: T01-P003

**nombre**: Memoria de acuerdos culturales: preparar qué retomar y qué volver a preguntar

**origen**: OPORTUNIDAD_PROPUESTA

**estado**: PROPUESTA_NO_IMPLEMENTADA

**funcion**: Recuperar por espacio los acuerdos prácticos, fuente/ocasión, notas propias y preguntas de revalidación para que otra persona del equipo prepare el acercamiento; conservar nota/calendario/mensajes que ya funcionan.

**usuarios**: - ACT01-A012

**historias**: - HU01-H007

- HU01-H008

- HU01-H010

- HU01-H011

- HU01-H012

**necesidades**: - N01-N010

- N01-N011

- N01-N012

- N01-N013

- N01-N015

- N01-N016

- N01-N017

**decision**: Qué se puede retomar antes de proponer fechas/formato, qué debe confirmarse con anfitriones/equipo y qué puede anunciarse o permanecer como idea sin fecha.

**argumento**: Tres encuentros se organizaron con consulta parcial, visita y confirmación de fechas. La comunicación simple bastó; la carpeta imaginada aporta relevo entre personas y preguntas para conversación nueva. La necesidad parcialmente abierta de explicitar autonomía de sesiones exige revisar lenguaje y recepción, no inferir preferencia de asistentes o construir un ranking de salones.

**alcance**: - Una página por relación con espacio, con interlocución funcional, acuerdos/pendientes y enlaces a calendario/notas autorizados. No agenda central para toda CDMX.

- Distinguir lo dicho antes de notas propias después y confirmar vigencia por ocasión; descripciones de ritmos sirven para preguntar y proponer formato.

- Vista de preparación y borrador revisable de qué comunicar sobre fechas/entrada/participación autónoma; ideas de futuro y cierre permanecen diferenciados.

**exclusiones**: - Sustituir negociación cultural, visita o mediación emergente; digitalizar cada conversación o exigir perfiles de asistentes y trayectos.

- Comprometer salón/equipo unilateralmente, predecir asistencia, fijar horario comunitario óptimo o medir impacto cultural total.

- Recomendación acústica, aforo técnico, modelo 3D, apertura automática de espacios o reservas en tiempo real.

**datos**: - **id**: T01-D008
  
  **variable**: Notas, interlocución funcional y acuerdos con equipo/anfitriones
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: acuerdo por asunto/función y, cuando se anuncie, fecha concreta confirmada; ocasión descriptiva si se retoma nota sin día exacto. No cambia resolución temporal desconocida de HU01.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

- **id**: T01-D009
  
  **variable**: Referencias de entrada y borradores de invitación/recepción
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: referencia verbal reconocible de puerta y alcance de participación por sesión; no precisión de coordenada ni ruta de asistentes.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

- **id**: T01-D010
  
  **variable**: Descripciones situadas de ritmos y notas propias posteriores
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: franja/ocasión con fuente y contexto del uso, sin convertir descripción en serie horaria; grano a acordar según duración/formato que se discuta.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

- **id**: T01-D011
  
  **variable**: Calendario de posibilidades/confirmaciones y estado de cierre/ideas
  
  **estado**: REQUERIDO_NO_DISPONIBLE
  
  **fuente**: null (no determinado según contexto)
  
  **acceso**: Fuente funcional candidata mencionada en relato; soporte original no aportado, disponibilidad y autorización por confirmar.
  
  **licencia**: No determinada para el soporte/contenido; no transferir MIT ni licencia de documentación al dato.
  
  **resolucion_requerida**: PROPUESTA: fecha y función confirmante para compromisos efectivos; idea admite ausencia de fecha, sin promoverla a programación. Valores originales no aportados.
  
  **limites**: No payload aportado o inspeccionado; no se afirma acceso operativo.

**operaciones**: - Recepción autorizada, identificación del espacio y referencias funcionales sin inventar contactos.

- Unificar estados posibilidad/confirmado/idea/pendiente/cerrado; separar fecha de visita, de confirmación, de actividad y de escritura de la nota.

- Construir C008 con fuente/ocasión y pregunta de vigencia; no copiar nota antigua como atributo permanente del lugar.

- Relacionar confirmación con fecha/función sin unir agendas por coincidencia de nombre ni interpretar silencio. Sin agregación areal ni tasa de participación.

- Preparar lectura C009 y vista C010. Validación del contenido de invitación es humana; otra voz debe poder matizar la referencia antes de tomarla como actual.

**modulos**: - T01-M001

- T01-M002

- T01-M004

- T01-M005

- T01-M006

**salida_e_interaccion**: Página inicial de acuerdos prácticos y preguntas, con fuente/ocasión, estados en palabras, alcance de cada fecha y enlace a calendario actual. Abrir nota anterior, distinguir relato/nota propia, preparar pregunta y marcar respuesta como nueva versión. Croquis de entrada opcional si se aporta y ayuda; comparación por espacio/ocasión sin puntuar barrios.

**actividad_humana**: Coordinar significa construir sentido, no solo cruzar horas. Equipo y anfitriones revalidan condiciones; mediadora mantiene margen para adaptar conversación. Al retomar, se pregunta cómo está ahora, sin explicarles su espacio desde una nota antigua. Nadie está contactado o comprometido por esta propuesta.

**responsables_pendientes**: - Quien mantendría notas entre personas del equipo y custodiaría respaldos, por confirmar.

- Anfitriones y programación/mediación tendrían que revisar pertinencia de referencias/fechas; no hay aceptación directa de carpeta.

- Responsabilidad de acceso y versión de calendario y de autorizar una eventual difusión.

**incertidumbres**: - No están calendario, mensajes, invitación o notas originales; no fuente de ritmos para todo espacio nuevo.

- Consulta fue parcial y no respuesta no explica disposición o ausencia; no perfiles individuales.

- Una visita en horario parecido no cubre todas las fechas; cambio de actividad puede exigir volver a visitar.

- Facilidad y carga de mantenimiento no probadas; interés en volver no obliga a nueva serie.

**cargas_y_beneficios**: Podría facilitar relevo sin pedir toda memoria oral y mejorar preguntas; no rapidez o ahorro demostrados. Coordinación seleccionaría notas mínimas, equipo sostendría versiones y anfitriones solo confirmarían lo pertinente a ocasión nueva. Se evita migrar toda comunicación que ya funciona o cargar a asistentes con registro continuo.

**criterios**: - **id**: T01-K009
  
  **dado**: Otra persona del equipo retoma una relación con notas autorizadas
  
  **cuando**: Prepara un nuevo acercamiento
  
  **entonces**: Distingue acuerdos prácticos y qué confirmar, fuente anterior y notas propias sin necesitar memoria oral completa ni tratar la nota como mandato
  
  **metodo**: Ensayo futuro de preparación con material real y revisión de coordinación; valorar esfuerzo de dejar notas y calidad de preguntas
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: No aprobación de anfitriones recabada; utilidad no medida. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K010
  
  **dado**: Se considera anunciar una serie con fechas posibles y confirmadas
  
  **cuando**: Se revisa el contenido comunicable
  
  **entonces**: Se separa posibilidad de confirmación por fecha/equipo/uso y quedan pendientes que impidan cumplir lo ofrecido
  
  **metodo**: Cotejo futuro de calendario, mensajes y borrador, sin envío; revisión con funciones pertinentes
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: Confirmaciones deben producirse realmente; no exigir asistencia exacta. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K011
  
  **dado**: Se revisa invitación/recepción de otra convocatoria
  
  **cuando**: Se comunica entrada y participación
  
  **entonces**: La indicación de puerta tiene respaldo y se entiende que escuchar basta, escritura es optativa y no se exige asistencia previa
  
  **metodo**: Prueba futura de comprensión voluntaria y cotejo con confirmación del espacio; no inventar respuestas
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: Pregunta de una persona no equivale a confusión general. Sin ensayo de producto, aceptación o desempeño medido en T01.

- **id**: T01-K012
  
  **dado**: La serie terminó y hay interés o ideas futuras
  
  **cuando**: Se retoma memoria del espacio
  
  **entonces**: Se distingue cierre de compromiso futuro; no se atribuye opinión colectiva ni fecha inexistente y descripción de ritmos se revalida
  
  **metodo**: Revisión futura de estados y procedencia con nota/calendario; ensayo de preguntar por vigencia
  
  **estado**: PROPUESTO_NO_EJECUTADO
  
  **limites**: Terminar es resultado válido; no promesa de seguimiento individual. Sin ensayo de producto, aceptación o desempeño medido en T01.

**condicion_descarte**: Si no hay relevo real o la nota/calendario/mensajes bastan, mantenerlos y usar una pauta mínima sin nuevo sistema. Reformular si sostener notas pesa más que su utilidad o si anfitriones/equipo no encuentran pertinente documentar; retirar descripciones que se conviertan en etiquetas rígidas.

**limites**: Historia H009 se preserva como mediación situada fuera del producto. Fuentes funcionales no son proveedores comprometidos ni instituciones enlazadas a E01/E02.

**trazabilidad_argumental**: - **tipo**: DEMANDA_EXPRESADA
  
  **contenido**: Carpeta ideal con acuerdos/preguntas y ritmos contados por quienes conocen, priorizando acuerdos y revalidación; comunicación pequeña actual suficiente.
  
  **fuentes_entrada**: - E03-P149–P169
  
  - E03-P181–P182
  
  - N01-N016
  
  - N01-N017
  
  - HU01-H011
  
  - HU01-H012

- **tipo**: CAPACIDAD_DERIVADA
  
  **contenido**: Conservar estados de compromiso y fuente/ocasión; distinguir visita de confirmación, idea de programación y pregunta individual de preferencia general.
  
  **fuentes_entrada**: - E03-P029
  
  - E03-P037–P040
  
  - E03-P050–P081
  
  - HU01-H007
  
  - HU01-H008
  
  - HU01-H010
  
  - C034
  
  - C042
  
  - C045
  
  - C060

- **tipo**: OPORTUNIDAD_PROPUESTA
  
  **contenido**: Memoria mínima para relevo con estados y preguntas versionadas, sin imponer plataforma al equipo o anfitriones.
  
  **fuentes_entrada**: - HU01-M007
  
  - HU01-M008
  
  - HU01-M010
  
  - HU01-M011
  
  - HU01-M012