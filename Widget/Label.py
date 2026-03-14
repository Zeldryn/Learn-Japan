from PySide6.QtWidgets import QLabel, QGraphicsOpacityEffect
from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer,QPropertyAnimation,QRect,Qt
import random

class Label(QLabel):
    def __init__(self,id,window):
        super().__init__(window)
        self.id = id
        self.window = window

 
        self.font = QFont()

        if self.id == "sapaMain":
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


        elif self.id == "titleLogin":
            self.setText("Login To Your Account")
            self.setStyleSheet("""QLabel {
                               color:white
                               }""")
            self.font.setPointSize(int(self.window.width() * 0.15))
            self.font.setItalic(True)
            self.setFont(self.font)


        elif self.id == "titleRegist":
            self.setText("Register New Account")
            self.setStyleSheet("""QLabel {
                               color:white
                               }""")
            self.font.setPointSize(15)
            self.font.setItalic(True)
            self.setFont(self.font)

        elif id == "failLogin":
            self.hide()
            self.setStyleSheet("color:white")
 



        elif self.id == "successLogin":
            self.hide()
            self.setStyleSheet("color:white;")
            self.font.setPointSize(int(self.window.width() * 0.1))
            self.setFont(self.font)

            self.opacityEffect = QGraphicsOpacityEffect()
            self.setGraphicsEffect(self.opacityEffect)
            self.opacityEffect.setOpacity(0)

            self.animSapa = QPropertyAnimation(self.opacityEffect,b"opacity")
            self.animSapa.setDuration(2000)
            self.animSapa.setStartValue(0)
            self.animSapa.setEndValue(1)
            self.animSapa.finished.connect(self.animFadeout)
        
        elif self.id == "textRegistFName":
            self.setStyleSheet("color:white")
            self.setText("First Name")

        elif self.id == "textRegistLName":
            self.setStyleSheet("color:white")
            self.setText("Last Name")

        elif self.id == "textRegistUsername":
            self.setStyleSheet("color:white")
            self.setText("Username")

        elif self.id == "textRegistPassword":
            self.setStyleSheet("color:white")
            self.setText("Password")

        elif self.id == "textRegistEmail":
            self.setStyleSheet("color:white")
            self.setText("Email Name")


        elif self.id == "textRegistYear":
            self.setStyleSheet("color:white")
            self.setText("Birthday")

        elif self.id == "TextLH":

            self.setStyleSheet("color: #0C7779")


        elif self.id == "textHiraganaMode":
            self.setText("Hiragana Train")
            self.setAlignment(Qt.AlignCenter)
            self.font.setPointSize(15)
            self.font.setItalic(True)
            self.setFont(self.font)
            self.setStyleSheet("""QLabel {
                               background-color : rgba(0, 183, 181, 1);
                               color : white;
                               border:2px solid white;
                               border-radius:10px;
                               }""")
            self.animHM = QPropertyAnimation(self,b"geometry")
            self.animHM.setDuration(2000)
            self.animHM.setStartValue(QRect(self.window.width() * 0.2175,self.window.height() * 0.33,0,0))
            self.animHM.setEndValue(QRect(self.window.width() * 0.145,self.window.height() * 0.22,self.window.width() * 0.1, self.window.height() * 0.05))
    
        elif self.id == "textKatakanaMode":
            self.setText("Katakana Train")
            self.setAlignment(Qt.AlignCenter)
            self.font.setPointSize(15)
            self.font.setItalic(True)
            self.setFont(self.font)
            self.setStyleSheet("""QLabel {
                               background-color : rgba(0, 183, 181, 1);
                               color : white;
                               border:2px solid white;
                               border-radius:10px;
                               }""")
            self.animHM = QPropertyAnimation(self,b"geometry")
            self.animHM.setDuration(2000)
            self.animHM.setStartValue(QRect(self.window.width() * 0.47,self.window.height() * 0.33,0,0))
            self.animHM.setEndValue(QRect(self.window.width() * 0.45,self.window.height() * 0.22,self.window.width() * 0.1, self.window.height() * 0.05))
    
    def animFadeout(self):
        self.animSapa.setDuration(2000)
        self.animSapa.setStartValue(1)
        self.animSapa.setEndValue(0)
        self.animSapa.finished.connect(self.delete)
        self.animSapa.start()

    def delete(self): 
        self.hide()
        self.window.FullScreen()



            
