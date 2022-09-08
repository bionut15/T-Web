#made by ionut b

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame 
from PyQt5 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        #Main window configuration
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
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
    def ui_componets(self):
  #Border settings
            #close button
        cbutton = QPushButton('', self)
        cbutton.clicked.connect(QApplication.instance().quit)
        cbutton.resize(20,20)
        cbutton.move(1560,18)   
        cbutton.setStyleSheet(
        """
            position: absolute;
            width: 19px;
            height: 19px;
            left: 1556px;
            top: 89px;
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
            position: absolute;
            width: 19px;
            height: 19px;
            left: 1556px;
            top: 89px;
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
            position: absolute;
            width: 19px;
            height: 19px;
            left: 1556px;
            top: 89px;
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
            position: absolute;
            background: rgba(255, 255, 255, 0.21);
            border-radius: 16px;
                """)
    def minimize(self):
        self.showMinimized()
    def maximize(self):
        self.showMaximized()
    def resizeEvent(self, event):
        path = QPainterPath()
        print(self.rect())
        path.addRoundedRect(QRectF(self.rect()),24, 24,Qt.AbsoluteSize)
        reg = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(reg)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
