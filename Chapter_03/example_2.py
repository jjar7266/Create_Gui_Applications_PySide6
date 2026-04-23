# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 3 — Qt Designer
# Page 182
#
# 3.2 — QUiLoader: example_2.py
#
# This example builds on example_1 by adding a function
# that modifies the loaded UI after it has been created.

# -----------------------------
# IMPORTS
# -----------------------------
import os
import sys

# QUiLoader loads .ui files created in Qt Designer
from PySide6.QtUiTools import QUiLoader

# QApplication is required for all Qt applications
from PySide6.QtWidgets import QApplication


# -----------------------------
# PATH SETUP
# -----------------------------
# __file__ gives us the current script's directory.
# We use this to reliably locate mainwindow.ui.
basedir = os.path.dirname(__file__)


# -----------------------------
# CREATE THE LOADER
# -----------------------------
loader = QUiLoader()


# -----------------------------
# SETUP FUNCTION
# -----------------------------
# This function receives the loaded UI object (the window)
# and applies additional configuration to it.
def mainwindow_setup(w):
    # Change the window title after loading the .ui file
    w.setWindowTitle("MainWindow Title")


# -----------------------------
# APPLICATION STARTUP
# -----------------------------
app = QApplication(sys.argv)


# -----------------------------
# LOAD THE .ui FILE (BOOK STYLE)
# -----------------------------
# The book uses the string-path version of loader.load().
# Your PySide6 build still supports this, so it works fine.
ui_path = os.path.join(basedir, "mainwindow.ui")
window = loader.load(ui_path, None)


# -----------------------------
# APPLY POST-LOAD SETUP
# -----------------------------
mainwindow_setup(window)


# -----------------------------
# SHOW THE WINDOW
# -----------------------------
window.show()


# -----------------------------
# START THE EVENT LOOP
# -----------------------------
app.exec()
