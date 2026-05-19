"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 376

6.1 Bitmap Graphics in Qt

Drawing Points with QPainter Using Mouse Movement

paint_start.py
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


    def mouseMoveEvent(self, e):
        pos = e.position()
        painter = QPainter(self.canvas)
        painter.drawPoint(pos)
        # or: painter.drawPoint(int(pos.x()), int(pos.y()))
        painter.end()
        self.label.setPixmap(self.canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

