import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import fontutils as font


class InputWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.parent = main

        # Enable styling and set background
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("detail")
        self.setStyleSheet('''#detail{background-image:
                        url(resources/images/detail_window.jpg)}''')