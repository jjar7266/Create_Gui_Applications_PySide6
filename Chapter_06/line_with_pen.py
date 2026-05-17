"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 366

6.1 Bitmap Graphics in Qt

QPainter - Drawing a Line Using a Custom Pen

line_with_pen.py
"""

# Import modules
import sys

from PySide6.QtCore import Qt, QPoint
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
        painter = QPainter(self.canvas)
        pen = QPen()
        pen.setWidth(15)
        pen.setColor(QColor("blue"))
        painter.setPen(pen)
        painter.drawLine(QPoint(100, 100), QPoint(300, 200))
        painter.end()
        self.label.setPixmap(self.canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



