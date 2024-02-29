#importations des librairies
import numpy as np
import matplotlib as plt
import pandas as pd 
from sklearn.metrics import confusion_matrix

# importation de l'ensemble de données
dataset  = pd.read_csv(r"C:\Users\IMAD\Documents\python udemy\ML+Resources\user+data.csv")
x = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, 4].values
print(x)
print(y)

#Fractionnement des données en ensembles de formation et test 
# Training and Testing Data (Divide the data into two parts)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x, y, test_size= 0.25, random_state=0)

#Mise à l'échelle des données
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()

#pour mettre à l'echelle il soustrait la moyenne et divise par l'ecart type donc devient centré et reduit
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

#importation du clasificateur KNN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, metric="minkowski", p=2)
classifier.fit(x_train, y_train)

#prediction des resultats et matrice de confusion
y_pred = classifier.predict(x_test)
# faire la matrice de confusion ou bien la matrice d'erreur
cm = confusion_matrix(y_pred, y_test)
print(cm)