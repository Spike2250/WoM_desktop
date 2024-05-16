# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'omr_Appointments.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc

class Ui_Appointments(object):
    def setupUi(self, Appointments):
        if not Appointments.objectName():
            Appointments.setObjectName(u"Appointments")
        Appointments.resize(1282, 649)
        Appointments.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_7 = QVBoxLayout(Appointments)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(Appointments)
        self.main.setObjectName(u"main")
        self.gridLayout_2 = QGridLayout(self.main)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pt_info_block = QFrame(self.main)
        self.pt_info_block.setObjectName(u"pt_info_block")
        self.pt_info_block.setStyleSheet(u"background-color: transparent;")
        self.pt_info_block.setFrameShape(QFrame.NoFrame)
        self.pt_info_block.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.pt_info_block)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_Pt_info = QLabel(self.pt_info_block)
        self.label_Pt_info.setObjectName(u"label_Pt_info")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(True)
        self.label_Pt_info.setFont(font)
        self.label_Pt_info.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: 13242B;\n"
"font-size: 11pt;\n"
"font-weight: bold;\n"
"border: 1px solid rgba(50, 98, 115, 255);")

        self.horizontalLayout_3.addWidget(self.label_Pt_info)

        self.labelTimeline = QLabel(self.pt_info_block)
        self.labelTimeline.setObjectName(u"labelTimeline")
        self.labelTimeline.setMaximumSize(QSize(80, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        self.labelTimeline.setFont(font1)
        self.labelTimeline.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(92, 158, 173, 200)\n"
"")
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/assignment_white_36dp.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTimeline)


        self.gridLayout_2.addWidget(self.pt_info_block, 0, 0, 1, 1)

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
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(50, 98, 115, 190))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush2 = QBrush(QColor(236, 236, 236, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(108, 108, 108, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(145, 145, 145, 255))
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
        brush8 = QBrush(QColor(50, 98, 115, 150))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        brush9 = QBrush(QColor(50, 98, 115, 40))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        brush10 = QBrush(QColor(217, 217, 217, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
        brush11 = QBrush(QColor(50, 98, 115, 75))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButtonHelp.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(False)
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
        icon = QIcon()
        icon.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHelp.setIcon(icon)

        self.verticalLayout_6.addWidget(self.pushButtonHelp)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.pushButtonNotSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        brush12 = QBrush(QColor(237, 237, 237, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        brush13 = QBrush(QColor(110, 110, 110, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush13)
        brush14 = QBrush(QColor(147, 147, 147, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush15 = QBrush(QColor(238, 238, 238, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        brush16 = QBrush(QColor(220, 220, 220, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonNotSaveExit.setPalette(palette1)
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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon1)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush17 = QBrush(QColor(92, 158, 173, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonSaveExit.setPalette(palette2)
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveExit.setIcon(icon2)
        self.pushButtonSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonSaveExit)


        self.gridLayout_2.addWidget(self.groupBox_wom, 0, 1, 3, 1)

        self.tabWidget = QTabWidget(self.main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget:pane {\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
"color: White;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 1px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QTabBar::tab:disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(32, 32))
        self.tabWidget.setTabsClosable(False)
        self.drugs = QWidget()
        self.drugs.setObjectName(u"drugs")
        self.horizontalLayout = QHBoxLayout(self.drugs)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.drugs)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setVerticalSpacing(1)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_diet = QLabel(self.frame_2)
        self.label_diet.setObjectName(u"label_diet")
        self.label_diet.setMaximumSize(QSize(80, 16777215))
        palette3 = QPalette()
        brush18 = QBrush(QColor(50, 98, 115, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        brush19 = QBrush(QColor(0, 0, 0, 0))
        brush19.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
        brush20 = QBrush(QColor(50, 98, 115, 128))
        brush20.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.label_diet.setPalette(palette3)
        self.label_diet.setFont(font)
        self.label_diet.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_diet, 0, 0, 1, 1)

        self.tableWidget_peros = QTableWidget(self.frame_2)
        if (self.tableWidget_peros.columnCount() < 5):
            self.tableWidget_peros.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_peros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_peros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_peros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_peros.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_peros.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_peros.setObjectName(u"tableWidget_peros")
        self.tableWidget_peros.setMinimumSize(QSize(0, 300))
        self.tableWidget_peros.setFont(font2)
        self.tableWidget_peros.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"   background-color: rgba(50, 98, 115, 220);\n"
"   color: #FFFFFF;\n"
"   font-family: Roboto;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #13242B;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"   border-style: none;\n"
"   border-bottom: #13242B;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: rgba(50, 98, 115, 70);\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.tableWidget_peros, 6, 0, 1, 5)

        self.tableWidget_sol = QTableWidget(self.frame_2)
        if (self.tableWidget_sol.columnCount() < 5):
            self.tableWidget_sol.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_sol.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_sol.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_sol.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_sol.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_sol.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_sol.setObjectName(u"tableWidget_sol")
        self.tableWidget_sol.setMinimumSize(QSize(0, 0))
        self.tableWidget_sol.setFont(font2)
        self.tableWidget_sol.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"   background-color: rgba(50, 98, 115, 220);\n"
"   color: #FFFFFF;\n"
"   font-family: Roboto;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #13242B;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"   border-style: none;\n"
"   border-bottom: #13242B;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: rgba(50, 98, 115, 70);\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.tableWidget_sol, 3, 0, 1, 5)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 4, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(180, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 2, 1, 2)

        self.comboBox_diet = QComboBox(self.frame_2)
        self.comboBox_diet.addItem("")
        self.comboBox_diet.addItem("")
        self.comboBox_diet.addItem("")
        self.comboBox_diet.addItem("")
        self.comboBox_diet.addItem("")
        self.comboBox_diet.setObjectName(u"comboBox_diet")
        self.comboBox_diet.setMaximumSize(QSize(150, 16777215))
        palette4 = QPalette()
        brush21 = QBrush(QColor(19, 36, 43, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        brush22 = QBrush(QColor(19, 36, 43, 128))
        brush22.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_diet.setPalette(palette4)
        self.comboBox_diet.setFont(font)
        self.comboBox_diet.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_diet.setEditable(True)

        self.gridLayout_5.addWidget(self.comboBox_diet, 0, 1, 1, 1)

        self.comboBox_functional_mode = QComboBox(self.frame_2)
        self.comboBox_functional_mode.addItem("")
        self.comboBox_functional_mode.addItem("")
        self.comboBox_functional_mode.addItem("")
        self.comboBox_functional_mode.setObjectName(u"comboBox_functional_mode")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_functional_mode.setPalette(palette5)
        self.comboBox_functional_mode.setFont(font)
        self.comboBox_functional_mode.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_functional_mode.setEditable(True)

        self.gridLayout_5.addWidget(self.comboBox_functional_mode, 1, 1, 1, 1)

        self.label_functional_mode = QLabel(self.frame_2)
        self.label_functional_mode.setObjectName(u"label_functional_mode")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.label_functional_mode.setPalette(palette6)
        self.label_functional_mode.setFont(font)
        self.label_functional_mode.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_functional_mode, 1, 0, 1, 1)

        self.label_Injections = QLabel(self.frame_2)
        self.label_Injections.setObjectName(u"label_Injections")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush23 = QBrush(QColor(112, 38, 50, 150))
        brush23.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush23)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush23)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush23)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush23)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush23)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush23)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush23)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush23)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush23)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_Injections.setPalette(palette7)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_Injections.setFont(font3)
        self.label_Injections.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_Injections.setTextFormat(Qt.AutoText)

        self.gridLayout_5.addWidget(self.label_Injections, 2, 0, 1, 5)

        self.label_PerOs = QLabel(self.frame_2)
        self.label_PerOs.setObjectName(u"label_PerOs")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush23)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush23)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush23)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush23)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush23)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush23)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush23)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush23)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush23)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_PerOs.setPalette(palette8)
        self.label_PerOs.setFont(font3)
        self.label_PerOs.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")

        self.gridLayout_5.addWidget(self.label_PerOs, 5, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 4, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.drugs)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.pushButton_add_and_continue = QPushButton(self.frame)
        self.pushButton_add_and_continue.setObjectName(u"pushButton_add_and_continue")
        self.pushButton_add_and_continue.setMinimumSize(QSize(0, 45))
        self.pushButton_add_and_continue.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(92, 158, 173, 190);\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/add_circle_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_and_continue.setIcon(icon3)
        self.pushButton_add_and_continue.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_add_and_continue, 10, 0, 1, 6)

        self.lineEdit_dose = QLineEdit(self.frame)
        self.lineEdit_dose.setObjectName(u"lineEdit_dose")
        self.lineEdit_dose.setMinimumSize(QSize(0, 0))
        self.lineEdit_dose.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_dose.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.lineEdit_dose.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit_dose, 7, 5, 1, 1)

        self.label_add_drug = QLabel(self.frame)
        self.label_add_drug.setObjectName(u"label_add_drug")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_add_drug.setFont(font4)
        self.label_add_drug.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")

        self.gridLayout.addWidget(self.label_add_drug, 0, 0, 1, 6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_set_adm_date = QPushButton(self.frame)
        self.pushButton_set_adm_date.setObjectName(u"pushButton_set_adm_date")
        self.pushButton_set_adm_date.setEnabled(True)
        self.pushButton_set_adm_date.setMinimumSize(QSize(140, 0))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButton_set_adm_date.setPalette(palette9)
        self.pushButton_set_adm_date.setFont(font2)
        self.pushButton_set_adm_date.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_set_adm_date)

        self.pushButton_set_today_date = QPushButton(self.frame)
        self.pushButton_set_today_date.setObjectName(u"pushButton_set_today_date")
        self.pushButton_set_today_date.setEnabled(True)
        self.pushButton_set_today_date.setMinimumSize(QSize(100, 0))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButton_set_today_date.setPalette(palette10)
        self.pushButton_set_today_date.setFont(font2)
        self.pushButton_set_today_date.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_set_today_date)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_clean = QPushButton(self.frame)
        self.pushButton_clean.setObjectName(u"pushButton_clean")
        self.pushButton_clean.setEnabled(True)
        self.pushButton_clean.setMinimumSize(QSize(115, 0))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButton_clean.setPalette(palette11)
        self.pushButton_clean.setFont(font2)
        self.pushButton_clean.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_clean)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 6)

        self.label_dose = QLabel(self.frame)
        self.label_dose.setObjectName(u"label_dose")
        self.label_dose.setMaximumSize(QSize(40, 16777215))
        self.label_dose.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_dose, 7, 4, 1, 1)

        self.label_DS = QLabel(self.frame)
        self.label_DS.setObjectName(u"label_DS")
        self.label_DS.setMaximumSize(QSize(25, 16777215))
        self.label_DS.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_DS, 8, 1, 2, 1)

        self.label_date = QLabel(self.frame)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_date, 6, 0, 1, 2)

        self.label_Rp = QLabel(self.frame)
        self.label_Rp.setObjectName(u"label_Rp")
        self.label_Rp.setMaximumSize(QSize(25, 16777215))
        self.label_Rp.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Rp, 7, 0, 1, 1)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
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
        self.checkBox.setChecked(False)

        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 5)

        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMaximumSize(QSize(16777215, 24))
        self.label_status.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_status, 6, 3, 1, 3)

        self.tableWidget_drugs = QTableWidget(self.frame)
        self.tableWidget_drugs.setObjectName(u"tableWidget_drugs")
        self.tableWidget_drugs.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"   background-color: rgba(50, 98, 115, 220);\n"
