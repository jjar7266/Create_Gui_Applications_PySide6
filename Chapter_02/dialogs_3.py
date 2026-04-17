# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features
# page 116

# 2.6 Dialogs - Message dialogs with QMessageBox
# ---------------------------------------------------------
# This version uses a helper function (create_qt_messagebox)
# to force Qt-style dialogs on Windows. This ensures:
#   - The dialog ALWAYS shows a title bar
#   - The dialog ALWAYS has a window frame
#   - The dialog matches the book's screenshot
# ---------------------------------------------------------

import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
)

# Import the helper that forces Qt-style dialog behavior.
# This helper lives in qt_dialog_helpers.py and wraps the
# QMessageBox constructor + window flag overrides.
from qt_dialog_helpers import create_qt_messagebox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window title
        self.setWindowTitle("My App")

        # -----------------------------------------------------
        # Create a QPushButton that will trigger the dialog.
        # When clicked, it calls self.button_clicked().
        # -----------------------------------------------------
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)

        # Make the button the central widget of the window
        self.setCentralWidget(button)

    def button_clicked(self, is_checked):
        """
        This method is called whenever the button is clicked.
        It creates and displays a QMessageBox using our helper.
        """

        # ---------------------------------------------------------
        # Create a QMessageBox using the helper function.
        #
        # Why use the helper?
        #   - On Windows 11, QMessageBox may use the *native*
        #     Windows dialog, which hides the title bar.
        #
        #   - The helper forces Qt to draw the dialog itself,
        #     guaranteeing the title bar appears.
        #
        # Parameters:
        #   parent  -> self (MainWindow)
        #   icon    -> Question mark icon
        #   title   -> Window title (book example)
        #   text    -> Main message text
        #   buttons -> OK button only
        # ---------------------------------------------------------
        dlg = create_qt_messagebox(
            parent=self,
            icon=QMessageBox.Icon.Question,
            title="I have a question!",
            text="This is a simple dialog",
            buttons=QMessageBox.StandardButton.Ok,
        )

        # ---------------------------------------------------------
        # Execute the dialog.
        # exec() blocks until the user clicks a button.
        #
        # The return value is the button pressed.
        # ---------------------------------------------------------
        button = dlg.exec()

        # ---------------------------------------------------------
        # Check which button the user pressed.
        # In this example, only OK exists.
        # ---------------------------------------------------------
        if button == QMessageBox.StandardButton.Ok:
            print("OK!")


# -------------------------------------------------------------
# Standard Qt application bootstrap.
# Creates the QApplication, the MainWindow, and starts the loop.
# -------------------------------------------------------------
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
