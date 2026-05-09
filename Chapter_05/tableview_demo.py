"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 311

5.5 Tabular data in ModelViews, with numpy & pandas

Intro to QTableView: basic QTableView with custom TableModel

tableview_demo.py
"""

# Import modules
import sys

from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableView,
)


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):     # type: ignore
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):       # type: ignore
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):    # type: ignore
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = [[4, 1, 3, 3, 7], [9, 1, 5, 3, 8], [2, 1, 5, 3, 9]]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

