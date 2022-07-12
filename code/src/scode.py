import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('.\data\S.csv')
df.head()
df.info()
df.columns

total_store= df['Store_Area'].count()
num_store_each_area= df.groupby('Store_Area').Store_Area.count()
num_store_each_area.describe()

#2. Which areas have less and more stores?
detail_stores_area= num_store_each_area.sort_values(ascending=False)
num1= detail_stores_area.apply(lambda x: x==1).sum()
num2= detail_stores_area.apply(lambda x: x==2).sum()
num3= detail_stores_area.apply(lambda x: x==3).sum()
num4= detail_stores_area.apply(lambda x: x==4).sum()
num5= detail_stores_area.apply(lambda x: x==5).sum()
print('num1: ', num1)
print('num2: ', num2)
print('num3: ', num3)
print('num4: ', num4)
print('num5: ', num5)
print('total of stores: ', detail_stores_area.count())


#3. How many percentage of detail_stores_area for each amount of store?
per1= num1/total_store*100
per2= num2*2/total_store*100
per3= num3*3/total_store*100
per4= num4*4/total_store*100
per5= num5*5/total_store*100
per_tot= pd.DataFrame([per1,per2,per3,per4,per5], index=['per1','per2','per3','per4','per5'], columns=['results'])
per_tot


x=[per1,per2,per3,per4,per5]
y=['per1','per2','per3','per4','per5']
plt.pie(x,labels=y,autopct='%1.2f%%')
plt.title('Percentage of store in each area')
plt.show()

#1. Check the correslations between 5 aspects
sns.heatmap(df.corr(),annot = True, cmap='coolwarm')
