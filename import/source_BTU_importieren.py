import pandas as pd

df = pd.read_excel('Datensammlung-versionen/Datensammlung-07-09-20.xlsx', index_col = [0,1])


print(df.head(20), df.columns)
