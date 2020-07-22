import pandas as pd
import numpy as np

filename = 'source_BTU_codes_2.csv'
df = pd.read_csv(filename, index_col=[1,3,2])
df = df.loc[:,~df.columns.str.contains('^Unnamed')]

# Mit Duplikaten umgehen
dupes = df[df.duplicated()]

new_df = pd.DataFrame(columns=['Entity', 'Year', 'Total energy consumption'])

new_df = new_df.append(pd.Series({'Entity':'a', 'Year':1, 'Total energy consumption': 0}, name=0))

new_df.set_index(['Entity', 'Year'], inplace=True)

# new_df.drop(new_df.head(1).index, inplace=True)

for index, row in df.iterrows():
    try:
        val = df.at[index, 'Value']
        new_df.loc[(index[0], index[1]), index[2]] = val
    except:
        print("Error: " + str(index))

print(new_df)

print(new_df.head())

new_df.to_csv('source_BTU_pivotted.csv')
