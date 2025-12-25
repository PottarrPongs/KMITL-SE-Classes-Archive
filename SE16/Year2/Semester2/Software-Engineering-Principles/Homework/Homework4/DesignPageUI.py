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

