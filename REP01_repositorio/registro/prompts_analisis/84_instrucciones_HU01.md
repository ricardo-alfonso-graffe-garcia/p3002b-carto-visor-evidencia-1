# HU01 · Historias de usuario, perfiles analíticos y objetos digitales

Encargo 1.0 · 25 de noviembre de 2026 · P3002B, Evidencia 1.

Lee estas instrucciones y 85_insumos_HU01.zip. Esta etapa transforma necesidades revisadas en historias, perfiles y metadatos, y los representa como prototipos locales orientados a FAIR Digital Objects (FDO). No implementa el visor, no publica un repositorio ni registra PIDs. El apartado técnico posterior decidirá productos y aplicaciones de los cuatro lentes con esta base.

## Base y objetivo

Comprueba manifest.json. Las entradas preferidas son cinco corpus 1.0, libro común 1.3, cinco recodificaciones y S01/P01/D01/ACT01/N01 revisadas 1.1. N01 conserva 29 necesidades, 351 evidencias, cinco casos, 22 hallazgos y 29 propuestas de comprobación. Hay 20 necesidades actuales atendidas, una parcial, una carencia declarada para explicar más, seis deseos ideales y una inferencia condicional. Prioridades son locales; portafolio entre casos pendiente. No convierte una necesidad atendida en fallo ni en función nueva obligatoria.

Lee las cinco conversaciones completas y sus procesos, con el ejercicio ideal, suficiencia, correcciones y restricciones. Después usa necesidades, actores y síntesis revisadas. JSON permite consulta precisa sin repetir íntegra la evidencia duplicada en todos los soportes; registra qué se leyó y con qué alcance. No equipares integridad con lectura.

En N01 los códigos_comunes son asignaciones existentes en segmentos citados; codigos_contextuales conserva seis relaciones conceptuales separadas. No las presentes como ocurrencias nuevas ni recodifiques. ACT01 distingue acciones propias y terceros relatados; todas las posiciones ante homologación siguen no recabadas. D01 mantiene cero episodios con fuente formal directamente atribuida y diez preguntas pendientes. No atribuyas manuales o aceptación a los casos por semejanza.

El objetivo es expresar quién intenta hacer qué y para qué decisión, en condiciones concretas, sin imponer base única, mapa, IA o automatización. Las historias son formulaciones analíticas derivadas: la frase «Como…, quiero…, para…» no es una cita ni un compromiso aceptado por la persona.

## Reglas de diseño

1. No fijes una historia por entrevista, una historia por necesidad o un número de arquetipos. Una historia puede integrar necesidades que concurren en una misma decisión, conservando restricciones distintas. Revisa las 29 necesidades y justifica el tratamiento de cada una. Los seis deseos ideales N004, N009, N016, N017, N023 y N029 deben tener desarrollo explícito en historias, sin declararlos carencias pasadas. N005 puede permanecer como condición pendiente si falta actividad futura definida.
2. Separa historias ACTUAL_A_PRESERVAR, IDEAL_A_CONTRASTAR y CONDICIONAL. Preservar una práctica no obliga a digitalizarla. El soporte ideal mencionado se registra como preferencia y su función se explica; no se sustituye muestra física por fotografía, conversación por formulario o exploración por recomendación automática sin fundamento.
3. Perfiles analíticos sintetizan actividad, capacidades, decisiones, restricciones y necesidades. No inventes edad, género, ingreso, biografía, jerarquía o motivación. Un PERFIL_FUNCIONAL puede limitarse a una voz; un ARQUETIPO_CANDIDATO necesita patrón respaldado entre al menos dos casos, variantes y contraejemplo/límite. No se vuelve representativo por agrupar casos. Cubrir las cinco voces no obliga a convertirlas en cinco arquetipos.
4. Conserva diversidad de usuarios y los dos perfiles no especializados. La autonomía del mostrador, el desempeño textil, el acuerdo con una amistad y el descubrimiento de libros no se convierten en obligaciones de productores públicos. No excluyas una necesidad legítima por no caber en un visor; distingue relevancia territorial, uso privado y pertinencia de producto por validar.
5. Cada historia tiene evidencia participante y referencias N01. Una síntesis, un mandato o una hipótesis de ganancia no sustituye esa fuente. Las preferencias de terceros siguen relatadas. Contexto de preguntas y ejercicio ideal permanece identificable.
6. Criterios de aceptación son propuestas observables, nunca pruebas ejecutadas o aceptación recabada. Usa Dado/Cuando/Entonces cuando ayude; indica qué criterio N01 adaptas, qué propuso el análisis, qué sigue desconocido y qué límite evita una promesa excesiva. No inventes porcentajes, tiempos, pesos, precisión, cantidades o umbrales de ruido.
7. No asignes una prioridad urbana o cartera implementable. Si integras necesidades con prioridades diferentes, explica momento y condición; no elijas automáticamente el máximo. La prioridad del análisis se distingue de importancia expresada y factibilidad pendiente.
8. El metaalgoritmo es una secuencia propuesta para atender una decisión: insumos, comprobación de significado/calidad, comparación/armonización pertinente, presentación, interpretación, confirmación y decisión. Incluye intervención humana donde hace falta. No todos los pasos se requieren en cada historia ni operaciones sofisticadas por demostrar temario. No describas el proceso actual como si ya ejecutara el nuevo método.

