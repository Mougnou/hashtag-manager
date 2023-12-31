from PyQt6.QtWidgets import QApplication
from controller.controller import Controller
from model.hashtag_manager import HashtagManager
from view.main_menu import MainMenuView
from helpers.constant import HASHTAG_LIST_JSON_PATH, SETTING_JSON_PATH



def main():
    
    app = QApplication([])  # Create a QApplication

    view = MainMenuView(app)
    model = HashtagManager(HASHTAG_LIST_JSON_PATH)
    controller = Controller(view, model, SETTING_JSON_PATH)
    controller.run()

    app.exec()  # Start the QApplication event loop

if __name__ == "__main__":
    main()

