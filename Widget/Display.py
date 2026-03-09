from PySide6.QtWidgets import QLineEdit
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
        
        