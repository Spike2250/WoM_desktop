# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'omr_Dynamic.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc

class Ui_Dynamic(object):
    def setupUi(self, Dynamic):
        if not Dynamic.objectName():
            Dynamic.setObjectName(u"Dynamic")
        Dynamic.resize(769, 629)
        Dynamic.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout = QVBoxLayout(Dynamic)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(Dynamic)
        self.main.setObjectName(u"main")
        self.gridLayout_4 = QGridLayout(self.main)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
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
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/accessible_forward_white_36dp.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTimeline)


        self.gridLayout_4.addWidget(self.pt_info_block, 0, 0, 1, 1)

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

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

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


        self.gridLayout_4.addWidget(self.groupBox_wom, 0, 1, 2, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_dyn = QFrame(self.main)
        self.frame_dyn.setObjectName(u"frame_dyn")
        self.frame_dyn.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_5 = QGridLayout(self.frame_dyn)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.comboBox_logo_proso = QComboBox(self.frame_dyn)
        self.comboBox_logo_proso.addItem("")
        self.comboBox_logo_proso.addItem("")
        self.comboBox_logo_proso.setObjectName(u"comboBox_logo_proso")
        self.comboBox_logo_proso.setFont(font)
        self.comboBox_logo_proso.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_proso.setEditable(True)

        self.gridLayout_5.addWidget(self.comboBox_logo_proso, 8, 6, 1, 1)

        self.label_logo = QLabel(self.frame_dyn)
        self.label_logo.setObjectName(u"label_logo")
        palette3 = QPalette()
        brush18 = QBrush(QColor(50, 98, 115, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
        brush19 = QBrush(QColor(50, 98, 115, 128))
        brush19.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label_logo.setPalette(palette3)
        self.label_logo.setFont(font)
        self.label_logo.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_logo, 5, 5, 1, 2)

        self.comboBox_moca = QComboBox(self.frame_dyn)
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.setObjectName(u"comboBox_moca")
        self.comboBox_moca.setFont(font)
        self.comboBox_moca.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_5.addWidget(self.comboBox_moca, 6, 2, 1, 2)

        self.label_psy = QLabel(self.frame_dyn)
        self.label_psy.setObjectName(u"label_psy")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label_psy.setPalette(palette4)
        self.label_psy.setFont(font)
        self.label_psy.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_psy, 5, 1, 1, 3)

        self.label_logo_dysphagia_2 = QLabel(self.frame_dyn)
        self.label_logo_dysphagia_2.setObjectName(u"label_logo_dysphagia_2")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        brush20 = QBrush(QColor(0, 0, 0, 0))
        brush20.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label_logo_dysphagia_2.setPalette(palette5)
        self.label_logo_dysphagia_2.setFont(font)
        self.label_logo_dysphagia_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_logo_dysphagia_2, 9, 5, 1, 1)

        self.label_logo_disart_2 = QLabel(self.frame_dyn)
        self.label_logo_disart_2.setObjectName(u"label_logo_disart_2")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label_logo_disart_2.setPalette(palette6)
        self.label_logo_disart_2.setFont(font)
        self.label_logo_disart_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_logo_disart_2, 7, 5, 1, 1)

        self.comboBox_logo_disart = QComboBox(self.frame_dyn)
        self.comboBox_logo_disart.addItem("")
        self.comboBox_logo_disart.addItem("")
        self.comboBox_logo_disart.setObjectName(u"comboBox_logo_disart")
        self.comboBox_logo_disart.setFont(font)
        self.comboBox_logo_disart.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_disart.setEditable(True)

        self.gridLayout_5.addWidget(self.comboBox_logo_disart, 7, 6, 1, 1)

        self.comboBox_hads_d = QComboBox(self.frame_dyn)
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.setObjectName(u"comboBox_hads_d")
        self.comboBox_hads_d.setMinimumSize(QSize(50, 0))
        self.comboBox_hads_d.setMaximumSize(QSize(50, 16777215))
        self.comboBox_hads_d.setFont(font)
        self.comboBox_hads_d.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_5.addWidget(self.comboBox_hads_d, 7, 3, 1, 1)

        self.comboBox_logo_wasserman = QComboBox(self.frame_dyn)
        self.comboBox_logo_wasserman.addItem("")
        self.comboBox_logo_wasserman.addItem("")
        self.comboBox_logo_wasserman.setObjectName(u"comboBox_logo_wasserman")
        self.comboBox_logo_wasserman.setMinimumSize(QSize(50, 0))
        self.comboBox_logo_wasserman.setMaximumSize(QSize(50, 16777215))
        self.comboBox_logo_wasserman.setFont(font)
        self.comboBox_logo_wasserman.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_wasserman.setEditable(True)

        self.gridLayout_5.addWidget(self.comboBox_logo_wasserman, 6, 6, 1, 1)

        self.label_psy_hads_2 = QLabel(self.frame_dyn)
        self.label_psy_hads_2.setObjectName(u"label_psy_hads_2")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label_psy_hads_2.setPalette(palette7)
        self.label_psy_hads_2.setFont(font)
        self.label_psy_hads_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_psy_hads_2, 7, 1, 1, 1)

        self.label_logo_proso_2 = QLabel(self.frame_dyn)
        self.label_logo_proso_2.setObjectName(u"label_logo_proso_2")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label_logo_proso_2.setPalette(palette8)
        self.label_logo_proso_2.setFont(font)
        self.label_logo_proso_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_logo_proso_2, 8, 5, 1, 1)

        self.comboBox_logo_dysphagia = QComboBox(self.frame_dyn)
        self.comboBox_logo_dysphagia.addItem("")
        self.comboBox_logo_dysphagia.addItem("")
        self.comboBox_logo_dysphagia.setObjectName(u"comboBox_logo_dysphagia")
        self.comboBox_logo_dysphagia.setFont(font)
        self.comboBox_logo_dysphagia.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_dysphagia.setEditable(True)

        self.gridLayout_5.addWidget(self.comboBox_logo_dysphagia, 9, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 7, 0, 1, 1)

        self.label_psy_moca_2 = QLabel(self.frame_dyn)
        self.label_psy_moca_2.setObjectName(u"label_psy_moca_2")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label_psy_moca_2.setPalette(palette9)
        self.label_psy_moca_2.setFont(font)
        self.label_psy_moca_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_psy_moca_2, 6, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 7, 4, 1, 1)

        self.comboBox_hads_t = QComboBox(self.frame_dyn)
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.setObjectName(u"comboBox_hads_t")
        self.comboBox_hads_t.setMinimumSize(QSize(50, 0))
        self.comboBox_hads_t.setMaximumSize(QSize(50, 16777215))
        self.comboBox_hads_t.setFont(font)
        self.comboBox_hads_t.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_5.addWidget(self.comboBox_hads_t, 7, 2, 1, 1)

        self.label_logo_wasserman_2 = QLabel(self.frame_dyn)
        self.label_logo_wasserman_2.setObjectName(u"label_logo_wasserman_2")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.label_logo_wasserman_2.setPalette(palette10)
        self.label_logo_wasserman_2.setFont(font)
        self.label_logo_wasserman_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_logo_wasserman_2, 6, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 7, 7, 1, 1)

        self.label_scale = QLabel(self.frame_dyn)
        self.label_scale.setObjectName(u"label_scale")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush21 = QBrush(QColor(112, 38, 50, 150))
        brush21.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush21)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush21)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush21)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush21)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush21)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush21)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush21)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush21)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_scale.setPalette(palette11)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_scale.setFont(font3)
        self.label_scale.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")

        self.gridLayout_5.addWidget(self.label_scale, 4, 0, 1, 8)

        self.label_dynamic = QLabel(self.frame_dyn)
        self.label_dynamic.setObjectName(u"label_dynamic")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush21)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush21)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush21)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush21)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush21)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush21)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush21)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush21)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_dynamic.setPalette(palette12)
        self.label_dynamic.setFont(font3)
        self.label_dynamic.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")

        self.gridLayout_5.addWidget(self.label_dynamic, 1, 0, 1, 8)

        self.plainTextEdit_dynamic = QPlainTextEdit(self.frame_dyn)
        self.plainTextEdit_dynamic.setObjectName(u"plainTextEdit_dynamic")
        self.plainTextEdit_dynamic.setMinimumSize(QSize(0, 250))
        self.plainTextEdit_dynamic.setFont(font)
        self.plainTextEdit_dynamic.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_5.addWidget(self.plainTextEdit_dynamic, 2, 0, 1, 8)


        self.gridLayout_3.addWidget(self.frame_dyn, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.frame_templates = QFrame(self.main)
        self.frame_templates.setObjectName(u"frame_templates")
        self.frame_templates.setMaximumSize(QSize(16777215, 115))
        self.frame_templates.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_13 = QGridLayout(self.frame_templates)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(5)
        self.gridLayout_13.setVerticalSpacing(1)
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.comboBox_templates = QComboBox(self.frame_templates)
        self.comboBox_templates.addItem("")
        self.comboBox_templates.setObjectName(u"comboBox_templates")
        self.comboBox_templates.setMaximumSize(QSize(16777215, 16777215))
        palette13 = QPalette()
        brush22 = QBrush(QColor(19, 36, 43, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush22)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush22)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush22)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        brush23 = QBrush(QColor(19, 36, 43, 128))
        brush23.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush23)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush22)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush22)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush22)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush23)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush22)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush22)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush22)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush23)
