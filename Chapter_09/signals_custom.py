"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 565

9.2 - Extending Signals

Custom Slots Demonstration with Typed and Overloaded Slot Methods

signals_custom.py
"""

# Import modules
import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    message  = Signal(str)
    value    = Signal(int, str, int)
    another  = Signal(list)
    onemore  = Signal(dict)
    anything = Signal(object)

    def __init__(self):
        super().__init__()

        self.message.connect(self.custom_slot)
        self.value.connect(self.custom_slot)
        self.another.connect(self.custom_slot)
        self.onemore.connect(self.custom_slot)
        self.anything.connect(self.custom_slot)

        self.message.emit("my message")
        self.value.emit(23, "abc", 1)
        self.another.emit([1, 2, 3, 4, 5])
        self.onemore.emit({"a": 2, "b": 7})
        self.anything.emit(1223)

    def custom_slot(self, *args):
        print(args)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()


