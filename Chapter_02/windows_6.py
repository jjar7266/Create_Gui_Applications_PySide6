# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 156
#
# 2.7 Windows — The complete working example of this persistent window
# and toggling the show/hide state is shown below

# Import modules
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
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        window_id = randint(0, 100)
        self.label = QLabel(f"Another Window {window_id}")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the secondary window ONCE (persistent window)
        self.w = AnotherWindow()

        # Button that toggles the window's visibility
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)

        self.setCentralWidget(self.button)

    def toggle_window(self, is_checked):
        # If the window is visible → hide it
        if self.w.isVisible():
            self.w.hide()

        # If the window is hidden → show it
        else:
            self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


# =============================================================================
# Teaching Notes — Persistent Window with Show/Hide Toggle (Page 156)
# =============================================================================
#
# 📝 Concept Overview
# This example demonstrates how to create a *persistent* secondary window and
# toggle its visibility using .show() and .hide(). Unlike earlier examples that
# created a new window each time, this pattern creates the window once and
# reuses it for the entire lifetime of the application.
#
# 🎯 Learning Objectives
# - Understand how to create a long-lived window instance.
# - Learn how to toggle visibility using isVisible(), show(), and hide().
# - See how Qt keeps a window alive as long as Python holds a reference to it.
# - Observe that the window’s internal state (like the random ID) persists.
#
# 📌 Key Ideas
# 1. Persistent Window Instance:
#       self.w = AnotherWindow()
#    This creates the window once in __init__. It stays alive until MainWindow
#    is destroyed.
#
# 2. Toggling Visibility:
#       if self.w.isVisible(): self.w.hide()
#       else: self.w.show()
#    This avoids destroying the window and preserves its state.
#
# 3. Random ID Demonstrates Persistence:
#    The ID stays the same every time you show/hide the window, proving that
#    the same window instance is reused.
#
# 4. Real-World Use Cases:
#    - Settings windows
#    - Tool panels
#    - Debug consoles
#    - Inspector windows
#
# ⚠️ Common Mistakes
# - Recreating the window each time instead of reusing it.
# - Using .close() instead of .hide() for persistent windows.
# - Forgetting to check visibility before toggling.
#
# 💡 Takeaways
# - Persistent windows are created once and reused.
# - .show() and .hide() control visibility without destroying the window.
# - isVisible() is the cleanest way to check window state.
# - This pattern is foundational for multi-window Qt applications.
# =============================================================================
