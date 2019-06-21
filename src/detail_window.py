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
        self.installEventFilter(self)

        # Create the line edits
        self.label_width, self.label_height = (74, 40)
        self.examinee_edit = self.create_line_edit(322, 264, 3)
        self.question_edit = self.create_line_edit(322, 332, 3)
        self.choices_edit = self.create_line_edit(322, 397, 3)
        # Create the submit button
        self.create_submit_button()

        # Go to the next line edit if enter/return is pressed
        self.examinee_edit.returnPressed.connect(lambda: self.question_edit.setFocus())
        self.question_edit.returnPressed.connect(lambda: self.choices_edit.setFocus())
        self.choices_edit.returnPressed.connect(lambda: self.submit.setFocus())

    def create_line_edit(self, x, y, max_length, width=None, height=None):
        ''' Returns a line edit using positional arguments '''

        if width is None:
            width = self.label_width
        if height is None:
            height = self.label_height

        # Set validator to accept only integers
        only_int = QIntValidator()

        # Create the line edit
        line_edit = QLineEdit(self)
        line_edit.setFont(font.set_font('Roboto'))
        line_edit.resize(width, height)
        line_edit.setMaxLength(max_length)
        line_edit.setValidator(only_int)
        line_edit.move(x, y)

        return line_edit

    def create_submit_button(self):
        self.submit = QPushButton("Submit", self)
        self.submit.setFont(font.set_font('Roboto', size=18, face='Medium'))
        self.submit.setObjectName("submitButton")
        self.submit.setStyleSheet(self.submit_button_style())
        self.submit.clicked.connect(self.change_window)
        self.submit.move(288, 481)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonRelease:
            print('clicked bg')
            self.setFocus()
        return super().eventFilter(obj, event)

    def submit_button_style(self):
        style = '''

                #submitButton:hover:pressed:!focus {color: white;
                background-image: url(resources/images/submit_pressed.png);
                min-width: 107; min-height: 46;
                border: none}

                #submitButton:hover:!pressed:focus {color: white;
                background-image: url(resources/images/submit_hover.png);
                min-width: 107; min-height: 46;
                border: none}

                #submitButton:hover:!pressed:!focus {color: white;
                background-image: url(resources/images/submit_hover.png);
                min-width: 107; min-height: 46;
                border: none}

                #submitButton:!hover:pressed:focus {color: white;
                background-image: url(resources/images/submit_pressed.png);
                min-width: 107; min-height: 46;
                border: none}

                #submitButton:!hover:pressed:!focus {color: white;
                background-image: url(resources/images/submit_pressed.png);
                min-width: 107; min-height: 46;
                border: none}

                #submitButton:!hover:!pressed:focus {color: white;
                background-image: url(resources/images/submit_hover.png);
                min-width: 107; min-height: 46;
                border: none}

                #submitButton:!hover:!pressed:!focus {color: white;
                background-image: url(resources/images/submit_not_pressed.png);
                min-width: 107; min-height: 46;
                border: none}

                #submitButton:hover:pressed:focus {color: white;
                background-image: url(resources/images/submit_pressed.png);
                min-width: 107; min-height: 46;
                border: none}
                '''
        return style

    def validate_input(self):
        pass

    def change_window(self):
        print('Changed Window')
        # pass