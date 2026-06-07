"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 503

7.4 - Graceful thread shutdown using a custom stop() method

qthread_3.py
"""

# Import modules
import sys
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



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
        self.data = None
        self.is_running = True
        print("Thread start")
        counter = 0
        while self.is_running:
            time.sleep(0.1)
            # Output the number as a formatted string.
            self.result.emit(f"The number is {counter}")
            counter += 1


    def stop(self):
        self.is_running = False



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create thread and start it.
        self.thread = Thread()  # type: ignore
        self.thread.start()     # type: ignore

        label = QLabel("Output will appear here")
        button = QPushButton("Shutdown thread")
        # Shutdown the thread nicely.
        button.pressed.connect(self.thread.stop)  # type: ignore

        # Connect signal, so output appears on label.
        self.thread.result.connect(label.setText)    # type: ignore
        self.thread.finished.connect(self.thread_has_finished)  #type: ignore

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        container.setLayout(layout)

        self.setCentralWidget(container)


    def thread_has_finished(self):
        print("Thread has finished.")
        print(
            self.thread,
            self.thread.isRunning(),  # type: ignore
            self.thread.isFinished(), # type: ignore
        )


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


