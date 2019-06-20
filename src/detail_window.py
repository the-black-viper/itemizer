import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import fontutils as font


class DetailWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.parent = main

        # Enable styling and set background
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("detail")
        self.setStyleSheet('''#detail{background-image:
                        url(resources/images/detail_window.jpg)}''')
        self.create_edits()

    def create_edits(self):
        # self.examinee_label = QLabel('Number of Examinees')
        # self.examinee_label.setFont(font.set_font('Roboto', 16))

        # self.question_label = QLabel('Number of Questions')
        # self.question_label.setFont(font.set_font('Roboto', 16))

        # self.choices_label = QLabel('Number of choices')
        # self.question_label.setFont(font.set_font('Roboto', 16))

        label_width, label_height = (74, 40)
        self.examinee_edit = QLineEdit(self)
        self.examinee_edit.resize(label_width, label_height)
        self.examinee_edit.move(322, 264)

        self.question_edit = QLineEdit(self)
        self.question_edit.resize(label_width, label_height)
        self.question_edit.move(322, 332)

        self.choices_edit = QLineEdit(self)
        self.choices_edit.resize(label_width, label_height)
        self.choices_edit.move(322, 397)

        # self.grid_layout = QGridLayout()
        # self.grid_layout.setOriginCorner(180)

        # self.grid_layout.addWidget(self.examinee_label, 0, 0)
        # self.grid_layout.addWidget(self.examinee_edit, 0, 1)

        # self.grid_layout.addWidget(self.question_label, 1, 0)
        # self.grid_layout.addWidget(self.question_edit, 1, 1)

        # self.grid_layout.addWidget(self.choices_label, 2, 0)
        # self.grid_layout.addWidget(self.choices_edit, 2, 1)

        # self.setLayout(self.grid_layout)