# Extension fair janus · Diseño para revisión

**medidas**: - **area**: Localización e identidad
  
  **accion**: Reusar ids canónicos y referencias del paquete; conservar ruta/version/huella de entradas y derivados. Identificadores T01 locales estables, sin PID/DOI inventado.
  
  **estado**: REGISTRO_LOCAL_REAL; RESOLUCION_PERSISTENTE_PENDIENTE

- **area**: Acceso, licencia y metadatos
  
  **accion**: Separar permiso de lectura, licencia de contenido, metadatos de conocimiento y del artefacto, e identidad/custodia física. No licenciar corpus con MIT ni publicar datos por cumplir trazabilidad.
  
  **estado**: PROPUESTA_DE_DATOS; ARCHIVOS_T01_CON_METADATOS_LOCALES

- **area**: Interoperabilidad y procedencia
  
  **accion**: Diccionarios por contrato y correspondencias versionadas de entidades/tiempo/espacio. Evaluar PROV-O Entity/Activity/Agent/derivación; no imponer vocabulario a diferencias legítimas.
  
  **estado**: CONTRATOS_PROPUESTOS; RDF_NO_IMPLEMENTADO

- **area**: Reutilización y empaquetado
  
  **accion**: Tablas completas derivadas, scripts usados, registro de consulta y huellas reales permiten revisar diseño. RO-Crate requeriría descriptor, entidades y validación; DataCite y nanopublicaciones requieren selección de contenido, permisos y esquema consultado antes de implementarlos.
  
  **estado**: PAQUETE_LOCAL_REAL; RO_CRATE_DATACITE_NANOPUBLICACIONES_PROPUESTOS

- **area**: Adaptación JANUS
  
  **accion**: Conservar instrucciones de análisis/integración, archivos de entrada/salida, versiones, estrategia de consulta dirigida, decisiones y limitaciones. Registro de controles mecánicos y revisión asistida separado de revisión humana.
  
  **estado**: REGISTRO_T01_REAL; REVISION_INDEPENDIENTE_PENDIENTE

**objetos afectados**: - Necesidades/historias/códigos y metadatos de HU01/N01 reutilizados sin recodificación; no se modifica corpus.

- Diseño, productos candidatos, contratos, diagramas y salidas documentales T01.

- Datos operativos y fuentes situadas futuras, aún no recibidos ni implementados.

**controles propuestos**: - Revisar correspondencia dato→significado→unidad→fuente y permisos de cada nueva incorporación.

- Si se adopta RO-Crate/PROV/DataCite, crear archivo real y aplicar control de sintaxis/semántica y accesos antes de declarar conformidad; T01 no lo hace.

- Revisión humana independiente/adversarial de interpretaciones y criterios; no sustituir con repetición de LLM ni calcular concordancia sin codificaciones independientes.

- En repositorio final excluir prompts de desarrollo de entrevistas. Este soporte conserva solo instrucciones de tarea y registro de prompts de análisis/integración T01.

**estados pendientes**: - Revisión humana independiente, evaluación ética/contextual y aceptación.

- FAIR integral, FDO, interoperabilidad operativa, publicación, PIDs y validación de productos.

- Documentos originales JANUS y clase no redistribuidos: se aplica síntesis del expediente, sin afirmar lectura de esos originales.

**limites**: SHA-256 acredita integridad, no verdad externa. Un ZIP o JSON no acredita por sí solo FAIR/FDO o conformidad JANUS. No se publicaron, registraron PIDs ni contactaron terceros.