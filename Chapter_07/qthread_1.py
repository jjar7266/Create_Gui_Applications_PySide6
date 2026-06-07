"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 498

7.4 - Long-running threads with a simple QThread

qthread_1.py
"""

# Import modules
import sys
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow



class Thread(QThread):
    """
    Worker thread
    """

    result = Signal(str)

    @Slot()
    def run(self):
        """
        Your code goes in this method
        """
        print("Thread start")
        counter = 0
        while True:
            time.sleep(0.1)
            # Output the number as a formatted string.
            self.result.emit(f"The number is {counter}")
            counter += 1
        print("Thread complete")



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create thread and start it.

        self.thread = Thread()                       # type: ignore[assignment]
        self.thread.start()                          # type: ignore[call-arg]

        label = QLabel("Oupput will appear here")

        # Connect signal, so output appears on label.
        self.thread.result.connect(label.setText)    # type: ignore[attr-defined]

        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



