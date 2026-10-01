from pathlib import Path
import json, joblib, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=ROOT/'data/processed'; Xtr=pd.read_csv(p/'X_train.csv'); ytr=pd.read_csv(p/'y_train.csv').iloc[:,0]; Xte=pd.read_csv(p/'X_test.csv'); yte=pd.read_csv(p/'y_test.csv').iloc[:,0]
    params={'n_estimators':int(__import__('os').environ.get('N_ESTIMATORS','100')),'max_depth':10,'random_state':42,'class_weight':'balanced'}
    m=RandomForestClassifier(**params,n_jobs=-1); m.fit(Xtr,ytr); pred=m.predict(Xte); prob=m.predict_proba(Xte)[:,1]
    metrics={k:float(v) for k,v in {'accuracy':accuracy_score(yte,pred),'precision':precision_score(yte,pred,zero_division=0),'recall':recall_score(yte,pred,zero_division=0),'f1':f1_score(yte,pred,zero_division=0),'roc_auc':roc_auc_score(yte,prob)}.items()}
    run={'run_name':'creditcard-random-forest','params':params,'metrics':metrics}
    (ROOT/'mlruns/local_tracking.json').write_text(json.dumps(run,indent=2)); joblib.dump(m,ROOT/'artifacts/mlflow_model.pkl'); print('[SUCCESS] tracking artifact created')
if __name__=='__main__': main()
