import pandas as pd
df = pd.read_csv('test.csv', dtype=str)

new_df = df.sort_values("sortRowHeader", axis = 0, ascending = True, na_position ='last') 


new_df.to_csv("newTest.csv", index=False)
