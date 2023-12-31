import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPlainTextEdit, QComboBox, QPushButton
from PyQt6.QtCore import Qt
from model.clickable_QPlainText import ClickableQPlainTextEdit

class MainMenuView(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Hashtag Manager")
        #get the screen size of the user
        screen = app.primaryScreen()
        size = screen.size()
        width = size.width()
        height = size.height()
        #set the window size to 1/4 of the screen size
        self.setGeometry(0, 0, int(width/4), int(height/4))
        
        

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create the left column widget (QPlainTextEdit)
        hashtags_display = ClickableQPlainTextEdit()
        hashtags_display.setObjectName("main_menu_textbox")
        main_layout.addWidget(hashtags_display)

        # Create the right column widget (QComboBox)
        hashtags_dropdown = QComboBox()
        hashtags_dropdown.addItem("Select a preset")
        hashtags_dropdown.setObjectName("main_menu_combobox")
        
        main_layout.addWidget(hashtags_dropdown)
        
        # Create the Horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Bouton to add a new preset
        add_button = QPushButton("Add")
        add_button.setObjectName("add_button")

        # Bouton to update a preset
        update_button = QPushButton("Update")
        update_button.setObjectName("update_button")
        update_button.setEnabled(False)

        #Process button
        process_button = QPushButton("Prompt")
        process_button.setObjectName("process_button")
        process_button.setEnabled(False)

        # Bouton to delete a preset
        delete_button = QPushButton("Delete")
        delete_button.setObjectName("delete_button")
        delete_button.setEnabled(False)
        
        button_layout.addWidget(add_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(process_button)
        button_layout.addWidget(delete_button)
        
        main_layout.addLayout(button_layout)
        # Create the "Apply" button
        apply_button = QPushButton("Apply")
        apply_button.setObjectName("apply_button")
        apply_button.setEnabled(False)
        main_layout.addWidget(apply_button)

        #Create a Settings button
        settings_button = QPushButton("Settings")
        settings_button.setObjectName("setting_button")
        main_layout.addWidget(settings_button)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

