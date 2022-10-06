
from PyQt5.QtCore import QSize, Qt, QRectF, QPoint 
from PyQt5.QtWidgets import (QApplication, QPushButton, QFrame, QWidget, QGridLayout, QSizeGrip)
from PyQt5 import QtGui
from PyQt5.QtGui import QPainterPath, QRegion

class tweb(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_config()
        self.ui_componets()
    def ui_config(self):
         self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
         self.setMinimumSize(900, 750)
         self.resize(1600, 900)
         self.setStyleSheet(
        """
            QWidget{  
            background: rgba(70, 70, 70, 0.58);
            border: 1px solid #BBBBBB;
            border-radius: 24px;
            }""")
    #     main_window = QWidgets.QWidget()
     #    sizegrip = QtWidgets.QSizegrip(main_window)
    def ui_componets(self):
            #window area
         frame =QFrame(self)
         frame.setFrameShape(QFrame.StyledPanel)
         frame.setLineWidth(6)
         frame.resize(1300,864)
         frame.setStyleSheet("""
            border: 1px solid #BBBBBB;
            border-radius: 16px;     
            background: #1B1D1E;
                """)
    #widget area
         widget =QFrame(self)
         widget.setFrameShape(QFrame.StyledPanel)
         widget.setLineWidth(6)
         widget.setFixedWidth(250)
         widget.setStyleSheet("""
            background: rgba(255, 255, 255, 0.21);
            border-radius: 16px;
                """)
#grid system 
         grid = QGridLayout()
         self.setLayout(grid)
         grid.addWidget(widget,0,0,1,1)
         grid.addWidget(frame,0,1,1,1)
         grid.setColumnMinimumWidth(1,1)
         grid.setHorizontalSpacing(12)
         sizegrip = QSizeGrip(self)
         sizegrip.setVisible(0)
#to be added
    def mouseMiddleClickEvent(self, event):
        self.showMinimized()
    def mouseDoubleClickEvent(self, event):
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
   # def size_screen_cal(self):
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = tweb()
    w.show()
    sys.exit(app.exec_())
