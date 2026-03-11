# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features

# 2.2. - Signals & Slots

# Import modules

# Only needed for accss to command line arguments
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

        button = QPushButton("Press Me!")
        button.clicked.connect(self.the_button_was_clicked)

        # Seth the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
