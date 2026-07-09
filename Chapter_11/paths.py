"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 9 - Further PySide6 Features
Page 577

9.3 - Working with Relative Paths

Paths Utility Class for Relative Resource Loading

paths.py
"""

# Import modules
from pathlib import Path


class Paths:
    base = Path(__file__).parent
    ui_files = base / "ui"
    images   = base / "images"
    icons    = images / "icons"
    data     = base / "data"

    # File loaders.
    @classmethod
    def ui_file(cls, filename):
        return (cls.ui_files / filename).as_posix()

    @classmethod
    def icon(cls, filename):
        return (cls.icons / filename).as_posix()

    @classmethod
    def image(cls, filename):
        return (cls.images / filename).as_posix()

    @classmethod
    def datafile(cls, filename):
        return (cls.data / filename).as_posix()
