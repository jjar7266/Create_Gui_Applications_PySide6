# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features
# page 136

# 2.6 Dialogs - file filters - continued
"""
Our example is updated below to use this approach, with the
FILE_FILTERS defined at the top of the file so they can be used
by all the file methods.
"""

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)

FILE_FILTERS = [
    "Portable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Comma Separated Values (*.csv)",
    "All files (*.*)",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)

    def get_filename(self):
        initial_filter = FILE_FILTERS[3]  # Select one from the list
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self, filter=filters, selectedFilter=initial_filter
        )
        print("Result:", filename, selected_filter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
