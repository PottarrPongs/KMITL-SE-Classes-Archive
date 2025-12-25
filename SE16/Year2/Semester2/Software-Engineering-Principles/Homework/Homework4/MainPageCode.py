import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from main import Ui_Form

white = "white"
lightGray = "#f4f4f4"
yellow = "#ffd77f"
blue = "#32a5da"
darkBlue = "#158bc1"


class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


class mainPage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        oldLogo = self.ui.logo
        self.ui.logo = ClickableLabel(oldLogo.parent())
        self.ui.logo.setObjectName(oldLogo.objectName())
        self.ui.logo.setGeometry(oldLogo.geometry())
        self.ui.logo.setAlignment(oldLogo.alignment())
        self.ui.logo.setScaledContents(oldLogo.hasScaledContents())
        oldLogo.deleteLater()

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

        logoImg = QPixmap("images/logo.png")
        self.ui.logo.setPixmap(logoImg.scaledToHeight(36, Qt.SmoothTransformation))

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

        self.saveSfx = QSoundEffect(self)
        self.saveSfx.setSource(QUrl.fromLocalFile("sounds/save.wav"))
        self.saveSfx.setVolume(0.7)

        for i in range(1, 8):
            projBtn = getattr(self.ui, "project" + str(i))
            projBtn.clicked.connect(lambda _, x=i: self.changeCurProj(x))
            projBtn.clicked.connect(self.saveSfx.play)

        self.ui.saveProjCharterBtn.clicked.connect(self.saveProjCharter)
        self.ui.saveProjCharterBtn.clicked.connect(self.saveSfx.play)

        for i in range(1, 6):
            saveTaskBtn = getattr(self.ui, "saveTask" + str(i) + "Btn")
            saveTaskBtn.clicked.connect(lambda _, x=i: self.saveTask(x))
            saveTaskBtn.clicked.connect(self.saveSfx.play)

        self.logoAnim = None
        self.logoBaseGeo = self.ui.logo.geometry()

        self.logoShadow = QGraphicsDropShadowEffect(self.ui.logo)
        self.logoShadow.setOffset(0, 0)
        self.logoShadow.setBlurRadius(0)
        self.logoShadow.setColor(QColor(255, 215, 127, 200))
        self.ui.logo.setGraphicsEffect(self.logoShadow)

        self.ui.logo.setCursor(Qt.PointingHandCursor)
        self.ui.logo.clicked.connect(self.playLogoAnim)

    def playLogoAnim(self):
        if self.logoAnim and self.logoAnim.state() == QAbstractAnimation.Running:
            return

        base = self.logoBaseGeo
        cx = base.center().x()
        cy = base.center().y()

        def scaledRect(scale: float) -> QRect:
            w = int(base.width() * scale)
            h = int(base.height() * scale)
            return QRect(cx - w // 2, cy - h // 2, w, h)

        group = QSequentialAnimationGroup(self)

        a1 = QPropertyAnimation(self.ui.logo, b"geometry")
        a1.setDuration(120)
        a1.setEasingCurve(QEasingCurve.OutCubic)
        a1.setStartValue(base)
        a1.setEndValue(scaledRect(1.12))

        a2 = QPropertyAnimation(self.ui.logo, b"geometry")
        a2.setDuration(120)
        a2.setEasingCurve(QEasingCurve.OutBack)
        a2.setStartValue(scaledRect(1.12))
        a2.setEndValue(scaledRect(0.98))

        a3 = QPropertyAnimation(self.ui.logo, b"geometry")
        a3.setDuration(140)
        a3.setEasingCurve(QEasingCurve.OutCubic)
        a3.setStartValue(scaledRect(0.98))
        a3.setEndValue(base)

        group.addAnimation(a1)
        group.addAnimation(a2)
        group.addAnimation(a3)

        glow = QSequentialAnimationGroup(self)
        g1 = QPropertyAnimation(self.logoShadow, b"blurRadius")
        g1.setDuration(140)
        g1.setStartValue(0)
        g1.setEndValue(22)

        g2 = QPropertyAnimation(self.logoShadow, b"blurRadius")
        g2.setDuration(240)
        g2.setStartValue(22)
        g2.setEndValue(0)

        glow.addAnimation(g1)
        glow.addAnimation(g2)

        both = QParallelAnimationGroup(self)
        both.addAnimation(group)
        both.addAnimation(glow)

        self.logoAnim = both
        self.logoAnim.start()

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