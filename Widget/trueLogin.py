from PySide6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QSizePolicy,QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint,QTimer, QUrl
from Widget.Display import Display
from Widget.Button import Button
class Main(QWidget):
    def __init__(self,wLogin):
        super().__init__(wLogin)
        self.wLogin = wLogin
        self.setObjectName("Main")
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setStyleSheet("""
                            #Main {
                            background-color: rgba(69, 104, 130, 0.5);
                            border: none 2px;
                            border-radius:10px;
                            }""")
        

        self.uDisplay = Display("usernameDisplay",self)
        self.pDisplay = Display("passwordDisplay",self)
        self.sButton = Button("submitButton",self)
        self.rButton = Button("registButton",self)
        self.truloginLayout = QVBoxLayout(self)
        self.truloginLayout.setContentsMargins(10,140,10,10)
        self.truloginLayout.addWidget(self.uDisplay,alignment=Qt.AlignCenter)
        self.truloginLayout.addWidget(self.pDisplay,alignment=Qt.AlignCenter)
        self.truloginLayout.addStretch()
        self.truloginLayout.addWidget(self.sButton,alignment=Qt.AlignCenter)
        self.truloginLayout.addWidget(self.rButton,alignment=Qt.AlignCenter)

        self.truloginLayout.addStretch()
