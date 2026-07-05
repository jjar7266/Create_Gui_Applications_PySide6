"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 8 - Plotting
Page 541

8.1 Plotting with PyQtGraph

Real-Time PyQtGraph Line Plot with QTimer-Driven Data Updates

pyqtgraph_6.py
"""

# Import modules
import sys
from random import randint

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

import pyqtgraph as pg  # import PyQtGraph afer Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))  # type: ignore # 100 time points
        self.y = [randint(0, 100) for _ in range(100)]  # type: ignore # 100 data points

        self.graphWidget.setBackground("w")

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(
            self.x, self.y, pen=pen
        )

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]  # type: ignore # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # type: ignore # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # type: ignore # Remove the first
        self.y.append(randint(0, 100))  # type: ignore # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
