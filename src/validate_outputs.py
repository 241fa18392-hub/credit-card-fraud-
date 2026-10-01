from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=ROOT/'data/processed'; files=['X_train.csv','X_test.csv','y_train.csv','y_test.csv']; assert all((p/f).exists() for f in files); print('[SUCCESS] processed outputs validated')
if __name__=='__main__': main()
