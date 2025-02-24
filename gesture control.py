import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Function to calculate Euclidean distance between two points
def get_distance(a, b):
    return np.hypot(b[0] - a[0], b[1] - a[1])

# Screen dimensions
screen_width, screen_height = pyautogui.size()

# MediaPipe Hands initialization
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

# Function to find index finger tip and middle finger tip
def find_finger_tips(processed):
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]  # Assuming only one hand is detected
        index_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
        middle_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP]
        return index_finger_tip, middle_finger_tip
    return None, None

# Function to detect scroll gesture
def is_scroll(index_finger_tip, middle_finger_tip):
    index_middle_dist = get_distance(
        (index_finger_tip.x, index_finger_tip.y),
        (middle_finger_tip.x, middle_finger_tip.y)
    )
    return index_middle_dist < 0.05, index_middle_dist  # Adjust threshold based on your need

# Function to detect gesture and perform corresponding action
def detect_gesture(frame, processed):
    if processed.multi_hand_landmarks:
        index_finger_tip, middle_finger_tip = find_finger_tips(processed)
        if index_finger_tip and middle_finger_tip:
            scroll_detected, index_middle_dist = is_scroll(index_finger_tip, middle_finger_tip)
            if scroll_detected:
                # Determine scroll direction based on finger positions
                if index_finger_tip.y < middle_finger_tip.y:  # Scroll up
                    pyautogui.scroll(-100)  # Adjust the scrolling increment as needed
                    cv2.putText(frame, "Scrolling Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif index_finger_tip.y > middle_finger_tip.y:  # Scroll down
                    pyautogui.scroll(100)  # Adjust the scrolling increment as needed
                    cv2.putText(frame, "Scrolling Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:  # Pause scrolling
                    cv2.putText(frame, "Scrolling Paused", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Function to initialize camera and perform hand gesture recognition
def MCV():
    draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frameRGB)

            detect_gesture(frame, processed)

            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]  # Assuming only one hand is detected
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting...")
    finally:
        cap.release()
        cv2.destroyAllWindows()

# Ensure the script doesn't run MCV() on import
if __name__ == "__main__":
    MCV()
