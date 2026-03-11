# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features

# 2.2. - Signals & Slots

# In this example we store the checked value of our button in a variable
# called - button_is_checked on self.

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

        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_toggled(self, is_checked):
        self.button_is_checked = is_checked

        print(self.button_is_checked)
