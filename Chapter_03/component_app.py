# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 3 — Qt Designer
# Page 188
#
# 3.2 — Example that constructs a UI
#       from two separately compiled Qt Designer files
# component_app.py

# -----------------------------
# Import modules
# -----------------------------
import sys

# Import our two custom components
from componenta import ComponentA
from componentb import ComponentB

# Import the compiled main window UI class
from mainwindow_tabs_ui import Ui_MainWindow

# Import Qt classes
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main application window.

    This class inherits from:
    - QMainWindow: the actual Qt window
    - Ui_MainWindow: the compiled UI from Qt Designer

    The combination allows us to:
    - Create a real QMainWindow
    - Automatically populate it with widgets from the .ui file
    """
    def __init__(self):
        super().__init__()

        # Load all widgets/layouts defined in mainwindow_tabs.ui
        self.setupUi(self)

        # Create instances of our two custom components
        self.component_a = ComponentA()
        self.component_b = ComponentB()

        # Retrieve the central widget created in the .ui file
        widget = self.centralWidget()

        # Retrieve the layout assigned to that central widget
        layout = widget.layout()

        # Add our two components to the layout
        layout.addWidget(self.component_a)  # type: ignore
        layout.addWidget(self.component_b)  # type: ignore


# -----------------------------
# Application entry point
# -----------------------------
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
