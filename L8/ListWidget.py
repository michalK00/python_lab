from PySide6.QtWidgets import QStackedWidget, QListWidget, QListWidgetItem, QListView, QPushButton
from functools import partial

from FilterByDateLayout import FilterByDateLayout
from data_managment import *


class ListWidget(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.main_log_list = QListWidget()
        self.main_log_list.setSelectionMode(QListView.SelectionMode.SingleSelection)
        self.main_log_list.itemPressed.connect(partial(
            self._handle_log_change,
            list_widget=self.main_log_list,
            item_getter=get_item_from_log_list))

        self.filtered_log_list = QListWidget()
        self.filtered_log_list.setSelectionMode(QListView.SelectionMode.SingleSelection)
        self.filtered_log_list.itemPressed.connect(partial(
            self._handle_log_change,
            list_widget=self.filtered_log_list,
            item_getter=get_item_from_filtered_list))

        self.addWidget(self.main_log_list)
        self.addWidget(self.filtered_log_list)

    def _apply_date_filter(self, button: QPushButton, filter_layout: FilterByDateLayout) -> None:
        if button.isChecked():
            self._load_filtered_list(filter_layout)
            self.setCurrentIndex(1)
        else:
            self.setCurrentIndex(0)

    def _load_main_log_list(self, file_path: str) -> None:
        if file_path is None:
            return

        gather_logs(file_path)
        for log in get_logs():
            item = QListWidgetItem(log)
            self.main_log_list.addItem(item)

    def _load_filtered_list(self, filter_layout: FilterByDateLayout) -> None:
        self.filtered_log_list.clear()
        for log in get_logs_between_dates(filter_layout.get_start_date(), filter_layout.get_end_date()):
            item = QListWidgetItem(log)
            self.filtered_log_list.addItem(item)

    @staticmethod
    def _handle_log_change(item: QListWidgetItem, list_widget: QListWidget, item_getter) -> None:
        print(item_getter(list_widget.indexFromItem(list_widget.selectedItems()[0]).row()))
        print(item.text())

    @property
    def apply_filter_method(self):
        return self._apply_date_filter

    @property
    def load_main_list(self):
        return self._load_main_log_list
