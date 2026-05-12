"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 322

5.5 Tabular data in ModelViews, with numpy & pandas

QTableView BackgroundRole - Numeric Heat-Map Gradient(-5 to +5)

tableview_format_5b.py
"""

# Import modules
import sys

from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

# 11 color range -5 to +5; 0 = light gray
COLORS = [
    "#053061",
    "#2166ac",
    "#4393c3",
    "#92c5de",
    "#d1e5f0",
    "#f7f7f7",
    "#fddbc7",
    "#f4a582",
    "#d6604d",
    "#b2182b",
    "#67001f",
]


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):     # type: ignore
        if role == Qt.ItemDataRole.BackgroundRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                # Convert to integer for indexing.
                value = int(value)

                # Limit to range -5 ... +5, then convert to 0..10
                value = max(-5, value)  # values < -5 become -5
                value = min(5, value)   # values > +5 become +5
                value = value + 5       # -5 becomes 0, +5 becomes +10

                return QColor(COLORS[value])

        # other 'if role == ...' blocks hidden for clarity.

        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]


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






