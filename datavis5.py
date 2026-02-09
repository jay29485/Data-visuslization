# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:51:19 2022

@author: karun
"""
import numpy as np
import seaborn as sns
df=sns.load_dataset("mpg")
print(df)
import matplotlib.pyplot as plt
def sinplot(flip = 1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


sns.set_context('paper')
sinplot()
plt.show()


x=df['mpg']
y=df['cylinders']
a=plt.subplots()
plt.plot(x,label="dd")
plt.plot(y,label="dd")