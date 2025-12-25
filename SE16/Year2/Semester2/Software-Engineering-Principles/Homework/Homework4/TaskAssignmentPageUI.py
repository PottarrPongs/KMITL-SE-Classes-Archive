# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAssignmentPage (1).ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 700)
        Form.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navbar_hbox = QHBoxLayout()
        self.navbar_hbox.setObjectName(u"navbar_hbox")
        self.logo = QLabel(Form)
        self.logo.setObjectName(u"logo")

        self.navbar_hbox.addWidget(self.logo)

        self.current_mode_label = QLabel(Form)
        self.current_mode_label.setObjectName(u"current_mode_label")
        font = QFont()
        font.setFamilies([u"CaskaydiaCove Nerd Font"])
        font.setPointSize(16)
        self.current_mode_label.setFont(font)

        self.navbar_hbox.addWidget(self.current_mode_label)

        self.toggle_btn = QPushButton(Form)
        self.toggle_btn.setObjectName(u"toggle_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_btn.sizePolicy().hasHeightForWidth())
        self.toggle_btn.setSizePolicy(sizePolicy)
        self.toggle_btn.setMinimumSize(QSize(0, 0))
        self.toggle_btn.setFont(font)

        self.navbar_hbox.addWidget(self.toggle_btn)

        self.navbar_hbox.setStretch(0, 1)
        self.navbar_hbox.setStretch(1, 6)

        self.verticalLayout.addLayout(self.navbar_hbox)

        self.mode_tab = QStackedWidget(Form)
        self.mode_tab.setObjectName(u"mode_tab")
        self.manual_mode_tab = QWidget()
        self.manual_mode_tab.setObjectName(u"manual_mode_tab")
        self.horizontalLayout = QHBoxLayout(self.manual_mode_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.editor_vbox = QVBoxLayout()
        self.editor_vbox.setObjectName(u"editor_vbox")
        self.code_label = QLabel(self.manual_mode_tab)
        self.code_label.setObjectName(u"code_label")
        font1 = QFont()
        font1.setPointSize(24)
        self.code_label.setFont(font1)

        self.editor_vbox.addWidget(self.code_label)

        self.editor = QTextEdit(self.manual_mode_tab)
        self.editor.setObjectName(u"editor")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setKerning(False)
        self.editor.setFont(font2)
        self.editor.setStyleSheet(u"background-color: #ffffff;")

        self.editor_vbox.addWidget(self.editor)

        self.manual_btn_hbox = QHBoxLayout()
        self.manual_btn_hbox.setObjectName(u"manual_btn_hbox")
        self.manual_load_btn = QPushButton(self.manual_mode_tab)
        self.manual_load_btn.setObjectName(u"manual_load_btn")

        self.manual_btn_hbox.addWidget(self.manual_load_btn)

        self.manual_convert_btn = QPushButton(self.manual_mode_tab)
        self.manual_convert_btn.setObjectName(u"manual_convert_btn")

        self.manual_btn_hbox.addWidget(self.manual_convert_btn)

        self.manual_save_btn = QPushButton(self.manual_mode_tab)
        self.manual_save_btn.setObjectName(u"manual_save_btn")

        self.manual_btn_hbox.addWidget(self.manual_save_btn)


        self.editor_vbox.addLayout(self.manual_btn_hbox)

        self.editor_vbox.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.editor_vbox)

        self.preview_vbox_manual = QVBoxLayout()
        self.preview_vbox_manual.setObjectName(u"preview_vbox_manual")
        self.preview_label_maual = QLabel(self.manual_mode_tab)
        self.preview_label_maual.setObjectName(u"preview_label_maual")
        self.preview_label_maual.setFont(font1)

        self.preview_vbox_manual.addWidget(self.preview_label_maual)


        self.horizontalLayout.addLayout(self.preview_vbox_manual)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.mode_tab.addWidget(self.manual_mode_tab)
        self.sync_mode_tab = QWidget()
        self.sync_mode_tab.setObjectName(u"sync_mode_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.sync_mode_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.preview_vbox_sync = QVBoxLayout()
        self.preview_vbox_sync.setObjectName(u"preview_vbox_sync")
        self.preview_label_sync = QLabel(self.sync_mode_tab)
        self.preview_label_sync.setObjectName(u"preview_label_sync")
        self.preview_label_sync.setFont(font1)

        self.preview_vbox_sync.addWidget(self.preview_label_sync)

        self.web_engine_hbox = QHBoxLayout()
        self.web_engine_hbox.setObjectName(u"web_engine_hbox")

        self.preview_vbox_sync.addLayout(self.web_engine_hbox)

        self.sync_btn_hbox = QHBoxLayout()
        self.sync_btn_hbox.setObjectName(u"sync_btn_hbox")
        self.sync_load_btn = QPushButton(self.sync_mode_tab)
        self.sync_load_btn.setObjectName(u"sync_load_btn")

        self.sync_btn_hbox.addWidget(self.sync_load_btn)

        self.sync_convert_btn = QPushButton(self.sync_mode_tab)
        self.sync_convert_btn.setObjectName(u"sync_convert_btn")

        self.sync_btn_hbox.addWidget(self.sync_convert_btn)

        self.sync_save_btn = QPushButton(self.sync_mode_tab)
        self.sync_save_btn.setObjectName(u"sync_save_btn")

        self.sync_btn_hbox.addWidget(self.sync_save_btn)


        self.preview_vbox_sync.addLayout(self.sync_btn_hbox)

        self.preview_vbox_sync.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.preview_vbox_sync)

        self.mode_tab.addWidget(self.sync_mode_tab)

        self.verticalLayout.addWidget(self.mode_tab)


        self.retranslateUi(Form)

        self.mode_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText("")
        self.current_mode_label.setText(QCoreApplication.translate("Form", u"Current Mode:", None))
        self.toggle_btn.setText(QCoreApplication.translate("Form", u"Toggle Mode", None))
        self.code_label.setText(QCoreApplication.translate("Form", u"Code:", None))
        self.editor.setPlaceholderText("")
        self.manual_load_btn.setText(QCoreApplication.translate("Form", u"Load", None))
        self.manual_convert_btn.setText(QCoreApplication.translate("Form", u"Convert", None))
        self.manual_save_btn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.preview_label_maual.setText(QCoreApplication.translate("Form", u"Preview:", None))
        self.preview_label_sync.setText(QCoreApplication.translate("Form", u"Preview:", None))
        self.sync_load_btn.setText(QCoreApplication.translate("Form", u"Load", None))
        self.sync_convert_btn.setText(QCoreApplication.translate("Form", u"Convert", None))
        self.sync_save_btn.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