## Dos clases de metadatos

**Metadatos de información requerida por la historia:** describen qué dato o conocimiento permitiría atenderla. Distingue valores respaldados, propuestas de diseño, desconocidos y no aplicables. Para una nota o muestra no impongas CRS, raster, resolución métrica o denominador poblacional. Cuando sí aplique, explica unidad, escala y límites sin inventarlos. Documento del dato no equivale a dato disponible; fuente deseada no equivale a proveedor dispuesto.

**Metadatos del objeto digital:** describen el artefacto analítico —necesidad, historia, perfil o perfil de metadatos—: id local, tipo, versión, contenido, procedencia, ubicación, integridad, acceso, licencia y relaciones. No confundir actor del relato con autor del archivo o responsable futuro de una base.

Cada necesidad N01 y cada historia, perfil y perfil de metadatos de HU01 tendrá representación JSON individual en el ZIP. El registro principal permitirá resolver ids a archivos. Es un prototipo local orientado a FDO, sin declarar conformidad integral o PIDs externos registrados. Un SHA-256 prueba integridad, no calidad de interpretación.

Las referencias primarias de preparación están en referencias_FAIR_FDO.md y .json. El FDO Forum remite a su especificación actual y distingue documentos anteriores; la arquitectura consultada se declara borrador. No mezcles versiones como una norma única ni adoptes atributos no leídos como requisitos universales. El perfil local de este ejercicio es una decisión metodológica documentada, sin registro externo de tipos/perfiles. FAIR admite condiciones de acceso: no concede permisos de publicación. Conserva licencias desconocidas como null; no apliques por defecto una licencia a las entrevistas o al conjunto.

Evalúa RO-Crate, metadatos DataCite, vocabulario PROV y nanopublicaciones por utilidad y alcance: USO_PROPUESTO, NO_IMPLEMENTADO o NO_PERTINENTE_CON_RAZON. La evaluación no es conformidad o implementación. Si necesitas afirmaciones técnicas nuevas, consulta fuente primaria oficial y registra lectura efectiva; si no puedes verificarla, limita la propuesta. No es obligatorio implementar esos empaquetados en HU01.

## Contrato JSON

Objeto con las siguientes claves. Los ids locales son estables; no reasignes un id a otra entidad si corriges una salida. Unknowns se registran, sin inventar fechas, nombres de autor o permisos.

