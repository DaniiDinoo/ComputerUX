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


class IDLabel(QLabel):
    def __init__(self, id: str, color: str):
        super().__init__()
        self.setText(id)
        self.setStyleSheet(f'background-color: {color}')


class Splash(QLabel):
    def __init__(self, bgColor: str, mainInstance):
        super().__init__()
        
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f'background-color: {bgColor}')
        self.heartGif = QMovie(mainInstance.getRightPath('mediumHeart.gif'))
        # self.heartGif.setScaledSize(self.size())
        self.setMovie(self.heartGif)
        self.heartGif.start() 



class Boton(QPushButton):
    def __init__(self, iconID: str):
        super().__init__()
        auxIcon = qta.icon(iconID, color = '#65dfd5')
        self.setIcon(auxIcon)