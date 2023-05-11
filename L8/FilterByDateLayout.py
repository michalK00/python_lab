from PySide6.QtWidgets import QHBoxLayout, QDateEdit, QLabel, QPushButton
from PySide6.QtCore import QDate
from typing import Callable


class FilterByDateLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self._start_date = QDateEdit()
        self._start_date.setDate(QDate.currentDate())
        self._start_date.setDisplayFormat("dd/MM")
        self._start_date.dateChanged.connect(self._update_end_date)
        self._start_date_label = QLabel("From")

        self._end_date = QDateEdit()
        self._end_date.setDate(QDate.currentDate())
        self._end_date.setDisplayFormat("dd/MM")
        self._end_date.dateChanged.connect(self._update_start_date)
        self._end_date_label = QLabel("To")

        self._apply_button = QPushButton("Apply Date Restrictions")
        self._apply_button.setCheckable(True)

        self.addWidget(self._start_date_label)
        self.addWidget(self._start_date)
        self.addWidget(self._end_date_label)
        self.addWidget(self._end_date)
        self.addWidget(self._apply_button)

    def _update_end_date(self, start_date: QDate) -> None:
        self._end_date.setMinimumDate(start_date)

    def _update_start_date(self, end_date: QDate) -> None:
        self._start_date.setMaximumDate(end_date)

    def get_start_date(self) -> QDate:
        return self._start_date.date()

    def get_end_date(self) -> QDate:
        return self._end_date.date()

    def connect_button(self, apply_date_filter):
        self._apply_button.toggled.connect(lambda _: apply_date_filter(self._apply_button))

