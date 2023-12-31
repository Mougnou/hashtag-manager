from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QPlainTextEdit

class AddBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Box")
        
        self.name_label = QLabel("Name:")
        self.name_text = QLineEdit()
        
        self.hashtag_label = QLabel("Hashtag:")
        self.hashtag_text = QPlainTextEdit()
        
        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")
        
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_text)
        layout.addWidget(self.hashtag_label)
        layout.addWidget(self.hashtag_text)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        
        self.setLayout(layout)
