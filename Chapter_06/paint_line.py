"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 378

6.1 Bitmap Graphics in Qt

Drawing Continuous Lines with QPainter and Mouse Tracking

paint_line.py
"""

# Import modules
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)

        self.last_position = None


    def mouseMoveEvent(self,e):
        pos = e.position()
        if self.last_position is None:  # First event.
            self.last_position = pos
            return  # Ignore the first time.

        painter = QPainter(self.canvas)
        painter.drawLine(self.last_position, pos)
        painter.end()

        self.label.setPixmap(self.canvas)

        # Update the origin for next time.
        self.last_position = pos


    def mouseReleaseEvent(self, e):
        self.last_position = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

