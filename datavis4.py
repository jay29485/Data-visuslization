# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:39:41 2022

@author: karun
"""

import seaborn as sns
df=sns.load_dataset("mpg")
print(df)
import matplotlib.pyplot as plt
x=df['mpg']
y=df['cylinders']
z=df['origin']
# use the scatter function
plt.scatter(x, y,  alpha=0.5,edgecolors='black')
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/karun/OneDrive/Desktop/FA/diamonds.csv")

print(df)

x=df['price']
y=df['depth']
z=df['table']

plt.scatter(x, y,z,  alpha=0.2,edgecolors='black',c='blue')
plt.show()