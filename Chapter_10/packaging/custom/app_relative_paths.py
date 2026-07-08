"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 10 - Packaging & Distribution
Page 617

10.1 - Packaging with PyInstaller

Add relative icon paths to Pyinstaller example and minor window resize

app_relative_paths.py
"""

# Import modules
import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        button = QPushButton("My simple app.")
        button.setIcon(QIcon(os.path.join(basedir, "icon.svg")))
        button.pressed.connect(self.close)

        self.setCentralWidget(button)


app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(basedir, "icon.svg")))
window = MainWindow()

# 👈 slightly larger window (not part of the book example)
window.resize(300, 200)

window.show()
app.exec()
