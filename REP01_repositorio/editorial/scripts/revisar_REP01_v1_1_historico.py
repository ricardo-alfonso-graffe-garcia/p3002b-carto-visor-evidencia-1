from pathlib import Path
import json,re,hashlib,shutil,collections,datetime

ROOT=Path.cwd(); WORK=ROOT/'tmp/review/REP01_revision_v1_1'; REPO=WORK/'REP01_repositorio'
def dump(p,v):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
src=ROOT/'upload/REP01_reporte_v1(1).md';md=src.read_text()
j=json.loads((ROOT/'upload/REP01_trazabilidad_v1(1).json').read_text())
edits=[]
def replace(old,new,label):
    global md
    assert old in md,label
    md=md.replace(old,new,1);edits.append(label)

replace('# Decidir con información suficiente: alcances de la homologación territorial ante cinco relatos situados',
        '# Procesos actores y necesidades de información territorial en cinco relatos','Título descriptivo')
replace('Manuscrito para revisión editorial · Versión 1.0  \nComprobación efectiva del máximo de diez páginas: **PENDIENTE_MAQUETACION**. Portada, referencias y anexos fuera del cuerpo. Revisión humana independiente pendiente.',
        'Reporte individual · Versión 1.1','Portada sin instrucciones de producción')
replace('Las cinco transcripciones conforman el corpus del ejercicio académico. Lo que sigue distingue relatos, documentación consultada, interpretación y propuestas.',
        'Las cinco transcripciones conforman el corpus del ejercicio académico. Distingo sus relatos de la documentación institucional y de las propuestas que elaboro; los ejemplos permiten examinar decisiones y necesidades, pero no demostrar cómo opera una dependencia concreta. La declaración final precisa el uso de IA y los registros disponibles.',
        'Alcance del ejercicio')
replace('El [libro completo](REP01_repositorio/55_libro_comun_v1_3.md), las [recodificaciones](REP01_repositorio/analisis/recodificacion/LEEME.md) y el [registro del corpus](REP01_repositorio/24_registro_corpus.json) permiten revisar el recorrido. Las fechas de entrevista no están consignadas. Los acuerdos verbales están contenidos en los diálogos; no acreditan grabaciones disponibles ni consentimientos firmados.',
        'El [libro completo](REP01_repositorio/55_libro_comun_v1_3.md), las [recodificaciones](REP01_repositorio/analisis/recodificacion/LEEME.md) y el [registro del corpus](REP01_repositorio/24_registro_corpus.json) permiten revisar ese recorrido y consultar los metadatos efectivamente conservados.',
        'Concentración del alcance administrativo en nota final')
replace('La revisión D01 identifica **cero fuentes formales directamente atribuibles a los cinco episodios y cero divergencias formalmente demostradas**.',
        'El contraste documental identifica **cero fuentes formales directamente atribuibles a los cinco episodios y cero divergencias formalmente demostradas**.',
        'Conceptos completos antes de identificadores')
doc_table='''
| Modelo documental | Qué permite examinar | Correspondencia que falta |
|---|---|---|
| Política de datos abiertos de 2020 | Preparación, publicación y vías de actualización; responsabilidades de entes públicos y ADIP. | Vincular un episodio con publicación abierta, conjunto, periodo y regla aplicable. |
| Manual de estudios territoriales de PAOT | Atribuciones de supervisión, procesamiento espacial y elaboración cartográfica. | Acreditar dependencia y procedimiento; la técnica refiere una alcaldía sin identificar. |
| Documentación de SIGCDMX | Relaciones entre unidades, datos y representaciones de consulta. | Comprobar archivos, correspondencias y uso; describir datos no documenta su producción. |
| Incorporación al SIG-PAOT | Condiciones normativas mínimas para incorporar información. | Determinar aplicación y operación concreta; la norma no prueba cumplimiento. |

*Tabla 3. Alcance de los cuatro modelos documentales. Fuentes y diagramas: contraste documental, modelos D01-M001 a D01-M004. Las diferencias de ámbito no se clasifican como incumplimientos.*
'''
anchor='Los [mapas completos](REP01_repositorio/67_procesos_descritos_v1_1.md) y el [contraste documental](REP01_repositorio/72_contraste_documental_v1_1.md) muestran qué evidencia permitiría hacerlo.'
replace(anchor,anchor+'\n'+doc_table,'Síntesis del contraste documental')
replace('En el escenario de homologación, las posiciones permanecen **NO_RECABADA**:',
        'En el escenario de homologación, **no se recabaron posturas de los actores**:',
        'Estado de posición explicado en prosa')
