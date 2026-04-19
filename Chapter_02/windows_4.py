# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 154
#
# 2.7 Windows — Closing a window

import sys
from random import randint

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    A simple standalone window that can be opened from the main window.

    This class represents a top-level QWidget. When shown, it appears as its
    own independent window (not embedded inside the main window).
    """
    def __init__(self):
        super().__init__()

        # Layout to stack widgets vertically.
        layout = QVBoxLayout()

        # Give each window a random ID so you can see when a new one is created.
        window_id = randint(0, 100)

        # Display the ID in a label.
        self.label = QLabel(f"Another Window {window_id}")

        # Add the label to the layout.
        layout.addWidget(self.label)

        # Apply the layout to this window.
        self.setLayout(layout)


class MainWindow(QMainWindow):
    """
    The main application window.

    Contains a button that toggles the creation and closing of a secondary window.
    """
    def __init__(self):
        super().__init__()

        # Holds a reference to the secondary window.
        # Starts as None because no window exists yet.
        self.w = None

        # Button that will open (or close) the secondary window.
        self.button = QPushButton("Push for Window")

        # Connect the button's clicked signal to our handler.
        self.button.clicked.connect(self.show_new_window)

        # Make the button the central widget of the main window.
        self.setCentralWidget(self.button)

    def show_new_window(self, is_checked):
        """
        Slot called when the button is clicked.

        This example demonstrates how closing a window works in Qt:
        - If no window exists, create one and show it.
        - If a window already exists, drop the reference so Qt closes it.
        """

        # If no window exists yet, create and show one.
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()

        else:
            # Dropping the reference allows Qt to close the window.
            # After this, clicking the button again will create a new window.
            self.w = None


# Standard Qt application setup.
app = QApplication(sys.argv)

# Create and show the main window.
window = MainWindow()
window.show()

# Start the Qt event loop.
app.exec()
