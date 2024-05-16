# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Entry.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Entry(object):
    def setupUi(self, Entry):
        if not Entry.objectName():
            Entry.setObjectName(u"Entry")
        Entry.resize(857, 317)
        Entry.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_2 = QVBoxLayout(Entry)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(Entry)
        self.main_frame.setObjectName(u"main_frame")
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, 10)
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: none;\n"
"color: rgba(112, 38, 50, 190);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.main_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: none;\n"
"color: rgba(112, 38, 50, 190);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_omr = QPushButton(self.main_frame)
        self.pushButton_omr.setObjectName(u"pushButton_omr")
        self.pushButton_omr.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"padding-top: 30px;\n"
"padding-bottom: 30px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_omr)

        self.pushButton_bta = QPushButton(self.main_frame)
        self.pushButton_bta.setObjectName(u"pushButton_bta")
        self.pushButton_bta.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"padding-top: 30px;\n"
"padding-bottom: 30px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_bta)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.main_frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: none;\n"
"color: rgba(112, 38, 50, 190);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.pushButton_almanac = QPushButton(self.main_frame)
        self.pushButton_almanac.setObjectName(u"pushButton_almanac")
        self.pushButton_almanac.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_almanac)


        self.verticalLayout_2.addWidget(self.main_frame)


        self.retranslateUi(Entry)

        QMetaObject.connectSlotsByName(Entry)
    # setupUi

    def retranslateUi(self, Entry):
        Entry.setWindowTitle(QCoreApplication.translate("Entry", u"Form", None))
        self.label.setText(QCoreApplication.translate("Entry", u"World of Medicine", None))
        self.label_2.setText(QCoreApplication.translate("Entry", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0431\u043e\u0447\u0435\u0435 \u043c\u0435\u0441\u0442\u043e", None))
        self.pushButton_omr.setText(QCoreApplication.translate("Entry", u"\u041e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0439 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438\n"
"\u0440\u0430\u0431\u043e\u0447\u0435\u0435 \u043c\u0435\u0441\u0442\u043e \u0432\u0440\u0430\u0447\u0430 \u0424\u0420\u041c", None))
        self.pushButton_bta.setText(QCoreApplication.translate("Entry", u"\u041a\u0430\u0431\u0438\u043d\u0435\u0442\n"
"\u0431\u043e\u0442\u0443\u043b\u0438\u043d\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Entry", u"\u041f\u0440\u043e\u0447\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b", None))
        self.pushButton_almanac.setText(QCoreApplication.translate("Entry", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432", None))
    # retranslateUi

