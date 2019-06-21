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
                        url(resources/images/detail_bg.jpg)}''')
        self.installEventFilter(self)

        # Create the line edits
        self.label_width, self.label_height = (74, 40)
        self.examinee_edit = self.create_line_edit(322, 264, 3)
        self.question_edit = self.create_line_edit(322, 332, 3)
        self.choices_edit = self.create_line_edit(322, 397, 3)

        # Create labels
        self.examinee_label = self.create_labels(84, 270, "Number of Examinees")
        self.question_label = self.create_labels(84, 342, "Number of Questions")
        self.choices_label = self.create_labels(84, 404, "Number of Choices")

        self.prompt1 = self.prompt_label(86, 294)
        self.prompt2 = self.prompt_label(86, 364)
        self.prompt3 = self.prompt_label(86, 427)

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

    def create_labels(self, x, y, text_label):
        '''Returns a set of labels'''
        label = QLabel(text_label, self)
        label.setFont(font.set_font('Roboto', size=16, face='Medium'))
        label.setStyleSheet('color: #094763; font-weight: bold')
        label.move(x, y)
        return label

    def prompt_label(self, x, y):
        '''Returns the label prompt when invalid input is detected'''
        label = QLabel('! Input must be a number from 0 - 999', self)
        label.setFont(font.set_font('Roboto', size=10, face='Medium'))
        label.setStyleSheet('color: rgba(194, 11, 11, 0)')
        label.move(x, y)
        return label

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

    def _input_prompt(self, label_list, line_edit_list, prompt_list):
        '''Updates UI by turning on/off prompts'''

        for obj in zip(label_list, line_edit_list, prompt_list):
            # prompt_flag.append((obj[0].pos(), obj[1].hasAcceptableInput()))
            if not obj[1].hasAcceptableInput():
                obj[0].setStyleSheet('color: #dc0303; font-weight: bold;')
                obj[1].setStyleSheet('border: 2px solid red;')
                obj[2].setStyleSheet('color: rgba(194, 11, 11, 255)')
                
            else:
                obj[0].setStyleSheet('color: #094763; font-weight: bold;')
                obj[1].setStyleSheet('border: 1px;')
                obj[2].setStyleSheet('color: rgba(194, 11, 11, 0)')


    def change_window(self):
        print('Current Window:', self.parent.stacked_layout.currentIndex())
        line_edit_list = (self.examinee_edit, self.question_edit, self.choices_edit)
        label_list = (self.examinee_label, self.question_label, self.choices_label)
        prompt_list = (self.prompt1, self.prompt2, self.prompt3)

        if self.examinee_edit.hasAcceptableInput() and self.question_edit.hasAcceptableInput() and self.choices_edit.hasAcceptableInput():
            self.parent.stacked_layout.setCurrentIndex(3)
        else:
            self._input_prompt(label_list, line_edit_list, prompt_list)
