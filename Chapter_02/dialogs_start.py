# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features
# page 107

# 2.6 Dialogs - GUI components that allow you to communicate with the user
# dialogs_start.py

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, is_checked):
        print("click", is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



