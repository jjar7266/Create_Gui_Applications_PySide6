# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features
# page 122
#
# 2.6 Dialogs - A simple example of using QInputDialog.get_int() static method

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_an_int)

        self.setCentralWidget(button1)

    def get_an_int(self):
        my_int_value, ok = QInputDialog.getInt(
            self, "Get an integer", "Enter a number"
        )
        print("Result:", ok, my_int_value)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

