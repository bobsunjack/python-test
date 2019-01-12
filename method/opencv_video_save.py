# coding:utf-8
import cv2
import cv2 as cv
import string, random
import threading


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

cap=cv2.VideoCapture("rtsp://admin:hik12345@192.168.0.122:554/h264/ch1/main/av_stream")
# cap=cv2.VideoCapture(0) #打开设备索引号对于设备的摄像头，一般电脑的默认索引号为0
# 人脸检测
face_detector = cv.CascadeClassifier("e:\\haarcascade_frontalface_alt_tree.xml")
def face_image(src):
    gray = cv2.cvtColor(src, cv.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.02, 1)   # 第二个参数是移动距离，第三个参数是识别度，越大识别读越高
    if len(faces):
        for x, y, w, h in faces:
            cv2.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 2)   # 后两个参数，一个是颜色，一个是边框宽度
        cv2.imshow("结果", src)
        cv2.imwrite("e://"+id_generator() + '人脸.jpg', src)
timeF = 1
c=0
while (True):
    ret,frame=cap.read()
    key = cv2.waitKey(1)
    c = c + 1
    if ret == True:
        print(c)
        if (c % timeF == 0):  # 每隔timeF帧进行存储操作
            cv2.imshow("video",frame)
            # 在播放每一帧时，使用cv2.waitKey()设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就会播放的很慢。通常情况下25ms就ok

            print(c)
            if key&0xFF==ord('q'):
                break
            elif key == ord('s'):
                cv2.imwrite("e://"+id_generator() + '.jpg', frame)
           # face_image(frame)
           # t =threading.Thread(target=face_image,args=(frame,))
           # t.start()
    else:
        break

cap.release()
cv2.destroyAllWindows()