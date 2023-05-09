import sys
from functools import partial
from PySide6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget,
                               QListWidget, QListWidgetItem, QListView, QStackedWidget)

from data_managment import *
from MainWindow import MainWindow
from FileLoadingLayout import FileLoadingLayout
from FilterByDateLayout import FilterByDateLayout

START_H = 1024
START_W = 768


def apply_date_filter(button: QPushButton) -> None:
    if button.isChecked():
        load_filtered_list()
        log_list_stacked_widget.setCurrentIndex(1)
    else:
        log_list_stacked_widget.setCurrentIndex(0)


def load_main_log_list(file_path: str) -> None:
    gather_logs(file_path)
    for log in get_logs():
        item = QListWidgetItem(log)
        main_log_list.addItem(item)


def load_filtered_list() -> None:
    filtered_log_list.clear()
    for log in get_logs_between_dates(filter_layout.get_start_date(), filter_layout.get_end_date()):
        item = QListWidgetItem(log)
        filtered_log_list.addItem(item)


def handle_log_change(item: QListWidgetItem, list_widget: QListWidget, item_getter) -> None:
    print(item_getter(list_widget.indexFromItem(list_widget.selectedItems()[0]).row()))
    print(item.text())


app = QApplication(sys.argv)
main_layout = QVBoxLayout()

# stacking two lists, so I don't have to reload everything everytime the user wants to view filtered logs
log_list_stacked_widget = QStackedWidget()
main_log_list = QListWidget()
main_log_list.setSelectionMode(QListView.SelectionMode.SingleSelection)
main_log_list.itemPressed.connect(partial(
    handle_log_change,
    list_widget=main_log_list,
    item_getter=get_item_from_log_list))

filtered_log_list = QListWidget()
filtered_log_list.setSelectionMode(QListView.SelectionMode.SingleSelection)
filtered_log_list.itemPressed.connect(partial(
    handle_log_change,
    list_widget=filtered_log_list,
    item_getter=get_item_from_filtered_list))


log_list_stacked_widget.addWidget(main_log_list)
log_list_stacked_widget.addWidget(filtered_log_list)

window = MainWindow(START_H, START_W)
file_layout = FileLoadingLayout(load_main_log_list)
filter_layout = FilterByDateLayout(apply_date_filter)

main_layout.addLayout(file_layout)
main_layout.addLayout(filter_layout)
main_layout.addWidget(log_list_stacked_widget)

widget = QWidget()
widget.setLayout(main_layout)
window.setCentralWidget(widget)

window.show()
sys.exit(app.exec())
