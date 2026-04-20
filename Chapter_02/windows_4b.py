# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 154
#
# 2.7 Windows — close window, explicitly call .close()

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
    A simple standalone top-level window.

    This window displays a random ID so you can see when a new instance
    is created. It is shown and closed explicitly by the main window.
    """
    def __init__(self):
        super().__init__()

        # Layout to stack widgets vertically.
        layout = QVBoxLayout()

        # Generate a random ID so each window instance is visibly unique.
        window_id = randint(0, 100)

        # Label showing the ID.
        self.label = QLabel(f"Another Window {window_id}")

        # Add the label to the layout.
        layout.addWidget(self.label)

        # Apply the layout to this window.
        self.setLayout(layout)


class MainWindow(QMainWindow):
    """
    The main application window.

    Contains a button that toggles the creation and explicit closing
    of a secondary window.
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

        This version demonstrates explicitly closing a window using .close(),
        instead of relying on Python reference deletion alone.
        """

        # If no window exists yet, create and show one.
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()

        else:
            # Explicitly close the window.
            # This immediately hides and destroys the window.
            self.w.close()

            # Drop the reference so the next click creates a new window.
            self.w = None


# Standard Qt application setup.
app = QApplication(sys.argv)

# Create and show the main window.
window = MainWindow()
window.show()

# Start the Qt event loop.
app.exec()
