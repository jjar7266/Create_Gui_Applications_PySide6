"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 296

5.4 - Todo List Model(Step 1: The Model)

todo_1.py
"""

# Import modules
import sys

from mainwindow_ui import Ui_MainWindow

from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow


class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):  # type: ignore
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]

    def rowCount(self, index):    # type: ignore
        return len(self.todos)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.todoView.setModel(self.model)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


