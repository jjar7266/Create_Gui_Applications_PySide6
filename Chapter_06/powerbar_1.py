"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 390

6.2 - Creating Custom Widgets

PowerBar Custom Widget with Basic Painted Bar

powerbar_1.py
"""

# Import modules
import sys

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtWidgets import (
    QApplication,
    QDial,
    QVBoxLayout,
    QWidget,
)


class _Bar(QWidget):
    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        rect = QRect(
            0, 0, painter.device().width(), painter.device().height()
        )
        painter.fillRect(rect, brush)



class PowerBar(QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, parent=None, step=5):
        super().__init__(parent)

        layout = QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QDial()
        layout.addWidget(self._dial)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = PowerBar()
window.show()
app.exec()


