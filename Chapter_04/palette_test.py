# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 4 — Theming
# Page 206
#
# 4.2 — Palettes
# palette_test.py
#
# This example demonstrates how to modify the application's
# color palette using QPalette. A palette defines the colors
# used for different UI roles (window background, text, buttons,
# highlights, etc.). Here we apply a custom background color and
# text color to the entire application.

# --------------------------------------------------------------
# Import modules
# --------------------------------------------------------------

import sys

# Qt provides color constants (e.g., Qt.white)
from PySide6.QtCore import Qt

# QColor represents an RGB color
# QPalette stores color roles for widgets and windows
from PySide6.QtGui import QColor, QPalette

# QLabel is used here as a simple window to display text
from PySide6.QtWidgets import QApplication, QLabel


# --------------------------------------------------------------
# Application setup
# --------------------------------------------------------------

# Every Qt application needs a QApplication instance
app = QApplication(sys.argv)

# Create a QPalette object that we will customize
palette = QPalette()

# --------------------------------------------------------------
# Set custom colors for the palette
#
# QPalette.ColorRole.Window:
#   The background color of windows and widgets.
#
# QPalette.ColorRole.WindowText:
#   The color of text displayed on window backgrounds.
#
# QColor(0, 128, 255):
#   A bright blue color defined using RGB values.
#
# Qt.GlobalColor.white:
#   A predefined Qt color constant.
# --------------------------------------------------------------

palette.setColor(QPalette.ColorRole.Window, QColor(0, 128, 255))
palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)

# Apply the palette to the entire application
app.setPalette(palette)


# --------------------------------------------------------------
# Create a simple window to demonstrate the palette
# --------------------------------------------------------------

window = QLabel("Palette Test")   # A label acts as our window
window.show()                     # Display the window


# --------------------------------------------------------------
# Start the Qt event loop
# --------------------------------------------------------------

app.exec()
