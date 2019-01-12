
import cv2 as cv


# 人脸检测
def face_image():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("e:\\haarcascade_profileface.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 1)   # 第二个参数是移动距离，第三个参数是识别度，越大识别读越高
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 2)   # 后两个参数，一个是颜色，一个是边框宽度
    cv.imshow("结果", src)


src = cv.imread("e:\\e.jpg")
#cv.imshow("原来", src)
face_image()
cv.waitKey(0)
cv.destroyAllWindows()