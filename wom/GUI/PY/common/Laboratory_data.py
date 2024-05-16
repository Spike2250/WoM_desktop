# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Laboratory_data.ui'
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
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc

class Ui_Lab_data(object):
    def setupUi(self, Lab_data):
        if not Lab_data.objectName():
            Lab_data.setObjectName(u"Lab_data")
        Lab_data.resize(998, 709)
        Lab_data.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_2 = QVBoxLayout(Lab_data)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(Lab_data)
        self.main.setObjectName(u"main")
        self.gridLayout_11 = QGridLayout(self.main)
        self.gridLayout_11.setSpacing(5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
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
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/lab_research_FILL0_wght400_GRAD0_opsz48_w.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTimeline)


        self.gridLayout_11.addWidget(self.pt_info_block, 0, 0, 1, 1)

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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

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


        self.gridLayout_11.addWidget(self.groupBox_wom, 0, 1, 2, 1)

        self.tabWidget = QTabWidget(self.main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget:pane {\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"background-color: transparent;\n"
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
"}")
        self.tabWidget.setIconSize(QSize(28, 28))
        self.oak_oam = QWidget()
        self.oak_oam.setObjectName(u"oak_oam")
        self.gridLayout_5 = QGridLayout(self.oak_oam)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(25)
        self.horizontalSpacer_3 = QSpacerItem(134, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.oak_frame = QFrame(self.oak_oam)
        self.oak_frame.setObjectName(u"oak_frame")
        self.oak_frame.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.oak_frame)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.dateEdit_OAK = QDateEdit(self.oak_frame)
        self.dateEdit_OAK.setObjectName(u"dateEdit_OAK")
        self.dateEdit_OAK.setFont(font)
        self.dateEdit_OAK.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.dateEdit_OAK, 0, 4, 1, 2)

        self.label_OAK_report = QLabel(self.oak_frame)
        self.label_OAK_report.setObjectName(u"label_OAK_report")
        self.label_OAK_report.setMaximumSize(QSize(16777215, 33))
        self.label_OAK_report.setFont(font)
        self.label_OAK_report.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_OAK_report.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_OAK_report, 18, 0, 1, 6)

        self.label_Er = QLabel(self.oak_frame)
        self.label_Er.setObjectName(u"label_Er")
        self.label_Er.setMaximumSize(QSize(16777215, 33))
        self.label_Er.setFont(font)
        self.label_Er.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Er, 1, 0, 1, 4)

        self.label_Le_Lym = QLabel(self.oak_frame)
        self.label_Le_Lym.setObjectName(u"label_Le_Lym")
        self.label_Le_Lym.setMaximumSize(QSize(16777215, 33))
        self.label_Le_Lym.setFont(font)
        self.label_Le_Lym.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Le_Lym, 12, 1, 1, 4)

        self.lineEdit_Le = QLineEdit(self.oak_frame)
        self.lineEdit_Le.setObjectName(u"lineEdit_Le")
        self.lineEdit_Le.setMinimumSize(QSize(0, 28))
        self.lineEdit_Le.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Le.setFont(font)
        self.lineEdit_Le.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Le, 5, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 0, 6, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.label_Le_N_s = QLabel(self.oak_frame)
        self.label_Le_N_s.setObjectName(u"label_Le_N_s")
        self.label_Le_N_s.setMaximumSize(QSize(16777215, 33))
        self.label_Le_N_s.setFont(font)
        self.label_Le_N_s.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Le_N_s, 10, 2, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.lineEdit_Le_Eoz = QLineEdit(self.oak_frame)
        self.lineEdit_Le_Eoz.setObjectName(u"lineEdit_Le_Eoz")
        self.lineEdit_Le_Eoz.setMinimumSize(QSize(0, 28))
        self.lineEdit_Le_Eoz.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Le_Eoz.setFont(font)
        self.lineEdit_Le_Eoz.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Le_Eoz, 7, 5, 1, 1)

        self.label_Ht = QLabel(self.oak_frame)
        self.label_Ht.setObjectName(u"label_Ht")
        self.label_Ht.setMaximumSize(QSize(16777215, 33))
        self.label_Ht.setFont(font)
        self.label_Ht.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Ht, 4, 0, 1, 5)

        self.label_soe = QLabel(self.oak_frame)
        self.label_soe.setObjectName(u"label_soe")
        self.label_soe.setMaximumSize(QSize(16777215, 33))
        self.label_soe.setFont(font)
        self.label_soe.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_soe, 14, 0, 1, 5)

        self.label_Le = QLabel(self.oak_frame)
        self.label_Le.setObjectName(u"label_Le")
        self.label_Le.setMaximumSize(QSize(16777215, 33))
        self.label_Le.setFont(font)
        self.label_Le.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Le, 5, 0, 1, 5)

        self.lineEdit_Le_Lym = QLineEdit(self.oak_frame)
        self.lineEdit_Le_Lym.setObjectName(u"lineEdit_Le_Lym")
        self.lineEdit_Le_Lym.setMinimumSize(QSize(0, 28))
        self.lineEdit_Le_Lym.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Le_Lym.setFont(font)
        self.lineEdit_Le_Lym.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Le_Lym, 12, 5, 1, 1)

        self.lineEdit_Er = QLineEdit(self.oak_frame)
        self.lineEdit_Er.setObjectName(u"lineEdit_Er")
        self.lineEdit_Er.setMinimumSize(QSize(0, 28))
        self.lineEdit_Er.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Er.setFont(font)
        self.lineEdit_Er.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Er, 1, 5, 1, 1)

        self.lineEdit_Tr = QLineEdit(self.oak_frame)
        self.lineEdit_Tr.setObjectName(u"lineEdit_Tr")
        self.lineEdit_Tr.setMinimumSize(QSize(0, 28))
        self.lineEdit_Tr.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Tr.setFont(font)
        self.lineEdit_Tr.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Tr, 13, 5, 1, 1)

        self.label_Le_M = QLabel(self.oak_frame)
        self.label_Le_M.setObjectName(u"label_Le_M")
        self.label_Le_M.setMaximumSize(QSize(16777215, 33))
        self.label_Le_M.setFont(font)
        self.label_Le_M.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Le_M, 11, 1, 1, 4)

        self.lineEdit_Le_B = QLineEdit(self.oak_frame)
        self.lineEdit_Le_B.setObjectName(u"lineEdit_Le_B")
        self.lineEdit_Le_B.setMinimumSize(QSize(0, 28))
        self.lineEdit_Le_B.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Le_B.setFont(font)
        self.lineEdit_Le_B.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Le_B, 6, 5, 1, 1)

        self.lineEdit_Ht = QLineEdit(self.oak_frame)
        self.lineEdit_Ht.setObjectName(u"lineEdit_Ht")
        self.lineEdit_Ht.setMinimumSize(QSize(0, 28))
        self.lineEdit_Ht.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Ht.setFont(font)
        self.lineEdit_Ht.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Ht, 4, 5, 1, 1)

        self.label_Le_N_p = QLabel(self.oak_frame)
        self.label_Le_N_p.setObjectName(u"label_Le_N_p")
        self.label_Le_N_p.setMaximumSize(QSize(16777215, 33))
        self.label_Le_N_p.setFont(font)
        self.label_Le_N_p.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Le_N_p, 9, 2, 1, 3)

        self.lineEdit_Hb = QLineEdit(self.oak_frame)
        self.lineEdit_Hb.setObjectName(u"lineEdit_Hb")
        self.lineEdit_Hb.setMinimumSize(QSize(0, 28))
        self.lineEdit_Hb.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Hb.setFont(font)
        self.lineEdit_Hb.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Hb, 2, 5, 1, 1)

        self.label_Le_N_yu = QLabel(self.oak_frame)
        self.label_Le_N_yu.setObjectName(u"label_Le_N_yu")
        self.label_Le_N_yu.setMaximumSize(QSize(16777215, 33))
        self.label_Le_N_yu.setFont(font)
        self.label_Le_N_yu.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Le_N_yu, 8, 2, 1, 3)

        self.lineEdit_Le_N_yu = QLineEdit(self.oak_frame)
        self.lineEdit_Le_N_yu.setObjectName(u"lineEdit_Le_N_yu")
        self.lineEdit_Le_N_yu.setMinimumSize(QSize(0, 28))
        self.lineEdit_Le_N_yu.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Le_N_yu.setFont(font)
        self.lineEdit_Le_N_yu.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Le_N_yu, 8, 5, 1, 1)

        self.label_Tr = QLabel(self.oak_frame)
        self.label_Tr.setObjectName(u"label_Tr")
        self.label_Tr.setMaximumSize(QSize(16777215, 33))
        self.label_Tr.setFont(font)
        self.label_Tr.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Tr, 13, 0, 1, 5)

        self.label_Le_Eoz = QLabel(self.oak_frame)
        self.label_Le_Eoz.setObjectName(u"label_Le_Eoz")
        self.label_Le_Eoz.setMaximumSize(QSize(16777215, 33))
        self.label_Le_Eoz.setFont(font)
        self.label_Le_Eoz.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Le_Eoz, 7, 1, 1, 4)

        self.lineEdit_soe = QLineEdit(self.oak_frame)
        self.lineEdit_soe.setObjectName(u"lineEdit_soe")
        self.lineEdit_soe.setMinimumSize(QSize(0, 28))
        self.lineEdit_soe.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_soe.setFont(font)
        self.lineEdit_soe.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_soe, 14, 5, 1, 1)

        self.label_Le_N = QLabel(self.oak_frame)
        self.label_Le_N.setObjectName(u"label_Le_N")
        self.label_Le_N.setMaximumSize(QSize(9, 100))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(5)
        font3.setBold(True)
        self.label_Le_N.setFont(font3)
        self.label_Le_N.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;\n"
