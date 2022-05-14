#Librerías
import numpy as np
from matplotlib import pyplot as plt
import cv2

#Cargar imagenes
imagen1 = cv2.imread('bat1.jpg',1)
imagen2 = cv2.imread('im1.jpg',1)

#Mostrar imagenes
cv2.imshow("Batman",imagen1)
cv2.moveWindow("Batman",0,200)
cv2.imshow("Iron Man",imagen2)
cv2.moveWindow("Iron Man",1985,200)

#Guardar tecla pulsada
resultado = cv2.waitKey(0)

######################################################################################################
#Suma
if resultado == 99: 
    suma = cv2.add(imagen1,imagen2) 
    cv2.imshow("Suma",suma)
    cv2.moveWindow("Suma",900,200)

#Resta
if resultado == 100:
    resta = cv2.subtract(imagen1,imagen2) 
    cv2.imshow("Resta",resta)
    cv2.moveWindow("Resta",900,200)

#Multiplicacion
if resultado == 101:
    multiplicacion = cv2.multiply(imagen1,imagen2) 
    cv2.imshow("Multiplicacion",multiplicacion)
    cv2.moveWindow("Multiplicacion",900,200)

#Division
if resultado == 102:
    division = cv2.divide(imagen1,imagen2) 
    cv2.imshow("Division",division)
    cv2.moveWindow("Division",900,200)

#Logaritmo
#Recuperado de https://theailearner.com/2019/01/01/log-transformation/
if resultado == 103:
    suma = cv2.add(imagen1,imagen2) 
    logaritmo = (np.log(suma+1)/(np.log(1+np.max(suma))))*255
    logaritmo = np.array(logaritmo,dtype=np.uint8)
    cv2.imshow("Logaritmo",logaritmo)
    cv2.moveWindow("Logaritmo",900,200)

#Raiz
if resultado == 104:
    suma = cv2.add(imagen1,imagen2) 
    raiz = cv2.sqrt(suma)
    cv2.imshow("Raiz",raiz)
    cv2.moveWindow("Raiz",900,200)

#Derivada
#Derivada https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html
if resultado == 105:
    suma = cv2.add(imagen1,imagen2)
    derivada = cv2.Laplacian(suma,cv2.CV_64F)
    cv2.imshow("Derivada",derivada)
    cv2.moveWindow("Derivada",900,200)

#Potencia
if resultado == 106:
    suma = cv2.add(imagen1,imagen2) 
    potencia = cv2.pow(suma,2)
    cv2.imshow("Potencia",potencia)
    cv2.moveWindow("Potencia",900,200)

#Conjuncion
if resultado == 107:
    conjuncion = cv2.bitwise_and(imagen1,imagen2)
    cv2.imshow("Conjuncion",conjuncion)
    cv2.moveWindow("Conjuncion",900,200)

#Disyuncion
if resultado == 108:
    disyuncion = cv2.bitwise_or(imagen1,imagen2)
    cv2.imshow("Disyuncion",disyuncion)
    cv2.moveWindow("Disyuncion",900,200)

#Negacion
if resultado == 109:
    negacion1 = cv2.bitwise_not(imagen1)
    negacion2 = cv2.bitwise_not(imagen2)
    cv2.destroyWindow("Batman")
    cv2.destroyWindow("Iron Man")
    cv2.imshow("Negacion 1",negacion1)
    cv2.moveWindow("Negacion 1",0,200)
    cv2.imshow("Negacion 2",negacion2)
    cv2.moveWindow("Negacion 2",1985,200)

#Traslacion
if resultado == 110:
    cv2.destroyWindow("Batman")
    cv2.destroyWindow("Iron Man")
    T1 = np.float32([[1,0,210],[0,1,20]])
    traslacion1 = cv2.warpAffine(imagen1,T1,(400,400))
    cv2.imshow("Traslacion 1",traslacion1)
    cv2.moveWindow("Traslacion 1",0,200)
    T2 = np.float32([[1,0,-210],[0,1,100]])
    traslacion2 = cv2.warpAffine(imagen2,T2,(400,400))
    cv2.imshow("Traslacion 2",traslacion2)
    cv2.moveWindow("Traslacion 2",1985,200)


#Rotacion
if resultado == 111:
    cv2.destroyWindow("Batman")
    cv2.destroyWindow("Iron Man")



    
#######################################################################################################
