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


        elif id == "titleLogin":
            self.setText("Login To Your Account")
            self.setStyleSheet("""QLabel {
                               color:white
                               }""")
            self.font.setPointSize(int(self.window.width() * 0.15))
            self.font.setItalic(True)
            self.setFont(self.font)


        elif id == "titleRegist":
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
 



        elif id == "successLogin":
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
        
        elif id == "textRegistFName":
            self.setStyleSheet("color:white")
            self.setText("First Name")

        elif id == "textRegistLName":
            self.setStyleSheet("color:white")
            self.setText("Last Name")

        elif id == "textRegistUsername":
            self.setStyleSheet("color:white")
            self.setText("Username")

        elif id == "textRegistPassword":
            self.setStyleSheet("color:white")
            self.setText("Password")

        elif id == "textRegistEmail":
            self.setStyleSheet("color:white")
            self.setText("Email Name")


        elif id == "textRegistYear":
            self.setStyleSheet("color:white")
            self.setText("Birthday")

        elif id == "TextLH":

            self.setStyleSheet("color: #0C7779")
            

    def animFadeout(self):
        self.animSapa.setDuration(2000)
        self.animSapa.setStartValue(1)
        self.animSapa.setEndValue(0)
        self.animSapa.finished.connect(self.delete)
        self.animSapa.start()

    def delete(self): 
        self.hide()
        self.window.FullScreen()



            
