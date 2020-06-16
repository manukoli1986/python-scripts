
import cv2, os

#Change path
os.chdir("C:\\Users\\Administrator\\Desktop\\vagrant\\python\\python-scripts\\face_Detection")

#Image path 
img = cv2.imread("faces.png")
#print(img.shape) # TO get the shape of image


#Import rules provided by Haarcascading face detecting file which have inbuilt coding to detect face. 
detect_face = cv2.CascadeClassifier("haarcascade_eye.xml")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#
faces = detect_face.detectMultiScale(gray_img, scaleFactor=1.01, minNeighbors=5)
# print(type(faces))
# print(faces)

#To draw rectangle on faces
for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), thickness=1)
    
#To show image on console
cv2.imshow("chuts", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()