"font-size: 5pt;")

        self.gridLayout.addWidget(self.label_Le_N, 8, 1, 3, 1)

        self.lineEdit_color = QLineEdit(self.oak_frame)
        self.lineEdit_color.setObjectName(u"lineEdit_color")
        self.lineEdit_color.setMinimumSize(QSize(0, 28))
        self.lineEdit_color.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_color.setFont(font)
        self.lineEdit_color.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_color, 3, 5, 1, 1)

        self.lineEdit_Le_N_s = QLineEdit(self.oak_frame)
        self.lineEdit_Le_N_s.setObjectName(u"lineEdit_Le_N_s")
        self.lineEdit_Le_N_s.setMinimumSize(QSize(0, 28))
        self.lineEdit_Le_N_s.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Le_N_s.setFont(font)
        self.lineEdit_Le_N_s.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Le_N_s, 10, 5, 1, 1)

        self.lineEdit_Le_N_p = QLineEdit(self.oak_frame)
        self.lineEdit_Le_N_p.setObjectName(u"lineEdit_Le_N_p")
        self.lineEdit_Le_N_p.setMinimumSize(QSize(0, 28))
        self.lineEdit_Le_N_p.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Le_N_p.setFont(font)
        self.lineEdit_Le_N_p.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Le_N_p, 9, 5, 1, 1)

        self.lineEdit_Le_M = QLineEdit(self.oak_frame)
        self.lineEdit_Le_M.setObjectName(u"lineEdit_Le_M")
        self.lineEdit_Le_M.setMinimumSize(QSize(0, 28))
        self.lineEdit_Le_M.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_Le_M.setFont(font)
        self.lineEdit_Le_M.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_Le_M, 11, 5, 1, 1)

        self.label_color = QLabel(self.oak_frame)
        self.label_color.setObjectName(u"label_color")
        self.label_color.setMaximumSize(QSize(16777215, 33))
        self.label_color.setFont(font)
        self.label_color.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_color, 3, 0, 1, 5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 16, 2, 2, 1)

        self.label_Le_B = QLabel(self.oak_frame)
        self.label_Le_B.setObjectName(u"label_Le_B")
        self.label_Le_B.setMaximumSize(QSize(16777215, 33))
        self.label_Le_B.setFont(font)
        self.label_Le_B.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Le_B, 6, 1, 1, 4)

        self.label_Hb = QLabel(self.oak_frame)
        self.label_Hb.setObjectName(u"label_Hb")
        self.label_Hb.setMaximumSize(QSize(16777215, 33))
        self.label_Hb.setFont(font)
        self.label_Hb.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_Hb, 2, 0, 1, 5)

        self.lineEdit_OAK_other_r = QLineEdit(self.oak_frame)
        self.lineEdit_OAK_other_r.setObjectName(u"lineEdit_OAK_other_r")
        self.lineEdit_OAK_other_r.setMinimumSize(QSize(0, 28))
        self.lineEdit_OAK_other_r.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_OAK_other_r.setFont(font)
        self.lineEdit_OAK_other_r.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_OAK_other_r, 15, 5, 1, 1)

        self.lineEdit_OAK_other = QLineEdit(self.oak_frame)
        self.lineEdit_OAK_other.setObjectName(u"lineEdit_OAK_other")
        self.lineEdit_OAK_other.setMinimumSize(QSize(0, 28))
        self.lineEdit_OAK_other.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_OAK_other.setFont(font)
        self.lineEdit_OAK_other.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_OAK_other, 15, 0, 1, 5)

        self.label = QLabel(self.oak_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.pushButton_add_OAK = QPushButton(self.oak_frame)
        self.pushButton_add_OAK.setObjectName(u"pushButton_add_OAK")
        self.pushButton_add_OAK.setMinimumSize(QSize(0, 25))
        self.pushButton_add_OAK.setFont(font2)
        self.pushButton_add_OAK.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_add_OAK, 16, 3, 2, 3)


        self.gridLayout_5.addWidget(self.oak_frame, 0, 1, 1, 1)

        self.oam_frame = QFrame(self.oak_oam)
        self.oam_frame.setObjectName(u"oam_frame")
        self.oam_frame.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_2 = QGridLayout(self.oam_frame)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_urine_gluc = QLabel(self.oam_frame)
        self.label_urine_gluc.setObjectName(u"label_urine_gluc")
        self.label_urine_gluc.setMaximumSize(QSize(16777215, 33))
        self.label_urine_gluc.setFont(font)
        self.label_urine_gluc.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_gluc, 4, 0, 1, 3)

        self.lineEdit_urine_cilindr = QLineEdit(self.oam_frame)
        self.lineEdit_urine_cilindr.setObjectName(u"lineEdit_urine_cilindr")
        self.lineEdit_urine_cilindr.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_cilindr.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_cilindr.setFont(font)
        self.lineEdit_urine_cilindr.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_cilindr, 12, 4, 1, 2)

        self.label_urine_protein = QLabel(self.oam_frame)
        self.label_urine_protein.setObjectName(u"label_urine_protein")
        self.label_urine_protein.setMaximumSize(QSize(16777215, 33))
        self.label_urine_protein.setFont(font)
        self.label_urine_protein.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_protein, 3, 0, 1, 3)

        self.label_OAM_report = QLabel(self.oam_frame)
        self.label_OAM_report.setObjectName(u"label_OAM_report")
        self.label_OAM_report.setMaximumSize(QSize(16777215, 33))
        self.label_OAM_report.setFont(font)
        self.label_OAM_report.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_OAM_report.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_OAM_report, 19, 0, 1, 6)

        self.lineEdit_urine_Le = QLineEdit(self.oam_frame)
        self.lineEdit_urine_Le.setObjectName(u"lineEdit_urine_Le")
        self.lineEdit_urine_Le.setMinimumSize(QSize(0, 28))
        self.lineEdit_urine_Le.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_urine_Le.setFont(font)
        self.lineEdit_urine_Le.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_Le, 7, 5, 1, 1)

        self.lineEdit_urine_protein = QLineEdit(self.oam_frame)
        self.lineEdit_urine_protein.setObjectName(u"lineEdit_urine_protein")
        self.lineEdit_urine_protein.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_protein.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_protein.setFont(font)
        self.lineEdit_urine_protein.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_protein, 3, 4, 1, 2)

        self.lineEdit_urine_color = QLineEdit(self.oam_frame)
        self.lineEdit_urine_color.setObjectName(u"lineEdit_urine_color")
        self.lineEdit_urine_color.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_color.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_color.setFont(font)
        self.lineEdit_urine_color.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_color, 1, 4, 1, 2)

        self.label_urine_Le = QLabel(self.oam_frame)
        self.label_urine_Le.setObjectName(u"label_urine_Le")
        self.label_urine_Le.setMaximumSize(QSize(16777215, 33))
        self.label_urine_Le.setFont(font)
        self.label_urine_Le.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_Le, 7, 0, 1, 5)

        self.lineEdit_urine_epit_pl = QLineEdit(self.oam_frame)
        self.lineEdit_urine_epit_pl.setObjectName(u"lineEdit_urine_epit_pl")
        self.lineEdit_urine_epit_pl.setMinimumSize(QSize(0, 28))
        self.lineEdit_urine_epit_pl.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_urine_epit_pl.setFont(font)
        self.lineEdit_urine_epit_pl.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_epit_pl, 9, 5, 1, 1)

        self.label_urine_cilindr = QLabel(self.oam_frame)
        self.label_urine_cilindr.setObjectName(u"label_urine_cilindr")
        self.label_urine_cilindr.setMaximumSize(QSize(16777215, 33))
        self.label_urine_cilindr.setFont(font)
        self.label_urine_cilindr.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_cilindr, 12, 0, 1, 3)

        self.lineEdit_urine_epit_zern = QLineEdit(self.oam_frame)
        self.lineEdit_urine_epit_zern.setObjectName(u"lineEdit_urine_epit_zern")
        self.lineEdit_urine_epit_zern.setMinimumSize(QSize(0, 28))
        self.lineEdit_urine_epit_zern.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_urine_epit_zern.setFont(font)
        self.lineEdit_urine_epit_zern.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_epit_zern, 10, 5, 1, 1)

        self.lineEdit_urine_Bacteria = QLineEdit(self.oam_frame)
        self.lineEdit_urine_Bacteria.setObjectName(u"lineEdit_urine_Bacteria")
        self.lineEdit_urine_Bacteria.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_Bacteria.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_Bacteria.setFont(font)
        self.lineEdit_urine_Bacteria.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_Bacteria, 15, 4, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.label_urine_Bacteria = QLabel(self.oam_frame)
        self.label_urine_Bacteria.setObjectName(u"label_urine_Bacteria")
        self.label_urine_Bacteria.setMaximumSize(QSize(16777215, 33))
        self.label_urine_Bacteria.setFont(font)
        self.label_urine_Bacteria.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_Bacteria, 15, 0, 1, 3)

        self.label_urine_epit_pl = QLabel(self.oam_frame)
        self.label_urine_epit_pl.setObjectName(u"label_urine_epit_pl")
        self.label_urine_epit_pl.setMaximumSize(QSize(16777215, 33))
        self.label_urine_epit_pl.setFont(font)
        self.label_urine_epit_pl.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_epit_pl, 9, 0, 1, 5)

        self.lineEdit_udel_ves = QLineEdit(self.oam_frame)
        self.lineEdit_udel_ves.setObjectName(u"lineEdit_udel_ves")
        self.lineEdit_udel_ves.setMinimumSize(QSize(0, 28))
        self.lineEdit_udel_ves.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_udel_ves.setFont(font)
        self.lineEdit_udel_ves.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_udel_ves, 6, 5, 1, 1)

        self.label_urine_color = QLabel(self.oam_frame)
        self.label_urine_color.setObjectName(u"label_urine_color")
        self.label_urine_color.setMaximumSize(QSize(16777215, 33))
        self.label_urine_color.setFont(font)
        self.label_urine_color.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_color, 1, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 17, 1, 2, 1)

        self.lineEdit_urine_epit_ren = QLineEdit(self.oam_frame)
        self.lineEdit_urine_epit_ren.setObjectName(u"lineEdit_urine_epit_ren")
        self.lineEdit_urine_epit_ren.setMinimumSize(QSize(0, 28))
        self.lineEdit_urine_epit_ren.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_urine_epit_ren.setFont(font)
        self.lineEdit_urine_epit_ren.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_epit_ren, 11, 5, 1, 1)

        self.label_urine_epit_ren = QLabel(self.oam_frame)
        self.label_urine_epit_ren.setObjectName(u"label_urine_epit_ren")
        self.label_urine_epit_ren.setMaximumSize(QSize(16777215, 33))
        self.label_urine_epit_ren.setFont(font)
        self.label_urine_epit_ren.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_epit_ren, 11, 0, 1, 5)

        self.label_urine_Er = QLabel(self.oam_frame)
        self.label_urine_Er.setObjectName(u"label_urine_Er")
        self.label_urine_Er.setMaximumSize(QSize(16777215, 33))
        self.label_urine_Er.setFont(font)
        self.label_urine_Er.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_Er, 8, 0, 1, 5)

        self.lineEdit_urine_aceton = QLineEdit(self.oam_frame)
        self.lineEdit_urine_aceton.setObjectName(u"lineEdit_urine_aceton")
        self.lineEdit_urine_aceton.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_aceton.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_aceton.setFont(font)
        self.lineEdit_urine_aceton.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_aceton, 5, 4, 1, 2)

        self.lineEdit_urine_Er = QLineEdit(self.oam_frame)
        self.lineEdit_urine_Er.setObjectName(u"lineEdit_urine_Er")
        self.lineEdit_urine_Er.setMinimumSize(QSize(0, 28))
        self.lineEdit_urine_Er.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_urine_Er.setFont(font)
        self.lineEdit_urine_Er.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_Er, 8, 5, 1, 1)

        self.label_urine_slime = QLabel(self.oam_frame)
        self.label_urine_slime.setObjectName(u"label_urine_slime")
        self.label_urine_slime.setMaximumSize(QSize(16777215, 33))
        self.label_urine_slime.setFont(font)
        self.label_urine_slime.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_slime, 14, 0, 1, 3)

        self.label_urine_epit_zern = QLabel(self.oam_frame)
        self.label_urine_epit_zern.setObjectName(u"label_urine_epit_zern")
        self.label_urine_epit_zern.setMaximumSize(QSize(16777215, 33))
        self.label_urine_epit_zern.setFont(font)
        self.label_urine_epit_zern.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_epit_zern, 10, 0, 1, 5)

        self.lineEdit_urine_gluc = QLineEdit(self.oam_frame)
        self.lineEdit_urine_gluc.setObjectName(u"lineEdit_urine_gluc")
        self.lineEdit_urine_gluc.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_gluc.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_gluc.setFont(font)
        self.lineEdit_urine_gluc.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_gluc, 4, 4, 1, 2)

        self.label_udel_ves = QLabel(self.oam_frame)
        self.label_udel_ves.setObjectName(u"label_udel_ves")
        self.label_udel_ves.setMaximumSize(QSize(16777215, 33))
        self.label_udel_ves.setFont(font)
        self.label_udel_ves.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_udel_ves, 6, 0, 1, 5)

        self.lineEdit_urine_light = QLineEdit(self.oam_frame)
        self.lineEdit_urine_light.setObjectName(u"lineEdit_urine_light")
        self.lineEdit_urine_light.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_light.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_light.setFont(font)
        self.lineEdit_urine_light.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_light, 2, 4, 1, 2)

        self.label_urine_aceton = QLabel(self.oam_frame)
        self.label_urine_aceton.setObjectName(u"label_urine_aceton")
        self.label_urine_aceton.setMaximumSize(QSize(16777215, 33))
        self.label_urine_aceton.setFont(font)
        self.label_urine_aceton.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_aceton, 5, 0, 1, 3)

        self.dateEdit_OAM = QDateEdit(self.oam_frame)
        self.dateEdit_OAM.setObjectName(u"dateEdit_OAM")
        self.dateEdit_OAM.setFont(font)
        self.dateEdit_OAM.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.dateEdit_OAM, 0, 4, 1, 2)

        self.lineEdit_urine_salt = QLineEdit(self.oam_frame)
        self.lineEdit_urine_salt.setObjectName(u"lineEdit_urine_salt")
        self.lineEdit_urine_salt.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_salt.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_salt.setFont(font)
        self.lineEdit_urine_salt.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_salt, 13, 4, 1, 2)

        self.label_urine_light = QLabel(self.oam_frame)
        self.label_urine_light.setObjectName(u"label_urine_light")
        self.label_urine_light.setMaximumSize(QSize(16777215, 33))
        self.label_urine_light.setFont(font)
        self.label_urine_light.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_light, 2, 0, 1, 3)

        self.lineEdit_urine_slime = QLineEdit(self.oam_frame)
        self.lineEdit_urine_slime.setObjectName(u"lineEdit_urine_slime")
        self.lineEdit_urine_slime.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_slime.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_slime.setFont(font)
        self.lineEdit_urine_slime.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_slime, 14, 4, 1, 2)

        self.label_urine_salt = QLabel(self.oam_frame)
        self.label_urine_salt.setObjectName(u"label_urine_salt")
        self.label_urine_salt.setMaximumSize(QSize(16777215, 33))
        self.label_urine_salt.setFont(font)
        self.label_urine_salt.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_urine_salt, 13, 0, 1, 3)

        self.lineEdit_urine_other_r = QLineEdit(self.oam_frame)
        self.lineEdit_urine_other_r.setObjectName(u"lineEdit_urine_other_r")
        self.lineEdit_urine_other_r.setMinimumSize(QSize(120, 28))
        self.lineEdit_urine_other_r.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_other_r.setFont(font)
        self.lineEdit_urine_other_r.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_other_r, 16, 4, 1, 2)

        self.lineEdit_urine_other = QLineEdit(self.oam_frame)
        self.lineEdit_urine_other.setObjectName(u"lineEdit_urine_other")
        self.lineEdit_urine_other.setMinimumSize(QSize(0, 28))
        self.lineEdit_urine_other.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_urine_other.setFont(font)
        self.lineEdit_urine_other.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_urine_other, 16, 0, 1, 4)

        self.label_2 = QLabel(self.oam_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 3)

        self.pushButton_add_OAM = QPushButton(self.oam_frame)
        self.pushButton_add_OAM.setObjectName(u"pushButton_add_OAM")
        self.pushButton_add_OAM.setMinimumSize(QSize(0, 25))
        self.pushButton_add_OAM.setFont(font2)
        self.pushButton_add_OAM.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.pushButton_add_OAM, 17, 3, 2, 3)


        self.gridLayout_5.addWidget(self.oam_frame, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(134, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 1, 2, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/note_add_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.oak_oam, icon3, "")
        self.bh_glyc_profile = QWidget()
        self.bh_glyc_profile.setObjectName(u"bh_glyc_profile")
        self.gridLayout_6 = QGridLayout(self.bh_glyc_profile)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(25)
        self.horizontalSpacer_7 = QSpacerItem(110, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.bh_frame = QFrame(self.bh_glyc_profile)
        self.bh_frame.setObjectName(u"bh_frame")
        self.bh_frame.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);\n"
"")
        self.gridLayout_3 = QGridLayout(self.bh_frame)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_12 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.lineEdit_bh_other_r_1 = QLineEdit(self.bh_frame)
        self.lineEdit_bh_other_r_1.setObjectName(u"lineEdit_bh_other_r_1")
        self.lineEdit_bh_other_r_1.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_other_r_1.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_other_r_1.setFont(font)
        self.lineEdit_bh_other_r_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_other_r_1, 10, 5, 1, 1)

        self.label_bh_gluc = QLabel(self.bh_frame)
        self.label_bh_gluc.setObjectName(u"label_bh_gluc")
        self.label_bh_gluc.setMaximumSize(QSize(16777215, 33))
        self.label_bh_gluc.setFont(font)
        self.label_bh_gluc.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_gluc, 1, 0, 1, 4)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_14, 1, 4, 1, 1)

        self.lineEdit_LSp_lponp = QLineEdit(self.bh_frame)
        self.lineEdit_LSp_lponp.setObjectName(u"lineEdit_LSp_lponp")
        self.lineEdit_LSp_lponp.setMinimumSize(QSize(0, 28))
        self.lineEdit_LSp_lponp.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_LSp_lponp.setFont(font)
        self.lineEdit_LSp_lponp.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_LSp_lponp, 16, 5, 1, 1)

        self.lineEdit_bh_mochevina = QLineEdit(self.bh_frame)
        self.lineEdit_bh_mochevina.setObjectName(u"lineEdit_bh_mochevina")
        self.lineEdit_bh_mochevina.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_mochevina.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_mochevina.setFont(font)
        self.lineEdit_bh_mochevina.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_mochevina, 4, 5, 1, 1)

        self.label_LSp_lponp = QLabel(self.bh_frame)
        self.label_LSp_lponp.setObjectName(u"label_LSp_lponp")
        self.label_LSp_lponp.setMaximumSize(QSize(16777215, 33))
        self.label_LSp_lponp.setFont(font)
        self.label_LSp_lponp.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_LSp_lponp, 16, 1, 1, 4)

        self.label_bh_ast = QLabel(self.bh_frame)
        self.label_bh_ast.setObjectName(u"label_bh_ast")
        self.label_bh_ast.setMaximumSize(QSize(16777215, 33))
        self.label_bh_ast.setFont(font)
        self.label_bh_ast.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_ast, 8, 0, 1, 5)

        self.label_LSp_lpvp = QLabel(self.bh_frame)
        self.label_LSp_lpvp.setObjectName(u"label_LSp_lpvp")
        self.label_LSp_lpvp.setMaximumSize(QSize(16777215, 33))
        self.label_LSp_lpvp.setFont(font)
        self.label_LSp_lpvp.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_LSp_lpvp, 14, 1, 1, 4)

        self.label_bh_alt = QLabel(self.bh_frame)
        self.label_bh_alt.setObjectName(u"label_bh_alt")
        self.label_bh_alt.setMaximumSize(QSize(16777215, 33))
        self.label_bh_alt.setFont(font)
        self.label_bh_alt.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_alt, 9, 0, 1, 5)

        self.lineEdit_bh_alt = QLineEdit(self.bh_frame)
        self.lineEdit_bh_alt.setObjectName(u"lineEdit_bh_alt")
        self.lineEdit_bh_alt.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_alt.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_alt.setFont(font)
        self.lineEdit_bh_alt.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_alt, 9, 5, 1, 1)

        self.label_lipid_spectr = QLabel(self.bh_frame)
        self.label_lipid_spectr.setObjectName(u"label_lipid_spectr")
        self.label_lipid_spectr.setMaximumSize(QSize(16777215, 33))
        self.label_lipid_spectr.setFont(font)
        self.label_lipid_spectr.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_lipid_spectr, 13, 0, 1, 5)

        self.lineEdit_bh_gluc = QLineEdit(self.bh_frame)
        self.lineEdit_bh_gluc.setObjectName(u"lineEdit_bh_gluc")
        self.lineEdit_bh_gluc.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_gluc.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_gluc.setFont(font)
        self.lineEdit_bh_gluc.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_gluc, 1, 5, 1, 1)

        self.lineEdit_bh_other_r_2 = QLineEdit(self.bh_frame)
        self.lineEdit_bh_other_r_2.setObjectName(u"lineEdit_bh_other_r_2")
        self.lineEdit_bh_other_r_2.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_other_r_2.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_other_r_2.setFont(font)
        self.lineEdit_bh_other_r_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_other_r_2, 11, 5, 1, 1)

        self.lineEdit_bh_Bilirubin_main = QLineEdit(self.bh_frame)
        self.lineEdit_bh_Bilirubin_main.setObjectName(u"lineEdit_bh_Bilirubin_main")
        self.lineEdit_bh_Bilirubin_main.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_Bilirubin_main.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_Bilirubin_main.setFont(font)
        self.lineEdit_bh_Bilirubin_main.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_Bilirubin_main, 5, 5, 1, 1)

        self.label_bh_mochevina = QLabel(self.bh_frame)
        self.label_bh_mochevina.setObjectName(u"label_bh_mochevina")
        self.label_bh_mochevina.setMaximumSize(QSize(16777215, 33))
        self.label_bh_mochevina.setFont(font)
        self.label_bh_mochevina.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_mochevina, 4, 0, 1, 5)

        self.lineEdit_LSp_triglic = QLineEdit(self.bh_frame)
        self.lineEdit_LSp_triglic.setObjectName(u"lineEdit_LSp_triglic")
        self.lineEdit_LSp_triglic.setMinimumSize(QSize(0, 28))
        self.lineEdit_LSp_triglic.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_LSp_triglic.setFont(font)
        self.lineEdit_LSp_triglic.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_LSp_triglic, 17, 5, 1, 1)

        self.lineEdit_bh_ast = QLineEdit(self.bh_frame)
        self.lineEdit_bh_ast.setObjectName(u"lineEdit_bh_ast")
        self.lineEdit_bh_ast.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_ast.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_ast.setFont(font)
        self.lineEdit_bh_ast.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_ast, 8, 5, 1, 1)

        self.label_bh_protein = QLabel(self.bh_frame)
        self.label_bh_protein.setObjectName(u"label_bh_protein")
        self.label_bh_protein.setMaximumSize(QSize(16777215, 33))
        self.label_bh_protein.setFont(font)
        self.label_bh_protein.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_protein, 2, 0, 1, 5)

        self.lineEdit_LSp_lpvp = QLineEdit(self.bh_frame)
        self.lineEdit_LSp_lpvp.setObjectName(u"lineEdit_LSp_lpvp")
        self.lineEdit_LSp_lpvp.setMinimumSize(QSize(0, 28))
        self.lineEdit_LSp_lpvp.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_LSp_lpvp.setFont(font)
        self.lineEdit_LSp_lpvp.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_LSp_lpvp, 14, 5, 1, 1)

        self.label_bh_holesterin = QLabel(self.bh_frame)
        self.label_bh_holesterin.setObjectName(u"label_bh_holesterin")
        self.label_bh_holesterin.setMaximumSize(QSize(16777215, 33))
        self.label_bh_holesterin.setFont(font)
        self.label_bh_holesterin.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_holesterin, 7, 0, 1, 5)

        self.label_LSp_triglic = QLabel(self.bh_frame)
        self.label_LSp_triglic.setObjectName(u"label_LSp_triglic")
        self.label_LSp_triglic.setMaximumSize(QSize(16777215, 33))
        self.label_LSp_triglic.setFont(font)
        self.label_LSp_triglic.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_LSp_triglic, 17, 1, 1, 4)

        self.label_bh_Bilirubin_main = QLabel(self.bh_frame)
        self.label_bh_Bilirubin_main.setObjectName(u"label_bh_Bilirubin_main")
        self.label_bh_Bilirubin_main.setMaximumSize(QSize(16777215, 33))
        self.label_bh_Bilirubin_main.setFont(font)
        self.label_bh_Bilirubin_main.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_Bilirubin_main, 5, 0, 1, 5)

        self.lineEdit_bh_creatinin = QLineEdit(self.bh_frame)
        self.lineEdit_bh_creatinin.setObjectName(u"lineEdit_bh_creatinin")
        self.lineEdit_bh_creatinin.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_creatinin.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_creatinin.setFont(font)
        self.lineEdit_bh_creatinin.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_creatinin, 3, 5, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 18, 2, 2, 1)

        self.lineEdit_bh_other_r_3 = QLineEdit(self.bh_frame)
        self.lineEdit_bh_other_r_3.setObjectName(u"lineEdit_bh_other_r_3")
        self.lineEdit_bh_other_r_3.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_other_r_3.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_other_r_3.setFont(font)
        self.lineEdit_bh_other_r_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_other_r_3, 12, 5, 1, 1)

        self.lineEdit_bh_holesterin = QLineEdit(self.bh_frame)
        self.lineEdit_bh_holesterin.setObjectName(u"lineEdit_bh_holesterin")
        self.lineEdit_bh_holesterin.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_holesterin.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_holesterin.setFont(font)
        self.lineEdit_bh_holesterin.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_holesterin, 7, 5, 1, 1)

        self.lineEdit_LSp_lpnp = QLineEdit(self.bh_frame)
        self.lineEdit_LSp_lpnp.setObjectName(u"lineEdit_LSp_lpnp")
        self.lineEdit_LSp_lpnp.setMinimumSize(QSize(0, 28))
        self.lineEdit_LSp_lpnp.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_LSp_lpnp.setFont(font)
        self.lineEdit_LSp_lpnp.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_LSp_lpnp, 15, 5, 1, 1)

        self.label_bh_creatinin = QLabel(self.bh_frame)
        self.label_bh_creatinin.setObjectName(u"label_bh_creatinin")
        self.label_bh_creatinin.setMaximumSize(QSize(16777215, 33))
        self.label_bh_creatinin.setFont(font)
        self.label_bh_creatinin.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_creatinin, 3, 0, 1, 5)

        self.lineEdit_bh_Bilirubin_svyaz = QLineEdit(self.bh_frame)
        self.lineEdit_bh_Bilirubin_svyaz.setObjectName(u"lineEdit_bh_Bilirubin_svyaz")
        self.lineEdit_bh_Bilirubin_svyaz.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_Bilirubin_svyaz.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_Bilirubin_svyaz.setFont(font)
        self.lineEdit_bh_Bilirubin_svyaz.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_Bilirubin_svyaz, 6, 5, 1, 1)

        self.label_LSp_lpnp = QLabel(self.bh_frame)
        self.label_LSp_lpnp.setObjectName(u"label_LSp_lpnp")
        self.label_LSp_lpnp.setMaximumSize(QSize(16777215, 33))
        self.label_LSp_lpnp.setFont(font)
        self.label_LSp_lpnp.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_LSp_lpnp, 15, 1, 1, 4)

        self.lineEdit_bh_protein = QLineEdit(self.bh_frame)
        self.lineEdit_bh_protein.setObjectName(u"lineEdit_bh_protein")
        self.lineEdit_bh_protein.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_protein.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_bh_protein.setFont(font)
        self.lineEdit_bh_protein.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_protein, 2, 5, 1, 1)

        self.label_bh_Bilirubin_svyaz = QLabel(self.bh_frame)
        self.label_bh_Bilirubin_svyaz.setObjectName(u"label_bh_Bilirubin_svyaz")
        self.label_bh_Bilirubin_svyaz.setMaximumSize(QSize(16777215, 33))
        self.label_bh_Bilirubin_svyaz.setFont(font)
        self.label_bh_Bilirubin_svyaz.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_bh_Bilirubin_svyaz, 6, 0, 1, 5)

        self.dateEdit_BhAK = QDateEdit(self.bh_frame)
        self.dateEdit_BhAK.setObjectName(u"dateEdit_BhAK")
        self.dateEdit_BhAK.setFont(font)
        self.dateEdit_BhAK.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.dateEdit_BhAK, 0, 4, 1, 2)

        self.label_BhAK_report = QLabel(self.bh_frame)
        self.label_BhAK_report.setObjectName(u"label_BhAK_report")
        self.label_BhAK_report.setMaximumSize(QSize(16777215, 33))
        self.label_BhAK_report.setFont(font)
        self.label_BhAK_report.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_BhAK_report.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_BhAK_report, 20, 0, 1, 6)

        self.lineEdit_bh_other_1 = QLineEdit(self.bh_frame)
        self.lineEdit_bh_other_1.setObjectName(u"lineEdit_bh_other_1")
        self.lineEdit_bh_other_1.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_other_1.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_bh_other_1.setFont(font)
        self.lineEdit_bh_other_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_other_1, 10, 0, 1, 5)

        self.lineEdit_bh_other_2 = QLineEdit(self.bh_frame)
        self.lineEdit_bh_other_2.setObjectName(u"lineEdit_bh_other_2")
        self.lineEdit_bh_other_2.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_other_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_bh_other_2.setFont(font)
        self.lineEdit_bh_other_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_other_2, 11, 0, 1, 5)

        self.lineEdit_bh_other_3 = QLineEdit(self.bh_frame)
        self.lineEdit_bh_other_3.setObjectName(u"lineEdit_bh_other_3")
        self.lineEdit_bh_other_3.setMinimumSize(QSize(0, 28))
        self.lineEdit_bh_other_3.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_bh_other_3.setFont(font)
        self.lineEdit_bh_other_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_bh_other_3, 12, 0, 1, 5)

        self.label_3 = QLabel(self.bh_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 3)

        self.pushButton_add_BhAK = QPushButton(self.bh_frame)
        self.pushButton_add_BhAK.setObjectName(u"pushButton_add_BhAK")
        self.pushButton_add_BhAK.setMinimumSize(QSize(0, 25))
        self.pushButton_add_BhAK.setFont(font2)
        self.pushButton_add_BhAK.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.pushButton_add_BhAK, 18, 3, 2, 3)


        self.gridLayout_6.addWidget(self.bh_frame, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.glyc_frame = QFrame(self.bh_glyc_profile)
        self.glyc_frame.setObjectName(u"glyc_frame")
        self.glyc_frame.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_4 = QGridLayout(self.glyc_frame)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_GlucPr_report = QLabel(self.glyc_frame)
        self.label_GlucPr_report.setObjectName(u"label_GlucPr_report")
        self.label_GlucPr_report.setMaximumSize(QSize(16777215, 33))
        self.label_GlucPr_report.setFont(font)
        self.label_GlucPr_report.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_GlucPr_report.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_GlucPr_report, 8, 0, 1, 6)

        self.lineEdit_glucprof_21_00 = QLineEdit(self.glyc_frame)
        self.lineEdit_glucprof_21_00.setObjectName(u"lineEdit_glucprof_21_00")
        self.lineEdit_glucprof_21_00.setMinimumSize(QSize(0, 28))
        self.lineEdit_glucprof_21_00.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_glucprof_21_00.setFont(font)
        self.lineEdit_glucprof_21_00.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit_glucprof_21_00, 4, 5, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_15, 1, 4, 4, 1)

        self.pushButton_add_GlucPr = QPushButton(self.glyc_frame)
        self.pushButton_add_GlucPr.setObjectName(u"pushButton_add_GlucPr")
        self.pushButton_add_GlucPr.setMinimumSize(QSize(0, 25))
        self.pushButton_add_GlucPr.setFont(font2)
        self.pushButton_add_GlucPr.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButton_add_GlucPr, 6, 2, 2, 4)

        self.lineEdit_glucprof_13_30 = QLineEdit(self.glyc_frame)
        self.lineEdit_glucprof_13_30.setObjectName(u"lineEdit_glucprof_13_30")
        self.lineEdit_glucprof_13_30.setMinimumSize(QSize(0, 28))
        self.lineEdit_glucprof_13_30.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_glucprof_13_30.setFont(font)
        self.lineEdit_glucprof_13_30.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit_glucprof_13_30, 2, 5, 1, 1)

        self.label_glucprof_08_00 = QLabel(self.glyc_frame)
        self.label_glucprof_08_00.setObjectName(u"label_glucprof_08_00")
        self.label_glucprof_08_00.setMaximumSize(QSize(16777215, 33))
        self.label_glucprof_08_00.setFont(font)
        self.label_glucprof_08_00.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_4.addWidget(self.label_glucprof_08_00, 1, 0, 1, 4)

        self.label_glucprof_17_30 = QLabel(self.glyc_frame)
        self.label_glucprof_17_30.setObjectName(u"label_glucprof_17_30")
        self.label_glucprof_17_30.setMaximumSize(QSize(16777215, 33))
        self.label_glucprof_17_30.setFont(font)
        self.label_glucprof_17_30.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_4.addWidget(self.label_glucprof_17_30, 3, 0, 1, 4)

        self.label_glucprof_21_00 = QLabel(self.glyc_frame)
        self.label_glucprof_21_00.setObjectName(u"label_glucprof_21_00")
        self.label_glucprof_21_00.setMaximumSize(QSize(16777215, 33))
        self.label_glucprof_21_00.setFont(font)
        self.label_glucprof_21_00.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_4.addWidget(self.label_glucprof_21_00, 4, 0, 1, 4)

        self.plainTextEdit_glucprof = QPlainTextEdit(self.glyc_frame)
        self.plainTextEdit_glucprof.setObjectName(u"plainTextEdit_glucprof")
        self.plainTextEdit_glucprof.setMaximumSize(QSize(16777215, 85))
        self.plainTextEdit_glucprof.setFont(font)
        self.plainTextEdit_glucprof.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.plainTextEdit_glucprof, 5, 0, 1, 6)

        self.lineEdit_glucprof_08_00 = QLineEdit(self.glyc_frame)
        self.lineEdit_glucprof_08_00.setObjectName(u"lineEdit_glucprof_08_00")
        self.lineEdit_glucprof_08_00.setMinimumSize(QSize(0, 28))
        self.lineEdit_glucprof_08_00.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_glucprof_08_00.setFont(font)
        self.lineEdit_glucprof_08_00.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit_glucprof_08_00, 1, 5, 1, 1)

        self.dateEdit_GlucPr = QDateEdit(self.glyc_frame)
        self.dateEdit_GlucPr.setObjectName(u"dateEdit_GlucPr")
        self.dateEdit_GlucPr.setFont(font)
        self.dateEdit_GlucPr.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.dateEdit_GlucPr, 0, 2, 1, 4)

        self.lineEdit_glucprof_17_30 = QLineEdit(self.glyc_frame)
        self.lineEdit_glucprof_17_30.setObjectName(u"lineEdit_glucprof_17_30")
        self.lineEdit_glucprof_17_30.setMinimumSize(QSize(0, 28))
        self.lineEdit_glucprof_17_30.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_glucprof_17_30.setFont(font)
        self.lineEdit_glucprof_17_30.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit_glucprof_17_30, 3, 5, 1, 1)

        self.label_glucprof_13_30 = QLabel(self.glyc_frame)
        self.label_glucprof_13_30.setObjectName(u"label_glucprof_13_30")
        self.label_glucprof_13_30.setMaximumSize(QSize(16777215, 33))
        self.label_glucprof_13_30.setFont(font)
        self.label_glucprof_13_30.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_4.addWidget(self.label_glucprof_13_30, 2, 0, 1, 4)

        self.horizontalSpacer_13 = QSpacerItem(15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_13, 0, 1, 1, 1)

        self.label_4 = QLabel(self.glyc_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 6, 0, 2, 1)


        self.verticalLayout.addWidget(self.glyc_frame)

        self.verticalSpacer_7 = QSpacerItem(178, 218, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)


        self.gridLayout_6.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(110, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 0, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(721, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 1, 1, 1, 2)

        self.tabWidget.addTab(self.bh_glyc_profile, icon3, "")
        self.custom = QWidget()
        self.custom.setObjectName(u"custom")
        self.gridLayout_9 = QGridLayout(self.custom)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_10 = QSpacerItem(266, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_10, 0, 0, 1, 1)

        self.my_lab_frame = QFrame(self.custom)
        self.my_lab_frame.setObjectName(u"my_lab_frame")
        self.my_lab_frame.setMinimumSize(QSize(450, 0))
        self.my_lab_frame.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);\n"
