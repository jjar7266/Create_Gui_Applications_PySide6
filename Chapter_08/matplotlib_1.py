"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 8 - Plotting
Page 544

8.2 Plotting with Matplotlib

A simple Example - Embedded Matplotlib Plot in a PySide6
                   QMainWindow Using FigureCanvasQTAgg

matplotlib_1.py
"""

# Import modules
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import matplotlib  # import matplotlib after PySide6
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


matplotlib.use("QtAgg")


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create the matplotlib FigureCanvasQTAgg object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        self.setCentralWidget(sc)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
