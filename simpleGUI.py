from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

import sys
from win32api import GetSystemMetrics

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))

buttons = {
    'small': {'w': 30, 'h': 20}
}


screen = {
    'w': GetSystemMetrics(0),
    'h': GetSystemMetrics(1)
}
appsize = {
    'w': 600,
    'h': 800
}

def on_click(self):
    sys.exit(app.exec_())
    print('Calculator closed')

styleSheet = "QPushButton:hover#quit_button" \
             "{" \
             "background-color: red;" \
             "}"



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        def button_clicked():
            print("clicked")

        # <Window properties>
        self.setGeometry(int(screen['w']/2 - (appsize['w']/2)), int(screen['h']/2 - (appsize['h']/2)), appsize['w'], appsize['h'])
        self.setWindowTitle("Calculator")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(styleSheet)
        # </Window properties>

        # <Close button>
        button = QPushButton('X', self)
        button.setToolTip('Quit calculator app')
        button.setGeometry(appsize['w'] - buttons['small']['w'], 0, buttons['small']['w'], buttons['small']['h'])
        button.setStyleSheet('border: none;')
        button.setObjectName('quit_button')
        button.clicked.connect(on_click)
        # </Close button>

        # <Number display top>
        # by default label will display at top left corner
        self.label_1 = QLabel('Light green', self)
        # </Number display top>

        # moving position
        self.label_1.move(100, 100)

        # setting up background color
        self.label_1.setStyleSheet("background-color: lightgreen")

        # creating a label widget
        # by default label will display at top left corner
        self.label_2 = QLabel('Yellow', self)

        # moving position
        self.label_2.move(100, 150)

        # setting up background color and border
        self.label_2.setStyleSheet("background-color: yellow; border: 1 px solid black;")

        # show all the widgets
        self.show()

        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())