**metadatos:** tarea HU01; resultado_version 1.0; corpus_version 1.0; libro_version 1.3; sintesis_version, procesos_version, documental_version, actores_version y necesidades_version 1.1; estado HISTORIAS_PARA_REVISION; tipo_revision ASISTIDA_POR_LLM; revision_humana_independiente PENDIENTE; modelo/parametros null si no constan; fuente_modelo explica lo informado por interfaz.

**lectura_entradas:** lista {archivo,alcance,comprobacion}. **decisiones_metodologicas:** lista {decision,fundamento}. **citas_ilustrativas:** lista, puede estar vacía; cada cita contiene referencia N01-V…, cita y uso. Debe ser fragmento continuo dentro de la cita canónica N01 correspondiente y conserva su párrafo/voz. No uses comillas para paráfrasis de historias.

**perfiles_analiticos:** lista, ids HU01-P001. Cada perfil: nombre, tipo PERFIL_FUNCIONAL o ARQUETIPO_CANDIDATO, descripcion, actores (ACT01-A…), entrevistas, necesidades (N01-N…), capacidades, restricciones, patron, contraejemplo_y_limite y evidencias (N01-V…). Capacidades/restricciones son listas de textos; patrón es síntesis, no biografía. Los perfiles deben cubrir las cinco voces. Un arquetipo candidato incluye dos casos o más con evidencia propia para cada uno.

**historias:** lista sin cuota, ids HU01-H001. Campos:

- titulo, formulacion («Como… quiero… para…»), actores (lista ACT01-A…), perfil (HU01-P… o null), necesidades (lista N01-N…), entrevistas, tipo (ACTUAL_A_PRESERVAR, IDEAL_A_CONTRASTAR, CONDICIONAL), contexto, objetivo, beneficio_o_decision, restricciones y preservar (listas), evidencias (N01-V… no vacía), limites.
- criterios: lista no vacía {id HU01-K001,dado,cuando,entonces,origen,criterios_n01,estado,limites}. origen PROPUESTA_ANALITICA o ADAPTADO_DE_CRITERIO_N01; criterios_n01 lista N01-K…; estado PROPUESTO_NO_EJECUTADO. Un observable declarado en N01 no vuelve aceptado el criterio de producto.
- prioridad: {nivel,ambito,origen,razon,limites}; nivel ALTA, MEDIA, BAJA o PENDIENTE; origen ANALISIS_CONDICIONAL; ámbito explícito de actividad/modalidad o PORTAFOLIO_EXPLORATORIO. No afirmar aceptación ADIP o factibilidad.
- perfil_metadatos: HU01-M… que describe información para esta historia.
- metaalgoritmo: lista no vacía {id HU01-OP001,nombre,entrada,operacion,salida,intervencion,precondicion,limite}. intervención HUMANA, AUTOMATIZABLE_POR_VALIDAR o MIXTA_POR_VALIDAR. Todos los pasos son propuestas; no se ejecuta el producto.

**perfiles_metadatos:** lista ids HU01-M001. Cada uno: nombre, historias (HU01-H…), descripcion y campos. campos cubre exactamente una vez estos 21 nombres:

variables_significados, fuente_responsable, unidad, cobertura_geografica, escala_espacial, resolucion_espacial, representacion, referencia_espacial, periodo, resolucion_temporal, actualizacion, calidad, incertidumbre, agregacion, denominador, acceso, licencia, procedencia, versiones, transformaciones, vocabulario.

Cada campo: {campo,estado,valor,justificacion,evidencias}. estado RESPALDADO, PROPUESTO, DESCONOCIDO o NO_APLICA. valor JSON o null; DESCONOCIDO/NO_APLICA exige null y razón. evidencias lista N01-V…, no vacía cuando es RESPALDADO; para propuestas o no aplicables explica la decisión. No inventes EPSG, precisión, actualización anual o responsable formal de perfiles anónimos.