actor_table='''
| Actor y ámbito de decisión | Poder e interés en ese ámbito | Preferencia y posibles consecuencias de un apoyo común |
|---|---|---|
| Técnica de registros; revisión entregada | Poder alto para decidir su copia; interés alto en referencias comprensibles. | Conservar contraste y consulta. Ganaría una explicación recuperable; cargas adicionales no determinadas. |
| Investigadora; comparación y escritura | Poder alto con su colega sobre el análisis; interés alto en sostener afirmaciones. | Comparar otra ocasión. Ganaría precisión; una estructura uniforme podría borrar diferencias entre observar y narrar. |
| Coordinadora; serie cultural | Poder medio: depende de espacio, mediadora y programación; interés alto en continuidad. | Retomar acuerdos y confirmar con anfitriones. Ganaría relevo; documentar podría exigir más esfuerzo que ayuda. |
| Responsable de mercería; surtido | Poder alto sobre reposición, sin controlar oferta; interés alto en explorar cantidades justificables. | Conservar muestra y prueba atribuida. Ganaría comparación; registrar todos los artículos añadiría trabajo. |
| Persona que propone la salida; propuesta propia | Poder alto sobre su propuesta, con encuentro acordado; interés alto en convivencia. | Guardar notas breves. Ganaría memoria útil; llenar fichas en cada visita sería una carga. |

*Tabla 4. Síntesis de cinco actores entrevistados; capacidades declaradas y consecuencias analíticas condicionales. El mapa ampliado conserva los 46 actores, incluidos terceros y unidades documentales. Ámbitos y evidencias: ACT01-A001, A005, A012, A019 y A024.*
'''
anchor='El [mapa ampliado](REP01_repositorio/76_actores_y_preferencias_v1_1.md) conserva ámbitos, ganancias, cargas y condiciones de las tres hipótesis de coordinación.'
replace(anchor,anchor+'\n'+actor_table,'Síntesis comparativa de actores')
needs_table='''
| Perfil y necesidad ideal | Información disponible y requerida | Decisión y comprobación futura |
|---|---|---|
| Técnica; explicación del último cambio | Hay notas útiles, pero otras son escuetas; requiere cambio, motivo, respaldo y revisión. | Usar o volver a consultar. Comprobar si otra persona explica la revisión y la duda abierta. |
| Investigadora; segunda ocasión | Hay una salida detallada y recuerdos de otras; requiere otra ocasión comparable y su procedencia. | Precisar una afirmación o justificar seguimiento. Examinar si el contraste cambia su alcance. |
| Coordinadora; acuerdos recuperables | Notas, mensajes y calendario bastaron; requiere interlocución, acuerdos y qué confirmar al retomar. | Preparar otro acercamiento. Comprobar si alguien distingue lo sabido de lo que debe revalidar. |
| Mercería; desempeño de materiales | Hay referencia, tacto y estiramiento; requiere pruebas atribuidas de cosido, uso o lavado. | Probar o dejar una alternativa. Justificar la decisión con comportamiento y contexto de prueba. |
| Salida personal; opción para conversar | La salida se resolvió en destino; desea observaciones breves con fuente y ocasión. | Proponer o descartar un lugar. Recuperar una razón y comprobar condiciones al llegar. |

*Tabla 5. Cinco ejemplos del inventario de 29 necesidades (N01-N004, N009, N016, N023 y N029). Todos tienen prioridad alta dentro de su propia actividad; no constituyen un ranking entre perfiles. Son deseos ideales y comprobaciones propuestas, todavía no ejecutadas.*
'''
anchor='Las 21 historias son elaboraciones analíticas de cinco perfiles funcionales, con 28 criterios y 90 operaciones propuestas; no requisitos aprobados.'
replace(anchor,anchor+'\n'+needs_table,'Necesidades comparables y verificables por perfil')
replace('Los casos aportan problemas acotados que requieren explicación:',
        'Los relatos plantean cuestiones acotadas que requieren explicación:',
        'Problemas del corpus sin atribución de hallazgo empírico')
replace('T01 decide no usar todavía escaneo, potencia/escalamiento ni agentes en los productos básicos.',
        'Por estas condiciones, no propongo todavía escaneo, potencia/escalamiento ni agentes en los productos básicos.',
        'Decisión analítica expresada por el autor')
