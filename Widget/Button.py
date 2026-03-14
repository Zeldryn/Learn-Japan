from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QTimer,Qt
from PySide6.QtGui import QFont
import json
import os
import time
from Pages.secondWindow import Dashboard



path = "Database/user.json"

def loadData():
    if not os.path.exists(path):
        return {
            "Account" :
                {}
                }
    
    try:
        with open(path,"r") as r:
            return json.load(r)
    except json.JSONDecodeError:
        return {
            "Account" :
            {}
        }


    


class Button(QPushButton):
    def __init__(self,id,window,uDisplay,pDisplay):
        super().__init__()
        self.id = id
        self.window = window
        self.uDisplay = uDisplay
        self.pDisplay = pDisplay
        self.data = loadData()
        self.Font = QFont()
        self.dashboard = Dashboard()
        
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
            self.setStyleSheet("""QPushButton {
                    background-color : rgba(255, 255, 255, 1);
                    color: black;
                    }
                    
                    QPushButton:hover {
                    background-color : rgba(255, 255, 255, 0.7)}
                    
                    QPushButton:pressed {
                    background-color : rgba(255, 255, 255, 0.4)}""")
            self.Font.setPointSize(15)
            self.clicked.connect(self.submitRegist)

            self.setFont(self.Font)

        elif self.id == "registCButton" :
            self.setText("C")
            self.setStyleSheet("""QPushButton {
                               background-color : rgba(255, 255, 255, 1);
                               color: red;

                               }
                               
                               QPushButton:hover {
                               background-color : rgba(255, 255, 255, 0.7)}
                               
                               QPushButton:pressed {
                               background-color : rgba(255, 255, 255, 0.4)}""")
            self.Font.setPointSize(20)

            self.setFont(self.Font)



    def login(self):
        self.data = loadData()
        foundAccount = False
        for username,value in self.data["Account"].items():
            if self.uDisplay.text() == username and self.pDisplay.text() == value["password"]:
                self.username = username
                self.window.wLogin.window.username = username
                self.window.wLogin.animLoginFinish.finished.connect(self.login1)
                self.window.wLogin.animLoginFinish.start()
                self.window.wLogin.window.registPage.animOut.start()
 
                foundAccount = True


        
        if not foundAccount:
            self.window.tfLogin.setText(f"Can't Found The Account With {self.uDisplay.text()} Username")
            self.window.tfLogin.show()



    
    def login1(self):
            self.window.wLogin.window.registPage.hide()
            self.window.wLogin.window.LoginPage.hide()
            self.window.wLogin.window.sapaLogin.setText(f"Hello {self.username}")
            self.window.wLogin.window.sapaLogin.show()
            self.window.wLogin.window.sapaLogin.animSapa.finished.connect(self.openWindow2,Qt.SingleShotConnection)
            self.window.wLogin.window.sapaLogin.animSapa.start()
    

    def registLogic(self):
        self.window.wLogin.window.registPage.show()
        self.window.wLogin.window.registPage.animIn.start()

    def submitRegist(self):
        self.data["Account"][self.window.window.window.registPage.trueRegist.usernameRegistDisplay.text()] = {
            "password"  : self.window.window.window.registPage.trueRegist.passwordRegistDisplay.text(),
            "firstName" : self.window.window.window.registPage.trueRegist.displayFName.text(),
            "lastName"  : self.window.window.window.registPage.trueRegist.displayLName.text(),
            "email"     : self.window.window.window.registPage.trueRegist.emailDisplay.text(),
            "day"     : self.window.window.window.registPage.trueRegist.dayDisplay.text(),
            "month"     : self.window.window.window.registPage.trueRegist.monthDisplay.text(),
            "years"     : self.window.window.window.registPage.trueRegist.yearDisplay.text(),

        }

        with open(path,"w") as w:
            json.dump(self.data,w,indent=4)

        self.data = loadData()

    
    def refreshData(self):
        self.data = self.loadData()

    def openWindow2(self):
        self.dashboard.show()
        self.dashboard.showMaximized()
        self.window.wLogin.window.hide()
        QTimer.singleShot(0,self.dashboard.profileDashboard.anim.start)
        QTimer.singleShot(0,self.dashboard.mainButton.anim.start)
        QTimer.singleShot(0,self.dashboard.mainButton2.anim.start)
        QTimer.singleShot(0,self.dashboard.mainButton3.anim.start)
        QTimer.singleShot(0,self.dashboard.textMB.animHM.start)
        QTimer.singleShot(0,self.dashboard.textMB1.animHM.start)
        QTimer.singleShot(0,self.dashboard.textMB2.animHM.start)





