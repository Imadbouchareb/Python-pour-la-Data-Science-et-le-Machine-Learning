#importer les  librairies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading the dataset
dataset = pd.read_csv(r"C:\Users\IMAD\Documents\python udemy\ML+Resources\50_Startups.csv")
x = dataset.iloc[:,:-1]
y = dataset.iloc[:, -1].values
dataset.head(5)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))   

# Fractionner les données en ensembles de formation 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2)

#Formation du modele sur l'ensemble d'entrainement
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Prediction des résultats de l'ensemble de tests
y_pred = regressor.predict(x_test)
df = pd.DataFrame({'Real Values':y_test,'Predicted values':y_pred})

#Evaluation des performances du modele de regression
#Utiliser le RMSE root mean square error (erreur quadratique moyenne racine)
from sklearn import metrics
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
 