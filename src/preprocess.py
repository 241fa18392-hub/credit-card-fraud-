import json
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data/raw/creditcard.csv'; PROC=ROOT/'data/processed'; PROC.mkdir(exist_ok=True)

def main():
    df=pd.read_csv(RAW)
    target='Class'
    X=df.drop(columns=[target]); y=df[target]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y,random_state=42)
    scaler=StandardScaler(); X_train_s=scaler.fit_transform(X_train); X_test_s=scaler.transform(X_test)
    pd.DataFrame(X_train_s,columns=X.columns).to_csv(PROC/'X_train.csv',index=False)
    pd.DataFrame(X_test_s,columns=X.columns).to_csv(PROC/'X_test.csv',index=False)
    y_train.to_csv(PROC/'y_train.csv',index=False); y_test.to_csv(PROC/'y_test.csv',index=False)
    meta={'dataset':'creditcard.csv','rows':int(len(df)),'columns':int(df.shape[1]),'features':int(X.shape[1]),'target':target,'class_counts':{str(k):int(v) for k,v in y.value_counts().to_dict().items()},'test_size':0.2,'random_state':42,'preprocessing':'StandardScaler'}
    (PROC/'dataset_metadata.json').write_text(json.dumps(meta,indent=2))
    print('[SUCCESS] preprocessing complete')
if __name__=='__main__': main()
