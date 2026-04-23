# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 3 — Qt Designer
# Page 182
#
# 3.2 — QUiLoader: Loading your .ui file in Python
# example_1.py

# -----------------------------
# IMPORTS
# -----------------------------
# sys → needed to pass command-line arguments to QApplication
# os → used to build a reliable path to the .ui file
import sys
import os

# QUiLoader → loads .ui files created in Qt Designer
from PySide6.QtUiTools import QUiLoader

# QApplication → the main Qt application object
from PySide6.QtWidgets import QApplication

# QFile → REQUIRED for modern PySide6 when loading .ui files
#         (the book uses a string path, but that no longer works)
from PySide6.QtCore import QFile


# -----------------------------
# PATH SETUP
# -----------------------------
# __file__ = the current Python file
# dirname(__file__) = the folder containing this script
# We use this so the script can find the .ui file no matter where it's run from.
basedir = os.path.dirname(__file__)


# -----------------------------
# CREATE THE LOADER
# -----------------------------
# QUiLoader is responsible for reading and constructing widgets
# from .ui files created in Qt Designer.
loader = QUiLoader()


# -----------------------------
# CREATE THE APPLICATION
# -----------------------------
# QApplication must be created before any Qt widgets.
app = QApplication(sys.argv)


# -----------------------------
# LOAD THE .ui FILE (MODERN WAY)
# -----------------------------
# IMPORTANT:
#   The book uses:
#       loader.load("mainwindow.ui")
#   But modern PySide6 requires a QFile object instead of a string.
#
# Step 1: Build the full path to the .ui file
ui_path = os.path.join(basedir, "mainwindow.ui")

# Step 2: Wrap the path in a QFile object
ui_file = QFile(ui_path)

# Step 3: Open the file in read-only mode
ui_file.open(QFile.ReadOnly)  # type: ignore

# Step 4: Load the UI using QUiLoader
window = loader.load(ui_file)

# Step 5: Close the QFile (good practice)
ui_file.close()


# -----------------------------
# SHOW THE WINDOW
# -----------------------------
window.show()


# -----------------------------
# START THE EVENT LOOP
# -----------------------------
app.exec()
