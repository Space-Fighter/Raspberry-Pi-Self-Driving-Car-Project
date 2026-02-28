import cv2
import matplotlib.pyplot as plt
fig = 0
for i in range(10):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    print(frame)

cap.release()
cv2.destroyAllWindows()

    