**cobertura_necesidades:** exactamente un registro por cada una de las 29 necesidades N01: {necesidad,tratamiento,historias,razon}. Tratamientos DESARROLLADA, INTEGRADA_CON_OTRA, CONSERVADA_COMO_CONDICION, FUERA_DE_ALCANCE_DE_PRODUCTO o PENDIENTE_DE_VALIDACION. Los dos primeros requieren historia y relación inversa. Las demás conservan la necesidad con razón y destino futuro, sin eliminarla. Los seis deseos ideales indicados deben figurar en historias.

**perfil_objeto_local:** {nombre,version,estado,campos,limites}; estado PROPUESTA_LOCAL_NO_REGISTRADA; campos lista de nombres y descripciones de los campos del registro siguiente. Explica cómo se resuelve un id local y qué queda pendiente para un despliegue FDO externo. No registrar tipos/perfiles/PIDs con estas herramientas.

**objetos_digitales:** un registro para cada necesidad N01, perfil analítico, historia y perfil de metadatos. id HU01-OD001; entidad es su id canónico N01-N…/HU01-P…/HU01-H…/HU01-M…; tipo NECESIDAD, PERFIL_ANALITICO, HISTORIA o PERFIL_METADATOS. Campos:

- titulo, descripcion, version (1.1 para necesidad heredada; 1.0 para entidad HU01), estado PROTOTIPO_LOCAL_NO_REGISTRADO.
- ruta_payload, ruta relativa segura a un JSON individual dentro de HU01_soportes_v1.zip; las rutas parten de su carpeta raíz, por ejemplo objetos/necesidades/N01-N001.json. El contenido debe coincidir exactamente con la entidad correspondiente del JSON principal o N01 revisada, sin campos contradictorios.
- sha256 calculado sobre los bytes del archivo individual ya escrito, no sobre una cadena imaginada. El manifiesto excluye su propia huella y no se exige que el JSON principal se hashee a sí mismo.
- pid_externo, tipo_registrado_externo y perfil_registrado_externo: null. El id local no es un DOI ni un PID global resoluble.
- procedencia: {actividad,fuentes,revision}; fuentes son referencias canónicas existentes (necesidades, historias, perfiles, metadatos o N01-V…); distinguir objeto derivado de fuente independiente. revision describe revisión asistida y humana pendiente, sin aval inexistente.
- acceso: {condicion,fundamento,autorizacion_publicacion}; autorización NO_CONSTA. No inferir permiso del consentimiento relatado o del acceso técnico a archivos.
- licencia: {valor,fundamento}; valor null salvo evidencia explícita de una licencia aplicable a ese artefacto concreto, sin ampliar la de fuentes públicas al corpus.
- relaciones: lista {tipo,destino_entidad}; tipo DERIVA_DE, DESCRITO_POR, REPRESENTA o RELACIONADO_CON; destino es id existente de entidad/need/evidencia. No apuntes a un id inexistente por conveniencia.

**estado_fair:** lista que cubre los 15 principios F1,F2,F3,F4,A1,A1.1,A1.2,A2,I1,I2,I3,R1,R1.1,R1.2,R1.3. Cada objeto: {principio,estado,evidencia_local,pendiente,limites}. estado PARCIAL, PENDIENTE o ATENDIDO_LOCALMENTE; ese último solo describe una medida local comprobada, nunca certificación. F1 y F4 no se dan por completos con ids locales/ZIP. No uses un protocolo o registro no desplegado como prueba de acceso o persistencia. No conviertas permiso desconocido en licencia abierta.

**evaluacion_empaquetado:** cuatro registros {opcion,estado,utilidad,dependencias,limites}; opciones RO_CRATE, DATACITE, PROV y NANOPUBLICACIONES; estados USO_PROPUESTO, NO_IMPLEMENTADO o NO_PERTINENTE_CON_RAZON. Incluye fuentes cuando se usen nuevas afirmaciones técnicas, con URL/localizador y lectura efectiva; no conjetures conformidad.

