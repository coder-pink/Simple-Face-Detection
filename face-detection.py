import cv2

face_capture = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

if face_capture.empty():
    raise IOError('Could not load Haar cascade classifier xml file')

video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    raise IOError("Cannot open webcam")

while True :
    rect, video = video_capture.read()

    if not rect:
        print("Failed to capture video frame")
        break

    color = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    #Detect faces in frame
    faces = face_capture.detectMultiScale(color, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Draw rectangle 
    for(x,y,w,h) in faces:
        cv2.rectangle(video, (x,y) ,(x+w, y+h),(0, 0, 255), 2)

    cv2.imshow("live video - q to quit", video)
    if cv2.waitKey(10) == ord("q") :
        break
video_capture.release()
cv2.destroyAllWindows()




#/// camera open
# video_capture = cv2.VideoCapture(0)
# while True :
#     rect, video = video_capture.read()
#     cv2.imshow("live video", video)
#     if cv2.waitKey(10) == ord("q") :
#         break
# video_capture.release()
# cv2.destroyAllWindows()