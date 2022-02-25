import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#captura = cv2.VideoCapture('vid02.mp4')


with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence =0.5, 
    min_tracking_confidence=0.5) as hands:

    while True:
        ret, frame = captura.read()
        if ret == False:
            break

        height, width, _ = frame.shape
        frame = cv2.flip(frame,1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results =hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,255),thickness=3, circle_radius=5),
                    mp_drawing.DrawingSpec(color=(255,0,255),thickness=3, circle_radius=5))
        
        cv2.imshow ('frame', frame)
        if cv2.waitKey(30) & 0xFF==ord('p'):
            break
captura.release()
cv2.destroyAllWindows()

