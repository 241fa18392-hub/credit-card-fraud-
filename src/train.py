from pathlib import Path
import joblib, pandas as pd
from sklearn.ensemble import RandomForestClassifier
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=ROOT/'data/processed'; X=pd.read_csv(p/'X_train.csv'); y=pd.read_csv(p/'y_train.csv').iloc[:,0]
    model=RandomForestClassifier(n_estimators=int(__import__('os').environ.get('N_ESTIMATORS','100')),max_depth=10,random_state=42,class_weight='balanced',n_jobs=-1)
    model.fit(X,y); (ROOT/'models').mkdir(exist_ok=True); joblib.dump(model,ROOT/'models/random_forest_baseline.pkl')
    print('[SUCCESS] baseline model saved')
if __name__=='__main__': main()
