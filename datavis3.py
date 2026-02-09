# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:00:22 2022

@author: karun
"""
import seaborn as sns
ft=sns.load_dataset("mpg")
sns.set(style="whitegrid")
l=sns.scatterplot(x="weight",y="mpg",data=ft)
sns.set(style="ticks")

sns.jointplot(ft.weight,ft.mpg, kind="hex",color="red")

sns.set(style="white")

sns.kdeplot(ft.weight,ft.mpg, kind="hex" , shade="true")
ll=sns.scatterplot(x="model_year",y="mpg",data=ft)
lf=sns.lineplot(x="model_year",y="mpg",data=ft,ci=88)
lg=sns.pairplot(data=ft, hue="mpg")




 

