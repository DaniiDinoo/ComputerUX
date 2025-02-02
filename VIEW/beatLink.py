from PySide6.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QDockWidget, QToolBar, QWidget, QSizePolicy,
                               QStatusBar, QMessageBox, QInputDialog, QPushButton)
from PySide6.QtCore import Qt, QTimer
from pathlib import Path
from PySide6.QtGui import QPixmap, QIcon, QAction, QGuiApplication, QMovie
from qt_material import apply_stylesheet
import qtawesome as qta  #https://fontawesome.com/v5/search?o=r&m=free&s=solid
import sys



class Box(QLabel):
    def __init__(self, color: str):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')

    def setBoxText(self, newText: str):
        self.setText(newText)

class Splash(QLabel):
    def __init__(self, bgColor: str, mainInstance):
        super().__init__()
        
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f'background-color: {bgColor}')
        self.heartGif = QMovie(mainInstance.getRightPath('mediumHeart.gif'))
        # self.heartGif.setScaledSize(self.size())
        self.setMovie(self.heartGif)
        self.heartGif.start() 
        
        
class boton(QPushButton):
    def __init__(self, iconID: str):
        super().__init__()
        auxIcon = qta.icon(iconID, color = '#65dfd5')
        self.setIcon(auxIcon)




class BeatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BeatLink")
        self.heartIcon = QIcon(self.getRightPath('heartIcon.png'))
        self.smallHeart = QPixmap(self.getRightPath('small.png'))

        self.resize(1400,700)
        self.setWindowIcon(self.heartIcon)

        heartSplash = Splash('#4CC6E0', self)
        self.setCentralWidget(heartSplash)

        QTimer.singleShot(4000, self.realApp)



    def realApp(self):


        self.idAndName = Box("#373d43")
        self.registerBox = Box("#373d43")
        leftVPane = QVBoxLayout()
        leftVPane.addWidget(self.idAndName,2)
        leftVPane.addWidget(self.registerBox,17)

        self.upArrowButton = boton("fa5s.angle-double-up")
        self.upArrowButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.downArrowButton = boton("fa5s.angle-double-down")
        self.downArrowButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.upArrowButton.pressed.connect(self.upArrowPressed)
        self.downArrowButton.pressed.connect(self.downArrowPressed)

        verticalButtons = QVBoxLayout()
        verticalButtons.addWidget(self.upArrowButton, 1)
        verticalButtons.addWidget(self.downArrowButton, 1)


        ecgSignalBox = Box("#373d43")
        horiSignal = QHBoxLayout()
        horiSignal.addLayout(verticalButtons, 1)
        horiSignal.addWidget(ecgSignalBox, 15)

        leftStat = Box("#373d43")
        mediumStat = Box("#373d43")
        rightStat = Box("#373d43")
        horiStats = QHBoxLayout()
        horiStats.addWidget(leftStat)
        horiStats.addWidget(mediumStat)
        horiStats.addWidget(rightStat)

        historical = Box("#373d43")
        signalInfo =Box("#373d43")
        horiInfo = QHBoxLayout()
        horiInfo.addWidget(historical, 2)
        horiInfo.addWidget(signalInfo, 3)

        rightVPane = QVBoxLayout()
        rightVPane.addLayout(horiSignal, 2)
        rightVPane.addLayout(horiStats, 3)
        rightVPane.addLayout(horiInfo, 2)


        leftRightLayout = QHBoxLayout()
        leftRightLayout.addLayout(leftVPane, 1)
        leftRightLayout.addLayout(rightVPane, 8)

        dummyWidget = QWidget()
        dummyWidget.setLayout(leftRightLayout)

        self.setCentralWidget(dummyWidget)

        


        #self.setCentralWidget(cajona)





        self.setStatusBar(QStatusBar(self))
        #Call the Menu Builder
        self.menuBuilder()
        self.toolBuilder()


    def menuBuilder(self):
        menuBar = self.menuBar()
        #FILE TAB CREATION
        fileTab = menuBar.addMenu("   &File   ")

        self.selectRegister = QAction('Select Register', self)
        self.selectRegister.setShortcut('Ctrl+R')
        openRegistericon = qta.icon('fa5s.file-medical-alt', color = '#65dfd5')
        self.selectRegister.setIcon(openRegistericon)
        self.selectRegister.setStatusTip("Select electrocardiographical register")
        self.selectRegister.triggered.connect(self.openRegisterPressed)

        self.selectPacient = QAction("Select a Pacient", self)
        self.selectPacient.setShortcut('Ctrl+P')
        pacienteIcon = qta.icon('fa5s.id-badge', color = '#65dfd5')
        self.selectPacient.setIcon(pacienteIcon)
        self.selectPacient.setStatusTip('Select a pacient to access them data')
        self.selectPacient.triggered.connect(self.selectPacientPressed)

        self.refresh = QAction('Refresh Database', self)
        self.refresh
    
        fileTab.addAction(self.selectPacient)
        fileTab.addAction(self.selectRegister)

        #VIEW TAB CREATION
        viewTab = menuBar.addMenu("   &View   ")


        #HELP TAB CREATION
        helpTab = menuBar.addMenu("   &Help   ")

        self.openUserGuide = QAction("Open User Guide", self)
        self.openUserGuide.setShortcut("Ctrl+D")
        openUGIcon = qta.icon('fa5s.file-alt', color = '#65dfd5')
        self.openUserGuide.setIcon(openUGIcon)
        self.openUserGuide.setStatusTip("Detailed guide for users")
        self.openUserGuide.triggered.connect(self.openUGPressed)

        welcome = QAction("Welcome", self)
        welcomeIcon = qta.icon('fa5s.medkit', color = '#65dfd5')
        welcome.setIcon(welcomeIcon)
        welcome.setStatusTip('Open Welcome message')
        welcome.triggered.connect(self.launchWelcome)

        helpTab.addAction(welcome)
        helpTab.addAction(self.openUserGuide)

    def toolBuilder(self):
        tools = QToolBar("Utilities")
        tools.setOrientation(Qt.Vertical)
        tools.addAction(self.selectPacient)
        tools.addAction(self.selectRegister)
        tools.addAction(self.openUserGuide)

        self.addToolBar(Qt.LeftToolBarArea, tools)
        




    def openRegisterPressed(self):
        print("Open register request")

    def openUGPressed(self):
        print("The documentation has been opened in the browser")

    def launchWelcome(self):
        pass

    def selectPacientPressed(self):
        print("Enter the user ID")


    def getRightPath(self, imageName: str)-> str:
        """This method returns the right direction of an specific image in the system
        always the image is located in the image folder

        Args:
            imageName (str): Name (with extension) of the image

        Returns:
            str: The real path
        """
        currenDir = Path(__file__).parent
        rightPath: str = str(currenDir/'images'/imageName)
        return rightPath
    

    def upArrowPressed(self):
        print("Up arrow button presed")


    def downArrowPressed(self):
        print("Down arrow button pressed")

