"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 434

7.2 - Using the thread pool

Emitting Signals from a Callable in QThreadPool

qthreadpool_start_2.py
"""

# Import modules
import sys
import time

from PySide6.QtCore import QThreadPool, QTimer, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



class MainWindow(QMainWindow):
    custom_signal = Signal()

    def __init__(self):
        super().__init__()

        # Connect our custom signal to a handler.
        self.custom_signal.connect(self.signal_handler)

        self.threadpool = QThreadPool()
        thread_n = self.threadpool.maxThreadCount()
        print(f"Threadpool with maximum {thread_n} threads")

        self.counter = 0

        layout = QVBoxLayout()

        self.l =  QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()


    def oh_no(self):
        self.threadpool.start(self.do_some_work)

    @Slot()
    def do_some_work(self):
        print("Thread start")
        # Emit our custom signal.
        self.custom_signal.emit()
        for n in range(5):
            time.sleep(1)
        self.counter = self.counter - 10
        print("Thread complete")

    def signal_handler(self):
        print("Signal received!")

    def recurring_timer(self):
        self.counter += 1
        self.l.setText(f"Counter: {self.counter}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

