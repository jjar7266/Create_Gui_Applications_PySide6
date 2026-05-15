"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 344

5.6 Querying SQL databases with Qt models

Using QSqlRelationalTableModel to Display Related SQL Tables

tableview_relationalmodel.py
"""

# Import modules
import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtSql import (
    QSqlDatabase,
    QSqlRelation,
    QSqlRelationalTableModel,
)
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

        self.model = QSqlRelationalTableModel(db=self.db)

        self.table.setModel(self.model)

        self.model.setTable("Track")
        self.model.setRelation(
            2, QSqlRelation("Album", "AlbumId", "Title")
        )
        self.model.setRelation(
            3, QSqlRelation("MediaType", "MediaTypeId", "Name")
        )
        self.model.setRelation(
            4, QSqlRelation("Genre", "GenreId", "Name")
        )
        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

