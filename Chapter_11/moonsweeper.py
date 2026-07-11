"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 11 - Example applications
Page 670

11.2 - Moonsweeper is a single-player puzzle video game.
       The objective of the game is to explore the area around
       your landed space rocket, without coming too close to the
       deadly B’ug aliens. Your trusty tricounter will tell you the
       number of B’ugs in the vicinity.

MoonSweeper: Dynamic Level Switching and Grid Rebuild Logic

moonsweeper.py
"""

import random
import sys
import time

from paths import Paths  # Utility Class we created in Chapter 9.3

from PySide6.QtCore import QSize, Qt, QTimer, Signal
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QFont,
    QIcon,
    QImage,
    QPainter,
    QPen,
    QPixmap,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

IMG_BOMB  = QImage(Paths.icon("bug.png"))
IMG_FLAG  = QImage(Paths.icon("flag.png"))
IMG_START = QImage(Paths.icon("rocket.png"))
IMG_CLOCK = QImage(Paths.icon("clock-select.png"))

print("Bomb loaded:", IMG_BOMB.isNull())
print("Flag loaded:", IMG_FLAG.isNull())
print("Start loaded:", IMG_START.isNull())
print("Clock loaded:", IMG_CLOCK.isNull())


NUM_COLORS = {
    1: QColor("#F44336"),
    2: QColor("#9C27B0"),
    3: QColor("#3F51B5"),
    4: QColor("#03A9F4"),
    5: QColor("#00BCD4"),
    6: QColor("#4CAF50"),
    7: QColor("#E91E63"),
    8: QColor("#FF9800")
}

STATUS_READY   = 0
STATUS_PLAYING = 1
STATUS_FAILED  = 2
STATUS_SUCCESS = 3

STATUS_ICONS = {
    STATUS_READY:   Paths.icon("plus.png"),
    STATUS_PLAYING: Paths.icon("smiley.png"),
    STATUS_FAILED:  Paths.icon("cross.png"),
    STATUS_SUCCESS: Paths.icon("smiley-lol.png"),
}
LEVELS = [("Easy", 8, 10), ("Medium", 16, 40), ("Hard", 24, 99)]

class Pos(QWidget):
    expandable = Signal(int, int)
    revealed   = Signal(object)
    clicked    = Signal()

    def __init__(self, x, y):
        super().__init__()

        self.setFixedSize(QSize(20, 20))
        self.x = x
        self.y = y
        self.reset()


    def reset(self):
        self.is_start    = False
        self.is_mine     = False
        self.adjacent_n  = 0
        self.is_revealed = False
        self.is_flagged  = False

        self.update()


    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        r = event.rect()

        if self.is_revealed:
            if self.is_start:
                p.drawPixmap(r, QPixmap(IMG_START))

            elif self.is_mine:
                p.drawPixmap(r, QPixmap(IMG_BOMB))

            elif self.adjacent_n > 0:
                pen = QPen(NUM_COLORS[self.adjacent_n])
                p.setPen(pen)
                f = p.font()
                f.setBold(True)
                p.setFont(f)
                p.drawText(
                    r,
                    Qt.AlignmentFlag.AlignHCenter
                    | Qt.AlignmentFlag.AlignVCenter,
                    str(self.adjacent_n),
                )

        else:
            p.fillRect(r, QBrush(Qt.GlobalColor.lightGray))
            pen = QPen(Qt.GlobalColor.gray)
            pen.setWidth(1)
            p.setPen(pen)
            p.drawRect(r)

            if self.is_flagged:
                p.drawPixmap(r, QPixmap(IMG_FLAG))


    def mouseReleaseEvent(self, e):
        if (
            e.button() == Qt.MouseButton.RightButton
            and not self.is_revealed
        ):
            self.toggle_flag()

        elif e.button() == Qt.MouseButton.LeftButton:
            # Block clicking on flagged mines.
            if not self.is_flagged and not self.is_revealed:
                self.click()


    def toggle_flag(self):
        self.is_flagged = not self.is_flagged
        self.update()

        self.clicked.emit()

    def click(self):
        self.reveal()
        if self.adjacent_n == 0:
            self.expandable.emit(self.x, self.y)

        self.clicked.emit()

    def reveal(self, emit=True):
        if not self.is_revealed:
            self.is_revealed = True
            self.update()

            if emit:
                self.revealed.emit(self)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = QWidget()

        hb = QHBoxLayout()
        hb.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self._timer = QTimer()
        self._timer.timeout.connect(self.update_timer)
        self._timer.start(1000)  # 1 second timer

        self.mines = QLabel()
        self.mines.setAlignment(
            Qt.AlignmentFlag.AlignHCenter
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.clock = QLabel()
        self.clock.setAlignment(
            Qt.AlignmentFlag.AlignHCenter
            | Qt.AlignmentFlag.AlignVCenter
        )

        f = self.mines.font()
        f.setPointSize(24)
        f.setWeight(QFont.Weight.Bold)
        self.mines.setFont(f)
        self.clock.setFont(f)

        self.clock.setText("000")

        self.button = QPushButton()
        self.button.setFixedSize(QSize(32, 32))
        self.button.setIconSize(QSize(32, 32))
        self.button.setIcon(QIcon(Paths.icon("smiley.png")))  # changed author's code to use the Utility Class we created in Chapter 9.3
        self.button.setFlat(True)

        self.button.pressed.connect(self.button_pressed)

        self.statusBar()

        bombl = QLabel()
        bombl.setPixmap(QPixmap.fromImage(IMG_BOMB))
        bombl.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignVCenter
        )
        hb.addWidget(bombl)

        hb.addWidget(self.mines)
        hb.addWidget(self.button)
        hb.addWidget(self.clock)

        clockl = QLabel()
        clockl.setPixmap(QPixmap.fromImage(IMG_CLOCK))
        clockl.setAlignment(
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        hb.addWidget(clockl)

        vb = QVBoxLayout()
        vb.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        vb.addLayout(hb)

        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        self.grid.setSizeConstraint(
            QLayout.SizeConstraint.SetFixedSize
        )

        vb.addLayout(self.grid)
        w.setLayout(vb)

        self.setCentralWidget(w)

        self.menuBar().setNativeMenuBar(False)

        game_menu = self.menuBar().addMenu("&Game")

        new_game_action = QAction("New game", self)
        new_game_action.setStatusTip(
            "Start a new game (your current game will be lost)"
        )
        new_game_action.triggered.connect(self.reset_map)
        game_menu.addAction(new_game_action)

        levels = game_menu.addMenu("Levels")
        for n, level in enumerate(LEVELS):
            level_action = QAction(level[0], self)
            level_action.setStatusTip(
                "{1}x{1} grid, with {2} mines".format(*level)
            )
            level_action.triggered.connect(
                lambda checked=None, n=n: self.set_level(n)
            )
            levels.addAction(level_action)

        self.set_level(0)


    def set_level(self, level):
        self.level_name, self.b_size, self.n_mines = LEVELS[level]

        self.setWindowTitle(f"Moonsweeper - {self.level_name}")
        self.mines.setText(f"{self.n_mines:03d}")

        self.clear_map()
        self.init_map()
        self.reset_map()

        # Predefine defaults so VScode doesn't complain
        base_w, base_h = 540, 520

        if level == 0:      # Easy
            base_w, base_h = 540, 520

        elif level == 1:    # Medium
            base_w, base_h = 640, 640

        elif level == 2:    # Hard
            base_w, base_h = 800, 800

        self.resize(base_w, base_h)


    def clear_map(self):
        # Remove all positions from the map, up to maximum size.
        for x in range(0, LEVELS[-1][1]):
            for y in range(0, LEVELS[-1][1]):
                c = self.grid.itemAtPosition(y, x)
                if c:
                    c.widget().close()
                    self.grid.removeItem(c)

        # Force layout to recalculate its geometry
        self.grid.invalidate()


    def init_map(self):
        # Add positions to the map
        for x in range(0, self.b_size):
            for y in range(0, self.b_size):
                w = Pos(x, y)
                self.grid.addWidget(w, y, x)
                # Connect signal to handle expansion.
                w.clicked.connect(self.trigger_start)
                w.revealed.connect(self.on_reveal)
                w.expandable.connect(self.expand_reveal)

        # Place resize on the event queue,
        # giving control back to Qt before resize is performed.
        QTimer.singleShot(0, lambda: self.resize(1, 1))


    def reset_map(self):
        self._reset_position_data()
        self._reset_add_mines()
        self._reset_calculate_adjacency()
        self._reset_add_starting_marker()
        self.update_timer()


    def _reset_position_data(self):
        # Clear all mine positions
        for x in range(0, self.b_size):
            for y in range(0, self.b_size):
                w = self.grid.itemAtPosition(y, x).widget()
                w.reset()


    def _reset_add_mines(self):
        # Add mine positions
        positions = []
        while len(positions) < self.n_mines:
            x, y = (
                random.randint(0, self.b_size - 1),
                random.randint(0, self.b_size - 1),
            )
            if (x, y) not in positions:
                w = self.grid.itemAtPosition(y, x).widget()
                w.is_mine = True
                positions.append((x, y))

        # Calculate end-game condition
        self.end_game_n = (self.b_size * self.b_size) - (
            self.n_mines + 1
        )
        return positions


    def _reset_calculate_adjacency(self):
        def get_adjacency_n(x, y):
            positions = self.get_surrounding(x, y)
            return sum(1 for w in positions if w.is_mine)

        # Add adjacencies to the positions
        for x in range(0, self.b_size):
            for y in range(0, self.b_size):
                w = self.grid.itemAtPosition(y, x).widget()
                w.adjacent_n = get_adjacency_n(x, y)


    def _reset_add_starting_marker(self):
        # Place starting marker.

        # Set initial status (needed for .click to function)
        self.update_status(STATUS_READY)

        while True:
            x, y = (
                random.randint(0, self.b_size - 1),
                random.randint(0, self.b_size - 1),
            )
            w = self.grid.itemAtPosition(y, x).widget()
            # We don't want to start on a mine.
            if not w.is_mine:
                w.is_start = True
                w.is_revealed = True
                w.update()

                # Reveal all positions around this,
                # if they are not mines either.
                for w in self.get_surrounding(x, y):
                    if not w.is_mine:
                        w.click()
                break

        # Reset status to ready following initial clicks.
        self.update_status(STATUS_READY)


    def get_surrounding(self, x, y):
        positions = []

        for xi in range(max(0, x - 1), min(x + 2, self.b_size)):
            for yi in range(max(0, y - 1), min(y + 2, self.b_size)):
                if not (xi == x and yi == y):
                    positions.append(
                        self.grid.itemAtPosition(yi, xi).widget()
                    )

        return positions


    def button_pressed(self):
        if self.status == STATUS_PLAYING:
            self.game_over()

        elif (
            self.status == STATUS_FAILED
            or self.status == STATUS_SUCCESS
        ):
            self.reset_map()


    def reveal_map(self):
        for x in range(0, self.b_size):
            for y in range(0, self.b_size):
                w = self.grid.itemAtPosition(y, x).widget()
                w.reveal(False)


    def expand_reveal(self, x, y):
        """
        Iterate outwards from the initial point, adding new locations
        to the queue. This allows us to expand all in a single go,
        rather than relying on multiple callbacks.
        """
        to_expand = [(x, y)]
        to_reveal = []
        any_added = True

        while any_added:
            any_added = False
            to_expand, locations = [], to_expand

            for x, y in locations:
                positions = self.get_surrounding(x, y)
                for w in positions:
                    if not w.is_mine and w not in to_reveal:
                        to_reveal.append(w)
                        if w.adjacent_n == 0:
                            to_expand.append((w.x, w.y))
                            any_added = True

        # Iterate an reveal all the positions we have found.
        for w in to_reveal:
            w.reveal()


    def trigger_start(self, *args):
        if self.status == STATUS_READY:
            # First click.
            self.update_status(STATUS_PLAYING)
            # Start timer.
            self._timer_start_nsecs = int(time.time())


    def update_status(self, status):
        self.status = status
        self.button.setIcon(QIcon(STATUS_ICONS[self.status]))

        if status == STATUS_READY:
            self.statusBar().showMessage("Ready")


    def update_timer(self):
        if self.status == STATUS_PLAYING:
            # Prevent crash if timer fires before start time is set
            if not hasattr(self, "_timer_start_nsecs"):
                return

            n_secs = int(time.time()) - self._timer_start_nsecs
            self.clock.setText(f"{n_secs:03d}")

        elif self.status == STATUS_READY:
            self.clock.setText("000")


    def on_reveal(self, w):
        if w.is_mine:
            self.game_over()

        else:
            self.end_game_n -= 1  # decrement remaining empty spaces

            if self.end_game_n == 0:
                self.game_won()


    def game_over(self):
        self.reveal_map()
        self.update_status(STATUS_FAILED)


    def game_won(self):
        self.reveal_map()
        self.update_status(STATUS_SUCCESS)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()













