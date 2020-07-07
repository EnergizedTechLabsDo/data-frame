import pandas as pd

dt_filename = 'Datensammlung.xlsx'
# Hier den Dateinamen der Quelldatein der fehldenden Werte angeben
new_data_filename = 'Daten_fehlende.xlsx'

# Dateien einlesen und die Spalten bennenen
dt = pd.read_csv(dt_filename, index_col = [0,1])
new_data = pd.read_excel(new_data_filename, index_col = [0,3])


# Spalten bennenen
# Alle Energieeinheiten in TWh, wenn nicht anders bezeichnet.
col_names = ['Code', 'Continent','Population','GDP per capita [$]','PEC [koe]','PEC [TWh]']
new_data.columns = col_names

dt.info()

# Daten übertragen
match = False
print('Schreibe . . .')
for i in dt.index:
    for j in new_data.index:
        if i == j:
            dt.loc[i, 'PEC [TWh]'] = new_data.loc[j, 'PEC [TWh]']
            match = True
            break
        else:
            match = False
    #if match == False:
        #print('Daten wurden nicht übertragen für: ', j)

dt.info()

dt.to_excel('daten_ergaenzt.xlsx')
dt.to_csv('daten_ergaenzt.csv')
