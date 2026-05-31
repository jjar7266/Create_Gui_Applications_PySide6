"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 467

7.3 - QRunnable I/O Parser - Concurrent HTML Extraction with Custom Regex Signals

qrunnable_io_parser.py
"""

# Import modules

import re
import sys
import requests

from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    Signal,
    Slot,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    data
        tuple of (identifier, data)
    """

    data = Signal(tuple)



class Worker(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.

    :param id: The id for this worker
    :param url: The url to retrieve
    """

    def __init__(self, id, url, parsers):
        super().__init__()
        self.id = id
        self.url = url
        self.parsers = parsers

        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        r = requests.get(self.url)

        data = {}
        for name, parser in self.parsers.items():
            m = parser.search(r.text)
            if m:
                data[name] = m.group(1).strip()

        self.signals.data.emit((self.id, data))



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.urls = [
            "https://www.pythonguis.com/",
            "https://www.martinfitzpatrick.com/",
            "https://www.google.com",
            "https://courses.pythonguis.com/"
        ]

        self.parsers = {
            # Regular expression parsers,
            # to extract data from the HTML.
            "title": re.compile(
                r"<title.*?>(.*?)<\/title>", re.M | re.S
            ),
            "h1": re.compile(r"<h1.*?>(.*?)<\/h1>", re.M | re.S),
            "h2": re.compile(r"<h2.*?>(.*?),\/h2>", re.M | re.S),
        }

        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        button = QPushButton("Go GET EM!")
        button.pressed.connect(self.execute)

        layout.addWidget(self.text)
        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.threadpool = QThreadPool()
        thread_n = self.threadpool.maxThreadCount()
        print(f"Threadpool with maximum {thread_n} threads")


    def execute(self):
        for n, url in enumerate(self.urls):
            worker = Worker(n, url, self.parsers)
            worker.signals.data.connect(self.display_output)

            # Execute
            self.threadpool.start(worker)


    def display_output(self, data):
        id, s = data
        self.text.appendPlainText(f"WORKER {id}: {s}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()




