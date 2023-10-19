from deepface import DeepFace
import cv2
import os
from time import time

cap = cv2.VideoCapture(0)
files = os.listdir('photos')
print(files)
for i in files:
    if i[-4:] == '.pkl':
        os.remove(f'photos/{i}')
print(os.listdir('photos'))
model_name = 'Facenet512'

while True:
    success,frame=cap.read()
    frame=cv2.flip(frame,1)
    all_image = DeepFace.find(frame,r'photos',enforce_detection=False,model_name=model_name, detector_backend='mtcnn')
    all_image_identity=(all_image[0]['identity'])
    person=[]
    score={}
    for j in all_image[0].iterrows():
        print(j[1])
        i=j[1]['identity']
        end=i.find('/')
        name=(i[7:end])
        person.append(name)
        if not name in score:
            score[name] = j[1][f'{model_name}_cosine']
        else:
            score[name] += j[1][f'{model_name}_cosine']
    if score:
        k,v=list(score.keys()),list(score.values())
        pin = (k[v.index(max(v))])
        print(score)
        print(pin)
        cv2.putText(frame,pin,(50,50),2,cv2.FONT_HERSHEY_PLAIN,(0,0,255),1)
    cv2.imshow('screen',frame)
    cv2.waitKey(1)
