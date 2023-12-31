from model.clean_prompt_model import convert_to_hashtags
from view.alerte_box import AlerteBox
from PyQt6.QtWidgets import QPlainTextEdit,QPushButton

class Prompt_Controller:
    def __init__(self, view, model,preset_name, parent_view):
        self.view = view
        self.preset_name = preset_name
        self.hashtag_manager = model
        self.parent_view = parent_view
        self.alerte_box = AlerteBox()
        

    def run(self):
        self.view.process_button.clicked.connect(self.clean_prompt)
        self.view.add_button.clicked.connect(self.add_hashtags_to_preset)
        self.view.replace_button.clicked.connect(self.replace_preset)
        self.hashtag_list = self.parent_view.findChild(QPlainTextEdit, "main_menu_textbox")
        self.update_button = self.parent_view.findChild(QPushButton, "update_button")
        self.view.output.setPlainText('')
        self.view.input.setPlainText('')

        
    def clean_prompt(self, prompt):
        #get the prompt from the view
        prompt = self.view.input.toPlainText()
        processed_prompt = convert_to_hashtags(prompt)
        self.view.output.setPlainText(processed_prompt)

    def add_hashtags_to_preset(self):
        #get the prompt from the view
        prompt = self.view.output.toPlainText()
        self.hashtag_manager.add_hashtags_to_preset(self.preset_name,prompt)
        self.hashtag_list.setPlainText(self.hashtag_manager.get_hashtags(self.preset_name))
        self.update_button.setEnabled(False)
        self.view.close()
        

    
    def replace_preset(self):
        #get the prompt from the view
        prompt = self.view.output.toPlainText()
        if self.alerte_box.update_alert():
            self.hashtag_manager.update_hashtags(self.preset_name,prompt)
            self.hashtag_list.setPlainText(self.hashtag_manager.get_hashtags(self.preset_name))
            self.update_button.setEnabled(False)
            self.view.close()

        


