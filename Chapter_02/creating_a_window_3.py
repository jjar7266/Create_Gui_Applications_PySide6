# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features

# 2.1. - My first Application

# Import modules

# Only needed for accss to command line arguments
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguements for your app.
# If you know you won't use command line arguements you can use
# QApplication([]) instead.
app = QApplication(sys.argv)

window = QMainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.





