from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self, w_height: int, w_width: int):
        super().__init__()
        font: QFont = QFont("Comic Sans MS")
        font.setBold(True)

        self.setFont(font)
        self.resize(w_height, w_width)
