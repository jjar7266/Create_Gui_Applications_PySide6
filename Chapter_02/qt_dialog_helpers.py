# qt_dialog_helpers.py
# Utility helpers for forcing Qt-style dialogs on Windows
# so titles, window frames, and sizing behave consistently.

# When to use this helper:
# - If Windows hides the title bar on QMessageBox
# - If the dialog looks native instead of Qt-style
# - If you want consistent behavior across OSes
# - If you want dialogs to match the book's screenshots

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox


def create_qt_messagebox(parent, icon, title, text, buttons):
    """
    Create a QMessageBox that ALWAYS uses Qt's own dialog engine,
    not the Windows native dialog. This ensures:

      - Title bar always visible
      - Window frame always visible
      - Dialog can be resized
      - Minimum width/height actually work
      - Layout matches the book's screenshots

    This solves the Windows 11 issue where native dialogs:
      - ignore sizing
      - clip long titles
      - use fixed-width layouts
    """

    # Use the full QMessageBox constructor
    dlg = QMessageBox(icon, title, text, buttons, parent)

    # Force Qt to draw the ENTIRE dialog (not Windows)
    dlg.setWindowFlags(
        Qt.WindowType.Dialog |
        Qt.WindowType.WindowTitleHint |
        Qt.WindowType.CustomizeWindowHint |
        Qt.WindowType.Window
    )

    # Provide a reasonable default width so titles don't clip
    dlg.setMinimumWidth(350)

    return dlg
