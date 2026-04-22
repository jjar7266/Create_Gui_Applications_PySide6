# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 160
#
# 2.8 Events - Basic mouse event handlers

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.setGeometry(100, 100, 280, 80)  # added: not in the book

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()




