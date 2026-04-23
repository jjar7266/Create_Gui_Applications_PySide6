# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 3 — The Qt Resource System
# Page 194
#
# Example 3.3 — qresource.py
#
# This example demonstrates how to load an image (PNG) directly
# from the filesystem using QIcon. This is *before* using the
# Qt Resource System (.qrc). The icon will only load correctly
# if the PNG file is located in the current working directory
# when the script is executed.

# --------------------------------------------------------------
# Import modules
# --------------------------------------------------------------

import sys

# QIcon is used to load and apply an image to a widget (like a button)
from PySide6.QtGui import QIcon

# QApplication initializes the Qt event loop
# QMainWindow provides a main application window
# QPushButton is the clickable button widget
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)


# --------------------------------------------------------------
# Main application window
# --------------------------------------------------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Hello World")

        # Create a QPushButton instance
        b = QPushButton("My button")

        # ----------------------------------------------------------
        # Load the PNG file using QIcon
        #
        # IMPORTANT:
        # QIcon("animal-penguin.png") looks for the file in the
        # *current working directory*, not the script's folder.
        #
        # This means the PNG must be located in the same folder
        # where you run the command:
        #     python qresource.py
        #
        # If the file is not found, the button will appear without
        # an icon, but no error will be raised.
        # ----------------------------------------------------------
        icon = QIcon("animal-penguin.png")

        # Apply the icon to the button
        b.setIcon(icon)

        # Set the button as the central widget of the window
        self.setCentralWidget(b)


# --------------------------------------------------------------
# Application entry point
# --------------------------------------------------------------

# Create the QApplication object (required for all Qt apps)
app = QApplication(sys.argv)

# Create and show the main window
window = MainWindow()
window.show()

# Start the Qt event loop
app.exec()
