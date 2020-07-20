 # Anpassung der Quelldatei IEA_HeadlineEnergyData
import pandas as pd
import numpy as np

filename_source = 'IEA_HeadlineEnergyData.csv'
sourcedata = pd.read_csv(filename_source, header = 1)

# Alle Spalten verwerfen, die leer oder unnötig sind
sourcedata = sourcedata.loc[:,~sourcedata.columns.str.contains('^Unnamed')]
del sourcedata['NoCountry']
del sourcedata['NoFlow']
del sourcedata['NoProduct']

# Die Spalte Flow enthält Daten darüber, wie sich die Energie auf Import und Export verteilt. Es sind also nur die Zeilen mit 'Total final consumption (ktoe)' interessant.
sourcedata = sourcedata.loc[sourcedata['Flow'] == 'Total final consumption (ktoe)',:]
del sourcedata['Flow']

# Verschmelzen und die Jahre, die noch in den Spalten stehen, als zweiten Index verwenden
sourcedata = pd.melt(sourcedata, id_vars = ['Country', 'Product'], var_name = 'Year', value_name = 'values')
sourcedata['Year'].loc[sourcedata.loc[:,'Year'] == '2018 Provisional'] = '2018'
sourcedata = sourcedata.pivot_table(index = ['Country', 'Year'], columns = 'Product', values = 'values', aggfunc = 'first')

# Ktoe in TWh umrechnen, vorher fehlende Werte mit 'Nan' ersetzten
for i in range(sourcedata.shape[1]):
    sourcedata.loc[sourcedata.iloc[:, i] == ".."] = np.nan
sourcedata[:] = sourcedata[:].astype('float')
# Umrechnungsfaktor 0.01163 von ktoe nach TWh
sourcedata = sourcedata.mul(0.01163)

# Spaltennamen anpassen
# unsere col_names der Datensammlung = ['Oil [TWh]', 'Coal','Gas', 'Hydropower','Nuclear', 'Solar','Wind', 'Other renewables']
col_names = ['Coal, peat and oil shale', 'Crude, NGL and feedstocks', 'Electricity',
       'Heat', 'Natural gas', 'Nuclear', 'Oil products',
       'Renewables and waste', 'PEC [TWh]']
sourcedata.columns = col_names

print(sourcedata.head(100), sourcedata.columns)

sourcedata.to_csv('source_IEA_HeadlineEnergyData_cleaned.csv')
#print(sourcedata.columns, sourcedata.info())
