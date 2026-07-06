"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 8 - Plotting
Page 554

8.2 Plotting with Matplotlib

Embedding a Pandas DataFrame Plot Inside a PySide6 Matplotlib Canvas

matplotlib_5.py
"""

# Import modules
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import matplotlib  # import matplotlib after PySide6
import pandas as pd
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

        # Create our pandas DataFrame with some simple
        # data and headers.
        df = pd.DataFrame(
            [[0, 10], [5, 15], [2, 20], [15, 25], [4, 10]],
            columns = ["A", "B"],
        )

        # plot the pandas DataFrame, passing in the
        # matplotlib Canvas axes.
        df.plot(ax=sc.axes)

        self.setCentralWidget(sc)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


