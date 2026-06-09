"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 7 - Concurrent Execution
Page 511

7.4 - QThread With Split Data Submission Methods and
      Explicit Triggered Calculation

qthread_6b.py
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
    QSpinBox,
    QVBoxLayout,
    QWidget,
)



class Thread(QThread):
    """
    Worker thread
    """

    result = Signal(str)

    def __init__(self, initial_counter):
        super().__init__()
        self.counter = initial_counter

    @Slot()
    def run(self):
        """
        Your code goes in this method
        """
        print("Thread start")
        self.is_running = True
        self.waiting_for_data = True
        while True:
            while self.waiting_for_data:
                if not self.is_running:
                    return  # Exit thread.
                time.sleep(0.1)  # wait for data

            # Output the number as a formatted string.
            self.counter += self.input_add
            self.counter *= self.input_multiply
            self.result.emit(
                f"The cumulative total is {self.counter}"
            )
            self.waiting_for_data = True


    def send_add(self, add):
        self.input_add = add


    def send_multiply(self, multiply):
        self.input_multiply = multiply


    def calculate(self):
        self.waiting_for_data = (
            False  # Release the lock & calculate.
        )

    def stop(self):
        self.is_running = False



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create thread and start it.
        self.thread = Thread(500)  #type: ignore
        self.thread.start()        #type: ignore

        self.add_input = QSpinBox()
        self.mult_input = QSpinBox()
        button_input = QPushButton("Submit number")

        label = QLabel("Output will appear here")

        button_stop = QPushButton("Shutdown thread")
        # Shutdown the thread nicely.
        button_stop.pressed.connect(self.thread.stop)    #type: ignore

        # Connect signal, so output appears on label.
        button_input.pressed.connect(self.submit_data)   #type: ignore
        self.thread.result.connect(label.setText)        #type: ignore
        self.thread.finished.connect(self.thread_has_finished)  #type: ignore

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.add_input)
        layout.addWidget(self.mult_input)
        layout.addWidget(button_input)
        layout.addWidget(label)
        layout.addWidget(button_stop)
        container.setLayout(layout)

        self.setCentralWidget(container)


    def submit_data(self):
        # Submit the value in the numeric_input widget to the thread.
        self.thread.send_add(self.add_input.value())        #type: ignore
        self.thread.send_multiply(self.mult_input.value())  #type: ignore
        self.thread.calculate()                             #type: ignore


    def thread_has_finished(self):
        print("Thread has finished.")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

