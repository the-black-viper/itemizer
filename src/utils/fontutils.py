import sys
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


def set_font(font, size=None):
    if size is None:
        default_size = 15
        size = default_size

    if font == 'Roboto':
        id = QFontDatabase.addApplicationFont("resources/fonts/Roboto-Light.ttf")
    elif font == 'Antonio':
        id = QFontDatabase.addApplicationFont("resource/fonts/Antonio-Regular.ttf")
    _fontstr = QFontDatabase.applicationFontFamilies(id)[0]       
    font = QFont(_fontstr, size)
    
    return font
