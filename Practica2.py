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
if resultado == 99:
    suma = cv2.add(imagen1,imagen2) #Variable imagen de suma
    cv2.imshow("Suma",suma)
    cv2.moveWindow("Suma",900,200)


if resultado == 100:
    resta = cv2.subtract(imagen1,imagen2) #Variable imagen de resta
    cv2.imshow("Resta",resta)
    cv2.moveWindow("Resta",900,200)


if resultado == 101:
    multiplicacion = cv2.multiply(imagen1,imagen2) #Variable imagen de multiplicacion
    cv2.imshow("Multiplicacion",multiplicacion)
    cv2.moveWindow("Multiplicacion",900,200)


if resultado == 102:
    division = cv2.divide(imagen1,imagen2) #Variable imagen de division
    cv2.imshow("Division",division)
    cv2.moveWindow("Division",900,200)


#Recuperado de https://theailearner.com/2019/01/01/log-transformation/
if resultado == 103:
    suma = cv2.add(imagen1,imagen2) #Variable imagen de suma para aplicar logaritmo
    logaritmo = (np.log(suma+1)/(np.log(1+np.max(suma))))*255
    logaritmo = np.array(logaritmo,dtype=np.uint8)
    cv2.imshow("Logaritmo",logaritmo)
    cv2.moveWindow("Logaritmo",900,200)


if resultado == 104:
    suma = cv2.add(imagen1,imagen2) #Variable imagen de suma para aplicar raiz
    raiz = cv2.sqrt(suma)
    cv2.imshow("Raiz",raiz)
    cv2.moveWindow("Raiz",900,200)


#Derivada https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html
if resultado == 105:
    suma = cv2.add(imagen1,imagen2) #Variable imagen de suma para aplicar derivada
    derivada = cv2.Laplacian(suma,cv2.CV_64F)
    cv2.imshow("Derivada",derivada)
    cv2.moveWindow("Derivada",900,200)


if resultado == 106:
    suma = cv2.add(imagen1,imagen2) #Variable imagen de suma para aplicar potencia
    potencia = cv2.pow(suma,2)
    cv2.imshow("Potencia",potencia)
    cv2.moveWindow("Potencia",900,200)
#######################################################################################################
