# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features

# 2.2. - Signals & Slots
# Changing the interface

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

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