replace('La maquetación deberá verificar legibilidad, enlaces y máximo efectivo de diez páginas del cuerpo, todavía pendiente. Mantener esos límites forma parte del resultado académico, porque impide que un soporte ordenado se confunda con evidencia que aún no existe.',
        'El siguiente paso de diseño consiste en contrastar esas condiciones con las personas que asumirían cada decisión y el mantenimiento del apoyo. Esa comprobación determinará si conviene integrar información, mejorar un documento existente o conservar una práctica que ya resulta suficiente.',
        'Conclusión académica separada de maquetación')
start=md.index('## Declaración ampliada de uso de IA y alcance documental')
end=md.index('<!-- DECLARACION_IA_FIN -->',start)
md=md[:start]+'''## Declaración de uso de IA y registros del ejercicio

Se utilizó asistencia de modelos de lenguaje para construir y revisar las transcripciones, esquema de códigos, recodificar, sintetizar y relacionar procesos, actores, necesidades e historias. El manuscrito y sus soportes se integraron y revisaron con asistencia de Codex, descrito por el entorno como basado en GPT-6, y controles programáticos de citas, relaciones, integridad y navegación. No consta un identificador verificable de ejecución ni sus parámetros; se registran como desconocidos. Los textos canónicos se conservaron.

Se utilizó asistencia de modelos de lenguaje para construir y revisar el esquema de códigos, recodificar, sintetizar y relacionar procesos, actores, necesidades e historias. El manuscrito y sus soportes se integraron y revisaron con asistencia de Codex, descrito por el entorno como basado en GPT-6, y controles programáticos de citas, relaciones, integridad y navegación. No consta un identificador verificable de ejecución ni sus parámetros; se registran como desconocidos. Los textos canónicos se conservaron.

La revisión documentada es asistida; la revisión humana independiente permanece pendiente. No se calcularon concordancia ni saturación, y las propuestas de utilidad no se probaron con participantes. La adaptación de JANUS se limita a organización, trazabilidad y revisión; no acredita conformidad integral. Los registros y prompts de análisis disponibles acompañan el repositorio; no se reconstruyeron exportaciones completas de conversaciones. El [registro de incidencias](REP01_repositorio/editorial/registros/incidencias_metodologicas.md) y el [cierre editorial](REP01_repositorio/editorial/registros/revision_coordinacion_v1_1.md) precisan los alcances.

'''+md[end:]
edits.append('Declaración breve de usos de IA y registros disponibles')
# Rótulos de tablas y títulos claros, con anclas estables.
md=md.replace('## 1. ','## 1 ').replace('## 2. ','## 2 ').replace('## 3. ','## 3 ').replace('## 4. ','## 4 ').replace('## 5. ','## 5 ').replace('## 6. ','## 6 ').replace('## 7. ','## 7 ').replace('## 8. ','## 8 ').replace('## 9. ','## 9 ')
md=md.replace('El [libro completo]', '*Tabla 1. Ejemplos del esquema de códigos; el libro común conserva las definiciones completas, reglas y fronteras.*\n\nEl [libro completo]',1)
md=md.replace('En investigación, formular, observar, comparar y escribir se superponen.', '*Tabla 2. Síntesis de los cinco procesos relatados; los mapas completos conservan decisiones, responsables y retornos.*\n\nEn investigación, formular, observar,comparar y escribir se superponen.',1).replace('observar,comparar','observar, comparar')
(WORK/'REP01_reporte_v1_1.md').write_text(md)
j['metadatos'].update(version='1.1',estado='REVISION_COORDINACION',paginacion_estado='PENDIENTE_MAQUETACION')
j['metadatos']['alcance_corpus']='Cinco transcripciones conforman el corpus del ejercicio.'
for s in j['secciones']:
    a=s['ancla'];part=md.split('<a id="'+a+'"></a>')[1].split('<a id=')[0].split('<!-- CUERPO_FIN -->')[0]
    s['titulo']=re.search(r'^## (.+)$',part,re.M).group(1)
    s['palabras_estimadas']=len(re.findall(r'\b[\wÁÉÍÓÚÑáéíóúñ]+\b',part));s['paginas_estimadas']=None
