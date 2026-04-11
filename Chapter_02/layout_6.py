# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features

# 2.4. Layouts - QGridLayout - widgets arranged in a grid
# page 68

# Import modules
import sys

from layout_colorwidget import Color

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

