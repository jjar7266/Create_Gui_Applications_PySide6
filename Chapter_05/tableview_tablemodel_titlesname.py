"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 339

5.6 Querying SQL databases with Qt models

Setting Column Headers by Field Name in QSqlTableModel

tableview_tablemodel_titlesname.py
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
        column_titles = {
            "Name": "Name",
            "AlbumId": "Album (ID)",
            "MediaTypeId": "Media Type (ID)",
            "GenreID": "Genre (ID)",
            "Composer": "Composer",
        }
        for n, t in column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(
                idx, Qt.Orientation.Horizontal, t
            )

        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


