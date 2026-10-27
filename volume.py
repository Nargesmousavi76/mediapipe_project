import cv2
import mediapipe as mp
#ارتباط با بعضی قابلیت‌های سیستم‌عامل
from ctypes import cast, POINTER
#کار با بعضی از رابط‌های سیستم ویندوز
#CLSCTX_ALL مشخص کردن نوع دسترسی مورد نیاز
from comtypes import CLSCTX_ALL
#AudioUtilities :برای دسترسی به Audio سیستم.
#IAudioEndpointVolume برای کنترل Volume
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
############################################################
mp_hand = mp.solutions.hands.Hands(max_num_hands=1)
draw_util = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

###########################################################
devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume

###########################################################
finger_counter = 0
numbers = []
last_number = 0
finger_tips = [8, 12, 16, 20]


while True:

    finger_counter = 0
    
    success, frame = cap.read()

    if not success:
        break

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hand.process(frameRGB)

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:
    
            landmark = hand.landmark
            draw_util.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

            for tip in finger_tips:

                if landmark[tip].y < landmark[tip-2].y :
                    finger_counter += 1

        if landmark[4].x > landmark[3].x :
            finger_counter += 1

        if finger_counter != last_number and finger_counter != 0:

            print('New number:', finger_counter)

            numbers.append(finger_counter)
            last_number = finger_counter

            if len(numbers) > 3:
                numbers.pop(0)
            print('Numbers:', numbers)

        # if finger_counter != last_number:
        #     numbers.append(finger_counter)
        #     last_number = finger_counter

        if numbers == [1, 2, 3]:
            print('INCREASE')
            current_volume = volume.GetMasterVolumeLevelScalar()
            current_volume = min(current_volume + 0.05, 1.0)
            volume.SetMasterVolumeLevelScalar(current_volume, None)
            numbers = []

        if numbers == [3, 2, 1]:
            print('DECREASE')
            current_volume = volume.GetMasterVolumeLevelScalar()
            current_volume = max(current_volume - 0.05, 0.0)
            volume.SetMasterVolumeLevelScalar(current_volume, None)
            numbers = []

    cv2.putText(frame,str(finger_counter),(50, 100),cv2.FONT_HERSHEY_COMPLEX,
        3,(0, 255, 0),3)

    cv2.imshow('WebCam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()