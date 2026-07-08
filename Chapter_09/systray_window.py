"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 585

9.4 - System tray & macOS menus

Full Application with System Tray Integration

systray_window.py
"""

# Import modules
import os
import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QSystemTrayIcon,
    QTextEdit,
)

basedir = os.path.dirname(__file__)

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon(os.path.join(basedir, "animal-penguin.png"))


# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()
        self.load()  # Load up the text from file.

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")

        self.reset = QAction("&Reset")
        self.reset.triggered.connect(self.editor.clear)
        file_menu.addAction(self.reset)

        self.quit = QAction("&Quit")
        self.quit.triggered.connect(app.quit)
        file_menu.addAction(self.quit)

        self.setCentralWidget(self.editor)

        self.setWindowTitle("PenguinNotes")


    def load(self):
        try:
            with open("notes.txt", "r") as f:
                text = f.read()

        except FileNotFoundError:
            pass  # ignore

        else:
            self.editor.setPlainText(text)


    def save(self):
        text = self.editor.toPlainText()
        with open("notes.txt", "w") as f:
            f.write(text)


    def activate(self, reason):
        if (
            reason == QSystemTrayIcon.ActivationReason.Trigger
        ):  # Icon clicked.
            self.show()


window = MainWindow()

tray.activated.connect(window.activate)
app.aboutToQuit.connect(window.save)

app.exec()
