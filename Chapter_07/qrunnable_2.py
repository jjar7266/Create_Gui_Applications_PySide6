"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 435

7.2 - Using the thread pool

Extending QRunnable to Pass Arguments to Worker Threads

qrunnable_2.py
"""

# Import modules
import sys

from PySide6.QtCore import QRunnable, QThreadPool, QTimer, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



class Worker(QRunnable):
    """
    Worker thread

    :param args: Arguments to make available to the run code
    :param kwargs: Keywords arguments to make available to the run
    :code
    :
    """

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        """
                Initialize the runner function with passed self.args,
                self.kwargs
        """
        print(self.args, self.kwargs)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = QThreadPool()
        thread_n = self.threadpool.maxThreadCount()
        print(f"Threadpool with maximum {thread_n}")

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
        worker = Worker("Some", "arguments", keywords=2)
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText(f"Counter: {self.counter}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


