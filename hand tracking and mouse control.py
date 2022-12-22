import cv2 as cv
import mediapipe as mp
import math
import pyautogui

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands

hands = mpHands.Hands()

mpdraw = mp.solutions.drawing_utils

while True:
    ret,frame = cap.read()
    frame = cv.flip(frame,1)
    frame = cv.resize(frame,(1466,850))
    img = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results = hands.process(img)
    
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame,handlms,mpHands.HAND_CONNECTIONS) 
            for id,lm in enumerate( handlms.landmark):
                h,w,c = frame.shape
                cx,cy = int(lm.x *w),int(lm.y *h)
                if id == 4:
                    thumbx,thumby = cx,cy
                if id == 12:
                    pyautogui.FAILSAFE=False 
                    cv.circle(frame, (cx,cy),25,(255,0,255),-1)
                    pyautogui.moveTo((cx+50),(cy+50),duration=0)
                    penx,peny= cx,cy
                    print(math.hypot(thumbx-penx,thumby-peny))
                    if(math.hypot(thumbx-penx,thumby-peny)<90):
                        print("click")
                        pyautogui.click()


    cv.imshow("final" , frame)
    if cv.waitKey(25) == 27 :
        break

cap.release()
cv.destroyAllWindows()