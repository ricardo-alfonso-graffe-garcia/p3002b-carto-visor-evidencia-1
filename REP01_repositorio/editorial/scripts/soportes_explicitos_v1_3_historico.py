from pathlib import Path
import json,csv,hashlib,shutil,re
W=Path('tmp/review/REP01_revision_v1_3');R=W/'REP01_repositorio';E=R/'editorial/revision_v1_3'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
hu=json.loads((R/'88_historias_y_objetos_v1_1.json').read_text());ob=next(x for x in hu['objetos_digitales']if x['entidad']=='HU01-H003');need=next(x for x in hu['objetos_digitales']if x['entidad']=='N01-N004')
save(E/'ejemplo_objeto_local_orientado_a_fdo.json',{'naturaleza':'VISTA_EDITORIAL_DE_PROTOTIPO_LOCAL_NO_REGISTRADO','estado':'SIN_PID_O_TIPO_Y_PERFIL_EXTERNOS_REGISTRADOS','registro_original':ob,'necesidad_relacionada':need,'fuente_registro':'88_historias_y_objetos_v1_1.json / objetos_digitales','interpretacion':'Se muestra un registro existente, sin alterar su contenido. Esta vista no es un FDO registrado ni introduce una nueva historia, versión de payload, entidad empírica o permiso.','huella_payload_verificada':hashlib.sha256((R/'analisis/historias/HU01/soportes_revisados_v1_1'/ob['ruta_payload']).read_bytes()).hexdigest()==ob['sha256']})
(E/'fair_fdo_y_janus.md').write_text('''# FAIR FDO y JANUS en la versión 1.3

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

El origen académico del corpus y la adaptación se mantienen declarados. La generación de entrevistas por excepción comunicada no se presenta como práctica de generación de evidencia autorizada por JANUS. Son condiciones distintas del ejercicio.
''')
gaps=[
('Historias explícitas','R065/R067','Sí: dos formulaciones completas y 21 en soporte.','CONSERVADO','Sección 5','No están las 21 fichas extensas dentro del cuerpo; no es necesario duplicarlas.'),
('Cadena de trazabilidad','R005/R040/R071','Sí: una cadena detallada en el cuerpo.','CONSERVADO','Sección 5','La comprobación asistida no acredita validación humana de toda interpretación.'),
('Esquema integrador','Figura 1 de especificaciones; R005/R014','Ausente del cuerpo; arquitectura de producto no era equivalente.','INCORPORADO','Figura 1, sección 2','La validación de productos se marca futura; no se representa como realizada.'),
('Mapa gráfico de actores','R047/R048/R050','Análisis y tabla en cuerpo; redes gráficas sólo en soportes.','INCORPORADO_SUBRED','Figura 3, sección 4','Se muestra la subred E01; redes completas y actores documentales siguen en soportes, sin fingir una cadena entre cinco casos.'),
('Mapa de procesos','R053/R054/R056/R143','Un diagrama E01, tabla de cinco procesos y contraste de tres momentos.','CONSERVADO','Figura 2, sección 3','Cinco mapas completos y cuatro modelos documentales permanecen en soporte.'),
('Explicación metodológica JANUS','R029/R038/R129','Declarado, pero explicado principalmente como alcance y límite.','AMPLIADO','Sección 2 y cierre de sección 9','No se afirma aplicación integral ni controles humanos no realizados.'),
('Principios FAIR','R123/R124/R126','Mencionados con límites; aplicación por dimensión principalmente en soporte.','EXPLICITADO_POR_DIMENSION','Sección 9','No hay conformidad completa, PID o acuerdos de derechos por nombrar los principios.'),
('Representación local orientada a FDO','R079/R128/R130','76 objetos en soporte; sigla FDO ausente del PDF.','EXPLICITADO_CON_EJEMPLO','Sección 5, HU01-OD037','No se crea un FDO plenamente registrado; identidad persistente, tipo y perfil externos siguen pendientes.'),
('Procesos institucionales aplicables','R053/R137/R143','Sin fuente formal directamente atribuible a los cinco episodios.','PENDIENTE_REAL','Secciones 3 y 6; D01','No hay divergencias institucionales demostradas; explicar diferencias de ámbito no equivale a documentar incumplimientos.'),
('Posición frente a homologación','R144/R147','NO_RECABADA para los 46 actores; hipótesis de incentivos separadas.','PENDIENTE_REAL','Sección 4; ACT01','No puede cerrarse mediante redacción ni inferir apoyo por preferir notas claras.'),
('Revisión humana independiente','R034/R038','Pendiente, con revisión asistida conservada.','PENDIENTE_REAL','Método y declaración','No se atribuyen dos revisores humanos a esta actividad.'),
('Concordancia y saturación','R039/R046','No medidas.','NO_REALIZADO_DECLARADO','Método y declaración','Recuentos de fragmentos no son medidas de acuerdo; no se inventa un índice.'),
('Privacidad antes de codificar','R023/R028','Escaneo técnico posterior documentado.','LIMITE_HISTORICO','Soportes metodológicos','Una comprobación actual no prueba haber aplicado una puerta histórica de JANUS antes del análisis.'),
('Registros completos de IA','R025/R026/R041','Se conservan prompts y salidas disponibles, sin exportación completa o parámetros exactos.','LIMITE_DOCUMENTAL','Declaración y registro','No se reconstruyen metadatos inexistentes ni se cambia el origen de los registros.'),
('Empaquetado semántico','R129','RO-Crate, PROV-O, DataCite y nanopublicaciones no implementados.','PENDIENTE_IMPLEMENTACION','Sección 9; HU01','El ZIP propio y relaciones locales no equivalen a esa pila tecnológica.'),
('Pruebas de productos','R060/R068/R161/R162/R164','Protocolos y puertas definidos, sin ejecución con participantes.','PROPUESTO_NO_EJECUTADO','Secciones 8 y 9','No hay resultado de utilidad, ahorro, línea de base o aceptación comprobados.'),
('Análisis espacial y cuatro lentes','R083–R122/R163','EX01 y fichas de métodos como propuestas.','FASE_POSTERIOR','Sección 7 y T01','No se adquirieron datos ni ejecutaron cruces, escaneos, ajustes, TDA o agentes.'),
('Ejemplo exacto Capybara de clase','R154/R157','Se incorporó un antecedente complementario accesible.','PARCIAL_CON_LIMITE','Sección 8 y referencias','No se afirma recuperar la captura o corrida exacta de clase.'),
('Audio fechas guion y consentimiento','R141/R142/R151/R153','Adaptación declarada según excepción comunicada.','ADAPTACION','Sección 1 y anexo','No se crean audios, fechas, firmas ni validación de guion no acreditados.'),
('Extensión y rúbrica','R145/R148/R173','La auditoría no recibió rúbrica y contó portada/referencias.','CONTEXTO_CORREGIDO','Control de páginas y fuente de rúbrica','El máximo aplicable aquí es diez páginas de cuerpo; no se garantiza calificación.')]
with(E/'brechas_y_presencia.csv').open('w',newline='',encoding='utf-8-sig')as f:
 wr=csv.writer(f);wr.writerow(['aspecto','requisitos','estado_1_2','tratamiento_1_3','destino','limite']);wr.writerows(gaps)
