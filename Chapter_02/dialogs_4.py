# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick
#
# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features
# page 118
#
# 2.6 Dialogs - question dialog with Yes and No buttons
#
# NOTE FOR WINDOWS USERS:
# -----------------------
# QMessageBox on Windows 11 uses the *native Windows dialog*.
# This means:
#   - The dialog will be smaller than the book's screenshot.
#   - The title bar text may appear clipped.
#   - resize(), setMinimumWidth(), etc. have NO effect.
#
# This is normal behavior on Windows and not a bug in your code.


# Import modules
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window title
        self.setWindowTitle("My App")

        # Create a button that will trigger the question dialog
        button = QPushButton("Press me for a question dialog!")
        button.clicked.connect(self.button_clicked)

        # Make the button the central widget of the window
        self.setCentralWidget(button)

    def button_clicked(self, is_checked):
        """
        Create a Yes/No question dialog using QMessageBox.
        This version matches the book exactly and does NOT
        use any helper overrides.
        """

        # Create the QMessageBox instance
        dlg = QMessageBox(self)

        # Set the dialog title
        dlg.setWindowTitle("I have a question!")

        # Set the main text of the dialog
        dlg.setText("This is a question dialog")

        # Add Yes and No buttons
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )

        # Set the question mark icon
        dlg.setIcon(QMessageBox.Icon.Question)

        # Execute the dialog and capture the button pressed
        button = dlg.exec()

        # Check which button the user clicked
        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")


# Standard Qt application bootstrap
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
