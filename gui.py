from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class ScrollerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
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
            transition: background-color 0.3s, transform 0.3s;
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
        if self.status_label.text() == "Scroller Inactive":
            self.status_label.setText("Scroller Active")
            self.status_label.setStyleSheet("color: #28a745;")  # Green color for active
            self.toggle_button.setText("Deactivate Scroll")
            self.toggle_button.setStyleSheet("""
                background-color: #dc3545;  # Red background
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 15px 25px;
                transition: background-color 0.3s, transform 0.3s;
            """)
        else:
            self.status_label.setText("Scroller Inactive")
            self.status_label.setStyleSheet("color: #333333;")  # Dark gray for inactive
            self.toggle_button.setText("Activate Scroll")
            self.toggle_button.setStyleSheet("""
                background-color: #007bff;  # Bright blue background
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 15px 25px;
                transition: background-color 0.3s, transform 0.3s;
            """)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Enter and source == self.toggle_button:
            source.setStyleSheet("""
                background-color: #0056b3;  # Darker blue on hover
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 15px 25px;
                transition: background-color 0.3s, transform 0.3s;
                transform: scale(1.05);
            """)
        elif event.type() == QtCore.QEvent.Leave and source == self.toggle_button:
            source.setStyleSheet("""
                background-color: #007bff;  # Original blue background
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 15px 25px;
                transition: background-color 0.3s, transform 0.3s;
                transform: scale(1);
            """)
        return super().eventFilter(source, event)

    def openSettings(self):
        # Placeholder for settings dialog
        QtWidgets.QMessageBox.information(self, "Settings", "Settings functionality is not yet implemented.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ScrollerApp()
    sys.exit(app.exec_())
