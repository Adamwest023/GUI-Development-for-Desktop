from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout


class RocWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # registers the click and manages the outcome
        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        # widget_layout = QHBoxlayout() #horizontal
        # setting the layout style and adding the buttons
        # widget_layout = QVBoxLayout() #vertical
        # widget_layout.addWidget(button1)
        # widget_layout.addWidget(button2)
        self.setLayout(button_layout)

    def button1_clicked(self):
        print("Button 1 clicked")

    def button2_clicked(self):
        print("Button 2 clicked")
