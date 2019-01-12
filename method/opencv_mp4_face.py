import cv2
import string, random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

face_detector = cv2.CascadeClassifier("e:\\haarcascade_frontalface_alt_tree.xml")
def face_image(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.02, 1)   # 第二个参数是移动距离，第三个参数是识别度，越大识别读越高
    if len(faces):
        for x, y, w, h in faces:
            cv2.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 2)   # 后两个参数，一个是颜色，一个是边框宽度
        cv2.imshow("结果", src)
        cv2.imwrite("e://"+id_generator() + '人脸.jpg', src)
cap = cv2.VideoCapture("e://a.mkv")

while cap.isOpened():
    ret, frame = cap.read()
    print('frame.shape:', frame.shape)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(delay=1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("e://"+id_generator() + '.jpg', frame)
    #face_image(frame)
cap.release()
cv2.destroyAllWindows()