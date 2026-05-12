"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 321

5.5 Tabular data in ModelViews, with numpy & pandas

Text colors

tableview_format_4.py
"""

# Import modules
import sys
from datetime import datetime

from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    # tag::data[]
    def data(self, index, role):     # type: ignore
        if role == Qt.ItemDataRole.ForegroundRole:
            value = self._data[index.row()][index.column()]

            if (
                isinstance(value, int) or isinstance(value, float)
            ) and value < 0:
                return QColor("red")

        # other 'if role == ...' blocks hidden for clarity.
        # end::data[]

        if role == Qt.ItemDataRole.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return (
                    Qt.AlignmentFlag.AlignVCenter
                    | Qt.AlignmentFlag.AlignRight
                )

        if role == Qt.ItemDataRole.DisplayRole:
            # Get the raw value
            value = self._data[index.row()][index.column()]

            # Perform per-type checks and render accordingly.
            if isinstance(value, datetime):
                # Render time to YYYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2 dp
                return f"{value:.2f}"

            if isinstance(value, str):
                # Render strings with quotes
                return f'"{value}"'

            # Default (anything not captured above: e.g. int)
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
            [1, -1, "hello"],
            [3.023, 5, -5],
            [3, 3, datetime(2017, 10, 1)],
            [7.555, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

