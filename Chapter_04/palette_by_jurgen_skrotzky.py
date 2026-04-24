# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 4 — Theming
# Page 207
#
# 4.2 — Palettes
# palette_by_jurgen_skrotzky.py
#
# This example applies a complete custom dark theme to the entire
# application using a QPalette created by Jürgen Skrotzky.
#
# A QPalette defines colors for many UI roles (Window, Text, Button,
# Highlight, etc.). By customizing these roles, we can create a
# consistent global theme without using stylesheets.

# --------------------------------------------------------------
# Import modules
# --------------------------------------------------------------

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow


# --------------------------------------------------------------
# Create a dark palette
# --------------------------------------------------------------

darkPalette = QPalette()

# Window background color
darkPalette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))

# Normal window text color
darkPalette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)

# Disabled window text color (grayed out)
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.WindowText,
    QColor(127, 127, 127)
)

# Base background for text entry widgets (QLineEdit, QTextEdit, etc.)
darkPalette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))

# Alternate row background (used in lists/tables)
darkPalette.setColor(QPalette.ColorRole.AlternateBase, QColor(66, 66, 66))

# Tooltip background and text
darkPalette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
darkPalette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)

# Normal text color
darkPalette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)

# Disabled text color
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.Text,
    QColor(127, 127, 127)
)

# Darker shadow and frame colors
darkPalette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
darkPalette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))

# Button background and text
darkPalette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
darkPalette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)

# Disabled button text
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.ButtonText,
    QColor(127, 127, 127)
)

# Bright text (used for warnings or emphasis)
darkPalette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)

# Link color
darkPalette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))

# Highlight color (selection background)
darkPalette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))

# Disabled highlight color
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.Highlight,
    QColor(80, 80, 80),
)

# Highlighted text color (text inside selected items)
darkPalette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)

# Disabled highlighted text
darkPalette.setColor(
    QPalette.ColorGroup.Disabled,
    QPalette.ColorRole.HighlightedText,
    QColor(127, 127, 127)
)


# --------------------------------------------------------------
# Apply the palette to the application
# --------------------------------------------------------------

app = QApplication(sys.argv)
app.setPalette(darkPalette)


# --------------------------------------------------------------
# Create a simple window to demonstrate the theme
# --------------------------------------------------------------

# In a real application, replace this with your own QMainWindow subclass.
window = QMainWindow()
window.setWindowTitle("Dark Palette Test")
window.resize(400, 300)
window.show()


# --------------------------------------------------------------
# Start the Qt event loop
# --------------------------------------------------------------

app.exec()
