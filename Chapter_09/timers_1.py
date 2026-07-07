"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 560

9.1 - Timers

Interval timers - QTimer-Driven Auto_Incrementing QDial in a PySide6 QMainWindow

timers_1.py
"""

# Import modules
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QDial, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.setValue(0)

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_dial)
        self.timer.start()

        self.setCentralWidget(self.dial)


    def update_dial(self):
        value = self.dial.value()
        value += 1  # increment
        if value > 100:
            value = 0
        self.dial.setValue(value)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

