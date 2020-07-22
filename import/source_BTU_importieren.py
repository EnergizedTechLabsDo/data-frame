import pandas as pd
import numpy as np

df = pd.read_excel('Datensammlung-versionen/Datensammlung-07-09-20.xlsx', index_col = [0,1])
source = pd.read_csv('Quelldateien/source_BTU_cleaned.csv', index_col = [0,1])

cols = ['PEC [TWh]', 'Coal', 'Gas']


uebertragungen = []

for col in cols:
    nan_indices = df.index[np.isnan(df[col])].tolist()
    print('Übertrage ', col ,' ...')
    count = 0
    for index in nan_indices:
        try:
            df.loc[index, col] = source.loc[index, col]
            if np.isnan(source.loc[index, col]):
                continue
            count += 1
            print("Transfered \'" + str(source.loc[index, col]) + "\' from sourcedata to " + str(index))
        except:
            pass
            # print("Not found in sourcedata: " + str(index))
    uebertragungen.append(count)

    print('Übertragene Werte für die Spalten ', cols, ': ', uebertragungen)

df.to_csv('Datensammlung-versionen/Datensammlung-07-22-20.csv')
df.to_excel('Datensammlung-versionen/Datensammlung-07-22-20.xlsx')
