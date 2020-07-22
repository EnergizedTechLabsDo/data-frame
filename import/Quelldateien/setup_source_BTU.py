import pandas as pd
import numpy as np
import re

filename = 'source_BTU_pivotted.csv'
df = pd.read_csv(filename, index_col=[0,1])
df = df.loc[:,~df.columns.str.contains('^Unnamed')]
df = df.iloc[1:,:]

col_names = ['PEC [TWh]', 'Gas', 'Coal', 'Petrol', 'Nuclear and renewables']
df.columns = col_names

df.replace("[^0-9.]", np.nan, regex=True, inplace=True)

# British Thermal Units (BTU) in Terwattstunden umrechnen. qBtu = 1055.05585262/3.6 TWh

df[:] = df[:].astype('float')
df = df.mul(1055.05585262/3.6)

print(df.loc[('Brazil'),:])

df.to_csv('source_BTU_cleaned.csv')
