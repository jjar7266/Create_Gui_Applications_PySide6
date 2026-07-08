"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 598

9.6 - Working with command-line arguments

Display Command-Line Arguments in a PySide6 Window

arguments.py
"""

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for arg in sys.argv:
            label = QLabel(arg)
            layout.addWidget(label)

        self.setLayout(layout)
        self.setWindowTitle("Arguments")


app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()


