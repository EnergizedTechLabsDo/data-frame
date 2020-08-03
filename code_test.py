# import necessary libs
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import nan
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import statsmodels.formula.api as smf
sns.set()

# data import and overview
import_data = "https://github.com/EnergizedTechLabsDo/data-frame/raw/test_new_data_mm/Norway_US_test.xlsx"
df = pd.read_excel(import_data)
df = df.set_index("Entity")
print(df)

print(df.shape)
print(len(df))
print(df.describe())
print(df.loc[:, df.isnull().any()])
print(df.isnull().sum())
print(df.isnull().sum())
print(df.head(-20))"""

# exploratory plots
plt.figure(figsize=(12, 4))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")
plt.show()
sns.distplot(df["GDP"].dropna(), color="purple", bins=30)
plt.show()
plt.subplot(2, 1, 1)
plt.plot(df["Year"], df["GDP"], "r")
plt.xlabel("Jahr")
plt.ylabel("Bruttoinlandsprodukt in Millarden $")
plt.ylim((0, 10000))
plt.subplot(2, 1, 2)
plt.plot(df["Coal consumption per capita"], df["Co2e"], "b")
plt.xlabel("Kohleverbrauch")
plt.ylabel("CO2 Verbrauch")

label_ger = df.loc["Germany"]
label_chn = df.loc["China"]
plt.scatter(label_ger["Year"], label_ger["GDP"],
            marker="o", color="green", label=label_ger)
plt.scatter(label_chn["Year"], label_chn["GDP"],
            marker="o", color="red", label=label_chn)
plt.style.use("ggplot")
plt.xlabel("Jahr")
plt.ylabel("Bruttoinlandsprodukt in 10 hoch 12 $")
# plt.legend(loc="upper left") # to modify
plt.title("Falafelburger")
plt.show()

# regression, kausaler zsmhang
sns.lmplot(x="Year", y="GDP", data=label_ger)
sns.lmplot(x="Year", y="GDP", data=label_chn)
plt.xlabel("Jahr")
plt.ylabel("Bruttoinlandsprodukt in 10 hoch 12 $")
plt.show()