"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 441

7.3 - QRunnable examples

All the examples follow the same general pattern — a custom QRunnable class
with custom WorkerSignals. The difference is in what we pass to the runner,
what it does with those parameters, and how we hook up the signals

qrunnable_base.py
"""

# Import modules
import sys

from PySide6.QtCore import QObject, QRunnable, Slot
from PySide6.QtWidgets import QApplication, QMainWindow



class WorkerSignals(QObject):
    pass



class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Store constructor arguments (re-used for processing)
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()


    @Slot()
    def run(self):
        pass



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


