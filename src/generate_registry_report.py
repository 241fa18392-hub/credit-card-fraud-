import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 r=json.loads((ROOT/'registry/registry.json').read_text()); (ROOT/'outputs/registry_report.json').write_text(json.dumps(r,indent=2)); print('[SUCCESS] registry report generated')
if __name__=='__main__': main()
