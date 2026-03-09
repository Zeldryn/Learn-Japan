from PySide6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self,id,window):
        super().__init__()
        self.id = id
        self.window = window
        
        if self.id == "submitButton":
            self.setText("Login")
        elif self.id == "registButton":
            self.setText("Register")
    