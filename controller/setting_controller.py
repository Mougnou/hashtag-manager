from PyQt6.QtWidgets import QPushButton,QLineEdit
from model.setting_update import SettingUpdater
class SettingController():
    def __init__(self, view, model, setting_json_path):
        self.view = view
        self.model = model
        self.updater = SettingUpdater(setting_json_path)
        self.set_cursor_position_button = self.view.findChild(QPushButton, "set_position_button")
        self.submit_button = self.view.findChild(QPushButton, "submit_button")

        self.time_input = self.view.findChild(QLineEdit, "time_input")
        self.cursor_postion_input = self.view.findChild(QLineEdit, "cursor_postion_input")

    def run(self):
        self.time_input.setText(self.updater.get_time_to_wait())
        x,y = self.updater.get_cursor_position()
        self.cursor_postion_input.setText(str(x) + ',' + str(y))
        self.set_cursor_position_button.clicked.connect(self.set_cursor_position)
        self.submit_button.clicked.connect(self.update_settings)

    def set_cursor_position(self):
        self.model.submit_clicked()
        self.view.cursor_postion_input.setText(str(self.model.mouse_position[0])+','+str(self.model.mouse_position[1]))
    
    def update_settings(self):
        self.updater.update_time_to_wait(self.view.time_input.text())
        if self.view.cursor_postion_input.text() != '':
            x,y = self.view.cursor_postion_input.text().split(',')
        else:
            x,y = '',''
        self.updater.update_cursor_position(x,y)
        self.view.close()

    