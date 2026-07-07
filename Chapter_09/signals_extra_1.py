"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 568

9.2 - Extending Signals

Intercepting the signal

signals_extra_1.py
"""

# Import modules
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        btn = QPushButton("Press Me")
        btn.setCheckable(True)
        btn.clicked.connect(
            lambda checked: self.button_clicked(checked, btn)
        )

        self.setCentralWidget(btn)


    def button_clicked(self, checked, btn):
        print(btn, checked)
        btn.hide()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
