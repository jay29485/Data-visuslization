import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
a=pd.read_csv("C:/Users/karun/OneDrive/Desktop/FA/diamonds.csv")

print(a.cut.unique())
print(a.clarity.unique())
c=pd.crosstab(index=a['cut'], columns='count')
print(c)
c.plot(kind='bar',color="red")
sns.catplot('cut',data=a,kind="count")


from numpy import mean,median
sns.set(style="whitegrid")
v=sns.barplot(x="cut", y="price",data=a, estimator=mean)

r=sns.barplot(x="cut", y="price",data=a, hue="clarity")
r.legend(loc="right",ncol=3)


r.set_xlabel('cut',fontdict={'fontsize':15})  
r.set_ylabel('price',fontdict={'fontsize':15})  
r.set_xticklabels(r.get_xticklabels(),fontsize=13, rotation=30)

sns.catplot('cut',data=a,kind="count")
ig=a.loc[a['cut']=='Ideal']
x=ig.index.tolist()[0]
y=len(ig)
print(x)
print(y)
sns.catplot('cut',data=a,aspect=1.5,kind="count",color="b")
plt.annotate("good rating",xy=(x,y),xytext=(x+0.3,y+2000),arrowprops=dict(facecolor="red"))

