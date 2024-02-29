#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

#Importing the dataset
dataset = pd.read_csv(r'C:\Users\IMAD\Documents\python udemy\ML+Resources\user+data.csv')
x = dataset.iloc[:,[2,4]].values
y = dataset.iloc[:,4].values

#Training and testing data (divide data into two parts)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state= 0)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print(y_pred)

#Making the confusion matrix 
import seaborn as sns

cm = confusion_matrix(y_pred,y_test)
print(cm)

sns.heatmap(cm)
