# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features

# 2.3. Widgets - adjust font parameters

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")

        # Get the current font and modify it
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)

        # --- ADD THE BOOK'S ALIGNMENT SNIPPET HERE ---

        align_top_left = (
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        # Apply it to your widget

        widget.setAlignment(align_top_left)
        # ----------------------------------------------

        # Align the text horizontally + vertically
#        widget.setAlignment(
#            Qt.AlignmentFlag.AlignHCenter
#            | Qt.AlignmentFlag.AlignVCenter
#        )

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
