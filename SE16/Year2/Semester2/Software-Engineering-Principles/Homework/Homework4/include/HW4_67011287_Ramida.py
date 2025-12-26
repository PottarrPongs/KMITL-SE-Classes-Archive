# HW4_67011287_Ramida.py



# ---------- DesignPage ----------



# DesignPageUI.py



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(966, 681)
        Form.setStyleSheet(u"background-color:  rgb(247, 247, 247)\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 971, 91))
        self.widget.setStyleSheet(u"background-color: #2f8ed2;\n"
"color: white;")
        self.class_2 = QPushButton(self.widget)
        self.class_2.setObjectName(u"class_2")
        self.class_2.setGeometry(QRect(220, 0, 171, 91))
        self.class_2.setStyleSheet(u"QPushButton {\n"
"                    font-size: 16px;\n"
"                    background: #2f8ed2;\n"
"                    color: white;\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background: #fdd148;\n"
"                    color: black;\n"
"                }")
        self.interaction = QPushButton(self.widget)
        self.interaction.setObjectName(u"interaction")
        self.interaction.setGeometry(QRect(400, 0, 171, 91))
        self.interaction.setStyleSheet(u"QPushButton {\n"
"                    font-size: 16px;\n"
"                    background: #2f8ed2;\n"
"                    color: white;\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background: #fdd148;\n"
"                    color: black;\n"
"                }")
        self.GanttChart = QPushButton(self.widget)
        self.GanttChart.setObjectName(u"GanttChart")
        self.GanttChart.setGeometry(QRect(580, 0, 171, 91))
        self.GanttChart.setStyleSheet(u"QPushButton {\n"
"                    font-size: 16px;\n"
"                    background: #2f8ed2;\n"
"                    color: white;\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background: #fdd148;\n"
"                    color: black;\n"
"                }")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 90, 961, 591))
        self.classPage = QWidget()
        self.classPage.setObjectName(u"classPage")
        self.widget_2 = QWidget(self.classPage)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 141, 591))
        self.widget_2.setStyleSheet(u"background-color: #d9ecf7;\n"
"            border-right: 1px solid #b0cddd;")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 51, 31))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 51, 31))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 70, 51, 31))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 100, 51, 31))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.classPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 20, 221, 31))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.classPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 60, 791, 511))
        self.label_6.setStyleSheet(u"background: #eeeeee;\n"
"            border: 2px dashed #999;\n"
"color: black;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.classPage)
        self.ganttPage = QWidget()
        self.ganttPage.setObjectName(u"ganttPage")
        self.label_14 = QLabel(self.ganttPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(380, 20, 221, 31))
        self.label_14.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.ganttPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 60, 931, 511))
        self.label_13.setStyleSheet(u"background: #eeeeee;\n"
"            border: 2px dashed #999;\n"
"color: black;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.ganttPage)
        self.interactionPage = QWidget()
        self.interactionPage.setObjectName(u"interactionPage")
        self.label_12 = QLabel(self.interactionPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(160, 60, 791, 511))
        self.label_12.setStyleSheet(u"background: #eeeeee;\n"
"            border: 2px dashed #999;\n"
"color: black;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.interactionPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(450, 20, 221, 31))
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font-size: 22px;\n"
"font-weight: bold;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_3 = QWidget(self.interactionPage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 141, 591))
        self.widget_3.setStyleSheet(u"background-color: #d9ecf7;\n"
"            border-right: 1px solid #b0cddd;")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 51, 31))
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 40, 51, 31))
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 70, 51, 31))
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 100, 51, 31))
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.interactionPage)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.class_2.setText(QCoreApplication.translate("Form", u"Class", None))
        self.interaction.setText(QCoreApplication.translate("Form", u"Interaction", None))
        self.GanttChart.setText(QCoreApplication.translate("Form", u"Gantt Chart", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tools:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tools 1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Tools 2", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Tools 3", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Class Diagram", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Class Diagram", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Gantt Chart", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Gantt Chart", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Interaction Diagram", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Interaction Diagram", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Tools:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Tools 1", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Tools 2", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Tools 3", None))
    # retranslateUi



# DesignPageCode.py



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



# ---------- UserSettingsPage ----------



# UserSettingsPageUI.py



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(966, 674)
        Form.setStyleSheet(u"background-color:  rgb(247, 247, 247);\n"
"color: black;")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 321, 631))
        self.widget.setStyleSheet(u"background-color: #fdd148; border-radius: 10px;\n"
"font-size:  16px\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 151, 41))
        self.label.setStyleSheet(u"font-size: 28px;\n"
"font-weight: bold;")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(60, 80, 201, 201))
        self.widget_2.setStyleSheet(u"background: gray; border-radius: 100px;")
        self.username = QLabel(self.widget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(0, 300, 321, 31))
        self.username.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gmail = QLabel(self.widget)
        self.gmail.setObjectName(u"gmail")
        self.gmail.setGeometry(QRect(0, 330, 321, 31))
        self.gmail.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.phone = QLabel(self.widget)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(0, 360, 321, 31))
        self.phone.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 390, 321, 31))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 420, 321, 31))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(360, 30, 591, 621))
        self.scrollArea.setStyleSheet(u"font-size: 16px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 587, 617))
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 321, 41))
        self.label_2.setStyleSheet(u"font-size: 24px;\n"
"font-weight: bold;")
        self.username_2 = QLabel(self.scrollAreaWidgetContents)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setGeometry(QRect(20, 60, 321, 31))
        self.username_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.usernameInput = QLineEdit(self.scrollAreaWidgetContents)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setGeometry(QRect(20, 100, 551, 31))
        self.usernameInput.setText(u"")
        self.username_3 = QLabel(self.scrollAreaWidgetContents)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setGeometry(QRect(20, 140, 321, 31))
        self.username_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.emailInput = QLineEdit(self.scrollAreaWidgetContents)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(20, 180, 551, 31))
        self.emailInput.setText(u"")
        self.username_4 = QLabel(self.scrollAreaWidgetContents)
        self.username_4.setObjectName(u"username_4")
        self.username_4.setGeometry(QRect(20, 220, 321, 31))
        self.username_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.phoneInput = QLineEdit(self.scrollAreaWidgetContents)
        self.phoneInput.setObjectName(u"phoneInput")
        self.phoneInput.setGeometry(QRect(20, 260, 551, 31))
        self.phoneInput.setText(u"")
        self.username_5 = QLabel(self.scrollAreaWidgetContents)
        self.username_5.setObjectName(u"username_5")
        self.username_5.setGeometry(QRect(20, 310, 321, 31))
        self.username_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 350, 551, 31))
        self.lineEdit_4.setText(u"12345")
        self.lineEdit_4.setReadOnly(True)
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 540, 571, 71))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"                background-color: #2f8ed2;\n"
"                color: white;\n"
"                border-radius: 8px;\n"
"                font-size: 18px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #fdd148;\n"
"                color: black;\n"
"            }")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Account:", None))
        self.username.setText(QCoreApplication.translate("Form", u"Username: Raph", None))
        self.gmail.setText(QCoreApplication.translate("Form", u"Email: raph@example.com", None))
        self.phone.setText(QCoreApplication.translate("Form", u"Phone: +66 1234 5678", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Account ID: 12345", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Status: Active", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Edit Account Information:", None))
        self.username_2.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.usernameInput.setInputMask("")
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("Form", u"Enter new username", None))
        self.username_3.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.emailInput.setInputMask("")
        self.emailInput.setPlaceholderText(QCoreApplication.translate("Form", u"Enter new email", None))
        self.username_4.setText(QCoreApplication.translate("Form", u"Phone:", None))
        self.phoneInput.setInputMask("")
        self.phoneInput.setPlaceholderText(QCoreApplication.translate("Form", u"Enter phone number", None))
        self.username_5.setText(QCoreApplication.translate("Form", u"Account ID (Read-only):", None))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Enter new username", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi



# UserSettingsPageCode.py



import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from UserSettingsPageUI import Ui_Form

class ProfileWidget(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(image_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        size = min(self.width(), self.height())
        rect = QRect(
            (self.width() - size) // 2,
            (self.height() - size) // 2,
            size,
            size
        )

        path = QPainterPath()
        path.addEllipse(rect)
        painter.setClipPath(path)

        painter.drawPixmap(
            rect,
            self.pixmap.scaled(
                rect.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
        )


class Setting(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.saveData)
        self.saveSfx = QSoundEffect(self)
        self.saveSfx.setSource(QUrl.fromLocalFile("./sounds.save_button.wav"))
        self.saveSfx.setVolume(0.5)
        self.hoverSfx = QSoundEffect(self)
        self.hoverSfx.setSource(QUrl.fromLocalFile("./sounds/hover.wav"))
       
        self.ui.pushButton.installEventFilter(self)
        self.ui.pushButton.setAttribute(Qt.WA_Hover)

        self.profileWidget = ProfileWidget("./images/profile.jpg", self.ui.widget_2.parent())
        self.profileWidget.setGeometry(self.ui.widget_2.geometry())

        self.ui.widget_2.deleteLater()
        self.ui.widget_2 = self.profileWidget

    def saveData(self):
        self.saveSfx.play()
        new_username = self.ui.usernameInput.text().strip()
        new_email = self.ui.emailInput.text().strip()
        new_phone = self.ui.phoneInput.text().strip()

        if new_username:
            self.ui.username.setText(f"Username: {new_username}")

        if new_email:
            self.ui.gmail.setText(f"Email: {new_email}")

        if new_phone:
            self.ui.phone.setText(f"Phone: {new_phone}")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            if obj == self.ui.pushButton:
                self.hoverSfx.play()
        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Setting()
    w.show()
    sys.exit(app.exec())
