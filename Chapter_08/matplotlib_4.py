"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 8 - Plotting
Page 552

8.2 Plotting with Matplotlib

Real-Time Matplotlib Plot Using Line Reference Updates in a PySide6 QmainWindow

matplotlib_4.py
"""

# Import modules
import random
import sys

from PySide6.QtCore import QTimer
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

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]

        # We need to store a reference to the plotted line
        # Somewhere, so we can apply the new data to it.
        self._plot_ref = None
        self.update_plot()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]

        # Note: we no longer need to clear the axis.
        if self._plot_ref is None:
            # First time we have no plot reference, so we call plot
            # normally, The .plot call returns a list of line
            # references, as we're only getting one we can take the
            # first element.
            plot_refs = self.canvas.axes.plot(
                self.xdata, self.ydata, "r"
            )
            self._plot_ref = plot_refs[0]

        else:
            # We have a reference, now we can use it
            # to update the data for that line.
            self._plot_ref.set_ydata(self.ydata)

        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


