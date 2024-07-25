import sys
import cv2
import mediapipe as mp
import pyautogui
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from threading import Thread

class ScrollerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.scroller_active = False

        # Start the hand gesture detection in a separate thread
        self.thread = Thread(target=self.run_camera)
        self.thread.start()

    def initUI(self):
        # Window settings
        self.setWindowTitle('Gesture Scroll Control')
        self.setGeometry(100, 100, 500, 350)
        self.setStyleSheet("background: linear-gradient(to bottom, #e0e0e0, #ffffff);")  # Light gradient background

        # Create layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)  # Margins for spacing
        main_layout.setSpacing(20)  # Space between widgets

        # Status label
        self.status_label = QtWidgets.QLabel("Scroller Inactive", self)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setFont(QtGui.QFont("Roboto", 16, QtGui.QFont.Bold))
        self.status_label.setStyleSheet("color: #333333;")  # Dark gray for status
        self.status_label.setGraphicsEffect(self.getShadowEffect())  # Adding shadow effect
        main_layout.addWidget(self.status_label)

        # Info section
        info_section = QtWidgets.QHBoxLayout()
        info_section.setAlignment(QtCore.Qt.AlignCenter)
        info_label = QtWidgets.QLabel("Control the scrolling with a single click!", self)
        info_label.setFont(QtGui.QFont("Roboto", 12))
        info_label.setStyleSheet("color: #666666;")  # Medium gray for info
        info_section.addWidget(info_label)
        main_layout.addLayout(info_section)

        # Center button layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Toggle button
        self.toggle_button = QtWidgets.QPushButton("Activate Scroll", self)
        self.toggle_button.setFont(QtGui.QFont("Roboto", 14))
        self.toggle_button.setStyleSheet("""
            background-color: #007bff;  # Bright blue background
            color: #ffffff;
            border: none;
            border-radius: 15px;
            padding: 15px 25px;
            font-size: 14px;
        """)
        self.toggle_button.setFixedSize(220, 60)
        self.toggle_button.clicked.connect(self.toggleScroller)
        self.toggle_button.installEventFilter(self)  # Install event filter for animation
        button_layout.addWidget(self.toggle_button)

        main_layout.addLayout(button_layout)

        # Settings icon
        settings_icon = QtWidgets.QPushButton(self)
        settings_icon.setIcon(QtGui.QIcon('path/to/settings_icon.png'))  # Replace with actual path
        settings_icon.setIconSize(QtCore.QSize(40, 40))
        settings_icon.setStyleSheet("""
            background: transparent;
            border: none;
            padding: 10px;
        """)
        settings_icon.clicked.connect(self.openSettings)  # Function to open settings (not implemented)
        settings_icon.setToolTip("Settings")
        main_layout.addWidget(settings_icon, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)

        # Set layout
        self.setLayout(main_layout)
        self.show()

    def getShadowEffect(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QtGui.QColor(0, 0, 0, 80))
        return shadow

    def toggleScroller(self):
        self.scroller_active = not self.scroller_active
        status_text = "Scroller Active" if self.scroller_active else "Scroller Inactive"
        status_color = "#28a745" if self.scroller_active else "#333333"
        button_text = "Deactivate Scroll" if self.scroller_active else "Activate Scroll"
        button_color = "#dc3545" if self.scroller_active else "#007bff"
        self.status_label.setText(status_text)
        self.status_label.setStyleSheet(f"color: {status_color};")
        self.toggle_button.setText(button_text)
        self.toggle_button.setStyleSheet(f"""
            background-color: {button_color};
            color: #ffffff;
            border: none;
            border-radius: 15px;
            padding: 15px 25px;
            font-size: 14px;
        """)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Enter and source == self.toggle_button:
            source.setStyleSheet("""
                background-color: #0056b3;  # Darker blue on hover
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 15px 25px;
                font-size: 14px;
            """)
        elif event.type() == QtCore.QEvent.Leave and source == self.toggle_button:
            source.setStyleSheet("""
                background-color: #007bff;  # Original blue background
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 15px 25px;
                font-size: 14px;
            """)
        return super().eventFilter(source, event)

    def openSettings(self):
        # Placeholder for settings dialog
        QtWidgets.QMessageBox.information(self, "Settings", "Settings functionality is not yet implemented.")

    def run_camera(self):
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7,
            max_num_hands=1
        )
        draw = mp.solutions.drawing_utils
        cap = cv2.VideoCapture(0)

        def get_distance(a, b):
            return np.hypot(b[0] - a[0], b[1] - a[1])

        def find_finger_tips(processed):
            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]
                index_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
                middle_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP]
                return index_finger_tip, middle_finger_tip
            return None, None

        def is_scroll(index_finger_tip, middle_finger_tip):
            index_middle_dist = get_distance(
                (index_finger_tip.x, index_finger_tip.y),
                (middle_finger_tip.x, middle_finger_tip.y)
            )
            return index_middle_dist < 0.05, index_middle_dist

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frameRGB)

            if self.scroller_active and processed.multi_hand_landmarks:
                index_finger_tip, middle_finger_tip = find_finger_tips(processed)
                if index_finger_tip and middle_finger_tip:
                    scroll_detected, _ = is_scroll(index_finger_tip, middle_finger_tip)
                    if scroll_detected:
                        if index_finger_tip.y < middle_finger_tip.y:  # Scroll up
                            pyautogui.scroll(-100)
                        elif index_finger_tip.y > middle_finger_tip.y:  # Scroll down
                            pyautogui.scroll(100)

            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

            cv2.imshow('Hand Gesture Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ScrollerApp()
    sys.exit(app.exec_())
