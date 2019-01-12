import cv2
import string, random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#cap = cv2.VideoCapture("rtsp://admin:hik12345@192.168.0.122:554/h264/ch1/main/av_stream") # 使用第5个摄像头（我的电脑插了5个摄像头）
cap = cv2.VideoCapture(0) # 使用第5个摄像头（我的电脑插了5个摄像头）
face_cascade = cv2.CascadeClassifier('e:\\haarcascade_frontalface_default.xml') # 加载人脸特征库
timeF = 1
c=0
while(True):
    ret, frame = cap.read() # 读取一帧的图像
    c=c+1
    if c%timeF!=0:
        continue
    c=0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 转灰

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5)) # 检测人脸
    ##if len(faces):
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # 用矩形圈出人脸

    cv2.imshow('Face Recognition', frame)
    if len(faces):
        cv2.imwrite("e://cap//"+id_generator() + '_face.jpg', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # 释放摄像头
cv2.destroyAllWindows()