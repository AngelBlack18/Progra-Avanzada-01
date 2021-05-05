import cv2
import numpy as numpy

img = cv2.imread("Cerveza.png")

cv2.imshow('mostrar imagen OPENCV', img)

pixel = img[100,100]
print (pixel)

color_bajo=(32,100,200)
color_alto=(22,209,252)