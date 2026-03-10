from  PySide6.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout,QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation,QPoint,QTimer,Qt
from Widget.Label import Label
from Widget.trueLogin import Main


class Login(QWidget):
    def __init__(self,window):
        super().__init__(window)
        self.window = window
        self.setObjectName("mainLogin")
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setStyleSheet("""#mainLogin {
                           border : 2px none;

                           border-radius: 10px;
                           background-color: rgba(35, 76, 106, 0.6);
                           }
                           
                           #mainLogin:hover {
                           border : 2px solid rgba(69, 104, 130, 1);

                           
                           }""")
        

        self.titleText = Label("titleLogin",self)
        self.dLogin = Main(self)

        self.loginLayout = QVBoxLayout(self)
        margins = self.loginLayout.contentsMargins()
        self.loginLayout.setContentsMargins(15,90,15,100)
        self.loginLayout.setSpacing(20)
        self.loginLayout.addStretch()
        self.loginLayout.addWidget(self.titleText,alignment=Qt.AlignTop | Qt.AlignCenter)
        self.loginLayout.addWidget(self.dLogin)
        self.loginLayout.addStretch()
        

        self.animLogin = QPropertyAnimation(self, b"pos")
        self.animLogin.setDuration(1500)
        self.animLogin.setStartValue(QPoint(self.window.pos().x() - 300,self.pos().y() + 40))
        self.animLogin.setEndValue(QPoint(self.window.xLogin + 51,self.pos().y() + 50))

        self.animLoginFinish = QPropertyAnimation(self, b"pos")
        self.animLoginFinish.setDuration(1500)
        self.animLoginFinish.setStartValue(QPoint(self.pos().x(),self.pos().y() + 40))
        self.animLoginFinish.setEndValue(QPoint(self.pos().x() - 1000,self.pos().y() + 40))
