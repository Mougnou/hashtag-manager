
from PyQt6.QtWidgets import  QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QTextEdit,QHBoxLayout

class PromptProcess(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 400, 300)

        self.input = QTextEdit()
        self.output = QTextEdit()
        self.process_button = QPushButton("Process")
        self.add_button = QPushButton("Add to preset")
        self.replace_button = QPushButton("Replace preset")

        self.input.setPlaceholderText("Enter prompt here...")

        self.input.setObjectName("input")
        self.output.setObjectName("output")
        self.process_button.setObjectName("process_button")
        self.add_button.setObjectName("add_button")
        self.replace_button.setObjectName("replace_button")

        V_layout = QVBoxLayout()
        H_layout = QHBoxLayout()
        V_layout.addWidget(QLabel("Prompt:"))
        V_layout.addWidget(self.input)
        V_layout.addWidget(QLabel("Output:"))
        V_layout.addWidget(self.output)
        V_layout.addWidget(self.process_button)

        H_layout.addWidget(self.add_button)
        H_layout.addWidget(self.replace_button)
        V_layout.addLayout(H_layout)

        central_widget = QWidget()
        central_widget.setLayout(V_layout)
        self.setCentralWidget(central_widget)

    

