# Import der Energiequellen nach Laendern und Jahren in die Datensammlung

import pandas as pd
import numpy as np

filename = 'Datensammlung_vorlage.csv'
dt = pd.read_csv(filename, index_col = [0,1])

print('Größenordnung der Öl-Werte in TWh: ', np.mean(dt['Oil']))
print('Größenordnung der PEC in TWh: ', np.mean(dt['PEC [TWh]']), '\nDie Werte für die verschiedenen Energiequellen machen anscheinend keinen Sinn.')

# Löschen der Spalten 'Oil' bis 'Other renewables'. Das entspricht den Indizes 5 bis 13
dt.iloc[:,5:13] = np.nan

# Hinzufügen der ersten Quelle
filename_source = 'Quelldateien/source_1_cleaned.csv'
sourcedt = pd.read_csv(filename_source, index_col = [0,1])
print(dt.head())
print(sourcedt.head(), sourcedt.columns)

# Zuerst durch die längere Zieltabelle iterieren und die Daten aus der Quelle übertragen
uebertragungen = 0
print('Übertrage Daten ...')
for target_country in dt.index:
    for source_country in sourcedt.index:
        if target_country[0] == source_country[0]:
            if target_country[1] == source_country[1]:
                # Leider etwas unsauber. Mit iloc ging es nicht so gut. Wenn jemand eine Idee für einen schöneren Code hat, dann freie Fahrt. :)
                dt.loc[target_country, 'Oil'] = sourcedt.loc[source_country, 'Oil [TWh]']
                dt.loc[target_country, 'Coal'] = sourcedt.loc[source_country, 'Coal']
                dt.loc[target_country, 'Gas'] = sourcedt.loc[source_country, 'Gas']
                dt.loc[target_country, 'Hydropower'] = sourcedt.loc[source_country, 'Hydropower']
                dt.loc[target_country, 'Nuclear'] = sourcedt.loc[source_country, 'Nuclear']
                dt.loc[target_country, 'Solar'] = sourcedt.loc[source_country, 'Solar']
                dt.loc[target_country, 'Wind'] = sourcedt.loc[source_country, 'Wind']
                uebertragungen += 1
                break

print('Übertragene Zeilen: ', uebertragungen)
print('Größenordnung der Öl-Werte in TWh: ', np.mean(dt['Oil']))

# Hier befinden sich die bereinigten Daten
dt.to_csv('Datensammlung.csv')
dt.to_excel('Datensammlung.xlsx')
