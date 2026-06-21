"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 8 - Plotting
Page 539

8.1 Plotting with PyQtGraph

PyQtGraph Multiple Line Plot with Reusable Plot Function

pyqtgraph_5.py
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
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

        # Add Background color to white
        self.graphWidget.setBackground("w")

        # Add Title
        self.graphWidget.setTitle(
            "Your Title Here", color="b", size="30pt"
        )

        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel(
            "left", "Temperature (°C)", **styles
        )
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)

        # Add legend (anchored to top-right corner)  # Not in the book
        legend = self.graphWidget.addLegend()
        legend.setParentItem(self.graphWidget.graphicsItem())
        legend.anchor((1, 0), (1, 0))  # (x, y): (1, 0) = top-right

        # Add grid
        self.graphWidget.showGrid(x=True, y=True)

        # Set Range
        self.graphWidget.setXRange(0, 10, padding=0)   #type: ignore
        self.graphWidget.setYRange(20, 55, padding=0)  #type: ignore

        self.plot(hour, temperature_1, "Sensor1", "r")
        self.plot(hour, temperature_2, "Sensor2", "b")


    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(
            x,
            y,
            name=plotname,
            pen=pen,
            symbol="+",
            symbolSize=30,
            symbolBrush=(color),
        )


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()








