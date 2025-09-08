import glob

import pandas as pd

files = glob.glob("*.csv")
for f in files:
    df = pd.read_csv(f)
    print(df.shape)
