import subprocess,sys
def execute_pipeline():
 print('[INFO] ========================================='); print('[INFO] Starting Lab 3: Baseline ML Pipeline'); print('[INFO] =========================================')
 for script in ['src/preprocess.py','src/train.py','src/evaluate.py']:
  print(f'\n[INFO] ---> Executing {script}...'); r=subprocess.run([sys.executable,script]);
  if r.returncode: print(f'[ERROR] Pipeline halted. {script} failed.'); sys.exit(1)
 print('[SUCCESS] Lab 3 Pipeline fully executed!')
if __name__=='__main__': execute_pipeline()
