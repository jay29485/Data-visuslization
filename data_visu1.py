import pandas as pd
import seaborn as sns
a=pd.read_csv("C:/Users/karun/OneDrive/Desktop/FA/diamonds.csv")
print(a)
print(a.describe())
print(a.info())



print(a.describe())
print(a.loc[[3]])

a['carat_price']=a['carat']/a['price']
print(a.info())
import numpy as np
print(a.head())
a['price_carat_high']=np.where(a['carat_price']>0.000706,1,0)

#maths function

def funti(x):
    bool_var='yes' if (x['cut']=="Ideal" and x['color']=="E")  else 'no'
    return(bool_var)


a['desired']=a.apply(funti,axis=1)

print(a)
                        
a.hist(['carat'])
        
sns.histplot(np.log(a['carat']))
        