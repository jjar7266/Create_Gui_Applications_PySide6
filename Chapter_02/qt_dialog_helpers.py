# qt_dialog_helpers.py
# Utility helpers for forcing Qt-style dialogs on Windows
# so titles and window frames always appear.

# When to use this helper:
# - If Windows hides the title bar on QMessageBox
# - If the dialog looks native instead of Qt-style
# - If you want consistent behavior across OSes
# - If you want dialogs to match the book's screenshots


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox


def create_qt_messagebox(parent, icon, title, text, buttons):
    """
    Creates a QMessageBox that ALWAYS shows:
      - a title bar
      - a window frame
      - Qt's own dialog style (not Windows native)

    Use this when Windows hides the title bar.
    """
    dlg = QMessageBox(icon, title, text, buttons, parent)

    # Force Qt window decorations
    dlg.setWindowFlags(
        dlg.windowFlags()
        | Qt.WindowType.WindowTitleHint
        | Qt.WindowType.CustomizeWindowHint
        | Qt.WindowType.Window
    )

    return dlg