j['tesis_y_estructura']['paginas_totales_presupuestadas']=None
j['tesis_y_estructura']['decisiones_editoriales']+=edits
j['lectura_entradas'].append({'archivo':'Coordinación REP01 v1.1','alcance':'Lectura del manuscrito y trazabilidad; contraste de citas y contexto cercano, cuatro modelos documentales, cinco actores seleccionados y cinco necesidades ideales; inspección visual de tres figuras.','comprobacion':'Validador original repetido sin errores sobre el ZIP real; fuentes canónicas preservadas y cambios editoriales registrados.'})
prov={'id':'MET-PROCEDENCIA-REP01','tipo':'REGISTRO_DE_COORDINACION','fuente':'Comunicación expresa del estudiante en esta conversación e instrucciones REP01 disponibles.','declaracion':'5 transcripciones','aprobacion_documental_adjunta':False,'alcance':'Registra la autorización informada por el estudiante; no sustituye un documento docente ni prueba identidad, campo o grabaciones.','registros':'Fechas no consignadas; aperturas y acuerdos contenidos en el corpus; acuerdos de participación conservados.','modelo_y_parametros':None}
dump(REPO/'editorial/registros/procedencia_REP01.json',prov)
for a in j['afirmaciones']:
    if a['id']=='REP01-A002':
        a.update(enunciado='El corpus del ejercicio reúne cinco transcripciones.',objetos_fuente=['MET-PROCEDENCIA-REP01'],soporte='editorial/registros/procedencia_REP01.json',localizador='declaracion y alcance',limite=prov['alcance'])
    if a['id']=='REP01-A005':
        a['soporte']='editorial/controles/conteos_y_fuentes_v1_1.json';a['localizador']='libro y recodificacion: cardinalidades calculadas de colecciones preferidas'
    if a['id']=='REP01-A008':a['localizador']='actores: 46 elementos; ambitos: 12 elementos; posicion_homologacion por actor'
    if a['id']=='REP01-A013':
        a['soporte']='editorial/controles/conteos_y_fuentes_v1_1.json';a['localizador']='necesidades e historias: cardinalidades y condicion_sin_historia'
j['afirmaciones'] += [
 {'id':'REP01-A030','seccion':'REP01-S004','enunciado':'Las capacidades de decisión y las consecuencias posibles de un apoyo común difieren entre los cinco actores entrevistados.','tipo':'INTERPRETACION','objetos_fuente':['ACT01-A001','ACT01-A005','ACT01-A012','ACT01-A019','ACT01-A024'],'soporte':'76_actores_y_preferencias_v1_1.json','localizador':'actores: poder, interes, preferencias, ganancias_y_perdidas; tabla 4','limite':'Ámbitos locales declarados y consecuencias condicionales; postura sobre homologación no recabada.'},
 {'id':'REP01-A031','seccion':'REP01-S003','enunciado':'Los cuatro modelos documentales describen publicación, atribuciones, relaciones de datos y condiciones normativas, con correspondencias distintas pendientes respecto a los episodios.','tipo':'DOCUMENTAL','objetos_fuente':['D01-M001','D01-M002','D01-M003','D01-M004'],'soporte':'72_contraste_documental_v1_1.json','localizador':'modelos_documentales: ambito, alcance, limites; tabla 3','limite':'No se demuestra una divergencia de cumplimiento ni un proceso oficial atribuible a cada entrevista.'},
 {'id':'REP01-A032','seccion':'REP01-S005','enunciado':'Cinco necesidades ideales ilustran decisiones y comprobaciones futuras, con prioridad alta dentro de actividades separadas.','tipo':'PROPUESTA','objetos_fuente':['N01-N004','N01-N009','N01-N016','N01-N023','N01-N029'],'soporte':'82_necesidades_v1_1.json','localizador':'necesidades: informacion_actual, decision, prioridad y verificacion; tabla 5','limite':'Muestra ilustrativa, no seis ideales completos ni ranking entre perfiles; verificaciones no ejecutadas.'}
]
book=json.loads((REPO/'55_libro_comun_v1_3.json').read_text());recs=[]
for i in range(1,6):
    f=next((REPO/f'analisis/recodificacion/R0{i}').glob('*.json'));d=json.loads(f.read_text());recs.append({'archivo':str(f.relative_to(REPO)),'version':d['metadatos']['resultado_version'],'parrafos':len(d['cobertura']),'fragmentos':len(d['segmentos']),'asignaciones':sum(len(s['codigos'])for s in d['segmentos']),'sha256':sha(f)})
