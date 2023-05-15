from PySide6.QtWidgets import QStackedWidget, QListWidget, QListWidgetItem, QListView, QPushButton, QVBoxLayout
from functools import partial
from typing import Callable, Any
from DetailsLayout import DetailsLayout
from FilterByDateLayout import FilterByDateLayout
from data_managment import *


class ListWidget(QStackedWidget):
    def __init__(self, details: DetailsLayout):
        super().__init__()
        self.details = details
        self._main_log_list: QListWidget = QListWidget()
        self._main_log_list.setSelectionMode(
            QListView.SelectionMode.SingleSelection)
        self._main_log_list.itemSelectionChanged.connect(
            self.handle_main_log_change())

        self._filtered_log_list: QListWidget = QListWidget()
        self._filtered_log_list.setSelectionMode(
            QListView.SelectionMode.SingleSelection)
        self._filtered_log_list.itemSelectionChanged.connect(
            self.handle_filtered_log_change())

        self.addWidget(self._main_log_list)
        self.addWidget(self._filtered_log_list)

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
            item: QListWidgetItem = QListWidgetItem(log)
            self._main_log_list.addItem(item)

    def _load_filtered_list(self, filter_layout: FilterByDateLayout) -> None:
        self._filtered_log_list.clear()
        for log in get_logs_between_dates(filter_layout.get_start_date(), filter_layout.get_end_date()):
            item: QListWidgetItem = QListWidgetItem(log)
            self._filtered_log_list.addItem(item)

    def _handle_log_change(self, list_widget: QListWidget, item_getter) -> None:
        self.details.update_details(item_getter(list_widget.currentRow()))

    def handle_main_log_change(self):
        return lambda: self._handle_log_change(self._main_log_list, get_item_from_log_list)

    def handle_filtered_log_change(self):
        return lambda: self._handle_log_change(self._filtered_log_list, get_item_from_filtered_list)

    def apply_filter_method(self, filter_layout: FilterByDateLayout) -> Callable[[QPushButton], None]:
        return partial(self._apply_date_filter, filter_layout=filter_layout)

    def inform_main_list_select(self, some_func: Callable[[Any], Any]):
        self._main_log_list.currentRowChanged.connect(some_func)

    def inform_filtered_list_select(self, some_func: Callable[[Any], Any]):
        self._filtered_log_list.currentRowChanged.connect(some_func)

    @property
    def load_main_list(self) -> Callable[[str], None]:
        return self._load_main_log_list

    @property
    def get_main_log_list(self) -> QListWidget:
        return self._main_log_list

    @property
    def get_filtered_log_list(self) -> QListWidget:
        return self._filtered_log_list
