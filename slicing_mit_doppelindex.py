#!/usr/bin/env python
# coding: utf-8

import pandas as pd

url="https://github.com/EnergizedTechLabsDo/data-frame/raw/master/Datensammlung.xlsx"
df = pd.read_excel(url, index_col = [0,1])



'''Beispiel für Slicing mit Doppelindizes: Für den Doppelindex wird ein Tupel mit ('Land', Jahr) angegeben.'''
print(df.loc[('Germany', 2005),'PEC [TWh]'])
print(df.columns)
