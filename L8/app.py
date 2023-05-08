import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout,
                               QLineEdit, QListWidget, QListWidgetItem, QListView, QDateEdit, QLabel, QStackedWidget,
                               QCalendarWidget, QSizePolicy)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QDate

from backend import get_logs, gather_logs, get_logs_between_dates

START_V = 768
START_H = 1024

app = QApplication(sys.argv)
window = QMainWindow()
window.resize(START_H, START_V)


def open_file_dialog() -> None:
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    dialog.setNameFilter("Log Files (*.log);;All Files (*)")

    if dialog.exec():
        file_paths = dialog.selectedFiles()[0]
        file_label.setText(file_paths)
        load_log_list(file_paths, all_log_list)


def load_log_list(file_path: str, list_widget: QListWidget) -> None:
    gather_logs(file_path)
    for log in get_logs():
        item = QListWidgetItem(log)
        list_widget.addItem(item)
    list_widget.itemPressed.connect(handle_log_change)


def load_filtered_list() -> None:
    filtered_log_list.clear()
    for log in get_logs_between_dates(start_date_filter.date(), end_date_filter.date()):
        item = QListWidgetItem(log)
        filtered_log_list.addItem(item)


def handle_log_change(item: QListWidgetItem) -> None:
    print(item.text())


def update_end_date(start_date: QDate) -> None:
    end_date_filter.setMinimumDate(start_date)


def update_start_date(end_date: QDate) -> None:
    start_date_filter.setMaximumDate(end_date)


def apply_date_filter() -> None:
    if date_filter_applying_button.isChecked():
        load_filtered_list()
        log_list_stacked_widget.setCurrentIndex(1)
    else:
        log_list_stacked_widget.setCurrentIndex(0)


font = QFont("Comic Sans MS")
font.setBold(True)
window.setFont(font)

layout = QVBoxLayout()

file_loading_layout = QHBoxLayout()
layout.addLayout(file_loading_layout)
date_filter_layout = QHBoxLayout()
layout.addLayout(date_filter_layout)

button = QPushButton("Open")
file_label = QLineEdit()
file_label.setReadOnly(True)

# stacking two lists, so I don't have to reload everything everytime the user wants to view filtered logs
log_list_stacked_widget = QStackedWidget()
all_log_list = QListWidget()
all_log_list.setSelectionMode(QListView.SelectionMode.SingleSelection)

filtered_log_list = QListWidget()
filtered_log_list.setSelectionMode(QListView.SelectionMode.SingleSelection)

log_list_stacked_widget.addWidget(all_log_list)
log_list_stacked_widget.addWidget(filtered_log_list)

layout.addWidget(log_list_stacked_widget)

# when implementing master-detail, please move them accordingly, because they look poo-poo
start_date_filter = QDateEdit()
start_date_filter.setDate(QDate.currentDate())
start_date_filter.setDisplayFormat("dd/MM")
start_date_filter.dateChanged.connect(update_end_date)
start_date_view = QLabel("From")

end_date_filter = QDateEdit()
end_date_filter.setDate(QDate.currentDate())
end_date_filter.setDisplayFormat("dd/MM")
end_date_filter.dateChanged.connect(update_start_date)
end_date_view = QLabel("To")

date_filter_applying_button = QPushButton("Apply Date Restrictions")
date_filter_applying_button.setCheckable(True)
date_filter_applying_button.toggled.connect(apply_date_filter)

file_loading_layout.addWidget(file_label)
file_loading_layout.addWidget(button)

date_filter_layout.addWidget(start_date_view)
date_filter_layout.addWidget(start_date_filter)
date_filter_layout.addWidget(end_date_view)
date_filter_layout.addWidget(end_date_filter)
date_filter_layout.addWidget(date_filter_applying_button)

widget = QWidget()
widget.setLayout(layout)
window.setCentralWidget(widget)

button.clicked.connect(open_file_dialog)
window.show()
sys.exit(app.exec())
