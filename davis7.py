import numpy as np
import seaborn as sns
import pandas as pd
a=pd.read_csv("C:/Users/karun/OneDrive/Desktop/FA/hpi_data.csv")
print(a.describe())
import matplotlib.pyplot as plt
f=plt.figure()
ax=f.add_subplot(111)
print(a.head())
print(a.columns)
ax=sns.scatterplot(x="Wellbeing (0-10)",y="Happy Planet Index",hue="Country",data=a.head())

plt.show()
print(a)
print(a.columns)

import altair as alt
#print(altair.__file__)
alt.Chart(a).mark_circle().encode(x="Wellbeing (0-10):Q",y="Happy Planet Index:Q",color="Region:N",tooltip=["Wellbeing (0-10):Q"]).interactive()
#alt.Chart(a).mark_circle().encode(x="Wellbeing (0-10)",y="Happy Planet Index",color="Region").interactive()