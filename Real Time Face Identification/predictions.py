import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
from numpy import savetxt
from numpy import loadtxt
import scipy
import matplotlib.pyplot as plt
from scipy.spatial.distance import cosine
import pandas as pd

og_embedding = pd.read_csv("embeddings.csv")


testing_model=load_model("predicitng_model.h5")
#testing_model.summary()

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


cap=cv2.VideoCapture(0)
while True:
    score_list=[]

    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y) ,(x+w,y+h),(0,255,0),4)
        pixels=img[y:y+w,x:x+w]
        a=img_to_array(pixels)
        a=cv2.resize(a,(224,224))
        a=np.expand_dims(a,axis=0)
        embedding=testing_model.predict(a)
        #print(embedding)

        pos=[]

        for i in og_embedding.columns:
            temp=cosine(og_embedding[i],embedding)
            score_list.append(temp)
            score=min(score_list)
            pos=score_list.index(score)
            print(score_list)

        if score<=0.5:
            if len(score_list)<=5:
                cv2.putText(img, og_embedding.columns[pos] , (x, y-50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
            else:
                cv2.putText(img, og_embedding.columns[pos%5] , (x, y-50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
        else:
            cv2.putText(img, "unknown", (x, y-50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