save(E/'brechas_y_presencia.json',{'version':'1.3','alcance':'Contraste de presencia y límites materiales, sin recalificar automáticamente los 175 requisitos compuestos.','hallazgos':[dict(zip(['aspecto','requisitos','estado_1_2','tratamiento_1_3','destino','limite'],x))for x in gaps]})
out=['# Presencia explícita y brechas restantes del reporte','Se compararon el reporte 1.2 y los archivos de auditoría y especificaciones nuevamente adjuntos. Sus SHA-256 coinciden exactamente con las copias previamente leídas; no son instrucciones nuevas. Esta revisión corrige las brechas visibles señaladas por el usuario y conserva el contenido analítico.','La matriz de 175 tratamientos de la revisión anterior no era una certificación de cumplimiento completo. Tener un soporte y mencionarlo en prosa no equivale a incluir un gráfico o explicar un objeto en el cuerpo. Estas distinciones se hacen explícitas aquí.']
for title,req,old,state,dest,lim in gaps:out+=['## '+title,f'**Fuente:** {req}. **Antes:** {old}',f'**Ahora:** {state}. **Destino:** {dest}.',f'**Límite:** {lim}']
(E/'contraste_especificaciones_y_auditoria.md').write_text('\n\n'.join(out)+'\n')
(E/'LEEME.md').write_text('''# Revisión de presencia explícita 1.3

Se añade el esquema integrador solicitado como figura 1, un mapa gráfico de actores E01 como figura 3, una explicación breve de JANUS en método, aplicación de las cuatro dimensiones FAIR en el cierre y un objeto local orientado a FDO como ejemplo en sección 5. El mapa de procesos pasa a figura 2. La arquitectura de producto permanece completa en soporte; es distinta del esquema de construcción del reporte.

Corpus, libro de códigos, recodificaciones y catálogos no cambian. No se registra un PID, se publica un corpus o se implementa retroactivamente JANUS integral. Los 76 objetos locales ya existían; esta revisión hace visible uno y explica qué le falta para una implementación FDO completa.

- [Contraste y brechas restantes](contraste_especificaciones_y_auditoria.md)
- [Tabla CSV](brechas_y_presencia.csv)
- [FAIR FDO y JANUS con ejemplo real](fair_fdo_y_janus.md)
- [Vista del objeto local](ejemplo_objeto_local_orientado_a_fdo.json)
- [Esquema vectorial del desarrollo](relacion_evidencia_diseno.svg)
- [Mapa vectorial de actores](mapa_actores_territorial.svg)

La revisión sigue siendo asistida; los pendientes de autoridad, posturas institucionales, derechos, validación humana y pruebas no se cierran por edición. Los controles de esta versión identifican el PDF y el cuerpo efectivamente maquetados.
''')
# La resolución anterior se preserva; se añade relación delta sin falsear que todo estaba en el cuerpo.
rows=json.loads((R/'editorial/revision_v1_2/resolucion_175.json').read_text())['filas']
changes={14:'Se incorpora esquema de construcción y mapa de actores al cuerpo.',50:'La red E01 ahora se muestra como figura 3; resto de redes en soportes.',71:'La cadena se conserva explícita y el esquema general la sitúa en el proceso.',79:'El registro HU01-OD037 queda explicado y enlazado desde el cuerpo.',123:'El cuerpo explica las cuatro dimensiones y sus límites.',128:'La sigla y la preparación hacia FDO son explícitas con un objeto existente; no registro pleno.',129:'Método JANUS explicado y tecnologías no implementadas nombradas como pendientes.'}
save(E/'delta_sobre_175_recomendaciones.json',{'version':'1.3','base':'editorial/revision_v1_2/resolucion_175.json','alcance':'Preservación de 175 IDs con precisiones de visibilidad; no prueba de conformidad integral.','filas':[{'id':x['id'],'titulo':x['titulo'],'tratamiento_previo':x['resolucion_v1_2'],'precision_1_3':changes.get(int(x['id'][1:]),'Se conserva el tratamiento previo y sus límites; véase contraste de brechas materiales.')}for x in rows]})
print('Soportes de presencia y brechas preparados')
