from PySide6.QtWidgets import QHBoxLayout, QPushButton, QLineEdit, QFileDialog
from typing import Callable
from os import path


class FileLoadingLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self._button: QPushButton = QPushButton("Open")
        self._file_label = QLineEdit()
        self._file_label.setReadOnly(True)

        self.addWidget(self._file_label)
        self.addWidget(self._button)

    def open_file_dialog(self) -> str:
        dialog: QFileDialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("Log Files (*.log);;All Files (*)")

        if dialog.exec() and path.exists(file_path := dialog.selectedFiles()[0]):
            self._file_label.setText(file_path)
            return file_path
            # load_log_list(file_path, log_list)

    def connect_button(self, load_log_list: Callable[[str], None]) -> None:
        self._button.clicked.connect(lambda _: load_log_list(self.open_file_dialog()))
