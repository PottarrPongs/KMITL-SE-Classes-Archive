import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from DesignPageUI import Ui_Form

class Design(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.toggle = QSoundEffect(self)
        self.toggle.setSource(QUrl.fromLocalFile("./sounds/page_toggle.wav"))
        self.toggle.setVolume(0.5)
        self.hoverSfx = QSoundEffect(self)
        self.hoverSfx.setSource(QUrl.fromLocalFile("./sounds/hover.wav"))
        self.ui.class_2.clicked.connect(lambda: self.changePage(0))
        self.ui.GanttChart.clicked.connect(lambda: self.changePage(1))
        self.ui.interaction.clicked.connect(lambda: self.changePage(2))

        for btn in (self.ui.class_2, self.ui.GanttChart, self.ui.interaction):
            btn.installEventFilter(self)
            btn.setAttribute(Qt.WA_Hover)

    def changePage(self, index):
        self.toggle.play()
        self.ui.stackedWidget.setCurrentIndex(index)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            if obj in (self.ui.class_2, self.ui.GanttChart, self.ui.interaction):
                self.hoverSfx.play()
        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Design()
    w.show()
    sys.exit(app.exec())
