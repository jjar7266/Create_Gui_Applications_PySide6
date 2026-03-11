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

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

# single pushable button
window = QPushButton("Push Me")

window.show()

app.exec()







