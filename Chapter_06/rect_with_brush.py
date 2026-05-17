"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 370

6.1 Bitmap Graphics in Qt

QPainter - Drawing Rectangles with a Brush Fill

rect_with_brush.py
"""

# Import modules
import sys

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QBrush
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
        pen.setWidth(3)
        pen.setColor(QColor("#376F9F"))
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(QColor("#FFD141"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)

        painter.drawRects(
            [
                QRect(50, 50, 100, 100),
                QRect(60, 60, 150, 100),
                QRect(70, 70, 100, 150),
                QRect(80, 80, 150, 100),
                QRect(90, 90, 100, 150),
            ]
        )
        painter.end()
        self.label.setPixmap(self.canvas)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



