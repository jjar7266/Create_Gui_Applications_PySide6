# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features
# page 150
#
# 2.7 Windows - Creating a new window
"""
If you run this, you’ll see the main window. Clicking the button
may show the second window, but if you see it it will only be visible
for a fraction of a second. What’s happening?
"""

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, is_checked):
        w = AnotherWindow()
        w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
