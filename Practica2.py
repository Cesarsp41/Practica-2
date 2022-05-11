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
cv2.moveWindow("Iron Man",1975,200)

#Guardar tecla pulsada
resultado = cv2.waitKey(0)


if resultado == 99:
    imagen3 = cv2.add(imagen1,imagen2)
    cv2.imshow("Suma",imagen3)
    cv2.moveWindow("Suma",900,200)


