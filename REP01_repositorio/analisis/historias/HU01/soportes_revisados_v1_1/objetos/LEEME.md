# Objetos locales

29 necesidades N01 1.1 copiadas exactamente; 5 perfiles, 21 historias y 21 perfiles de información HU01 1.0. registro_objetos.json es copia exacta de objetos_digitales del JSON principal. Cada registro resuelve entidad a ruta_payload y huella calculada del archivo escrito. manifiesto.json inventaría todos los soportes y excluye su propia huella. No se exige que el JSON principal se hashee a sí mismo.

Uso: resolver id → ruta → bytes → SHA-256 → entidad. Entradas canónicas en paquete de insumos y JSON principal de entrega; no son datos primarios aportados por cada actor. Los objetos son prototipos sin PID/tipo/perfil externo registrado. Integridad no es calidad interpretativa.

Revisión 1.1: contexto temporal separado en los 21 perfiles y contexto espacial en dos; resolución/escala quedan desconocidas sin perder descripciones. Nueve tablas y 76 payloads, con versiones por entidad en registro.
