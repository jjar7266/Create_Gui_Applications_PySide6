"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 11 - Example applications
Page 655

11.1 - Mozzarella Ashbadger
    -- Mozzarella Ashbadger is the latest revolution
       in web browsing! Go back and forward! Print!
       Save files! Get help! (you’ll need it).
       Any similarity to other browsers is entirely
       coincidental.

The browser widget - QWebEngineView - This provides a complete browser
  window, which handles the rendering of the downloaded pages. Below is
  the bare-minimum of code required to use

browser_skeleton.py
"""

# Import modules
import sys

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.setCentralWidget(self.browser)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
