import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
os.chdir('/Users/cyprien/Documents/TIPE/Images/')


img=Image.open('/Users/cyprien/Documents/TIPE/Images/R.jpg')


A=np.array(img)

def niveaudegris():
    T=np.array(img)
    L=np.zeros((np.shape(T)[0],np.shape(T)[1]))
    n,m=np.shape(T)[0],np.shape(T)[1]
    for i in range(n):
        for k in range(m):
            L[i][k]=T[i][k][0]*0.2126+T[i][k][1]*0.7152+T[i][k][2]*0.0722
    return Image.fromarray(L,mode=None)

def Norme(p1,p2,p3,p4):
        n = np.sqrt((p1[0]-p3[0])*(p1[0]-p3[0]) + (p2[0]-p4[0])*(p2[0]-p4[0]))    
        return n


def contour():
    colonne,ligne = img.size
    imgC = Image.new(img.mode,img.size)
    seuil = 80
    L=[]
    for i in range(1,ligne-1):
        for j in range(1,colonne-1):
            p1 = img.getpixel((j-1,i))
            p2 = img.getpixel((j,i-1))
            p3 = img.getpixel((j+1,i))
            p4 = img.getpixel((j,i+1))
            n = Norme(p1,p2,p3,p4)
            if n < seuil:
                p = (255,255,255)
            else:
                L.append([i,j])  
                p = (0,0,0)
            imgC.putpixel((j,i),p)
    return imgC,L
    

def rgb2gray():
    rgb=np.array(contour()[0])
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gris = (0.2989 * r + 0.5870 * g + 0.1140 * b)/255
    return gris

def hough(seuil):
    Ni,Nj=np.shape(img)[0], np.shape(img)[1]#récupère la taille de l'image
    Ntheta = 180#domaine de validité de theta
    Nrho = int((Ni*Ni+Nj*Nj)**0.5)#domaine de validité de rho, 
    dtheta = np.pi/Ntheta#petite variation de theta
    drho = 1#petite variation de rho
    accum = np.zeros((Ntheta,Nrho))# création de l'accumulateur avec comme dimension la taille de l'image
    L=rgb2gray()# passage de l'image de RGB en niveau de gris
    for i in range(Ni):#parcourt les abscisses
           for j in range(Nj):#parcourt les ordonnées 
              if L[i][j]<0.99:#condition pour ne choisir que les pixels qui forment les contours dans l'image
                  for i_theta in range(Ntheta):#fait varier theta de 0 à 180
                    theta = i_theta*dtheta#theta prend cette valeur
                    rho = i*np.cos(theta)+(Nj-j)*np.sin(theta)#on calcule toutes les valeurs de rho
                    
                    i_rho = int(rho/drho)# on calcule la partie entière de rho
                    if (i_rho>0) and (i_rho<Nrho):# si rho est compris dans son domaine de validité 
                        accum[i_theta][i_rho] += 1
                        
                        
    lignes=[]

    for i_theta in range(Ntheta):
        for i_rho in range(Nrho):
            if accum[i_theta][i_rho]>=seuil:
                lignes.append((i_rho*drho,i_theta*dtheta))
                plt.axis([0,Ni,0,Nj])
    for rho,theta in lignes:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))      
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        plt.plot([x1,x2],[y1,y2],color="b",linewidth=1)
    plt.show()
