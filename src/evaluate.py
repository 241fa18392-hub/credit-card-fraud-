from pathlib import Path
import json, joblib, pandas as pd
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,confusion_matrix
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=ROOT/'data/processed'; X=pd.read_csv(p/'X_test.csv'); y=pd.read_csv(p/'y_test.csv').iloc[:,0]
    m=joblib.load(ROOT/'models/random_forest_baseline.pkl'); pred=m.predict(X); prob=m.predict_proba(X)[:,1]
    out={'accuracy':accuracy_score(y,pred),'precision':precision_score(y,pred,zero_division=0),'recall':recall_score(y,pred,zero_division=0),'f1':f1_score(y,pred,zero_division=0),'roc_auc':roc_auc_score(y,prob),'confusion_matrix':confusion_matrix(y,pred).tolist()}
    (ROOT/'outputs').mkdir(exist_ok=True); (ROOT/'outputs/metrics.json').write_text(json.dumps(out,indent=2))
    pd.DataFrame({'actual':y,'predicted':pred,'probability':prob}).to_csv(ROOT/'outputs/predictions.csv',index=False)
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
