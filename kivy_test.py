import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
QPushButton, QGridLayout)
from PyQt5.QtWidgets import QFrame

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):   
        grid = QGridLayout()  
        self.setLayout(grid)
        self.resize(300, 400)
        self.frame = QFrame(self)
        buttons = QPushButton("Toggle", self)
        buttons.move(200, 200)
        self.setWindowTitle('PyQt window')  
        self.show()

if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     sys.exit(app.exec_())    
