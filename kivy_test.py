


import sys
from PyQt5.QtCore import Qt,  QRectF
from PyQt5.QtGui import QPainterPath, QRegion
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame

class Example(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600,400)
        self.mainframe=QFrame(self)
        self.mainframe.setStyleSheet("background:blue;border-radius:25px")
        self.setCentralWidget(self.mainframe)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    def resizeEvent(self, event):
        path = QPainterPath()
        print(self.rect())
        path.addRoundedRect(QRectF(self.rect()),25, 25,Qt.AbsoluteSize)
        reg = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(reg)     

   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(app.exec_())  

