import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import fontutils as font
from popup_choice import PopupWidget

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        
        # Set dimensions and fix scaling
        width, height = 480, 720
        self.setFixedSize(width, height)

        # Center to the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Create a stack object
        self.stacked_layout = QStackedLayout()

        # Set central widget
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        # Create window widgets
        main_window = MainWindow(self)
        popup_window = PopupWidget(self)

        # Add the main window widget to the stack
        self.stacked_layout.addWidget(main_window)
        self.stacked_layout.addWidget(popup_window)

    def change_window(self):
        self.stacked_layout.setCurrentIndex(1)


class MainWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        # Turn on styling of derived classes
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("widget")
        self.setStyleSheet('''#widget{background-image:
                        url(resources/images/main_bg.jpg)}''')

        # Create start button
        self.startbtn = QPushButton("START", self)
        self.startbtn.setFont(font.set_font('Roboto', 15))
        self.startbtn.clicked.connect(main.change_window)
        self.startbtn.setObjectName("start")
        self.startbtn.installEventFilter(self)
        self.startbtn.setStyleSheet('''#start{color: white;
                                    background-color: rgb(11, 91, 127);}''')
        self.startbtn.move(210, 405)

    def eventFilter(self, obj, event):
        if obj == self.startbtn and event.type() == QEvent.HoverEnter:
            self.startbtn.setStyleSheet('''#start:hover{color: white;
                                     background-color: rgb(23, 121, 164);}''')
            print("On hover")
        elif obj == self.startbtn and event.type() == QEvent.HoverLeave:
            print("Not hovered")
            self.startbtn.setStyleSheet('''#start:!hover{color: white;
                                     background-color: rgb(11, 91, 127);}''')
        return super().eventFilter(obj, event)


def main():
    main_app = QApplication(sys.argv)
    main_window = UI()
    main_window.show()
    main_window.raise_()
    main_app.exec_()

if __name__ == '__main__':
    main()
