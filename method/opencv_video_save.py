# -*- coding=GBK -*-
import cv2
import string, random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

cap=cv2.VideoCapture("rtsp://admin:hik12345@192.168.0.122:554/h264/ch1/main/av_stream")
# cap=cv2.VideoCapture(0) #打开设备索引号对于设备的摄像头，一般电脑的默认索引号为0

while (True):
    ret,frame=cap.read()

    if ret == True:

        cv2.imshow("video",frame)
        # 在播放每一帧时，使用cv2.waitKey()设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就会播放的很慢。通常情况下25ms就ok
        key = cv2.waitKey(25)
        if key&0xFF==ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("e://"+id_generator() + '.jpg', frame)
    else:
        break

cap.release()
cv2.destroyAllWindows()