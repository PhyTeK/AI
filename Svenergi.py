import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

name_sheet=pd.read_csv('./data/bransle.csv',encoding="ISO-8859-1")
Value='2019'
name_sheet.pop('Main')
name_sheet.pop('Typ')
#handle missing data on imported data
name_sheet=name_sheet.fillna(0)
print(name_sheet)

#view summary of how data looks
print(name_sheet.describe())
sweden_sheet=name_sheet.pivot_table(index='Grp',aggfunc={Value:sum},columns='Kod')
sweden_sheet=sweden_sheet.fillna(0)
pd.set_option('display.max_columns',None)
sweden_sheet = sweden_sheet.loc[:, sweden_sheet.nunique() > 1] #Make sure columns have non unique values
print(sweden_sheet)
gmt = sns.clustermap(sweden_sheet, metric="euclidean", method="single", cmap="Blues", standard_scale=1)
plt.show()
plt.pause(1)
#sns.clustermap(sweden_sheet['1991'],standard_scale=1)
print(sweden_sheet.describe())

sns.histplot(sweden_sheet['2019','E02'],bins=15).set_title('Histogram & KDE Distribution for 2019')
plt.pause(1)

sns.jointplot(sweden_sheet['2019','E02'],sweden_sheet['2019','E01'],sweden_sheet,kind='kde')

plt.show()
