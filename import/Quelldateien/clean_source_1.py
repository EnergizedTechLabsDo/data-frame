# Anpassung der ersten Quelldatei
import pandas as pd

filename = 'source_1.csv'
sourcedata = pd.read_csv(filename, index_col = [0,2])

# Anpassung der Spaltennamen
# Alle Einheiten in TWh, wenn nicht anders angegeben
del sourcedata['Code']
col_names = ['Oil [TWh]', 'Coal','Gas', 'Hydropower','Nuclear', 'Solar','Wind', 'Other renewables']
sourcedata.columns = col_names

print(sourcedata.head(), sourcedata.columns)
print('Alle Einheiten in TWh')

sourcedata.to_csv('source_1_cleaned.csv')
