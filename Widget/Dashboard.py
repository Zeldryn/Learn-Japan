from PySide6.QtWidgets import QWidget,QSizePolicy,QHBoxLayout,QVBoxLayout,QPushButton
from PySide6.QtCore import Qt,QPropertyAnimation,QRect
from PySide6.QtGui import QFont
from Widget.blackScreenHelper import blackScreen

from Widget.Label import Label


class profileDashboard(QWidget):
    def __init__(self,window):
        super().__init__(window)
        self.window = window
        self.setObjectName("line")
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.setStyleSheet("""#line{
                           background-color : transparent;
                           border : none;
                           border-bottom : 2px solid #005461;
                           }""")
        

        self.anim = QPropertyAnimation(self,b"geometry")
        self.anim.setDuration(2500)
        self.anim.setStartValue(QRect(self.window.width() // 2,0,0,self.window.height() * 0.05))
        self.anim.setEndValue(QRect(0,0,self.window.width(),self.window.height() * 0.05))
        self.anim.finished.connect(self.Text,Qt.SingleShotConnection)

        self.textMain = Label("TextLH",self)
        self.layout = QVBoxLayout(self)
        self.secondLayout = QHBoxLayout()
        self.layout.addLayout(self.secondLayout)
     





    def Text(self):
        self.textMain.setText("Learn Japan Demo Version")
        self.secondLayout.addWidget(self.textMain,alignment=Qt.AlignCenter)

class MainButton(QPushButton):
    def __init__(self,window):
        super().__init__()
        self.Expanding = False    
        self.window = window
        self.clicked.connect(self.Pesan)
        self.font = QFont()
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setObjectName("B1") 
        self.setStyleSheet("""#B1{
                           background-image: url(Image/AnyImage/DashboardImage/hiraganaImage.jpg);
                           background-position:center;
                           border: 5px solid rgba(0, 183, 181, 1);
                           border-radius: 20px;
                           }


                           #B1:pressed {
                            border: 5px solid rgba(0, 183, 181, 0.3);
                            border-radius: 20px;
                           }
                           """)
        
        self.blackScreen = QWidget(self)
        self.blackScreen.setStyleSheet("""
                            QWidget{
                                background-color: rgba(0,0,0,0.5);
                                border: 2px solid transparent;
                                border-radius: 20px;
                                       }
                            
                            QWidget:hover {
                                background-color: rgba(0,0,0,0.2);
                                border: 2px solid transparent;
                                border-radius: 20px;}           
                                       """)
        self.blackScreen.setGeometry(self.contentsRect())
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.blackScreen)


        self.anim = QPropertyAnimation(self,b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.window.width() * 0.2, self.window.height() * 0.55 ,0,0))
        self.anim.setEndValue(QRect(self.window.width() * 0.075,self.window.height() * 0.325, self.window.width() * 0.25,self.window.height() * 0.45 ))
        self.anim.finished.connect(self.flag1)

    def flag1(self):
        self.Expanding = True

    def Pesan(self):
        print("Ditekan")

    
    def enterEvent(self,event):
        if self.Expanding == True:
            self.anim1 = QPropertyAnimation(self,b"geometry")
            self.anim1.setDuration(100)
            self.anim1.setStartValue(QRect(self.window.width() * 0.075,self.window.height() * 0.325, self.window.width() * 0.25,self.window.height() * 0.45))
            self.anim1.setEndValue(QRect(self.window.width()*0.0625,self.window.height()*0.3025,self.window.width()*0.275,self.window.height()*0.495))
            self.anim1.start()
    
    def leaveEvent(self,event):
        if self.Expanding == True:
            self.anim2 = QPropertyAnimation(self,b"geometry")
            self.anim2.setDuration(100)
            self.anim2.setStartValue(QRect(self.window.width()*0.0625,self.window.height()*0.3025,self.window.width()*0.275,self.window.height()*0.495))
            self.anim2.setEndValue(QRect(self.window.width() * 0.075,self.window.height() * 0.325, self.window.width() * 0.25,self.window.height() * 0.45 ))
            self.anim2.start()


class MainButton2(QPushButton):
    def __init__(self,window):
        super().__init__()
        self.window = window
  
        
        self.anim = QPropertyAnimation(self,b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.window.width() * 0.5, self.window.height() * 0.55 ,0,0))
        self.anim.setEndValue(QRect(self.window.width() * 0.375,self.window.height() * 0.325, self.window.width() * 0.25,self.window.height() * 0.45 ))

class MainButton3(QPushButton):
    def __init__(self,window):
        super().__init__()
        self.window = window
  
        
        self.anim = QPropertyAnimation(self,b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.window.width() * 0.8, self.window.height() * 0.55 ,0,0))
        self.anim.setEndValue(QRect(self.window.width() * 0.675,self.window.height() * 0.325, self.window.width() * 0.25,self.window.height() * 0.45 ))