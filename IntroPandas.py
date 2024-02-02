maListe=[['Pomme', 'Rouge'],
         ['Banane', 'Jaune'],
         ['Orange','Orange']]

import pandas as pd
monDataFrame = pd.DataFrame(maListe)#sans etiquette
print(monDataFrame)

monDataFrame = pd.DataFrame(maListe, columns=['Fruit', 'Couleur'])#avec etiquette
print(monDataFrame)

myDictionary = {'Fruit':['Apple', 'Banana', 'Orange'],'Color':['Red', 'Yellow', 'Orange']}
myDataFrame = pd.DataFrame(myDictionary)
print(myDataFrame)

#chargement d'un fichier csv
df = pd.read_csv(r'C:\Users\IMAD\Downloads\New folder\cereals.csv')
print(df)
#Définir l'une des colonne comme la nouvelle colonne index (l'original ne change pas)
df.set_index('name')
print(df)

#Définir l'une des colonne comme la nouvelle colonne index de maniere permanente
df.set_index('name',inplace = True)
print(df)

#par defaut cette fonction nous donne les 5 premieres lignes du DataFrame
df.head(7)

#par defaut cette fonction nous donne les 5 dernieres lignes du DataFrame
df.tail(10)

#resume stastique rapide
df.describe()

#Decoupage par ligne
df[1:4]

#Decoupage par colonne
df[['calories', 'rating']]

#appliquer des conditions
condition = df['calories'] > 70
df[condition]
#on peut faire aussi comme ça
df[df['calories'] > 70]

#condition avec and et or
df[(df['calories'] > 70) & (df['protein'] < 4)] # et

df[(df['calories'] > 70) | (df['protein'] < 4)] # ou

#index avec etiquette de ligne et de colonne et non les positions
df.loc['100% Natural Bran', 'calories']#donne l'element de ce croisement 

#donne le dataframe de ce croisement  
df.loc[['100% Natural Bran'],['calories']]

#donne le croisement allant de l'etiquette de debut vers celle de fin pour les lignes et les colonnes
df.loc['100% Natural Bran' : 'Basic 4', 'calories' : 'vitamins']

#indexer et decouper simultanement 
df.loc[['100% Natural Bran' , 'Basic 4'], 'calories' : 'vitamins']

#le iloc cest comme loc sauf qu'on va prendre la position des lignes et colonnes à la place des etiquettes
df.iloc[9,2]

#pour obtenir un dataframe
df.iloc[[9],[2]]
#decoupage
df.iloc[0:5,0:3]
#indexer et decouper simultanement 
df.iloc[[0,2,4], 0:3]

#ajout de ligne à notre DataFrame
df.loc['Trix'] = [110, 1, 25, 27.753301]
#suppression des lignes
df.drop('100% Natural Bran', axis = 0, inplace = True)

#ajout de colonne à notre Dataframe sans le loc
df['Ma colonne']=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#suppression de colonne
df.drop('Ma colonne', axis = 1, inplace = True)

#triage des valeurs
#trier un DataFrame par ordre croissant
df.sort_values(by='calories')
#trier un DataFrame par ordre decroissant
df.sort_values(by='calories', ascending = False)

#exporter un DataFrame
df.to_csv('myNewFile')
df.to_csv('myNewFile', index_label=False)#pour ne pas stocker la colonne index dans le fichier
#verifier qu'on a bien creer le fichier 
NouveauDF = df.to_csv('myNewFile')
print(NouveauDF)


df1 = df[0:3]
df2 = df[5:8]
#Si y'a l'index de colonne : df2 = df2.reset_index(drop=True)
#concatenation de DataFrame l'un dessous de l'autre
pd.concat([df1, df2])

#joindre un DataFrame cote à cote
pd.concat([df1, df2], axis = 1)

#Group by
df.groupby(df['sexe']).mean()

