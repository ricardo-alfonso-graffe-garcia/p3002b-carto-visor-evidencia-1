# Guía del snapshot público GeoInsights

Repositorio de autores: https://github.com/data-lama/covid_geoinsights_pipeline. Commit ab60b86a6a87bca0dd370c7c4af3ada4185d187e, recuperado 25 noviembre 2026. No se afirma identidad con ZIP original del curso. Datos externos y ejecución no incluidos. Licencia de código MIT, DataLama Team 2020–2021; no licencia del corpus, datos externos o productos futuros. No ejecutar scripts ni instalar dependencias históricas.

Después de descomprimir GeoInsights_snapshot.zip de forma segura, leer README completo y LICENSE; el código queda dentro de covid_geoinsights_pipeline-ab60b86a6a87bca0dd370c7c4af3ada4185d187e/.

La preparación inspeccionó estáticamente las secciones de arquitectura del README, LICENSE, el orquestador pipeline_scripts/excecute_all.py y configuración selected_excecutions.csv. Consultó cabeceras y fragmentos iniciales de generic_unifier_class.py, universal_generic_unifier.py, agregadores geometry/radius/community, constructor daily_graphs, tda_script.R y requirements_excecution.txt. No se acredita lectura completa de todos esos archivos o ejecución del pipeline.

T01 debe ampliar y localizar la lectura necesaria para sus afirmaciones. El orquestador distingue PRE, seis etapas por localización y POS. GenericUnifier crea árboles raw/unified/agglomerated/constructed; no los crea en este ejercicio. La unificación de casos en universal_generic_unifier.py contiene DEBUG y un DataFrame temporal en lugar de la llamada comentada build_cases_geo. Debe revisarse antes de inferir un funcionamiento. tda_script.R remite a un mapper_dir externo y carga módulos ajenos si existen. Las dependencias fijadas son históricas y su compatibilidad no está probada. README mantiene cita del artículo pendiente.

Esas observaciones acotan qué se puede tomar como patrón de adaptación. No equivalen a auditoría completa de seguridad, conformidad o funcionamiento, ni justifican resultados para CDMX. No reproducir claves/configuración sensible en la explicación.
