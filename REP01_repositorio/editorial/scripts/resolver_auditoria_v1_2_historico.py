from pathlib import Path
import json,csv,re,hashlib
R=Path('tmp/review/REP01_revision_v1_2/REP01_repositorio');E=R/'editorial/revision_v1_2'
src=json.load(open('tmp/review/auditoria_recibida/fichas_175.json'))
groups={
'G01':('LEEME.md','Se reconcilia el alcance con Canvas, la rúbrica conservada y las decisiones expresas del usuario.','No es una calificación oficial ni una verificación de entrega en Canvas.'),
'G02':('LEEME.md','Se incorporan rutas humanas, fichas y control de vínculos; se conserva trazabilidad canónica y se cotejan fuentes e inventario.','Los controles estructurales no acreditan toda interpretación semántica.'),
'G03':('portafolio_y_validacion.md','Se conservan tres candidatos, se jerarquiza el expediente y se explicitan valor público, recursos, funciones, cargas y condiciones de avance o descarte.','La pertinencia pública del cuaderno y la aceptación de mantenimiento siguen por contrastar.'),
'G04':('perfiles_y_sintesis.md','Se hacen visibles temas transversales, perfiles y contraejemplos; las historias enlazan necesidades, metadatos y operaciones. El contraste de procesos comparte tres momentos y distingue roles propuestos.','Las funciones institucionales nuevas son propuestas, sin transferencia observada entre episodios ni posturas recabadas sobre homologación.'),
'G05':('contratos_y_metadatos.md','Se desarrolla el contrato de la historia territorial con diccionario, nulos, operación, falla, incidencia y autoridad; se conservan los once contratos T01.','Son especificaciones y pruebas futuras, sin datos de producto ni implementación.'),
'G06':('LEEME.md','Se retiran hashes largos del cuerpo, se definen siglas y se comprueba la maquetación final respetando diez páginas de cuerpo.','Portada, referencias y anexos se excluyen por instrucción expresa; Word puede repaginar en otro editor.'),
'G07':('lentes_y_antecedentes.md','Se compara el aporte y límite de referentes y se añade una lectura primaria complementaria de Capybara; se preserva la procedencia del snapshot GeoInsights.','No se acredita lectura de capturas originales ausentes ni reejecución de modelos externos.'),
'G08':('fair_janus_y_controles.md','Se conserva la adaptación declarada y se distingue requisito ordinario de cobertura disponible. Citas cotejadas sobre corpus canónico.','No se fabrican audios, fechas, firmas, validación de guion o autorización documental independiente.'),
'G09':('fair_janus_y_controles.md','Se separan acceso, licencia, custodia y difusión por familia y se especifica solicitud, retirada y condiciones futuras.','No hay permisos de terceros o política institucional aceptada; la revisión actual no prueba una revisión previa al análisis.'),
'G10':('fair_janus_y_controles.md','Se reúnen controles reales, métricas con unidades, versiones y límites; la presente nota es retrospectiva y no reinicia la codificación.','Revisión humana independiente, concordancia, saturación y registros de IA ausentes permanecen pendientes o no medidos.'),
'G11':('portafolio_y_validacion.md','Se convierte la agenda en puertas con dependencia, función propuesta y evidencia de cierre; se definen tarea, respuesta, ayudas y registro para probar cada candidato.','No se ejecutó prueba de utilidad, medición de línea de base o aceptación por participantes.'),
'G12':('fair_janus_y_controles.md','Se vinculan ficha y objeto de la misma entidad, se conserva el catálogo de 76 objetos y se presenta la matriz FAIR con evidencias y pendientes.','No hay PID externo ni conformidad FDO o FAIR integral; empaquetados especializados siguen propuestos.'),
'G13':('protocolo_espacial_futuro.md','Se añade EX01 con variables, recursos candidatos, denominadores, alineación, MAUP, sensibilidad, exclusiones y condiciones de abstención, separado del corpus.','No hay datos adquiridos, cálculos o efectos territoriales comprobados; los parámetros son propuestas sujetas al insumo.'),
'G14':('lentes_y_antecedentes.md','Se incorpora matriz de 21 historias por cuatro lentes y fichas de pregunta, datos, preparación, parámetros, salida, sensibilidad y retorno a fuentes.','No se ejecutan métodos ni se imponen a historias sin pregunta y datos pertinentes.')}
specific={
1:('CONTEXTO_RECONCILIADO','La rúbrica sí está conservada en editorial/fuentes/06_canvas_rubrica_y_feedback.md; se cotejan sus cuatro criterios sin estimar nota automática.'),
2:('MEJORA_DOCUMENTAL_APLICADA','El registro de decisiones recoge conservar tres candidatos y añadir EX01; esta resolución conserva origen, acción y destino de cada recomendación.'),
11:('SOPORTE_PREEXISTENTE_Y_MEJORA','El paquete completo contiene corpus, objetos, mapas, snapshot y controles; se añade índice humano de la revisión.'),
12:('CONTROL_LITERAL','Se cotejan las siete citas del manuscrito contra párrafos canónicos; el control no valida una observación externa.'),
17:('SOPORTE_PREEXISTENTE_Y_MEJORA','El registro de corpus conserva cinco sesiones y metadatos disponibles. Se enlaza la distinción ordinario/adaptado.'),
18:('MEJORA_DOCUMENTAL_APLICADA','Se mantiene cobertura de cinco funciones y dos voces no especializadas. Captura SSC y postura ADIP no están cubiertas por entrevista, por decisión de alcance.'),
19:('MEJORA_DOCUMENTAL_APLICADA','Se conservan en cuerpo las inducciones observables E05-P153 y E01-P070–P073, y el contexto de elicitación por historia en las fichas.'),
20:('SOPORTE_PREEXISTENTE_Y_MEJORA','Se reúnen cinco mapas existentes y sus límites de inicio/cierre; no se genera una cadena entre las cinco entrevistas.'),
21:('SOPORTE_PREEXISTENTE_Y_MEJORA','Se conservan seis historias ideales y se identifica su elicitación. No se reducen a una afirmación espontánea de carencia.'),
23:('PARCIAL_CON_PENDIENTE_REAL','Se revisa el alcance de acceso y se especifica retirada; el escaneo técnico actual no acredita revisión humana ni desidentificación histórica.'),
24:('SOPORTE_PREEXISTENTE_Y_MEJORA','Se conservan 916 párrafos canónicos con voces y localizadores; el validador coteja segmentos y offsets sin alterar textos.'),
25:('PARCIAL_CON_PENDIENTE_REAL','Se entregan prompts y salidas conservados; no se reconstruyen conversaciones completas ausentes ni parámetros desconocidos.'),
26:('PARCIAL_CON_PENDIENTE_REAL','Se conservan los prompts históricos como procedencia; no se sustituyen por instrucciones actuales fingiendo que guiaron el análisis anterior.'),
27:('PROPUESTA_NO_EJECUTADA','Se separan funciones de custodia, revisión y aprobación; nombres, unidades y aceptación requieren acuerdo real.'),
28:('PARCIAL_CON_PENDIENTE_REAL','La nota de esta revisión es retrospectiva y no acredita limpieza o permiso anterior a la codificación.'),
29:('MEJORA_DOCUMENTAL_APLICADA','El cuerpo explicita estrategia híbrida y unidad de fragmento; las preguntas se usan como contexto, sin contarlas como respuestas.'),
30:('SOPORTE_PREEXISTENTE_Y_MEJORA','El libro 1.3 mantiene 64 códigos, 123 ejemplos, reglas y fronteras; no se agrega un catálogo alternativo.'),
31:('PARCIAL_CON_PENDIENTE_REAL','Se conservan los campos reales de segmentos y revisión; no se inventa confianza cuantitativa o identidad de codificador humano.'),
32:('CONTROL_LITERAL','Se comprueba texto[inicio:fin] con convención Python de inicio inclusivo y fin exclusivo sobre el párrafo canónico.'),
34:('PARCIAL_CON_PENDIENTE_REAL','Revisión humana no realizada: se especifican tarea, función y evidencia futura de cierre, conservando el pendiente.'),
35:('MEJORA_DOCUMENTAL_APLICADA','El cuerpo muestra S01-T001 y S01-T006 con hallazgos H001/H016/H018/H019 y códigos, variantes y contraejemplos reales.'),
37:('SOPORTE_PREEXISTENTE_Y_MEJORA','Se conservan memos analíticos y se añade nota reflexiva retrospectiva en la revisión editorial actual, sin atribuirla a otro momento.'),
38:('PARCIAL_CON_PENDIENTE_REAL','La auditoría externa y esta revisión son asistidas; dos revisores humanos complementarios no están acreditados.'),
39:('NO_APLICA_CALCULO_NO_REALIZADO','No se calculó acuerdo; no se añaden kappa, alpha ni umbral ficticio. La confiabilidad entre personas sigue sin medirse.'),
40:('SOPORTE_PREEXISTENTE_Y_MEJORA','Se conserva la matriz de afirmaciones y se añaden nuevas afirmaciones editoriales con su fuente y naturaleza; las propuestas no se presentan como hallazgos.'),
41:('PARCIAL_CON_PENDIENTE_REAL','Registros reales conservados; modelo exacto y parámetros no verificables permanecen nulos.'),
43:('CONTROL_EJECUTADO','Los resultados y fallas del validador actual se entregan con su alcance. No equivalen a haber ejecutado JANUS completo.'),
44:('MEJORA_DOCUMENTAL_APLICADA','Se conserva la 1.1, la auditoría recibida y scripts de esta revisión; cambios e impacto editorial se documentan sin reescribir análisis.'),
47:('PARCIAL_CON_PENDIENTE_REAL','Los 46 actores se conservan; se indican funciones institucionales y ausencias. No se inventan unidades pertinentes sin fuente o interlocución real.'),
48:('PROPUESTA_NO_EJECUTADA','El recorrido institucional separa SSC, coordinación ADIP, desarrollo, consulta y autoridad de cambio; la desagregación competente requiere documentación.'),
51:('MEJORA_DOCUMENTAL_APLICADA','Cinco fichas funcionales completas en soporte; dos perfiles desarrollados en el cuerpo, incluidas capacidades, confianza situada y límites.'),
52:('MEJORA_DOCUMENTAL_APLICADA','Se separan IDs de voz E, actor ACT01, perfil HU01-P e historia HU01-H; no se inventan personas adicionales para aparentar síntesis.'),
53:('PROPUESTA_NO_EJECUTADA','Se preserva el recorrido E01 y se añade mapa propuesto por funciones con origen SSC desconocido, sin afirmar una transferencia institucional observada.'),
54:('SOPORTE_PREEXISTENTE_Y_MEJORA','Se preservan los cinco diagramas SVG/DOT ya existentes y se aporta matriz de inicio, soportes y cierre por perfil.'),
55:('CONSERVADO','Se mantienen leyendas de relato, documento y propuesta, y la procedencia académica del corpus.'),
58:('PROPUESTA_NO_EJECUTADA','Se define secuencia propuesta-consulta-autorización-incorporación y el requisito de competencia acreditada antes de cambiar la fuente.'),
61:('SOPORTE_PREEXISTENTE_Y_MEJORA','Los 29 enunciados y observables N01 se conservan; no se cambia su estado de suficiencia o prioridad para fabricar demanda.'),
65:('MEJORA_DOCUMENTAL_APLICADA','Se incluyen literalmente las formulaciones completas HU01-H003 y HU01-H006 en el cuerpo; las 21 fichas están enlazadas.'),
67:('MEJORA_DOCUMENTAL_APLICADA','La historia territorial reúne contexto, perfil, necesidad, metadatos, operación, restricción, criterio y decisión; las demás conservan su ficha fuente.'),
71:('CONTROL_Y_MEJORA','La cadena exacta usa E01-P125/R01-S093, C016/C017, S01-T006/H016 y HU01-H003; E01-P137 aporta prioridad y C016, sin atribuir C004 a ese párrafo.'),
79:('CONTROL_Y_MEJORA','Ficha humana y objeto HU01-H003 comparten contenido y versión; el control coteja los 76 payloads y sus huellas.'),
80:('PROPUESTA_NO_EJECUTADA','Se especifica manifiesto futuro separando dato, metadato, método, configuración y vista; no se presenta una ejecución inexistente.'),
90:('PROPUESTA_NO_EJECUTADA','Comparar capas exige entidad, periodo y autoridad compatibles y una operación común; igual resultado no acredita identidad jurídica.'),
103:('NO_APLICA_TERMINO_NO_UTILIZADO','No se promete gemelo digital ni vínculo continuo con un sistema real; escenarios permanecen escenarios.'),
106:('PROPUESTA_NO_EJECUTADA','Por decisión nueva del usuario se incorpora EX01 vegetación/equipamientos con pregunta, datos necesarios, variables y pruebas de robustez, sin atribución al corpus.'),
108:('SOPORTE_PREEXISTENTE_Y_MEJORA','Se coteja snapshot archivado y su procedencia; la falla de acceso remoto del auditor no se interpreta como ausencia de commit.'),
123:('SOPORTE_PREEXISTENTE_Y_MEJORA','Se hace visible la matriz de los 15 principios FAIR de HU01 y se preservan pendientes por principio y objeto.'),
124:('PARCIAL_CON_PENDIENTE_REAL','Catálogo y versiones locales sí existen; resolución persistente y registro externo permanecen pendientes.'),
125:('PARCIAL_CON_PENDIENTE_REAL','Se separa acceso académico de publicación y se propone solicitud/retirada; permisos y canal institucional requieren acuerdo real.'),
127:('PARCIAL_CON_PENDIENTE_REAL','Se conserva MIT del snapshot y se distinguen licencias de corpus, fuentes, figuras y salidas, dejando derechos desconocidos sin licencia inventada.'),
129:('PARCIAL_CON_PENDIENTE_REAL','RO-Crate, PROV-O, DataCite y nanopublicaciones no se declaran implementados; se conserva su evaluación futura.'),
131:('NO_APLICA_CONDICIONAL','No se identifica condición que active CARE; se documenta activación futura si ingresa conocimiento con gobernanza pertinente.'),
135:('CONSERVADO','Los materiales de Emilio permanecen antecedente; no se transfieren entrevistas, cifras o resultados al corpus propio.'),
140:('MEJORA_DOCUMENTAL_APLICADA','Se explicita aportación individual para discusión del equipo sin afirmar una integración conjunta no documentada.'),
141:('ADAPTACION_DECLARADA','Cinco voces y tipos funcionales están presentes; la excepción comunicada no se convierte en cinco entrevistas de campo verificadas.'),
142:('CONTROL_LITERAL_CON_ADAPTACION','Citas cotejadas contra corpus canónico; audio no aportado sigue sujeto a adaptación, sin verificación acústica ficticia.'),
144:('PARCIAL_CON_PENDIENTE_REAL','Se añaden hipótesis de incentivos institucionales; la posición frente a homologación sigue NO_RECABADA para los actores.'),
145:('CONTEXTO_CORREGIDO','El usuario excluyó portada y referencias del máximo; se verifica cuerpo ≤10 páginas del PDF. No corresponde eliminar portada para aplicar un criterio distinto.'),
148:('CONTEXTO_CORREGIDO','Los descriptores Destacado están conservados en el expediente; se contrastan sus cuatro criterios sin atribuir una nota oficial.'),
150:('CONSERVADO','Se mantiene procedencia de generación por IA y alcance académico, sin convertir diálogos en constatación empírica.'),
151:('ADAPTACION_DECLARADA','No se fabrican audios, consentimiento firmado o autorización independiente. La excepción se atribuye a comunicación del estudiante.'),
152:('CONSERVADO','Declaración incluye generación, codificación, síntesis y escritura y conserva parámetros y revisión humana pendientes.'),
153:('MEJORA_DOCUMENTAL_APLICADA','Se incorpora cuadro ordinario/adaptado en el soporte metodológico, enlazado desde la declaración y la revisión.'),
154:('PARCIAL_ANTECEDENTE_COMPLEMENTARIO','Se añade aprendizaje primario de un reporte Capybara accesible, identificado como complemento; el ejemplo exacto de capturas de clase no se declara recuperado.'),
166:('PROCEDIMIENTO_DE_AUDITORIA','Se conserva inventario del auditor y se amplía con soportes reales; no es una exigencia temática adicional del reporte.'),
167:('PROCEDIMIENTO_DE_AUDITORIA','Se preservan los 175 IDs y se registra resolución por fila, sin convertir recuentos de estados en porcentaje de nota.'),
168:('PROCEDIMIENTO_DE_AUDITORIA','Los destinos de corrección se localizan por sección y archivo; páginas efectivas se obtienen del render final.'),
169:('PROCEDIMIENTO_DE_AUDITORIA','Se preserva prioridad del auditor y se distingue acción editorial de pendiente empírico o institucional.'),
170:('CONTROL_Y_MEJORA','Los soportes faltantes al auditor ahora se incluyen y se cotejan; conformidad integral JANUS/FAIR sigue sin acreditarse.'),
171:('CONTROL_Y_MEJORA','Se comprueba cadena territorial desde segmento y tema hasta historia, contrato y producto, con origen institucional desconocido explicitado.'),
172:('CONSERVADO','No se crean citas, entrevistas, consensos, permisos o resultados territoriales. Corpus y codificación permanecen inmutables.'),
173:('CONTEXTO_CORREGIDO','Se usa la rúbrica conservada; no se estima nivel por una suma mecánica de las 175 fichas.'),
174:('CONTROL_EJECUTADO','Se repiten conteo de páginas, citas, versiones, enlaces, objetos e integridad sobre los artefactos 1.2 finales.'),
175:('MEJORA_DOCUMENTAL_APLICADA','La versión 1.2 y sus controles aportan evidencia de aplicación; los pendientes que requieren personas, datos o decisiones externas se mantienen abiertos.')}
rows=[]
for a in src:
 n=int(a['id'][1:]);g=re.search(r'G\d\d',a['Estado']).group();dest,action,limit=groups[g]
 state='MEJORA_DOCUMENTAL_APLICADA'
 if 'No verificable' in a['Estado']:state='SOPORTE_PREEXISTENTE_Y_MEJORA'
 if g in ['G13','G14']:state='ESPECIFICACION_FUTURA_NO_EJECUTADA'
 if 'Cumple   ' in a['Estado']:state='CONSERVADO'
 if n in specific:state,action=specific[n]
 rows.append({'id':a['id'],'titulo':a['titulo'],'estado_auditor':a['Estado'],'diagnostico_auditor':a['Diagnóstico y brecha'],'accion_solicitada':a['Acción'],'resolucion_v1_2':state,'accion_y_razon':action,'soporte':dest,'limite_y_pendiente':limit})
