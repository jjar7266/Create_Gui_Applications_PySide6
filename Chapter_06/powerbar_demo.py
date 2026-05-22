"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 6 - Custom Widgets
Page 414

6.2 - Creating Custom Widgets

PowerBar Demo Integrated into a Standard Main Window

powerbar_demo.py
"""

# Import modules
import sys

from powerbar import PowerBar

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        powerbar = PowerBar(steps=10)
        layout.addWidget(powerbar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


