"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
(not in the book, but it is included in the source code)

9.2 - Extending Signals

using QObject.sender() to identify Signal Sources

signals_extra_4.py
"""

# Import modules
import sys

from PySide6.QtCore import QObject
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        v = QVBoxLayout()
        h = QHBoxLayout()

        for a in range(10):
            button = QPushButton(str(a))
            button.clicked.connect(self.button_clicked)
            h.addWidget(button)

        v.addLayout(h)
        self.label = QLabel("")
        v.addWidget(self.label)

        w = QWidget()
        w.setLayout(v)
        self.setCentralWidget(w)


    def button_clicked(self, n):
        button = QObject.sender(self)
        text = button.text()  # type: ignore
        self.label.setText(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
