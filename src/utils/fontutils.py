import sys
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


def set_font(font, size=None, face=None):
    if size is None:
        size = 15
    if face is None:
        face = 'Regular'
    id = None
    if font == 'Roboto':
        if face == 'Light':
            id = QFontDatabase.addApplicationFont("resources/fonts/Roboto-Light.ttf")
        elif face == 'Regular':
            id = QFontDatabase.addApplicationFont("resources/fonts/Roboto-Regular.ttf")
        elif face == 'Medium':
            id = QFontDatabase.addApplicationFont("resources/fonts/Roboto-Medium.ttf")
        elif face == 'Bold':
            id = QFontDatabase.addApplicationFont("resources/fonts/Roboto-Bold.ttf")
    else:
        id = QFontDatabase.addApplicationFont("resource/fonts/Antonio-Regular.ttf")

    _fontstr = QFontDatabase.applicationFontFamilies(id)[0]       
    font = QFont(_fontstr, size)
    
    return font