"")
        self.gridLayout_7 = QGridLayout(self.my_lab_frame)
        self.gridLayout_7.setSpacing(2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.dateEdit_my_lab = QDateEdit(self.my_lab_frame)
        self.dateEdit_my_lab.setObjectName(u"dateEdit_my_lab")
        self.dateEdit_my_lab.setMinimumSize(QSize(120, 0))
        self.dateEdit_my_lab.setMaximumSize(QSize(120, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(True)
        self.dateEdit_my_lab.setFont(font4)
        self.dateEdit_my_lab.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.dateEdit_my_lab, 3, 4, 1, 2)

        self.pushButton_mylab_clean = QPushButton(self.my_lab_frame)
        self.pushButton_mylab_clean.setObjectName(u"pushButton_mylab_clean")
        self.pushButton_mylab_clean.setMinimumSize(QSize(100, 25))
        self.pushButton_mylab_clean.setFont(font2)
        self.pushButton_mylab_clean.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_7.addWidget(self.pushButton_mylab_clean, 13, 1, 1, 1)

        self.comboBox_mylab_template = QComboBox(self.my_lab_frame)
        self.comboBox_mylab_template.setObjectName(u"comboBox_mylab_template")
        self.comboBox_mylab_template.setFont(font)
        self.comboBox_mylab_template.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_mylab_template.setEditable(True)

        self.gridLayout_7.addWidget(self.comboBox_mylab_template, 2, 1, 1, 3)

        self.lineEdit_my_lab_3 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_3.setObjectName(u"lineEdit_my_lab_3")
        self.lineEdit_my_lab_3.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_3.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_3.setFont(font4)
        self.lineEdit_my_lab_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_3, 6, 0, 1, 4)

        self.lineEdit_my_lab_7 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_7.setObjectName(u"lineEdit_my_lab_7")
        self.lineEdit_my_lab_7.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_7.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_7.setFont(font4)
        self.lineEdit_my_lab_7.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_7, 10, 0, 1, 4)

        self.lineEdit_my_lab_6 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_6.setObjectName(u"lineEdit_my_lab_6")
        self.lineEdit_my_lab_6.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_6.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_6.setFont(font4)
        self.lineEdit_my_lab_6.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_6, 9, 0, 1, 4)

        self.lineEdit_my_lab_r_3 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_r_3.setObjectName(u"lineEdit_my_lab_r_3")
        self.lineEdit_my_lab_r_3.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_r_3.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_my_lab_r_3.setFont(font4)
        self.lineEdit_my_lab_r_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_r_3, 6, 5, 1, 1)

        self.lineEdit_my_lab_r_5 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_r_5.setObjectName(u"lineEdit_my_lab_r_5")
        self.lineEdit_my_lab_r_5.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_r_5.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_my_lab_r_5.setFont(font4)
        self.lineEdit_my_lab_r_5.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_r_5, 8, 5, 1, 1)

        self.lineEdit_my_lab_8 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_8.setObjectName(u"lineEdit_my_lab_8")
        self.lineEdit_my_lab_8.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_8.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_8.setFont(font4)
        self.lineEdit_my_lab_8.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_8, 11, 0, 1, 4)

        self.label_my_lab_template = QLabel(self.my_lab_frame)
        self.label_my_lab_template.setObjectName(u"label_my_lab_template")
        self.label_my_lab_template.setMaximumSize(QSize(16777215, 33))
        self.label_my_lab_template.setFont(font)
        self.label_my_lab_template.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_7.addWidget(self.label_my_lab_template, 2, 0, 1, 1)

        self.label_my_lab_report = QLabel(self.my_lab_frame)
        self.label_my_lab_report.setObjectName(u"label_my_lab_report")
        self.label_my_lab_report.setMaximumSize(QSize(16777215, 33))
        self.label_my_lab_report.setFont(font)
        self.label_my_lab_report.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_my_lab_report.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_my_lab_report, 14, 0, 1, 6)

        self.lineEdit_my_lab_r_8 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_r_8.setObjectName(u"lineEdit_my_lab_r_8")
        self.lineEdit_my_lab_r_8.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_r_8.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_my_lab_r_8.setFont(font4)
        self.lineEdit_my_lab_r_8.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_r_8, 11, 5, 1, 1)

        self.lineEdit_my_lab_2 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_2.setObjectName(u"lineEdit_my_lab_2")
        self.lineEdit_my_lab_2.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_2.setFont(font4)
        self.lineEdit_my_lab_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_2, 5, 0, 1, 4)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 12, 2, 2, 1)

        self.pushButton_add_mylab = QPushButton(self.my_lab_frame)
        self.pushButton_add_mylab.setObjectName(u"pushButton_add_mylab")
        self.pushButton_add_mylab.setMinimumSize(QSize(0, 25))
        self.pushButton_add_mylab.setFont(font2)
        self.pushButton_add_mylab.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_7.addWidget(self.pushButton_add_mylab, 13, 3, 1, 3)

        self.lineEdit_my_lab_r_1 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_r_1.setObjectName(u"lineEdit_my_lab_r_1")
        self.lineEdit_my_lab_r_1.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_r_1.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_my_lab_r_1.setFont(font4)
        self.lineEdit_my_lab_r_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_r_1, 4, 5, 1, 1)

        self.lineEdit_my_lab_r_6 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_r_6.setObjectName(u"lineEdit_my_lab_r_6")
        self.lineEdit_my_lab_r_6.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_r_6.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_my_lab_r_6.setFont(font4)
        self.lineEdit_my_lab_r_6.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_r_6, 9, 5, 1, 1)

        self.lineEdit_my_lab_r_2 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_r_2.setObjectName(u"lineEdit_my_lab_r_2")
        self.lineEdit_my_lab_r_2.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_r_2.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_my_lab_r_2.setFont(font4)
        self.lineEdit_my_lab_r_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_r_2, 5, 5, 1, 1)

        self.label_6 = QLabel(self.my_lab_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 6)

        self.lineEdit_my_lab_r_4 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_r_4.setObjectName(u"lineEdit_my_lab_r_4")
        self.lineEdit_my_lab_r_4.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_r_4.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_my_lab_r_4.setFont(font4)
        self.lineEdit_my_lab_r_4.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_r_4, 7, 5, 1, 1)

        self.lineEdit_my_lab_1 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_1.setObjectName(u"lineEdit_my_lab_1")
        self.lineEdit_my_lab_1.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_1.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_1.setFont(font4)
        self.lineEdit_my_lab_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_1, 4, 0, 1, 4)

        self.lineEdit_my_lab_r_7 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_r_7.setObjectName(u"lineEdit_my_lab_r_7")
        self.lineEdit_my_lab_r_7.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_r_7.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_my_lab_r_7.setFont(font4)
        self.lineEdit_my_lab_r_7.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_r_7, 10, 5, 1, 1)

        self.pushButton_insert_mylab_template = QPushButton(self.my_lab_frame)
        self.pushButton_insert_mylab_template.setObjectName(u"pushButton_insert_mylab_template")
        self.pushButton_insert_mylab_template.setMinimumSize(QSize(0, 25))
        self.pushButton_insert_mylab_template.setFont(font2)
        self.pushButton_insert_mylab_template.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_7.addWidget(self.pushButton_insert_mylab_template, 2, 5, 1, 1)

        self.lineEdit_my_lab_name = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_name.setObjectName(u"lineEdit_my_lab_name")
        self.lineEdit_my_lab_name.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_name.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_name.setFont(font4)
        self.lineEdit_my_lab_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 2px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_name, 3, 0, 1, 4)

        self.lineEdit_my_lab_5 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_5.setObjectName(u"lineEdit_my_lab_5")
        self.lineEdit_my_lab_5.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_5.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_5.setFont(font4)
        self.lineEdit_my_lab_5.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_5, 8, 0, 1, 4)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_9, 5, 4, 1, 1)

        self.lineEdit_my_lab_4 = QLineEdit(self.my_lab_frame)
        self.lineEdit_my_lab_4.setObjectName(u"lineEdit_my_lab_4")
        self.lineEdit_my_lab_4.setMinimumSize(QSize(0, 28))
        self.lineEdit_my_lab_4.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_my_lab_4.setFont(font4)
        self.lineEdit_my_lab_4.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_my_lab_4, 7, 0, 1, 4)

        self.frame_tpl = QFrame(self.my_lab_frame)
        self.frame_tpl.setObjectName(u"frame_tpl")
        self.frame_tpl.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);\n"
