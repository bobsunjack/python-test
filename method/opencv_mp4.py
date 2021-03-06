import cv2
import string, random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


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

cap.release()
cv2.destroyAllWindows()