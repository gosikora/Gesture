import cv2
import os


i = 7000
path = os.path.dirname(os.path.abspath(__file__))
cap = cv2.VideoCapture(0)

while True:
    ret1, frame = cap.read()
    cv2.imshow('window', frame)
    i += 1

    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite(path + '/' + str(i) + '.jpg', frame)
        i += 1

    key = cv2.waitKey(1)  # pauses for 3 seconds before fetching next image
    if key == 27:  # if ESC is pressed, exit loop
        cv2.destroyAllWindows()
        cap.relase()
        break

'''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()'''