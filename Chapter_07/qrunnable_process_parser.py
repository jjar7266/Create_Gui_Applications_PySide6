"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 485

7.3 - QRunnable subprocess parser example with real-time progress
      extraction via regex

qrunnable_process_parser.py
"""

# Import modules
import os
import re
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
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

basedir = os.path.dirname(__file__)

progress_re = re.compile(r"Total complete: (\d+)%")


def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex,
    returning a single integer for the % progress.
    """
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)



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
    progress = Signal(
        int
    )  # Return an integer 0-100 showing the current progress.
    finished = Signal()



class SubProcessWorker(QRunnable):
    """
    ProcessWorker worker thread

    Inherits from QRunnable to handle worker thread setup,
    signals and wrap-up.

    :param command: command to execute with 'subprocess'.
    """

    def __init__(self, command, parser=None):
        super().__init__()

        # Store constructor arguments (re-used for processing).
        self.signals = WorkerSignals()

        # The command to be executed.
        self.command = command

        # The parser function to extract the progress information.
        self.parser = parser


    @Slot()
    def run(self):
        """
        Initialize the runner function with passed args, kwargs.
        """

        result = []

        with subprocess.Popen(
            self.command,
            bufsize=1,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        ) as proc:
            while proc.poll() is None:
                data = proc.stdout.readline()  #type: ignore
                result.append(data)
                if self.parser:
                    value = self.parser(data)
                    if value:
                        self.signals.progress.emit(value)

        output = "".join(result)

        self.signals.result.emit(output)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        layout.addWidget(self.text)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

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
            [sys.executable, script_path],
            parser=simple_percent_parser,
        )
        self.runner.signals.result.connect(self.result)
        self.runner.signals.progress.connect(self.progress.setValue)
        self.threadpool.start(self.runner)


    def result(self, s):
        self.text.appendPlainText(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


