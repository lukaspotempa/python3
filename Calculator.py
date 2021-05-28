from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

import sys
from win32api import GetSystemMetrics

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))


css = """
QPushButton:hover#quit_button
    {
        background-color: red;
    }
    
"""

buttons = {
    'small': {'w': 30, 'h': 20},
    'number': {'w': 100, 'h': 100, 'wm': 75, 'hm': 25}
}

numberdisplay = {
    'w': 500,
    'h': 150
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

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # <Window properties>
        self.setGeometry(int(screen['w']/2 - (appsize['w']/2)), int(screen['h']/2 - (appsize['h']/2)), appsize['w'], appsize['h'])
        self.setWindowTitle("Calculator")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(css)
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
        ninput = QLabel('12345678910', self) # Max 12
        ninput.setGeometry(int(numberdisplay['w']/10), buttons['small']['h'] + 10, numberdisplay['w'], numberdisplay['h'])
        ninput.setStyleSheet("border: 1px solid black;")
        ninput.setFont(QFont('Arial', 55))
        # </Number display top>

        # <Number Buttons>
        #button = QPushButton(str(j + 1), self)
        #button.setGeometry(buttons['number']['wm'] + (i * buttons['number']['w']), 50, 50, 50)
        # </Number Buttons>

        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())