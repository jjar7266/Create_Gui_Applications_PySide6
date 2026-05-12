"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 322

5.5 Tabular data in ModelViews, with numpy & pandas

TableView Formatting - Row & Column Background Highlighting

tableview_format_5.py
"""

# Import modules
import sys

from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    # tag::data[]
    def data(self, index, role):     # type: ignore
        if role == Qt.ItemDataRole.BackgroundRole:
            if index.row() == 0:
                return QColor("lightgray")
            if index.column() == 0:
                return QColor("lightblue")
        # other 'if role == ...' blocks hidden for clarity.
        # end::data[]

        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            return value

    def rowCount(self, index):     # type: ignore
        return len(self._data)

    def columnCount(self, index):  # type: ignore
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        data = [
            [4, 9, 2],
            [1, -1, -1],
            [3, 5, -5],
            [3, 3, 2],
            [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
