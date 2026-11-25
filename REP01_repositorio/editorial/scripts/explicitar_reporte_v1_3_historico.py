from pathlib import Path
import json,shutil,subprocess,re,hashlib
ROOT=Path.cwd();OLD=ROOT/'output/REP01_entrega_v1_2';W=ROOT/'tmp/review/REP01_revision_v1_3';W.mkdir(exist_ok=True)
R=W/'REP01_repositorio';shutil.copytree(OLD/'REP01_repositorio',R,dirs_exist_ok=True);E=R/'editorial/revision_v1_3';E.mkdir(exist_ok=True)
s=(OLD/'REP01_reporte_v1_2.md').read_text().replace('Reporte individual · Versión 1.2','Reporte individual · Versión 1.3')
def rep(a,b):
 global s
 assert a in s,a[:90];s=s.replace(a,b,1)
def before(a,b):rep(a,b+'\n\n'+a)
rep('No acredita actualizar todas las bases; la figura 1 sitúa la decisión.','No acredita actualizar todas las bases; la figura 2 sitúa la decisión.')
rep('![Figura 1. Reconstrucción sintética','![Figura 2. Reconstrucción sintética')
rep('*Figura 1. Flechas de recorrido','*Figura 2. Flechas de recorrido')
before('La técnica explica:', '''Utilizo una **adaptación de JANUS**: el marco enlaza preparación de fuentes, codificación, síntesis, revisión de afirmaciones, redacción y empaquetado con procedencia (Feged Rivadeneira, 2025, Métodos). En este ejercicio se conservan versiones, segmentos y vínculos entre afirmaciones y respaldos. La comparación de interpretaciones y los controles documentales son asistidos; siguen pendientes la revisión humana independiente y el empaquetado interoperable completo. Citar el método no acredita haber superado todas sus puertas de calidad.

![Figura 1. Relaciones entre evidencia, necesidades y productos en el desarrollo del reporte.](REP01_repositorio/editorial/revision_v1_3/relacion_evidencia_diseno.png)

*Figura 1. Adaptación del esquema de las especificaciones integrales, sección 8. Las flechas muestran relaciones analíticas, no un orden rígido de ejecución; las pruebas de productos permanecen propuestas. Los vínculos deben poder recorrerse también desde el diseño hasta sus fuentes.*''')
# El mapa de actores ocupa el lugar de una descripción repetida; se preservan los ámbitos y la tabla.
rep('Poder significa capacidad relativa para condicionar una decisión; interés, lo que está en juego en ella; posición, una postura expresada sobre un cambio concreto. La técnica decide la revisión entregada y tiene interés en que se entienda; eso no le da autoridad sobre las visitas. En investigación, quienes comparten experiencias controlan su participación, mientras el equipo responde por la interpretación. La coordinadora no compromete sola salón, mediadora y programación. En la mercería, ambas personas sostienen atención autónoma; el proveedor condiciona oferta y presentación, pero no decide el surtido.', '''Poder es capacidad relativa para condicionar una decisión; interés, lo que está en juego; posición, una postura expresada sobre un cambio concreto. La figura 3 distingue quién solicita, quién revisa, quién aclara y quién decide sobre la copia, sin atribuir una autoridad institucional general.

![Figura 3. Mapa de actores y circulación de información en la revisión territorial.](REP01_repositorio/editorial/revision_v1_3/mapa_actores_territorial.png)

*Figura 3. Subred del mapa ampliado: técnica, solicitante, equipo del recorrido y compañera. Flecha continua: acción propia declarada; discontinua: intervención de terceros relatada por E01, sin voz independiente. Fuentes: ACT01-R001–R005. Las redes de los otros cuatro casos y las documentales se conservan en el soporte.*''')
rep('Sus ámbitos abarcan los cinco episodios, gestión pública de datos, homologación como escenario, incorporación y estudios PAOT, norma de metadatos, consulta territorial y prototipo institucional. La Subdirección de Estudios y Reportes de Ordenamiento Territorial y el Líder Coordinador de Proyectos de Estudios de Ordenamiento Territorial aparecen por el manual PAOT, sin atribuir esos puestos a la técnica entrevistada.','Incluye los cinco episodios, datos públicos, homologación, incorporación y estudios PAOT, metadatos, consulta y prototipo. Los puestos PAOT proceden de su manual, sin atribuirlos a la técnica entrevistada.')
rep('Análogamente, comparar otra ocasión beneficiaría al análisis universitario y podría exigir esfuerzo a quien comparte su experiencia. Su disposición no fue recabada. En el escenario de homologación, **no se recabaron posturas de los actores**: entusiasmo por una carpeta no equivale a apoyo a centralizar. Tampoco corresponde ubicar actores en un cuadrante global de poder e interés. El [mapa ampliado](REP01_repositorio/76_actores_y_preferencias_v1_1.md) conserva ámbitos, ganancias, cargas y condiciones de las tres hipótesis de coordinación.','Comparar otra ocasión también podría trasladar esfuerzo a quien comparte su experiencia; su disposición no fue recabada. Frente a homologación, **no se recabaron posturas**: preferir mejores notas no equivale a apoyar centralización ni justifica un cuadrante global. El [mapa ampliado](REP01_repositorio/76_actores_y_preferencias_v1_1.md) conserva ámbitos, relaciones y tres hipótesis condicionales de coordinación.')
# Tabla de ideales más compacta; mismas cinco necesidades y decisiones, sin retirar evidencia.
a=s.index('| Perfil y necesidad ideal |');b=s.index('*Tabla 5.',a)
s=s[:a]+'''| Perfil y necesidad ideal | Información actual y requerida | Comprobación futura |
|---|---|---|
| Técnica; último cambio | Algunas notas bastan; requiere motivo, respaldo, revisión y duda. | Explicar la revisión y decidir usar o consultar. |
| Investigadora; otra ocasión | Una salida detallada; requiere otra comparable con procedencia. | Precisar o reducir la afirmación y decidir si seguir aporta. |
| Coordinadora; acuerdos | Notas, mensajes y calendario bastaron; requiere qué retomar y revalidar. | Distinguir confirmado, posible y pendiente al relevar. |
| Mercería; desempeño | Referencia y tacto; requiere pruebas atribuidas de cosido, uso o lavado. | Justificar probar o dejar una alternativa. |
| Salida personal; conversación | Resolvió en destino; desea notas con fuente y ocasión. | Recuperar una razón y comprobarla al llegar. |

'''+s[b:]
rep('![Figura 2. Arquitectura propuesta con agregación opcional y retorno de incidencias.](REP01_repositorio/editorial/figuras/REP01-F003.png)\n\n*Figura 2. La rama directa conserva análisis por caso. El retorno expresa revisión propuesta del contrato o insumo; no una corrección automática de fuentes.*','La [arquitectura gráfica del producto](REP01_repositorio/editorial/figuras/REP01-F003.svg) conserva agregación opcional y retorno de incidencias. Es distinta de la figura 1, que explica cómo este reporte fundamenta el diseño.')
# FAIR y FDO: resultados reales existentes y límites formales, no registro externo ficticio.
before('La operación propuesta recibe identificador', '''**Representación digital de la historia.** El registro HU01-OD037 describe la historia HU01-H003, versión 1.0, mediante su [objeto estructurado JSON](REP01_repositorio/analisis/historias/HU01/soportes_revisados_v1_1/objetos/historias/HU01-H003.json). Enlaza la necesidad N01-N004, el perfil HU01-P001 y los metadatos HU01-M003; conserva procedencia, huella y acceso. Forma parte de 76 objetos locales. Es un prototipo orientado a **FAIR Digital Objects (FDO)**: carece de identificador persistente, tipo y perfil registrados, por lo que no se presenta como FDO plenamente implementado (FDO Forum, s. f.).''')
rep('La trazabilidad hace discutible esa interpretación. Identificadores, objetos locales, versiones, relaciones y huellas permiten localizar y cotejar; no certifican verdad ni conformidad FAIR. Localización, acceso, interoperabilidad y reutilización requieren también identificadores persistentes, registros externos, permisos, licencias y semántica compartida (GO FAIR Foundation, s. f.). El corpus no adquiere licencia abierta por acompañar código MIT. La adaptación de JANUS organiza afirmaciones y evidencia y conserva decisiones, sin certificar revisión integral, saturación o concordancia (Feged Rivadeneira, 2025).', '''Aplico los **principios FAIR** como orientación: **localización**, mediante identificadores y catálogo; **accesibilidad**, mediante rutas y condiciones de consulta; **interoperabilidad**, mediante campos y relaciones explícitos; y **reutilización**, mediante versiones, procedencia y límites. El cumplimiento es parcial: faltan persistencia y registro externo, semántica compartida y acuerdos de derechos; el corpus no hereda la licencia MIT del código (GO FAIR Foundation, s. f.). La [matriz por principio y la ficha del objeto](REP01_repositorio/editorial/revision_v1_3/fair_fdo_y_janus.md) distinguen evidencia disponible y pendientes. FAIR es un conjunto de principios, no una certificación obtenida por guardar JSON.''')
rep('La revisión aplica JANUS como organización de evidencia, control de afirmaciones y registro de límites. No incorpora retroactivamente dos revisores, concordancia ni registros de prompts inexistentes. Los objetos locales de necesidad, perfil e historia ya enlazan datos y metadatos; su ficha humana y JSON corresponden a la misma versión. La [matriz FAIR y los controles](REP01_repositorio/editorial/revision_v1_2/fair_janus_y_controles.md) distinguen localización y relaciones comprobables de persistencia, permisos y revisión humana pendientes. Esta separación permite avanzar con una decisión verificable sin confundir especificación con operación.','Las limitaciones de JANUS permanecen explícitas: no se acreditan dos revisores humanos, concordancia ni parámetros de generación desconocidos. RO-Crate, PROV-O, DataCite y nanopublicaciones no están implementados. La ficha humana y el JSON permiten revisar un objeto concreto; completar su registro y validación requiere trabajo posterior, sin modificar retrospectivamente el corpus.')
rep('- GO FAIR Foundation.','- FDO Forum. (s. f.). *FAIR Data What is an FDO?* [Descripción](https://fairdo.org/about/what_is_an_fdo/), apartados An FDO is y What are Core FDOs. Consulta: 25 de noviembre de 2026. Referencia para delimitar los prototipos locales; no acredita su registro.\n- GO FAIR Foundation.')
rep('[registro de cambios de esta revisión](REP01_repositorio/editorial/revision_v1_2/LEEME.md)','[registro de cambios de esta revisión](REP01_repositorio/editorial/revision_v1_3/LEEME.md)')
(W/'REP01_reporte_v1_3.md').write_text(s)
# Esquema adaptado de la imagen adjunta; dibujo exacto con Graphviz, sin generación de imagen.
flow='''digraph G {
graph[rankdir=TB,bgcolor="white",pad=.15,nodesep=.3,ranksep=.26];
node[shape=box,style="rounded,filled",fillcolor="#f3f6f8",color="#607587",fontname="Liberation Sans",fontsize=12,margin=".10,.07"];
edge[color="#52697b",arrowsize=.65,fontname="Liberation Sans",fontsize=10];
a[label="Fuentes y segmentos\\nProcedencia y versión"];
b[label="Actores y perfiles"];c[label="Procesos y decisiones"];d[label="Códigos y temas"];
e[label="Necesidades verificables\\nActuales y deseadas",fillcolor="#e3eef1"];
f[label="Historias de usuario\\nCapacidad y propósito"];
g[label="Información y metadatos"];h[label="Operaciones y métodos"];
i[label="Tres candidatos\\nAlcance y criterios propuestos",fillcolor="#e3eef1"];
j[label="Pruebas futuras y revisión\\nEvidencia por obtener"];
{rank=same;b;c;d;}{rank=same;g;h;}
a->b;a->c;a->d;b->e;c->e;d->e;e->f;f->g;f->h;g->i;h->i;i->j;
j:e->e:e[style=dashed,label="revisar",constraint=false];
}'''
(E/'relacion_evidencia_diseno.dot').write_text(flow)
# Subred heredada, simplificada para el cuerpo; sus relaciones no se convierten en observación directa.
actor='''digraph G {
graph[rankdir=LR,bgcolor="white",pad=.12,nodesep=.22,ranksep=.60];
node[shape=box,style="rounded,filled",fillcolor="#f3f6f8",color="#607587",fontname="Liberation Sans",fontsize=12,margin=".11,.08"];
edge[color="#52697b",fontname="Liberation Sans",fontsize=10,arrowsize=.65];
t[label="Técnica de registros\\nDecide su copia"];
s[label="Solicitante\\nDelimita y media"];
r[label="Equipo del recorrido\\nAporta aclaración"];
c[label="Compañera\\nContrasta antecedentes"];
{rank=same;t;c;}
s->t[label="Petición",style=dashed];t->s[label="Pregunta y devolución"];
s->r[label="Consulta",style=dashed];r->s[label="Aclaración",style=dashed];c->t[label="Otra lectura",style=dashed];
}'''
(E/'mapa_actores_territorial.dot').write_text(actor)
for stem in ['relacion_evidencia_diseno','mapa_actores_territorial']:
 for fmt in ['png','svg']:subprocess.run(['dot','-T'+fmt,'-Gdpi=240',str(E/(stem+'.dot')),'-o',str(E/(stem+'.'+fmt))],check=True)
# Copia controlada de la imagen usada como referencia, sin editar sus píxeles.
shutil.copy2(ROOT/'upload/image(20261125-193833).png',E/'esquema_fuente_usuario.png')
# Maquetador derivado, con mismos tipos y dimensiones; el cuerpo se verifica por PDF.
fmt=(ROOT/'tmp/review/maquetar_REP01_v1_2.py').read_text().replace('REP01_revision_v1_2','REP01_revision_v1_3').replace('REP01_reporte_v1_2.md','REP01_reporte_v1_3.md')
fmt=fmt.replace("width=6.65 if 'F001'in target or 'F002'in target else 4.6","width=5.55 if 'relacion_evidencia' in target else 6.65")
(ROOT/'tmp/review/maquetar_REP01_v1_3.py').write_text(fmt)
print('Palabras cuerpo',len(s.split('<!-- CUERPO_INICIO -->')[1].split('<!-- CUERPO_FIN -->')[0].split()))
