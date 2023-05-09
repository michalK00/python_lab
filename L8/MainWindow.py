from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self, w_height, w_width):
        super().__init__()
        self.resize(w_height, w_width)
        font = QFont("Comic Sans MS")
        font.setBold(True)
        self.setFont(font)