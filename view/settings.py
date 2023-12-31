
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hashtag Manager")
        self.setGeometry(100, 100, 400, 200)

        # Create the main layout
        main_layout = QVBoxLayout()
        TTW_layout = QHBoxLayout()
        cursor_postion_layout = QHBoxLayout()

        # Time to wait field
        self.time_label = QLabel("Time to wait (in seconds):")
        self.time_input = QLineEdit()
        self.time_input.setObjectName("time_input")
        TTW_layout.addWidget(self.time_label)
        TTW_layout.addWidget(self.time_input)

        # cursor_postion field
        self.cursor_postion_label = QLabel("Hashtag field position:")
        self.cursor_postion_input = QLineEdit()
        self.cursor_postion_input.setObjectName("cursor_postion_input")
        self.set_position_button = QPushButton("Set position")
        self.set_position_button.setObjectName("set_position_button")
        cursor_postion_layout.addWidget(self.cursor_postion_label)
        cursor_postion_layout.addWidget(self.cursor_postion_input)
        cursor_postion_layout.addWidget(self.set_position_button)

        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setObjectName("submit_button")

        # Add the layouts to the main layout
        main_layout.addLayout(TTW_layout)
        main_layout.addLayout(cursor_postion_layout)
        main_layout.addWidget(self.submit_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

