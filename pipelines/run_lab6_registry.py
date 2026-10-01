import subprocess,sys
def execute_pipeline():
 print('[INFO] ========================================='); print('[INFO] Starting Lab 6: Model Registry & Lifecycle'); print('[INFO] =========================================')
 for script in ['src/train_registry.py','src/automate_lifecycle.py','src/generate_registry_report.py']:
  print(f'\n[INFO] ---> Executing {script}...'); r=subprocess.run([sys.executable,script]);
  if r.returncode: print('[ERROR] Pipeline halted.'); sys.exit(1)
 print('[SUCCESS] Lab 6 Model Registry Pipeline fully executed!')
if __name__=='__main__': execute_pipeline()