"")
        self.gridLayout_8 = QGridLayout(self.frame_tpl)
        self.gridLayout_8.setSpacing(2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(2, 2, 2, 2)
        self.checkBox_mylab = QCheckBox(self.frame_tpl)
        self.checkBox_mylab.setObjectName(u"checkBox_mylab")
        self.checkBox_mylab.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"   color: #EEEEEE;\n"
"}\n"
" \n"
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
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #EEEEEE;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")
        self.checkBox_mylab.setChecked(True)

        self.gridLayout_8.addWidget(self.checkBox_mylab, 1, 0, 1, 2)

        self.pushButton_save_mylab_template = QPushButton(self.frame_tpl)
        self.pushButton_save_mylab_template.setObjectName(u"pushButton_save_mylab_template")
        self.pushButton_save_mylab_template.setMinimumSize(QSize(100, 0))
        self.pushButton_save_mylab_template.setFont(font2)
        self.pushButton_save_mylab_template.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_8.addWidget(self.pushButton_save_mylab_template, 2, 1, 1, 1)

        self.lineEdit_mylab_template = QLineEdit(self.frame_tpl)
        self.lineEdit_mylab_template.setObjectName(u"lineEdit_mylab_template")
        self.lineEdit_mylab_template.setEnabled(False)
        self.lineEdit_mylab_template.setFont(font4)
        self.lineEdit_mylab_template.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_mylab_template, 2, 0, 1, 1)

        self.label_5 = QLabel(self.frame_tpl)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.frame_tpl, 15, 0, 1, 6)


        self.gridLayout_9.addWidget(self.my_lab_frame, 0, 1, 2, 1)

        self.horizontalSpacer_11 = QSpacerItem(266, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_11, 1, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_10, 2, 1, 1, 1)

        self.tabWidget.addTab(self.custom, icon3, "")
        self.result = QWidget()
        self.result.setObjectName(u"result")
        self.gridLayout_10 = QGridLayout(self.result)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.textEdit_lab_result = QTextEdit(self.result)
        self.textEdit_lab_result.setObjectName(u"textEdit_lab_result")
        self.textEdit_lab_result.setMinimumSize(QSize(800, 550))
        self.textEdit_lab_result.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_10.addWidget(self.textEdit_lab_result, 0, 1, 2, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 47, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_11, 2, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(91, 547, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_17, 0, 2, 2, 1)

        self.horizontalSpacer_16 = QSpacerItem(91, 547, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_16, 0, 0, 2, 1)

        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/create_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.result, icon4, "")

        self.gridLayout_11.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.main)

        QWidget.setTabOrder(self.dateEdit_OAK, self.lineEdit_Er)
        QWidget.setTabOrder(self.lineEdit_Er, self.lineEdit_Hb)
        QWidget.setTabOrder(self.lineEdit_Hb, self.lineEdit_color)
        QWidget.setTabOrder(self.lineEdit_color, self.lineEdit_Ht)
        QWidget.setTabOrder(self.lineEdit_Ht, self.lineEdit_Le)
        QWidget.setTabOrder(self.lineEdit_Le, self.lineEdit_Le_B)
        QWidget.setTabOrder(self.lineEdit_Le_B, self.lineEdit_Le_Eoz)
        QWidget.setTabOrder(self.lineEdit_Le_Eoz, self.lineEdit_Le_N_yu)
        QWidget.setTabOrder(self.lineEdit_Le_N_yu, self.lineEdit_Le_N_p)
        QWidget.setTabOrder(self.lineEdit_Le_N_p, self.lineEdit_Le_N_s)
        QWidget.setTabOrder(self.lineEdit_Le_N_s, self.lineEdit_Le_M)
        QWidget.setTabOrder(self.lineEdit_Le_M, self.lineEdit_Le_Lym)
        QWidget.setTabOrder(self.lineEdit_Le_Lym, self.lineEdit_Tr)
        QWidget.setTabOrder(self.lineEdit_Tr, self.lineEdit_soe)
        QWidget.setTabOrder(self.lineEdit_soe, self.lineEdit_OAK_other)
        QWidget.setTabOrder(self.lineEdit_OAK_other, self.lineEdit_OAK_other_r)
        QWidget.setTabOrder(self.lineEdit_OAK_other_r, self.pushButton_add_OAK)
        QWidget.setTabOrder(self.pushButton_add_OAK, self.dateEdit_OAM)
        QWidget.setTabOrder(self.dateEdit_OAM, self.lineEdit_urine_color)
        QWidget.setTabOrder(self.lineEdit_urine_color, self.lineEdit_urine_light)
        QWidget.setTabOrder(self.lineEdit_urine_light, self.lineEdit_urine_protein)
        QWidget.setTabOrder(self.lineEdit_urine_protein, self.lineEdit_urine_gluc)
        QWidget.setTabOrder(self.lineEdit_urine_gluc, self.lineEdit_urine_aceton)
        QWidget.setTabOrder(self.lineEdit_urine_aceton, self.lineEdit_udel_ves)
        QWidget.setTabOrder(self.lineEdit_udel_ves, self.lineEdit_urine_Le)
        QWidget.setTabOrder(self.lineEdit_urine_Le, self.lineEdit_urine_Er)
        QWidget.setTabOrder(self.lineEdit_urine_Er, self.lineEdit_urine_epit_pl)
        QWidget.setTabOrder(self.lineEdit_urine_epit_pl, self.lineEdit_urine_epit_zern)
        QWidget.setTabOrder(self.lineEdit_urine_epit_zern, self.lineEdit_urine_epit_ren)
        QWidget.setTabOrder(self.lineEdit_urine_epit_ren, self.lineEdit_urine_cilindr)
        QWidget.setTabOrder(self.lineEdit_urine_cilindr, self.lineEdit_urine_salt)
        QWidget.setTabOrder(self.lineEdit_urine_salt, self.lineEdit_urine_slime)
        QWidget.setTabOrder(self.lineEdit_urine_slime, self.lineEdit_urine_Bacteria)
        QWidget.setTabOrder(self.lineEdit_urine_Bacteria, self.lineEdit_urine_other)
        QWidget.setTabOrder(self.lineEdit_urine_other, self.lineEdit_urine_other_r)
        QWidget.setTabOrder(self.lineEdit_urine_other_r, self.pushButton_add_OAM)
        QWidget.setTabOrder(self.pushButton_add_OAM, self.dateEdit_BhAK)
        QWidget.setTabOrder(self.dateEdit_BhAK, self.lineEdit_bh_gluc)
        QWidget.setTabOrder(self.lineEdit_bh_gluc, self.lineEdit_bh_protein)
        QWidget.setTabOrder(self.lineEdit_bh_protein, self.lineEdit_bh_creatinin)
        QWidget.setTabOrder(self.lineEdit_bh_creatinin, self.lineEdit_bh_mochevina)
        QWidget.setTabOrder(self.lineEdit_bh_mochevina, self.lineEdit_bh_Bilirubin_main)
        QWidget.setTabOrder(self.lineEdit_bh_Bilirubin_main, self.lineEdit_bh_Bilirubin_svyaz)
        QWidget.setTabOrder(self.lineEdit_bh_Bilirubin_svyaz, self.lineEdit_bh_holesterin)
        QWidget.setTabOrder(self.lineEdit_bh_holesterin, self.lineEdit_bh_ast)
        QWidget.setTabOrder(self.lineEdit_bh_ast, self.lineEdit_bh_alt)
        QWidget.setTabOrder(self.lineEdit_bh_alt, self.lineEdit_bh_other_1)
        QWidget.setTabOrder(self.lineEdit_bh_other_1, self.lineEdit_bh_other_r_1)
        QWidget.setTabOrder(self.lineEdit_bh_other_r_1, self.lineEdit_bh_other_2)
        QWidget.setTabOrder(self.lineEdit_bh_other_2, self.lineEdit_bh_other_r_2)
        QWidget.setTabOrder(self.lineEdit_bh_other_r_2, self.lineEdit_bh_other_3)
        QWidget.setTabOrder(self.lineEdit_bh_other_3, self.lineEdit_bh_other_r_3)
        QWidget.setTabOrder(self.lineEdit_bh_other_r_3, self.lineEdit_LSp_lpvp)
        QWidget.setTabOrder(self.lineEdit_LSp_lpvp, self.lineEdit_LSp_lpnp)
        QWidget.setTabOrder(self.lineEdit_LSp_lpnp, self.lineEdit_LSp_lponp)
        QWidget.setTabOrder(self.lineEdit_LSp_lponp, self.lineEdit_LSp_triglic)
        QWidget.setTabOrder(self.lineEdit_LSp_triglic, self.pushButton_add_BhAK)
        QWidget.setTabOrder(self.pushButton_add_BhAK, self.dateEdit_GlucPr)
        QWidget.setTabOrder(self.dateEdit_GlucPr, self.lineEdit_glucprof_08_00)
        QWidget.setTabOrder(self.lineEdit_glucprof_08_00, self.lineEdit_glucprof_13_30)
        QWidget.setTabOrder(self.lineEdit_glucprof_13_30, self.lineEdit_glucprof_17_30)
        QWidget.setTabOrder(self.lineEdit_glucprof_17_30, self.lineEdit_glucprof_21_00)
        QWidget.setTabOrder(self.lineEdit_glucprof_21_00, self.plainTextEdit_glucprof)
        QWidget.setTabOrder(self.plainTextEdit_glucprof, self.pushButton_add_GlucPr)
        QWidget.setTabOrder(self.pushButton_add_GlucPr, self.lineEdit_my_lab_name)
        QWidget.setTabOrder(self.lineEdit_my_lab_name, self.dateEdit_my_lab)
        QWidget.setTabOrder(self.dateEdit_my_lab, self.lineEdit_my_lab_1)
        QWidget.setTabOrder(self.lineEdit_my_lab_1, self.lineEdit_my_lab_r_1)
        QWidget.setTabOrder(self.lineEdit_my_lab_r_1, self.lineEdit_my_lab_2)
        QWidget.setTabOrder(self.lineEdit_my_lab_2, self.lineEdit_my_lab_r_2)
        QWidget.setTabOrder(self.lineEdit_my_lab_r_2, self.lineEdit_my_lab_3)
        QWidget.setTabOrder(self.lineEdit_my_lab_3, self.lineEdit_my_lab_r_3)
        QWidget.setTabOrder(self.lineEdit_my_lab_r_3, self.lineEdit_my_lab_4)
        QWidget.setTabOrder(self.lineEdit_my_lab_4, self.lineEdit_my_lab_r_4)
        QWidget.setTabOrder(self.lineEdit_my_lab_r_4, self.lineEdit_my_lab_5)
        QWidget.setTabOrder(self.lineEdit_my_lab_5, self.lineEdit_my_lab_r_5)
        QWidget.setTabOrder(self.lineEdit_my_lab_r_5, self.lineEdit_my_lab_6)
        QWidget.setTabOrder(self.lineEdit_my_lab_6, self.lineEdit_my_lab_r_6)
        QWidget.setTabOrder(self.lineEdit_my_lab_r_6, self.lineEdit_my_lab_7)
        QWidget.setTabOrder(self.lineEdit_my_lab_7, self.lineEdit_my_lab_r_7)
        QWidget.setTabOrder(self.lineEdit_my_lab_r_7, self.lineEdit_my_lab_8)
        QWidget.setTabOrder(self.lineEdit_my_lab_8, self.lineEdit_my_lab_r_8)
        QWidget.setTabOrder(self.lineEdit_my_lab_r_8, self.pushButton_add_mylab)
        QWidget.setTabOrder(self.pushButton_add_mylab, self.pushButton_mylab_clean)
        QWidget.setTabOrder(self.pushButton_mylab_clean, self.checkBox_mylab)
        QWidget.setTabOrder(self.checkBox_mylab, self.lineEdit_mylab_template)
        QWidget.setTabOrder(self.lineEdit_mylab_template, self.pushButton_save_mylab_template)
        QWidget.setTabOrder(self.pushButton_save_mylab_template, self.comboBox_mylab_template)
        QWidget.setTabOrder(self.comboBox_mylab_template, self.pushButton_insert_mylab_template)
        QWidget.setTabOrder(self.pushButton_insert_mylab_template, self.pushButtonNotSaveExit)
        QWidget.setTabOrder(self.pushButtonNotSaveExit, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.pushButtonHelp)
        QWidget.setTabOrder(self.pushButtonHelp, self.textEdit_lab_result)

        self.retranslateUi(Lab_data)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Lab_data)
    # setupUi

    def retranslateUi(self, Lab_data):
        Lab_data.setWindowTitle(QCoreApplication.translate("Lab_data", u"Form", None))
        self.label_Pt_info.setText(QCoreApplication.translate("Lab_data", u"PatientInfo\n"
"fff", None))
        self.labelTimeline.setText("")
        self.groupBox_wom.setTitle(QCoreApplication.translate("Lab_data", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("Lab_data", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("Lab_data", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("Lab_data", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.label_OAK_report.setText(QCoreApplication.translate("Lab_data", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_Er.setText(QCoreApplication.translate("Lab_data", u"\u042d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u044b, \u044510(^12)/\u043b", None))
        self.label_Le_Lym.setText(QCoreApplication.translate("Lab_data", u"\u041b\u0438\u043c\u0444\u043e\u0446\u0438\u0442\u044b, %", None))
        self.label_Le_N_s.setText(QCoreApplication.translate("Lab_data", u"\u0441\u0435\u0433\u043c\u0435\u043d\u0442\u043e\u044f\u0434\u0435\u0440\u043d\u044b\u0435, %", None))
        self.label_Ht.setText(QCoreApplication.translate("Lab_data", u"\u0413\u0435\u043c\u0430\u0442\u043e\u043a\u0440\u0438\u0442, %", None))
        self.label_soe.setText(QCoreApplication.translate("Lab_data", u"\u0421\u041e\u042d, \u0441\u0435\u043a", None))
        self.label_Le.setText(QCoreApplication.translate("Lab_data", u"\u041b\u0435\u0439\u043a\u043e\u0446\u0438\u0442\u044b, \u044510(^9)/\u043b", None))
        self.label_Le_M.setText(QCoreApplication.translate("Lab_data", u"\u041c\u043e\u043d\u043e\u0446\u0438\u0442\u044b, %", None))
        self.label_Le_N_p.setText(QCoreApplication.translate("Lab_data", u"\u043f\u0430\u043b\u043e\u0447\u043a\u043e\u044f\u0434\u0435\u0440\u043d\u044b\u0435, %", None))
        self.label_Le_N_yu.setText(QCoreApplication.translate("Lab_data", u"\u044e\u043d\u044b\u0435 (\u043c\u0435\u0442\u0430\u043c\u0438\u0435\u043b\u043e\u0446\u0438\u0442\u044b), %", None))
        self.label_Tr.setText(QCoreApplication.translate("Lab_data", u"\u0422\u0440\u043e\u043c\u0431\u043e\u0446\u0438\u0442\u044b, \u044510(^9)/\u043b", None))
        self.label_Le_Eoz.setText(QCoreApplication.translate("Lab_data", u"\u042d\u043e\u0437\u0438\u043d\u043e\u0444\u0438\u043b\u044b, %", None))
        self.label_Le_N.setText(QCoreApplication.translate("Lab_data", u"<html><head/><body><p>\u041d<br/>\u0435<br/>\u0439<br/>\u0442<br/>\u0440<br/>\u043e<br/>\u0444<br/>\u0438<br/>\u043b<br/>\u044b</p></body></html>", None))
        self.label_color.setText(QCoreApplication.translate("Lab_data", u"\u0426\u0432\u0435\u0442\u043e\u0432\u043e\u0439 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c, \u043f\u0433", None))
        self.label_Le_B.setText(QCoreApplication.translate("Lab_data", u"\u0411\u0430\u0437\u043e\u0444\u0438\u043b\u044b, %", None))
        self.label_Hb.setText(QCoreApplication.translate("Lab_data", u"\u0413\u0435\u043c\u043e\u0433\u043b\u043e\u0431\u0438\u043d, \u0433/\u043b", None))
        self.label.setText(QCoreApplication.translate("Lab_data", u"\u041e\u0431\u0449\u0438\u0439 \u0430\u043d\u0430\u043b\u0438\u0437 \u043a\u0440\u043e\u0432\u0438", None))
        self.pushButton_add_OAK.setText(QCoreApplication.translate("Lab_data", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_urine_gluc.setText(QCoreApplication.translate("Lab_data", u"\u0413\u043b\u044e\u043a\u043e\u0437\u0430, \u043a\u0430\u0447.", None))
        self.label_urine_protein.setText(QCoreApplication.translate("Lab_data", u"\u0411\u0435\u043b\u043e\u043a, \u0433/\u043b", None))
        self.label_OAM_report.setText(QCoreApplication.translate("Lab_data", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lineEdit_urine_protein.setText(QCoreApplication.translate("Lab_data", u"\u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u043e", None))
        self.lineEdit_urine_color.setText(QCoreApplication.translate("Lab_data", u"\u0441\u0432\u0435\u0442\u043b\u043e-\u0436\u0435\u043b\u0442\u044b\u0439", None))
        self.label_urine_Le.setText(QCoreApplication.translate("Lab_data", u"\u041b\u0435\u0439\u043a\u043e\u0446\u0438\u0442\u044b, \u0432 \u043f.\u0437.", None))
        self.label_urine_cilindr.setText(QCoreApplication.translate("Lab_data", u"\u0426\u0438\u043b\u0438\u043d\u0434\u0440\u044b, \u0432 \u043f.\u0437.", None))
        self.label_urine_Bacteria.setText(QCoreApplication.translate("Lab_data", u"\u0411\u0430\u043a\u0442\u0435\u0440\u0438\u0438", None))
        self.label_urine_epit_pl.setText(QCoreApplication.translate("Lab_data", u"\u042d\u043f\u0438\u0442\u0435\u043b\u0438\u0439 \u043f\u043b\u043e\u0441\u043a., \u0432 \u043f.\u0437.", None))
        self.lineEdit_udel_ves.setText(QCoreApplication.translate("Lab_data", u"\u043c/\u043c", None))
        self.label_urine_color.setText(QCoreApplication.translate("Lab_data", u"\u0426\u0432\u0435\u0442", None))
        self.label_urine_epit_ren.setText(QCoreApplication.translate("Lab_data", u"\u042d\u043f\u0438\u0442\u0435\u043b\u0438\u0439 \u043f\u043e\u0447., \u0432 \u043f.\u0437.", None))
        self.label_urine_Er.setText(QCoreApplication.translate("Lab_data", u"\u042d\u0440\u0438\u0442\u0440\u043e\u0446\u0438\u0442\u044b, \u0432 \u043f.\u0437.", None))
        self.lineEdit_urine_aceton.setText(QCoreApplication.translate("Lab_data", u"\u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u043e", None))
        self.label_urine_slime.setText(QCoreApplication.translate("Lab_data", u"\u0421\u043b\u0438\u0437\u044c, \u043f\u0440\u0438\u043c\u0435\u0441\u0438", None))
        self.label_urine_epit_zern.setText(QCoreApplication.translate("Lab_data", u"\u042d\u043f\u0438\u0442\u0435\u043b\u0438\u0439 \u0437\u0435\u0440\u043d., \u0432 \u043f.\u0437.", None))
        self.lineEdit_urine_gluc.setText(QCoreApplication.translate("Lab_data", u"\u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u043e", None))
        self.label_udel_ves.setText(QCoreApplication.translate("Lab_data", u"\u0423\u0434\u0435\u043b\u044c\u043d\u044b\u0439 \u0432\u0435\u0441", None))
        self.lineEdit_urine_light.setText(QCoreApplication.translate("Lab_data", u"\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f", None))
        self.label_urine_aceton.setText(QCoreApplication.translate("Lab_data", u"\u041a\u0435\u0442\u043e\u043d\u043e\u0432\u044b\u0435 \u0442\u0435\u043b\u0430, \u043a\u0430\u0447.", None))
        self.label_urine_light.setText(QCoreApplication.translate("Lab_data", u"\u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c", None))
        self.label_urine_salt.setText(QCoreApplication.translate("Lab_data", u"\u0421\u043e\u043b\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Lab_data", u"\u041e\u0431\u0449\u0438\u0439 \u0430\u043d\u0430\u043b\u0438\u0437 \u043c\u043e\u0447\u0438", None))
        self.pushButton_add_OAM.setText(QCoreApplication.translate("Lab_data", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.oak_oam), QCoreApplication.translate("Lab_data", u"  \u041e\u0410\u041a, \u041e\u0410\u041c   ", None))
        self.label_bh_gluc.setText(QCoreApplication.translate("Lab_data", u"\u0413\u043b\u044e\u043a\u043e\u0437\u0430, \u043c\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_LSp_lponp.setText(QCoreApplication.translate("Lab_data", u"\u041b\u041f\u041e\u041d\u041f, \u043c\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_bh_ast.setText(QCoreApplication.translate("Lab_data", u"\u0410\u0421\u0422, \u0435\u0434/\u043b", None))
        self.label_LSp_lpvp.setText(QCoreApplication.translate("Lab_data", u"\u041b\u041f\u0412\u041f, \u043c\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_bh_alt.setText(QCoreApplication.translate("Lab_data", u"\u0410\u041b\u0422, \u0435\u0434/\u043b", None))
        self.label_lipid_spectr.setText(QCoreApplication.translate("Lab_data", u"<html><head/><body><p>\u041b\u0438\u043f\u0438\u0434\u043d\u044b\u0439 \u0441\u043f\u0435\u043a\u0442\u0440</p></body></html>", None))
        self.label_bh_mochevina.setText(QCoreApplication.translate("Lab_data", u"\u041c\u043e\u0447\u0435\u0432\u0438\u043d\u0430, \u043c\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_bh_protein.setText(QCoreApplication.translate("Lab_data", u"\u041e\u0431\u0449\u0438\u0439 \u0431\u0435\u043b\u043e\u043a, \u0433/\u043b", None))
        self.label_bh_holesterin.setText(QCoreApplication.translate("Lab_data", u"\u0425\u043e\u043b\u0435\u0441\u0442\u0435\u0440\u0438\u043d \u043e\u0431\u0449\u0438\u0439, \u043c\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_LSp_triglic.setText(QCoreApplication.translate("Lab_data", u"\u0422\u0440\u0438\u0433\u043b\u0438\u0446\u0435\u0440\u0438\u0434\u044b, \u043c\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_bh_Bilirubin_main.setText(QCoreApplication.translate("Lab_data", u"\u0411\u0438\u043b\u0438\u0440\u0443\u0431\u0438\u043d \u043e\u0431\u0449\u0438\u0439, \u043c\u043a\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_bh_creatinin.setText(QCoreApplication.translate("Lab_data", u"\u041a\u0440\u0435\u0430\u0442\u0438\u043d\u0438\u043d, \u043c\u043a\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_LSp_lpnp.setText(QCoreApplication.translate("Lab_data", u"\u041b\u041f\u041d\u041f, \u043c\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_bh_Bilirubin_svyaz.setText(QCoreApplication.translate("Lab_data", u"\u0411\u0438\u043b\u0438\u0440\u0443\u0431\u0438\u043d \u0441\u0432\u044f\u0437\u0430\u043d\u044b\u0439, \u043c\u043a\u043c\u043e\u043b\u044c/\u043b", None))
        self.label_BhAK_report.setText(QCoreApplication.translate("Lab_data", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Lab_data", u"\u0411\u0438\u043e\u0445\u0438\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u043d\u0430\u043b\u0438\u0437 \u043a\u0440\u043e\u0432\u0438", None))
        self.pushButton_add_BhAK.setText(QCoreApplication.translate("Lab_data", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_GlucPr_report.setText(QCoreApplication.translate("Lab_data", u"<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_add_GlucPr.setText(QCoreApplication.translate("Lab_data", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_glucprof_08_00.setText(QCoreApplication.translate("Lab_data", u"\u0413\u043b\u044e\u043a\u043e\u0437\u0430, \u043c\u043c\u043e\u043b\u044c/\u043b // 08:00", None))
        self.label_glucprof_17_30.setText(QCoreApplication.translate("Lab_data", u"\u0413\u043b\u044e\u043a\u043e\u0437\u0430, \u043c\u043c\u043e\u043b\u044c/\u043b // 17:30", None))
        self.label_glucprof_21_00.setText(QCoreApplication.translate("Lab_data", u"\u0413\u043b\u044e\u043a\u043e\u0437\u0430, \u043c\u043c\u043e\u043b\u044c/\u043b // 21:00", None))
        self.plainTextEdit_glucprof.setPlaceholderText(QCoreApplication.translate("Lab_data", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0434\u0438\u0435\u0442\u0443 \u0438 \u0433\u0438\u043f\u043e\u0433\u043b\u0438\u043a\u0435\u043c\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0442\u0435\u0440\u0430\u043f\u0438\u044e \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0435\u0442\u0441\u044f \u0433\u043b\u0438\u043a\u0435\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c, \u0435\u0441\u043b\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e", None))
        self.label_glucprof_13_30.setText(QCoreApplication.translate("Lab_data", u"\u0413\u043b\u044e\u043a\u043e\u0437\u0430, \u043c\u043c\u043e\u043b\u044c/\u043b // 13:30", None))
        self.label_4.setText(QCoreApplication.translate("Lab_data", u"\u0413\u043b\u0438\u043a\u0435\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bh_glyc_profile), QCoreApplication.translate("Lab_data", u"             \u0411/\u0445 \u0410\u041a, \u0433\u043b\u0438\u043a\u0435\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c             ", None))
        self.pushButton_mylab_clean.setText(QCoreApplication.translate("Lab_data", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.comboBox_mylab_template.setPlaceholderText(QCoreApplication.translate("Lab_data", u"\u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.lineEdit_my_lab_3.setPlaceholderText(QCoreApplication.translate("Lab_data", u"                             \u0438 \u0442.\u0434.", None))
        self.lineEdit_my_lab_7.setPlaceholderText("")
        self.lineEdit_my_lab_6.setPlaceholderText("")
        self.lineEdit_my_lab_8.setPlaceholderText("")
        self.label_my_lab_template.setText(QCoreApplication.translate("Lab_data", u"<html><head/><body><p align=\"right\">\u0428\u0430\u0431\u043b\u043e\u043d</p></body></html>", None))
        self.label_my_lab_report.setText(QCoreApplication.translate("Lab_data", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lineEdit_my_lab_2.setPlaceholderText(QCoreApplication.translate("Lab_data", u"\u041b\u0430\u0431.\u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c # 2", None))
        self.pushButton_add_mylab.setText(QCoreApplication.translate("Lab_data", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("Lab_data", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u044b\u0439 \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437", None))
        self.lineEdit_my_lab_1.setPlaceholderText(QCoreApplication.translate("Lab_data", u"\u041b\u0430\u0431.\u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c # 1", None))
        self.pushButton_insert_mylab_template.setText(QCoreApplication.translate("Lab_data", u"\u0432\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        self.lineEdit_my_lab_name.setPlaceholderText(QCoreApplication.translate("Lab_data", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
        self.lineEdit_my_lab_5.setPlaceholderText("")
        self.lineEdit_my_lab_4.setPlaceholderText("")
        self.checkBox_mylab.setText(QCoreApplication.translate("Lab_data", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
        self.pushButton_save_mylab_template.setText(QCoreApplication.translate("Lab_data", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.lineEdit_mylab_template.setPlaceholderText(QCoreApplication.translate("Lab_data", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Lab_data", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.custom), QCoreApplication.translate("Lab_data", u"     \u0421\u0432\u043e\u0439 \u0430\u043d\u0430\u043b\u0438\u0437       ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.result), QCoreApplication.translate("Lab_data", u"     \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442     ", None))
    # retranslateUi

