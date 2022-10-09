#made by ionut b

from PyQt5.QtCore import QSize, Qt, QRectF, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QSizeGrip 
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPainterPath, QRegion

class MainWindow(QMainWindow):
    _gripSize = 8
    def __init__(self):
        super(MainWindow, self).__init__()
        #Main window configuration
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(900, 750)
        self.resize(1600, 900)
        self.mainframe=QFrame(self)
        self.mainframe.setStyleSheet(
        """
            background: rgba(70, 70, 70, 0.58);
            border: 1px solid #BBBBBB;
            border-radius: 24px;
                """)
        self.setCentralWidget(self.mainframe)
        self.ui_componets()
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

 
    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        # top left grip doesn't need to be moved...
        # top right
        self.grips[1].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[2].move( rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)

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
        # top right
        self.cornerGrips[1].setGeometry(
            QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())
        # bottom right
        self.cornerGrips[2].setGeometry(
            QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))
        # bottom left
        self.cornerGrips[3].setGeometry(
            QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

        # left edge
        self.sideGrips[0].setGeometry(
            0, inRect.top(), self.gripSize, inRect.height())
        # top edge
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self.gripSize)
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
    def ui_componets(self):
  #Border settings
            #close button
        cbutton = QPushButton('', self)
        cbutton.clicked.connect(QApplication.instance().quit)
        cbutton.resize(20,20)
        cbutton.move(1560,18)   
        cbutton.setStyleSheet(
        """
            background: #FF2626;
            border-radius: 10px;
                """)
            #maximize button
        mbutton = QPushButton('', self)
        mbutton.clicked.connect(self.maximize)
        mbutton.resize(20,20)
        mbutton.move(1530,18) 
        mbutton.setStyleSheet(
        """
            background: #34FF6D;
            border-radius : 10px;
                """)
            #minimize button
        nbutton = QPushButton('', self)
        nbutton.clicked.connect(self.minimize)
        nbutton.resize(20,20)
        nbutton.move(1500,18)        
        nbutton.setStyleSheet(
        """
            background: #F0FF40;
            border-radius : 10px; 
                """)
    #window area
        frame =QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(6)
        frame.resize(1300,864)
        frame.move(18,18)
        frame.setStyleSheet("""
            border: 1px solid #BBBBBB;
            border-radius: 16px;     
            background: #1B1D1E;
                """)
    #widget area
        widget =QFrame(self)
        widget.setFrameShape(QFrame.StyledPanel)
        widget.setLineWidth(6)
        widget.move(1332, 50)
        widget.resize(250, 832)
        widget.setStyleSheet("""
            background: rgba(255, 255, 255, 0.21);
            border-radius: 16px;
                """)
    def minimize(self):
        self.showMinimized()
    def maximize(self):
        state = int(self.windowState())
        if state == 0:
            self.showMaximized()
        else:
             self.showNormal()
    def resizeEvent(self, event):
        path = QPainterPath()
        print(self.rect())
        path.addRoundedRect(QRectF(self.rect()),25, 25,Qt.AbsoluteSize)
        reg = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(reg)
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
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
