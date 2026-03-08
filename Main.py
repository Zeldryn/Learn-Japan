import json
import sys
from PySide6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QSizePolicy,QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint,QTimer, QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtGui import QCursor,QMouseEvent, QIcon

#import Local
from Widget.Label import Label

from PySide6.QtMultimediaWidgets import QVideoWidget
import time
import random
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.resize(600,600)
        self.setWindowTitle("Learn Japan (Welcome)")
        self.setWindowIcon(QIcon("Image/Icon/mainIcon.png"))
        self.setMinimumSize(200,200)

        #Widget
        self.sapa = Label("sapaMain",self)


        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.sapa,alignment=Qt.AlignCenter)
        #FLAG
        self.maxWidget = False

    def FullScreen(self):
        screen = QApplication.primaryScreen()
        size = screen.size()
        if self.sapa.isHidden() and not self.maxWidget:
            self.showMaximized()
            self.maxWidget = True
            





app = QApplication(sys.argv)

window = Window()
window.show()
app.exec()
