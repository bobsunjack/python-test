# -*- coding=GBK -*-
import cv2
import sys

cap=cv2.VideoCapture("rtsp://admin:hik12345@192.168.0.122:554/h264/ch1/main/av_stream")
# cap=cv2.VideoCapture(0) #���豸�����Ŷ����豸������ͷ��һ����Ե�Ĭ��������Ϊ0

while (True):
    ret,frame=cap.read()

    if ret == True:

        cv2.imshow("video",frame)
        # �ڲ���ÿһ֡ʱ��ʹ��cv2.waitKey()�����ʵ��ĳ���ʱ�䡣������õ�̫����Ƶ�ͻᲥ�ŵķǳ��죬������õ�̫�߾ͻᲥ�ŵĺ�����ͨ�������25ms��ok
        if cv2.waitKey(25)&0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()