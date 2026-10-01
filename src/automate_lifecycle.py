import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=ROOT/'registry/registry.json'; r=json.loads(p.read_text()); r['stage']='Production'; r['lifecycle_note']='Promoted after validation of registered model artifact.'; p.write_text(json.dumps(r,indent=2)); print('[SUCCESS] champion promoted to Production')
if __name__=='__main__': main()
