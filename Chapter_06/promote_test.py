"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 419

6.3 - Using Custom Widgets in Qt Designer

Creating & Promoting Widgets in Designer

promote_test.py
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


