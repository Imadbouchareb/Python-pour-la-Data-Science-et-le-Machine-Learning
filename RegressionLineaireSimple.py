import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\IMAD\Documents\python udemy\ML+Resources\homeprices.csv")
print(df)

plt.xlabel('Area(sqr ft)')
plt.ylabel('Price(US$')
plt.scatter(df.Area, df.Price, color ='red', marker='+')

reg = LinearRegression()
reg.fit(df[['Area']], df.Price)
LinearRegression()
# predit le prix 
v = reg.predict([[3300]])
c = reg.coef_
i = reg.intercept_
# donc v = c * 3300 + i