"""
Create GUI Applications with Python & Qt6 — Sixth Edition (PySide6)
Coded along by Jose "Joe" Ruiz
Chapter 11 - Example applications
Page 665

11.1 - Mozzarella Ashbadger
    -- Mozzarella Ashbadger is the latest revolution
       in web browsing! Go back and forward! Print!
       Save files! Get help! (you’ll need it).
       Any similarity to other browsers is entirely
       coincidental.

Adding Tabbed Browsing to our browser.py file

browser_tabs.py
"""

# Import modules
import sys

from paths import Paths  # Utility Class we created in Chapter 9.3

from PySide6.QtCore import QSize, Qt, QUrl
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QTabWidget,
    QToolBar,
    QVBoxLayout,
)


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        QBtn = QDialogButtonBox.StandardButton.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Mozzarella Ashbadger")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(Paths.icon("ma-icon-128.png")))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 Mozzarella Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(  # type: ignore
                Qt.AlignmentFlag.AlignHCenter
            )

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(
            self.tab_open_doubleclick
        )
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(
            QIcon(Paths.icon("arrow-180.png")), "Back", self
        )
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(
            lambda: self.tabs.currentWidget().back()                           # type: ignore
        )
        navtb.addAction(back_btn)

        next_btn = QAction(
            QIcon(Paths.icon("arrow-000.png")), "Forward", self
        )
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(
            lambda: self.tabs.currentWidget().forward()                        # type: ignore
        )
        navtb.addAction(next_btn)

        reload_btn = QAction(
            QIcon(Paths.icon("arrow-circle-315.png")), "Reload", self
        )
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(
            lambda: self.tabs.currentWidget().reload()                         # type: ignore
        )
        navtb.addAction(reload_btn)

        home_btn = QAction(
            QIcon(Paths.icon("home.png")), "Home", self
        )
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(
            QPixmap(Paths.icon("lock-nossl.png"))
        )
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(
            QIcon(Paths.icon("cross-circle.png")), "Stop", self
        )
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(
            lambda: self.tabs.currentWidget().stop()                           # type: ignore
        )
        navtb.addAction(stop_btn)

        self.menuBar().setNativeMenuBar(False)
        self.statusBar()

        file_menu = self.menuBar().addMenu("&File")

        new_tab_action = QAction(
            QIcon(Paths.icon("ui-tab--plus.png")), "New Tab", self
        )
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.triggered.connect(
            lambda _: self.add_new_tab()
        )
        file_menu.addAction(new_tab_action)

        open_file_action = QAction(
            QIcon(Paths.icon("disk--arrow.png")),
            "Open file...",
            self,
        )
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(
            QIcon(Paths.icon("disk--pencil.png")),
            "Save Page As...",
            self,
        )
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(
            QIcon(Paths.icon("printer.png")), "Print...", self
        )
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        # Create our system printer instance.
        self.printer = QPrinter()

        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction(
            QIcon(Paths.icon("question.png")),
            "About Mozzarella Ashbadger",
            self,
        )
        about_action.setStatusTip(
            "Find out more about Mozzarella Ashbadger"
        )  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_mozarella_action = QAction(
            QIcon(Paths.icon("lifebuoy.png")),
            "Mozzarella Ashbadger Homepage",
            self,
        )
        navigate_mozarella_action.setStatusTip(
            "Go to Mozzarella Ashbadger Homepage"
        )
        navigate_mozarella_action.triggered.connect(
            self.navigate_mozarella
        )
        help_menu.addAction(navigate_mozarella_action)

        self.add_new_tab(QUrl("http://duckduckgo.com"), "Homepage")

        self.setWindowTitle("Mozzarella Ashbadger")
        self.setWindowIcon(QIcon(Paths.icon("ma-icon-64.png")))


    def add_new_tab(self, qurl=None, label="Blank"):
        if qurl is None:
            qurl = QUrl("")

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's
        # from the correct tab
        browser.urlChanged.connect(
            lambda qurl, browser=browser: self.update_urlbar(
                qurl, browser
            )
        )

        browser.loadFinished.connect(
            lambda _, i=i, browser=browser: self.tabs.setTabText(
                i, browser.page().title()
            )
        )


    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()


    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()                                 # type: ignore
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())


    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)


    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tabs, ignore
            return

        title = self.tabs.currentWidget().page().title()                       # type: ignore
        self.setWindowTitle(f"{title} - Mozzarella Ashbadger")


    def navigate_mozarella(self):
        self.tabs.currentWidget().setUrl(                                      # type: ignore
            QUrl("https://www.pythonguis.com/")
        )


    def about(self):
        dlg = AboutDialog()
        dlg.exec()


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "Hypertext Markup Language (*.htm *.html);;"
            "All files (*.*)",
        )

        if filename:
            with open(filename, "r") as f:
                html = f.read()

            self.tabs.currentWidget().setHtml(html)                            # type: ignore
            self.urlbar.setText(filename)


    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Page As",
            "",
            "Hypertext Markup Language (*.htm *html);;"
            "All files (*.*)",
        )

        if filename:
            # Define callback method to handle the write.
            def writer(html):
                with open(filename, "w") as f:
                    f.write(html)

            self.tabs.currentWidget().page().toHtml(writer)                    # type: ignore


    def print_page(self):
        page = self.tabs.currentWidget().page()                                # type: ignore

        def callback(*args):
            pass

        dlg = QPrintDialog(self.printer)
        dlg.accepted.connect(callback)
        if dlg.exec() == QDialog.Accepted:                                     # type: ignore
            page.print(self.printer, callback)


    def navigate_home(self):
        self.tabs.currentWidget().setUrl(                                      # type: ignore
            QUrl("http://duckduckgo.com")
        )


    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)                                    # type: ignore


    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == "https":
            # Secure padlock icon
            self.httpsicon.setPixmap(
                QPixmap(Paths.icon("lock-ssl.png"))
            )
        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(
                QPixmap(Paths.icon("lock-nossl.png"))
            )

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName("Mozzarella Ashbadger")
app.setOrganizationName("Mozzarella")
app.setOrganizationDomain("mozzarella.org")

window = MainWindow()
window.show()
app.exec()

