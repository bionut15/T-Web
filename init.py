#made by ionut b
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainterPath, QRegion
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QSizeGrip, QGridLayout 

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
       # self.setAttribute(Qt.WA_TranslucentBackground)
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
       # self.setMinimumSize(800, 550)
        self.mainframe=QFrame(self)
        self.mainframe.setStyleSheet(
        """
            background: rgba(70, 70, 70, 0.58);
            border: 1px solid #BBBBBB;
            border-radius: 24px;
                """)
        self.setCentralWidget(self.mainframe)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        #main_frame
        frame =QtWidgets.QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(0)
        frame.setStyleSheet("""
            border: 1px solid #BBBBBB;
            border-radius: 16px;     
            background: #1B1D1E;
                """)
        self.setCentralWidget(frame)
        grid_1 = QGridLayout()
        grid_1.setHorizontalSpacing(10)
        grid_1.setVerticalSpacing(10)
        frame.setLayout(grid_1)
        #window_1
        window_1 = QFrame(self)
        grid_1.addWidget(window_1,0,1,1,1)
        window_1.setStyleSheet("""
            border: 1px solid #BBBBBB;
            border-radius: 16px;     
            background: #1B1D1E;
                """)
        #widgets_area
        widgets_area = QFrame(self)
        widgets_area.setFixedWidth(256)
        widgets_area.setStyleSheet("""
            background: rgba(255, 255, 255, 0.21);
            border-radius: 16px;
        """)
        grid_1.addWidget(widgets_area,0,0,1,1)
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
    def resizeEvent(self, event):
        QtWidgets.QMainWindow.resizeEvent(self, event)
        self.updateGrips()
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(),self.y() + delta.y())
        self.oldPosition = event.globalPos()
    def mouseDoubleClickEvent(self, event):
        state = int(self.windowState())
        if state == 0:
            self.showMaximized()
        else:
            self.showNormal()
app = QtWidgets.QApplication([])
m = Main()
m.show()
app.exec_()
