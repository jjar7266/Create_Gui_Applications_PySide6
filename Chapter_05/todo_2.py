"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 302

5.4 - Todo List Model - (Step 2: Add items to the Model)

todo_2.py
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

    def data(self, index, role):  # type: ignore
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):  # type: ignore
        return len(self.todos)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.todoView.setModel(self.model)
        # Connect the button.
        self.addButton.pressed.connect(self.add)

    def add(self):
        """
        Add an item to our todo list, getting the text from the
        QLineEdit .todoEdit and then clearing it.
        """
        text = self.todoEdit.text()
        # Remove whitespace from the ends of the string.
        text = text.strip()
        if text:  # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()  # <1>
            # Empty the input
            self.todoEdit.setText("")




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