with (E/'resolucion_175.csv').open('w',newline='',encoding='utf-8-sig')as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(E/'resolucion_175.json').write_text(json.dumps({'version':'1.2','naturaleza':'Resolución editorial asistida, no nueva auditoría humana o calificación','filas':rows},ensure_ascii=False,indent=2)+'\n')
out=['# Resolución de las ciento setenta y cinco recomendaciones','Cada registro conserva el diagnóstico del auditor y nuestra acción con un destino comprobable. «Aplicada» se refiere a una mejora documental; no equivale a cumplimiento total del requisito ni validación de campo. Las especificaciones futuras y limitaciones reales siguen identificadas. Los destinos se leen junto al reporte 1.2. La matriz de 208 requisitos previa permanece como control histórico 1.1; esta tabla registra las recomendaciones de la auditoría recibida, sin mezclarlas.']
for a in rows:out+=['## '+a['id']+' '+a['titulo'],'**Diagnóstico recibido:** '+a['diagnostico_auditor'],'**Acción solicitada:** '+a['accion_solicitada'],'**Tratamiento 1.2:** '+a['resolucion_v1_2']+'. '+a['accion_y_razon'],f"**Destino:** [{a['soporte']}]({a['soporte']}).",'**Límite:** '+a['limite_y_pendiente']]
(E/'resolucion_175.md').write_text('\n\n'.join(out)+'\n')
print('Recomendaciones registradas',len(rows))
