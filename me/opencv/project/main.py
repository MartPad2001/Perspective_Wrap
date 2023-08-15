import cv2 as cv
import mediapipe as mp
import socket


video = cv.VideoCapture(0)
video.set(3,1280)
video.set(4,720)
video.set(10,100)



mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands = 1)
draw = mp.solutions.drawing_utils

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
AdressPort = ("127.0.0.1", 4037)

while True:
    isTrue , frame = video.read()
    h,w,c = frame.shape
    frame = cv.flip(frame,1)
    
    rgbFrame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    frameProcess = hands.process(rgbFrame)

    if(frameProcess.multi_hand_landmarks):
        lm_list = []
        for hand in frameProcess.multi_hand_landmarks:
            draw.draw_landmarks(frame,hand,mpHands.HAND_CONNECTIONS,connection_drawing_spec=draw.DrawingSpec(color = (255,0,0)),landmark_drawing_spec=draw.DrawingSpec(color = (0,0,0)))
            for id,lm in enumerate(hand.landmark):
                
                lm_x = int(lm.x * w)
                lm_y = int(lm.y * h)
                lm_list.extend([lm_x,h-lm_y])
            sock.sendto(str.encode(str(lm_list)), AdressPort)
    
    key = cv.waitKey(1)
    if(key == 27):
        break
    frame = cv.resize(frame,(0,0),None,0.5,0.5)
    cv.imshow('web',frame)
video.release()
cv.destroyAllWindows()
