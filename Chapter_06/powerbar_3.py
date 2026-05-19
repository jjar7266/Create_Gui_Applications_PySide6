"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 391

6.2 - Creating Custom Widgets

PowerBar with Dynamic Value Rendering

powerbar_3.py
"""

# Import modules
import sys

from PySide6.QtCore import QRect, Qt, QSize
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtWidgets import (
    QApplication,
    QDial,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class _Bar(QWidget):
    def __init__(self):
        super().__init__()

        self.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding,
            QSizePolicy.Policy.MinimumExpanding,
        )


    def sizeHint(self):
        return QSize(40, 120)


    def paintEvent(self, e):
        painter = QPainter(self)

        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        rect = QRect(
            0, 0, painter.device().width(), painter.device().height()
        )
        painter.fillRect(rect, brush)

        # Get current state.
        dial = self.parent()._dial     # type: ignore
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QColor("red"))
        painter.setPen(pen)

        font = painter.font()
        font.setFamily("Times")
        font.setPointSize(18)
        painter.setFont(font)

        painter.drawText(
            25, 25, "{}-->{}<--{}".format(vmin, value, vmax)
        )
        painter.end()



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


