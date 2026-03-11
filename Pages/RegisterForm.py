from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout, QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QRect,QPoint
from Widget.Label import Label
from Widget.trueRegist import trueRegist

class Register(QWidget):
    def __init__(self,window):
        super().__init__(window)
        self.window = window
        self.widthAva = self.screen().availableGeometry().width()
        self.heightAva = self.screen().availableGeometry().height()
        self.mainX = self.window.width()
        self.mainY = self.window.height()
        self.hide()
        self.setObjectName("mainRegist")
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setMinimumSize(self.window.width() * 0.3,self.window.height() * 0.8)
        self.setStyleSheet("""#mainRegist {
                           border : 2px none;

                           border-radius: 10px;
                           background-color: rgba(35, 76, 106, 0.6);
                           }
                           
                           #mainLogin:hover {
                           border : 2px solid rgba(69, 104, 130, 1);

                           
                           }""")
        #Widget
        self.rTitle = Label("titleRegist",self)
        self.trueRegist =  trueRegist(self)
    
        
        self.registLayout = QVBoxLayout(self)
        self.registLayout.setContentsMargins(15,100,15,100)
        self.registLayout.setSpacing(20)
        self.registLayout.addWidget(self.rTitle,alignment=Qt.AlignTop | Qt.AlignCenter)
        self.registLayout.addWidget(self.trueRegist,alignment=Qt.AlignCenter)

        self.opacityEffect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacityEffect)
        self.opacityEffect.setOpacity(0)

        self.animIn = QPropertyAnimation(self.opacityEffect, b"opacity")
        self.animIn.setDuration(1500)
        self.animIn.setStartValue(0)
        self.animIn.setEndValue(1)

        self.animOut = QPropertyAnimation(self.opacityEffect,b'opacity')
        self.animOut.setDuration(1000)
        self.animOut.setStartValue(1)
        self.animOut.setEndValue(0)
   
        