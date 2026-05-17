"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 366

6.1 Bitmap Graphics in Qt

QPainter - Drawing Random Colored Points

points_color.py
"""

# Import modules
import sys

from random import randint, choice
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)

        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        colors = [
            "#FFD141",
            "#376F9F",
            "#0D1F2D",
            "#E9EBEF",
            "#EB5160",
        ]

        painter = QPainter(self.canvas)
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(10000):
            # pen = painter.pen() you could get the active pen here
            pen.setColor(QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200 + randint(-100, 100),
                150 + randint(-100, 100),  # x  # y
            )
        painter.end()
        self.label.setPixmap(self.canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



