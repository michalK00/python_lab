from PySide6.QtWidgets import QStackedWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtGui import Qt, QPixmap
from typing import Callable
from os import path
from PySide6.QtCore import QUrl
from type_enum import TypeOfMessage
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

ERROR_IMG_FILEPATH: str = "./img/error.png"
OTHER_IMG_FILEPATH: str = "./img/other.jpg"
PASSWORD_DENIED_FILEPATH: str = "./img/password_denied.png"
ERROR_MUSIC_FILEPATH: str = "./sounds/boom.mp3"
ERROR_MUSIC_VOLUME: float = 1


class DetailsLayout(QVBoxLayout):
    def __init__(self, app):
        super().__init__()

        self.audio: QAudioOutput = QAudioOutput()
        self.audio.setVolume(ERROR_MUSIC_VOLUME)

        self.media_player: QMediaPlayer = QMediaPlayer(parent=app)
        self.media_player.setAudioOutput(self.audio)
        self.media_player.setSource(
            QUrl.fromLocalFile(ERROR_MUSIC_FILEPATH))

        self.ip = self._create_labeled_input("IP Address:")
        self.user = self._create_labeled_input("User:")
        self.date = self._create_labeled_input("Date:")
        self.time = self._create_labeled_input("Time:")
        self.msg_type = self._create_labeled_input("Message type:")
        self.pid = self._create_labeled_input("PID:")

        col1_layout = QVBoxLayout()
        col1_layout.addWidget(self.ip.label)
        col1_layout.addWidget(self.user.label)
        col1_layout.addWidget(self.date.label)
        col1_layout.addWidget(self.time.label)
        col1_layout.addWidget(self.msg_type.label)
        col1_layout.addWidget(self.pid.label)

        col2_layout = QVBoxLayout()
        col2_layout.addWidget(self.ip.input)
        col2_layout.addWidget(self.user.input)
        col2_layout.addWidget(self.date.input)
        col2_layout.addWidget(self.time.input)
        col2_layout.addWidget(self.msg_type.input)
        col2_layout.addWidget(self.pid.input)

        main_layout = QVBoxLayout()

        details_layout = QHBoxLayout()
        details_layout.addLayout(col1_layout)
        details_layout.addLayout(col2_layout)
        details_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.imgs: QStackedWidget = QStackedWidget()
        self.imgs.setMaximumHeight(150)
        self.imgs.setMaximumWidth(300)

        other_img = QLabel()

        other_img.setPixmap(QPixmap(OTHER_IMG_FILEPATH))
        error_img = QLabel()
        error_img.setPixmap(QPixmap(ERROR_IMG_FILEPATH))
        pass_den_img = QLabel()
        pass_den_img.setPixmap(QPixmap(PASSWORD_DENIED_FILEPATH))

        other_img.setScaledContents(True)
        error_img.setScaledContents(True)
        pass_den_img.setScaledContents(True)

        # QPixmap.scaled(other_img.pixmap(), 150, 300)
        # QPixmap.scaled(error_img.pixmap(), 150, 300)
        # QPixmap.scaled(pass_den_img.pixmap(), 150, 300)

        self.imgs.addWidget(other_img)
        self.imgs.addWidget(error_img)
        self.imgs.addWidget(pass_den_img)
        self.imgs.setVisible(False)

        main_layout.addLayout(details_layout)
        main_layout.addWidget(self.imgs)

        self.addLayout(main_layout)

    def update_details(self, log):
        self.ip.input.setText(str(log[2]))
        self.user.input.setText(str(log[1]))
        self.date.input.setText(str(log[0].date()))
        self.time.input.setText(str(log[0].time()))
        self._handle_msg_type(log[3])
        self.pid.input.setText(str(log[4]))

    def _handle_msg_type(self, type: TypeOfMessage):
        match type:
            case type.ERROR:
                self.media_player.play()
                img = QLabel()
                img.setPixmap(QPixmap(ERROR_IMG_FILEPATH))
                self.imgs.setCurrentIndex(1)
            case type.OTHER:
                self.imgs.setCurrentIndex(0)
            case type.PASSWORD_DENIED:
                self.imgs.setCurrentIndex(2)

        self.imgs.setVisible(True)

        self.msg_type.input.setText(str(type.name))

    def _create_labeled_input(self, label_text):
        label = QLabel(label_text)
        input = QLineEdit()
        input.setReadOnly(True)

        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        input.setAlignment(Qt.AlignmentFlag.AlignRight)
        input.setMaximumWidth(200)
        input.setContentsMargins(0, 20, 0, 0)
        label.setContentsMargins(0, 20, 0, 0)
        return LabeledInput(label, input)


class LabeledInput:
    def __init__(self, label, input):
        self.label = label
        self.input = input
