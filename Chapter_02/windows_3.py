# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 152
#
# 2.7 Windows — Creating additional windows in PySide6

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

    This class inherits from QWidget, meaning it is a top-level window
    (not a dialog, not embedded in another widget).
    """
    def __init__(self):
        super().__init__()

        # Create a vertical layout to stack widgets top-to-bottom.
        layout = QVBoxLayout()

        # Generate a random ID so each new window looks unique.
        window_id = randint(0, 100)

        # Create a label showing the window ID.
        self.label = QLabel(f"Another Window {window_id}")

        # Add the label to the layout.
        layout.addWidget(self.label)

        # Apply the layout to this window.
        self.setLayout(layout)


class MainWindow(QMainWindow):
    """
    The main application window.

    Contains a single button that, when pressed, opens a new window.
    """
    def __init__(self):
        super().__init__()

        # Placeholder for the secondary window.
        # Starts as None because no window has been created yet.
        self.w = None

        # Create a button that will open the new window.
        self.button = QPushButton("Push for Window")

        # Connect the button's clicked signal to our handler method.
        self.button.clicked.connect(self.show_new_window)

        # Make the button the central widget of the main window.
        self.setCentralWidget(self.button)

    def show_new_window(self, is_checked):
        """
        Slot called when the button is clicked.

        Creates and shows AnotherWindow, but only once.
        """
        # Only create the window if it doesn't already exist.
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
            # Note: If the window is closed manually, `self.w` still holds
            # the old reference. The book covers this behavior later.
            # For now, this ensures only one window appears.


# Standard Qt application setup.
app = QApplication(sys.argv)

# Create and show the main window.
window = MainWindow()
window.show()

# Start the Qt event loop.
app.exec()
