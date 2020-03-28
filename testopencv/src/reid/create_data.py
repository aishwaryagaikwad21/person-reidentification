import numpy as np
import cv2
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('../cascades/data/haarcascade_eye.xml')
cam = cv2.VideoCapture(0)
count = 0
face_id = input('\n enter user id end press <return> ==>  ')
while(True):
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)     
        count += 1
        # Save the captured image into the datasets folder

        cv2.imwrite("dataset/User." + str(face_id) + '.' +  
                    str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', frame)
    eyes = eye_cascade.detectMultiScale(gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 60: # Take 30 face sample and stop video
         break# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()