"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 8 - Plotting
Page 524

8.1 Plotting with PyQtGraph

Basic PyQtGraph Line Plot Embedded in a QMainWindow

pyqtgraph_1.py
"""

# Import modules
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg  # import PyQtGraph after PySide6


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # plot data: x, y, values
        self.graphWidget.plot(hour, temperature)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
