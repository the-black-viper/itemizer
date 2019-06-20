import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import fontutils as font


class PopupWidget(QWidget):
    def __init__(self, main):
        super().__init__()
        self.parent = main
        # Enable styling and set background
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("popup")
        self.setStyleSheet('''#popup{background-image:
                        url(resources/images/popup_bg.jpg)}''')

        # Create buttons
        self.create_manual_button()
        self.create_auto_button()

    def create_manual_button(self):
        self.manual_button = QPushButton("Manual", self)
        self.manual_button.setFont(font.set_font('Roboto', size=15, face='Medium'))
        self.manual_button.setObjectName("manualButton")
        self.manual_button.setStyleSheet(self.manual_button_syle())
        self.manual_button.clicked.connect(self.change_window)
        self.manual_button.move(260, 350)

    def create_auto_button(self):
        self.auto_button = QPushButton("Auto", self)
        self.auto_button.setFont(font.set_font('Roboto', size=15, face='Medium'))
        self.auto_button.setObjectName("autoButton")
        self.auto_button.setStyleSheet(self.auto_button_style())
        self.auto_button.move(150, 350)

    def manual_button_syle(self):
        style = '''
                #manualButton:hover:!pressed {color: white;
                background-image: url(resources/images/blue_button_hover.png);
                min-width: 90; min-height: 39;
                border: none}

                #manualButton:!hover:!pressed {color: white;
                background-image: url(resources/images/blue_button_not_pressed.png);
                min-width: 90; min-height: 39;
                border: none}

                #manualButton:hover:pressed {color: white;
                background-image: url(resources/images/blue_button_pressed.png);
                min-width: 90; min-height: 39;
                border: none}
                '''
        return style

    def auto_button_style(self):
        style = '''
                #autoButton:hover:!pressed {color: white;
                background-image: url(resources/images/blue_button_hover.png);
                min-width: 90; min-height: 39;
                border: none}

                #autoButton:!hover:!pressed {color: white;
                background-image: url(resources/images/blue_button_not_pressed.png);
                min-width: 90; min-height: 39;
                border: none}

                #autoButton:hover:pressed {color: white;
                background-image: url(resources/images/blue_button_pressed.png);
                min-width: 90; min-height: 39;
                border: none}
                '''
        return style

    def change_window(self):
        print(self.parent.stacked_layout.currentIndex())
        self.parent.stacked_layout.setCurrentIndex(2)
