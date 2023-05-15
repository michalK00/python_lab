import sys
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy

from MainWindow import MainWindow
from FileLoadingLayout import FileLoadingLayout
from FilterByDateLayout import FilterByDateLayout
from ListWidget import ListWidget
from IterationButtonLayout import IterationButtonLayout
from DetailsLayout import DetailsLayout

START_H: int = 600
START_W: int = 800

BACKGROUND_MUSIC_FILEPATH: str = "./sounds/Social CREDITS.mp3"
BACKGROUND_MUSIC_VOLUME: float = 0.1

app: QApplication = QApplication(sys.argv)
main_layout: QVBoxLayout = QVBoxLayout()

window: MainWindow = MainWindow(START_W, START_H)

details: DetailsLayout = DetailsLayout(app)
stacked_list: ListWidget = ListWidget(details)
file_layout: FileLoadingLayout = FileLoadingLayout()
file_layout.connect_button(stacked_list.load_main_list)

iteration_button_layout: IterationButtonLayout = IterationButtonLayout()
iteration_button_layout.connect_stacked_list_widget(stacked_list)

filter_layout: FilterByDateLayout = FilterByDateLayout()
filter_layout.connect_button(stacked_list.apply_filter_method(filter_layout))
filter_layout.connect_button(
    iteration_button_layout.apply_filter_method(filter_layout))

main_layout.addLayout(file_layout)
main_layout.addLayout(filter_layout)

master_detail_layout: QHBoxLayout = QHBoxLayout()
master_detail_layout.addWidget(stacked_list)
master_detail_layout.addWidget(details)

main_layout.addLayout(master_detail_layout)
main_layout.addWidget(iteration_button_layout)

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
