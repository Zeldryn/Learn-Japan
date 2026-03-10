from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QTimer
import json
import os
import time
from Pages.secondWindow import Dashboard


path = "Database/user.json"

def loadData():
    if not os.path.exists(path):
        return [{
            "Account" :
                {
                    "username" : "",
                    "password" : ""
                }
                }]
    
    try:
        with open(path,"r") as r:
            return json.load(r)
    except json.JSONDecodeError:
        return [{
            "Account" :
            {
                "username" : "",
                "password" : ""
            }
        }]
    


class Button(QPushButton):
    def __init__(self,id,window,uDisplay,pDisplay):
        super().__init__()
        self.id = id
        self.window = window
        self.uDisplay = uDisplay
        self.pDisplay = pDisplay
        self.data = loadData()
        
        #Flag
        self.checkButton = False

        if self.id == "submitButton":
            self.setText("Login")
            self.setStyleSheet("""QPushButton {
                                background-color : rgba(234, 239, 239, 0.8);
                                color:black;
                                border: 2px solid transparent;
                                border-radius: 5px;}
                               
                                QPushButton:hover {
                                    background-color : rgba(234, 239, 239, 0.6)
                                } 
                                
                                QPushButton:pressed {
                                background-color : rgba(234, 239, 239, 0.3)}""")
            self.clicked.connect(self.login)

        elif self.id == "registButton":
            self.setText("Register")
            self.setStyleSheet("""QPushButton {
                                background-color : rgba(234, 239, 239, 0.8);
                                color:black;
                                border: 2px solid transparent;
                                border-radius: 5px;}
                               
                                QPushButton:hover {
                                    background-color : rgba(234, 239, 239, 0.6)
                                } 
                                
                                QPushButton:pressed {
                                background-color : rgba(234, 239, 239, 0.3)}""")
            
            self.clicked.connect(self.registLogic)
            
        
        elif self.id == "registSubmitButton":
            self.setText("Register")

    def login(self):
        foundAccount = False
        for username,value in self.data["Account"].items():
            if self.uDisplay.text() == username and self.pDisplay.text() == value["password"]:
                self.username = username
                self.window.wLogin.window.username = username
                self.window.wLogin.animLoginFinish.finished.connect(self.login1)
                self.window.wLogin.animLoginFinish.start()
 
                foundAccount = True


        
        if not foundAccount:
            self.window.tfLogin.setText(f"Can't Found The Accout With {self.uDisplay.text()} Username")
            self.window.tfLogin.show()



    
    def login1(self):
            self.window.wLogin.window.LoginPage.hide()
            self.window.wLogin.window.sapaLogin.setText(f"Hello {self.username}")
            self.window.wLogin.window.sapaLogin.show()
            self.window.wLogin.window.sapaLogin.animSapa.start()
    

    def registLogic(self):
        self.window.wLogin.window.registPage.show()