#made by ionut b

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        #Main window configuration
       
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(QSize(1600, 900))
        self.setWindowOpacity(0.6)

        self.setStyleSheet(
        """ 
            background: rgba(70, 70, 70, 0.58);
            border: 1px solid #BBBBBB;
            border-radius: 20px;
                """)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