"   color: #FFFFFF;\n"
"   font-family: Roboto;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #13242B;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"   border-style: none;\n"
"   border-bottom: #13242B;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: rgba(50, 98, 115, 70);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.tableWidget_drugs, 3, 0, 1, 6)

        self.lineEdit_drug = QLineEdit(self.frame)
        self.lineEdit_drug.setObjectName(u"lineEdit_drug")
        self.lineEdit_drug.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.lineEdit_drug.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit_drug, 7, 1, 1, 3)

        self.pushButton_restart = QPushButton(self.frame)
        self.pushButton_restart.setObjectName(u"pushButton_restart")
        self.pushButton_restart.setMinimumSize(QSize(0, 25))
        self.pushButton_restart.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_restart, 2, 0, 1, 6)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.dateEdit, 6, 2, 1, 1)

        self.lineEdit_DS = QLineEdit(self.frame)
        self.lineEdit_DS.setObjectName(u"lineEdit_DS")
        self.lineEdit_DS.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_DS, 8, 2, 2, 4)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 3)


        self.horizontalLayout.addWidget(self.frame)

        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/vaccines_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.drugs, icon4, "")
        self.lkf = QWidget()
        self.lkf.setObjectName(u"lkf")
        self.verticalLayout_2 = QVBoxLayout(self.lkf)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_lfk = QFrame(self.lkf)
        self.add_lfk.setObjectName(u"add_lfk")
        self.add_lfk.setMaximumSize(QSize(16777215, 170))
        self.horizontalLayout_5 = QHBoxLayout(self.add_lfk)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.frame_3 = QFrame(self.add_lfk)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(550, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_lfk_regimen = QLabel(self.frame_3)
        self.label_lfk_regimen.setObjectName(u"label_lfk_regimen")
        self.label_lfk_regimen.setMaximumSize(QSize(16777215, 16777215))
        self.label_lfk_regimen.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_lfk_regimen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_lfk_regimen, 3, 0, 1, 1)

        self.label_lfk_ed = QLabel(self.frame_3)
        self.label_lfk_ed.setObjectName(u"label_lfk_ed")
        self.label_lfk_ed.setMaximumSize(QSize(40, 16777215))
        self.label_lfk_ed.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_lfk_ed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_lfk_ed, 3, 2, 1, 1)

        self.comboBox_lfk_duration = QComboBox(self.frame_3)
        self.comboBox_lfk_duration.addItem("")
        self.comboBox_lfk_duration.addItem("")
        self.comboBox_lfk_duration.addItem("")
        self.comboBox_lfk_duration.addItem("")
        self.comboBox_lfk_duration.setObjectName(u"comboBox_lfk_duration")
        self.comboBox_lfk_duration.setMaximumSize(QSize(16777215, 16777215))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_lfk_duration.setPalette(palette12)
        self.comboBox_lfk_duration.setFont(font)
        self.comboBox_lfk_duration.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_lfk_duration.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox_lfk_duration, 3, 1, 1, 1)

        self.label_add_lfk = QLabel(self.frame_3)
        self.label_add_lfk.setObjectName(u"label_add_lfk")
        self.label_add_lfk.setFont(font4)
        self.label_add_lfk.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_add_lfk.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_add_lfk, 0, 0, 1, 4)

        self.pushButton_add_lfk = QPushButton(self.frame_3)
        self.pushButton_add_lfk.setObjectName(u"pushButton_add_lfk")
        self.pushButton_add_lfk.setMinimumSize(QSize(0, 45))
        self.pushButton_add_lfk.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(92, 158, 173, 190);\n"
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
        self.pushButton_add_lfk.setIcon(icon3)
        self.pushButton_add_lfk.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.pushButton_add_lfk, 6, 0, 1, 4)

        self.comboBox_lfk_ed = QComboBox(self.frame_3)
        self.comboBox_lfk_ed.addItem("")
        self.comboBox_lfk_ed.addItem("")
        self.comboBox_lfk_ed.addItem("")
        self.comboBox_lfk_ed.addItem("")
        self.comboBox_lfk_ed.addItem("")
        self.comboBox_lfk_ed.addItem("")
        self.comboBox_lfk_ed.addItem("")
        self.comboBox_lfk_ed.addItem("")
        self.comboBox_lfk_ed.setObjectName(u"comboBox_lfk_ed")
        self.comboBox_lfk_ed.setMaximumSize(QSize(16777215, 16777215))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_lfk_ed.setPalette(palette13)
        self.comboBox_lfk_ed.setFont(font)
        self.comboBox_lfk_ed.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_lfk_ed.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox_lfk_ed, 3, 3, 1, 1)

        self.comboBox_lfk = QComboBox(self.frame_3)
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.addItem("")
        self.comboBox_lfk.setObjectName(u"comboBox_lfk")
        self.comboBox_lfk.setMaximumSize(QSize(16777215, 16777215))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_lfk.setPalette(palette14)
        self.comboBox_lfk.setFont(font)
        self.comboBox_lfk.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_lfk.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox_lfk, 2, 0, 1, 4)

        self.label_status_lfk = QLabel(self.frame_3)
        self.label_status_lfk.setObjectName(u"label_status_lfk")
        self.label_status_lfk.setMaximumSize(QSize(16777215, 24))
        self.label_status_lfk.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_status_lfk, 7, 0, 1, 4)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.frame_templates = QFrame(self.add_lfk)
        self.frame_templates.setObjectName(u"frame_templates")
        self.frame_templates.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_7 = QGridLayout(self.frame_templates)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setVerticalSpacing(1)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.comboBox_lfk_template = QComboBox(self.frame_templates)
        self.comboBox_lfk_template.addItem("")
        self.comboBox_lfk_template.setObjectName(u"comboBox_lfk_template")
        self.comboBox_lfk_template.setMaximumSize(QSize(16777215, 16777215))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_lfk_template.setPalette(palette15)
        self.comboBox_lfk_template.setFont(font)
        self.comboBox_lfk_template.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.comboBox_lfk_template, 2, 0, 1, 1)

        self.pushButton_lfk_add_new_template = QPushButton(self.frame_templates)
        self.pushButton_lfk_add_new_template.setObjectName(u"pushButton_lfk_add_new_template")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_lfk_add_new_template.setPalette(palette16)
        self.pushButton_lfk_add_new_template.setFont(font2)
        self.pushButton_lfk_add_new_template.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_7.addWidget(self.pushButton_lfk_add_new_template, 4, 1, 1, 1)

        self.label = QLabel(self.frame_templates)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 2)

        self.pushButton_lfk_push_temp = QPushButton(self.frame_templates)
        self.pushButton_lfk_push_temp.setObjectName(u"pushButton_lfk_push_temp")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_lfk_push_temp.setPalette(palette17)
        self.pushButton_lfk_push_temp.setFont(font2)
        self.pushButton_lfk_push_temp.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_7.addWidget(self.pushButton_lfk_push_temp, 2, 1, 1, 1)

        self.lineEdit_lfk_new_template_name = QLineEdit(self.frame_templates)
        self.lineEdit_lfk_new_template_name.setObjectName(u"lineEdit_lfk_new_template_name")
        self.lineEdit_lfk_new_template_name.setMinimumSize(QSize(350, 0))
        self.lineEdit_lfk_new_template_name.setFont(font)
        self.lineEdit_lfk_new_template_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_lfk_new_template_name, 4, 0, 1, 1)

        self.label_3 = QLabel(self.frame_templates)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_templates)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_templates)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addWidget(self.add_lfk)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_lfk_md_2 = QLabel(self.lkf)
        self.label_lfk_md_2.setObjectName(u"label_lfk_md_2")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.label_lfk_md_2.setPalette(palette18)
        self.label_lfk_md_2.setFont(font)
        self.label_lfk_md_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_lfk_md_2)

        self.comboBox_lfk_name = QComboBox(self.lkf)
        self.comboBox_lfk_name.setObjectName(u"comboBox_lfk_name")
        self.comboBox_lfk_name.setMinimumSize(QSize(300, 0))
        self.comboBox_lfk_name.setMaximumSize(QSize(16777215, 20))
        self.comboBox_lfk_name.setFont(font)
        self.comboBox_lfk_name.setStyleSheet(u"QComboBox  {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QComboBox::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        self.comboBox_lfk_name.setEditable(True)

        self.horizontalLayout_4.addWidget(self.comboBox_lfk_name)

        self.checkBox_lfk_same = QCheckBox(self.lkf)
        self.checkBox_lfk_same.setObjectName(u"checkBox_lfk_same")
        self.checkBox_lfk_same.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"	font-size: 11pt;\n"
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
        self.checkBox_lfk_same.setChecked(False)

        self.horizontalLayout_4.addWidget(self.checkBox_lfk_same)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.tableWidget_lfk = QTableWidget(self.lkf)
        if (self.tableWidget_lfk.columnCount() < 4):
            self.tableWidget_lfk.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_lfk.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_lfk.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_lfk.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_lfk.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.tableWidget_lfk.setObjectName(u"tableWidget_lfk")
        self.tableWidget_lfk.setMinimumSize(QSize(900, 0))
        self.tableWidget_lfk.setFont(font2)
        self.tableWidget_lfk.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"   background-color: rgba(50, 98, 115, 220);\n"
"   color: #FFFFFF;\n"
"   font-family: Roboto;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #13242B;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"   border-style: none;\n"
"   border-bottom: #13242B;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: rgba(50, 98, 115, 70);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.tableWidget_lfk)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/conditions_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.lkf, icon5, "")
        self.physio = QWidget()
        self.physio.setObjectName(u"physio")
        self.verticalLayout_4 = QVBoxLayout(self.physio)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.physio_2 = QFrame(self.physio)
        self.physio_2.setObjectName(u"physio_2")
        self.physio_2.setMaximumSize(QSize(16777215, 170))
        self.horizontalLayout_7 = QHBoxLayout(self.physio_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.frame_4 = QFrame(self.physio_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(550, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_add_physio = QLabel(self.frame_4)
        self.label_add_physio.setObjectName(u"label_add_physio")
        self.label_add_physio.setFont(font4)
        self.label_add_physio.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_add_physio.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_add_physio, 0, 0, 1, 4)

        self.comboBox_physio_duration = QComboBox(self.frame_4)
        self.comboBox_physio_duration.addItem("")
        self.comboBox_physio_duration.addItem("")
        self.comboBox_physio_duration.addItem("")
        self.comboBox_physio_duration.addItem("")
        self.comboBox_physio_duration.addItem("")
        self.comboBox_physio_duration.setObjectName(u"comboBox_physio_duration")
        self.comboBox_physio_duration.setMaximumSize(QSize(16777215, 16777215))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_physio_duration.setPalette(palette19)
        self.comboBox_physio_duration.setFont(font)
        self.comboBox_physio_duration.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_physio_duration.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox_physio_duration, 3, 3, 1, 1)

        self.label_physio_place = QLabel(self.frame_4)
        self.label_physio_place.setObjectName(u"label_physio_place")
        self.label_physio_place.setMaximumSize(QSize(16777215, 16777215))
        self.label_physio_place.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_physio_place.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_physio_place, 3, 0, 1, 1)

        self.comboBox_physio_place = QComboBox(self.frame_4)
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.addItem("")
        self.comboBox_physio_place.setObjectName(u"comboBox_physio_place")
        self.comboBox_physio_place.setMaximumSize(QSize(16777215, 16777215))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_physio_place.setPalette(palette20)
        self.comboBox_physio_place.setFont(font)
        self.comboBox_physio_place.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_physio_place.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox_physio_place, 3, 1, 1, 1)

        self.label_status_physio = QLabel(self.frame_4)
        self.label_status_physio.setObjectName(u"label_status_physio")
        self.label_status_physio.setMaximumSize(QSize(16777215, 24))
        self.label_status_physio.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_4.addWidget(self.label_status_physio, 7, 0, 1, 4)

        self.label_physio = QLabel(self.frame_4)
        self.label_physio.setObjectName(u"label_physio")
        self.label_physio.setMaximumSize(QSize(16777215, 16777215))
        self.label_physio.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_physio.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_physio, 3, 2, 1, 1)

        self.comboBox_physio = QComboBox(self.frame_4)
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.addItem("")
        self.comboBox_physio.setObjectName(u"comboBox_physio")
        self.comboBox_physio.setMaximumSize(QSize(16777215, 16777215))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_physio.setPalette(palette21)
        self.comboBox_physio.setFont(font)
        self.comboBox_physio.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_physio.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox_physio, 1, 0, 1, 4)

        self.pushButton_add_physio = QPushButton(self.frame_4)
        self.pushButton_add_physio.setObjectName(u"pushButton_add_physio")
        self.pushButton_add_physio.setMinimumSize(QSize(0, 45))
        self.pushButton_add_physio.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(92, 158, 173, 190);\n"
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
        self.pushButton_add_physio.setIcon(icon3)
        self.pushButton_add_physio.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.pushButton_add_physio, 6, 0, 1, 4)


        self.horizontalLayout_7.addWidget(self.frame_4)

        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.frame_templates_2 = QFrame(self.physio_2)
        self.frame_templates_2.setObjectName(u"frame_templates_2")
        self.frame_templates_2.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_8 = QGridLayout(self.frame_templates_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(5)
        self.gridLayout_8.setVerticalSpacing(1)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.comboBox_template_physio = QComboBox(self.frame_templates_2)
        self.comboBox_template_physio.addItem("")
        self.comboBox_template_physio.setObjectName(u"comboBox_template_physio")
        self.comboBox_template_physio.setMaximumSize(QSize(16777215, 16777215))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBox_template_physio.setPalette(palette22)
        self.comboBox_template_physio.setFont(font)
        self.comboBox_template_physio.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_8.addWidget(self.comboBox_template_physio, 2, 0, 1, 1)

        self.pushButton_add_new_template_physio = QPushButton(self.frame_templates_2)
        self.pushButton_add_new_template_physio.setObjectName(u"pushButton_add_new_template_physio")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette23.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_add_new_template_physio.setPalette(palette23)
        self.pushButton_add_new_template_physio.setFont(font2)
        self.pushButton_add_new_template_physio.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_8.addWidget(self.pushButton_add_new_template_physio, 4, 1, 1, 1)

        self.label_2 = QLabel(self.frame_templates_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 2)

        self.pushButton_push_temp_physio = QPushButton(self.frame_templates_2)
        self.pushButton_push_temp_physio.setObjectName(u"pushButton_push_temp_physio")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush)
        palette24.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette24.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_push_temp_physio.setPalette(palette24)
        self.pushButton_push_temp_physio.setFont(font2)
        self.pushButton_push_temp_physio.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_8.addWidget(self.pushButton_push_temp_physio, 2, 1, 1, 1)

        self.lineEdit_new_template_name_physio = QLineEdit(self.frame_templates_2)
        self.lineEdit_new_template_name_physio.setObjectName(u"lineEdit_new_template_name_physio")
        self.lineEdit_new_template_name_physio.setMinimumSize(QSize(350, 0))
        self.lineEdit_new_template_name_physio.setFont(font)
        self.lineEdit_new_template_name_physio.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_new_template_name_physio, 4, 0, 1, 1)

        self.label_5 = QLabel(self.frame_templates_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_templates_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_6, 3, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_templates_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)


        self.verticalLayout_4.addWidget(self.physio_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_physio_md = QLabel(self.physio)
        self.label_physio_md.setObjectName(u"label_physio_md")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette25.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette25.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette25.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette25.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette25.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette25.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.label_physio_md.setPalette(palette25)
        self.label_physio_md.setFont(font)
        self.label_physio_md.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.label_physio_md)

        self.comboBox_physio_name = QComboBox(self.physio)
        self.comboBox_physio_name.setObjectName(u"comboBox_physio_name")
        self.comboBox_physio_name.setMinimumSize(QSize(300, 0))
        self.comboBox_physio_name.setMaximumSize(QSize(16777215, 20))
        self.comboBox_physio_name.setFont(font)
        self.comboBox_physio_name.setStyleSheet(u"QComboBox  {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QComboBox::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        self.comboBox_physio_name.setEditable(True)

        self.horizontalLayout_6.addWidget(self.comboBox_physio_name)

        self.checkBox_physio_same = QCheckBox(self.physio)
        self.checkBox_physio_same.setObjectName(u"checkBox_physio_same")
        self.checkBox_physio_same.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"	font-size: 11pt;\n"
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
        self.checkBox_physio_same.setChecked(False)

        self.horizontalLayout_6.addWidget(self.checkBox_physio_same)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.tableWidget_physio = QTableWidget(self.physio)
        if (self.tableWidget_physio.columnCount() < 4):
            self.tableWidget_physio.setColumnCount(4)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_physio.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_physio.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_physio.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_physio.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        self.tableWidget_physio.setObjectName(u"tableWidget_physio")
        self.tableWidget_physio.setMinimumSize(QSize(900, 0))
        self.tableWidget_physio.setFont(font2)
        self.tableWidget_physio.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"   background-color: rgba(50, 98, 115, 220);\n"
"   color: #FFFFFF;\n"
"   font-family: Roboto;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #13242B;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"   border-style: none;\n"
"   border-bottom: #13242B;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: rgba(50, 98, 115, 70);\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.tableWidget_physio)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/record_voice_over_FILL1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.physio, icon6, "")
        self.consult = QWidget()
        self.consult.setObjectName(u"consult")
        self.verticalLayout_5 = QVBoxLayout(self.consult)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_physio_place_2 = QLabel(self.consult)
        self.label_physio_place_2.setObjectName(u"label_physio_place_2")
        self.label_physio_place_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_physio_place_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;\n"
"font-size: 14pt;\n"
"")
        self.label_physio_place_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_physio_place_2)

        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/clinical_notes_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.consult, icon7, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.main)

        QWidget.setTabOrder(self.pushButton_set_adm_date, self.pushButton_set_today_date)
        QWidget.setTabOrder(self.pushButton_set_today_date, self.pushButton_clean)
        QWidget.setTabOrder(self.pushButton_clean, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.lineEdit_drug)
        QWidget.setTabOrder(self.lineEdit_drug, self.lineEdit_dose)
        QWidget.setTabOrder(self.lineEdit_dose, self.lineEdit_DS)
        QWidget.setTabOrder(self.lineEdit_DS, self.pushButton_add_and_continue)
        QWidget.setTabOrder(self.pushButton_add_and_continue, self.comboBox_lfk)
        QWidget.setTabOrder(self.comboBox_lfk, self.comboBox_lfk_duration)
        QWidget.setTabOrder(self.comboBox_lfk_duration, self.comboBox_lfk_ed)
        QWidget.setTabOrder(self.comboBox_lfk_ed, self.pushButton_add_lfk)
        QWidget.setTabOrder(self.pushButton_add_lfk, self.comboBox_physio)
        QWidget.setTabOrder(self.comboBox_physio, self.comboBox_physio_place)
        QWidget.setTabOrder(self.comboBox_physio_place, self.comboBox_physio_duration)
        QWidget.setTabOrder(self.comboBox_physio_duration, self.pushButton_add_physio)
        QWidget.setTabOrder(self.pushButton_add_physio, self.pushButton_restart)
        QWidget.setTabOrder(self.pushButton_restart, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.comboBox_diet)
        QWidget.setTabOrder(self.comboBox_diet, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.tableWidget_sol)
        QWidget.setTabOrder(self.tableWidget_sol, self.pushButtonHelp)
        QWidget.setTabOrder(self.pushButtonHelp, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.comboBox_functional_mode)
        QWidget.setTabOrder(self.comboBox_functional_mode, self.comboBox_lfk_template)
        QWidget.setTabOrder(self.comboBox_lfk_template, self.pushButton_lfk_add_new_template)
        QWidget.setTabOrder(self.pushButton_lfk_add_new_template, self.pushButton_lfk_push_temp)
        QWidget.setTabOrder(self.pushButton_lfk_push_temp, self.lineEdit_lfk_new_template_name)
        QWidget.setTabOrder(self.lineEdit_lfk_new_template_name, self.comboBox_lfk_name)
        QWidget.setTabOrder(self.comboBox_lfk_name, self.checkBox_lfk_same)
        QWidget.setTabOrder(self.checkBox_lfk_same, self.tableWidget_lfk)
        QWidget.setTabOrder(self.tableWidget_lfk, self.tableWidget_drugs)
        QWidget.setTabOrder(self.tableWidget_drugs, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.pushButtonNotSaveExit)
        QWidget.setTabOrder(self.pushButtonNotSaveExit, self.tableWidget_peros)
        QWidget.setTabOrder(self.tableWidget_peros, self.comboBox_template_physio)
        QWidget.setTabOrder(self.comboBox_template_physio, self.pushButton_add_new_template_physio)
        QWidget.setTabOrder(self.pushButton_add_new_template_physio, self.pushButton_push_temp_physio)
        QWidget.setTabOrder(self.pushButton_push_temp_physio, self.lineEdit_new_template_name_physio)
        QWidget.setTabOrder(self.lineEdit_new_template_name_physio, self.comboBox_physio_name)
        QWidget.setTabOrder(self.comboBox_physio_name, self.checkBox_physio_same)
        QWidget.setTabOrder(self.checkBox_physio_same, self.tableWidget_physio)

        self.retranslateUi(Appointments)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Appointments)
    # setupUi

    def retranslateUi(self, Appointments):
        Appointments.setWindowTitle(QCoreApplication.translate("Appointments", u"Form", None))
        self.label_Pt_info.setText(QCoreApplication.translate("Appointments", u"PatientInfo\n"
"fff", None))
        self.labelTimeline.setText("")
        self.groupBox_wom.setTitle(QCoreApplication.translate("Appointments", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("Appointments", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("Appointments", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("Appointments", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.label_diet.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p>\u0421\u0442\u043e\u043b \u2116</p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_peros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Appointments", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0437\u043d\u0430\u0447.", None));
        ___qtablewidgetitem1 = self.tableWidget_peros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Appointments", u"\u041f\u0440\u0435\u043f\u0430\u0440\u0430\u0442", None));
        ___qtablewidgetitem2 = self.tableWidget_peros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Appointments", u"\u0414\u043e\u0437\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget_peros.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Appointments", u"\u0420\u0435\u0436\u0438\u043c", None));
        ___qtablewidgetitem4 = self.tableWidget_sol.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Appointments", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0437\u043d\u0430\u0447.", None));
        ___qtablewidgetitem5 = self.tableWidget_sol.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Appointments", u"\u041f\u0440\u0435\u043f\u0430\u0440\u0430\u0442", None));
        ___qtablewidgetitem6 = self.tableWidget_sol.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Appointments", u"\u0414\u043e\u0437\u0430", None));
        ___qtablewidgetitem7 = self.tableWidget_sol.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Appointments", u"\u0420\u0435\u0436\u0438\u043c", None));
        self.comboBox_diet.setItemText(0, QCoreApplication.translate("Appointments", u"15", None))
        self.comboBox_diet.setItemText(1, QCoreApplication.translate("Appointments", u"9", None))
        self.comboBox_diet.setItemText(2, QCoreApplication.translate("Appointments", u"15 \u0447\u0435\u0440\u0435\u0437 \u0437\u043e\u043d\u0434 (\u0431\u043b\u0435\u043d\u0434\u0435\u0440)", None))
        self.comboBox_diet.setItemText(3, QCoreApplication.translate("Appointments", u"15 + \u0437\u043e\u043d\u0434\u043e\u0432\u043e\u0435 \u043f\u0438\u0442\u0430\u043d\u0438\u0435", None))
        self.comboBox_diet.setItemText(4, QCoreApplication.translate("Appointments", u"9 + \u0437\u043e\u043d\u0434\u043e\u0432\u043e\u0435 \u043f\u0438\u0442\u0430\u043d\u0438\u0435", None))

        self.comboBox_functional_mode.setItemText(0, QCoreApplication.translate("Appointments", u"III \u0410", None))
        self.comboBox_functional_mode.setItemText(1, QCoreApplication.translate("Appointments", u"III \u0411", None))
        self.comboBox_functional_mode.setItemText(2, "")

        self.label_functional_mode.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p>\u0420\u0435\u0436\u0438\u043c:</p></body></html>", None))
        self.label_Injections.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p align=\"center\">\u041f\u0430\u0440\u0435\u043d\u0442\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0444\u043e\u0440\u043c\u044b:</p></body></html>", None))
        self.label_PerOs.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p align=\"center\">\u042d\u043d\u0442\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0444\u043e\u0440\u043c\u044b:</p></body></html>", None))
        self.pushButton_add_and_continue.setText(QCoreApplication.translate("Appointments", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043c\u0435\u0434\u0438\u043a\u0430\u043c\u0435\u043d\u0442 \u0432 \u043b\u0438\u0441\u0442 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439", None))
        self.label_add_drug.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p align=\"center\">\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043b\u0435\u043a.\u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442\u0430 \u0432 \u043b\u0438\u0441\u0442 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439</p></body></html>", None))
        self.pushButton_set_adm_date.setText(QCoreApplication.translate("Appointments", u"\u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButton_set_today_date.setText(QCoreApplication.translate("Appointments", u"\u0441\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.pushButton_clean.setText(QCoreApplication.translate("Appointments", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043b\u044f", None))
        self.label_dose.setText(QCoreApplication.translate("Appointments", u"dose", None))
        self.label_DS.setText(QCoreApplication.translate("Appointments", u"DS.", None))
        self.label_date.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p align=\"center\">\u0414\u0430\u0442\u0430:</p></body></html>", None))
        self.label_Rp.setText(QCoreApplication.translate("Appointments", u"Rp.:", None))
        self.checkBox.setText(QCoreApplication.translate("Appointments", u"\u043f\u043e-\u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438", None))
        self.label_status.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton_restart.setText(QCoreApplication.translate("Appointments", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0438 \u043d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043d\u043e\u0432\u043e", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Appointments", u"\u0432 \u0438\u043d\u044a\u0435\u043a\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043b/\u043d", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Appointments", u"\u0432 \u044d\u043d\u0442\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043b/\u043d", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drugs), QCoreApplication.translate("Appointments", u" \u041b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442\u044b  ", None))
        self.label_lfk_regimen.setText(QCoreApplication.translate("Appointments", u"\u0440\u0435\u0436\u0438\u043c", None))
        self.label_lfk_ed.setText(QCoreApplication.translate("Appointments", u"\u0415\u0434.", None))
        self.comboBox_lfk_duration.setItemText(0, QCoreApplication.translate("Appointments", u"\u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e", None))
        self.comboBox_lfk_duration.setItemText(1, QCoreApplication.translate("Appointments", u"\u21165", None))
        self.comboBox_lfk_duration.setItemText(2, QCoreApplication.translate("Appointments", u"\u21167", None))
        self.comboBox_lfk_duration.setItemText(3, QCoreApplication.translate("Appointments", u"\u211610", None))

        self.label_add_lfk.setText(QCoreApplication.translate("Appointments", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.pushButton_add_lfk.setText(QCoreApplication.translate("Appointments", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u041b\u0424\u041a", None))
        self.comboBox_lfk_ed.setItemText(0, "")
        self.comboBox_lfk_ed.setItemText(1, QCoreApplication.translate("Appointments", u"1,0", None))
        self.comboBox_lfk_ed.setItemText(2, QCoreApplication.translate("Appointments", u"1,5", None))
        self.comboBox_lfk_ed.setItemText(3, QCoreApplication.translate("Appointments", u"2,0", None))
        self.comboBox_lfk_ed.setItemText(4, QCoreApplication.translate("Appointments", u"2,5", None))
        self.comboBox_lfk_ed.setItemText(5, QCoreApplication.translate("Appointments", u"3,0", None))
        self.comboBox_lfk_ed.setItemText(6, QCoreApplication.translate("Appointments", u"4,5", None))
        self.comboBox_lfk_ed.setItemText(7, QCoreApplication.translate("Appointments", u"6,0", None))

        self.comboBox_lfk.setItemText(0, "")
        self.comboBox_lfk.setItemText(1, QCoreApplication.translate("Appointments", u"\u043f\u043e \u043c\u0430\u043b\u043e\u0433\u0440\u0443\u043f\u043f\u043e\u0432\u043e\u0439 \u043c\u0435\u0442\u043e\u0434\u0438\u043a\u0435", None))
        self.comboBox_lfk.setItemText(2, QCoreApplication.translate("Appointments", u"\u043f\u043e \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0435\u0442\u043e\u0434\u0438\u043a\u0435", None))
        self.comboBox_lfk.setItemText(3, QCoreApplication.translate("Appointments", u"\u0437\u0430\u043d\u044f\u0442\u0438\u044f \u043d\u0430 \u0432\u0435\u043b\u043e\u0442\u0440\u0435\u043d\u0430\u0436\u0435\u0440\u0435, \u0441\u0442\u0435\u043f\u043f\u0435\u0440\u0435", None))
        self.comboBox_lfk.setItemText(4, QCoreApplication.translate("Appointments", u"\u0431\u0435\u0433\u043e\u0432\u0430\u044f \u0434\u043e\u0440\u043e\u0436\u043a\u0430 \u0432 \u0440\u0435\u0436\u0438\u043c\u0435 \u0445\u043e\u0434\u044c\u0431\u044b", None))
        self.comboBox_lfk.setItemText(5, QCoreApplication.translate("Appointments", u"\u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: \u043a\u043e\u043b\u0435\u043d\u043d\u044b\u0439 \u0443\u043f\u043e\u0440, \u0448\u0430\u0433\u043e\u0445\u043e\u0434", None))
        self.comboBox_lfk.setItemText(6, QCoreApplication.translate("Appointments", u"\u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f: \u0441\u0442\u043e\u043b-\u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438\u0437\u0430\u0442\u043e\u0440", None))
        self.comboBox_lfk.setItemText(7, QCoreApplication.translate("Appointments", u"Artromot \u043d\u0430 \u043f\u043e\u0440\u0430\u0436\u0435\u043d\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_lfk.setItemText(8, QCoreApplication.translate("Appointments", u"Artromot \u043d\u0430 \u043f\u0440\u0430\u0432\u044b\u0439 \u043a\u043e\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_lfk.setItemText(9, QCoreApplication.translate("Appointments", u"Artromot \u043d\u0430 \u043b\u0435\u0432\u044b\u0439 \u043a\u043e\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_lfk.setItemText(10, QCoreApplication.translate("Appointments", u"Artromot \u043d\u0430 \u043f\u0440\u0430\u0432\u044b\u0439 \u0442\u0430\u0437\u043e\u0431\u0435\u0434\u0440\u0435\u043d\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_lfk.setItemText(11, QCoreApplication.translate("Appointments", u"Artromot \u043d\u0430 \u043b\u0435\u0432\u044b\u0439 \u0442\u0430\u0437\u043e\u0431\u0435\u0434\u0440\u0435\u043d\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_lfk.setItemText(12, QCoreApplication.translate("Appointments", u"Artromot \u043d\u0430 \u043f\u0440\u0430\u0432\u044b\u0439 \u0433\u043e\u043b\u0435\u043d\u043e\u0441\u0442\u043e\u043f\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_lfk.setItemText(13, QCoreApplication.translate("Appointments", u"Artromot \u043d\u0430 \u043b\u0435\u0432\u044b\u0439 \u0433\u043e\u043b\u0435\u043d\u043e\u0441\u0442\u043e\u043f\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_lfk.setItemText(14, QCoreApplication.translate("Appointments", u"\u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043c\u0430\u0441\u0441\u0430\u0436 \u043f\u0430\u0440\u0435\u0442\u0438\u0447\u043d\u043e\u0439 \u0440\u0443\u043a\u0438", None))
        self.comboBox_lfk.setItemText(15, QCoreApplication.translate("Appointments", u"\u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043c\u0430\u0441\u0441\u0430\u0436 \u0448\u0435\u0439\u043d\u043e-\u0433\u0440\u0443\u0434\u043d\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438", None))
        self.comboBox_lfk.setItemText(16, QCoreApplication.translate("Appointments", u"\u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043c\u0430\u0441\u0441\u0430\u0436 \u043f\u043e\u044f\u0441\u043d\u0438\u0447\u043d\u043e-\u043a\u0440\u0435\u0441\u0442\u0446\u043e\u0432\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438", None))
        self.comboBox_lfk.setItemText(17, QCoreApplication.translate("Appointments", u"\u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043c\u0430\u0441\u0441\u0430\u0436 \u0440\u0443\u043a", None))
        self.comboBox_lfk.setItemText(18, QCoreApplication.translate("Appointments", u"\u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043c\u0430\u0441\u0441\u0430\u0436 \u043d\u0438\u0436\u043d\u0438\u0445 \u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0441\u0442\u0435\u0439", None))
        self.comboBox_lfk.setItemText(19, QCoreApplication.translate("Appointments", u"\u0437\u0430\u043d\u044f\u0442\u0438\u044f \u043c\u0435\u043b\u043a\u043e\u0439 \u043c\u043e\u0442\u043e\u0440\u0438\u043a\u043e\u0439, \u044d\u0440\u0433\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u0435\u0439", None))
        self.comboBox_lfk.setItemText(20, QCoreApplication.translate("Appointments", u"\u043f\u0430\u0441\u0441\u0438\u0432\u043d\u043e-\u0430\u043a\u0442\u0438\u0432\u043d\u0430\u044f \u043c\u0435\u0445\u0430\u043d\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044f", None))
        self.comboBox_lfk.setItemText(21, QCoreApplication.translate("Appointments", u"\u0437\u0430\u043d\u044f\u0442\u0438\u044f \u0441\u0442\u0430\u0431\u0438\u043b\u043e\u043c\u0435\u0442\u0440\u0438\u0435\u0439", None))
        self.comboBox_lfk.setItemText(22, QCoreApplication.translate("Appointments", u"\u041b\u0424\u041a \u0432 \u0431\u0430\u0441\u0441\u0435\u0439\u043d\u0435", None))
        self.comboBox_lfk.setItemText(23, QCoreApplication.translate("Appointments", u"\u041b\u0424\u041a \u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439 \u0440\u0430\u0437\u0433\u0440\u0443\u0437\u043a\u0438 Levitas", None))

        self.label_status_lfk.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.comboBox_lfk_template.setItemText(0, "")

        self.pushButton_lfk_add_new_template.setText(QCoreApplication.translate("Appointments", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.label.setText(QCoreApplication.translate("Appointments", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u041b\u0424\u041a", None))
        self.pushButton_lfk_push_temp.setText(QCoreApplication.translate("Appointments", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit_lfk_new_template_name.setText("")
        self.lineEdit_lfk_new_template_name.setPlaceholderText(QCoreApplication.translate("Appointments", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Appointments", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Appointments", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_lfk_md_2.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p align=\"right\">\u0412\u0440\u0430\u0447-\u041b\u0424\u041a:</p></body></html>", None))
        self.checkBox_lfk_same.setText(QCoreApplication.translate("Appointments", u"\u0441\u043e\u0432\u043f\u0430\u0434\u0430\u0435\u0442 \u0441 \u043b\u0435\u0447\u0430\u0449\u0438\u043c \u0432\u0440\u0430\u0447\u043e\u043c", None))
        ___qtablewidgetitem8 = self.tableWidget_lfk.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Appointments", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem9 = self.tableWidget_lfk.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Appointments", u"\u0420\u0435\u0436\u0438\u043c", None));
        ___qtablewidgetitem10 = self.tableWidget_lfk.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Appointments", u"\u0415\u0434.", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lkf), QCoreApplication.translate("Appointments", u" \u041b\u0424\u041a  ", None))
        self.label_add_physio.setText(QCoreApplication.translate("Appointments", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.comboBox_physio_duration.setItemText(0, "")
        self.comboBox_physio_duration.setItemText(1, QCoreApplication.translate("Appointments", u"\u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e", None))
        self.comboBox_physio_duration.setItemText(2, QCoreApplication.translate("Appointments", u"\u21165", None))
        self.comboBox_physio_duration.setItemText(3, QCoreApplication.translate("Appointments", u"\u21167", None))
        self.comboBox_physio_duration.setItemText(4, QCoreApplication.translate("Appointments", u"\u211610", None))

        self.label_physio_place.setText(QCoreApplication.translate("Appointments", u"\u043e\u0431\u043b\u0430\u0441\u0442\u044c", None))
        self.comboBox_physio_place.setItemText(0, "")
        self.comboBox_physio_place.setItemText(1, QCoreApplication.translate("Appointments", u"\u0422\u041c\u0422 \u043f\u0440.\u21161", None))
        self.comboBox_physio_place.setItemText(2, QCoreApplication.translate("Appointments", u"\u0422\u041c\u0422 \u043f\u0440.\u21162", None))
        self.comboBox_physio_place.setItemText(3, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u043f\u0430\u0440\u0435\u0442\u0438\u0447\u043d\u044b\u0435 \u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0441\u0442\u0438", None))
        self.comboBox_physio_place.setItemText(4, QCoreApplication.translate("Appointments", u"\u043c\u044b\u0448\u0446 \u0440\u0430\u0437\u0433\u0438\u0431\u0430\u0442\u0435\u043b\u0435\u0439 \u043f\u0430\u0440\u0435\u0442\u0438\u0447\u043d\u044b\u0445 \u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0441\u0442\u0435\u0439", None))
        self.comboBox_physio_place.setItemText(5, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u043c\u043e\u0447\u0435\u0432\u043e\u0433\u043e \u043f\u0443\u0437\u044b\u0440\u044f", None))
        self.comboBox_physio_place.setItemText(6, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u043f\u043e\u0440\u0430\u0436\u0435\u043d\u043d\u044b\u0439 \u043f\u043b\u0435\u0447\u0435\u0432\u043e\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_physio_place.setItemText(7, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u043f\u043e\u0440\u0430\u0436\u0435\u043d\u043d\u044b\u0439 \u043a\u043e\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_physio_place.setItemText(8, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u043f\u043e\u0440\u0430\u0436\u0435\u043d\u043d\u044b\u0439 \u0442\u0430\u0437\u043e\u0431\u0435\u0434\u0440\u0435\u043d\u043d\u044b\u0439 \u0441\u0443\u0441\u0442\u0430\u0432", None))
        self.comboBox_physio_place.setItemText(9, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u043f\u0440\u043e\u043b\u0435\u0436\u043d\u044f", None))
        self.comboBox_physio_place.setItemText(10, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u0422\u0421\u0422", None))
        self.comboBox_physio_place.setItemText(11, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u043f\u043e\u044f\u043d\u0438\u0447\u043d\u043e-\u043a\u0440\u0435\u0441\u0442\u0446\u043e\u0432\u0443\u044e \u043e\u0431\u043b\u0430\u0441\u0442\u044c", None))
        self.comboBox_physio_place.setItemText(12, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u0448\u0435\u0439\u043d\u043e-\u0433\u0440\u0443\u0434\u043d\u0443\u044e \u043e\u0431\u043b\u0430\u0441\u0442\u044c", None))
        self.comboBox_physio_place.setItemText(13, QCoreApplication.translate("Appointments", u"\u043d\u0430 \u0448\u0435\u0439\u043d\u043e-\u0432\u043e\u0440\u043e\u0442\u043d\u0438\u043a\u043e\u0432\u0443\u044e \u043e\u0431\u043b\u0430\u0441\u0442\u044c", None))

        self.label_status_physio.setText(QCoreApplication.translate("Appointments", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_physio.setText(QCoreApplication.translate("Appointments", u"\u0440\u0435\u0436\u0438\u043c", None))
        self.comboBox_physio.setItemText(0, "")
        self.comboBox_physio.setItemText(1, QCoreApplication.translate("Appointments", u"\u041f\u0435\u041c\u041f", None))
        self.comboBox_physio.setItemText(2, QCoreApplication.translate("Appointments", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0444\u043e\u0440\u0435\u0437 2% \u0440-\u0440\u0430 \u041d\u043e\u0432\u043e\u043a\u0430\u0438\u043d\u0430", None))
        self.comboBox_physio.setItemText(3, QCoreApplication.translate("Appointments", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0444\u043e\u0440\u0435\u0437 2,4% \u0440-\u0440\u0430 \u042d\u0443\u0444\u0438\u043b\u043b\u0438\u043d\u0430", None))
        self.comboBox_physio.setItemText(4, QCoreApplication.translate("Appointments", u"\u0421\u041c\u0422-\u0444\u043e\u0440\u0435\u0437 0,5% \u0440-\u0440\u0430 \u041d\u043e\u0432\u043e\u043a\u0430\u0438\u043d\u0430", None))
        self.comboBox_physio.setItemText(5, QCoreApplication.translate("Appointments", u"\u0421\u041c\u0422-\u0444\u043e\u0440\u0435\u0437 2,4% \u0440-\u0440\u0430 \u042d\u0443\u0444\u0438\u043b\u043b\u0438\u043d\u0430", None))
        self.comboBox_physio.setItemText(6, QCoreApplication.translate("Appointments", u"\u0410\u043f\u043f\u043b\u0438\u043a\u0430\u0446\u0438\u0438 \u043e\u0437\u043e\u043a\u0435\u0440\u0438\u0442\u0430", None))
        self.comboBox_physio.setItemText(7, QCoreApplication.translate("Appointments", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0441\u0442\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u044f", None))
        self.comboBox_physio.setItemText(8, QCoreApplication.translate("Appointments", u"\u041c\u0430\u0433\u043d\u0438\u0442\u043d\u0430\u044f \u0441\u0442\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u044f", None))
        self.comboBox_physio.setItemText(9, QCoreApplication.translate("Appointments", u"\u0418\u043d\u0433\u0430\u043b\u044f\u0446\u0438\u0438", None))
        self.comboBox_physio.setItemText(10, QCoreApplication.translate("Appointments", u"\"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0441\u043e\u043d\"", None))
        self.comboBox_physio.setItemText(11, QCoreApplication.translate("Appointments", u"\u041f\u043d\u0435\u0432\u043c\u043e\u043c\u0430\u0441\u0441\u0430\u0436", None))
        self.comboBox_physio.setItemText(12, QCoreApplication.translate("Appointments", u"\u041d\u0435\u0441\u0435\u043b\u0435\u043a\u0442\u0438\u0432\u043d\u0430\u044f \u0445\u0440\u043e\u043c\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044f", None))

        self.pushButton_add_physio.setText(QCoreApplication.translate("Appointments", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0444\u0438\u0437\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u0438", None))
        self.comboBox_template_physio.setItemText(0, "")

        self.pushButton_add_new_template_physio.setText(QCoreApplication.translate("Appointments", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Appointments", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0444\u0438\u0437\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u0438", None))
        self.pushButton_push_temp_physio.setText(QCoreApplication.translate("Appointments", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit_new_template_name_physio.setText("")
        self.lineEdit_new_template_name_physio.setPlaceholderText(QCoreApplication.translate("Appointments", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Appointments", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.label_6.setText(QCoreApplication.translate("Appointments", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_physio_md.setText(QCoreApplication.translate("Appointments", u"\u0412\u0440\u0430\u0447-\u0444\u0438\u0437\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442:", None))
        self.checkBox_physio_same.setText(QCoreApplication.translate("Appointments", u"\u0441\u043e\u0432\u043f\u0430\u0434\u0430\u0435\u0442 \u0441 \u043b\u0435\u0447\u0430\u0449\u0438\u043c \u0432\u0440\u0430\u0447\u043e\u043c", None))
        ___qtablewidgetitem11 = self.tableWidget_physio.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Appointments", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem12 = self.tableWidget_physio.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Appointments", u"\u041e\u0431\u043b\u0430\u0441\u0442\u044c", None));
        ___qtablewidgetitem13 = self.tableWidget_physio.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Appointments", u"\u0420\u0435\u0436\u0438\u043c", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.physio), QCoreApplication.translate("Appointments", u" \u0424\u0438\u0437\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044f  ", None))
        self.label_physio_place_2.setText(QCoreApplication.translate("Appointments", u"\u0420\u0430\u0437\u0434\u0435\u043b \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0432 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435\n"
"\u043f\u0440\u0438\u043d\u043e\u0441\u0438\u043c \u0438\u0437\u0432\u0438\u043d\u0435\u043d\u0438\u044f \u0437\u0430 \u043d\u0435\u0443\u0434\u043e\u0431\u0441\u0442\u0432\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.consult), QCoreApplication.translate("Appointments", u" \u0418\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f \u0438 \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438  ", None))
    # retranslateUi

