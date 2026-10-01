from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=ROOT/'data/raw/creditcard.csv'; df=pd.read_csv(p); assert 'Class' in df.columns; assert df.isnull().sum().sum()==0; assert set(df['Class'].unique())<=set([0,1]); print(f'[SUCCESS] validated {len(df):,} rows and {df.shape[1]} columns')
if __name__=='__main__': main()
