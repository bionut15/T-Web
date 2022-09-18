
from PyQt5.QtCore import QSize, Qt, QRectF, QPoint 
from PyQt5.QtWidgets import (QApplication, QPushButton, QFrame, QWidget, QGridLayout)
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
    def ui_componets(self):
          #close button
         cbutton = QPushButton('', self)
         cbutton.clicked.connect(QApplication.instance().quit)
         cbutton.setFixedSize(20,20)
         cbutton.move(1560,18)   
         cbutton.setStyleSheet(
         """
            background: #FF2626;
            border-radius: 10px;
                """)
           #maximize button
         mbutton = QPushButton('', self)
         mbutton.clicked.connect(self.maximize)
         mbutton.setFixedSize(20,20)
         mbutton.move(1530,18) 
         mbutton.setStyleSheet(
         """
            background: #34FF6D;
            border-radius : 10px;
                """)
            #minimize button
         nbutton = QPushButton('', self)
         nbutton.clicked.connect(self.minimize)
         nbutton.setFixedSize(20,20)
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

         grid = QGridLayout()
         self.setLayout(grid)
         grid.addWidget(widget)
         grid.addWidget(frame)
         grid.addWidget(nbutton)
         grid.addWidget(mbutton)
         grid.addWidget(cbutton)
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
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = tweb()
    w.show()
    sys.exit(app.exec_())
