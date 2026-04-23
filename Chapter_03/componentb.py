# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 3 — Qt Designer
# Page 189
#
# 3.2 — Component B widget
# componentb.py

# -----------------------------
# Import modules
# -----------------------------
from componentb_ui import Ui_ComponentB
from PySide6.QtWidgets import QWidget


class ComponentB(QWidget, Ui_ComponentB):
    """
    ComponentB is a custom widget built from a Qt Designer .ui file.

    It inherits from:
    - QWidget: the base class for all UI components
    - Ui_ComponentB: the compiled UI class generated from componentb.ui

    This pattern allows us to:
    - Create a real QWidget
    - Automatically populate it with all widgets defined in the .ui file
    """
    def __init__(self):
        super().__init__()

        # Load all widgets/layouts defined in componentb.ui
        self.setupUi(self)

        # Connect the QDial's valueChanged signal to our handler method
        self.dial.valueChanged.connect(self.handle_dial_changed)

    def handle_dial_changed(self, value: int):
        """
        Slot method called whenever the user rotates the QDial.

        Parameters:
            value (int): The current numeric value of the dial.
        """
        print(value)
