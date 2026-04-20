# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 155
#
# 2.7 Windows — Persistent windows

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

    This example demonstrates a *persistent* window: it is created once
    and then shown repeatedly without being recreated.
    """
    def __init__(self):
        super().__init__()

        # Layout to stack widgets vertically.
        layout = QVBoxLayout()

        # Give each window a random ID so you can see that it is created only once.
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

    This version creates the secondary window *once* during initialization.
    Pressing the button simply calls .show() on the same window instance.
    """
    def __init__(self):
        super().__init__()

        # Create the secondary window immediately.
        # This makes it persistent — it exists for the lifetime of MainWindow.
        self.w = AnotherWindow()

        # Button that will show the persistent window.
        self.button = QPushButton("Push for Window")

        # Connect the button's clicked signal to our handler.
        self.button.clicked.connect(self.show_new_window)

        # Make the button the central widget of the main window.
        self.setCentralWidget(self.button)

    def show_new_window(self, is_checked):
        """
        Slot called when the button is clicked.

        Since the window already exists, we simply call .show() on it.
        If the user closes the window manually, .show() will reopen it.
        """
        self.w.show()


# Standard Qt application setup.
app = QApplication(sys.argv)

# Create and show the main window.
window = MainWindow()
window.show()

# Start the Qt event loop.
app.exec()
