# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 150
#
# 2.7 Windows — Creating a new window (continued)
#
# In Qt, a window will close immediately if no reference to it is kept.
# To ensure the secondary window stays open, we store it on the main
# window instance (self.w). This keeps it alive for as long as the main
# window exists.

import sys

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
    A simple standalone QWidget that acts as a separate window.
    Because it has no parent, Qt treats it as an independent,
    free‑floating top‑level window.
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
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
        """
        Create and show a new window.

        IMPORTANT:
        We assign the window to self.w so Python keeps a reference to it.
        Without this, the window would be garbage‑collected immediately
        after this function exits, causing it to appear briefly and then
        disappear.
        """
        self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
