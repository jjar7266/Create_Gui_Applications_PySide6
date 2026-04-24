# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 4 — Theming
# Page 217
#
# 4.2 — Palettes
# linux.py
#
# This example demonstrates how to load a system theme icon using
# QIcon.fromTheme(). This is commonly used on Linux desktop environments
# (GNOME, KDE, XFCE) where applications share a global icon theme.
#
# IMPORTANT:
# - On Linux, if the icon name exists in the system theme, it will load.
# - On Windows and macOS, theme icons usually DO NOT exist, so the icon
#   will appear blank unless a fallback is provided.

# --------------------------------------------------------------
# Import modules
# --------------------------------------------------------------

import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QPushButton


# --------------------------------------------------------------
# Application setup
# --------------------------------------------------------------

app = QApplication(sys.argv)

# Create a simple button
button = QPushButton("Hello")

# --------------------------------------------------------------
# Load a theme icon
#
# QIcon.fromTheme("document-new") attempts to load an icon named
# "document-new" from the system's active icon theme.
#
# This works on Linux desktops that support icon themes.
#
# On Windows/macOS:
#   - The icon will likely NOT appear.
#   - Qt does not ship with theme icons on these platforms.
#
# This example is included to demonstrate cross-platform differences
# in theming behavior.
# --------------------------------------------------------------

icon = QIcon.fromTheme("document-new")
button.setIcon(icon)

# Show the button
button.show()


# --------------------------------------------------------------
# Start the Qt event loop
# --------------------------------------------------------------

app.exec()
