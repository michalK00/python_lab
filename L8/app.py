import sys
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from MainWindow import MainWindow
from FileLoadingLayout import FileLoadingLayout
from FilterByDateLayout import FilterByDateLayout
from ListWidget import ListWidget

START_H: int = 1024
START_W: int = 768

BACKGROUND_MUSIC_FILEPATH: str = "./sounds/Social CREDITS.mp3"
BACKGROUND_MUSIC_VOLUME: float = 0.2

app: QApplication = QApplication(sys.argv)
main_layout: QVBoxLayout = QVBoxLayout()

window: MainWindow = MainWindow(START_H, START_W)

stacked_list: ListWidget = ListWidget()
file_layout: FileLoadingLayout = FileLoadingLayout()
file_layout.connect_button(stacked_list.load_main_list)

filter_layout: FilterByDateLayout = FilterByDateLayout()
filter_layout.connect_button(stacked_list.apply_filter_method(filter_layout))

main_layout.addLayout(file_layout)
main_layout.addLayout(filter_layout)
main_layout.addWidget(stacked_list)

audio: QAudioOutput = QAudioOutput()
audio.setVolume(BACKGROUND_MUSIC_VOLUME)

media_player: QMediaPlayer = QMediaPlayer()
media_player.setAudioOutput(audio)
media_player.setSource(QUrl.fromLocalFile(BACKGROUND_MUSIC_FILEPATH))
media_player.setLoops(media_player.Loops.Infinite)
media_player.play()

main_widget: QWidget = QWidget()
main_widget.setLayout(main_layout)
window.setCentralWidget(main_widget)

window.show()

if __name__ == "__main__":
    sys.exit(app.exec())
