from PyQt5.QtWidgets import QMainWindow, QApplication
from Canvas import Canvas
import sys


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        canvas = Canvas()
        canvas.setVisible(True)
        self.setCentralWidget(canvas)
        self.setWindowTitle("Snake Game")


app = QApplication(sys.argv)
window = main()
window.show()
app.exec()