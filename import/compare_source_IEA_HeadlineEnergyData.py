# Anpassung der Quelldatei IEA_HeadlineEnergyData
import pandas as pd
import numpy as np

filename_source = 'Quelldateien/IEA_HeadlineEnergyData.csv'
sourcedata = pd.read_csv(filename_source, index_col = 0, header = 1)

filename_data = 'Datensammlung-versionen/Datensammlung-07-09-20.xlsx'
dataframe = pd.read_excel(filename_data, index_col = [0,1])
print(dataframe.head())

# Alle Spalten verwerfen, die leer sind
sourcedata = sourcedata.loc[:,~sourcedata.columns.str.contains('^Unnamed')]


# Für welche Länder haben wir überhaupt neue Daten?
countries = np.array(sourcedata.index)

# Anzahl der Länder bestimmen und vergleichen. Gibt es überhaupt Länder, für die noch keine Daten vorliegen?
pre_country = ''
countries_clean = np.array([''])
countries_count = 0

# Array mit Ländern, für die neue Daten vorliegen
# for country in countries:
#     if country != pre_country:
#         countries_count += 1
#         countries_clean = np.append(countries_clean, country)
#     pre_country = country

print(dataframe.columns)

# Dataframe mit Ländern, bei denen mind. ein Feld fehlt
empty_data = print(dataframe.loc[:,'PEC [TWh]'].isnull)
