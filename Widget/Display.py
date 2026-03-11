from PySide6.QtWidgets import QLineEdit, QSizePolicy
from PySide6.QtCore import Qt,QPoint
from PySide6.QtGui import QFont
class Display(QLineEdit):
    def __init__(self,id,window):
        super().__init__(window)
        self.id = id
        self.window = window

        self.font= QFont()
        
        if self.id == "usernameDisplay":
            self.setPlaceholderText("Username")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)
            self.font.setPointSize(15)
            self.setFont(self.font)

        elif self.id == "passwordDisplay":
            self.setPlaceholderText("Password")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)
            self.font.setPointSize(15)
            self.setFont(self.font)
            self.setEchoMode(QLineEdit.Password)
        
        elif self.id == "firstNameDisplay":
            self.setPlaceholderText("First Name")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)
            
        elif self.id == "lastNameDisplay":
            self.setPlaceholderText("Last Name")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)

        elif self.id == "usernameRegistDisplay":
            self.setPlaceholderText("Username")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)
            self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.setMinimumHeight(window.height() *0.1)
            self.setMinimumWidth(window.width() * 0.8)

        elif self.id == "passwordRegistDisplay":
            self.setPlaceholderText("********")
            self.setEchoMode(QLineEdit.Password)
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)
            self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.setMinimumHeight(window.height() *0.1)
            self.setMinimumWidth(window.width() * 0.8)

        elif self.id == "emailDisplay":
            self.setPlaceholderText("YourEmail@Gmail.com")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)
            self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
            self.setMinimumHeight(window.height() *0.1)
            self.setMinimumWidth(window.width() * 0.8)

        elif self.id == "dayDisplay":
            self.setPlaceholderText("0")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)

        elif self.id == "monthDisplay":
            self.setPlaceholderText("0")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)
        
        elif self.id == "yearDisplay":
            self.setPlaceholderText("0")
            self.setReadOnly(False)
            self.setAlignment(Qt.AlignCenter)
