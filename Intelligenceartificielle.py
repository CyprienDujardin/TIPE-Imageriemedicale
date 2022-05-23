


#On cherche à classifier des données en probabilité d'os cassé ou non 
import numpy as np
import matplotlib.pyplot as plt
import cv2 
from sklearn import preprocessing
import glob  
from PIL import Image

def sigmoide (x) :
    return 1/(1+np.exp(-x))

def derivative (x):
    return x*(1-x)
def trace (n):
    X=np.linspace(-10,10,n)
    Y=sigmoide(X)
    Z=derivative(sigmoide(X))
    plt.plot(X,Y)
    plt.plot(X,Z)
    plt.show()
    
#lis les données dans un fichier 
#on sépare les données entrainement/ test
X=glob.glob('/Users/cyprien/Documents/TIPE/Images/Os/*.jpg')

Y=[]

for k in range (len(X)):
    Y.append (np.array(Image.open(X[k])))
    Y[k]=cv2.cvtColor(Y[k],cv2.COLOR_BGR2GRAY)
    X[k]=preprocessing.scale(Y[k])
#on sépare les données entrainement/ test
tailleY=len(Y)

Ytrain = Y[:(tailleY*(5//6))]
Ytest= Y[(tailleY*5//6):]
Xtrain = X[:(tailleY*(5//6))]
Xtest = X[(tailleY*5//6):]
    
        
    
   
dim1 = np.size(X[0],0)

dim2 = int((dim1+1)/2)

    




#on définit aléatoirement les poids (entre -1 et 1)(Tableu de dimention des données)
    
  
poid1 = 2* np.random.random((dim1,dim2)) -1
poid2 = 2* np.random.random((dim2,1)) -1
    
 #on entraine le modèle 
for k in range (20000):
         
    #on calcul la sortie du sigmode  
    layer_1 = Xtrain
    layer_2 = sigmoide(np.dot(layer_1,poid1))
    layer_3 = sigmoide(np.dot(layer_2,poid2))
    #On calcul l'erreur
    Error3= Ytrain-layer_1
        
    #on la corrige avec la rétropropagation 
    Dlayer3= Error3 * derivative(layer_3)
    Error2 = Dlayer3.dot(poid1.T)
    Dlayer2 = Error2 * derivative(layer_1)
    
        
    #on applique le correction sur les poid
    poid1 += layer_2.T.dot(Dlayer3)
    poid2 += layer_1.T.dot(Dlayer2)
        
#on test les data séparées 
layer_0 = Xtest
layer_1 = sigmoide(np.dot(layer_1,poid1))
layer_2 = sigmoide(np.dot(layer_2,poid2))
correct = 0
#on compte le nombre de succès d'échec et on conclue
for i in range(len(layer_3)):
    if(layer_3[i][0] > 0.5):
        layer_3[i][0] = 1
    else:
        layer_3[i][0] = 0
    if(layer_3[i][0] == Ytest[i][0]):
        correct += 1
# printing the output
 print (correct)
 print ((correct*100)/len(layer_3))

