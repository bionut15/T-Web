#made by ionut b

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton 
from PyQt5 import QtGui
from BlurWindow.blurWindow import GlobalBlur

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        #Main window configuration
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(QSize(1600, 900))
       # self.setWindowOpacity(0.6)
        self.setStyleSheet(
        """
            background: rgba(70, 70, 70, 0.58);
            border: 1px solid #BBBBBB;
            border-radius: 20px;
                """)
    #Border settings
            #close button
        cbutton = QPushButton('', self)
        cbutton.clicked.connect(self.clickMethod)
        cbutton.resize(20,20)
        cbutton.move(1560,10)   
        cbutton.setStyleSheet(
        """
            position: absolute;
            width: 19px;
            height: 19px;
            left: 1556px;
            top: 89px;
            background: #FF2626;
            border-radius: 20px;

                """)
            #maximize button
        mbutton = QPushButton('', self)
        mbutton.clicked.connect(self.clickMethod)
        mbutton.resize(20,20)
        mbutton.move(1530,10) 
        mbutton.setStyleSheet(
        """
            position: absolute;
            width: 19px;
            height: 19px;
            left: 1556px;
            top: 89px;
            background: #34FF6D;
                """)

            #minimize button
        nbutton = QPushButton('', self)
        nbutton.clicked.connect(self.clickMethod)
        nbutton.resize(20,20)
        nbutton.move(1500,10)        
        nbutton.setStyleSheet(
        """
            position: absolute;
            width: 19px;
            height: 19px;
            left: 1556px;
            top: 89px;
            background: #F0FF40;

                """)
    def clickMethod(self):
        print('Clicked Pyqt button.')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
