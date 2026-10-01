import subprocess,sys
def execute_pipeline():
 print('[INFO] ========================================='); print('[INFO] Starting Lab 5: Production Data Pipeline'); print('[INFO] =========================================')
 for script in ['src/validate_data.py','src/preprocess_pipeline.py','src/validate_outputs.py']:
  print(f'\n[INFO] ---> Executing {script}...'); r=subprocess.run([sys.executable,script]);
  if r.returncode: print(f'[ERROR] Pipeline halted. {script} failed.'); sys.exit(1)
 print('[SUCCESS] Lab 5 Production Pipeline fully executed!')
if __name__=='__main__': execute_pipeline()
