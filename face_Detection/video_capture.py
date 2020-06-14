
import numpy as np
import cv2, os

#Change path
os.chdir("C:\\Users\\Administrator\\Desktop\\vagrant\\python\\python-scripts\\face_Detection")

cap = cv2.VideoCapture(0)
# print(type(cap))



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    detect_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect_face.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5)
    #To draw rectangle on faces
    for x,y,w,h in faces:
        gray=cv2.rectangle(gray, (x,y), (x+w,y+h), (255,0,0), thickness=3)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()