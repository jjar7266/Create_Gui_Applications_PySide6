# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#
# Coded along by Joe Ruiz
# Chapter 3 — Qt Designer
# Page 189
#
# 3.2 — Component A widget
# componenta.py

# -----------------------------
# Import modules
# -----------------------------
from componenta_ui import Ui_ComponentA
from PySide6.QtWidgets import QWidget


class ComponentA(QWidget, Ui_ComponentA):
    """
    ComponentA is a custom widget built from a Qt Designer .ui file.

    It inherits from:
    - QWidget: the base class for all UI components
    - Ui_ComponentA: the compiled UI class generated from componenta.ui

    This pattern allows us to:
    - Create a real QWidget
    - Automatically populate it with all widgets defined in the .ui file
    """
    def __init__(self):
        super().__init__()

        # Load all widgets/layouts defined in componenta.ui
        self.setupUi(self)

        # Connect the QLineEdit's textChanged signal to our handler method
        self.lineEdit.textChanged.connect(self.handle_lineedit_changed)

    def handle_lineedit_changed(self, text: str):
        """
        Slot method called whenever the user types into the QLineEdit.

        Parameters:
            text (str): The current text inside the lineEdit widget.
        """
        print(text)
