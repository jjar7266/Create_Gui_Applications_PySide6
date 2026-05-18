"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 374

6.1 Bitmap Graphics in Qt

QPainter - Centered Text Rendering with QPainter Alignment Flags

text_b.py
"""
# This code is not in the book

# Import modules
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        """
        Draws centered text onto the QPixmap canvas using QPainter.
        This version uses Qt's alignment system instead of fixed coordinates,
        ensuring the text appears centered on all platforms and DPI settings.
        """

        # Create a QPainter object that will draw directly onto the QPixmap.
        painter = QPainter(self.canvas)

        # -------------------------------
        # 1. Configure the drawing pen
        # -------------------------------
        pen = QPen()
        pen.setWidth(1)                    # Thin outline for the text
        pen.setColor(QColor("green"))      # Text color
        painter.setPen(pen)

        # -------------------------------
        # 2. Configure the font
        # -------------------------------
        font = QFont()
        font.setFamily("Times")            # Font family
        font.setBold(True)                 # Make the text bold
        font.setPointSize(40)              # Large readable size
        painter.setFont(font)

        # ---------------------------------------------------------
        # 3. Draw the text centered inside the entire canvas area
        # ---------------------------------------------------------
        # Instead of fixed coordinates (100, 100), we pass the full
        # rectangle of the pixmap and tell Qt to center the text.
        painter.drawText(
            self.canvas.rect(),            # The full drawing area
            Qt.AlignmentFlag.AlignCenter,  # Center horizontally & Vertically
            "Hello, World!"                # The text to draw
        )

        # Finalize painting operations
        painter.end()

        # Update the QLabel so the new drawing appears in the window
        self.label.setPixmap(self.canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


