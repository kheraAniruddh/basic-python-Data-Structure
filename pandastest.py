import pandas as pd 
import numpy as np
df = pd.read_csv("./train_small.csv", index_col='jobId')
print(df.head(1))
df1=(df.sort_values('label'))
print(df1.head(1))