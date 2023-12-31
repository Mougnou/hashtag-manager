import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox

class AlerteBox(QWidget):
    def __init__(self):
        super().__init__()

    def delete_alert(self):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the current preset?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            return True
        else:
            return False
    
    def update_alert(self):
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to update the current preset?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            return True
        else:
            return False
        
    def setting_alert(self):
        QMessageBox.question(self, 'Error', 'Please fill at least one field in the setting panel', QMessageBox.StandardButton.Ok)


        

