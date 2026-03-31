# Create GUI Applications with
#   Python & Qt6
#     Sixth Edition | PySide6
#       Author: Martin Fitzpatrick

# coded along by Joe Ruiz
# Chapter 2 - Basic PySide6 Features

# 2.3. Widgets - QDial: page 53
"""
QDial is a rotatable widget that functions just like the slider, but appears
as an analogue dial. This looks nice, but from a UI perspective is not
particularly user friendly. However, they are often used in audio applications
as representation of real-world analogue dials.
"""

# Import modules
import sys
from PySide6.QtWidgets import (
    QApplication,
    QDial,
    QMainWindow
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)


    def slider_position(self, p):
        print("position", p)


    def slider_pressed(self):
        print("Pressed")


    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



