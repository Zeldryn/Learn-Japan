import json
import sys
from PySide6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QSizePolicy,QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint,QTimer, QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtGui import QCursor,QMouseEvent, QIcon,QPixmap,QPalette,QBrush

#import Local
from Widget.Label import Label
from Pages.Login import Login
from Pages.RegisterForm import Register

from PySide6.QtMultimediaWidgets import QVideoWidget
import time
import random
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setObjectName("mainWindow")
        self.setStyleSheet("""#mainWindow {
            background-color : #1B3C53;
            }""")
        self.xLogin = 0
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.monitorSizeHeight  = self.screen().availableGeometry().height()
        self.monitorSizeWidth   = self.screen().availableGeometry().width()
        self.resize(self.monitorSizeWidth * 0.3 ,self.monitorSizeHeight * 0.3)
        self.setWindowTitle("Learn Japan (Welcome)")
        self.setWindowIcon(QIcon("Image/Icon/mainIcon.png"))

        self.setMinimumSize(self.monitorSizeWidth * 0.2,self.monitorSizeHeight * 0.5)

        #Widget
        self.sapa = Label("sapaMain",self)
        self.LoginPage = Login(self)
        self.LoginPage.hide()
        self.sapaLogin = Label("successLogin",self)
        self.registPage = Register(self)


        self.mainLayout = QVBoxLayout(self)
        self.secondLayout = QHBoxLayout()

        self.mainLayout.addLayout(self.secondLayout)
        self.secondLayout.addWidget(self.LoginPage,alignment=Qt.AlignLeft)
        self.secondLayout.addWidget(self.registPage,alignment=Qt.AlignRight)
        self.secondLayout.addWidget(self.sapaLogin,alignment=Qt.AlignCenter)
        margins = self.secondLayout.contentsMargins()
        self.secondLayout.setContentsMargins(40,2,30,2)
        self.mainLayout.addWidget(self.sapa,alignment=Qt.AlignCenter)

        #Flag
        self.maxWidget = False
        self.changeTitle = False

        


 
    def resizeEvent(self,event):


        #LoginPage
        if  self.width() <= self.monitorSizeWidth * 0.22:
            self.LoginPage.setMinimumWidth(self.width() * 0.8)
            self.LoginPage.setMinimumHeight(self.height() * 0.6)
            self.LoginPage.setMaximumHeight(self.height() * 0.9)
        elif self.width() <= self.monitorSizeWidth * 0.4 and self.width() >= self.monitorSizeWidth * 0.22:
            self.LoginPage.setMinimumWidth(self.width() * 0.6)
            self.LoginPage.setMinimumHeight(self.height() * 0.6)
            self.LoginPage.setMaximumHeight(self.height() * 0.9)      
        elif self.width() <= self.monitorSizeWidth * 0.6 and self.width() >= self.monitorSizeWidth * 0.4:
            self.LoginPage.setMinimumWidth(self.width() * 0.4)
            self.LoginPage.setMinimumHeight(self.height() * 0.6)
            self.LoginPage.setMaximumHeight(self.height() * 0.9)    
        else: 
            self.LoginPage.setMinimumWidth(self.width() * 0.25)
            self.LoginPage.setMinimumHeight(self.height() * 0.6)
            self.LoginPage.setMaximumHeight(self.height() * 0.9)


        #dLogin
        self.LoginPage.dLogin.setMinimumSize(self.LoginPage.width() * 0.6, self.LoginPage.height() * 0.8)
        self.LoginPage.dLogin.uDisplay.setMinimumSize(self.LoginPage.width() * 0.8, self.LoginPage.height() * 0.1)
        self.LoginPage.dLogin.pDisplay.setMinimumSize(self.LoginPage.width() * 0.8, self.LoginPage.height() * 0.1)
        self.LoginPage.dLogin.sButton.setMinimumSize(self.LoginPage.width() * 0.6, self.LoginPage.height() * 0.1)
        self.LoginPage.dLogin.rButton.setMinimumSize(self.LoginPage.width() * 0.6, self.LoginPage.height() * 0.1)

        #Register
        self.registPage.setMinimumSize(self.width() * 0.25,self.height() * 0.8)
        self.registPage.setMaximumSize(self.width() * 0.25,self.height() * 1)

        if  self.width() <= self.monitorSizeWidth * 0.22:
            self.registPage.setMinimumWidth(self.width() * 0.8)
            self.registPage.setMinimumHeight(self.height() * 0.6)
            self.registPage.setMaximumHeight(self.height() * 0.9)
        elif self.width() <= self.monitorSizeWidth * 0.4 and self.width() >= self.monitorSizeWidth * 0.22:
            self.registPage.setMinimumWidth(self.width() * 0.6)
            self.registPage.setMinimumHeight(self.height() * 0.6)
            self.registPage.setMaximumHeight(self.height() * 0.9)      
        elif self.width() <= self.monitorSizeWidth * 0.6 and self.width() >= self.monitorSizeWidth * 0.4:
            self.registPage.setMinimumWidth(self.width() * 0.4)
            self.registPage.setMinimumHeight(self.height() * 0.6)
            self.registPage.setMaximumHeight(self.height() * 0.9)    
        else: 
            self.registPage.setMinimumWidth(self.width() * 0.3)
            self.registPage.setMinimumHeight(self.height() * 0.6)
            self.registPage.setMaximumHeight(self.height() * 0.9)
        
        self.registPage.trueRegist.setMinimumSize(self.registPage.width() *0.8, self.registPage.height() * 0.8)
        self.registPage.trueRegist.setMaximumSize(self.registPage.width() *0.8, self.registPage.height() * 0.8)

        self.registPage.trueRegist.displayFName.setMinimumSize(self.registPage.trueRegist.width() * 0.4, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.displayLName.setMinimumSize(self.registPage.trueRegist.width() * 0.4, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.displayFName.setMaximumSize(self.registPage.trueRegist.width() * 0.4, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.displayLName.setMaximumSize(self.registPage.trueRegist.width() * 0.4, self.registPage.trueRegist.height() * 0.07)

        self.registPage.trueRegist.passwordRegistDisplay.setMinimumSize(self.registPage.trueRegist.width() * 0.83, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.usernameRegistDisplay.setMinimumSize(self.registPage.trueRegist.width() * 0.83, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.emailDisplay.setMinimumSize(self.registPage.trueRegist.width() * 0.83, self.registPage.trueRegist.height() * 0.07)
       
        #Month-Day-Years Birth
        self.registPage.trueRegist.dayDisplay.setMinimumSize(self.registPage.trueRegist.width() * 0.27, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.monthDisplay.setMinimumSize(self.registPage.trueRegist.width() * 0.27, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.yearDisplay.setMinimumSize(self.registPage.trueRegist.width() * 0.27, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.dayDisplay.setMaximumSize(self.registPage.trueRegist.width() * 0.27, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.monthDisplay.setMaximumSize(self.registPage.trueRegist.width() * 0.27, self.registPage.trueRegist.height() * 0.07)
        self.registPage.trueRegist.yearDisplay.setMaximumSize(self.registPage.trueRegist.width() * 0.27, self.registPage.trueRegist.height() * 0.07)


    def FullScreen(self):
        if self.sapa.isHidden() and not self.maxWidget:
            self.LoginPage.show()
            self.showMaximized()
            self.maxWidget = True
            self.changeTitle = True

            self.LoginPage.animLogin.start()
            if self.changeTitle == True:
                self.setWindowTitle("Learn Japan (Login)")
            




app = QApplication(sys.argv)

window = Window()
window.show()
app.exec()

