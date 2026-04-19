# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 152
#
# 2.7 Windows — show a random number in the label each time it is created.
"""
The __init__ block is only run when creating the window. If you keep
clicking the button the number will change, showing that the window
is being re-created.
"""

import sys

from random import randint
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        window_id = randint(0, 100)
        self.label = QLabel(f"Another Window {window_id}")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Button that triggers the creation of the secondary window.
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)

        # The button becomes the central widget of the main window.
        self.setCentralWidget(self.button)

    def show_new_window(self, is_checked):

        self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
