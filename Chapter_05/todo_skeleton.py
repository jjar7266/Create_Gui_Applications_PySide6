"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 296

5.4 - A simple Model View -- a Todo List

    To demonstrate how to use the ModelViews in practice, we’ll put together
    a very simple implementation of a desktop Todo List. This will consist
    of a QListView for the list of items, a QLineEdit to enter new items,
    and a set of buttons to add, delete, or mark items as done.

todo_skeleton.py
"""

# Import modules
import sys

from mainwindow_ui import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