#endif
        self.comboBox_templates.setPalette(palette13)
        self.comboBox_templates.setFont(font)
        self.comboBox_templates.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_13.addWidget(self.comboBox_templates, 2, 0, 1, 1)

        self.pushButtonAddNewTemplate = QPushButton(self.frame_templates)
        self.pushButtonAddNewTemplate.setObjectName(u"pushButtonAddNewTemplate")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonAddNewTemplate.setPalette(palette14)
        self.pushButtonAddNewTemplate.setFont(font2)
        self.pushButtonAddNewTemplate.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_13.addWidget(self.pushButtonAddNewTemplate, 4, 1, 1, 1)

        self.label_14 = QLabel(self.frame_templates)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_14, 0, 0, 1, 2)

        self.pushButton_push_temp = QPushButton(self.frame_templates)
        self.pushButton_push_temp.setObjectName(u"pushButton_push_temp")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_push_temp.setPalette(palette15)
        self.pushButton_push_temp.setFont(font2)
        self.pushButton_push_temp.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_13.addWidget(self.pushButton_push_temp, 2, 1, 1, 1)

        self.lineEdit_new_template_name = QLineEdit(self.frame_templates)
        self.lineEdit_new_template_name.setObjectName(u"lineEdit_new_template_name")
        self.lineEdit_new_template_name.setMinimumSize(QSize(350, 0))
        self.lineEdit_new_template_name.setFont(font)
        self.lineEdit_new_template_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_13.addWidget(self.lineEdit_new_template_name, 4, 0, 1, 1)

        self.label_15 = QLabel(self.frame_templates)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.frame_templates)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_16, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_templates, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.main)

        QWidget.setTabOrder(self.pushButtonNotSaveExit, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.pushButtonHelp)

        self.retranslateUi(Dynamic)

        QMetaObject.connectSlotsByName(Dynamic)
    # setupUi

    def retranslateUi(self, Dynamic):
        Dynamic.setWindowTitle(QCoreApplication.translate("Dynamic", u"Form", None))
        self.label_Pt_info.setText(QCoreApplication.translate("Dynamic", u"PatientInfo\n"
"fff", None))
        self.labelTimeline.setText("")
        self.groupBox_wom.setTitle(QCoreApplication.translate("Dynamic", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("Dynamic", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("Dynamic", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("Dynamic", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.comboBox_logo_proso.setItemText(0, "")
        self.comboBox_logo_proso.setItemText(1, QCoreApplication.translate("Dynamic", u"UN", None))

        self.label_logo.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p align=\"center\">\u041b\u043e\u0433\u043e\u043f\u0435\u0434</p></body></html>", None))
        self.comboBox_moca.setItemText(0, "")
        self.comboBox_moca.setItemText(1, QCoreApplication.translate("Dynamic", u"UN", None))
        self.comboBox_moca.setItemText(2, QCoreApplication.translate("Dynamic", u"30", None))
        self.comboBox_moca.setItemText(3, QCoreApplication.translate("Dynamic", u"29", None))
        self.comboBox_moca.setItemText(4, QCoreApplication.translate("Dynamic", u"28", None))
        self.comboBox_moca.setItemText(5, QCoreApplication.translate("Dynamic", u"27", None))
        self.comboBox_moca.setItemText(6, QCoreApplication.translate("Dynamic", u"26", None))
        self.comboBox_moca.setItemText(7, QCoreApplication.translate("Dynamic", u"25", None))
        self.comboBox_moca.setItemText(8, QCoreApplication.translate("Dynamic", u"24", None))
        self.comboBox_moca.setItemText(9, QCoreApplication.translate("Dynamic", u"23", None))
        self.comboBox_moca.setItemText(10, QCoreApplication.translate("Dynamic", u"22", None))
        self.comboBox_moca.setItemText(11, QCoreApplication.translate("Dynamic", u"21", None))
        self.comboBox_moca.setItemText(12, QCoreApplication.translate("Dynamic", u"20", None))
        self.comboBox_moca.setItemText(13, QCoreApplication.translate("Dynamic", u"19", None))
        self.comboBox_moca.setItemText(14, QCoreApplication.translate("Dynamic", u"18", None))
        self.comboBox_moca.setItemText(15, QCoreApplication.translate("Dynamic", u"17", None))
        self.comboBox_moca.setItemText(16, QCoreApplication.translate("Dynamic", u"16", None))
        self.comboBox_moca.setItemText(17, QCoreApplication.translate("Dynamic", u"15", None))
        self.comboBox_moca.setItemText(18, QCoreApplication.translate("Dynamic", u"14", None))
        self.comboBox_moca.setItemText(19, QCoreApplication.translate("Dynamic", u"13", None))
        self.comboBox_moca.setItemText(20, QCoreApplication.translate("Dynamic", u"12", None))
        self.comboBox_moca.setItemText(21, QCoreApplication.translate("Dynamic", u"11", None))
        self.comboBox_moca.setItemText(22, QCoreApplication.translate("Dynamic", u"10", None))
        self.comboBox_moca.setItemText(23, QCoreApplication.translate("Dynamic", u"9", None))
        self.comboBox_moca.setItemText(24, QCoreApplication.translate("Dynamic", u"8", None))
        self.comboBox_moca.setItemText(25, QCoreApplication.translate("Dynamic", u"7", None))
        self.comboBox_moca.setItemText(26, QCoreApplication.translate("Dynamic", u"6", None))
        self.comboBox_moca.setItemText(27, QCoreApplication.translate("Dynamic", u"5", None))
        self.comboBox_moca.setItemText(28, QCoreApplication.translate("Dynamic", u"4", None))
        self.comboBox_moca.setItemText(29, QCoreApplication.translate("Dynamic", u"3", None))
        self.comboBox_moca.setItemText(30, QCoreApplication.translate("Dynamic", u"2", None))
        self.comboBox_moca.setItemText(31, QCoreApplication.translate("Dynamic", u"1", None))
        self.comboBox_moca.setItemText(32, QCoreApplication.translate("Dynamic", u"0", None))

        self.label_psy.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p align=\"center\">\u041f\u0441\u0438\u0445\u043e\u043b\u043e\u0433</p></body></html>", None))
        self.label_logo_dysphagia_2.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0433\u043b\u043e\u0442\u0430\u043d\u0438\u044f \u041a\u0418\u041c:</p></body></html>", None))
        self.label_logo_disart_2.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0414\u0438\u0437\u0430\u0440\u0442\u0440\u0438\u0438:</p></body></html>", None))
        self.comboBox_logo_disart.setItemText(0, "")
        self.comboBox_logo_disart.setItemText(1, QCoreApplication.translate("Dynamic", u"UN", None))

        self.comboBox_hads_d.setItemText(0, "")
        self.comboBox_hads_d.setItemText(1, QCoreApplication.translate("Dynamic", u"UN", None))
        self.comboBox_hads_d.setItemText(2, QCoreApplication.translate("Dynamic", u"0", None))
        self.comboBox_hads_d.setItemText(3, QCoreApplication.translate("Dynamic", u"1", None))
        self.comboBox_hads_d.setItemText(4, QCoreApplication.translate("Dynamic", u"2", None))
        self.comboBox_hads_d.setItemText(5, QCoreApplication.translate("Dynamic", u"3", None))
        self.comboBox_hads_d.setItemText(6, QCoreApplication.translate("Dynamic", u"4", None))
        self.comboBox_hads_d.setItemText(7, QCoreApplication.translate("Dynamic", u"5", None))
        self.comboBox_hads_d.setItemText(8, QCoreApplication.translate("Dynamic", u"6", None))
        self.comboBox_hads_d.setItemText(9, QCoreApplication.translate("Dynamic", u"7", None))
        self.comboBox_hads_d.setItemText(10, QCoreApplication.translate("Dynamic", u"8", None))
        self.comboBox_hads_d.setItemText(11, QCoreApplication.translate("Dynamic", u"9", None))
        self.comboBox_hads_d.setItemText(12, QCoreApplication.translate("Dynamic", u"10", None))
        self.comboBox_hads_d.setItemText(13, QCoreApplication.translate("Dynamic", u"11", None))
        self.comboBox_hads_d.setItemText(14, QCoreApplication.translate("Dynamic", u"12", None))
        self.comboBox_hads_d.setItemText(15, QCoreApplication.translate("Dynamic", u"13", None))
        self.comboBox_hads_d.setItemText(16, QCoreApplication.translate("Dynamic", u"14", None))
        self.comboBox_hads_d.setItemText(17, QCoreApplication.translate("Dynamic", u"15", None))
        self.comboBox_hads_d.setItemText(18, QCoreApplication.translate("Dynamic", u"16", None))
        self.comboBox_hads_d.setItemText(19, QCoreApplication.translate("Dynamic", u"17", None))
        self.comboBox_hads_d.setItemText(20, QCoreApplication.translate("Dynamic", u"18", None))
        self.comboBox_hads_d.setItemText(21, QCoreApplication.translate("Dynamic", u"19", None))
        self.comboBox_hads_d.setItemText(22, QCoreApplication.translate("Dynamic", u"20", None))
        self.comboBox_hads_d.setItemText(23, QCoreApplication.translate("Dynamic", u"21", None))

        self.comboBox_logo_wasserman.setItemText(0, "")
        self.comboBox_logo_wasserman.setItemText(1, QCoreApplication.translate("Dynamic", u"UN", None))

        self.label_psy_hads_2.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p>HADS:</p></body></html>", None))
        self.label_logo_proso_2.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0425\u0430\u0443\u0441-\u0411\u0440\u0430\u0430\u043a\u043c\u0430\u043d:</p></body></html>", None))
        self.comboBox_logo_dysphagia.setItemText(0, "")
        self.comboBox_logo_dysphagia.setItemText(1, QCoreApplication.translate("Dynamic", u"UN", None))

        self.label_psy_moca_2.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p>MoCA:</p></body></html>", None))
        self.comboBox_hads_t.setItemText(0, "")
        self.comboBox_hads_t.setItemText(1, QCoreApplication.translate("Dynamic", u"UN", None))
        self.comboBox_hads_t.setItemText(2, QCoreApplication.translate("Dynamic", u"0", None))
        self.comboBox_hads_t.setItemText(3, QCoreApplication.translate("Dynamic", u"1", None))
        self.comboBox_hads_t.setItemText(4, QCoreApplication.translate("Dynamic", u"2", None))
        self.comboBox_hads_t.setItemText(5, QCoreApplication.translate("Dynamic", u"3", None))
        self.comboBox_hads_t.setItemText(6, QCoreApplication.translate("Dynamic", u"4", None))
        self.comboBox_hads_t.setItemText(7, QCoreApplication.translate("Dynamic", u"5", None))
        self.comboBox_hads_t.setItemText(8, QCoreApplication.translate("Dynamic", u"6", None))
        self.comboBox_hads_t.setItemText(9, QCoreApplication.translate("Dynamic", u"7", None))
        self.comboBox_hads_t.setItemText(10, QCoreApplication.translate("Dynamic", u"8", None))
        self.comboBox_hads_t.setItemText(11, QCoreApplication.translate("Dynamic", u"9", None))
        self.comboBox_hads_t.setItemText(12, QCoreApplication.translate("Dynamic", u"10", None))
        self.comboBox_hads_t.setItemText(13, QCoreApplication.translate("Dynamic", u"11", None))
        self.comboBox_hads_t.setItemText(14, QCoreApplication.translate("Dynamic", u"12", None))
        self.comboBox_hads_t.setItemText(15, QCoreApplication.translate("Dynamic", u"13", None))
        self.comboBox_hads_t.setItemText(16, QCoreApplication.translate("Dynamic", u"14", None))
        self.comboBox_hads_t.setItemText(17, QCoreApplication.translate("Dynamic", u"15", None))
        self.comboBox_hads_t.setItemText(18, QCoreApplication.translate("Dynamic", u"16", None))
        self.comboBox_hads_t.setItemText(19, QCoreApplication.translate("Dynamic", u"17", None))
        self.comboBox_hads_t.setItemText(20, QCoreApplication.translate("Dynamic", u"18", None))
        self.comboBox_hads_t.setItemText(21, QCoreApplication.translate("Dynamic", u"19", None))
        self.comboBox_hads_t.setItemText(22, QCoreApplication.translate("Dynamic", u"20", None))
        self.comboBox_hads_t.setItemText(23, QCoreApplication.translate("Dynamic", u"21", None))

        self.label_logo_wasserman_2.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0412\u0430\u0441\u0441\u0435\u0440\u043c\u0430\u043d\u0430:</p></body></html>", None))
        self.label_scale.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p align=\"center\">\u0428\u043a\u0430\u043b\u044b \u043f\u0440\u0438 \u0432\u044b\u043f\u0438\u0441\u043a\u0435</p></body></html>", None))
        self.label_dynamic.setText(QCoreApplication.translate("Dynamic", u"<html><head/><body><p align=\"center\">\u0414\u0438\u043d\u0430\u043c\u0438\u043a\u0430:</p></body></html>", None))
        self.comboBox_templates.setItemText(0, "")

        self.pushButtonAddNewTemplate.setText(QCoreApplication.translate("Dynamic", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.label_14.setText(QCoreApplication.translate("Dynamic", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u0434\u0438\u043d\u0430\u043c\u0438\u043a\u0438", None))
        self.pushButton_push_temp.setText(QCoreApplication.translate("Dynamic", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit_new_template_name.setText("")
        self.lineEdit_new_template_name.setPlaceholderText(QCoreApplication.translate("Dynamic", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_15.setText(QCoreApplication.translate("Dynamic", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.label_16.setText(QCoreApplication.translate("Dynamic", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
    # retranslateUi

