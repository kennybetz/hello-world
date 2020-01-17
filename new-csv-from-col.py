import pandas as pd
f = pd.read_csv('tcopy.csv')
keep_col = ['rowHeader']
new_f = f[keep_col]
new_f.to_csv("newFileTCopy.csv", index=False)
