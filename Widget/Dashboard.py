from PySide6.QtWidgets import QWidget,QSizePolicy,QHBoxLayout,QVBoxLayout,QPushButton
from PySide6.QtCore import Qt,QPropertyAnimation,QRect

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
        self.window = window
  
        
        self.anim = QPropertyAnimation(self,b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.window.width() * 0.2, self.window.height() * 0.55 ,0,0))
        self.anim.setEndValue(QRect(self.window.width() * 0.075,self.window.height() * 0.325, self.window.width() * 0.25,self.window.height() * 0.45 ))

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