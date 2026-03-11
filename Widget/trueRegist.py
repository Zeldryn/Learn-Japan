from PySide6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QSizePolicy,QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint,QTimer, QUrl
from Widget.Display import Display
from Widget.Button import Button
from Widget.Label import Label

class trueRegist(QWidget):
    def __init__(self,window):
        super().__init__(window)
        self.setObjectName("Main")
        self.window = window
        self.setMinimumSize(self.window.width() * 0.8, self.window.height() * 0.6)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setStyleSheet("""
                            #Main {
                            background-color: rgba(69, 104, 130, 0.5);
                            border: none 2px;
                            border-radius:10px;
                            }""")
        #Widget Display
        self.displayFName = Display("firstNameDisplay",self)
        self.displayLName = Display("lastNameDisplay",self)
        self.usernameRegistDisplay = Display("usernameRegistDisplay",self)
        self.passwordRegistDisplay = Display("passwordRegistDisplay",self)
        self.emailDisplay = Display("emailDisplay",self)
        self.dayDisplay   = Display("dayDisplay",self)
        self.monthDisplay = Display("monthDisplay",self)
        self.yearDisplay  = Display("yearDisplay",self)

        #Button Widget
        self.submitButton = Button("registSubmitButton",self,None,None)
        self.cSubmitButton = Button("registCButton",self,None,None)

        #Widget Label
        self.textRegistFName = Label("textRegistFName",self)
        self.textRegistLName = Label("textRegistLName",self)
        self.textRegistUsername = Label("textRegistUsername",self)
        self.textRegistPassword = Label("textRegistPassword",self)
        self.textRegistEmail = Label("textRegistEmail",self)
        self.textRegistDay = Label("textRegistDay",self)
        self.textRegistMonth =Label("textRegistMonth",self)
        self.textRegistYear = Label("textRegistYear",self)
        
        

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setSpacing(8)
        self.mainLayout.setContentsMargins(20,80,20,20)
        margins = self.mainLayout.contentsMargins()
        self.hbox1 = QHBoxLayout()
        self.hbox1.setSpacing(10)
        self.hboxPw = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox4.setSpacing(5)


        self.hbox1Text = QHBoxLayout()
        self.hbox1Text.setContentsMargins(10,10,20,0)
        self.hbox2Text = QHBoxLayout()
        self.hboxPwText = QHBoxLayout()
        self.hbox3Text = QHBoxLayout()

        self.hbox4Text = QHBoxLayout()

        self.hbox5 = QHBoxLayout()
        self.hbox5.setContentsMargins(10,20,10,10)

        self.hbox5.setSpacing(3)




    
        self.mainLayout.addLayout(self.hbox1Text)
        self.mainLayout.addLayout(self.hbox1)

        self.mainLayout.addLayout(self.hbox2Text)
        self.mainLayout.addLayout(self.hbox2)

        self.mainLayout.addLayout(self.hboxPwText)
        self.mainLayout.addLayout(self.hboxPw)

        self.mainLayout.addLayout(self.hbox3Text)
        self.mainLayout.addLayout(self.hbox3)

        self.mainLayout.addLayout(self.hbox4Text)
        self.mainLayout.addLayout(self.hbox4)

        self.mainLayout.addLayout(self.hbox5)


        
        
        self.hbox1Text.addWidget(self.textRegistFName,alignment=Qt.AlignCenter)
        self.hbox1Text.addWidget(self.textRegistLName,alignment=Qt.AlignCenter)

        self.hbox1.addStretch()
        self.hbox1.addWidget(self.displayFName,alignment=Qt.AlignCenter)
        self.hbox1.addWidget(self.displayLName,alignment=Qt.AlignCenter)
        self.hbox1.addStretch()

        self.hbox2Text.addWidget(self.textRegistUsername,alignment=Qt.AlignCenter)
        self.hbox2.addWidget(self.usernameRegistDisplay,alignment=Qt.AlignCenter)
        self.mainLayout.addStretch()

        self.hboxPwText.addWidget(self.textRegistPassword,alignment=Qt.AlignCenter)
        self.hboxPw.addWidget(self.passwordRegistDisplay,alignment=Qt.AlignCenter)

        self.hbox3Text.addWidget(self.textRegistEmail,alignment=Qt.AlignCenter)
        self.hbox3.addWidget(self.emailDisplay,alignment=Qt.AlignCenter)

        self.hbox4Text.addStretch()

        self.hbox4Text.addWidget(self.textRegistYear,alignment=Qt.AlignCenter)
        self.hbox4Text.addStretch()
        
        self.hbox4.addStretch()
        self.hbox4.addWidget(self.dayDisplay,alignment=Qt.AlignLeft)
        self.hbox4.addWidget(self.monthDisplay,alignment=Qt.AlignCenter)
        self.hbox4.addWidget(self.yearDisplay,alignment=Qt.AlignRight)
        self.hbox4.addStretch()


        self.hbox5.addStretch()
        self.hbox5.addWidget(self.submitButton,alignment=Qt.AlignCenter)
        self.hbox5.addWidget(self.cSubmitButton,alignment=Qt.AlignCenter)
        self.hbox5.addStretch()


        