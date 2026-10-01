from pathlib import Path
import json, joblib, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=ROOT/'data/processed'; X=pd.read_csv(p/'X_train.csv'); y=pd.read_csv(p/'y_train.csv').iloc[:,0]; Xt=pd.read_csv(p/'X_test.csv'); yt=pd.read_csv(p/'y_test.csv').iloc[:,0]
 m=RandomForestClassifier(n_estimators=int(__import__('os').environ.get('N_ESTIMATORS','100')),max_depth=10,random_state=42,class_weight='balanced',n_jobs=-1); m.fit(X,y); score=float(roc_auc_score(yt,m.predict_proba(Xt)[:,1])); joblib.dump(m,ROOT/'registry/model_v1.pkl')
 reg={'model_name':'creditcard-fraud-random-forest','version':1,'stage':'Staging','roc_auc':score,'artifact':'registry/model_v1.pkl'}; (ROOT/'registry/registry.json').write_text(json.dumps(reg,indent=2)); print('[SUCCESS] model version 1 registered')
if __name__=='__main__': main()
