"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 10 - Packaging & Distribution
Page 607

10.1 - Packaging with PyInstaller

PyInstaller Packaging Skeleton App

app.py
"""

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        button = QPushButton("My simple app.")
        button.pressed.connect(self.close)

        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
