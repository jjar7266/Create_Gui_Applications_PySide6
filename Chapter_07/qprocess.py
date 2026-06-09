"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 515

7.5 - Running external commands & processes

QProcess Exteranl Command Runner with Live Progress Parsing and
Status-Bar State Updates

qprocess.py
"""

# Import modules
import os
import re
import sys

from PySide6.QtCore import QProcess
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

STATES = {
    QProcess.ProcessState.NotRunning: "Not running",
    QProcess.ProcessState.Starting: "Starting...",
    QProcess.ProcessState.Running: "Running...",
}

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


def extract_vars(output):
    """
    Extracts variables from lines, looking for lines
    containing an equals, and splitting into key=value.
    """
    data = {}
    for s in output.splitlines():
        if "=" in s:
            name, value = s.split("=")
            data[name] = value
    return data



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Hold process reference.
        self.p = None

        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        layout.addWidget(self.text)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        btn_run = QPushButton("Execute")
        btn_run.clicked.connect(self.start)

        layout.addWidget(btn_run)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)


    def start(self):
        if self.p is not None:
            return

        self.p = QProcess()
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.readyReadStandardError.connect(self.handle_stderr)
        self.p.stateChanged.connect(self.handle_state)
        self.p.finished.connect(self.cleanup)

        script_path = os.path.join(basedir, "dummy_script.py")
        self.p.start("python", [script_path])


    def handle_stderr(self):
        result = bytes(self.p.readAllStandardError()).decode("utf8")  #type: ignore
        progress = simple_percent_parser(result)
        if progress is not None:
            self.progress.setValue(progress)


    def handle_stdout(self):
        result = bytes(self.p.readAllStandardOutput()).decode("utf8") #type: ignore
        data = extract_vars(result)

        self.text.appendPlainText(str(data))


    def handle_state(self, state):
        self.statusBar().showMessage(STATES[state])


    def cleanup(self):
        self.p = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()




