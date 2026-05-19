"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 381

6.1 Bitmap Graphics in Qt

Color-Palette Drawing Canvas with QPainter

paint.py
"""

# Import modules
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QPainter, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self._pixmap = QPixmap(600, 300)
        self._pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self._pixmap)

        self.last_position = None
        self.pen_color = QColor("#000000")


    def set_pen_color(self, c):
        self.pen_color = QColor(c)


    def mouseMoveEvent(self, e):
        pos = e.position()
        if self.last_position is None:  # First event.
            self.last_position = pos
            return  # Ignore the first time.

        painter = QPainter(self._pixmap)
        p = painter.pen()
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_position, pos)
        painter.end()
        self.setPixmap(self._pixmap)

        # Update the origin for next time.
        self.last_position = pos


    def mouseReleaseEvent(self, e):
        self.last_position = None


COLORS = [
    # 17 undertones https://lospec.com/palette-list/17undertones
    "#000000",
    "#141923",
    "#414168",
    "#3a7fa7",
    "#35e3e3",
    "#8fd970",
    "#5ebb49",
    "#458352",
    "#dcd37b",
    "#fffee5",
    "#ffd035",
    "#cc9245",
    "#a15c3e",
    "#a42f3b",
    "#f45b7a",
    "#c24998",
    "#81588d",
    "#bcb0c2",
    "#ffffff",
]


class QPaletteButton(QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QSize(24, 24))
        self.color = color
        self.setStyleSheet(f"background-color: {color};")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QWidget()
        layout = QVBoxLayout()
        w.setLayout(layout)
        layout.addWidget(self.canvas)

        palette = QHBoxLayout()
        self.add_palette_buttons(palette)
        layout.addLayout(palette)

        self.setCentralWidget(w)


    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(
                lambda c=c: self.canvas.set_pen_color(c)
            )
            layout.addWidget(b)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()






