
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
os.chdir('C:\\Users\\Cypri\\Desktop\\TIPE\\Photo')



img=Image.open('C:\\Users\\Cypri\\Desktop\\TIPE\\Photo\\losange.png')




def rectangle ():                             
    img=Image.open('C:\\Users\\Cypri\\Desktop\\TIPE\\Photo\\losange.png')

    tabl = np.array(img)
    
    n,m=np.shape(tabl)[0],np.shape(tabl)[1]
    
    L=[]
    
    for i in range (1,n+1):
        for j in range (2,m+1):
            P1,P2=img.getpixel(i,j)[0],img.getpixel(i,(j-1))[0]           #permet de comparer chaque pixel et de reperrer les contours d'un réctangle noir
            if P1-P2 != 0:
                L.append([i,j])
    return L                
            
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
os.chdir('/Users/cyprien/Documents/TIPE/Images/')


img=Image.open('/Users/cyprien/Documents/TIPE/Images/R.jpg')


def Norme(p1,p2,p3,p4):
        n = np.sqrt((p1[0]-p3[0])*(p1[0]-p3[0]) + (p2[0]-p4[0])*(p2[0]-p4[0]))    #Calcul de la norme euclidienne pour un pixel
        return n


def contour():
    colonne,ligne = img.size                #obtention des dimensions de l'image 
    imgC = Image.new(img.mode,img.size)     #Création d'une image blanche de même dmension
    seuil = 80                              #À adapter en focntion de l'exigence souhaité 
    L=[]
    for i in range(1,ligne-1):
        for j in range(1,colonne-1):        #On parcours l'image pixel par pixel
            p1 = img.getpixel((j-1,i))      #P1 -> Pixel "au dessus" du pixel séléctioné 
            p2 = img.getpixel((j,i-1))      #P2 -> Pixel "à droite" du pixel séléctioné 
            p3 = img.getpixel((j+1,i))      #P3 -> Pixel "en dessous" du pixel séléctioné 
            p4 = img.getpixel((j,i+1))      #P4 -> Pixel "à gauche" du pixel séléctioné 
            n = Norme(p1,p2,p3,p4)
            if n < seuil:
                p = (255,255,255)
            else:
                L.append([i,j])  
                p = (0,0,0)
            imgC.putpixel((j,i),p)
    return imgC,L                           #Renvoie les contours de l'image d'entrée, La liste des coordonées de ces contours


def centre():
    Img,L=contour()[0], contour()[1]
    n = len(L)
    Ml, Mc=0,0
    for k in range(n):
        Ml+=L[k][0]
        Mc+=L[k][1]
    return ((1/n)*Ml,(1/n)*Mc) 
  
def trirapide(L):
  n=len(L)
  if n<=1:
    return L
  PS=[]
  LR=[]
  P=L[0]
  for k in range (1,n):
    if L[k]<= p:
      PS.append(L[k])
     else :
      LR.append(L[k])
   return (trirapide(PS)+[p] + trirapide(LR))
    
  
  def coin():
    L=contour()[1]
    Centre=centre()
    D=[]
    for k in range (len(L)):
      a=np.sqrt((L[k][0]-Centre[0])**2) + (L[k][1]-Centre[1])**2))
      D.append(a)
    D=trirapide(D)
    Coin=[D[-1],D[-2],D[-3],D[-4]]
    return Coin
  
def distance():
  Coin=coin()
  for k in range(len(Coin)-1):
    if Coin[k]-Coin[k+1] !=0 :
      return False
  return True
      

