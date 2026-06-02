"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 478

7.3 - QRunnable subprocess example for executing external scripts
      in a worker thread.

qrunnable_process.py
"""

# Import modules

import os
import subprocess
import sys

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

basedir = os.path.dirname(__file__)



class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished: No data
    result: str
    """

    result = Signal(
        str
    )  # Send back the output from the process as a string.
    finished = Signal()



class SubProcessWorker(QRunnable):
    """
    ProcessWorker worker thread

    Inherits from QRunnable to handle worker thread setup,
    signals and wrap-up.

    :param command: command to execute with 'subprocess'.

    """

    def __init__(self, command):
        super().__init__()

        # Super constructor arguments (re-used for processing).
        self.signals = WorkerSignals()

        # The command to be executed.
        self.command = command


    @Slot()
    def run(self):
        """
        Execute the command, returning the result.
        """

        output = subprocess.getoutput(self.command)
        self.signals.result.emit(output)
        self.signals.finished.emit()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Some buttons
        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        layout.addWidget(self.text)

        btn_run = QPushButton("Execute")
        btn_run.clicked.connect(self.start)

        layout.addWidget(btn_run)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        # Thread runner
        self.threadpool = QThreadPool()


    def start(self):
        script_path = os.path.join(basedir, "dummy_script.py")

        # Create a runner
        self.runner = SubProcessWorker(
            f"{sys.executable} {script_path}"
        )
        self.runner.signals.result.connect(self.result)
        self.threadpool.start(self.runner)


    def result(self, s):
        self.text.appendPlainText(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()





