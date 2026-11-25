"""Cierra inventario, ejecuta controles y verifica ZIP sin ciclos de huellas."""
from pathlib import Path
import json,hashlib,subprocess,argparse,zipfile,datetime

def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rd(p):return json.loads(p.read_text())
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def main(base,out):
 repo=out/'REP01_repositorio';md=out/'REP01_reporte_v1.md';trace=out/'REP01_trazabilidad_v1.json';control=out/'REP01_control_editorial.json'
 comp=repo/'editorial/controles/complementarios.json'
 subprocess.run(['python3',str(repo/'editorial/scripts/controles_complementarios.py'),str(repo),str(md),str(trace),str(base),'--salida',str(comp)],check=True)
 inv=[{'ruta':str(p.relative_to(repo)),'bytes':p.stat().st_size,'sha256':sh(p)}for p in sorted(repo.rglob('*'))if p.is_file() and p!=repo/'manifest.json' and '__pycache__'not in p.parts]
 dump(repo/'manifest.json',{'paquete':'REP01_repositorio','version':'1.0','estado':'MANUSCRITO_PARA_REVISION','inventario':inv,'exclusion':'Solo manifest.json raíz; manuscrito/trazabilidad/control externos, sin ciclo de inventario.'})
 j=rd(trace);j['repositorio']['inventario']=inv;dump(trace,j)
 subprocess.run(['python3',str(base/'validar_reporte.py'),str(base),str(md),str(trace),'--repositorio',str(repo),'--salida',str(control)],check=True)
 z=out/'REP01_soportes_v1.zip'
 with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED,compresslevel=8)as f:
  for p in sorted(repo.rglob('*')):
   if p.is_file()and'__pycache__'not in p.parts:f.write(p,'REP01_repositorio/'+str(p.relative_to(repo)))
 with zipfile.ZipFile(z)as f:
  bad=f.testzip();assert bad is None,bad
  names=f.namelist();assert len(names)==len(set(names))
  assert all(n.startswith('REP01_repositorio/')and'..'not in Path(n).parts for n in names)
  actual={str(p.relative_to(repo)):p for p in repo.rglob('*')if p.is_file()and'__pycache__'not in p.parts}
  assert {n.removeprefix('REP01_repositorio/')for n in names}==set(actual)
  for n in names:
   p=actual[n.removeprefix('REP01_repositorio/')]
   assert hashlib.sha256(f.read(n)).hexdigest()==sh(p),n
 c=rd(control);r=rd(comp)
 c['controles_complementarios']={'estado':r['estado'],'errores':r['errores'],'soporte':'REP01_repositorio/editorial/controles/complementarios.json','sha256_soporte':sh(comp),'resumen':{k:v for k,v in r['resultados'].items()if k!='navegacion_editorial'},'navegacion_editorial':{'enlaces_comprobados':r['resultados']['navegacion_editorial']['enlaces_comprobados'],'alcance':r['resultados']['navegacion_editorial']['alcance']}}
 c['revision_figuras']={'estado':'REALIZADA_ASISTIDA','soporte':'REP01_repositorio/editorial/controles/revision_figuras.json','sha256':sh(repo/'editorial/controles/revision_figuras.json'),'limite':'Inspección visual de tres figuras nuevas; no revisión humana ni prueba en página definitiva.'}
 c['revision_editorial_asistida']={'soporte':'REP01_repositorio/editorial/controles/revision_editorial_asistida.json','sha256':sh(repo/'editorial/controles/revision_editorial_asistida.json'),'estado':'REALIZADA_EN_ALCANCE_DECLARADO','revision_humana_independiente':'PENDIENTE'}
 c['empaquetado']={'archivo':z.name,'bytes':z.stat().st_size,'sha256':sh(z),'archivos_zip':len(names),'raiz_unica':'REP01_repositorio/','prueba_crc':'SIN_ERRORES','cotejo_todos_los_payloads':'COINCIDEN_CON_CARPETA_FINAL','manifest_sha256':sh(repo/'manifest.json'),'inventario_excluye_su_propio_manifiesto':True,'trazabilidad_y_control_externos':True}
 c['paginacion_efectiva']={'estado':'PENDIENTE_MAQUETACION','maximo_cuerpo':10,'paginas_presupuestadas':j['tesis_y_estructura']['paginas_totales_presupuestadas'],'nota':'Presupuesto por secciones y palabras, sin medir Word/PDF; no equivale a cumplimiento.'}
 c['cierre']={'fecha_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'estado':'ARCHIVOS_PARA_REVISION','sha256_script_cierre':sh(Path(__file__)),'sin_publicacion':True,'sin_implementacion':True}
 dump(control,c)
 # Consistencia final de bytes de fuentes y artefactos ya controlados.
 assert c['ejecucion']['sha256_manuscrito']==sh(md)
 assert c['ejecucion']['sha256_trazabilidad']==sh(trace)
 assert c['empaquetado']['sha256']==sh(z)
 print(json.dumps({'estado':c['estado'],'archivos_repositorio_sin_manifest':len(inv),'archivos_zip':len(names),'palabras_cuerpo':c['conteos']['palabras_cuerpo'],'zip_bytes':z.stat().st_size,'paginacion':c['paginacion_efectiva']['estado']},ensure_ascii=False))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--base',required=True);ap.add_argument('--entrega',required=True);a=ap.parse_args();main(Path(a.base).resolve(),Path(a.entrega).resolve())