n=json.loads((REPO/'82_necesidades_v1_1.json').read_text());h=json.loads((REPO/'88_historias_y_objetos_v1_1.json').read_text())
counts={'libro':{'archivo':'55_libro_comun_v1_3.json','codigos':len(book['codigos_comunes']),'ejemplos':sum(len(c['ejemplos'])for c in book['codigos_comunes']),'sha256':sha(REPO/'55_libro_comun_v1_3.json')},'recodificacion':{'archivos':recs,'parrafos':sum(r['parrafos']for r in recs),'fragmentos':sum(r['fragmentos']for r in recs),'asignaciones':sum(r['asignaciones']for r in recs)},'necesidades':{'archivo':'82_necesidades_v1_1.json','total':len(n['necesidades']),'deseos_ideales':sum(x['tipo']=='DESEO_IDEAL'for x in n['necesidades'])},'historias':{'archivo':'88_historias_y_objetos_v1_1.json','total':len(h['historias'])},'condicion_sin_historia':'N01-N005','alcance':'Conteos de fuentes preferidas, sin equiparar frecuencia con importancia o validación.'}
dump(REPO/'editorial/controles/conteos_y_fuentes_v1_1.json',counts)
changes={
 'ALC02':('ATENDIDO_EN_SOPORTE','Cinco transcripciones completas E01–E05 y análisis conservados.','editorial/registros/procedencia_REP01.json'),
 'COD07':('ATENDIDO_EN_SOPORTE','Libro común 1.3 y cinco recodificaciones preferidas conservados; control repetido de 545 párrafos, 713 fragmentos y 971 asignaciones. Pilotaje humano separado y pendiente.','editorial/controles/conteos_y_fuentes_v1_1.json'),
 'FDO02':('ATENDIDO_EN_SOPORTE','Los 76 objetos locales conservan ids, versiones, metadatos y procedencia; el cotejo de payloads y relaciones fue repetido.','88_historias_y_objetos_v1_1.json'),
 'FDO04':('ATENDIDO_EN_MANUSCRITO','La sección 9 distingue acceso con permisos de apertura del contenido; no exige abrir el corpus para satisfacer la distinción.','88_historias_y_objetos_v1_1.json'),
 'FDO05':('ATENDIDO_EN_SOPORTE','Los PID externos permanecen nulos y no se inventan depósitos ni DOI del proyecto.','88_historias_y_objetos_v1_1.json'),
 'FDO06':('ATENDIDO_EN_SOPORTE','El índice inverso y las relaciones de objetos conservan vínculos desde párrafos a necesidades, historias y propuestas.','editorial/registros/indice_inverso.json'),
 'FDO07':('ATENDIDO_EN_MANUSCRITO','La sección 9 limita los hashes a integridad y distingue ese control de la verdad del contenido.','88_historias_y_objetos_v1_1.json'),
 'FDO08':('ATENDIDO_EN_SOPORTE','HU01 evalúa empaquetado y T01 evalúa extensión FAIR/JANUS; la evaluación no requiere implementar RO-Crate para este enunciado.','88_historias_y_objetos_v1_1.json'),
 'FDO09':('ATENDIDO_EN_SOPORTE','Versiones de corpus, libro, recodificaciones, dato/metadato y representaciones se conservan diferenciadas.','88_historias_y_objetos_v1_1.json'),
 'JAN09':('ATENDIDO_EN_MANUSCRITO','La nota metodológica y la conclusión distinguen revisión asistida de revisión humana independiente pendiente; distinguirlas no exige haber completado ambas.','editorial/registros/revision_coordinacion_v1_1.md'),
 'CTX06':('ATENDIDO_EN_SOPORTE','Los paquetes explícitos de análisis A01–A05 y sus primeras lecturas preceden a la síntesis en los registros conservados. No se certifica una configuración histórica no registrada.','24_protocolo_analisis.md'),
 'CTX07':('ATENDIDO_EN_SOPORTE','S01 identifica corpus cerrado y libro común como entradas; se conservan las versiones preferidas sin reiniciar entrevistas.','63_sintesis_transversal_v1_1.json'),
 'CTX08':('ATENDIDO_EN_SOPORTE','La matriz editorial separa 208 requisitos especificados de los estados de ejecución y explica límites por requisito.','editorial/registros/cobertura_requisitos.json'),
 'CTX11':('ATENDIDO_EN_SOPORTE','Revisión asistida efectiva de manuscrito, literalidad/contexto, trazabilidad, figuras y navegación además de controles estructurales.','editorial/registros/revision_coordinacion_v1_1.md'),
 'NAT12':('ATENDIDO_EN_SOPORTE','Comparación binaria de fuentes canónicas y conservación de contraejemplos; no se cambiaron testimonios para sostener la tesis.','editorial/controles/conteos_y_fuentes_v1_1.json'),
}
adjust=[]
for x in j['cobertura_requisitos']:
    if x['requisito']in changes:
        state,proof,support=changes[x['requisito']];adjust.append({'requisito':x['requisito'],'antes':x['estado'],'despues':state,'razon':proof});x['estado']=state;x['evidencia_cumplimiento']=proof
        if support not in x['soportes']:x['soportes'].append(support)
        x['limite']='Estado referido al enunciado concreto; no certifica revisión humana independiente, conformidad FAIR/JANUS integral, configuración histórica ausente o implementación.'
