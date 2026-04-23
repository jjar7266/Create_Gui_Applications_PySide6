# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 3 — Qt Designer
# Page 183
#
# 3.2 — Create a wrapper class and load the UI inside it
# example_3.py
#
# This example introduces a wrapper class (not a widget subclass)
# that loads the .ui file and exposes it as self.ui.

# -----------------------------
# IMPORTS
# -----------------------------
import os
import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


# -----------------------------
# PATH + LOADER SETUP
# -----------------------------
basedir = os.path.dirname(__file__)
loader = QUiLoader()


# -----------------------------
# WRAPPER CLASS
# -----------------------------
# This class is NOT a QWidget subclass.
# It simply loads the UI and stores it in self.ui.
class MainUI:
    def __init__(self):
        super().__init__()

        # Load the UI using the book-style string path
        ui_path = os.path.join(basedir, "mainwindow.ui")
        self.ui = loader.load(ui_path, None)

        # Apply additional setup
        self.ui.setWindowTitle("MainWindow Title")

        # Show the loaded UI
        self.ui.show()


# -----------------------------
# APPLICATION STARTUP
# -----------------------------
app = QApplication(sys.argv)

# Create the wrapper class instance
ui = MainUI()

# Start the event loop
app.exec()
