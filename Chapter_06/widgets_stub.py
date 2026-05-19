"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 387

6.2 - Creating Custom Widgets

Stub Implementation for PowerBar Custom Widget

widgets_stub.py
"""

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QDial,
    QVBoxLayout,
    QWidget,
)



class _Bar(QWidget):
    pass



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


