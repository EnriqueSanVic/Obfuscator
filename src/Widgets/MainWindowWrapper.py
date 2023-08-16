from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from src.Contants import *
from src.Widgets.Obfuscator import Obfuscator


ICON_PATH = './assets/icon.ico'

class MainWindowWrapper(QMainWindow):

    def __init__(self):
        super().__init__()
        self.windowIcon = None
        self.offset = None

    def render(self):
        self.loadResources()
        self.confWindow()
        obfuscator = Obfuscator(self)
        obfuscator.render()
        obfuscator.show()
        self.show()

    def loadResources(self):
        self.windowIcon = QIcon(ICON_PATH)    

    def confWindow(self):

        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(self.windowIcon)
        
        #self.setAttribute(Qt.WA_TranslucentBackground, True)
        #self.setWindowFlags(Qt.FramelessWindowHint)

        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)