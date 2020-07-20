# Anpassung der Quelldatei source_BTU
import pandas as pd
import numpy as np

filename_source = 'source_BTU.csv'
sourcedata = pd.read_csv(filename_source, header = 1)
pd.set_option('display.max_columns', 5)
# Transponieren ist das Mittel der Wahl.
frame = sourcedata.T

indices = frame.index.tolist()
for i in range(2, frame.shape[0], 2):
    index = indices[i]
    frame = frame.drop(index, axis=0)

frame.columns = frame.iloc[0]
frame = frame.drop('Series Key', axis=0)
frame.drop(['Units', 'Frequency'], axis = 1, inplace=True)
frame.reset_index(inplace = True)

#
frame = pd.melt(frame, id_vars = ['index', 'Series Name'], var_name = 'Year', value_name = 'values')

# Die Beschreibung der Energiequellen enhalten immer den Namen des jeweiligen Landes. Um nicht für jedes Land eine eigene Spalte zu erhalten,
# werden die Strings reduziert.
categories = ["Total energy consumption from nuclear, renewables, and other", "Total energy consumption from petroleum and other liquids",
                "Total energy consumption from natural gas", "Total energy consumption from coal", "Total energy consumption"]
print("Entferne Ländernamen aus den Kategorien ...")
for i in range(frame.shape[0]):
    series_name = frame.iloc[i, 1]
    for category in categories:
        if category in series_name:
            frame.iloc[i, 1] = category
            break

# Indexspalten umbennen
index_names = ['Entity', 'Category', 'Year', 'Value']
frame.columns = index_names

# Nachgucken !!!

# Tab
frame = frame.pivot_table(index = ['Entity', 'Year'], columns = 'Category', values = 'Value', aggfunc = 'first')

print(frame.head(25), frame.columns)

frame.to_csv('source_BTU_cleaned_pivot.csv')
