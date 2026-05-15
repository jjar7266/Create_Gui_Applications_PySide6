"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 343

5.6 Querying SQL databases with Qt models

Cleaning User Input Before Filtering in QSqlTableModel

tableview_tablemodel_filter_clean.py
"""

# Import modules
import os
import re
import sys

from PySide6.QtCore import QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QTableView,
    QVBoxLayout,
    QWidget,
)

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        layout = QVBoxLayout()

        self.search = QLineEdit()
        self.search.textChanged.connect(self.update_filter)
        self.table = QTableView()

        layout.addWidget(self.search)
        layout.addWidget(self.table)
        container.setLayout(layout)

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(
            os.path.join(basedir, "Chinook_Sqlite.sqlite")
        )
        self.db.open()

        self.model = QSqlTableModel(db=self.db)

        self.table.setModel(self.model)

        self.model.setTable("Track")
        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(container)

    def update_filter(self, s):
        s = re.sub(r"[\W_]+", "", s)
        filter_str = f'Name LIKE "%{s}%"'
        self.model.setFilter(filter_str)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
