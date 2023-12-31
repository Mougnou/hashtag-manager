from PyQt6.QtWidgets import QPlainTextEdit
from PyQt6.QtCore import pyqtSignal

class ClickableQPlainTextEdit(QPlainTextEdit):
    clicked = pyqtSignal()  # Define a clicked signal

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit()  # Emit the clicked signal