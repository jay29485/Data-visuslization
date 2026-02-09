# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:12:24 2022

@author: karun
"""

import numpy as np
import seaborn as sns
df=sns.load_dataset("flights")
print(df)
df_p=df.pivot("month","year", "passengers")
av=sns.boxplot(x="month",y="year",data=df.tail())
print(df_p)
#ax=sns.heatmap(df_p)

#ax=sns.clustermap(df_p,col_cluster=False, row_cluster=True,metric="correlation",method="average")


dff=sns.load_dataset("mpg")
print(dff)
x=dff['mpg']
y=dff['model_year']
#av=sns.boxplot(x,y,data=dff)
dff['model_d']=np.floor(dff.model_year/10)*10
dff['model_d']=dff['model_d'].astype(int)
print(dff)
print(dff.model_d)

av=sns.boxplot(x="mpg",y="model_d",data=dff.tail())

av=sns.violinplot(x="mpg",y="model_year",data=dff.tail())