import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from MainPageUI import Ui_Form

white = "white"
lightGray = "#f4f4f4"
yellow = "#ffd77f"
blue = "#32a5da"
darkBlue = "#158bc1"

class mainPage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setStyleSheet(f"""
            QMainWindow {{ 
                background-color: {lightGray}; 
            }}
        """)

        self.ui.headerFrame.setStyleSheet(f"""
            QFrame#headerFrame {{
                color: white;
                background-color: {blue};
                border: 2px solid {blue};
                border-radius: 12px;
                padding: 8px;
            }}

            QFrame#headerFrame QLabel {{
                color: white;
            }}
        """)

        logoImg = QPixmap("images/logo-171.png")
        self.ui.logo.setPixmap(logoImg)

        curMemImg = QPixmap("images/member.png")
        self.ui.curMem.setPixmap(curMemImg)

        userImg = QPixmap("images/active.png")
        self.ui.userPic.setPixmap(userImg)

        self.ui.projectFrame.setStyleSheet(f"""
            QFrame#projectFrame {{
                border: 2px solid {blue};
                border-radius: 12px;
                padding: 8px;
            }}

            QFrame#projectTitleFrame {{
                background-color: {yellow};
                border: 2px solid {blue};
                border-radius: 8px;
                padding: 4px;
            }}

            QFrame#projectFrame QPushButton {{
                background-color: white;
                border: 1px solid {blue};
                border-radius: 6px;
                margin: 4px 0px;
            }}

            QFrame#projectFrame QPushButton::hover {{
                background-color: {blue};
                color: white
            }}
        """)


        self.ui.notiFrame.setStyleSheet(f"""
            QFrame#notiFrame {{
                border: 2px solid {blue};
                border-radius: 12px;
                padding: 8px;
            }}

            QFrame#notiTitleFrame {{
                background-color: {yellow};
                border: 2px solid {blue};
                border-radius: 8px;
                padding: 4px;
            }}
        """)

        self.ui.projCharterFrame.setStyleSheet(f"""
            QFrame#projCharterFrame {{
                border: 2px solid {blue};
                border-radius: 12px;
                padding: 8px;
            }}

            QFrame#projCharterTitleFrame {{
                background-color: {yellow};
                border: 2px solid {blue};
                border-radius: 8px;
                padding: 4px;
            }}

            QFrame#projCharterFrame QPushButton {{
                background-color: white;
                border: 1px solid {blue};
                border-radius: 6px;
            }}

            QFrame#projCharterFrame QPushButton::hover {{
                background-color: {blue};
                color: white;
            }}
        """)

        self.ui.assignFrame.setStyleSheet(f"""
            QFrame#assignFrame {{
                border: 2px solid {blue};
                border-radius: 12px;
                padding: 8px;
            }}

            QFrame#assignTitleFrame {{
                background-color: {yellow};
                border: 2px solid {blue};
                border-radius: 8px;
                padding: 4px;
            }}

            QFrame#assignFrame QPushButton {{
                background-color: white;
                border: 1px solid {blue};
                border-radius: 6px;
            }}

            QFrame#assignFrame QPushButton::hover {{
                background-color: {blue};
                color: white;
            }}
        """)

        for i in range(1, 8):
            projBtn = getattr(self.ui, "project" + str(i))
            projBtn.clicked.connect(lambda _, x=i: self.changeCurProj(x))

        self.ui.saveProjCharterBtn.clicked.connect(self.saveProjCharter)
        
        for i in range(1, 6):
            saveTaskBtn = getattr(self.ui, "saveTask" + str(i) + "Btn")
            saveTaskBtn.clicked.connect(lambda _, x=i: self.saveTask(x))

    def changeCurProj(self, i):
        self.ui.curProj.setText("Current Project: Project " + str(i))

    def saveProjCharter(self):
        projObjText = self.ui.projObjInput.text()
        self.ui.projObjInput.setText(projObjText)

        projStructText = self.ui.projStructInput.text()
        self.ui.projStructInput.setText(projStructText)

        projMemText = self.ui.projMemInput.text()
        self.ui.projMemInput.setText(projMemText)

        projDurText = self.ui.projDurInput.text()
        self.ui.projDurInput.setText(projDurText)

        projDeadlineText = self.ui.projDeadlineInput.text()
        self.ui.projDeadlineInput.setText(projDeadlineText)

    def saveTask(self, i):
        taskInput = getattr(self.ui, "task" + str(i) + "Input")
        taskInputText = taskInput.text()
        taskInput.setText(taskInputText)

        nameInput = getattr(self.ui, "name" + str(i) + "Input")
        nameInputText = nameInput.text()
        nameInput.setText(nameInputText)

        statusInput = getattr(self.ui, "status" + str(i) + "Input")
        statusInputText = statusInput.text()
        statusInput.setText(statusInputText)

if __name__ == "__main__":
    app = QApplication()
    w = mainPage()
    w.show()
    sys.exit(app.exec())
