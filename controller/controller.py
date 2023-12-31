from PyQt6.QtWidgets import QComboBox,QPlainTextEdit,QPushButton
from view.alerte_box import AlerteBox
from view.add_box import AddBox
from view.settings import SettingsWindow
from view.clean_prompt import PromptProcess
from model.write_hashtag import ClickAndType
from model.setting_update import SettingUpdater

from .setting_controller import SettingController
from .clean_prompt_controller import Prompt_Controller
from model.get_cursor_position import CursorPosition
class Controller:
    def __init__(self, view, model, setting_json_path):
        self.view = view
        self.model = model
        self.setting_json_path = setting_json_path
        self.add_box = AddBox()
        self.alerte_box = AlerteBox()
        self.writer = ClickAndType()
        self.setting_window = SettingsWindow()
        self.setting_updater = SettingUpdater(self.setting_json_path)
        self.clean_prompt_window = PromptProcess()
        # Find widgets in the view by object name
        self.preset_list = self.view.findChild(QComboBox, "main_menu_combobox")
        self.hashtag_list = self.view.findChild(QPlainTextEdit, "main_menu_textbox")
        self.add_button = self.view.findChild(QPushButton, "add_button")
        self.update_button = self.view.findChild(QPushButton, "update_button")
        self.process_button = self.view.findChild(QPushButton, "process_button")
        self.delete_button = self.view.findChild(QPushButton, "delete_button")
        self.apply_button = self.view.findChild(QPushButton, "apply_button")
        self.setting_button = self.view.findChild(QPushButton, "setting_button")

        self.preset_list.currentIndexChanged.connect(self.handle_selection_and_reset_buttons)
        self.hashtag_list.clicked.connect(self.change_to_edit_mode)
        self.update_button.clicked.connect(self.handle_update)
        self.process_button.clicked.connect(self.process_prompt)
        self.add_button.clicked.connect(self.add_preset)
        self.delete_button.clicked.connect(self.delete_preset)
        self.apply_button.clicked.connect(self.apply_hashtags)
        self.setting_button.clicked.connect(self.open_setting)

    def run(self):
        self.view.show()
        self.preset_list.addItems(self.model.get_hashtags_title())

    def handle_selection_and_reset_buttons(self, index):
        selected_item = self.preset_list.currentText()  # Get the selected item from the combobox
        index = self.preset_list.findText(selected_item)
        self.reset_buttons()
        self.handle_selection(selected_item,index)
        
    def reset_buttons(self):
        self.apply_button.setEnabled(False)
        self.update_button.setEnabled(False)
        self.delete_button.setEnabled(False)
        self.process_button.setEnabled(False)

    def handle_selection(self, selected_item,index):
        hashtag = self.model.get_hashtags(selected_item)  # Load the data from the model
        self.hashtag_list.setPlainText(hashtag)
        if index != 0:
            self.delete_button.setEnabled(True)
            self.apply_button.setEnabled(True)
            self.process_button.setEnabled(True)
        
    def change_to_edit_mode(self):
        selected_item = self.preset_list.currentText()
        index = self.preset_list.findText(selected_item)
        if index != 0:
            self.update_button.setEnabled(True)
        else:
            self.update_button.setEnabled(False)

    def handle_update(self):
        if self.alerte_box.update_alert():
            selected_item = self.preset_list.currentText()
            hashtag_list = self.hashtag_list.toPlainText()
            self.model.update_hashtags(selected_item, hashtag_list)
            self.update_button.setEnabled(False)

    def add_preset(self):
        self.add_box.show()
        self.add_box.confirm_button.clicked.connect(
            lambda: (
                self.model.add_preset_hashtags(
                    self.add_box.name_text.text(),
                    self.add_box.hashtag_text.toPlainText()),
                self.preset_list.addItem(self.add_box.name_text.text()),
                self.add_box.close()
            )
        )

    def delete_preset(self):
        selected_item = self.preset_list.currentText()
        if self.alerte_box.delete_alert():
            self.model.delete_hashtags(selected_item)
            self.preset_list.removeItem(self.preset_list.currentIndex())
            self.preset_list.setCurrentIndex(0)
            self.hashtag_list.clear()
            self.delete_button.setEnabled(False)

    def open_setting(self):
        self.setting_window.show()
        self.setting_controller = SettingController(self.setting_window, CursorPosition(),self.setting_json_path)
        self.setting_controller.run()

    def apply_hashtags(self):
        waiting_time = self.setting_updater.get_time_to_wait()
        x,y = self.setting_updater.get_cursor_position()
        
        hashtag_list = self.hashtag_list.toPlainText().split(',')
        #delete hashtag in double
        hashtag_list = list(dict.fromkeys(hashtag_list))
        
        self.writer.click_and_type(hashtag_list,waiting_time,x,y)

    def process_prompt(self):
        selected_item = self.preset_list.currentText()
        self.clean_prompt_window.show()
        self.clean_prompt_controller = Prompt_Controller(self.clean_prompt_window, self.model,selected_item, self.view)
        self.clean_prompt_controller.run()
        



        
        
        
        