dump(REPO/'editorial/registros/ajustes_cobertura_v1_1.json',adjust)
j['incidencias'].append({'objeto':'Cobertura y narrativa REP01 1.1','descripcion':'Algunos estados parciales exigían condiciones adicionales al enunciado; actores/necesidades/contraste quedaban excesivamente remitidos a soportes.','resolucion':'Estados revisados con pruebas específicas; tres tablas y localizadores de conteos y procedencia. Fuentes canónicas sin cambios.','estado':'RESUELTA'})
j['incidencias'].append({'objeto':'Límite documental persistente','descripcion':'No hay fuente formal directamente atribuible a los cinco episodios; por ello no se demuestran divergencias formales.','resolucion':'Se mantiene el límite y se hace visible la correspondencia pendiente por modelo. No se declara logro Destacado ni se inventan incumplimientos.','estado':'ABIERTA'})
j['pendientes_maquetacion']=['Renderizar Word/PDF y verificar páginas, imágenes y enlaces antes de declarar extensión comprobada.']
j['revision_coordinacion']={'version':'1.1','cambios':edits,'control_original_repetido':'SIN_ERRORES_ESTRUCTURALES','fuentes_canonicas':'PRESERVADAS','revision_humana_independiente':'PENDIENTE'}
dump(WORK/'REP01_trazabilidad_v1_1.json',j)
dump(REPO/'editorial/registros/cobertura_requisitos.json',j['cobertura_requisitos'])
(REPO/'editorial/registros/revision_coordinacion_v1_1.md').write_text('''# Revisión de coordinación REP01 1.1

Recepción completa de cuatro originales; huella y CRC del ZIP coinciden. Validador original repetido sin errores en carpeta real. Se inspeccionaron las tres figuras nuevas y se cotejaron sus fuentes y simplificaciones. La revisión es asistida; no se sustituye una revisión humana independiente.

Se añadieron tablas de correspondencia documental, capacidades/preferencias de cinco actores y cinco necesidades ideales con verificación propuesta. Se conservaron todas las citas y las fuentes canónicas. Los objetos, prioridades e historias no se reescribieron. La procedencia se registra en procedencia_REP01.json.

El registro ajustes_cobertura_v1_1.json explica cada cambio de estado por su enunciado. No se transforman estados en calificación. Los registros administrativos ausentes y la aplicabilidad documental a episodios mantienen sus límites.

Se precisaron localizadores de cifras y procedencia. Los controles de recodificación, libro, necesidades y objetos se repiten sin cambios sustantivos. El cierre de maquetación se registra en un control separado tras producir Word y PDF; no se infiere del conteo de palabras.

La tabla de contraste no demuestra incumplimientos. El criterio de divergencias documentadas continúa limitado por falta de fuentes directamente aplicables a los episodios.
''')
# El cierre posterior actualizará guías, paginación, inventario y controles.
shutil.copy2(Path(__file__),REPO/'editorial/scripts/revisar_REP01_v1_1_historico.py')
print(json.dumps({'version':'1.1','cambios':len(edits),'ajustes_cobertura':len(adjust),'palabras_cuerpo':len(re.findall(r'\b[\wÁÉÍÓÚÑáéíóúñ]+\b',md.split('<!-- CUERPO_INICIO -->')[1].split('<!-- CUERPO_FIN -->')[0]))},ensure_ascii=False))
