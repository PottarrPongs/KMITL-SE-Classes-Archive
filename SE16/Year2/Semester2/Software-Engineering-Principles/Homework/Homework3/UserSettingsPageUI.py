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

