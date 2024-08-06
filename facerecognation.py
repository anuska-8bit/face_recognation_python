import cv2
print("press X for exit")
face_cap=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_cap=cv2.VideoCapture(0)
while True:
    ret,video_data=video_cap.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces= face_cap.detectMultiScale(image=col,scaleFactor=1.1,minNeighbors=5,minSize=(38,30),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("x"):
        break
video_cap.release()

