# made by ionut b
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainterPath, QRegion
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QSizeGrip, QGridLayout, QVBoxLayout, QStatusBar, QHBoxLayout, QAction, QLineEdit, QTabWidget
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os


class SideGrip(QtWidgets.QWidget):
    def __init__(self, parent, edge):
        QtWidgets.QWidget.__init__(self, parent)
        if edge == QtCore.Qt.LeftEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeLeft
        elif edge == QtCore.Qt.TopEdge:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeTop
        elif edge == QtCore.Qt.RightEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeRight
        else:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeBottom
        self.mousePos = None

    def resizeLeft(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunc(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None


class Main(QtWidgets.QMainWindow):
    _gripSize = 8

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.sideGrips = [
            SideGrip(self, QtCore.Qt.LeftEdge),
            SideGrip(self, QtCore.Qt.TopEdge),
            SideGrip(self, QtCore.Qt.RightEdge),
            SideGrip(self, QtCore.Qt.BottomEdge),
        ]
        # corner grips should be "on top" of everything, otherwise the side grips
        # will take precedence on mouse events, so we are adding them *after*;
        # alternatively, widget.raise_() can be used
        self.cornerGrips = [QtWidgets.QSizeGrip(self) for i in range(4)]
        self.resize(1600, 900)
        self.mainframe = QFrame(self)
        self.mainframe.setStyleSheet(
            """
            QFrame{background-color:rgba(r, g, b, alpha);
            border: 1px solid #BBBBBB;
            border-radius: 24px;
            opacity: 0.6;
                }""")
        self.setCentralWidget(self.mainframe)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        # main_frame
        frame = QtWidgets.QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        
        frame.setStyleSheet("""
            QFrame{border: 1px solid #BBBBBB;
            border-radius: 16px;     
            background: #1B1D1E;
                }""")
        self.setCentralWidget(frame)
    # Grid main
        grid_1 = QGridLayout()
        grid_1.setSpacing(2)
        frame.setLayout(grid_1)
        # window_1
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        grid_1.addWidget(self.browser, 0, 1, 3, 3)
        self.browser.setStyleSheet("""
            border: 1px solid #BBBBBB;
            border-radius: 16em;     
            background: #1B1D34;
                """)
        # widgets_area
   # Grid second
        grid_2 = QVBoxLayout()
        grid_1.addLayout(grid_2, 0, 0, 1, 1)
        grid_2.setContentsMargins(0, 0, 0, 0)
        grid_2.setSpacing(10)
    # Grid 3
        grid_3 = QHBoxLayout()

        back_btn = QPushButton("<", self)
      #  back_btn.triggered.connect(self.browser.back)
        back_btn.setStyleSheet("""color:white;
                               height:1em;
                               font-size:20px;
                               background-color:gray;
                                margin:1em;width:1em; border-radius: 0.5em;""")
        forward_btn = QPushButton(">", self)
        forward_btn.setStyleSheet("""color:white;
                               height:1em;
                                font-size:20px;
                                background-color:gray;
                                margin:1em;width:1em; border-radius: 0.5em;""")
        reload_btn = QPushButton("o", self)
        reload_btn.setStyleSheet("""color:white; height:1em;
                                font-size:20px;
                                background-color:gray;
                                margin:1em;width:1em; border-radius: 0.5em;""")
        self.searchBar = QLineEdit()
        self.searchBar.setStyleSheet(
            """
                height:2em;
                width:3em;
                border-radius: 1em;
                """
        )
        self.searchBar.setFixedWidth(250)
        self.searchBar.returnPressed.connect(self.loadUrl)
        grid_2.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)
        grid_2.addLayout(grid_3)
        self.tabs = QTabWidget()
        self.tabs.TabShape(1)
        self.tabs.setFixedWidth(250)
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        grid_2.addWidget(self.tabs)
        grid_3.addWidget(back_btn)
        grid_3.addWidget(reload_btn)
        grid_3.addWidget(forward_btn)

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    def add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = QUrl('')

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

    def add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = QUrl('')

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))
        # method to load the required url

    def loadUrl(self):
        # fetching entered url from searchBar
        url = self.searchBar.text()
        # loading url
        self.browser.setUrl(QUrl(url))

    def update_urlbar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(
                QPixmap(os.path.join('icons', 'lock-ssl.png')))

        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(
                QPixmap(os.path.join('icons', 'lock-nossl.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
    # method to update the url

    def updateUrl(self, url):
        # changing the content(text) of searchBar
        self.searchBar.setText(url.toString())

    def resizeEvent(self, event):
        QtWidgets.QMainWindow.resizeEvent(self, event)
        self.updateGrips()

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def mouseDoubleClickEvent(self, event):
        state = int(self.windowState())
        if state == 0:
            self.showMaximized()
        else:
            self.showNormal()

    @property
    def gripSize(self):
        return self._gripSize

    def setGripSize(self, size):
        if size == self._gripSize:
            return
        self._gripSize = max(2, size)
        self.updateGrips()

    def updateGrips(self):
        self.setContentsMargins(*[self.gripSize] * 4)

        outRect = self.rect()
        # an "inner" rect used for reference to set the geometries of size grips
        inRect = outRect.adjusted(self.gripSize, self.gripSize,
                                  -self.gripSize, -self.gripSize)

        # top left
        self.cornerGrips[0].setGeometry(
            QtCore.QRect(outRect.topLeft(), inRect.topLeft()))
        self.cornerGrips[0].setStyleSheet("""
                background-color: transparent; 
        """)
        # top right
        self.cornerGrips[1].setGeometry(
            QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())
        self.cornerGrips[1].setStyleSheet("""
                background-color: transparent; 
        """)
        # bottom right
        self.cornerGrips[2].setGeometry(
            QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))
        self.cornerGrips[2].setStyleSheet("""
                background-color: transparent; 
        """)
        # bottom left
        self.cornerGrips[3].setGeometry(
            QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())
        self.cornerGrips[3].setStyleSheet("""
                background-color: transparent; 
        """)
        # left edge
        self.sideGrips[0].setGeometry(
            0, inRect.top(), self.gripSize, inRect.height())
        self.sideGrips[3].setStyleSheet("""
                background-color: transparent; 
        """)
        # top edge
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self.gripSize)
        self.sideGrips[1].setStyleSheet("""
                background-color: transparent; 
        """)
        # right edge
        self.sideGrips[2].setGeometry(
            inRect.left() + inRect.width(),
            inRect.top(), self.gripSize, inRect.height())
        # bottom edge
        self.sideGrips[3].setGeometry(
            self.gripSize, inRect.top() + inRect.height(),
            inRect.width(), self.gripSize)


app = QtWidgets.QApplication([])
m = Main()
m.show()
app.exec_()
