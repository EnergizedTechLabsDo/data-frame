# Importieren von 'source_IEA_HeadlineEnergyData_cleaned' in die Datensammlung

import pandas as pd
import numpy as np

col = 'PEC [TWh]'

source_name = 'Quelldateien/source_IEA_HeadlineEnergyData_cleaned.csv'
sourcedata = pd.read_csv(source_name, index_col = [0,1])
dataframe_name = 'Datensammlung-versionen/Datensammlung-07-09-20.xlsx'
dataframe = pd.read_excel(dataframe_name, index_col = [0,1])
# Alle Einheiten in TWh

# dataframe.loc[('Germany', 2000), col] = np.nan

nan_indices = dataframe.index[np.isnan(dataframe[col])].tolist()

uebertragungen = 0
print('Übertrage Daten ...')
for index in nan_indices:
    try:
        dataframe.loc[index, col] = sourcedata.loc[index, col]
        if np.isnan(sourcedata.loc[index, col]):
            continue
        uebertragungen += 1
        print("Transfered \'" + str(sourcedata.loc[index, col]) + "\' from sourcedata to " + str(index))
    except:
        pass
        # print("Not found in sourcedata: " + str(index))


print('Übertragene Zeilen: ', uebertragungen)

# Leider keine neuen Daten vorhanden :(
# print(dataframe.info())
