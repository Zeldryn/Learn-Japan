from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from Widget.Dashboard import profileDashboard, MainButton, MainButton2, MainButton3
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        print(self.width())
        self.resize(self.screen().availableGeometry().width(),self.screen().availableGeometry().height())
        self.setFixedSize(self.screen().availableGeometry().width(),self.screen().availableGeometry().height())
        self.setWindowTitle("Home")
        self.setWindowIcon(QIcon("Image/Icon/mainIcon.png"))
        self.profileDashboard = profileDashboard(self)
        self.profileDashboard.setParent(self)

        
        self.mainButton = MainButton(self)
        self.mainButton.setParent(self)

        self.mainButton2 = MainButton2(self)
        self.mainButton2.setParent(self)

        self.mainButton3 = MainButton3(self)
        self.mainButton3.setParent(self)

    
