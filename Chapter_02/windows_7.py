# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 2 — Basic PySide6 Features
# Page 158
#
# 2.7 Windows — Connect a text input on the main window
# to a QLabel on a sub-window.

# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    A simple secondary window that displays a QLabel.

    This window is created once and reused. Because it has no parent,
    it appears as a floating top-level window.
    """

    def __init__(self):
        super().__init__()

        # Layout to stack widgets vertically.
        layout = QVBoxLayout()

        # Label that will receive text updates from the main window.
        self.label = QLabel("Another Window")

        # Add the label to the layout.
        layout.addWidget(self.label)

        # Apply the layout to this window.
        self.setLayout(layout)


class MainWindow(QMainWindow):
    """
    The main application window.

    This example demonstrates:
    - Creating a persistent secondary window
    - Toggling its visibility
    - Connecting a QLineEdit's textChanged signal to a QLabel on the sub-window
    """

    def __init__(self):
        super().__init__()

        # Create the secondary window ONCE (persistent window)
        self.w = AnotherWindow()

        # Button that toggles the visibility of the secondary window
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)

        # Text input field
        self.input = QLineEdit()

        # Connect the textChanged signal directly to the label's setText slot
        # This means: whenever the user types, the sub-window label updates instantly.
        self.input.textChanged.connect(self.w.label.setText)

        # Layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.input)

        # Container widget to hold the layout
        container = QWidget()
        container.setLayout(layout)

        # Set the container as the central widget
        self.setCentralWidget(container)

    def toggle_window(self, is_checked):
        """
        Show or hide the secondary window depending on its current visibility.
        """

        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


# Standard Qt application setup
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


# =============================================================================
# Teaching Notes — Connecting Widgets Across Windows (Page 158)
# =============================================================================
#
# 📝 Concept Overview
# This example introduces a powerful Qt concept:
#     Connecting a widget in one window to a widget in another window.
#
# The main window contains a QLineEdit. As the user types, the text is sent
# directly to a QLabel inside a separate floating window.
#
# This demonstrates Qt’s signal/slot system working *across window boundaries*.
#
# -----------------------------------------------------------------------------
# 🎯 Learning Objectives
# - Understand how to connect signals between different windows.
# - Learn how to update UI elements in a sub-window from the main window.
# - Reinforce the idea of persistent windows created once and reused.
# - See how Qt’s signal/slot system allows clean, decoupled communication.
#
# -----------------------------------------------------------------------------
# 📌 Key Ideas
#
# 1. Persistent Window Instance
#    The secondary window is created once:
#        self.w = AnotherWindow()
#    This allows us to safely connect signals to its widgets.
#
# 2. Direct Signal-to-Slot Connection
#    The magic line:
#        self.input.textChanged.connect(self.w.label.setText)
#    This means:
#    - Every time the text changes in QLineEdit,
#    - Qt automatically calls QLabel.setText(new_text)
#    - No intermediate function needed.
#
# 3. Toggling Window Visibility
#    Same pattern as the previous example:
#        if self.w.isVisible(): hide()
#        else: show()
#
# 4. Decoupled Communication
#    The main window does NOT need to know how the sub-window works internally.
#    It simply calls a public slot: label.setText.
#
# -----------------------------------------------------------------------------
# ⚠️ Common Mistakes
# - Recreating the sub-window each time (breaks the signal connection).
# - Forgetting to store the window in self.w (window gets garbage-collected).
# - Trying to update the label before the window exists.
#
# -----------------------------------------------------------------------------
# 💡 Takeaways
# - Qt’s signal/slot system works seamlessly across multiple windows.
# - You can directly connect signals to widget methods (slots).
# - Persistent windows make cross-window communication easy.
# - This pattern is foundational for multi-window applications with shared data.
#
# =============================================================================
