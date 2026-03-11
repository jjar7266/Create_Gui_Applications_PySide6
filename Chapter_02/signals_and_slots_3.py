# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features

# 2.2. - Signals & Slots
# complex example, we connect the .windowTitleChanged signal on
# the QMainWindow to a custom slot method

# Import modules

import sys
from random import choice

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

window_titles = [
    "My App",
    "Still My App",
    "What on earth",
    "This is surprising",
    "Something went wrong",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Pres Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(
            self.the_window_title_changed
        )

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



