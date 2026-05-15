"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 327

5.5 Tabular data in ModelViews, with numpy & pandas

Displaying NumPy Array Data in a QTableView Model

tableview_numpy.py
"""

# Import modules
import sys

import numpy as np

from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):     # type: ignore
        if role == Qt.ItemDataRole.DisplayRole:
            # self._data[index.row()][index.column()] will also work.
            value = self._data[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):     # type: ignore
        return self._data.shape[0]

    def columnCount(self, index):  # type: ignore
        return self._data.shape[1]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = np.array(
            [[1, 9, 2], [1, 0, -1], [3, 5, 2], [3, 3, 2], [5, 8, 9]]
        )

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


