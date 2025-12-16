import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from DesignPageUI import Ui_Form

class Design(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.class_2.clicked.connect(lambda: self.changePage(0))
        self.ui.GanttChart.clicked.connect(lambda: self.changePage(1))
        self.ui.interaction.clicked.connect(lambda: self.changePage(2))

    def changePage(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Design()
    w.show()
    sys.exit(app.exec())
