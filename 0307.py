import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2
import numpy as np
os.chdir("C:/beryl/")

store = []
store2 = []
contrast = 200
for i in range(6):
    img  = cv2.imread(str(i) + '.jpg')
    print(type(img))
    #img = cv2.resize(img, (270, 420))
    img = np.uint8(img)
    print(type(img))
    img *= (contrast/127 + 1) - contrast
    img = np.clip(img, 0, 255)
    img = np.uint8(img)
    store.append(img)
    
for i in range(6, 12):
    img  = cv2.imread(str(i) + '.jpg')
    img = cv2.resize(img, (270, 420))
    img *= (contrast/127 + 1) - contrast
    img = np.clip(img, 0, 255)
    img = np.uint8(img)
    store2.append(img)

imgs = np.hstack([i for i in store])
imgs2 = np.hstack([i for i in store2])
imgv = np.vstack((imgs, imgs2))
cv2.imshow('1', imgv)

cv2.waitKey()
cv2.destroyAllWindows()
