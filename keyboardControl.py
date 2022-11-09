from djitellopy import Tello
import keyPressModule as kp
from time import sleep
import cv2


kp.init()
tello = Tello()
tello.connect()
print(tello.get_battery()) 
tello.streamon()


def getKeyboardInput():
    lr, fb, up, yv = 0, 0 , 0 , 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("q"): yv = -speed
    elif kp.getKey("e"): yv = speed

    if kp.getKey("z"): up = speed
    elif kp.getKey("x"): up = -speed

    if kp.getKey("t"): tello.takeoff()
    if kp.getKey("y"): tello.land()

    return [lr, fb, up, yv]

while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
