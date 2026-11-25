from pathlib import Path
import json,re,hashlib,datetime
R=Path(__file__).resolve().parent;B=R/'trabajo/REP01_insumos_v1';O=R/'entrega';P=O/'REP01_repositorio'
def rd(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
S={'C':'55_libro_comun_v1_3.json','S':'63_sintesis_transversal_v1_1.json','P':'67_procesos_descritos_v1_1.json','D':'72_contraste_documental_v1_1.json','A':'76_actores_y_preferencias_v1_1.json','N':'82_necesidades_v1_1.json','H':'88_historias_y_objetos_v1_1.json','T':'93_diseno_y_fundamentos_v1_1.json'}
d={k:rd(P/v)for k,v in S.items()}
reg=rd(B/'registro_entradas.json');md=(O/'REP01_reporte_v1.md').read_text()
canon={}
for f in (P/'analisis/insumos').glob('E0*_corpus_analisis_v1.json'):canon.update({x['id']:x for x in rd(f)['parrafos']})
sections=[]
functions=[
'Formular la pregunta y tesis; delimitar muestra y naturaleza del corpus.',
'Explicar instrumentos, elicitación y recorrido real de análisis mediante un ejemplo.',
'Comparar cinco procesos completos y separar reconstrucción y modelo documental.',
'Relacionar capacidades, interés, preferencias y condiciones de coordinación por ámbito.',
'Discutir estados de necesidades y desarrollar cadenas y contraejemplos de diseño.',
'Contrastar diagnóstico, hipótesis y supuestos del encargo con sus dependencias.',
'Fundamentar consecuencias de representación y descartar aplicación prematura de lentes.',
'Articular arquitectura propuesta y tres candidatos con comprobaciones futuras.',
'Concluir el argumento y priorizar verificación, auditabilidad y maquetación.']
support=[
['24_registro_corpus.json',S['S'],S['D']],
['11_guion_base_y_adaptaciones.md','24_protocolo_analisis.md',S['C'],'analisis/recodificacion/LEEME.md'],
[S['P'],S['D'],'analisis/procesos/P01/figuras_revisadas_v1_1/LEEME.md','editorial/figuras/REP01-F001.svg'],
[S['A'],'76_actores_y_preferencias_v1_1.md'],
[S['N'],S['H'],'editorial/figuras/REP01-F002.svg'],
[S['D'],S['S'],S['N'],'editorial/registros/agenda_pendientes.md'],
[S['T'],'analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/fundamentos_criticos.md','analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/lentes.md'],
[S['T'],'analisis/diseno/T01/soportes_revisados_v1_1/esquemas/contratos_propuestos.json','analisis/referencias/GeoInsights/README.md','editorial/figuras/REP01-F003.svg'],
[S['H'],'editorial/fuentes/fuente_metodo_JANUS.json','editorial/registros/agenda_pendientes.md']]
pages=[0.55,1.05,1.40,0.80,1.65,0.55,1.15,1.10,0.65]
chunks=re.split(r'<a id="rep01-s\d{3}"></a>',md.split('<!-- CUERPO_INICIO -->')[1].split('<!-- CUERPO_FIN -->')[0])[1:]
for i,c in enumerate(chunks):
 title=re.search(r'## (.+)',c).group(1)
 sections.append({'id':f'REP01-S{i+1:03}','titulo':title,'ancla':f'rep01-s{i+1:03}','funcion_argumental':functions[i],'palabras_estimadas':len(re.findall(r'\b[\wÁÉÍÓÚÑáéíóúñ]+\b',c)),'paginas_estimadas':pages[i],'soportes':support[i],'nota_estimacion':'Palabras calculadas con patrón del validador; páginas son presupuesto, no medida de PDF.'})

quotespec=[
('E01-P065','Conservé el identificador y la ubicación del espacio.',2,['E01-P064'],'Ilustrar conservación deliberada con C004.','Fragmento del cambio en una copia; no propagación a todas las bases.'),
('E03-P182','Con una nota clara, el calendario y mensajes directos nos entendemos.',4,['E03-P181'],'Mostrar suficiencia de soportes actuales frente a posible nueva carga.','No oposición expresada a homologación; respuesta sobre una serie pequeña.'),
('E02-P083','La suficiencia dependía de la afirmación, no era una propiedad de todo el material de una vez.',5,['E02-P080'],'Distinguir descripción sustentable de explicaciones más amplias.','Continuación de P081/P082; no prueba externa de los episodios relatados.'),
('E01-P137','La explicación del último cambio que afecta la identificación del lugar.',5,['E01-P136'],'Prioridad ideal que origina cadena N004/H003.','Ejercicio ideal solicitado; no falla del episodio atendido.'),
('E02-P148','O explicar menos, pero mejor.',5,['E02-P147','E02-P144'],'Ilustrar utilidad de acotar una afirmación en cadena N009/H006.','Matiza recapitulación del entrevistador; no aceptación de un producto.'),
('E04-P152','Pero para la suavidad preferiría tener el pedazo en la mano.',5,['E04-P150'],'Explicar materialidad que limita un soporte digital.','Continuación del cuaderno ideal; no prueba cosida o lavada aportada.'),
('E05-P119','No saber qué libro iba a encontrar era parte de las ganas de ir.',5,['E05-P118'],'Conservar indeterminación valiosa en la salida personal.','Se refiere a esta salida; no preferencia general de población.')]
citas=[]
for i,(pid,q,s,ctx,use,lim) in enumerate(quotespec,1):
 assert q in canon[pid]['texto'] and q in md
 e=pid[:3]
 citas.append({'id':f'REP01-Q{i:03}','entrevista':e,'parrafo':pid,'voz':'Participante','cita':q,'seccion':f'REP01-S{s:03}','uso':use,'ruta_fuente':f'corpus/{e}/{e}_texto_con_localizadores.txt','contexto_pregunta':ctx,'limite':lim})

# Registro de lectura: no confundir resultados heredados, inspección dirigida e integridad.
lecturas=[]
def lectura(file,scope,check):lecturas.append({'archivo':file,'alcance':scope,'comprobacion':check})
lectura('95_instrucciones_REP01(1).md','Lectura íntegra de instrucciones externas; continuación y cierre consultados sin truncamiento.','Delimitadores, entregables y alcance aplicados; copia en editorial/fuentes/instrucciones_REP01.md.')
lectura('manifest.json','Cotejo de las 495 entradas por bytes y SHA-256; lectura de estructura y alcance.','495 coincidencias; editorial/controles/integridad_insumos.json. No equivale a lectura semántica.')
lectura('catalogo_base.json','Consulta estructural de 446 registros y tratamientos; procedencia de base curada.','439 copias idénticas y 7 adaptaciones de rutas históricas; conservado en editorial/fuentes.')
lectura('registro_entradas.json','Lectura completa del registro de versiones y fuentes inmutables.','Versiones preferidas preservadas y cotejadas por control.')
lectura('requisitos/06_canvas_rubrica_y_feedback.md','Lectura íntegra de transcripción operativa de Canvas, rúbrica y ocho puntos de feedback.','No consulta directa a Canvas; contenido usado en cobertura.')
lectura('requisitos/02_matriz_requisitos.json','Lectura de los 208 enunciados y sus comprobaciones, con categorías y metadatos de origen consultados.','Cobertura uno a uno; no se reutilizan como estados de ejecución los pendientes de especificación.')
lectura('requisitos/01_expediente_maestro_extracto.md','Lectura de encuadre, decisiones, apertura, instrumentos y formulaciones metodológicas/técnicas pertinentes.','Consulta dirigida; no se incorporan registros de otras conversaciones enlazadas.')
lectura('11_guiones_entrevistas.json','Guion base completo y adaptaciones consultadas junto a intervenciones efectivas de las cinco entrevistas.','Estado histórico aplicación pendiente registrado como incidencia, sin certificar aplicación humana.')
lectura('24_protocolo_analisis.md','Lectura íntegra de protocolo, cierre, secuencia y actualización HU01/T01.','Secuencia asistida y revisión humana pendiente diferenciadas.')
lectura('24_registro_corpus.json','Lectura completa de cinco registros.','Fechas NO_CONSIGNADA y encabezados conservados.')
for e in range(1,6):
 ee=f'E0{e}';lectura(f'corpus/{ee}/{ee}_texto_con_localizadores.txt','Lectura completa de entrevista, preguntas, continuaciones, correcciones y cierre; regreso a citas seleccionadas.','Cotejo de citas/voz/offsets contra JSON analisis/insumos; sin certificar hechos externos.')
lectura(S['C'],'Lectura de los 64 nombres, definiciones y fronteras de inclusión/exclusión; reglas y fronteras; ejemplos relacionados con pasajes del corpus.','123 ejemplos cotejados programáticamente; no se declara nuevo pilotaje humano.')
for i,v in enumerate(['1_3','1_3','1_2','1_1','1_1'],1):
 f=f'analisis/recodificacion/R0{i}/R0{i}_resultado_revisado_v{v}.json'
 lectura(f,'Consulta de metadatos, balance, memos/incidencias y segmentos pertinentes a ejemplos. Todos los segmentos/códigos/estatus se recorren para controles, sin afirmar nueva recodificación semántica integral.','Versiones heterogéneas conservadas; citas/offsets/cobertura revisados mediante controles complementarios.')
for k,scope in {
'S':'Todos los enunciados de 22 hallazgos, temas, decisiones y límites; evidencias seleccionadas contrastadas con las entrevistas completas.',
'P':'Los cinco procesos y todos sus nodos de inicio/decisión/cierre, soportes y agrupaciones; correspondencia dirigida con relaciones y preguntas originales.',
'D':'Los 21 registros de fuente y alcance, cuatro modelos, 13 contrastes, 22 afirmaciones del encargo y diez pendientes. Originales externos no se declaran todos leídos nuevamente.',
'A':'Los 46 actores, procedencia funcional, 12 ámbitos, capacidades/preferencias y tres hipótesis con condiciones y contraargumentos.',
'N':'Los 29 enunciados, estados, información actual y deseada, criterios de prioridad y vínculos; consulta dirigida de evidencias de las cadenas.',
'H':'Las 21 historias y su cobertura de 29 necesidades; criterios/metadatos/operaciones de cadenas y perfil local FAIR; objetos recorridos para control.',
'T':'Fundamentos, ocho alternativas, cuatro prácticas, lentes/herramientas y productos; arquitectura, contratos y representaciones consultados con sus límites.'}.items():lectura(S[k],scope,'Versión 1.1 preferida; se distingue lectura de contenidos y cotejo automatizado.')
for fn in ['fundamentos_criticos.md','practicas_diseno.md','seleccion_portafolio.md','lentes.md','herramientas.md']:
 lectura('analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/'+fn,'Lectura íntegra del desarrollo temático.','Usado como soporte de síntesis técnica; no ejecución de las propuestas.')
lectura('analisis/referencias/GeoInsights/README.md','Lectura completa; procedencia y licencia consultadas.','Snapshot y commit preservados; no pipeline ejecutado.')
dump(P/'editorial/registros/lectura_efectiva.json',lecturas)

# Afirmaciones centrales con objetos fuente definidos, sin convertir elaboraciones en literales.
af=[]
def claim(sec,text,kind,ids,key,loc,lim):
 af.append({'id':f'REP01-A{len(af)+1:03}','seccion':f'REP01-S{sec:03}','enunciado':text,'tipo':kind,'objetos_fuente':ids,'soporte':S.get(key,key),'localizador':loc,'limite':lim})
claim(1,'La utilidad de organizar información depende de recuperar significado y respaldo para decisiones situadas.','INTERPRETACION',['S01-H001','S01-H016','S01-H019'],'S','hallazgos H001/H016/H019','Tesis de este manuscrito; no necesidad institucional representativa.')
claim(1,'Las transcripciones fueron generadas con IA para el ejercicio; no se acreditan grabaciones ni trabajo de campo.','DOCUMENTAL',['E01-P004','E01-P005','MET-JANUS'],'editorial/fuentes/instrucciones_REP01.md','Qué debe lograr el manuscrito: declaración de generación y registros disponibles','La instrucción fija declaración; frases del corpus no acreditan registros externos.')
claim(2,'Los instrumentos solicitan asociaciones, reconstrucción e información ideal; la forma de elicitación afecta su interpretación.','INTERPRETACION',['R006','R007','R008','R009','E05-P153'],'C','reglas_recodificacion R006–R009','No neutralidad completa ni nueva aplicación del guion.')
claim(2,'La técnica conservó identificador y punto tras contrastar identidad; modificó acceso en la copia.','RELATO',['E01-P065','C004'],'P','proceso E01, nodos N009/N010','Relato de una entrega, no propagación de actualizaciones.')
claim(2,'El libro común conserva 64 códigos y 123 ejemplos; 545 párrafos participantes, 713 fragmentos y 971 asignaciones tienen unidades distintas.','DOCUMENTAL',['R013','R014','S01-D013'],'C','codigos_comunes y reglas R013/R014; S01-D013','Conteo documental, no relevancia ni validez humana.')
claim(3,'Los cinco procesos tienen inicios, cierres, decisiones y retornos diferentes; no forman una cadena observada.','INTERPRETACION',['S01-H003','S01-H009','S01-H010','S01-H013','S01-D006'],'P','procesos E01–E05 e integracion_entre_casos','Reconstrucciones relatadas, no auditoría de operación efectiva.')
claim(3,'D01 sostiene cuatro modelos parciales, sin fuentes directamente atribuibles a los cinco episodios ni divergencias formalmente demostradas.','DOCUMENTAL',['D01-M001','D01-M002','D01-M003','D01-M004','D01-C003','D01-C009'],'D','modelos_documentales; cobertura_casos y contrastes','No demuestra inexistencia de documentos ni cumplimiento de actores.')
claim(4,'El mapa ampliado comprende 46 actores en doce ámbitos; origen y capacidad no equivalen a postura de homologación.','DOCUMENTAL',['ACT01-AMB007','ACT01-A001','ACT01-A033','ACT01-A046'],'A','ambitos/actores/posicion_homologacion','Poder e interés relativos; todas las posiciones no recabadas.')
claim(4,'La coordinación cultural puede compartir beneficios y cargas de memoria, condicionadas a mantener revalidación con anfitriones.','INTERPRETACION',['ACT01-H002','E03-P172','E03-P182'],'A','hipotesis_coordinacion H002','Alianza posible, sin aceptación ni resistencia observada.')
claim(4,'La investigación puede trasladar esfuerzo de contraste a quienes comparten experiencias.','INTERPRETACION',['ACT01-H003','E02-P159'],'A','hipotesis_coordinacion H003','Preocupación de esta voz; no carga sentida u oposición recabada.')
claim(5,'La suficiencia de una descripción y la carencia para explicar alternativas de elección pueden coexistir.','INTERPRETACION',['N01-N006','N01-N007','N01-N008','E02-P083'],'N','necesidades N006–N008','No reconstruye las alternativas faltantes.')
claim(5,'N013 conserva comunicación parcialmente abierta de autonomía de sesiones, sin confusión general demostrada.','RELATO',['N01-N013','E03-P184'],'N','necesidades N013','Perspectiva de coordinación; no voz de toda comunidad.')
claim(5,'Los 29 enunciados, seis deseos y 21 historias no son requisitos aprobados; N005 sigue como condición sin historia.','DOCUMENTAL',['N01-N005','N01-N004','HU01-H003','HU01-H021'],'H','historias/cobertura_necesidades','28 criterios y 90 operaciones son propuestas, no ensayos ejecutados.')
claim(5,'La cadena de último cambio vincula deseo E01, N004, H003, metadatos y criterio futuro de retomar sin memoria oral completa.','PROPUESTA',['E01-P137','N01-N004','HU01-H003','HU01-M003','HU01-K004'],'H','historias H003; perfiles_metadatos M003','Ideal solicitado; conversación nueva no se sustituye por el archivo.')
claim(5,'La segunda ocasión vincula N009 y H006 con un contraste voluntario de unidad y afirmación.','PROPUESTA',['E02-P143','N01-N009','HU01-H006','HU01-M006','HU01-K008'],'H','historias H006; perfiles_metadatos M006','Aceptación y esfuerzo por comprobar; resolución temporal desconocida.')
claim(5,'En mercería, tocar el material no prueba desempeño cosido ni elimina la restricción de cantidad.','INTERPRETACION',['E04-P075','E04-P152','N01-N020','N01-N023','HU01-H017'],'N','necesidades N020/N023','Sin defecto observado, ensayos aportados ni ventas futuras.')
claim(5,'La indeterminación forma parte de la salida personal; la nota ideal no asegura ambiente o mesa actuales.','INTERPRETACION',['E05-P119','E05-P160','N01-N029','HU01-H021'],'N','necesidades N025–N029','No se implementan notas ni se generaliza a usuarios urbanos.')
claim(6,'La distribución de información tiene respaldo acotado, pero su efecto y la base común son hipótesis a comprobar.','DOCUMENTAL',['D01-A002','D01-A003','D01-A004','D01-C013'],'D','afirmaciones_encargo A002–A004; contraste C013','Documentación del sistema y relatos no son medición causal de daño.')
claim(6,'La ausencia absoluta de plataformas necesita matizarse por antecedentes SIGCDMX; ello no prueba homologación completa.','DOCUMENTAL',['D01-F004','D01-F005','D01-A001'],'D','fuentes F004/F005 y afirmacion A001','Se consulta el contraste documental recibido; no nueva prueba de servicios en vivo.')
claim(6,'Identidad, versión, periodicidad y permisos de las dos capas SSC permanecen sin comprobar.','DOCUMENTAL',['D01-A006','D01-A007','D01-A008','D01-A009','D01-A011'],'D','afirmaciones_encargo A006–A011','No se sustituye el insumo por catálogo público parecido.')
claim(7,'La retórica cartográfica selecciona y jerarquiza; título y unidad requieren respaldo.','DOCUMENTAL',['T01-F002','T01-G001'],'T','fundamentos G001; Harley resumen y pp. 10–11','Fundamento externo consultado; no prueba exclusión local específica.')
claim(7,'MAUP distingue escala y zonificación; la igualdad de conteos no demuestra identidad de capas.','DOCUMENTAL',['T01-F001','T01-G005','T01-V002'],'T','G005/V002; Openshaw pp. 8–10','Experimento de sensibilidad propuesto, no ejecutado.')
claim(7,'El Marco Geoestadístico sirve al censo mediante límites convencionales.','DOCUMENTAL',['T01-F041'],'T','fuente F041; INEGI 2021 §6.2 p.7','Fundamento histórico; no inspección vectorial ni equivalencia jurídica.')
claim(7,'Se proponen cuatro prácticas para incertidumbre, unidades, escenarios y exclusiones.','PROPUESTA',['T01-V001','T01-V002','T01-V003','T01-V004','HU01-H001','HU01-H006','HU01-H011'],'T','practicas_diseno V001–V004','Sin universo no se calculan porcentajes ni tasas.')
claim(7,'SCAN, potencia/escalamiento y ABM no se usan en productos básicos; TDA es condicional.','PROPUESTA',['T01-L001','T01-L002','T01-L003','T01-L004','HU01-H003','HU01-H006','HU01-H011'],'T','lentes L001–L004','Herramientas candidatas y compatibilidad no probada; no se ejecuta ningún lente.')
claim(8,'La adaptación de GeoInsights separa etapas, procedencia, ramas y retornos.','PROPUESTA',['T01-F020','T01-F033','T01-P001','T01-P002','T01-P003','HU01-H003','HU01-H006','HU01-H011'],'T','arquitectura/adaptacion_geoinsights','Snapshot estático MIT, no pipeline probado en CDMX.')
claim(8,'Los tres candidatos articulan expediente, cuaderno y memoria con ensayos futuros y condiciones de descarte.','PROPUESTA',['T01-P001','T01-P002','T01-P003','N01-N004','N01-N009','N01-N016','HU01-H003','HU01-H006','HU01-H011'],'T','productos/criterios y condicion_descarte','Sin aceptación ni impacto; no incluye muestras físicas como función pública obligatoria.')
claim(9,'Identificadores locales y hashes facilitan revisión, sin certificar FAIR ni verdad.','DOCUMENTAL',['T01-F017','HU01-H003'],'H','estado_fair y perfil_objeto_local','Faltan registros externos, gobernanza y permisos/licencias pertinentes.')
claim(9,'JANUS se adapta a trazabilidad y revisión; no se acredita revisión humana independiente ni concordancia.','DOCUMENTAL',['MET-JANUS'],'editorial/fuentes/fuente_metodo_JANUS.json','nota completa y consulta REP01 de métodos del preprint','No conformidad integral; generación del corpus y registros faltantes explicitados.')

figuras=[
{'id':'REP01-F001','titulo':'Conservar el punto después de interpretar la diferencia','seccion':'REP01-S003','archivo':'editorial/figuras/REP01-F001.png','fuentes':['P01-E01-N001','P01-E01-N002','P01-E01-N003','P01-E01-N005','P01-E01-N006','P01-E01-N007','P01-E01-N008','P01-E01-N009','P01-E01-N010','P01-E01-N011','P01-E01-N012','P01-E01-N013','P01-E01-N014','E01-P065','E01-P071','E01-P081'],'relacion_representada':'Secuencia comprimida de revisión y aclaración mediada; línea final sin flecha indica límite, no transferencia.','simplificacion':'Agrupa N001–N002 recepción/alcance; N003/N005/N006 contraste; N007–N008 consulta; N009–N011 decisión/copia; N012–N014 entrega y pregunta. Omite N004 de otros dos registros, N015 de práctica general y contingencias contrafactuales; no afirma una cronología sin solapamientos.','estado_revision':'REALIZADA','alcance_revision':'Inspección visual asistida de exportación y cotejo de significados/medios con nodos citados y E01 completa. No revisión humana independiente; tamaño final en maquetación pendiente.','editable':'editorial/figuras/REP01-F001.dot','vector':'editorial/figuras/REP01-F001.svg','tamano_propuesto':'Ancho 11–13 cm; figura vertical, se debe revisar espacio y tipo efectivo al maquetar.'},
{'id':'REP01-F002','titulo':'Dos cadenas de necesidad ideal a comprobación futura','seccion':'REP01-S005','archivo':'editorial/figuras/REP01-F002.png','fuentes':['E01-P137','N01-N004','HU01-H003','HU01-M003','HU01-K004','E02-P143','N01-N009','HU01-H006','HU01-M006','HU01-K008'],'relacion_representada':'Derivación analítica en dos columnas independientes; no flujo institucional o aceptación.','simplificacion':'Conserva origen ideal, historia, campos clave y criterio; omite pasos y campos completos que permanecen en HU01. Restricciones se explican en prosa: consulta nueva y participación/carga.','estado_revision':'REALIZADA','alcance_revision':'Inspección asistida de PNG individual tras corregir composición horizontal demasiado ancha; dos columnas sin cruces. Cotejo de ids y criterios contra HU01. Legibilidad de maquetación pendiente.','editable':'editorial/figuras/REP01-F002.dot','vector':'editorial/figuras/REP01-F002.svg','tamano_propuesto':'Ancho 16.5–17 cm; comprobar etiquetas en Word/PDF.'},
{'id':'REP01-F003','titulo':'Arquitectura propuesta con rama por caso y revisión de incidencias','seccion':'REP01-S008','archivo':'editorial/figuras/REP01-F003.png','fuentes':['T01-F020','T01-M001','T01-M002','T01-M003','T01-M004','T01-M005','T01-M006','T01-P001','T01-P002','T01-P003'],'relacion_representada':'Extracción→unificación; rama agregada o directa→construcción→análisis→productos. Retorno discontinuo de revisión a unificación.','simplificacion':'Sintetiza etapas de arquitectura; omite atajos agregación→análisis y construcción→productos, detalle de once contratos, adaptadores y ocho representaciones. El retorno agrupa el camino análisis→construcción→unificación para una duda de significado, sin afirmar enlace directo obligatorio ni corrección automática. Otros retornos a extracción/agregación quedan en arquitectura completa.','estado_revision':'REALIZADA','alcance_revision':'Inspección asistida de exportación y ramas/retorno con arquitectura T01 y README GeoInsights. No diagrama operativo ejecutado. Revisión en página final pendiente.','editable':'editorial/figuras/REP01-F003.dot','vector':'editorial/figuras/REP01-F003.svg','tamano_propuesto':'Ancho 16.5–17 cm; comprobar etiquetas y pies.'}]
dump(P/'editorial/controles/revision_figuras.json',{'tipo':'INSPECCION_VISUAL_ASISTIDA','figuras':figuras,'limite':'Tres figuras nuevas inspeccionadas realmente; revisión de diagramas originales se conserva como registro histórico, no nueva inspección global.'})

# Bibliografía del manuscrito: solamente objetos citados y consultados.
refs=[]
def ref(cite,full,url,source,loc,lim,route='CONSULTA_PRIMARIA_DIRIGIDA'):
 refs.append({'id':f'REP01-B{len(refs)+1:03}','cita_en_texto':cite,'referencia_completa':full,'url':url,'fuente_registro':source,'localizador_consultado':loc,'estado':'VERIFICADA','limites':lim,'ruta_consulta':route})
ref('D01 (documento interno)','D01: Contraste documental y revisión del encargo. (s. f.). Versión revisada 1.1. Documento interno de coordinación asistida, autor personal no consignado.',None,'D01-F001/F002/F004/F009/F010 (fuentes subyacentes)','72_contraste_documental_v1_1.md; modelos, contrastes y registros de fuentes','Consulta del documento de contraste, no nueva lectura de todos sus originales. No se asume autoría personal ni año desde el nombre.','DOCUMENTO_INTERNO_CONSULTADO')
ref('DataLama Team, 2020–2021','DataLama Team. (2020–2021). COVID-19 GeoInsights Mobility Pipeline. Código/documentación, commit ab60b86a6a87bca0dd370c7c4af3ada4185d187e. Licencia MIT.','https://github.com/data-lama/covid_geoinsights_pipeline/tree/ab60b86a6a87bca0dd370c7c4af3ada4185d187e','T01-F020/T01-F033','README completo: Architecture/Configuration/External data/Credits; LICENSE; procedencia_snapshot.json','Referencia estática; el periodo es el atribuido al equipo, no año de un artículo; no ejecución.','COPIA_LOCAL_PRIMARIA')
ref('Feged Rivadeneira, 2025','Feged Rivadeneira, A. (2025). The JANUS Framework: Leveraging Large Language Models for Qualitative Analysis and Manuscript Writing. Preprint v1, Research Square. DOI 10.21203/rs.3.rs-7580516/v1.','https://doi.org/10.21203/rs.3.rs-7580516/v1','MET-JANUS','Cubierta; Methods, pp. PDF 9–10, preparación/codificación, revisión y producción. PDF primario recuperado tras fallo del DOI.','No apéndices completos ni revisión por pares afirmada; no valida este corpus. Nombre de cubierta abreviado.')
ref('GO FAIR Foundation, s. f.','GO FAIR Foundation. (s. f.). The FAIR Guiding Principles. Consulta: 25 de noviembre de 2026.','https://www.gofair.foundation/fair-principles','T01-F017','Findable/Accessible/Interoperable/Reusable, A1.2; página consultada en REP01.','Principios y autorización, sin evaluación FAIR integral; no artículo Nature declarado leído.')
ref('Grimm et al., 2020','Grimm, V., Railsback, S. F., Vincenot, C. E., Berger, U., Gallagher, C., DeAngelis, D. L., Edmonds, B., Ge, J., Giske, J., Groeneveld, J., Johnston, A. S. A., Milles, A., Nabe-Nielsen, J., Polhill, J. G., Radchuk, V., Rohwäder, M.-S., Stillman, R. A., Thiele, J. C., y Ayllón, D. (2020). The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism. JASSS, 23(2), 7.','https://www.jasss.org/23/2/7.html','T01-F012','Título/autores, resumen y pasajes de propósito/patrones, entidades, escalas y scheduling.','Consulta dirigida; no modelos calibrados ni aplicaciones completas leídas.')
ref('Harley, 1989','Harley, J. B. (1989). Deconstructing the Map. Cartographica, 26(2), 1–20.','https://disp.web.uniroma1.it/sites/default/files/Harley%20-%20deconstructing%20the%20map.pdf','T01-F002','Resumen; retórica pp. 10–11.','No lectura de bibliografía ni identificación de Andrea con Harley.')
ref('INEGI, 2021','Instituto Nacional de Estadística y Geografía. (2021). Características de las localidades 2020: Síntesis metodológica y conceptual.','https://www.inegi.org.mx/contenidos/inegi/spc/doc/bibliografia/CL_SMC_2020.pdf','T01-F041','Portada/datos editoriales y §6.2 p. impresa 7, PDF índice cero 15 (página 16 contando desde 1).','Alcance metodológico histórico del Censo 2020; no edición vectorial ni aplicación jurídica acreditada.')
ref('Openshaw, s. f.','Openshaw, S. (s. f.). The Modifiable Areal Unit Problem. CATMOG 38. Geo Books.','https://www.uio.no/studier/emner/sv/iss/SGO9010/openshaw1983.pdf','T01-F001','Introducción pp. 3–4 y III(i) definiciones pp. 8–10; páginas enfrentadas.','Año no comprobado en ejemplar; no se infiere 1983/1984 del nombre. No monografía completa ni resultados locales.')
ref('van Veen et al., s. f.','van Veen, H. J., Saul, N., Eargle, D., y Mangham, S. W. (s. f.). KeplerMapper: Background. Documentación 2.1.0.','https://kepler-mapper.scikit-tda.org/en/latest/theory.html','T01-F009','Background/Mapper: proyección, cobertura, agrupamiento y miembros compartidos; cabecera 2.1.0.','No adopta garantías promocionales de robustez ni compatibilidad probada; no artículo original Mapper declarado leído.')
dump(P/'editorial/registros/bibliografia_consultada.json',refs)

# Evidencia específica por requisito; estados conservadores donde falta acreditación externa.
M='ATENDIDO_EN_MANUSCRITO';SOP='ATENDIDO_EN_SOPORTE';PAR='PARCIAL';PEN='PENDIENTE';NA='NO_APLICA_JUSTIFICADO'
cat={
'ALC':([1,2,6,8],['24_registro_corpus.json',S['D'],'editorial/fuentes/06_canvas_rubrica_y_feedback.md']),
'APE':([2],['11_guion_base_y_adaptaciones.md',S['C'],S['S']]),
'NAT':([2],['corpus/LEEME.md',S['C'],'editorial/registros/incidencias_metodologicas.md']),
'INS':([2,3,5],['11_guion_base_y_adaptaciones.md','24_registro_corpus.json',S['P'],S['N']]),
'COD':([2], [S['C'],'analisis/recodificacion/LEEME.md',S['S']]),
'PRO':([3],[S['P'],S['D'],'analisis/procesos/P01/figuras_revisadas_v1_1/LEEME.md']),
'ACT':([4],[S['A'],'76_actores_y_preferencias_v1_1.md']),
'NEC':([5],[S['N'],S['H'],'88_historias_y_objetos_v1_1.md']),
'GCR':([7],[S['T'],'analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/fundamentos_criticos.md','analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/practicas_diseno.md','analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/alternativas_agregacion.md']),
'LEN':([7],[S['T'],'analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/lentes.md','analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/herramientas.md']),
'DAT':([8],[S['T'],'analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/arquitectura.md','analisis/diseno/T01/soportes_revisados_v1_1/esquemas/contratos_propuestos.json','analisis/diseno/T01/soportes_revisados_v1_1/desarrollo/productos.md']),
'FDO':([9],[S['H'],'analisis/historias/HU01/LEEME.md']),
'JAN':([2,9],['24_protocolo_analisis.md','editorial/registros/memo_integracion.md','editorial/registros/incidencias_metodologicas.md','editorial/registros/bibliografia_consultada.json']),
'RED':([1,2,3,4,5,6,7,8,9],['editorial/registros/guia_por_seccion.md','editorial/controles/revision_figuras.json']),
'REP':([9],['LEEME.md','editorial/registros/indice_inverso.json','editorial/registros/agenda_pendientes.md']),
'CTX':([2,9],['registro/prompts_analisis/LEEME.md','registro/salidas_iniciales/LEEME.md','editorial/registros/memo_integracion.md'])}
proofs={
'ALC':[
'Portada individual y S001/S008 delimitan Descubre/Define y propuestas sin implementación.',
'Registro corpus contiene E01–E05 y cinco DOCX/vistas completas. Se declara generación con IA; no acreditación de cinco entrevistas de campo.',
'S001 distingue mantenimiento/actualización pública, análisis universitario, coordinación civil y consumo comercial/personal.',
'Los cinco perfiles de 24_registro_corpus carecen de voz ADIP; S001 conserva la exclusión.',
'Se presupuestan secciones y figuras; no existe Word/PDF maquetado para contar diez páginas.',
'Delimitadores separan portada, cuerpo y referencias; anexos en ZIP y declaración ampliada fuera del cuerpo.',
'Portada no fija entrega; fechas de revisión no se presentan como entrevista ni plazo.',
'S008 presenta candidatos y ensayos futuros; se entregan documentos, no producto implementado.',
'29 necesidades de cinco ámbitos en N01; no se limita el análisis a capas SSC ausentes.',
'S007 evalúa métodos por pregunta; no se convierten árboles/crimen o crisis en escenarios del corpus.',
'S001/S006 contrastan el planteamiento institucional; D01-A001–A022 diferencia evidencia, objetivos y supuestos.',
'S002 y guion identifican diseño/editorial asistido, sin afirmar otro instrumento validado.',
'S001 y registro corpus identifican E04/E05 como dos usos no especializados diferentes.'],
'APE':[
'Guion B03–B06 y aperturas E01-P006, E04-P007 y E05-P006 parten de actividad/propósito.',
'S001/S006 no concluyen base única; guion B25–B31 permite soportes y prácticas suficientes.',
'Listas y asociaciones parten de lo introducido por participantes; P01 conserva roles por episodio.',
'Guion contiene cinco adaptaciones; las entrevistas no especializadas explican mercería y salida sin imponer jerga.',
'S002 comenta repreguntas y correcciones concretas; libro R006–R009 separa forma, función y sugerencia.',
'Cada entrevista desarrolla un episodio en P01, desde inicio hasta cierre reconocido.',
'S003/S005 conservan puertas, alternativas y perspectivas desconocidas; no se completan.',
'ACT01 distingue VOZ_ENTREVISTADA, TERCERO_RELATADO y ACTOR_DOCUMENTAL; S004 explica alcance.',
'E01-P120, E02-P128, E03-P149, E04-P138 y E05-P136 introducen ideal después de prácticas.',
'Guiones y entrevistas no requieren que la persona proponga SCAN, potencia, TDA o ABM; S007 los evalúa después.',
'El paquete final no contiene corpus del compañero; no se dispone aquí de todos los paquetes originales de desarrollo para certificar aislamiento histórico.',
'Se conservan análisis locales A01–A05 y sus entradas; no se certifica retrospectivamente la configuración o contexto de generación de cada entrevista.',
'S005/S008 distinguen deseos, historias analíticas y candidatos sin aceptación o impacto medido.',
'S001/S002 explican muestra funcional y elicitación; no saturación, neutralidad completa o representatividad.'],
'NAT':[
'Las cinco fuentes conservan preguntas breves y extensas; no se reescriben para homogeneizar estilo.',
'Párrafos y turnos de longitudes distintas se preservan íntegros; no se usa longitud como calidad.',
'Se conservan muletillas tal como aparecen; no nueva intervención ni prueba objetiva de naturalidad.',
'E05-P069 autocorrige cronología y E04-P112 cambia nombre del cierre; sin editar fuentes.',
'S002 documenta aclaraciones y recapitulaciones más allá de un listado; corpus completo las permite revisar.',
'E01-P071, E03-P189 y E05-P173 corrigen entendimientos; el manuscrito conserva esas rectificaciones.',
'Encabezados y primeras respuestas explican cinco funciones y actividades, sin identidades inventadas.',
'Se usan funciones sin nombres personales de participantes; no certificación de anonimato irreversible.',
'E01-P164–P165, E02-P179–P180, E03-P196–P197, E04-P192–P193, E05-P185–P186 conservan cierre.',
'P01 registra solapamientos y cambios de nombres; las fuentes conservan tres instrumentos sin ordenar artificialmente su discurso.',
'Las respuestas no especializadas describen materiales y convivencia; se conserva la voz generada sin certificar naturalidad empírica.',
'Cotejo de fuentes inmutables mantiene mismos bytes; el argumento reconoce casos suficientes y contraejemplos.'],
'INS':[
'Registro de cobertura localiza actores/asociaciones, proceso/fases y necesidades/ideal en E01–E05.',
'P01/ACT01 preservan identificación situada de roles y límites de conocimiento.',
'Las asociaciones se explican en E01-P041/P047, E02-P025/P033, E03-P026/P031, E04-P043/P048 y E05-P023/P038.',
'Guion B09/B10 y adaptaciones usan comparación verbal elegida y explicación; no se inventan tarjetas empleadas.',
'Libro R005 y S002 analizan función de la metáfora, no significados externos.',
'Guion acepta imágenes/analogías; las fuentes usan ejercicio verbal, sin tarot obligatorio.',
'P01 contiene inicio y cierre por entrevista; S003 no impone hito común.',
'P01.agrupaciones_participante y correcciones_y_solapamientos conservan nombres revisados.',
'S003 y mapas completos identifican roles, tabla/croquis/notas/muestras, canales conocidos y vacíos.',
'P01 distingue retornos ocurridos y contingencias declaradas; S003 conserva pregunta posterior y revisión entre encuentros.',
'S003 sigue de consulta a copia explicada, interpretación, anuncio, despacho y convivencia.',
'S005 y N01.necesidades vinculan objeto de información a decisión, contexto y suficiencia.',
'S005 distingue atendida, parcial, carencia declarada, ideal y condicional; N008/N013 son ejemplos.',
'N004/N009/N016/N017/N023/N029 conservan seis deseos; sus ejercicios y barreras son localizables.',
'Guion B27 y E05-P153 permiten formas diferentes; S002 reconoce influencia de opciones ofrecidas.',
'HU01 separa contexto temporal/espacial de resolución/escala desconocidas; S005/S007 lo explican.',
'24_registro_corpus y guion existen; fechas y algunos encabezados de versión no consignados se mantienen.',
'Aperturas contienen aceptación textual; no audio/fecha/firma adicionales ni consentimiento documental independiente.'],
'COD':[
'Cinco DOCX 1.0 y JSON canónicos con hashes se preservan sin cambio.',
'E0x-Pnnn, R0x-Snnn y códigos comunes se mantienen; citas editoriales agregan REP01-Qnnn.',
'Segmentos tienen párrafo, turno y offsets; controles complementarios cotejan continuidad.',
'Siete citas REP01 cotejadas contra participante y contexto; validador y control complementario ejecutados.',
'Libro R009/R011 y trace citas exigen voz Participante; preguntas solo aportan contexto.',
'registro/salidas_iniciales/primeras_lecturas conserva A01–A05 antes de libro y síntesis.',
'Libro 1.3 y R01/R02 1.3, R03 1.2, R04/R05 1.1 preservados como aplicaciones operativas, no pilotaje humano.',
'Los 64 códigos incluyen nombre, definición, inclusión y exclusión en JSON/Markdown.',
'123 ejemplos tienen cita/párrafo y nota de alcance; cotejo programático contra corpus.',
'S002 incluye tabla con conceptos y fronteras; libro conserva explicación completa sin exigir memorizar ids.',
'Fuentes preferidas y objetos HU01 conservan identificadores canónicos; índice inverso los enlaza sin recodificar.',
'Afirmaciones REP01 distinguen RELATO/DOCUMENTAL/INTERPRETACION/PROPUESTA; fuentes conservan modalidades más finas.',
'S003/S005 conservan recursos suficientes, compra no obligatoria y limitaciones de interpretación.',
'S002 explica unidades de 545/713/971; prioridad local no deriva de frecuencias.',
'Metadatos, linajes y decisiones del libro/recodificaciones preservados; rótulos históricos señalados.',
'S002 muestra ejemplo cita→C004→interpretación y esquema; libro completo queda localizable.'],
'PRO':[
'Cinco mapas relatados y cuatro modelos documentales parciales se preservan, sin correspondencia documental directa por episodio.',
'D01 identifica fuentes y alcance por modelo; falta documento directamente aplicable a cada episodio anónimo.',
'S003/S006 separan modelo publicado, encargo y operación relatada; no manual PAOT atribuido a E01.',
'P01 contiene cinco reconstrucciones completas; S003 sintetiza inicio/decisión/cierre de cada una.',
'S003 sigue origen, entrega, uso/decisión y retorno propios; tramos posteriores no observados siguen desconocidos.',
'S003 y figura F001 no conectan sectores distintos; cada proceso conserva su perspectiva.',
'Mapas P01 enlazan roles, objetos, entradas/salidas y criterios; tabla S003 explica ejemplos legibles.',
'Cero divergencias formalmente demostradas; D01 conserva contraste de ámbitos e hipótesis, sin inventar mecanismos de incumplimiento.',
'D01 distingue fuentes normativas, históricas y autodescripciones; S003 no llama vigente a flujo del episodio.',
'Agenda documental conserva diez pendientes y soportes requeridos; S003 señala otra puerta y uso posterior.',
'S003/S004 distinguen revisión técnica, consulta y decisiones de otros; no aprobación jerárquica supuesta.',
'Figuras nuevas inspeccionadas y fuentes editables presentes; legibilidad real del manuscrito final todavía pendiente.'],
'ACT':[
'S004 y ACT01 contienen 46 actores, más amplios que las cinco voces.',
'ACT01 incluye nombre funcional, institución/unidad cuando constan y estados no identificados; S004 nombra unidades PAOT específicas.',
'S004 define poder/interés/posición y explica su relatividad al ámbito; homologación NO_RECABADA.',
'ACT01.ganancias_y_perdidas y S004 relacionan continuidad y carga condicional sin ahorro medido.',
'Tres hipótesis ACT01-H001–H003 explicitan mecanismo, condición y contraargumento; S004 no las trata como posturas recabadas.',
'S004 distingue decisión de técnica y aportación de compañera/proveedor sin jerarquía inventada.',
'Origen por actor y fuente se preserva; S004 separa voces, terceros y actores documentales.',
'Cinco fichas funcionales con decisiones/restricciones están en ACT01/HU01 y sus figuras originales; no arquetipos representativos.',
'Unidades identificables se conservan con fuente; no se verifican instituciones anónimas ni nombres de departamentos faltantes.'],
'NEC':[
'29 enunciados con decisión/objeto/contexto y verificaciones futuras en N01; S005 ejemplifica su uso.',
'Cada necesidad vincula actores, entrevista, contexto y decisión; dos cadenas desarrolladas en S005.',
'N01 diferencia información actual y faltante/deseada; S005 no convierte ideales en déficits.',
'Cinco criterios de prioridad local y límites explícitos; S005 admite orden parcial y empates.',
'N01.vinculos_sectoriales distingue actividad pública/civil/privada/personal y programas no identificados.',
'Cinco perfiles analíticos funcionales de HU01 se derivan con límites; no se acreditan cinco arquetipos representativos.',
'21 historias con relaciones múltiples a 29 necesidades; no una historia por entrevistado.',
'S005 explica objetivo/decisión de H003/H006 y naturaleza analítica, sin copiar códigos como historias.',
'S005 y figura F002 enlazan párrafo, necesidad, historia, metadatos y criterio.',
'28 criterios Dado/Cuando/Entonces propuestos, no ejecutados ni aceptados, con origen y límites.',
'HU01.perfiles_analiticos y restricciones de historias preservan autoridad, materialidad, autonomía y carga.',
'76 objetos locales con payload, versión, metadatos y relaciones; control de resolución/huellas ejecutado.',
'21 perfiles preliminares de metadatos; dos cadenas S005 explican campos y desconocidos.',
'N005 y resoluciones/escala/acceso no aportados permanecen desconocidos/condicionales; no se inventan insumos.',
'90 operaciones con entrada/operación/salida e intervención humana; se explican dos recorridos en S005.'],
'GCR':[
'S007 y T01-G002/G007 discuten propósito, autoría y límites cuestionables.',
'S007 distingue retórica visual/verbal/metodológica con ejemplo de acceso no comprobado; T01-G001.',
'S007 y T01-G003 relacionan selección, disponibilidad, registro y ausencia sin tasa de subregistro inventada.',
'S007 define escala y zonificación; T01-G005 propone sensibilidad sin ejecutarla.',
'S003/S007 no asumen diferencia de entrada/geometría como error; T01-G007 conserva pluralidad legítima.',
'S007 requiere población elegible y denominador; T01-V001 impide tasa con base desconocida/cero.',
'S007 compara jurisdicción y pregunta analítica; T01-G007 no adjudica competencias locales no documentadas.',
'T01.alternativas_agregacion y arquitectura versionan partición/parámetros/tiempo de manera propuesta.',
'T01-G002/G003/V004 permiten objeción y describen exclusiones; S007 conserva voces no observadas.',
'Ocho familias de agregación evaluadas en soporte con pertinencia por pregunta; S007 selecciona comparación condicional.',
'S007 y T01-G008 separan incertidumbre, error, desconocimiento y desacuerdo, sin probabilidades fabricadas.',
'T01-V002 propone comparar unidades sobre registros/periodo comunes; sin prueba local ejecutada.',
'T01-V003 propone escenarios con configuración versionada; S007 declara no ejecución.',
'T01-V004 propone conteos solo con marco conocido; S007 conserva descripción cualitativa sin universo.',
'S007 y T01-V002 distinguen igualdad de conteos de identidad geométrica/semántica o jurisdicción.'],
'LEN':[
'T01-L001 define pregunta, evento/control, nula, ventanas y sensibilidad; S007 lo descarta en básicos.',
'T01-L002 diferencia Y=aN^beta de distribución de duraciones, estimación y alternativas; S007 sintetiza.',
'T01-L003 define unidad, matriz, métrica, filtro/cobertura/agrupamiento y lectura de aristas.',
'T01-L004 define agentes/entorno/reglas, calibración y evaluación futura sin simular.',
'S007 explica ausencia de datos/pregunta que justifiquen tres lentes y condición adicional para TDA.',
'T01 fuentes primarias y herramientas identifican documentación y compatibilidad NO_PROBADA; no se recomienda despliegue actual.',
'S007 y metadatos T01 no declaran ejecución de ninguno de los cuatro lentes.',
'S007 y T01-L001 conservan sensibilidad a unidades y parámetros; escaneo no elimina MAUP.',
'T01.afirmaciones_tecnicas coteja abreviaturas docentes con fuentes primarias; REP01 usa F041 en vez del texto indexado F014.',
'S007/S008 no trasladan datos/experimentos epidemiológicos o británicos a CDMX.'],
'DAT':[
'S008 atribuye DataLama Team 2020–2021, commit y MIT; README/procedencia/licencia conservados.',
'S008 y figura F003 distinguen seis etapas, rama directa y retorno; arquitectura desarrolla responsabilidades.',
'Once contratos propuestos con 119 campos en esquemas/contratos_propuestos; no controles de sistema implementado.',
'S008 separa originales y derivados; contratos conservan fuente, revisión y límites sin sobreescritura.',
'T01 evalúa ocho alternativas con pertenencias y resultados comparables propuestos; no cálculo territorial.',
'Arquitectura.representaciones contempla puntos/líneas/polígonos/ráster/red y límites de adaptadores.',
'Representaciones T01 evalúan 3D condicional y exclusión sin necesidad actual acreditada.',
'Arquitectura y contratos distinguen CRS, resolución, unidades y tiempo; null real separado de granularidad requerida propuesta.',
'Módulos/adaptadores de arquitectura exigen semántica, fuente y validación para incorporar insumo.',
'Arquitectura.google_earth_engine identifica pertinencia y dependencias; sin integración o ejecución.',
'S008 distingue preparación y análisis de producto/interfaz; contrato no se sustituye por dashboard.',
'S008/README GeoInsights indican datos/configuración externos y lectura estática, sin prueba para Carto-Visor.',
'S008 fundamenta expediente/cuaderno/memoria con datos, decisión, comprobación futura y descarte.',
'S005/S008 separan necesidad expresada e innovación del análisis; no aprobación institucional.'],
'FDO':[
'S009 y estado_fair de HU01 mapean principios a controles/pendientes; no certificación integral.',
'76 registros locales incluyen ids, entidad, versiones, procedencia y payloads; cotejo en controles complementarios.',
'Registro de objetos especifica consulta académica y licencia desconocida; publicación NO_CONSTA, permisos por resolver.',
'S009 y A1.2 de FAIR distinguen acceso autorizado y publicación abierta.',
'S009 y objetos conservan pid_externo null; no depósitos/DOI del proyecto inventados.',
'Relaciones derivadas y referencias canónicas preservadas; índice inverso permite párrafo→necesidad→historia.',
'S009 explica hash como integridad; manifest no certifica verdad de contenido.',
'HU01.evaluacion_empaquetado y T01.extension_fair_janus evalúan RO-Crate/PROV sin implementarlos.',
'Versiones de dato, metadato e historias se distinguen; figuras nuevas tienen fuente y exportaciones con huellas.'],
'JAN':[
'29 afirmaciones centrales tipadas enlazan objetos canónicos y localizadores; sin reemplazar evidencia por prosa.',
'Relectura asistida de cinco entrevistas, siete citas y límites frente a las afirmaciones; revisión humana independiente pendiente.',
'Examen asistido acotado del manuscrito/figuras usa funciones y datos de autor autorizados; no auditoría integral de privacidad histórica.',
'Prompts y salidas recibidas se preservan más memo de integración; no constan exportaciones completas de todos los chats/contextos.',
'Metadatos registran descripción Codex/GPT-6 y modelo/parametros null, sin extrapolar identificador.',
'Memos recibidos y memo REP01 explican conservación de contraejemplos, tesis y decisiones editoriales.',
'Incidencias metodológicas registran alcance, resolución o pendiente; S006 contrasta generalizaciones sin corregir fuentes.',
'Bibliografía seleccionada registra consulta primaria dirigida o registro interno/segunda fuente, con año desconocido explícito.',
'S002/S009/declaración distinguen revisión asistida y humana independiente PENDIENTE.',
'No se calcula concordancia: faltan codificaciones humanas independientes de las mismas unidades.',
'S002/S009 no trasladan métricas de JANUS ni tratan 971 asignaciones como calidad.',
'Memo y LEEME distinguen auditabilidad y regeneración idéntica; entradas/modelo/rutas históricas limitan reproducción.',
'Controles principal/complementarios registran hechos ejecutados; pendientes no se rotulan PASS humano.',
'Linajes de R01–R05 y libro se conservan; REP01 no cambia códigos ni fuentes y no activa nueva recodificación.'],
'RED':[
'S001–S009 desarrollan conceptos antes de localizadores; tesis formulada en lenguaje sustantivo.',
'Identificadores se añaden entre paréntesis/enlaces; tabla de códigos define conceptos completos.',
'Siete citas de cinco voces se introducen con función y uso analítico; enlaces al corpus y contexto en trazabilidad.',
'S002/S005 y afirmaciones distinguen literal, paráfrasis e interpretación/propuesta.',
'Argumento avanza de suficiencia al método, procesos, autoridad, necesidad, crítica y diseño.',
'Se reserva desarrollo completo a soportes; el cuerpo explica decisiones con ejemplos y contraejemplos.',
'Enlaces locales del manuscrito comprobados; guía por sección e índice inverso amplían navegación.',
'Tres figuras nuevas con función argumental, DOT/SVG/PNG y revisión asistida; tamaño definitivo pendiente.',
'S006 razona distribución/daño, hipótesis de integración y supuestos de capas sin clasificación mecánica.',
'S002 explica instrumentos/recodificación/alcance y muestra ejemplo de interpretación trazable.',
'S005 desarrolla N004/H003/M003/K004 y N009/H006/M006/K008 con restricciones.',
'No se justifica contenido porque lo pidió el profesor; el encargo se contrasta como planteamiento institucional.',
'Cuerpo en presupuesto orientativo 2800–3400 palabras antes de enlaces; revisión humana de calidad pendiente.',
'S001/S002 y declaración ampliada describen generación, análisis, organización y escritura con IA; no transcripción de audios aportados.',
'Se entrega Markdown editable y ZIP según encargo REP01; Word/PDF y diez páginas son etapa de maquetación pendiente.'],
'REP':[
'LEEME raíz presenta pregunta, método, hallazgos y orden de lectura con regreso al manuscrito externo.',
'Cada carpeta contiene LEEME/README; controles comprueban presencia y navegación editorial.',
'Cinco DOCX/vistas, guion, registro de corpus y metadatos disponibles preservados; ausencias administrativas explícitas.',
'Libro, recodificaciones y S01 preferidos presentes con versiones y relaciones canónicas.',
'N01/HU01, 76 objetos locales, metadatos y criterios presentes con índices/huellas.',
'Scripts históricos y entradas/salidas recibidos, scripts editoriales y memo efectivo incluidos; no regeneración prometida.',
'Base curada excluye prompts de desarrollo de entrevistas; no se reintroducen del expediente maestro.',
'No carpetas vacías ni anexos que aparenten audio/firmas; diseños y controles distinguen propuesta/ejecución.',
'Validador principal coteja rutas/huellas/citas/estructura y complementario navegación/objetos.',
'Agenda conserva diez preguntas, posturas no recabadas, dependencias de diseño y maquetación.'],
'CTX':[
'Se conservan instrucciones y registros de integración; no se dispone de conversación maestra completa para certificar su gestión previa.',
'La instrucción actual prohíbe reiniciar entrevistas; solo se preserva corpus y registro histórico, sin certificar cómo se abrieron sus chats.',
'No se realizan nuevas entrevistas o ramas; aislamiento histórico no está acreditado con exportaciones.',
'No hay registro verificable de configuración de contexto antes de cada entrevista; no se reconstruye.',
'Cinco transcripciones y salidas están disponibles; no se acreditan modalidad temporal o momento exacto de exportación.',
'Primeras lecturas A01–A05 y paquetes de análisis separados preservados, sin nueva generación de entrevistas.',
'S01.lectura_entradas y registro preferido identifican corpus/libro usados; no se modifican para integración.',
'208 estados editoriales se asignan con prueba y límite; no se convierten estados de especificación en ejecución.',
'Versiones/linajes y decisiones de coordinación preservados; incidencias editoriales explican desajustes históricos.',
'Cobertura reúne cuatro dimensiones y sus límites; sin divergencias demostradas, firmas, paginación o revisión humana integral no se acredita nivel Destacado.',
'Se revisan texto, citas, fuentes dirigidas y figuras además de controles técnicos; revisión humana independiente pendiente.',
'No se abren espacios de entrevista en REP01; disponibilidad previa de paquetes históricos no completamente verificable.']}
coverage=[]
for req in rd(B/'requisitos/02_matriz_requisitos.json'):
 catid=req['categoria'];n=int(req['id'][len(catid):]);sec,sp=cat[catid];proof=proofs[catid][n-1]
 state=M
 limit='Atención editorial o diseño según el alcance indicado; no implica validación humana independiente ni implementación.'
 if catid in ['NAT']:state=PAR;limit='Se conserva material generado con IA; revisión asistida de adecuación no certifica naturalidad de conversación real. No se altera para aparentar cumplimiento.'
 if catid in ['GCR','LEN','DAT']:state=SOP;limit='Fundamento o especificación de diseño, no aplicación territorial ni utilidad probada. Herramientas candidatas; sin compatibilidad ejecutada.'
 if catid=='FDO':state=PAR;limit='Medidas locales presentes; registros externos, permisos y evaluación integral faltan según estado_fair. No conformidad por JSON o hash.'
 if catid=='REP':state=SOP;limit='Paquete para revisión, sin publicación ni licencia abierta del corpus. Registros disponibles no equivalen a expediente histórico completo.'
 if catid=='CTX':state=PAR;limit='Se conserva evidencia disponible de organización; no se certifican retrospectivamente todos los chats, configuraciones o aprobaciones.'
 if catid=='APE'and n in [11,12]:state=PAR;limit='Exclusión observable en la entrega; no auditoría de todo el contexto histórico de generación.'
 if catid=='ALC'and n==2:state=PAR;limit='Cinco entrevistas/transcripciones disponibles y analizadas; no se acredita su realización empírica independiente.'
 if req['id'] in ['ALC05','CTX04']:state=PEN;limit='Falta comprobación efectiva; no se sustituye por estimación o reconstrucción de un registro.'
 if req['id']=='ALC06':limit='Separación implementada en Markdown; recuento de páginas reales pendiente.'
 if req['id'] in ['INS17','INS18','COD07','PRO01','PRO02','PRO08','PRO12','ACT09','JAN02','JAN03','JAN04','JAN09','JAN14','RED08','RED13','RED15','CTX10','CTX11']:
  state=PAR;limit='Cumplimiento parcial con soporte y alcance en evidencia_cumplimiento; datos administrativos, aplicabilidad, ejecución o revisión humana/maquetación señalados no se acreditan.'
 if req['id']=='NEC06':state=PAR;limit='Se derivaron perfiles funcionales con trazabilidad, sin afirmar arquetipos representativos o validación poblacional.'
 if req['id']=='JAN10':state=NA;limit='No existen codificaciones humanas independientes de las mismas unidades; calcular concordancia sería improcedente. Se mantiene revisión humana pendiente.'
 if req['id']=='LEN06':state=PAR;limit='Documentación primaria registrada por T01 y reconsulta dirigida de Mapper/ODD; compatibilidad de herramientas no probada ni recomendación actual de despliegue.'
 if req['id'] in ['COD01','COD02','COD03','COD06','COD08','COD09','COD11','COD15','NEC12','NEC13','NEC15','JAN06','JAN08']:
  state=SOP
 coverage.append({'requisito':req['id'],'estado':state,'secciones':[f'REP01-S{x:03}'for x in sec],'soportes':sp,'evidencia_cumplimiento':proof,'limite':limit,'enunciado_original':req['requisito'],'prueba_original':req['comprobacion']})
assert len(coverage)==208

inc=[
('Corpus y consentimiento','Aperturas mencionan grabación y aceptación, sin audio/firma; instrucciones exigen declarar generación con IA.','Se preservan literales y se declara origen/alcance en S001 y declaración ampliada; acreditación externa no disponible.','ABIERTA'),
('Guion y fechas','11_guiones_entrevistas.json estado histórico aplicación pendiente; fechas de entrevista NO_CONSIGNADA.','No se actualizan fuentes; incidencia metodológica 2 y cobertura administrativa parcial.','ABIERTA'),
('Pilotaje y revisión','Libro R018 solicita revisión/pilotaje humano; secuencia continuó operativamente asistida.','S002 relata alcance efectivo y S009 conserva revisión humana independiente pendiente.','ABIERTA'),
('Rótulos históricos','Balances/memos R01 1.1, R02 1.2, R03 copia 1.1 y título de laguna R04 no coinciden con metadatos preferidos.','Priorizar linaje actual y conservar historia; localizadores en incidencias_metodologicas.md punto 4.','RESUELTA'),
('D01 aplicabilidad','Cero documentos aplicables a episodios y cero divergencias demostradas.','Mantener cumplimiento parcial de contraste y diez preguntas abiertas.','ABIERTA'),
('T01-F014 frente a F041','Texto indexado no acredita lectura vectorial del Marco Geoestadístico.','Se usa F041/INEGI 2021 §6.2 reconsultado y se conserva T01 intacto.','RESUELTA'),
('Registros de contexto y privacidad','Faltan exportaciones completas y registros históricos de configuración/control de privacidad.','Se incluye memo efectivo y examen editorial acotado, sin fingir exportaciones o anonimato certificado.','ABIERTA'),
('JANUS y generación','Methods del preprint limita generación de evidencia/resultados; el corpus del ejercicio se generó con IA.','JANUS se usa solo como adaptación de trazabilidad/revisión, sin validación empírica o conformidad integral; se señala discrepancia para revisión del usuario.','ABIERTA')]
incs=[{'objeto':a,'descripcion':b,'resolucion':c,'estado':e}for a,b,c,e in inc]

j={'metadatos':{'tarea':'REP01','version':'1.0','estado':'MANUSCRITO_PARA_REVISION','autor':'Ricardo Alfonso Graffe Garcia','matricula':'A01664904','revision_humana_independiente':'PENDIENTE','paginacion_estado':'PENDIENTE_MAQUETACION','versiones_fuentes_preferidas':{'corpus':'1.0','libro':'1.3','S01':'1.1','P01':'1.1','D01':'1.1','ACT01':'1.1','N01':'1.1','HU01':'1.1','T01':'1.1','R01':'1.3','R02':'1.3','R03':'1.2','R04':'1.1','R05':'1.1'},'modelo':None,'parametros':None,'herramienta_declarada':'Codex descrito por el entorno como basado en GPT-6; sin identificador verificable de ejecución.','limites':['Corpus generado con IA; no campo/audio/firma acreditados.','Estados editoriales no califican automáticamente la rúbrica.','Paginación estimada sin Word/PDF final.']},
'lectura_entradas':lecturas,
'tesis_y_estructura':{'argumento':'La utilidad de organizar información territorial depende de recuperar significado, respaldo, responsabilidad y ocasión para una decisión; centralizar es una posibilidad condicionada y no una necesidad demostrada por estos casos.','alcance':'Comparación interpretativa de cinco voces del corpus generado con IA y contraste documental de alcance explícito; no generalización institucional/urbana.','secciones':[x['id']for x in sections],'decisiones_editoriales':['Tesis y contraejemplos fijados antes de redactar; memo_integracion documenta selección.','Espacio principal a método/procesos/actores/necesidades/crítica; desarrollo técnico completo en soportes.','Siete citas de cinco voces, continuas y sin normalizar.','Tres figuras de síntesis con fuentes editables; otros mapas completos preservados.','No cambios de corpus, códigos, prioridades ni objetos para sostener argumento.','Trazabilidad/control/manuscrito externos al inventario; sin ciclo.'],'paginas_totales_presupuestadas':sum(pages),'presupuesto_no_medicion':True},
'secciones':sections,'citas':citas,'afirmaciones':af,'figuras':figuras,'referencias':refs,'cobertura_requisitos':coverage,
'repositorio':{'raiz':'REP01_repositorio','inventario':[],'originales_preservados':{'catalogo_base':'editorial/fuentes/catalogo_base.json','registro_inmutables':'editorial/fuentes/registro_entradas.json','regla':'Todos los originales de la base curada idénticos salvo LEEME raíz humano reemplazado por guía final; comprobado por comparación binaria.','versiones':reg['recodificaciones']},'adaptaciones':['Raíz base_repositorio/ pasa a REP01_repositorio/; se conservan rutas internas de subpaquetes y objetos.','LEEME raíz se reemplaza como guía editorial; fuentes canónicas conservadas.','Se añaden editorial/ y manifest.json local; no se duplican paquetes históricos fuera de la base curada.'],'exclusiones':['Prompts de desarrollo de entrevistas no incluidos.','No originales de otras conversaciones o paquetes de todas las etapas fuera de la base curada.','No audio, firmas o fechas reconstruidas.','No copia de trazabilidad/control externos dentro de raíz inventariada.'],'instrucciones_verificacion':['Conservar los cuatro archivos externos y extraer ZIP a su lado.','Cotejar manifest.json contra bytes y SHA-256 de cada ruta, salvo manifest mismo.','Ejecutar validar_reporte.py con raíz original REP01_insumos_v1, manuscrito/trazabilidad y --repositorio.','Consultar controles complementarios para literalidad, objetos, vínculos y navegación editorial.'],'limites':['Los scripts históricos pueden requerir entradas/rutas no incluidas; no regeneración idéntica garantizada.','La navegación de objetos se resuelve desde la raíz del subpaquete correspondiente, no desde raíz global.','El control de enlaces de lectura editorial no convierte rutas históricas dentro de prompts en enlaces operativos actuales.']},
'incidencias':incs,
'pendientes_maquetacion':['Producir Word/PDF después de cotejo editorial, conservar separación exacta de cuerpo.','Contar páginas reales del cuerpo: máximo diez; portada, referencias, anexos y nota ampliada fuera.','Revisar tipografía, tablas, figuras al ancho indicado, saltos y legibilidad sin reducir letra artificialmente.','Resolver imágenes/enlaces al extraer ZIP y comprobar navegación del documento final.'],
'limites':['Sin revisión humana independiente, concordancia, saturación o conformidad JANUS/FAIR integral.','Diez páginas PENDIENTE_MAQUETACION, sin sustituirlas por palabras.','Testimonios y terceros relatados no verifican hechos externos; corpus generado con IA declarado.','D01 no demuestra divergencias ni aplicabilidad formal a cinco episodios.','Prioridad local, aceptación, permisos, licencias y factibilidad de productos distintos; no implementación.']}

# Guía humana y navegación inversa, con granularidad de párrafo y objeto.
guide='# Guía del manuscrito a la evidencia\n\nManuscrito externo: `../../..` desde esta carpeta conduce a REP01_repositorio; el reporte está a su lado. Para volver, abrir `../../../REP01_reporte_v1.md` desde la raíz editorial/registros requiere un nivel adicional: use la ruta exacta `../../../../REP01_reporte_v1.md` solo si su contenedor agrega una carpeta. En la distribución estándar la ruta es `../../../REP01_reporte_v1.md` desde registros.\n\n'
# Ruta calculada desde registros: registros -> editorial -> repo -> entrega, tres ..
guide='# Guía del manuscrito a la evidencia\n\nAbrir [manuscrito externo](../../../REP01_reporte_v1.md) junto a la carpeta extraída. Las rutas de la tabla se expresan desde la raíz REP01_repositorio; los enlaces se ajustan desde esta guía.\n\n| Sección/ancla | Función | Lectura principal |\n|---|---|---|\n'
for s in sections:
 link=s['soportes'][0]
 guide+=f"| {s['id']} / {s['ancla']} | {s['funcion_argumental']} | [{link}](../../{link}) |\n"
(P/'editorial/registros/guia_por_seccion.md').write_text(guide)
invindex={}
for pid in canon:invindex[pid]={'citas_reporte':[],'afirmaciones_reporte':[],'necesidades':[],'historias':[],'productos':[]}
for q in citas:invindex[q['parrafo']]['citas_reporte'].append({'id':q['id'],'seccion':q['seccion']})
for a in af:
 for pid in a['objetos_fuente']:
  if pid in invindex:invindex[pid]['afirmaciones_reporte'].append(a['id'])
evidence={x['id']:x for x in d['N']['evidencias']}
for n in d['N']['necesidades']:
 for eid in n['evidencias']+n.get('evidencia_que_limita',[]):
  ev=evidence[eid]
  # El esquema usa parrafo_id como localizador canónico.
  pid=ev.get('parrafo_id',ev.get('parrafo',ev.get('referencia')))
  if pid in invindex and n['id'] not in invindex[pid]['necesidades']:invindex[pid]['necesidades'].append(n['id'])
for pid,item in invindex.items():
 item['historias']=[x['id']for x in d['H']['historias']if set(x['necesidades'])&set(item['necesidades'])]
 item['productos']=[x['id']for x in d['T']['productos']if set(x['historias'])&set(item['historias'])]
dump(P/'editorial/registros/indice_inverso.json',{'alcance':'Todos los párrafos canónicos, incluidos contextuales/administrativos sin necesidad. Enlaces por evidencias N01; relaciones derivadas no son pruebas independientes.','rutas_fuente':{f'E0{i}':f'corpus/E0{i}/E0{i}_texto_con_localizadores.txt'for i in range(1,6)},'parrafos':invindex})
dump(P/'editorial/registros/cobertura_requisitos.json',coverage)
dump(O/'REP01_trazabilidad_v1.json',j)
print('Trazabilidad preparada:',len(sections),'secciones,',len(citas),'citas,',len(af),'afirmaciones,',len(coverage),'requisitos; páginas estimadas',sum(pages))
