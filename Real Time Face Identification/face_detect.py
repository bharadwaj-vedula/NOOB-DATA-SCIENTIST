import cv2
import tensorflow as tf
import numpy as np
from keras_vggface.vggface import VGGFace
from keras.preprocessing.image import load_img,img_to_array
from numpy import savetxt
from numpy import loadtxt
from keras.models import Model,load_model
import  matplotlib.pyplot  as plt

testing_model=load_model("predicitng_model.h5")

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("obama-2.jpg")
img2=plt.imread("obama-2.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.1,15)
for (x,y,w,h) in faces:
  cv2.rectangle(img, (x,y) ,(x+w,y+h),(0,255,0),4)
  pixels=img[y:y+w,x:x+w]
  print(x,y,w,h)


plt.imshow(img)
plt.show()
plt.imshow(pixels)
plt.show()
a=img_to_array(pixels)
a=cv2.resize(a,(224,224))
a=np.expand_dims(a,axis=0)
print(a.shape)

embedding=testing_model.predict(a)
savetxt('obama-2.csv', embedding[0][0][0], delimiter=',')
