import sys
from functools import partial
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from MainWindow import MainWindow
from FileLoadingLayout import FileLoadingLayout
from FilterByDateLayout import FilterByDateLayout
from ListWidget import ListWidget

START_H = 1024
START_W = 768

BACKGROUND_MUSIC_FILEPATH = "./sounds/Social CREDITS.mp3"
BACKGROUND_MUSIC_VOLUME = 0.2

app = QApplication(sys.argv)
main_layout = QVBoxLayout()

window = MainWindow(START_H, START_W)

stacked_list = ListWidget()
file_layout = FileLoadingLayout()
file_layout.connect_button(stacked_list.load_main_list)

filter_layout = FilterByDateLayout()
filter_layout.connect_button(partial(stacked_list.apply_filter_method, filter_layout=filter_layout))

main_layout.addLayout(file_layout)
main_layout.addLayout(filter_layout)
main_layout.addWidget(stacked_list)

audio = QAudioOutput()
audio.setVolume(BACKGROUND_MUSIC_VOLUME)

media_player = QMediaPlayer()
media_player.setAudioOutput(audio)
media_player.setSource(QUrl.fromLocalFile(BACKGROUND_MUSIC_FILEPATH))
media_player.setLoops(media_player.Loops.Infinite)
media_player.play()

widget = QWidget()
widget.setLayout(main_layout)
window.setCentralWidget(widget)

window.show()

if __name__ == "__main__":
    sys.exit(app.exec())
