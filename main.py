from VIEW.beatLink import BeatWindow
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'dark_cyan.xml')
    mWindow = BeatWindow()
    mWindow.show()
    sys.exit(app.exec())  