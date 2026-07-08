"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 600

9.6 - Working with command-line arguments

Open a Text File from Command-Line Arguments in PySide6

arguments_open.py
"""

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()

        print(sys.argv)

        if len(sys.argv) > 1:
            filename = sys.argv[1]
            self.open_file(filename)

        self.setCentralWidget(self.editor)
        self.setWindowTitle("Text viewer")


    def open_file(self, fn):
        with open(fn, "r") as f:
            text = f.read()

        self.editor.setPlainText(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