**agenda_validacion:** lista {objeto,pendiente,comprobacion}; objeto id de historia/perfil/metadatos/necesidad o null. **limites:** lista {descripcion,consecuencia}. Mantén incertidumbre sobre factibilidad, aceptación, permisos y aplicabilidad documental.

## Explicación y soportes

HU01_explicacion_v1.md explica el recorrido desde necesidades a historias, decisiones de integración y diferencias entre perfiles. Incluye ejemplos desarrollados de los cinco casos, actuales e ideales, citas verificables y referencias a los archivos. La prosa usa conceptos completos antes de ids; no se convierte en manual de claves. Describe límites y por qué no se producen 29 funciones obligatorias. Las tablas no tienen líneas vacías entre filas.

HU01_soportes_v1.zip incluye:

- LEEME general y un LEEME por subcarpeta que explique el contenido, uso, entradas y límites.
- objetos/: JSON individuales de las 29 necesidades, perfiles, historias y perfiles de metadatos; registro de objetos y manifiesto que permita resolver id→ruta→contenido. El registro principal ya está en el JSON de entrega; la copia del ZIP debe coincidir.
- tablas/: historias, cobertura de 29 necesidades, perfiles, criterios, metadatos y estado FAIR en CSV legible.
- figuras/: visuales de perfiles y del recorrido necesidad→historia→criterio/metadatos que cubran los cinco casos; SVG con fuente editable y exportación para inspección. No rostros inventados ni números sin evidencia. No hay cuota por historia; puedes seleccionar ejemplos sin ocultar cobertura completa en tablas.
- control/: verificación de payloads, ids, huellas, tablas y figuras, con registro de exportación e inspección efectivamente realizados. No copies una inspección a cambios posteriores.

El ZIP no necesita duplicar todos los insumos: el catálogo/procedencia puede referir archivos de entrada por nombre y huella; si una ruta no está dentro del ZIP, debe decir PAQUETE_ENTRADA y no presentarse como archivo local incluido. No incluyas prompts de desarrollo de entrevistas en el repositorio de entrega. Los prompts de análisis e integración sí se conservarán en la etapa de empaquetado final.

No hay límite de diez páginas para soportes. La futura narrativa final sí tendrá máximo diez páginas de cuerpo, con portada, referencias y anexos fuera. Arquetipos, historias, metadatos y FDO se usarán en ese reporte; conceptos de Andrea, cuatro lentes, GeoInsights y dos/tres productos técnicos concretos tendrán la siguiente etapa de fundamento. No simules ejecución o conformidad para anticiparlos.

## Validación y entrega

Ejecuta validar_historias.py sobre el JSON final. Después descomprime o usa la carpeta final de soportes y ejecuta con --soportes para comprobar payloads reales:

```bash
python3 validar_historias.py . /ruta/HU01_historias_fdo_v1.json --soportes /ruta/HU01_soportes_v1 --salida /ruta/HU01_control_validacion.json
```

La carpeta pasada debe contener objetos/ y su LEEME directamente, sin añadir una raíz duplicada. El control contiene fecha, comando, huellas de resultado/script y archivos comprobados. Si cambias el JSON o los payloads, repite. Un control estructural no valida preferencia, interpretación, accesibilidad externa, adecuación de metadatos, utilidad, revisión humana o conformidad FDO. comprobacion_validador.json son pruebas técnicas, no tu resultado.

Entrega cuatro archivos completos:

- HU01_historias_fdo_v1.json.
- HU01_explicacion_v1.md.
- HU01_control_validacion.json, ejecutado con los payloads finales.
- HU01_soportes_v1.zip.

Conserva salida completa y resumen. No añadas intervenciones de entrevista ni registros de campo, consentimientos, firmas, fechas de levantamiento o aprobaciones. No publiques, registres PIDs ni contactes a terceros. JANUS se aplica como trazabilidad y revisión asistida con revisión humana independiente pendiente; no inventes concordancia, saturación o aval externo.
