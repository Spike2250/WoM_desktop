# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Discharge_details.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTimeEdit, QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc

class Ui_Dis_details(object):
    def setupUi(self, Dis_details):
        if not Dis_details.objectName():
            Dis_details.setObjectName(u"Dis_details")
        Dis_details.resize(1013, 628)
        Dis_details.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout = QVBoxLayout(Dis_details)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(Dis_details)
        self.main.setObjectName(u"main")
        self.horizontalLayout_2 = QHBoxLayout(self.main)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.discharge = QFrame(self.main)
        self.discharge.setObjectName(u"discharge")
        self.discharge.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.discharge)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_discharge = QFrame(self.discharge)
        self.frame_discharge.setObjectName(u"frame_discharge")
        self.frame_discharge.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_2 = QGridLayout(self.frame_discharge)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_dis = QLabel(self.frame_discharge)
        self.label_dis.setObjectName(u"label_dis")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        self.label_dis.setFont(font)
        self.label_dis.setStyleSheet(u"border: none;\n"
"background-color: transparent;")

        self.gridLayout_2.addWidget(self.label_dis, 4, 0, 1, 1)

        self.checkBox_dis = QCheckBox(self.frame_discharge)
        self.checkBox_dis.setObjectName(u"checkBox_dis")
        self.checkBox_dis.setFont(font)
        self.checkBox_dis.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_dis.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_2.addWidget(self.checkBox_dis, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_discharge)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.pushButtonDischarge_and_close_history = QPushButton(self.frame_discharge)
        self.pushButtonDischarge_and_close_history.setObjectName(u"pushButtonDischarge_and_close_history")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(112, 38, 50, 190))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush2 = QBrush(QColor(237, 237, 237, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(110, 110, 110, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(147, 147, 147, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(238, 238, 238, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        brush9 = QBrush(QColor(220, 220, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonDischarge_and_close_history.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButtonDischarge_and_close_history.setFont(font1)
        self.pushButtonDischarge_and_close_history.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(112, 38, 50, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(112, 38, 50, 255);\n"
"border: 2px solid rgba(145, 47, 64, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(145, 47, 64, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(112, 38, 50, 255);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/icons/person_off_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonDischarge_and_close_history.setIcon(icon)
        self.pushButtonDischarge_and_close_history.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButtonDischarge_and_close_history, 2, 0, 2, 1)


        self.horizontalLayout.addWidget(self.frame_discharge)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addWidget(self.discharge, 2, 1, 1, 1)

        self.frame_discharge_details = QFrame(self.main)
        self.frame_discharge_details.setObjectName(u"frame_discharge_details")
        self.frame_discharge_details.setMinimumSize(QSize(800, 0))
        self.frame_discharge_details.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.frame_discharge_details)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.labelPtNMU_code = QLabel(self.frame_discharge_details)
        self.labelPtNMU_code.setObjectName(u"labelPtNMU_code")
        palette1 = QPalette()
        brush10 = QBrush(QColor(50, 98, 115, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        brush11 = QBrush(QColor(0, 0, 0, 0))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
        brush12 = QBrush(QColor(50, 98, 115, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtNMU_code.setPalette(palette1)
        self.labelPtNMU_code.setFont(font1)
        self.labelPtNMU_code.setLayoutDirection(Qt.LeftToRight)
        self.labelPtNMU_code.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtNMU_code, 17, 0, 1, 1)

        self.labelPtMKB10_main = QLabel(self.frame_discharge_details)
        self.labelPtMKB10_main.setObjectName(u"labelPtMKB10_main")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtMKB10_main.setPalette(palette2)
        self.labelPtMKB10_main.setFont(font1)
        self.labelPtMKB10_main.setLayoutDirection(Qt.LeftToRight)
        self.labelPtMKB10_main.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtMKB10_main.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtMKB10_main, 15, 0, 1, 1)

        self.labelPtAdmissionDay = QLabel(self.frame_discharge_details)
        self.labelPtAdmissionDay.setObjectName(u"labelPtAdmissionDay")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        brush13 = QBrush(QColor(236, 236, 236, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(108, 108, 108, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(145, 145, 145, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        brush16 = QBrush(QColor(217, 217, 217, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtAdmissionDay.setPalette(palette3)
        self.labelPtAdmissionDay.setFont(font1)
        self.labelPtAdmissionDay.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtAdmissionDay, 7, 0, 1, 1)

        self.comboBoxPtHoptitalisationType = QComboBox(self.frame_discharge_details)
        self.comboBoxPtHoptitalisationType.addItem("")
        self.comboBoxPtHoptitalisationType.addItem("")
        self.comboBoxPtHoptitalisationType.addItem("")
        self.comboBoxPtHoptitalisationType.addItem("")
        self.comboBoxPtHoptitalisationType.setObjectName(u"comboBoxPtHoptitalisationType")
        palette4 = QPalette()
        brush17 = QBrush(QColor(19, 36, 43, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush18 = QBrush(QColor(19, 36, 43, 128))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBoxPtHoptitalisationType.setPalette(palette4)
        self.comboBoxPtHoptitalisationType.setFont(font1)
        self.comboBoxPtHoptitalisationType.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBoxPtHoptitalisationType, 3, 1, 1, 4)

        self.comboBoxPtMKB10_main = QComboBox(self.frame_discharge_details)
        self.comboBoxPtMKB10_main.setObjectName(u"comboBoxPtMKB10_main")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBoxPtMKB10_main.setPalette(palette5)
        self.comboBoxPtMKB10_main.setFont(font1)
        self.comboBoxPtMKB10_main.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtMKB10_main.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxPtMKB10_main, 15, 1, 1, 4)

        self.labelDischarge_data_2 = QLabel(self.frame_discharge_details)
        self.labelDischarge_data_2.setObjectName(u"labelDischarge_data_2")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelDischarge_data_2.setPalette(palette6)
        self.labelDischarge_data_2.setFont(font1)
        self.labelDischarge_data_2.setLayoutDirection(Qt.LeftToRight)
        self.labelDischarge_data_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelDischarge_data_2, 21, 0, 1, 1)

        self.labelPtDischargeDate = QLabel(self.frame_discharge_details)
        self.labelPtDischargeDate.setObjectName(u"labelPtDischargeDate")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtDischargeDate.setPalette(palette7)
        self.labelPtDischargeDate.setFont(font1)
        self.labelPtDischargeDate.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDischargeDate.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtDischargeDate, 13, 0, 1, 1)

        self.timeEditDischargeTime = QTimeEdit(self.frame_discharge_details)
        self.timeEditDischargeTime.setObjectName(u"timeEditDischargeTime")
        self.timeEditDischargeTime.setFont(font1)
        self.timeEditDischargeTime.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.timeEditDischargeTime, 13, 2, 1, 1)

        self.labelPtDischargeDate_plan = QLabel(self.frame_discharge_details)
        self.labelPtDischargeDate_plan.setObjectName(u"labelPtDischargeDate_plan")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtDischargeDate_plan.setPalette(palette8)
        self.labelPtDischargeDate_plan.setFont(font1)
        self.labelPtDischargeDate_plan.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDischargeDate_plan.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtDischargeDate_plan, 12, 0, 1, 1)

        self.label = QLabel(self.frame_discharge_details)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 19, 2, 1, 1)

        self.comboBoxDischargeData_1 = QComboBox(self.frame_discharge_details)
        self.comboBoxDischargeData_1.addItem("")
        self.comboBoxDischargeData_1.addItem("")
        self.comboBoxDischargeData_1.addItem("")
        self.comboBoxDischargeData_1.addItem("")
        self.comboBoxDischargeData_1.setObjectName(u"comboBoxDischargeData_1")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBoxDischargeData_1.setPalette(palette9)
        self.comboBoxDischargeData_1.setFont(font1)
        self.comboBoxDischargeData_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBoxDischargeData_1, 20, 1, 1, 4)

        self.labelDischarge_data_1 = QLabel(self.frame_discharge_details)
        self.labelDischarge_data_1.setObjectName(u"labelDischarge_data_1")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelDischarge_data_1.setPalette(palette10)
        self.labelDischarge_data_1.setFont(font1)
        self.labelDischarge_data_1.setLayoutDirection(Qt.LeftToRight)
        self.labelDischarge_data_1.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelDischarge_data_1, 20, 0, 1, 1)

        self.label_referring_health_facility = QLabel(self.frame_discharge_details)
        self.label_referring_health_facility.setObjectName(u"label_referring_health_facility")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.label_referring_health_facility.setPalette(palette11)
        self.label_referring_health_facility.setFont(font1)
        self.label_referring_health_facility.setLayoutDirection(Qt.LeftToRight)
        self.label_referring_health_facility.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_referring_health_facility, 4, 0, 1, 1)

        self.label_department_head = QLabel(self.frame_discharge_details)
        self.label_department_head.setObjectName(u"label_department_head")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.label_department_head.setPalette(palette12)
        self.label_department_head.setFont(font1)
        self.label_department_head.setLayoutDirection(Qt.LeftToRight)
        self.label_department_head.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_department_head, 23, 0, 1, 1)

        self.comboBoxDischargeData_3 = QComboBox(self.frame_discharge_details)
        self.comboBoxDischargeData_3.addItem("")
        self.comboBoxDischargeData_3.addItem("")
        self.comboBoxDischargeData_3.addItem("")
        self.comboBoxDischargeData_3.addItem("")
        self.comboBoxDischargeData_3.addItem("")
        self.comboBoxDischargeData_3.setObjectName(u"comboBoxDischargeData_3")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBoxDischargeData_3.setPalette(palette13)
        self.comboBoxDischargeData_3.setFont(font1)
        self.comboBoxDischargeData_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBoxDischargeData_3, 22, 1, 1, 4)

        self.timeEditPtAdmissionTime = QTimeEdit(self.frame_discharge_details)
        self.timeEditPtAdmissionTime.setObjectName(u"timeEditPtAdmissionTime")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.timeEditPtAdmissionTime.setPalette(palette14)
        self.timeEditPtAdmissionTime.setFont(font1)
        self.timeEditPtAdmissionTime.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.timeEditPtAdmissionTime, 7, 2, 1, 1)

        self.labelPtHoptitalisationType = QLabel(self.frame_discharge_details)
        self.labelPtHoptitalisationType.setObjectName(u"labelPtHoptitalisationType")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtHoptitalisationType.setPalette(palette15)
        self.labelPtHoptitalisationType.setFont(font1)
        self.labelPtHoptitalisationType.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtHoptitalisationType, 3, 0, 1, 1)

        self.dateEditDischargeDate = QDateEdit(self.frame_discharge_details)
        self.dateEditDischargeDate.setObjectName(u"dateEditDischargeDate")
        self.dateEditDischargeDate.setFont(font1)
        self.dateEditDischargeDate.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.dateEditDischargeDate, 13, 1, 1, 1)

        self.labelDischarge_data_3 = QLabel(self.frame_discharge_details)
        self.labelDischarge_data_3.setObjectName(u"labelDischarge_data_3")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelDischarge_data_3.setPalette(palette16)
        self.labelDischarge_data_3.setFont(font1)
        self.labelDischarge_data_3.setLayoutDirection(Qt.LeftToRight)
        self.labelDischarge_data_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelDischarge_data_3, 22, 0, 1, 1)

        self.label_room_number = QLabel(self.frame_discharge_details)
        self.label_room_number.setObjectName(u"label_room_number")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.label_room_number.setPalette(palette17)
        self.label_room_number.setFont(font1)
        self.label_room_number.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_room_number, 2, 0, 1, 1)

        self.label_mkb = QLabel(self.frame_discharge_details)
        self.label_mkb.setObjectName(u"label_mkb")
        self.label_mkb.setMinimumSize(QSize(0, 20))
        self.label_mkb.setFont(font)

        self.gridLayout.addWidget(self.label_mkb, 16, 1, 1, 4)

        self.lineEdit_room_number = QLineEdit(self.frame_discharge_details)
        self.lineEdit_room_number.setObjectName(u"lineEdit_room_number")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.lineEdit_room_number.setPalette(palette18)
        self.lineEdit_room_number.setFont(font1)
        self.lineEdit_room_number.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_room_number, 2, 1, 1, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 14, 2, 1, 1)

        self.label_history_number = QLabel(self.frame_discharge_details)
        self.label_history_number.setObjectName(u"label_history_number")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette19.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette19.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette19.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette19.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.label_history_number.setPalette(palette19)
        self.label_history_number.setFont(font1)
        self.label_history_number.setLayoutDirection(Qt.LeftToRight)
        self.label_history_number.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_history_number, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 6, 2, 1, 1)

        self.label_nmu = QLabel(self.frame_discharge_details)
        self.label_nmu.setObjectName(u"label_nmu")
        self.label_nmu.setMinimumSize(QSize(0, 20))
        self.label_nmu.setFont(font)

        self.gridLayout.addWidget(self.label_nmu, 18, 1, 1, 4)

        self.comboBoxDischargeData_2 = QComboBox(self.frame_discharge_details)
        self.comboBoxDischargeData_2.addItem("")
        self.comboBoxDischargeData_2.addItem("")
        self.comboBoxDischargeData_2.addItem("")
        self.comboBoxDischargeData_2.addItem("")
        self.comboBoxDischargeData_2.addItem("")
        self.comboBoxDischargeData_2.addItem("")
        self.comboBoxDischargeData_2.setObjectName(u"comboBoxDischargeData_2")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBoxDischargeData_2.setPalette(palette20)
        self.comboBoxDischargeData_2.setFont(font1)
        self.comboBoxDischargeData_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBoxDischargeData_2, 21, 1, 1, 4)

        self.dateEditPtAdmissionDay = QDateEdit(self.frame_discharge_details)
        self.dateEditPtAdmissionDay.setObjectName(u"dateEditPtAdmissionDay")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.dateEditPtAdmissionDay.setPalette(palette21)
        self.dateEditPtAdmissionDay.setFont(font1)
        self.dateEditPtAdmissionDay.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.dateEditPtAdmissionDay.setTimeSpec(Qt.LocalTime)

        self.gridLayout.addWidget(self.dateEditPtAdmissionDay, 7, 1, 1, 1)

        self.comboBox_referring_health_facility = QComboBox(self.frame_discharge_details)
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.addItem("")
        self.comboBox_referring_health_facility.setObjectName(u"comboBox_referring_health_facility")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBox_referring_health_facility.setPalette(palette22)
        self.comboBox_referring_health_facility.setFont(font1)
        self.comboBox_referring_health_facility.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_referring_health_facility.setEditable(True)

        self.gridLayout.addWidget(self.comboBox_referring_health_facility, 4, 1, 1, 4)

        self.comboBoxTherapist = QComboBox(self.frame_discharge_details)
        self.comboBoxTherapist.addItem("")
        self.comboBoxTherapist.addItem("")
        self.comboBoxTherapist.addItem("")
        self.comboBoxTherapist.addItem("")
        self.comboBoxTherapist.addItem("")
        self.comboBoxTherapist.addItem("")
        self.comboBoxTherapist.setObjectName(u"comboBoxTherapist")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBoxTherapist.setPalette(palette23)
        self.comboBoxTherapist.setFont(font1)
        self.comboBoxTherapist.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxTherapist.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxTherapist, 24, 1, 1, 4)

        self.lineEdit_history_number = QLineEdit(self.frame_discharge_details)
        self.lineEdit_history_number.setObjectName(u"lineEdit_history_number")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.lineEdit_history_number.setPalette(palette24)
        self.lineEdit_history_number.setFont(font1)
        self.lineEdit_history_number.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_history_number, 1, 1, 1, 4)

        self.labelTherapist = QLabel(self.frame_discharge_details)
        self.labelTherapist.setObjectName(u"labelTherapist")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette25.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette25.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette25.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette25.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette25.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelTherapist.setPalette(palette25)
        self.labelTherapist.setFont(font1)
        self.labelTherapist.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelTherapist, 24, 0, 1, 1)

        self.comboBoxPtNMU_code = QComboBox(self.frame_discharge_details)
        self.comboBoxPtNMU_code.setObjectName(u"comboBoxPtNMU_code")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBoxPtNMU_code.setPalette(palette26)
        self.comboBoxPtNMU_code.setFont(font1)
        self.comboBoxPtNMU_code.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtNMU_code.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxPtNMU_code, 17, 1, 1, 4)

        self.dateEditDischargeDate_plan = QDateEdit(self.frame_discharge_details)
        self.dateEditDischargeDate_plan.setObjectName(u"dateEditDischargeDate_plan")
        self.dateEditDischargeDate_plan.setFont(font1)
        self.dateEditDischargeDate_plan.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.dateEditDischargeDate_plan, 12, 1, 1, 1)

        self.comboBox_department_head = QComboBox(self.frame_discharge_details)
        self.comboBox_department_head.addItem("")
        self.comboBox_department_head.addItem("")
        self.comboBox_department_head.addItem("")
        self.comboBox_department_head.addItem("")
        self.comboBox_department_head.setObjectName(u"comboBox_department_head")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette27.setBrush(QPalette.Active, QPalette.Light, brush)
        palette27.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette27.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush18)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette27.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette27.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.comboBox_department_head.setPalette(palette27)
        self.comboBox_department_head.setFont(font1)
        self.comboBox_department_head.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_department_head.setEditable(True)

        self.gridLayout.addWidget(self.comboBox_department_head, 23, 1, 1, 4)

        self.label_3 = QLabel(self.frame_discharge_details)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.comboBox_bedprofile = QComboBox(self.frame_discharge_details)
        self.comboBox_bedprofile.setObjectName(u"comboBox_bedprofile")
        self.comboBox_bedprofile.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBox_bedprofile, 5, 1, 1, 4)


        self.gridLayout_3.addWidget(self.frame_discharge_details, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.pt_info_block = QFrame(self.main)
        self.pt_info_block.setObjectName(u"pt_info_block")
        self.pt_info_block.setMaximumSize(QSize(16777215, 50))
        self.pt_info_block.setStyleSheet(u"background-color: transparent;")
        self.pt_info_block.setFrameShape(QFrame.NoFrame)
        self.pt_info_block.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.pt_info_block)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_Pt_info = QLabel(self.pt_info_block)
        self.label_Pt_info.setObjectName(u"label_Pt_info")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_Pt_info.setFont(font2)
        self.label_Pt_info.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: 13242B;\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")

        self.horizontalLayout_3.addWidget(self.label_Pt_info)

        self.labelTimeline = QLabel(self.pt_info_block)
        self.labelTimeline.setObjectName(u"labelTimeline")
        self.labelTimeline.setMaximumSize(QSize(80, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setItalic(False)
        self.labelTimeline.setFont(font3)
        self.labelTimeline.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(92, 158, 173, 200)\n"
"")
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/moving_beds_FILL0_wght400_GRAD0_opsz48.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTimeline)


        self.gridLayout_3.addWidget(self.pt_info_block, 0, 0, 1, 3)


        self.horizontalLayout_2.addLayout(self.gridLayout_3)

        self.groupBox_wom = QGroupBox(self.main)
        self.groupBox_wom.setObjectName(u"groupBox_wom")
        self.groupBox_wom.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);\n"
