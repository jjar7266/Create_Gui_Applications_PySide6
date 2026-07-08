"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 603

9.7 - Pythonic PySide6

Pythonic PySide6 Table Insert Example Using
snake_case and true_property

pythonic_2.py
"""
# NOTE:
# VS Code (Pylance) may flag PySide6 Pythonic features as "missing" or "unknown".
# This is normal — PySide6 enables these features at runtime.
# The code runs correctly; warnings can be ignored or silenced with `# type: ignore`.


# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from __feature__ import snake_case, true_property # noqa


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        self.table.column_count = 2

        self.text = QLineEdit()

        self.button = QPushButton()
        self.button.text = "Insert item"
        self.button.enabled = True
        self.button.pressed.connect(self.add_item)

        layout = QVBoxLayout()
        layout.add_widget(self.table)
        layout.add_widget(self.text)
        layout.add_widget(self.button)
        self.set_layout(layout)


    def add_item(self):
        text = self.text.text
        item = QTableWidgetItem(text)
        self.table.insert_row(0)
        self.table.set_item(0, 0, item)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()









