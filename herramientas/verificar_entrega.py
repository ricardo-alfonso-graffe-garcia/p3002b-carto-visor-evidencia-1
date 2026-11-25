"""Verificación reproducible de referencias e integridad de esta distribución."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,json,html,hashlib,zipfile,xml.etree.ElementTree as ET,argparse

URL='https://github.com/ricardo-alfonso-graffe-garcia/p3002b-carto-visor-evidencia-1'
def verify(root):
 root=root.resolve();errors=[];counts={'referencias_relativas':0,'referencias_github':0,'hipervinculos_word':0,'archivos_con_huella':0}
 def check(p,target):
  if not target or target.startswith('#'):return
  u=urlsplit(html.unescape(target));remote=False
  if target.startswith(URL+'/blob/main/'):
   path=unquote(u.path.split('/blob/main/',1)[1]);dst=(root/path).resolve();remote=True;counts['referencias_github']+=1
  elif u.scheme or u.netloc:return
  else:dst=(p.parent/unquote(u.path)).resolve();counts['referencias_relativas']+=1
  if not dst.is_relative_to(root)or not dst.exists():errors.append({'archivo':str(p.relative_to(root)),'destino':target,'error':'Referencia fuera de la entrega o inexistente'})
 for p in root.rglob('*'):
  if '.git'in p.parts or not p.is_file():continue
  if p.suffix in ['.md','.html']:
   text=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
   links=re.findall(r'!?\[[^\]]*\]\(([^\n)]+)\)',text)if p.suffix=='.md'else re.findall(r'(?:href|src)=[\"\x27]([^\"\x27]+)',text)
   for x in links:check(p,x.strip().strip('<>'))
  elif p.suffix=='.docx'and (p.parent==root or p.parent==root/'en_linea'):
   with zipfile.ZipFile(p)as z:
    for x in ET.fromstring(z.read('word/_rels/document.xml.rels')):
     if x.get('Type','').endswith('/hyperlink'):counts['hipervinculos_word']+=1;check(p,x.get('Target'))
 manifest=root/'validacion/manifiesto_distribucion.json'
 if manifest.is_file():
  for x in json.loads(manifest.read_text())['archivos']:
   p=root/x['ruta'];counts['archivos_con_huella']+=1
   if not p.is_file()or hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']:errors.append({'archivo':x['ruta'],'error':'Huella distinta o archivo ausente'})
 return {'estado':'SIN_ERRORES'if not errors else'ERROR','conteos':counts,'errores':errors,'alcance':'Resolución de destinos y huellas locales, incluidos los destinos web equivalentes. No consulta servidores externos ni sustituye validación humana.'}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('carpeta',nargs='?',default=str(Path(__file__).resolve().parents[1]));parser.add_argument('--salida');args=parser.parse_args()
 out=verify(Path(args.carpeta))
 if args.salida:Path(args.salida).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(bool(out['errores']))
