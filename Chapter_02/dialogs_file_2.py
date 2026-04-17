# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features
# page 135
#
# 2.6 Dialogs - file filters
"""
The Qt standard for file filters is a string consisting of the following
format, where User friendly name can be any text and the *.ext is the
file-matching filter and extension. This should be included in brackets
at the end of the filter string
    - "User-friendly name (*.ext)"
    - "Portable Network Graphics Image (*.png);;Comma Separated files
       (*.csv);;All files (*.*)"
"""
# Below is our example updated to provide the above example filters to the
# QFileDialog.getOpenFilename() method

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)


    def get_filename(self):
        filters = (
            "Portable Network Graphics files (*.png);;"
            "Comma Separated Values (*.csv);;"
            "All files (*.*)"
        )
        print("Filters are:", filters)
        filename, selected_filter = QFileDialog.getOpenFileName(
            self, filter=filters
        )
        print("Result:", filename, selected_filter)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
