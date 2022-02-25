import cv2
import numpy 
import pyautogui

while True:
    screen = pyautogui.screenshot(region=(150,160,780,480))
    screen = numpy.array(screen)

    cv2.imshow('screen', screen)
    if cv2.waitKey(1) & 0xFF ==27:
        break
cv2.destroyAllWindows()

