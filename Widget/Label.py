from PySide6.QtWidgets import QLabel, QGraphicsOpacityEffect
from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer,QPropertyAnimation
import random

class Label(QLabel):
    def __init__(self,id,window):
        super().__init__(window)
        self.id = id
        self.window = window

 
        self.font = QFont()

        if id == "sapaMain":
            self.setText("Hello Welcome To Learn Japan :D")
            self.setFont(self.font)
            self.setStyleSheet("color:white;")

            self.opacityEffect = QGraphicsOpacityEffect()
            self.setGraphicsEffect(self.opacityEffect)
            self.opacityEffect.setOpacity(0)

            self.animSapa = QPropertyAnimation(self.opacityEffect,b"opacity")
            self.animSapa.setDuration(2000)
            self.animSapa.setStartValue(0)
            self.animSapa.setEndValue(1)
            self.animSapa.finished.connect(self.animFadeout)
            self.animSapa.start()

            self.timer1 = QTimer()
            self.timer1.timeout.connect(self.Check)
            self.timer1.start(16)

        elif id == "titleLogin":
            self.setText("Login To Your Account")
            self.setStyleSheet("""QLabel {
                               color:white
                               }""")
            self.font.setPointSize(self.window.width() * 0.15)
            self.font.setItalic(True)
            self.setFont(self.font)
            

    def animFadeout(self):
        self.animSapa.setDuration(2000)
        self.animSapa.setStartValue(1)
        self.animSapa.setEndValue(0)
        self.animSapa.finished.connect(self.delete)
        self.animSapa.start()

    def delete(self): 
        self.hide()
        self.timer1.stop()
        self.window.FullScreen()


    def Check(self):
        self.font.setPointSize(int(self.window.width() * 0.02))
        self.font.setPointSize(int(self.window.height() * 0.02))
        if self.window.width() <= 400 or self.window.height() <= 350:
            self.font.setPointSize(int(self.width() * 0.05))
        self.setFont(self.font)
            
