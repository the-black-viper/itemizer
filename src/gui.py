import sys
from PyQt5.QtCore import QSize, QEvent
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QImage, QPalette, QFont
from PyQt5.QtWidgets import *

from utils import fontutils as font

StyleSheet = '''
QPushButton#startButton:hover {
    background-color: #79c2fc;
    color: white;
}

QPushButton#startButton:pressed {
    background-color: #bbdefb;
}
'''


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = 480
        self.window_height = 720
        self.init_ui(self.window_width, self.window_height)
        self.set_bg()

    def init_ui(self, width, height):
        self.resize(width, height)
        self.center()
        self.setWindowTitle('Main Window')
        self.start_button = self.init_start()
        self.start_button.objectName = "startButton"

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_bg(self):
        oImage = QImage("resources/images/main_bg.jpg")
        # resize Image to widgets size
        sImage = oImage.scaled(QSize(self.window_width, self.window_height))
        palette = QPalette()
        # 10 = Windowrole
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    def init_start(self):
        startbtn = QPushButton("START", self)
        startbtn.setFont(font.set_font('Roboto', 15))
        startbtn.clicked.connect(QApplication.instance().quit)
        startbtn.resize(startbtn.sizeHint())
        startbtn.setStyleSheet("color: white; background-color:#0d4d6a;")
        startbtn.installEventFilter(self)
        startbtn.move(210, 405)
        return startbtn

    def eventFilter(self, obj, event):
        if obj == self.start_button and event.type() == QEvent.HoverEnter:
            self.start_hover(True)
            print("On hover")
        elif obj == self.start_button and event.type() == QEvent.HoverLeave:
            print("Not hovered")
            self.start_hover(False)
        return super().eventFilter(obj, event)

    def start_hover(self, hover):
        if hover:
            self.start_button.setStyleSheet("color: #fff; background-color:#1577a4;")
        else:
            self.start_button.setStyleSheet("color: white; background-color:#0d4d6a;")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    # oStartbutton = StartButton()
    oMainwindow = MainWindow()
    oMainwindow.show()
    sys.exit(app.exec_())
