from PySide6.QtWidgets import QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QListWidget, QStackedWidget, QWidget
from functools import partial
from typing import Callable

from ListWidget import ListWidget


class IterationButtonLayout(QStackedWidget):
    def __init__(self):
        super().__init__()
        self._main_layout: QHBoxLayout = QHBoxLayout()
        self._next_button_main: QPushButton = QPushButton("Next")
        self._previous_button_main: QPushButton = QPushButton("Previous")

        self._main_layout.addWidget(self._previous_button_main)
        self._main_layout.addSpacerItem(QSpacerItem(80, 40, QSizePolicy.Policy.MinimumExpanding))
        self._main_layout.addWidget(self._next_button_main)

        self._filtered_layout: QHBoxLayout = QHBoxLayout()
        self._next_button_filtered: QPushButton = QPushButton("Next")
        self._previous_button_filtered: QPushButton = QPushButton("Previous")

        self._filtered_layout.addWidget(self._previous_button_filtered)
        self._filtered_layout.addSpacerItem(QSpacerItem(80, 40, QSizePolicy.Policy.MinimumExpanding))
        self._filtered_layout.addWidget(self._next_button_filtered)

        self._main_widget: QWidget = QWidget()
        self._main_widget.setLayout(self._main_layout)
        self.addWidget(self._main_widget)

        self._filtered_widget: QWidget = QWidget()
        self._filtered_widget.setLayout(self._filtered_layout)
        self.addWidget(self._filtered_widget)

        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)

    def apply_filter_method(self, _) -> Callable[[QPushButton], None]:
        def _apply_date_filter(button: QPushButton) -> None:

            if button.isChecked():
                self.setCurrentIndex(1)
            else:
                self.setCurrentIndex(0)

        return _apply_date_filter

    @staticmethod
    def _next_item(list_widget: QListWidget, update: Callable[[int], None]) -> None:
        curr_row = list_widget.currentRow()
        if curr_row < list_widget.count() - 1:
            list_widget.setCurrentRow(curr_row + 1)

        update(list_widget.currentRow())

    @staticmethod
    def _previous_item(list_widget: QListWidget, update: Callable[[int], None]) -> None:
        curr_row = list_widget.currentRow()
        if curr_row > 0:
            list_widget.setCurrentRow(curr_row - 1)

        update(list_widget.currentRow())

    @staticmethod
    def update_main_button_states(curr_row: int, list_widget: QListWidget, next_button: QPushButton,
                                  previous_button: QPushButton) -> None:
        next_button.setEnabled(curr_row < list_widget.count() - 1)
        previous_button.setEnabled(curr_row > 0)

    def connect_stacked_list_widget(self, list_widget: ListWidget) -> None:
        main_button_update = partial(
            self.update_main_button_states,
            list_widget=list_widget.get_main_log_list,
            next_button=self._next_button_main,
            previous_button=self._previous_button_main
        )

        filtered_button_update = partial(
            self.update_main_button_states,
            list_widget=list_widget.get_filtered_log_list,
            next_button=self._next_button_filtered,
            previous_button=self._previous_button_filtered
        )

        list_widget.inform_main_list_select(main_button_update)

        list_widget.inform_filtered_list_select(filtered_button_update)

        self._next_button_main.clicked.connect(
            partial(
                self._next_item,
                list_widget=list_widget.get_main_log_list,
                update=main_button_update
            )
        )
        self._next_button_main.clicked.connect(list_widget.handle_main_log_change())
        self._previous_button_main.clicked.connect(
            partial(
                self._previous_item,
                list_widget=list_widget.get_main_log_list,
                update=main_button_update
            )
        )
        self._previous_button_main.clicked.connect(list_widget.handle_main_log_change())

        self._next_button_filtered.clicked.connect(
            partial(
                self._next_item,
                list_widget=list_widget.get_filtered_log_list,
                update=filtered_button_update
            )
        )
        self._next_button_filtered.clicked.connect(list_widget.handle_filtered_log_change())
        self._previous_button_filtered.clicked.connect(
            partial(
                self._previous_item,
                list_widget=list_widget.get_filtered_log_list,
                update=filtered_button_update
            )
        )
        self._previous_button_filtered.clicked.connect(list_widget.handle_filtered_log_change())
