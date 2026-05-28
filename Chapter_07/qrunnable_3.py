"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 437

7.2 - Worker Signals and Thread I/O with QRunnable

Thread IO

qrunnable_3.py
"""

# Import modules
import random
import sys
import time

from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    QTimer,
    Signal,
    Slot,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        'str' Exception string

    result
        'dict' data returned from processing

    """

    finished = Signal()
    error = Signal(str)
    result = Signal(dict)



class Worker(QRunnable):
    """
    Worker thread

    :param args: Arguments to make available to the run code
    :param kwargs: Keywords arguments to make available to the run code
    :
    """

    def __init__(self, iterations=5):
        super().__init__()
        self.signals = (
            WorkerSignals()
        )  # Create an instance of our signals class.
        self.iterations = iterations


    @Slot()
    def run(self):
        """
        Initialize the runner function with passed self.args,
        self.kwargs.
        """
        try:
            for n in range(self.iterations):
                time.sleep(0.01)
                v = 5 / (40 - n)

        except Exception as e:
            self.signals.error.emit(str(e))

        else:
            self.signals.finished.emit()
            self.signals.result.emit({"n": n, "value": v})  #type: ignore



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = QThreadPool()
        thread_n = self.threadpool.maxThreadCount()
        print(f"ThreadPool with maximum {thread_n} threads")

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
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
        worker = Worker(iterations=random.randint(10, 50))
        worker.signals.result.connect(self.worker_output)
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)


    def worker_output(self, result):
        print("RESULT", result)


    def worker_complete(self):
        print("THREAD COMPLETE!")


    def worker_error(self, error):
        print(f"ERROR: {error}")


    def recurring_timer(self):
        self.counter += 1
        self.l.setText(f"Counter: {self.counter}")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()




