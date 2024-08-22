# -*- coding: utf-8 -*-
"""CIE 2 exam

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d0YlnOV0dzo1TcDnLFvCdhdhqPr7pJVA
"""

import numpy as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('/content/Titanic-Dataset.csv')
data

import pandas as pd
data
null_values=data.isnull().sum()
data_filled=data.fillna(data.mean(numeric_only=True))
null_values, data_filled.head()

import numpy as np
from scipy import stats
mean1 = np.mean(data['Age'])
median1 = np.median(data['Age'])
mode1=stats.mode(data['Age'],keepdims = True).mode[0]
mean2 = np.mean(data['Fare'])
median2 = np.median(data['Fare'])
mode2=stats.mode(data['Fare'],keepdims = True).mode[0]
print("Central Trndency:")
print("mean Age:",mean1)
print("median Age:",median1)
print("mode Age:",mode1)
print("mean Fare:",mean2)
print("median Fare:",median2)
print("mode Fare:",mode2)

import pandas as pd
import matplotlib.pyplot as plt
data_grouped = data_grouped['survived','Pclass'],count().unstack()
data_grouped.plot(kind='bar',figsize=(10,6))
plt.title('survived count as Pclass')
plt.xlabel('survived')
plt.ylabel('count')
plt.ticks = (ticks[0,1],labels=['not survived','survived'],rotation=0)
plt.show()