"")
        self.groupBox_wom.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_wom)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 20, 5, 5)
        self.pushButtonHelp = QPushButton(self.groupBox_wom)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        self.pushButtonHelp.setEnabled(False)
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush19 = QBrush(QColor(50, 98, 115, 190))
        brush19.setStyle(Qt.SolidPattern)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette28.setBrush(QPalette.Active, QPalette.Light, brush)
        palette28.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette28.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush)
        palette28.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette28.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette28.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette28.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette28.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette28.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette28.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        brush20 = QBrush(QColor(50, 98, 115, 150))
        brush20.setStyle(Qt.SolidPattern)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush20)
        brush21 = QBrush(QColor(50, 98, 115, 40))
        brush21.setStyle(Qt.SolidPattern)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush21)
        palette28.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette28.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush20)
        palette28.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush20)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush21)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush21)
        palette28.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette28.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
        brush22 = QBrush(QColor(50, 98, 115, 75))
        brush22.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.pushButtonHelp.setPalette(palette28)
        self.pushButtonHelp.setFont(font2)
        self.pushButtonHelp.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHelp.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.pushButtonHelp)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.pushButtonNotSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette29.setBrush(QPalette.Active, QPalette.Light, brush)
        palette29.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette29.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette29.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette29.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette29.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette29.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette29.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette29.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette29.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette29.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette29.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette29.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette29.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette29.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette29.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonNotSaveExit.setPalette(palette29)
        self.pushButtonNotSaveExit.setFont(font2)
        self.pushButtonNotSaveExit.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
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
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon2)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush23 = QBrush(QColor(92, 158, 173, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush23)
        palette30.setBrush(QPalette.Active, QPalette.Light, brush)
        palette30.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette30.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush)
        palette30.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush23)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush23)
        palette30.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette30.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush23)
        palette30.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush23)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush23)
        palette30.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonSaveExit.setPalette(palette30)
        self.pushButtonSaveExit.setFont(font2)
        self.pushButtonSaveExit.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
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
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveExit.setIcon(icon3)
        self.pushButtonSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonSaveExit)


        self.horizontalLayout_2.addWidget(self.groupBox_wom)


        self.verticalLayout.addWidget(self.main)

        QWidget.setTabOrder(self.lineEdit_history_number, self.lineEdit_room_number)
        QWidget.setTabOrder(self.lineEdit_room_number, self.comboBoxPtHoptitalisationType)
        QWidget.setTabOrder(self.comboBoxPtHoptitalisationType, self.comboBox_referring_health_facility)
        QWidget.setTabOrder(self.comboBox_referring_health_facility, self.dateEditPtAdmissionDay)
        QWidget.setTabOrder(self.dateEditPtAdmissionDay, self.timeEditPtAdmissionTime)
        QWidget.setTabOrder(self.timeEditPtAdmissionTime, self.dateEditDischargeDate_plan)
        QWidget.setTabOrder(self.dateEditDischargeDate_plan, self.dateEditDischargeDate)
        QWidget.setTabOrder(self.dateEditDischargeDate, self.timeEditDischargeTime)
        QWidget.setTabOrder(self.timeEditDischargeTime, self.comboBoxPtMKB10_main)
        QWidget.setTabOrder(self.comboBoxPtMKB10_main, self.comboBoxPtNMU_code)
        QWidget.setTabOrder(self.comboBoxPtNMU_code, self.comboBoxDischargeData_1)
        QWidget.setTabOrder(self.comboBoxDischargeData_1, self.comboBoxDischargeData_2)
        QWidget.setTabOrder(self.comboBoxDischargeData_2, self.comboBoxDischargeData_3)
        QWidget.setTabOrder(self.comboBoxDischargeData_3, self.comboBox_department_head)
        QWidget.setTabOrder(self.comboBox_department_head, self.comboBoxTherapist)
        QWidget.setTabOrder(self.comboBoxTherapist, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.pushButtonNotSaveExit)
        QWidget.setTabOrder(self.pushButtonNotSaveExit, self.checkBox_dis)
        QWidget.setTabOrder(self.checkBox_dis, self.pushButtonDischarge_and_close_history)
        QWidget.setTabOrder(self.pushButtonDischarge_and_close_history, self.pushButtonHelp)

        self.retranslateUi(Dis_details)

        QMetaObject.connectSlotsByName(Dis_details)
    # setupUi

    def retranslateUi(self, Dis_details):
        Dis_details.setWindowTitle(QCoreApplication.translate("Dis_details", u"Form", None))
        self.label_dis.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"center\">NB! \u0414\u0430\u043d\u043d\u043e\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u043d\u0435\u043b\u044c\u0437\u044f \u043e\u0442\u043c\u0435\u043d\u0438\u0442\u044c!</p></body></html>", None))
        self.checkBox_dis.setText(QCoreApplication.translate("Dis_details", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u044e \u0432\u044b\u043f\u0438\u0441\u043a\u0443", None))
        self.label_2.setText(QCoreApplication.translate("Dis_details", u"\u0412\u044b\u043f\u0438\u0441\u043a\u0430 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonDischarge_and_close_history.setText(QCoreApplication.translate("Dis_details", u"\u0412\u044b\u043f\u0438\u0441\u0430\u0442\u044c \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 \u0438 \u0437\u0430\u043a\u0440\u044b\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u0431\u043e\u043b\u0435\u0437\u043d\u0438", None))
        self.labelPtNMU_code.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u041a\u043e\u0434 \u043c\u0435\u0434.\u0443\u0441\u043b\u0443\u0433\u0438:</p></body></html>", None))
        self.labelPtMKB10_main.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p>\u041a\u043e\u0434 \u041c\u041a\u0411-10:</p></body></html>", None))
        self.labelPtAdmissionDay.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f:</p></body></html>", None))
        self.comboBoxPtHoptitalisationType.setItemText(0, QCoreApplication.translate("Dis_details", u"\u041a\u0440\u0443\u0433\u043b\u043e\u0441\u0443\u0442\u043e\u0447\u043d\u044b\u0439 \u0441\u0442\u0430\u0446\u0438\u043e\u043d\u0430\u0440", None))
        self.comboBoxPtHoptitalisationType.setItemText(1, QCoreApplication.translate("Dis_details", u"\u0414\u043d\u0435\u0432\u043d\u043e\u0439 \u0441\u0442\u0430\u0446\u0438\u043e\u043d\u0430\u0440", None))
        self.comboBoxPtHoptitalisationType.setItemText(2, QCoreApplication.translate("Dis_details", u"\u0411\u0422 - \u043a\u0440\u0443\u0433\u043b\u043e\u0441\u0443\u0442\u043e\u0447\u043d\u044b\u0439", None))
        self.comboBoxPtHoptitalisationType.setItemText(3, QCoreApplication.translate("Dis_details", u"\u0411\u0422 - \u0434\u043d\u0435\u0432\u043d\u043e\u0439", None))

        self.labelDischarge_data_2.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440 \u0432\u044b\u043f\u0438\u0441\u043a\u0438:</p></body></html>", None))
        self.labelPtDischargeDate.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u0438\u0441\u043a\u0438:</p></body></html>", None))
        self.labelPtDischargeDate_plan.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u0438\u0441\u043a\u0438 (\u043f\u043b\u0430\u043d.):</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dis_details", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0432\u044b\u043f\u0438\u0441\u043a\u0438, \u0441\u0440\u043e\u043a\u0438 \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.comboBoxDischargeData_1.setItemText(0, QCoreApplication.translate("Dis_details", u"\u0432\u044b\u043f\u0438\u0441\u043a\u0430", None))
        self.comboBoxDischargeData_1.setItemText(1, QCoreApplication.translate("Dis_details", u"\u043f\u0435\u0440\u0435\u0432\u043e\u0434 \u0432 \u0434\u0440\u0443\u0433\u043e\u0435 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.comboBoxDischargeData_1.setItemText(2, QCoreApplication.translate("Dis_details", u"\u043f\u0435\u0440\u0435\u0432\u043e\u0434 \u0432 \u0434\u0440\u0443\u0433\u0443\u044e \u041c\u041e", None))
        self.comboBoxDischargeData_1.setItemText(3, QCoreApplication.translate("Dis_details", u"\u0441\u043c\u0435\u0440\u0442\u044c", None))

        self.labelDischarge_data_1.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u0412\u0438\u0434 \u0432\u044b\u0431\u044b\u0442\u0438\u044f:</p></body></html>", None))
        self.label_referring_health_facility.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u041d\u0430\u043f\u0440\u0430\u0432\u0438\u0432\u0448\u0435\u0435 \u041b\u041f\u0423:</p></body></html>", None))
        self.label_department_head.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u0417\u0430\u0432.\u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435\u043c:</p></body></html>", None))
        self.comboBoxDischargeData_3.setItemText(0, QCoreApplication.translate("Dis_details", u"\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u0434\u0438\u043d\u0430\u043c\u0438\u043a\u0438", None))
        self.comboBoxDischargeData_3.setItemText(1, QCoreApplication.translate("Dis_details", u"\u0441 \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u0435\u043c", None))
        self.comboBoxDischargeData_3.setItemText(2, QCoreApplication.translate("Dis_details", u"\u0441 \u0443\u0445\u0443\u0434\u0448\u0435\u043d\u0438\u0435\u043c", None))
        self.comboBoxDischargeData_3.setItemText(3, QCoreApplication.translate("Dis_details", u"\u0432\u044b\u0437\u0434\u043e\u0440\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.comboBoxDischargeData_3.setItemText(4, QCoreApplication.translate("Dis_details", u"\u0441\u043c\u0435\u0440\u0442\u044c", None))

        self.labelPtHoptitalisationType.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u0422\u0438\u043f \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438:</p></body></html>", None))
        self.labelDischarge_data_3.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u0418\u0442\u043e\u0433 \u0432\u044b\u043f\u0438\u0441\u043a\u0438:</p></body></html>", None))
        self.label_room_number.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u043b\u0430\u0442\u044b:</p></body></html>", None))
        self.label_mkb.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"center\">-</p></body></html>", None))
        self.label_history_number.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u041d\u043e\u043c\u0435\u0440 \u0418\u0411:</p></body></html>", None))
        self.label_nmu.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"center\">-</p></body></html>", None))
        self.comboBoxDischargeData_2.setItemText(0, QCoreApplication.translate("Dis_details", u"\u043f\u043b\u0430\u043d\u043e\u0432\u043e", None))
        self.comboBoxDischargeData_2.setItemText(1, QCoreApplication.translate("Dis_details", u"\u043f\u043e \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0439 \u0438\u043d\u0438\u0446\u0438\u0430\u0442\u0438\u0432\u0435", None))
        self.comboBoxDischargeData_2.setItemText(2, QCoreApplication.translate("Dis_details", u"\u043f\u043e \u044d\u043f\u0438\u0434.\u043f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f\u043c", None))
        self.comboBoxDischargeData_2.setItemText(3, QCoreApplication.translate("Dis_details", u"\u0441\u0430\u043c\u043e\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u0443\u0445\u043e\u0434", None))
        self.comboBoxDischargeData_2.setItemText(4, QCoreApplication.translate("Dis_details", u"\u043f\u043e \u044d\u043a\u0441\u0442\u0440\u0435\u043d\u043d\u044b\u043c \u043f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f\u043c", None))
        self.comboBoxDischargeData_2.setItemText(5, QCoreApplication.translate("Dis_details", u"\u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0435 \u0432\u043d\u0443\u0442\u0440\u0438\u0431\u043e\u043b\u044c\u043d\u0438\u0447\u043d\u043e\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u0430", None))

        self.dateEditPtAdmissionDay.setDisplayFormat(QCoreApplication.translate("Dis_details", u"dd.MM.yyyy", None))
        self.comboBox_referring_health_facility.setItemText(0, "")
        self.comboBox_referring_health_facility.setItemText(1, QCoreApplication.translate("Dis_details", u"\u043f\u043e\u043b\u0438\u043a\u043b\u0438\u043d\u0438\u043a\u0430 \u0413\u041a\u0411 \u0438\u043c.\u0421.\u041d.\u0413\u0440\u0438\u043d\u0431\u0435\u0440\u0433\u0430", None))
        self.comboBox_referring_health_facility.setItemText(2, QCoreApplication.translate("Dis_details", u"\u0413\u041a\u041f 2", None))
        self.comboBox_referring_health_facility.setItemText(3, QCoreApplication.translate("Dis_details", u"\u043d\u0435\u0432\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0413\u041a\u0411 \u0438\u043c.\u0421.\u041d.\u0413\u0440\u0438\u043d\u0431\u0435\u0440\u0433\u0430", None))
        self.comboBox_referring_health_facility.setItemText(4, QCoreApplication.translate("Dis_details", u"\u043d\u0435\u0432\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0413\u041a\u0411 \u0438\u043c.\u041c.\u0410.\u0422\u0432\u0435\u0440\u044c\u0435", None))
        self.comboBox_referring_health_facility.setItemText(5, QCoreApplication.translate("Dis_details", u"\u041a\u0440\u0430\u0441\u043d\u043e\u043a\u0430\u043c\u0441\u043a\u0430\u044f \u0413\u0411", None))
        self.comboBox_referring_health_facility.setItemText(6, QCoreApplication.translate("Dis_details", u"\u041d\u044b\u0442\u0432\u0435\u043d\u0441\u043a\u0430\u044f \u0420\u0411", None))
        self.comboBox_referring_health_facility.setItemText(7, QCoreApplication.translate("Dis_details", u"\u0411\u043e\u043b\u044c\u0448\u0435\u0441\u043e\u0441\u043d\u043e\u0432\u0441\u043a\u0430\u044f \u0426\u0420\u0411", None))
        self.comboBox_referring_health_facility.setItemText(8, QCoreApplication.translate("Dis_details", u"\u041e\u0441\u0438\u043d\u0441\u043a\u0430\u044f \u0426\u0420\u0411", None))
        self.comboBox_referring_health_facility.setItemText(9, QCoreApplication.translate("Dis_details", u"\u0411\u0430\u0440\u0434\u044b\u043c\u0441\u043a\u0430\u044f \u0426\u0420\u0411", None))
        self.comboBox_referring_health_facility.setItemText(10, QCoreApplication.translate("Dis_details", u"\u041e\u0440\u0434\u0438\u043d\u0441\u043a\u0430\u044f \u0426\u0420\u0411", None))

        self.comboBoxTherapist.setItemText(0, QCoreApplication.translate("Dis_details", u"\u0428\u0438\u043b\u043e\u0432 \u0418.\u0421.", None))
        self.comboBoxTherapist.setItemText(1, QCoreApplication.translate("Dis_details", u"\u0422\u044b\u0440\u0438\u0447\u0435\u0432 \u0421.\u0412.", None))
        self.comboBoxTherapist.setItemText(2, QCoreApplication.translate("Dis_details", u"\u0428\u0430\u0434\u0440\u0438\u043d \u0410.\u0410.", None))
        self.comboBoxTherapist.setItemText(3, QCoreApplication.translate("Dis_details", u"\u0422\u0438\u043c\u043e\u0444\u0435\u0435\u0432 \u0410.\u041f.", None))
        self.comboBoxTherapist.setItemText(4, QCoreApplication.translate("Dis_details", u"\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0430 \u0412.\u0412.", None))
        self.comboBoxTherapist.setItemText(5, QCoreApplication.translate("Dis_details", u"\u0421\u0435\u043b\u0435\u0437\u043d\u0451\u0432\u0430 \u0421.\u0418.", None))

        self.labelTherapist.setText(QCoreApplication.translate("Dis_details", u"<html><head/><body><p align=\"right\">\u041b\u0435\u0447\u0430\u0449\u0438\u0439 \u0432\u0440\u0430\u0447:</p></body></html>", None))
        self.comboBox_department_head.setItemText(0, QCoreApplication.translate("Dis_details", u"\u0422\u044b\u0440\u0438\u0447\u0435\u0432 \u0421.\u0412.", None))
        self.comboBox_department_head.setItemText(1, QCoreApplication.translate("Dis_details", u"\u0418.\u041e.\u0417.\u041e. - \u0422\u0438\u043c\u043e\u0444\u0435\u0435\u0432 \u0410.\u041f.", None))
        self.comboBox_department_head.setItemText(2, QCoreApplication.translate("Dis_details", u"\u0418.\u041e.\u0417.\u041e. - \u0428\u0430\u0434\u0440\u0438\u043d \u0410.\u0410.", None))
        self.comboBox_department_head.setItemText(3, QCoreApplication.translate("Dis_details", u"\u0418.\u041e.\u0417.\u041e. - \u0428\u0438\u043b\u043e\u0432 \u0418.\u0421.", None))

        self.label_3.setText(QCoreApplication.translate("Dis_details", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u043a\u043e\u0435\u043a:", None))
        self.label_Pt_info.setText(QCoreApplication.translate("Dis_details", u"PatientInfo\n"
"fff", None))
        self.labelTimeline.setText("")
        self.groupBox_wom.setTitle(QCoreApplication.translate("Dis_details", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("Dis_details", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("Dis_details", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("Dis_details", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
    # retranslateUi

