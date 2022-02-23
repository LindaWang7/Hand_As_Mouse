import cv2

cap = cv2.VideoCapture(0)
cap.set (3,1280)
cap.set (4,720)

while True:
    success, img = cap.read()
    cv2.imshow ("Image", img)
    cv2.waitKey(1)

# import cv2;
#
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
#
# video = cv2.VideoCapture(0);
#
# while True:
#     check, frame = video.read();
#     faces = face_cascade.detectMultiScale(frame,
#                                           scaleFactor=1.1, minNeighbors=5);
#     for x,y,w,h in faces:
#         frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3);
#
#     cv2.imshow('Face Detector', frame);
#
#     key = cv2.waitKey(1);
#
#     if key == ord('q'):
#         break;
#
# video.release();
# cv2.destroyAllWindows();