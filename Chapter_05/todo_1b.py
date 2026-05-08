"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 300

5.4 - Todo List Model - Basic implementation

The code below shows the basic model we’ve created in the application
skeleton, which has the code necessary to take the model and display it
 — although it is empty! We’ll add our model code and application logic
to this base.

todo_1b.py
"""

# Import modules
import sys

from mainwindow_ui import Ui_MainWindow

from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow


class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):     # type: ignore
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):       # type: ignore
        return len(self.todos)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel(todos=[(False, 'my first todo')])
        self.todoView.setModel(self.model)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()





