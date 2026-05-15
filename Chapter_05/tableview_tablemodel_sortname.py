"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 336

5.6 Querying SQL databases with Qt models

Sorting a SQL Table by Field Name with QSqlTableModel

tableview_tablemodel_sortname.py
"""

# Import modules
import os
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName(
            os.path.join(basedir, "Chinook_Sqlite.sqlite")
        )
        self.db.open()

        self.model = QSqlTableModel(db=self.db)

        self.table.setModel(self.model)

        self.model.setTable("Track")
        idx = self.model.fieldIndex("Milliseconds")
        self.model.setSort(idx, Qt.SortOrder.DescendingOrder)
        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


