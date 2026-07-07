"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 569

9.2 - Extending Signals

Problems with loops

signals_extra_2.py
"""

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        v = QVBoxLayout()
        h = QHBoxLayout()

        for a in range(10):
            button = QPushButton(str(a))
            button.clicked.connect(
                lambda checked: self.button_clicked(a)
            )
            h.addWidget(button)

        v.addLayout(h)
        self.label = QLabel("")
        v.addWidget(self.label)

        w = QWidget()
        w.setLayout(v)
        self.setCentralWidget(w)


    def button_clicked(self, n):
        self.label.setText(str(n))


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()


