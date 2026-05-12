"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 324

5.5 Tabular data in ModelViews, with numpy & pandas

QTableView DecorationRole - Date Formatting with Calendar icon

tableview_format_6.py
"""

# Import modules
import os

import sys
from datetime import datetime

from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):     # type: ignore
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")

            return value

        if role == Qt.ItemDataRole.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return QIcon(os.path.join(basedir, "calendar.png"))


    def rowCount(self, index):     # type: ignore
        return len(self._data)

    def columnCount(self, index):  # type: ignore
        return len(self._data[0])



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = [
            [True, 9, 2],
            [1, 0, -1],
            [3, 5, False],
            [3, 3, 2],
            [datetime(2019, 5, 4), 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


