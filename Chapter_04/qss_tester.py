"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Joe Ruiz
Chapter 4 — Theming
Page 218

4.4 — Qt Style Sheets (QSS) — Style Editor
Example: qss_tester.py

This version is cleaned, structured, and fully commented for teaching clarity.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """
    A simple QSS testing tool.

    The user types QSS into the editor, and the entire window updates live.
    This is extremely useful for experimenting with Qt Style Sheets.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSS Tester")

        # ---------------------------------------------------------
        # QSS Editor
        # ---------------------------------------------------------
        # QPlainTextEdit is ideal for code-like text.
        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText("Type QSS here…")
        self.editor.textChanged.connect(self.update_styles)

        # ---------------------------------------------------------
        # Demo widgets to style
        # ---------------------------------------------------------
        layout = QVBoxLayout()
        layout.addWidget(self.editor)

        # Checkbox
        checkbox = QCheckBox("Checkbox")
        layout.addWidget(checkbox)

        # ComboBox with objectName for targeted styling
        combo = QComboBox()
        combo.setObjectName("thecombo")
        combo.addItems(["First", "Second", "Third", "Fourth"])
        layout.addWidget(combo)

        # SpinBox
        spinbox = QSpinBox()
        spinbox.setRange(0, 99999)
        layout.addWidget(spinbox)

        # Label
        label = QLabel("This is a label")
        layout.addWidget(label)

        # LineEdit with objectName for targeted styling
        lineedit = QLineEdit()
        lineedit.setObjectName("mylineedit")
        layout.addWidget(lineedit)

        # PushButton
        button = QPushButton("Push me!")
        layout.addWidget(button)

        # ---------------------------------------------------------
        # Central widget setup
        # ---------------------------------------------------------
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # -------------------------------------------------------------
    # Live QSS updater
    # -------------------------------------------------------------
    def update_styles(self):
        """
        Called whenever the text in the editor changes.
        Applies the QSS to the entire window.
        """
        qss = self.editor.toPlainText()
        self.setStyleSheet(qss)


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Optional: consistent cross‑platform theme

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
