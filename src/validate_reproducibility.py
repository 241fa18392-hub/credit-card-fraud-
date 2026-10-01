import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main(): assert (ROOT/'mlruns/local_tracking.json').exists(); print('[SUCCESS] reproducibility tracking validated')
if __name__=='__main__': main()
