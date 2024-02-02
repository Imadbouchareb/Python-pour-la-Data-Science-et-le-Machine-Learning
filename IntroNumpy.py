import numpy as np
# un tableau à 1 dimension 1D
oneDarray = np.array([1,2,3,4,5])
print(oneDarray)

# ndim pour avoir la dimension 
print(oneDarray.ndim)

# un tableau à 2 dimension 2D
Tableau2D = np.array([[1, 2, 3], [4, 5, 6]])
print(Tableau2D)
 
print(Tableau2D.ndim)

# un tableau à 3 dimension 3D

Tableau3D = np.array([[[1, 2, 3], [-1, -2, -3]], [[4, 5, 6], [-4, -5, -6]]])
print(Tableau3D)
 
print(Tableau3D.ndim)

print(oneDarray[4])
print(Tableau2D[1][1])
print(Tableau2D[1,1])
print(Tableau2D.shape) 

# affiche  les tableaux 1D du Tableau2D
for i in Tableau2D: 
    print(i)

# affiche  les elements du Tableau2D    
for i in Tableau2D: 
    for j in i :
        print(j)

# remplir avec des zeros de type float        
zerosArray = np.zeros(10)
# changer le type 
zerosArray = zerosArray.astype(int)

# creation d'un tableau de 10 elements rempli de 5
TableauPreRempli = np.full(10, 5)

#Transposé d'un tableau 
TableauTrasposse = Tableau2D.T

matrice1 = np.array([[[1, 2, 3], [4, 5, 6], [0, 0, 0]]])
matrice2 = np.array([[[-1, -2, -3], [-4, -5, -6], [0, 0, 0]]])
#Multiplication matricielle
np.matmul(matrice1, matrice2)

np.min(matrice1)# donne la valeur minimal
np.max(matrice1)# donne la valeur maximal
np.sum(matrice1)# la somme des elements
np.mean(matrice1# donne la moyenne
np.std(matrice1)# donne l'ecart type
np.median(matrice1)#donne la mediane