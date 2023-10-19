import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)
while True:
    success,frame=cap.read()
    frame=cv2.flip(frame,1)
    analysis=DeepFace.analyze(detector_backend='mtcnn',img_path=frame,actions=["age","gender","emotion","race"],enforce_detection=False)
    analysis = analysis[0]
    cv2.rectangle(frame,(analysis["region"]["x"],analysis["region"]["y"]),(analysis["region"]["x"]+analysis["region"]["w"],analysis["region"]["y"]+analysis["region"]["h"]),(255,0,255),2)
    cv2.putText(frame,f'Age: {analysis["age"]}',(20,50),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
    cv2.putText(frame, f'Gender: {analysis["dominant_gender"]}', (20, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    cv2.putText(frame, f'Emotion: {analysis["dominant_emotion"]}', (20, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    cv2.putText(frame, f'Race: {analysis["dominant_race"]}', (20, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    cv2.imshow('screen',frame)
    cv2.waitKey(1)
