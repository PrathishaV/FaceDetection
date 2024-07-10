import cv2

alg=("Samplefile.xml")

haar_cascade=cv2.CascadeClassifier(alg)

cam=cv2.VideoCapture(0)

while True:
    _,img=cam.read()

    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face=haar_cascade.detectMultiScale(grayImg, 1.3, 4)
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (180,150,240),3)
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    if key == ord("a"):
        break
cam.release()
cv2.destroyAllWindows()
