# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 165
#
# 2.8 Events - QContextMenuEvent (custom context menu)

# Import modules
import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()




