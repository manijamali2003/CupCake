from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

name = "Parisa"


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('background-color: #123456')
        self.showFullScreen()

        self.f = QFont()
        self.f.setPixelSize(20)

        self.lb = QLabel()
        self.lb.setFont(self.f)
        self.lb.setText(f"<center>Welcome to <strong>{name} CupCake</strong>!</center><br/><center>Your System has "
                        "been locked by Mani Hacker</center>")
        self.lb.setStyleSheet('color: white;')

        self.setCentralWidget(self.lb)


app = QApplication([])
w = Main()
app.exec()
