import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout, QLineEdit
from PySide6.QtGui import QFont

app = QApplication(sys.argv)
window = QMainWindow()


def open_file_dialog():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.ExistingFile)
    dialog.setNameFilter(
        "Log Files (*.log);;All Files (*)")

    if dialog.exec():
        file_paths = dialog.selectedFiles()[0]
        file_label.setText(file_paths)


font = QFont("Comic Sans MS")
font.setPointSize(12)
font.setBold(True)
window.setFont(font)


layout = QVBoxLayout()


top_layout = QHBoxLayout()
layout.addLayout(top_layout)

button = QPushButton("Open")
file_label = QLineEdit()
file_label.setReadOnly(True)

top_layout.addWidget(file_label)
top_layout.addWidget(button)

widget = QWidget()
widget.setLayout(layout)
window.setCentralWidget(widget)

button.clicked.connect(open_file_dialog)
window.show()
sys.exit(app.exec())
