"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 10 - Packaging & Distribution
Page 614

10.1 - Packaging with PyInstaller

Add application icon to PyInstaller skeleton app and minor window resize

app.py
"""

# Import modules
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        button = QPushButton("My simple app.")
        button.pressed.connect(self.close)

        self.setCentralWidget(button)


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon.svg"))
window = MainWindow()

# 👈 slightly larger window (not part of the book example)
window.resize(300, 200)

window.show()
app.exec()
