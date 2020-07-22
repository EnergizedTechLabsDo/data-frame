import pandas as pd

filename = 'source_BTU_tidy.csv'
df = pd.read_csv(filename)
df = df.loc[:,~df.columns.str.contains('^Unnamed')]

filename_codes = 'country_codes.csv'
country_codes = pd.read_csv(filename_codes)
del country_codes['Latitude (average)']
del country_codes['Longitude (average)']
del country_codes['Alpha-2 code']
del country_codes['Numeric code']
country_codes.columns = ['Entity', 'Code']

# Anführungszeichen abschneiden
pos = 0
for code in country_codes['Code']:
    country_codes.iloc[pos,1] = code[2:5]
    pos += 1

# Ländernamen berichtigen
print('Schreibe Ländercodes zu Ländernamen um.')
i = 0
for nation in df['Entity']:
    j = 0
    for code in country_codes['Code']:
        if code in nation:
            df.iloc[i,0] = country_codes.iloc[j,0]
            break
        j += 1
    i += 1

# Übrig gebliebene Länder löschen
is_important = []
for nation in df['Entity']:
    if 'INTL' in nation:
        is_important.append(False)
    else:
        is_important.append(True)

is_important_series = pd.Series(is_important)
df = df[is_important_series]



print(country_codes.head())
print(df.head())

df.to_csv('source_BTU_codes.csv')
