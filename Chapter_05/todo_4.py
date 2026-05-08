"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 5 - Model View Controller
Page 304

5.4 - Todo List Model -

todo_4.py
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
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

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
            self.model.layoutChanged.emit()
            # Empty the input
            self.todoEdit.setText("")

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a single-item list in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and botton right, which
            # are equal for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

