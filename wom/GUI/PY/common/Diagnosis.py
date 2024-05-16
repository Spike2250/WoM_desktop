# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Diagnosis.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc

class Ui_Diagnosis(object):
    def setupUi(self, Diagnosis):
        if not Diagnosis.objectName():
            Diagnosis.setObjectName(u"Diagnosis")
        Diagnosis.resize(1013, 712)
        Diagnosis.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout = QVBoxLayout(Diagnosis)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(Diagnosis)
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

        self.label_adm_or_dis = QLabel(self.pt_info_block)
        self.label_adm_or_dis.setObjectName(u"label_adm_or_dis")
        self.label_adm_or_dis.setMaximumSize(QSize(110, 16777215))
        self.label_adm_or_dis.setFont(font)
        self.label_adm_or_dis.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: white;\n"
"font-size: 11pt;\n"
"font-weight: bold;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.label_adm_or_dis.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_adm_or_dis)

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
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/clinical_notes_FILL0_wght400_GRAD0_opsz48.svg"))
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
        self.frame_3 = QFrame(self.main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(750, 0))
        self.frame_3.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);\n"
"")
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.plainTextEditPtDiagnosisMain = QPlainTextEdit(self.frame_3)
        self.plainTextEditPtDiagnosisMain.setObjectName(u"plainTextEditPtDiagnosisMain")
        self.plainTextEditPtDiagnosisMain.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEditPtDiagnosisMain.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.plainTextEditPtDiagnosisMain, 2, 0, 1, 3)

        self.plainTextEditPtDiagnosisConcomitant = QPlainTextEdit(self.frame_3)
        self.plainTextEditPtDiagnosisConcomitant.setObjectName(u"plainTextEditPtDiagnosisConcomitant")
        self.plainTextEditPtDiagnosisConcomitant.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEditPtDiagnosisConcomitant.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.plainTextEditPtDiagnosisConcomitant, 4, 0, 1, 3)

        self.label_diagnosis = QLabel(self.frame_3)
        self.label_diagnosis.setObjectName(u"label_diagnosis")
        self.label_diagnosis.setMaximumSize(QSize(16777215, 25))
        self.label_diagnosis.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_diagnosis.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_diagnosis, 0, 0, 1, 3)

        self.pushButton_helper_diag_main = QPushButton(self.frame_3)
        self.pushButton_helper_diag_main.setObjectName(u"pushButton_helper_diag_main")
        self.pushButton_helper_diag_main.setEnabled(False)
        self.pushButton_helper_diag_main.setMaximumSize(QSize(16777215, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButton_helper_diag_main.setPalette(palette3)
        self.pushButton_helper_diag_main.setFont(font2)
        self.pushButton_helper_diag_main.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_helper_diag_main, 1, 2, 1, 1)

        self.pushButton_helper_diag_concominant = QPushButton(self.frame_3)
        self.pushButton_helper_diag_concominant.setObjectName(u"pushButton_helper_diag_concominant")
        self.pushButton_helper_diag_concominant.setEnabled(False)
        self.pushButton_helper_diag_concominant.setMaximumSize(QSize(16777215, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButton_helper_diag_concominant.setPalette(palette4)
        self.pushButton_helper_diag_concominant.setFont(font2)
        self.pushButton_helper_diag_concominant.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_helper_diag_concominant, 3, 2, 1, 1)

        self.labelPtDiagnosisConcomitant = QLabel(self.frame_3)
        self.labelPtDiagnosisConcomitant.setObjectName(u"labelPtDiagnosisConcomitant")
        palette5 = QPalette()
        brush18 = QBrush(QColor(50, 98, 115, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
        brush19 = QBrush(QColor(50, 98, 115, 128))
        brush19.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelPtDiagnosisConcomitant.setPalette(palette5)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.labelPtDiagnosisConcomitant.setFont(font3)
        self.labelPtDiagnosisConcomitant.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDiagnosisConcomitant.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtDiagnosisConcomitant, 3, 0, 1, 2)

        self.labelPtDiagnosisMain = QLabel(self.frame_3)
        self.labelPtDiagnosisMain.setObjectName(u"labelPtDiagnosisMain")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelPtDiagnosisMain.setPalette(palette6)
        self.labelPtDiagnosisMain.setFont(font3)
        self.labelPtDiagnosisMain.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDiagnosisMain.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtDiagnosisMain, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.labelDiagnosisAdmFS_Hauser = QLabel(self.frame_4)
        self.labelDiagnosisAdmFS_Hauser.setObjectName(u"labelDiagnosisAdmFS_Hauser")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        brush20 = QBrush(QColor(0, 0, 0, 0))
        brush20.setStyle(Qt.SolidPattern)
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
        self.labelDiagnosisAdmFS_Hauser.setPalette(palette7)
        self.labelDiagnosisAdmFS_Hauser.setFont(font)
        self.labelDiagnosisAdmFS_Hauser.setLayoutDirection(Qt.LeftToRight)
        self.labelDiagnosisAdmFS_Hauser.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelDiagnosisAdmFS_Hauser.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelDiagnosisAdmFS_Hauser, 6, 0, 1, 2)

        self.comboBoxDiagnosisFS_VAS_1 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.addItem("")
        self.comboBoxDiagnosisFS_VAS_1.setObjectName(u"comboBoxDiagnosisFS_VAS_1")
        self.comboBoxDiagnosisFS_VAS_1.setEnabled(False)
        palette8 = QPalette()
        brush21 = QBrush(QColor(19, 36, 43, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        brush22 = QBrush(QColor(19, 36, 43, 128))
        brush22.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        brush23 = QBrush(QColor(221, 221, 221, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush23)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush23)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush23)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush18)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        brush24 = QBrush(QColor(221, 221, 221, 128))
        brush24.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.comboBoxDiagnosisFS_VAS_1.setPalette(palette8)
        self.comboBoxDiagnosisFS_VAS_1.setFont(font)
        self.comboBoxDiagnosisFS_VAS_1.setStyleSheet(u"QComboBox {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"background-color: #326273;\n"
"color: #DDDDDD;\n"
"font-weight: normal;\n"
"font-size: 10pt;\n"
"}")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_VAS_1, 8, 2, 1, 1)

        self.labelPtDiagnosisFuncScale_3 = QLabel(self.frame_4)
        self.labelPtDiagnosisFuncScale_3.setObjectName(u"labelPtDiagnosisFuncScale_3")
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
        self.labelPtDiagnosisFuncScale_3.setPalette(palette9)
        self.labelPtDiagnosisFuncScale_3.setFont(font)
        self.labelPtDiagnosisFuncScale_3.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDiagnosisFuncScale_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtDiagnosisFuncScale_3, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 5, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.comboBoxDiagnosisFS_RRS_2 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_RRS_2.addItem("")
        self.comboBoxDiagnosisFS_RRS_2.addItem("")
        self.comboBoxDiagnosisFS_RRS_2.addItem("")
        self.comboBoxDiagnosisFS_RRS_2.addItem("")
        self.comboBoxDiagnosisFS_RRS_2.addItem("")
        self.comboBoxDiagnosisFS_RRS_2.addItem("")
        self.comboBoxDiagnosisFS_RRS_2.addItem("")
        self.comboBoxDiagnosisFS_RRS_2.setObjectName(u"comboBoxDiagnosisFS_RRS_2")
        self.comboBoxDiagnosisFS_RRS_2.setEnabled(True)
        self.comboBoxDiagnosisFS_RRS_2.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_RRS_2.setMaximumSize(QSize(70, 16777215))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush23)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush23)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush23)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush18)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.comboBoxDiagnosisFS_RRS_2.setPalette(palette10)
        self.comboBoxDiagnosisFS_RRS_2.setFont(font)
        self.comboBoxDiagnosisFS_RRS_2.setStyleSheet(u"QComboBox {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"background-color: #326273;\n"
"color: #DDDDDD;\n"
"font-weight: normal;\n"
"font-size: 10pt;\n"
"}background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_RRS_2, 3, 3, 1, 1)

        self.comboBoxDiagnosisFS_VAS_2 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.addItem("")
        self.comboBoxDiagnosisFS_VAS_2.setObjectName(u"comboBoxDiagnosisFS_VAS_2")
        self.comboBoxDiagnosisFS_VAS_2.setEnabled(False)
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush23)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush23)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush23)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush18)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.comboBoxDiagnosisFS_VAS_2.setPalette(palette11)
        self.comboBoxDiagnosisFS_VAS_2.setFont(font)
        self.comboBoxDiagnosisFS_VAS_2.setStyleSheet(u"QComboBox {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"background-color: #326273;\n"
"color: #DDDDDD;\n"
"font-weight: normal;\n"
"font-size: 10pt;\n"
"}background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_VAS_2, 8, 3, 1, 1)

        self.comboBoxDiagnosisFS_mRs_1 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_mRs_1.addItem("")
        self.comboBoxDiagnosisFS_mRs_1.addItem("")
        self.comboBoxDiagnosisFS_mRs_1.addItem("")
        self.comboBoxDiagnosisFS_mRs_1.addItem("")
        self.comboBoxDiagnosisFS_mRs_1.addItem("")
        self.comboBoxDiagnosisFS_mRs_1.addItem("")
        self.comboBoxDiagnosisFS_mRs_1.setObjectName(u"comboBoxDiagnosisFS_mRs_1")
        self.comboBoxDiagnosisFS_mRs_1.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_mRs_1.setMaximumSize(QSize(70, 16777215))
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
        self.comboBoxDiagnosisFS_mRs_1.setPalette(palette12)
        self.comboBoxDiagnosisFS_mRs_1.setFont(font)
        self.comboBoxDiagnosisFS_mRs_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_mRs_1, 4, 2, 1, 1)

        self.comboBoxDiagnosisFS_RRS_1 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_RRS_1.addItem("")
        self.comboBoxDiagnosisFS_RRS_1.addItem("")
        self.comboBoxDiagnosisFS_RRS_1.addItem("")
        self.comboBoxDiagnosisFS_RRS_1.addItem("")
        self.comboBoxDiagnosisFS_RRS_1.addItem("")
        self.comboBoxDiagnosisFS_RRS_1.addItem("")
        self.comboBoxDiagnosisFS_RRS_1.addItem("")
        self.comboBoxDiagnosisFS_RRS_1.setObjectName(u"comboBoxDiagnosisFS_RRS_1")
        self.comboBoxDiagnosisFS_RRS_1.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_RRS_1.setMaximumSize(QSize(70, 16777215))
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
        self.comboBoxDiagnosisFS_RRS_1.setPalette(palette13)
        self.comboBoxDiagnosisFS_RRS_1.setFont(font)
        self.comboBoxDiagnosisFS_RRS_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_RRS_1, 3, 2, 1, 1)

        self.labelPtDiagnosisPainVAS = QLabel(self.frame_4)
        self.labelPtDiagnosisPainVAS.setObjectName(u"labelPtDiagnosisPainVAS")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelPtDiagnosisPainVAS.setPalette(palette14)
        self.labelPtDiagnosisPainVAS.setFont(font)
        self.labelPtDiagnosisPainVAS.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDiagnosisPainVAS.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtDiagnosisPainVAS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelPtDiagnosisPainVAS, 8, 0, 1, 2)

        self.labelDiagnosisAdmFS_RRS_2 = QLabel(self.frame_4)
        self.labelDiagnosisAdmFS_RRS_2.setObjectName(u"labelDiagnosisAdmFS_RRS_2")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelDiagnosisAdmFS_RRS_2.setPalette(palette15)
        self.labelDiagnosisAdmFS_RRS_2.setFont(font)
        self.labelDiagnosisAdmFS_RRS_2.setLayoutDirection(Qt.LeftToRight)
        self.labelDiagnosisAdmFS_RRS_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelDiagnosisAdmFS_RRS_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelDiagnosisAdmFS_RRS_2, 2, 1, 1, 1)

        self.comboBoxDiagnosisFS_Hauser_2 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.addItem("")
        self.comboBoxDiagnosisFS_Hauser_2.setObjectName(u"comboBoxDiagnosisFS_Hauser_2")
        self.comboBoxDiagnosisFS_Hauser_2.setEnabled(True)
        self.comboBoxDiagnosisFS_Hauser_2.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_Hauser_2.setMaximumSize(QSize(70, 16777215))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush23)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush23)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush23)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush18)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.comboBoxDiagnosisFS_Hauser_2.setPalette(palette16)
        self.comboBoxDiagnosisFS_Hauser_2.setFont(font)
        self.comboBoxDiagnosisFS_Hauser_2.setStyleSheet(u"QComboBox {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"background-color: #326273;\n"
"color: #DDDDDD;\n"
"font-weight: normal;\n"
"font-size: 10pt;\n"
"}background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_Hauser_2, 6, 3, 1, 1)

        self.labelDiagnosisAdmFS_mRs = QLabel(self.frame_4)
        self.labelDiagnosisAdmFS_mRs.setObjectName(u"labelDiagnosisAdmFS_mRs")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelDiagnosisAdmFS_mRs.setPalette(palette17)
        self.labelDiagnosisAdmFS_mRs.setFont(font)
        self.labelDiagnosisAdmFS_mRs.setLayoutDirection(Qt.LeftToRight)
        self.labelDiagnosisAdmFS_mRs.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelDiagnosisAdmFS_mRs.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelDiagnosisAdmFS_mRs, 4, 0, 1, 2)

        self.labelPtDiagnosisFuncScale_2 = QLabel(self.frame_4)
        self.labelPtDiagnosisFuncScale_2.setObjectName(u"labelPtDiagnosisFuncScale_2")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelPtDiagnosisFuncScale_2.setPalette(palette18)
        self.labelPtDiagnosisFuncScale_2.setFont(font)
        self.labelPtDiagnosisFuncScale_2.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDiagnosisFuncScale_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtDiagnosisFuncScale_2, 1, 2, 1, 1)

        self.comboBoxDiagnosisFS_IMR_2 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.addItem("")
        self.comboBoxDiagnosisFS_IMR_2.setObjectName(u"comboBoxDiagnosisFS_IMR_2")
        self.comboBoxDiagnosisFS_IMR_2.setEnabled(True)
        self.comboBoxDiagnosisFS_IMR_2.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_IMR_2.setMaximumSize(QSize(70, 16777215))
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
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush23)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush23)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush23)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush18)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.comboBoxDiagnosisFS_IMR_2.setPalette(palette19)
        self.comboBoxDiagnosisFS_IMR_2.setFont(font)
        self.comboBoxDiagnosisFS_IMR_2.setStyleSheet(u"QComboBox {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"background-color: #326273;\n"
"color: #DDDDDD;\n"
"font-weight: normal;\n"
"font-size: 10pt;\n"
"}background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_IMR_2, 5, 3, 1, 1)

        self.comboBoxDiagnosisFS_Hauser_1 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.addItem("")
        self.comboBoxDiagnosisFS_Hauser_1.setObjectName(u"comboBoxDiagnosisFS_Hauser_1")
        self.comboBoxDiagnosisFS_Hauser_1.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_Hauser_1.setMaximumSize(QSize(70, 16777215))
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
        self.comboBoxDiagnosisFS_Hauser_1.setPalette(palette20)
        self.comboBoxDiagnosisFS_Hauser_1.setFont(font)
        self.comboBoxDiagnosisFS_Hauser_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_Hauser_1, 6, 2, 1, 1)

        self.checkBoxPainCheck = QCheckBox(self.frame_4)
        self.checkBoxPainCheck.setObjectName(u"checkBoxPainCheck")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        self.checkBoxPainCheck.setFont(font4)
        self.checkBoxPainCheck.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_2.addWidget(self.checkBoxPainCheck, 7, 2, 1, 3)

        self.labelDiagnosisAdmFS_IMR = QLabel(self.frame_4)
        self.labelDiagnosisAdmFS_IMR.setObjectName(u"labelDiagnosisAdmFS_IMR")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette21.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette21.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette21.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette21.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette21.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette21.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelDiagnosisAdmFS_IMR.setPalette(palette21)
        self.labelDiagnosisAdmFS_IMR.setFont(font)
        self.labelDiagnosisAdmFS_IMR.setLayoutDirection(Qt.LeftToRight)
        self.labelDiagnosisAdmFS_IMR.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelDiagnosisAdmFS_IMR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelDiagnosisAdmFS_IMR, 5, 0, 1, 2)

        self.comboBoxDiagnosisFS_mRs_2 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_mRs_2.addItem("")
        self.comboBoxDiagnosisFS_mRs_2.addItem("")
        self.comboBoxDiagnosisFS_mRs_2.addItem("")
        self.comboBoxDiagnosisFS_mRs_2.addItem("")
        self.comboBoxDiagnosisFS_mRs_2.addItem("")
        self.comboBoxDiagnosisFS_mRs_2.addItem("")
        self.comboBoxDiagnosisFS_mRs_2.setObjectName(u"comboBoxDiagnosisFS_mRs_2")
        self.comboBoxDiagnosisFS_mRs_2.setEnabled(True)
        self.comboBoxDiagnosisFS_mRs_2.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_mRs_2.setMaximumSize(QSize(70, 16777215))
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
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush23)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush23)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush23)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush18)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush24)
#endif
        self.comboBoxDiagnosisFS_mRs_2.setPalette(palette22)
        self.comboBoxDiagnosisFS_mRs_2.setFont(font)
        self.comboBoxDiagnosisFS_mRs_2.setStyleSheet(u"QComboBox {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"background-color: #326273;\n"
"color: #DDDDDD;\n"
"font-weight: normal;\n"
"font-size: 10pt;\n"
"}background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_mRs_2, 4, 3, 1, 1)

        self.labelDiagnosisAdmFS_RRS = QLabel(self.frame_4)
        self.labelDiagnosisAdmFS_RRS.setObjectName(u"labelDiagnosisAdmFS_RRS")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette23.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette23.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette23.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette23.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette23.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette23.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelDiagnosisAdmFS_RRS.setPalette(palette23)
        self.labelDiagnosisAdmFS_RRS.setFont(font)
        self.labelDiagnosisAdmFS_RRS.setLayoutDirection(Qt.LeftToRight)
        self.labelDiagnosisAdmFS_RRS.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelDiagnosisAdmFS_RRS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelDiagnosisAdmFS_RRS, 3, 0, 1, 2)

        self.labelPtDiagnosisPainCheck = QLabel(self.frame_4)
        self.labelPtDiagnosisPainCheck.setObjectName(u"labelPtDiagnosisPainCheck")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush18)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush18)
        palette24.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush18)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette24.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush18)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush18)
        palette24.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush18)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette24.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette24.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette24.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.labelPtDiagnosisPainCheck.setPalette(palette24)
        self.labelPtDiagnosisPainCheck.setFont(font)
        self.labelPtDiagnosisPainCheck.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDiagnosisPainCheck.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtDiagnosisPainCheck.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelPtDiagnosisPainCheck, 7, 0, 1, 2)

        self.comboBoxDiagnosisFS_IMR_1 = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.addItem("")
        self.comboBoxDiagnosisFS_IMR_1.setObjectName(u"comboBoxDiagnosisFS_IMR_1")
        self.comboBoxDiagnosisFS_IMR_1.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_IMR_1.setMaximumSize(QSize(70, 16777215))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBoxDiagnosisFS_IMR_1.setPalette(palette25)
        self.comboBoxDiagnosisFS_IMR_1.setFont(font)
        self.comboBoxDiagnosisFS_IMR_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_IMR_1, 5, 2, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 5)

        self.comboBoxDiagnosisFS_NIHSS = QComboBox(self.frame_4)
        self.comboBoxDiagnosisFS_NIHSS.setObjectName(u"comboBoxDiagnosisFS_NIHSS")
        self.comboBoxDiagnosisFS_NIHSS.setMinimumSize(QSize(70, 0))
        self.comboBoxDiagnosisFS_NIHSS.setMaximumSize(QSize(70, 16777215))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush21)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush12)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush13)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush14)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush21)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush21)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush22)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush21)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush12)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush13)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush14)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush21)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush21)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush12)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush13)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush14)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.comboBoxDiagnosisFS_NIHSS.setPalette(palette26)
        self.comboBoxDiagnosisFS_NIHSS.setFont(font)
        self.comboBoxDiagnosisFS_NIHSS.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxDiagnosisFS_NIHSS.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxDiagnosisFS_NIHSS, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.main)

        QWidget.setTabOrder(self.pushButton_helper_diag_main, self.plainTextEditPtDiagnosisMain)
        QWidget.setTabOrder(self.plainTextEditPtDiagnosisMain, self.plainTextEditPtDiagnosisConcomitant)
        QWidget.setTabOrder(self.plainTextEditPtDiagnosisConcomitant, self.pushButton_helper_diag_concominant)
        QWidget.setTabOrder(self.pushButton_helper_diag_concominant, self.comboBoxDiagnosisFS_NIHSS)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_NIHSS, self.comboBoxDiagnosisFS_RRS_1)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_RRS_1, self.comboBoxDiagnosisFS_RRS_2)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_RRS_2, self.comboBoxDiagnosisFS_mRs_1)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_mRs_1, self.comboBoxDiagnosisFS_mRs_2)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_mRs_2, self.comboBoxDiagnosisFS_IMR_1)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_IMR_1, self.comboBoxDiagnosisFS_IMR_2)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_IMR_2, self.comboBoxDiagnosisFS_Hauser_1)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_Hauser_1, self.comboBoxDiagnosisFS_Hauser_2)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_Hauser_2, self.checkBoxPainCheck)
        QWidget.setTabOrder(self.checkBoxPainCheck, self.comboBoxDiagnosisFS_VAS_1)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_VAS_1, self.comboBoxDiagnosisFS_VAS_2)
        QWidget.setTabOrder(self.comboBoxDiagnosisFS_VAS_2, self.pushButtonNotSaveExit)
        QWidget.setTabOrder(self.pushButtonNotSaveExit, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.pushButtonHelp)

        self.retranslateUi(Diagnosis)

        QMetaObject.connectSlotsByName(Diagnosis)
    # setupUi

    def retranslateUi(self, Diagnosis):
        Diagnosis.setWindowTitle(QCoreApplication.translate("Diagnosis", u"Form", None))
        self.label_Pt_info.setText(QCoreApplication.translate("Diagnosis", u"PatientInfo\n"
"fff", None))
        self.label_adm_or_dis.setText(QCoreApplication.translate("Diagnosis", u"adm/dis", None))
        self.labelTimeline.setText("")
        self.groupBox_wom.setTitle(QCoreApplication.translate("Diagnosis", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("Diagnosis", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("Diagnosis", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("Diagnosis", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.label_diagnosis.setText(QCoreApplication.translate("Diagnosis", u"\u041a\u043b\u0438\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.pushButton_helper_diag_main.setText(QCoreApplication.translate("Diagnosis", u"\u043f\u043e\u043c\u043e\u0449\u043d\u0438\u043a \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.pushButton_helper_diag_concominant.setText(QCoreApplication.translate("Diagnosis", u"\u043f\u043e\u043c\u043e\u0449\u043d\u0438\u043a \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.labelPtDiagnosisConcomitant.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>\u0421\u043e\u043f\u0443\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439</p></body></html>", None))
        self.labelPtDiagnosisMain.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439</p></body></html>", None))
        self.labelDiagnosisAdmFS_Hauser.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>\u0425\u043e\u0434\u044c\u0431\u0430 \u043f\u043e \u0425\u0430\u0443\u0437\u0435\u0440\u0443:</p></body></html>", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(0, QCoreApplication.translate("Diagnosis", u"0", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(1, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(2, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(3, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(4, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(5, QCoreApplication.translate("Diagnosis", u"5", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(6, QCoreApplication.translate("Diagnosis", u"6", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(7, QCoreApplication.translate("Diagnosis", u"7", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(8, QCoreApplication.translate("Diagnosis", u"8", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(9, QCoreApplication.translate("Diagnosis", u"9", None))
        self.comboBoxDiagnosisFS_VAS_1.setItemText(10, QCoreApplication.translate("Diagnosis", u"10", None))

        self.labelPtDiagnosisFuncScale_3.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p align=\"center\">\u0432\u044b\u043f.</p></body></html>", None))
        self.comboBoxDiagnosisFS_RRS_2.setItemText(0, QCoreApplication.translate("Diagnosis", u"0", None))
        self.comboBoxDiagnosisFS_RRS_2.setItemText(1, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_RRS_2.setItemText(2, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_RRS_2.setItemText(3, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_RRS_2.setItemText(4, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_RRS_2.setItemText(5, QCoreApplication.translate("Diagnosis", u"5", None))
        self.comboBoxDiagnosisFS_RRS_2.setItemText(6, QCoreApplication.translate("Diagnosis", u"6", None))

        self.comboBoxDiagnosisFS_VAS_2.setItemText(0, QCoreApplication.translate("Diagnosis", u"0", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(1, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(2, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(3, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(4, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(5, QCoreApplication.translate("Diagnosis", u"5", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(6, QCoreApplication.translate("Diagnosis", u"6", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(7, QCoreApplication.translate("Diagnosis", u"7", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(8, QCoreApplication.translate("Diagnosis", u"8", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(9, QCoreApplication.translate("Diagnosis", u"9", None))
        self.comboBoxDiagnosisFS_VAS_2.setItemText(10, QCoreApplication.translate("Diagnosis", u"10", None))

        self.comboBoxDiagnosisFS_mRs_1.setItemText(0, QCoreApplication.translate("Diagnosis", u"0", None))
        self.comboBoxDiagnosisFS_mRs_1.setItemText(1, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_mRs_1.setItemText(2, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_mRs_1.setItemText(3, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_mRs_1.setItemText(4, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_mRs_1.setItemText(5, QCoreApplication.translate("Diagnosis", u"5", None))

        self.comboBoxDiagnosisFS_RRS_1.setItemText(0, QCoreApplication.translate("Diagnosis", u"0", None))
        self.comboBoxDiagnosisFS_RRS_1.setItemText(1, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_RRS_1.setItemText(2, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_RRS_1.setItemText(3, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_RRS_1.setItemText(4, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_RRS_1.setItemText(5, QCoreApplication.translate("Diagnosis", u"5", None))
        self.comboBoxDiagnosisFS_RRS_1.setItemText(6, QCoreApplication.translate("Diagnosis", u"6", None))

        self.labelPtDiagnosisPainVAS.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>\u0412\u0410\u0428 \u0431\u043e\u043b\u0438:</p></body></html>", None))
        self.labelDiagnosisAdmFS_RRS_2.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>NIHSS:</p></body></html>", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(0, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(1, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(2, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(3, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(4, QCoreApplication.translate("Diagnosis", u"5", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(5, QCoreApplication.translate("Diagnosis", u"6", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(6, QCoreApplication.translate("Diagnosis", u"7", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(7, QCoreApplication.translate("Diagnosis", u"8", None))
        self.comboBoxDiagnosisFS_Hauser_2.setItemText(8, QCoreApplication.translate("Diagnosis", u"9", None))

        self.labelDiagnosisAdmFS_mRs.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>\u041c\u043e\u0434\u0438\u0444\u0438\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0448\u043a\u0430\u043b\u0430 \u0420\u044d\u043d\u043a\u0438\u043d (mRs):</p></body></html>", None))
        self.labelPtDiagnosisFuncScale_2.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p align=\"center\">\u043f\u043e\u0441\u0442.</p></body></html>", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(0, QCoreApplication.translate("Diagnosis", u"0", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(1, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(2, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(3, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(4, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(5, QCoreApplication.translate("Diagnosis", u"5", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(6, QCoreApplication.translate("Diagnosis", u"6", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(7, QCoreApplication.translate("Diagnosis", u"7", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(8, QCoreApplication.translate("Diagnosis", u"8", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(9, QCoreApplication.translate("Diagnosis", u"9", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(10, QCoreApplication.translate("Diagnosis", u"10", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(11, QCoreApplication.translate("Diagnosis", u"11", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(12, QCoreApplication.translate("Diagnosis", u"12", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(13, QCoreApplication.translate("Diagnosis", u"13", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(14, QCoreApplication.translate("Diagnosis", u"14", None))
        self.comboBoxDiagnosisFS_IMR_2.setItemText(15, QCoreApplication.translate("Diagnosis", u"15", None))

        self.comboBoxDiagnosisFS_Hauser_1.setItemText(0, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_Hauser_1.setItemText(1, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_Hauser_1.setItemText(2, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_Hauser_1.setItemText(3, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_Hauser_1.setItemText(4, QCoreApplication.translate("Diagnosis", u"5", None))
        self.comboBoxDiagnosisFS_Hauser_1.setItemText(5, QCoreApplication.translate("Diagnosis", u"6", None))
        self.comboBoxDiagnosisFS_Hauser_1.setItemText(6, QCoreApplication.translate("Diagnosis", u"7", None))
        self.comboBoxDiagnosisFS_Hauser_1.setItemText(7, QCoreApplication.translate("Diagnosis", u"8", None))
        self.comboBoxDiagnosisFS_Hauser_1.setItemText(8, QCoreApplication.translate("Diagnosis", u"9", None))

        self.checkBoxPainCheck.setText(QCoreApplication.translate("Diagnosis", u"\u0435\u0441\u0442\u044c \u0431\u043e\u043b\u0435\u0432\u043e\u0439 \u0441\u0438\u043d\u0434\u0440\u043e\u043c", None))
        self.labelDiagnosisAdmFS_IMR.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>\u0418\u043d\u0434\u0435\u043a\u0441 \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0420\u0438\u0432\u0435\u0440\u043c\u0438\u0434 (IMR):</p></body></html>", None))
        self.comboBoxDiagnosisFS_mRs_2.setItemText(0, QCoreApplication.translate("Diagnosis", u"0", None))
        self.comboBoxDiagnosisFS_mRs_2.setItemText(1, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_mRs_2.setItemText(2, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_mRs_2.setItemText(3, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_mRs_2.setItemText(4, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_mRs_2.setItemText(5, QCoreApplication.translate("Diagnosis", u"5", None))

        self.labelDiagnosisAdmFS_RRS.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0438\u0437\u0430\u0446\u0438\u0438 (\u0428\u0420\u041c):</p></body></html>", None))
        self.labelPtDiagnosisPainCheck.setText(QCoreApplication.translate("Diagnosis", u"<html><head/><body><p>\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0431\u043e\u043b\u0435\u0432\u043e\u0433\u043e \u0441\u0438\u043d\u0434\u0440\u043e\u043c\u0430:</p></body></html>", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(0, QCoreApplication.translate("Diagnosis", u"0", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(1, QCoreApplication.translate("Diagnosis", u"1", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(2, QCoreApplication.translate("Diagnosis", u"2", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(3, QCoreApplication.translate("Diagnosis", u"3", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(4, QCoreApplication.translate("Diagnosis", u"4", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(5, QCoreApplication.translate("Diagnosis", u"5", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(6, QCoreApplication.translate("Diagnosis", u"6", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(7, QCoreApplication.translate("Diagnosis", u"7", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(8, QCoreApplication.translate("Diagnosis", u"8", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(9, QCoreApplication.translate("Diagnosis", u"9", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(10, QCoreApplication.translate("Diagnosis", u"10", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(11, QCoreApplication.translate("Diagnosis", u"11", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(12, QCoreApplication.translate("Diagnosis", u"12", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(13, QCoreApplication.translate("Diagnosis", u"13", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(14, QCoreApplication.translate("Diagnosis", u"14", None))
        self.comboBoxDiagnosisFS_IMR_1.setItemText(15, QCoreApplication.translate("Diagnosis", u"15", None))

        self.label.setText(QCoreApplication.translate("Diagnosis", u"\u0424\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0448\u043a\u0430\u043b\u044b", None))
    # retranslateUi

