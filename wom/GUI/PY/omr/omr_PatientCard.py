# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'omr_PatientCard.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)
import res_main_rc

class Ui_omr_patient_card(object):
    def setupUi(self, omr_patient_card):
        if not omr_patient_card.objectName():
            omr_patient_card.setObjectName(u"omr_patient_card")
        omr_patient_card.resize(1370, 737)
        omr_patient_card.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_3 = QVBoxLayout(omr_patient_card)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(omr_patient_card)
        self.main.setObjectName(u"main")
        self.horizontalLayout_2 = QHBoxLayout(self.main)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left = QFrame(self.main)
        self.left.setObjectName(u"left")
        self.verticalLayout_5 = QVBoxLayout(self.left)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.left)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMaximumSize(QSize(16777215, 200))
        self.frame_logo.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 2px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 130);")
        self.verticalLayout = QVBoxLayout(self.frame_logo)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_uin = QFrame(self.frame_logo)
        self.frame_uin.setObjectName(u"frame_uin")
        self.frame_uin.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_uin)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_status_4 = QLabel(self.frame_uin)
        self.label_status_4.setObjectName(u"label_status_4")
        self.label_status_4.setMaximumSize(QSize(24, 24))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        font.setBold(False)
        self.label_status_4.setFont(font)
        self.label_status_4.setStyleSheet(u"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_status_4.setPixmap(QPixmap(u":/icon/icons/person_outline_white_36dp.svg"))
        self.label_status_4.setScaledContents(True)
        self.label_status_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_status_4)

        self.label_status_3 = QLabel(self.frame_uin)
        self.label_status_3.setObjectName(u"label_status_3")
        self.label_status_3.setMaximumSize(QSize(30, 16777215))
        self.label_status_3.setFont(font)
        self.label_status_3.setStyleSheet(u"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_status_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_status_3)

        self.label_unic_number = QLabel(self.frame_uin)
        self.label_unic_number.setObjectName(u"label_unic_number")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_unic_number.setFont(font1)
        self.label_unic_number.setStyleSheet(u"color: White;")
        self.label_unic_number.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_unic_number)


        self.verticalLayout.addWidget(self.frame_uin)

        self.ptFullNameCard = QLabel(self.frame_logo)
        self.ptFullNameCard.setObjectName(u"ptFullNameCard")
        self.ptFullNameCard.setMinimumSize(QSize(0, 65))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.ptFullNameCard.setFont(font2)
        self.ptFullNameCard.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad, x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0 rgba(238, 238, 238, 255),\n"
"    stop:1 rgba(50, 98, 115, 10));\n"
"color: rgba(50, 98, 115, 255);\n"
"font-size: 10pt;\n"
"font-weight: bold;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"padding-left: 5px;")
        self.ptFullNameCard.setFrameShape(QFrame.NoFrame)
        self.ptFullNameCard.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.ptFullNameCard)

        self.frame_ln_hosp = QFrame(self.frame_logo)
        self.frame_ln_hosp.setObjectName(u"frame_ln_hosp")
        self.frame_ln_hosp.setStyleSheet(u"border: none")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_ln_hosp)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_type_hospitalisation = QLabel(self.frame_ln_hosp)
        self.label_type_hospitalisation.setObjectName(u"label_type_hospitalisation")
        self.label_type_hospitalisation.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_type_hospitalisation.setFont(font3)
        self.label_type_hospitalisation.setStyleSheet(u"color: White;\n"
"font-size: 11pt;\n"
"border: none;")
        self.label_type_hospitalisation.setFrameShape(QFrame.NoFrame)
        self.label_type_hospitalisation.setFrameShadow(QFrame.Plain)
        self.label_type_hospitalisation.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_type_hospitalisation)

        self.label_LN = QLabel(self.frame_ln_hosp)
        self.label_LN.setObjectName(u"label_LN")
        self.label_LN.setMaximumSize(QSize(50, 20))
        self.label_LN.setFont(font3)
        self.label_LN.setStyleSheet(u"color: White;\n"
"font-size: 11pt;\n"
"border: none;")
        self.label_LN.setFrameShape(QFrame.NoFrame)
        self.label_LN.setFrameShadow(QFrame.Plain)
        self.label_LN.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_LN)


        self.verticalLayout.addWidget(self.frame_ln_hosp)

        self.frame_check = QFrame(self.frame_logo)
        self.frame_check.setObjectName(u"frame_check")
        self.frame_check.setStyleSheet(u"border: none")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_check)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_b20 = QLabel(self.frame_check)
        self.label_b20.setObjectName(u"label_b20")
        self.label_b20.setMaximumSize(QSize(16777215, 20))
        self.label_b20.setFont(font3)
        self.label_b20.setStyleSheet(u"color: #13242B;;\n"
"font-size: 11pt;\n"
"border: none;")
        self.label_b20.setFrameShape(QFrame.NoFrame)
        self.label_b20.setFrameShadow(QFrame.Plain)
        self.label_b20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_b20)

        self.label_hvc = QLabel(self.frame_check)
        self.label_hvc.setObjectName(u"label_hvc")
        self.label_hvc.setMaximumSize(QSize(16777215, 20))
        self.label_hvc.setFont(font3)
        self.label_hvc.setStyleSheet(u"color: #13242B;;\n"
"font-size: 11pt;\n"
"border: none;")
        self.label_hvc.setFrameShape(QFrame.NoFrame)
        self.label_hvc.setFrameShadow(QFrame.Plain)
        self.label_hvc.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_hvc)

        self.label_diabet = QLabel(self.frame_check)
        self.label_diabet.setObjectName(u"label_diabet")
        self.label_diabet.setMaximumSize(QSize(16777215, 20))
        self.label_diabet.setFont(font3)
        self.label_diabet.setStyleSheet(u"color: #13242B;;\n"
"font-size: 11pt;\n"
"border: none;")
        self.label_diabet.setFrameShape(QFrame.NoFrame)
        self.label_diabet.setFrameShadow(QFrame.Plain)
        self.label_diabet.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_diabet)


        self.verticalLayout.addWidget(self.frame_check)


        self.verticalLayout_5.addWidget(self.frame_logo)

        self.frame_data_block = QFrame(self.left)
        self.frame_data_block.setObjectName(u"frame_data_block")
        self.frame_data_block.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_2 = QVBoxLayout(self.frame_data_block)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_adm_data = QLabel(self.frame_data_block)
        self.label_adm_data.setObjectName(u"label_adm_data")
        self.label_adm_data.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_adm_data.setFont(font4)
        self.label_adm_data.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_adm_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_adm_data)

        self.pushButtonOpenPtPassportData = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtPassportData.setObjectName(u"pushButtonOpenPtPassportData")
        self.pushButtonOpenPtPassportData.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtPassportData.setMaximumSize(QSize(16777215, 25))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(50, 98, 115, 100))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(60, 145, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(36, 119, 227, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(6, 47, 100, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(8, 62, 133, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(133, 174, 227, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush10 = QBrush(QColor(238, 238, 238, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush11 = QBrush(QColor(12, 94, 200, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtPassportData.setPalette(palette)
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        self.pushButtonOpenPtPassportData.setFont(font5)
        self.pushButtonOpenPtPassportData.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtPassportData.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon = QIcon()
        icon.addFile(u":/icon/icons/account_box_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtPassportData.setIcon(icon)
        self.pushButtonOpenPtPassportData.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtPassportData)

        self.pushButtonOpenPtObjStatusAdm = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtObjStatusAdm.setObjectName(u"pushButtonOpenPtObjStatusAdm")
        self.pushButtonOpenPtObjStatusAdm.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtObjStatusAdm.setMaximumSize(QSize(16777215, 25))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtObjStatusAdm.setPalette(palette1)
        self.pushButtonOpenPtObjStatusAdm.setFont(font5)
        self.pushButtonOpenPtObjStatusAdm.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtObjStatusAdm.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon1.addFile(u":/icon/icons/stethoscope_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtObjStatusAdm.setIcon(icon1)
        self.pushButtonOpenPtObjStatusAdm.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtObjStatusAdm)

        self.pushButtonOpenPtNeuralStatusAdm = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtNeuralStatusAdm.setObjectName(u"pushButtonOpenPtNeuralStatusAdm")
        self.pushButtonOpenPtNeuralStatusAdm.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtNeuralStatusAdm.setMaximumSize(QSize(16777215, 25))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtNeuralStatusAdm.setPalette(palette2)
        self.pushButtonOpenPtNeuralStatusAdm.setFont(font5)
        self.pushButtonOpenPtNeuralStatusAdm.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtNeuralStatusAdm.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon2.addFile(u":/icon/icons/neurology_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtNeuralStatusAdm.setIcon(icon2)
        self.pushButtonOpenPtNeuralStatusAdm.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtNeuralStatusAdm)

        self.pushButtonOpenPtDiagnosisAdm = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtDiagnosisAdm.setObjectName(u"pushButtonOpenPtDiagnosisAdm")
        self.pushButtonOpenPtDiagnosisAdm.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtDiagnosisAdm.setMaximumSize(QSize(16777215, 25))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtDiagnosisAdm.setPalette(palette3)
        self.pushButtonOpenPtDiagnosisAdm.setFont(font5)
        self.pushButtonOpenPtDiagnosisAdm.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtDiagnosisAdm.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/clinical_notes_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtDiagnosisAdm.setIcon(icon3)
        self.pushButtonOpenPtDiagnosisAdm.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtDiagnosisAdm)

        self.pushButtonOpen_icf = QPushButton(self.frame_data_block)
        self.pushButtonOpen_icf.setObjectName(u"pushButtonOpen_icf")
        self.pushButtonOpen_icf.setMinimumSize(QSize(0, 25))
        self.pushButtonOpen_icf.setMaximumSize(QSize(16777215, 25))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpen_icf.setPalette(palette4)
        self.pushButtonOpen_icf.setFont(font5)
        self.pushButtonOpen_icf.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpen_icf.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/personal_injury_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpen_icf.setIcon(icon4)
        self.pushButtonOpen_icf.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpen_icf)

        self.pushButtonOpenPtAppointments = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtAppointments.setObjectName(u"pushButtonOpenPtAppointments")
        self.pushButtonOpenPtAppointments.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtAppointments.setMaximumSize(QSize(16777215, 25))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtAppointments.setPalette(palette5)
        self.pushButtonOpenPtAppointments.setFont(font5)
        self.pushButtonOpenPtAppointments.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtAppointments.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/assignment_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtAppointments.setIcon(icon5)
        self.pushButtonOpenPtAppointments.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtAppointments)

        self.pushButtonOpen_mdrk = QPushButton(self.frame_data_block)
        self.pushButtonOpen_mdrk.setObjectName(u"pushButtonOpen_mdrk")
        self.pushButtonOpen_mdrk.setMinimumSize(QSize(0, 25))
        self.pushButtonOpen_mdrk.setMaximumSize(QSize(16777215, 25))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpen_mdrk.setPalette(palette6)
        self.pushButtonOpen_mdrk.setFont(font5)
        self.pushButtonOpen_mdrk.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpen_mdrk.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/conditions_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpen_mdrk.setIcon(icon6)
        self.pushButtonOpen_mdrk.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpen_mdrk)

        self.label_instr_data = QLabel(self.frame_data_block)
        self.label_instr_data.setObjectName(u"label_instr_data")
        self.label_instr_data.setMaximumSize(QSize(16777215, 30))
        self.label_instr_data.setFont(font4)
        self.label_instr_data.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_instr_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_instr_data)

        self.pushButtonOpenPtLaboratoryData = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtLaboratoryData.setObjectName(u"pushButtonOpenPtLaboratoryData")
        self.pushButtonOpenPtLaboratoryData.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtLaboratoryData.setMaximumSize(QSize(16777215, 25))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtLaboratoryData.setPalette(palette7)
        self.pushButtonOpenPtLaboratoryData.setFont(font5)
        self.pushButtonOpenPtLaboratoryData.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtLaboratoryData.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/lab_research_FILL0_wght400_GRAD0_opsz48_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtLaboratoryData.setIcon(icon7)
        self.pushButtonOpenPtLaboratoryData.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtLaboratoryData)

        self.pushButtonOpenPtInstrumentalData = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtInstrumentalData.setObjectName(u"pushButtonOpenPtInstrumentalData")
        self.pushButtonOpenPtInstrumentalData.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtInstrumentalData.setMaximumSize(QSize(16777215, 25))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtInstrumentalData.setPalette(palette8)
        self.pushButtonOpenPtInstrumentalData.setFont(font5)
        self.pushButtonOpenPtInstrumentalData.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtInstrumentalData.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/radiology_FILL1_wght400_GRAD0_opsz48_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtInstrumentalData.setIcon(icon8)
        self.pushButtonOpenPtInstrumentalData.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtInstrumentalData)

        self.pushButtonOpenPtConsultationData = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtConsultationData.setObjectName(u"pushButtonOpenPtConsultationData")
        self.pushButtonOpenPtConsultationData.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtConsultationData.setMaximumSize(QSize(16777215, 25))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtConsultationData.setPalette(palette9)
        self.pushButtonOpenPtConsultationData.setFont(font5)
        self.pushButtonOpenPtConsultationData.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtConsultationData.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/record_voice_over_FILL1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtConsultationData.setIcon(icon9)
        self.pushButtonOpenPtConsultationData.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtConsultationData)

        self.label_dis_data = QLabel(self.frame_data_block)
        self.label_dis_data.setObjectName(u"label_dis_data")
        self.label_dis_data.setMaximumSize(QSize(16777215, 30))
        self.label_dis_data.setFont(font4)
        self.label_dis_data.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_dis_data.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_dis_data)

        self.pushButtonOpenPtObjStatusDischarge = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtObjStatusDischarge.setObjectName(u"pushButtonOpenPtObjStatusDischarge")
        self.pushButtonOpenPtObjStatusDischarge.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtObjStatusDischarge.setMaximumSize(QSize(16777215, 25))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtObjStatusDischarge.setPalette(palette10)
        self.pushButtonOpenPtObjStatusDischarge.setFont(font5)
        self.pushButtonOpenPtObjStatusDischarge.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtObjStatusDischarge.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        self.pushButtonOpenPtObjStatusDischarge.setIcon(icon1)
        self.pushButtonOpenPtObjStatusDischarge.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtObjStatusDischarge)

        self.pushButtonOpenPtNeuralStatusDischarge = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtNeuralStatusDischarge.setObjectName(u"pushButtonOpenPtNeuralStatusDischarge")
        self.pushButtonOpenPtNeuralStatusDischarge.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtNeuralStatusDischarge.setMaximumSize(QSize(16777215, 25))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtNeuralStatusDischarge.setPalette(palette11)
        self.pushButtonOpenPtNeuralStatusDischarge.setFont(font5)
        self.pushButtonOpenPtNeuralStatusDischarge.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtNeuralStatusDischarge.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        self.pushButtonOpenPtNeuralStatusDischarge.setIcon(icon2)
        self.pushButtonOpenPtNeuralStatusDischarge.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtNeuralStatusDischarge)

        self.pushButtonOpenPtDiagnosisDischarge = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtDiagnosisDischarge.setObjectName(u"pushButtonOpenPtDiagnosisDischarge")
        self.pushButtonOpenPtDiagnosisDischarge.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtDiagnosisDischarge.setMaximumSize(QSize(16777215, 25))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtDiagnosisDischarge.setPalette(palette12)
        self.pushButtonOpenPtDiagnosisDischarge.setFont(font5)
        self.pushButtonOpenPtDiagnosisDischarge.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtDiagnosisDischarge.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        self.pushButtonOpenPtDiagnosisDischarge.setIcon(icon3)
        self.pushButtonOpenPtDiagnosisDischarge.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtDiagnosisDischarge)

        self.pushButtonOpen_dynamic = QPushButton(self.frame_data_block)
        self.pushButtonOpen_dynamic.setObjectName(u"pushButtonOpen_dynamic")
        self.pushButtonOpen_dynamic.setMinimumSize(QSize(0, 25))
        self.pushButtonOpen_dynamic.setMaximumSize(QSize(16777215, 25))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpen_dynamic.setPalette(palette13)
        self.pushButtonOpen_dynamic.setFont(font5)
        self.pushButtonOpen_dynamic.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpen_dynamic.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/accessible_forward_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpen_dynamic.setIcon(icon10)
        self.pushButtonOpen_dynamic.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpen_dynamic)

        self.pushButtonOpenPtStatisticData = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtStatisticData.setObjectName(u"pushButtonOpenPtStatisticData")
        self.pushButtonOpenPtStatisticData.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtStatisticData.setMaximumSize(QSize(16777215, 25))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtStatisticData.setPalette(palette14)
        self.pushButtonOpenPtStatisticData.setFont(font5)
        self.pushButtonOpenPtStatisticData.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtStatisticData.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/moving_beds_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtStatisticData.setIcon(icon11)
        self.pushButtonOpenPtStatisticData.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtStatisticData)

        self.pushButtonOpenPtDischargeRecommend = QPushButton(self.frame_data_block)
        self.pushButtonOpenPtDischargeRecommend.setObjectName(u"pushButtonOpenPtDischargeRecommend")
        self.pushButtonOpenPtDischargeRecommend.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenPtDischargeRecommend.setMaximumSize(QSize(16777215, 25))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenPtDischargeRecommend.setPalette(palette15)
        self.pushButtonOpenPtDischargeRecommend.setFont(font5)
        self.pushButtonOpenPtDischargeRecommend.setLayoutDirection(Qt.LeftToRight)
        self.pushButtonOpenPtDischargeRecommend.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 100);\n"
"font-size: 14pt;\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/icon/icons/list_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenPtDischargeRecommend.setIcon(icon12)
        self.pushButtonOpenPtDischargeRecommend.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtDischargeRecommend)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_10)


        self.verticalLayout_5.addWidget(self.frame_data_block)


        self.horizontalLayout_2.addWidget(self.left)

        self.center = QFrame(self.main)
        self.center.setObjectName(u"center")
        self.verticalLayout_6 = QVBoxLayout(self.center)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tabPtCard = QTabWidget(self.center)
        self.tabPtCard.setObjectName(u"tabPtCard")
        self.tabPtCard.setStyleSheet(u"\n"
"QTabWidget:pane {\n"
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
"}")
        self.tabPtCard.setIconSize(QSize(32, 32))
        self.Page_events = QWidget()
        self.Page_events.setObjectName(u"Page_events")
        self.gridLayout_7 = QGridLayout(self.Page_events)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.frame_events = QFrame(self.Page_events)
        self.frame_events.setObjectName(u"frame_events")
        self.frame_events.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.frame_events)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.tableWidget_dynamic = QTableWidget(self.frame_events)
        if (self.tableWidget_dynamic.columnCount() < 5):
            self.tableWidget_dynamic.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_dynamic.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_dynamic.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_dynamic.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_dynamic.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_dynamic.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_dynamic.setObjectName(u"tableWidget_dynamic")
        self.tableWidget_dynamic.setEnabled(False)
        self.tableWidget_dynamic.setMinimumSize(QSize(600, 0))
        self.tableWidget_dynamic.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_dynamic.setFont(font1)
        self.tableWidget_dynamic.setStyleSheet(u"QTableWidget {\n"
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

        self.gridLayout.addWidget(self.tableWidget_dynamic, 1, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.pushButtonAddEvent = QPushButton(self.frame_events)
        self.pushButtonAddEvent.setObjectName(u"pushButtonAddEvent")
        self.pushButtonAddEvent.setEnabled(False)
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush12 = QBrush(QColor(50, 98, 115, 190))
        brush12.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        brush13 = QBrush(QColor(50, 98, 115, 150))
        brush13.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        brush14 = QBrush(QColor(50, 98, 115, 40))
        brush14.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush15 = QBrush(QColor(50, 98, 115, 75))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButtonAddEvent.setPalette(palette16)
        self.pushButtonAddEvent.setFont(font1)
        self.pushButtonAddEvent.setStyleSheet(u"QPushButton {\n"
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
        icon13 = QIcon()
        icon13.addFile(u":/icon/icons/add_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddEvent.setIcon(icon13)
        self.pushButtonAddEvent.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButtonAddEvent, 2, 2, 1, 1)

        self.label_events = QLabel(self.frame_events)
        self.label_events.setObjectName(u"label_events")
        self.label_events.setMaximumSize(QSize(16777215, 30))
        self.label_events.setFont(font4)
        self.label_events.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_events.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_events, 0, 0, 1, 4)


        self.gridLayout_7.addWidget(self.frame_events, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_10, 0, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_11, 1, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_6, 3, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)

        self.label_sorry = QLabel(self.Page_events)
        self.label_sorry.setObjectName(u"label_sorry")
        self.label_sorry.setMaximumSize(QSize(16777215, 16777215))
        self.label_sorry.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;\n"
"font-size: 14pt;\n"
"")
        self.label_sorry.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_sorry, 2, 1, 1, 1)

        icon14 = QIcon()
        icon14.addFile(u":/icon/icons/library_add_FILL1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPtCard.addTab(self.Page_events, icon14, "")
        self.Page_diaries = QWidget()
        self.Page_diaries.setObjectName(u"Page_diaries")
        self.gridLayout_8 = QGridLayout(self.Page_diaries)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(2, 2, 2, 2)
        self.label_diaries_2 = QLabel(self.Page_diaries)
        self.label_diaries_2.setObjectName(u"label_diaries_2")
        self.label_diaries_2.setMinimumSize(QSize(0, 0))
        self.label_diaries_2.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setItalic(False)
        self.label_diaries_2.setFont(font6)
        self.label_diaries_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 120);\n"
"border: none;\n"
"")
        self.label_diaries_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_diaries_2, 0, 2, 1, 2)

        self.frame_diaries_main = QFrame(self.Page_diaries)
        self.frame_diaries_main.setObjectName(u"frame_diaries_main")
        self.frame_diaries_main.setMaximumSize(QSize(315, 16777215))
        self.frame_diaries_main.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_3 = QGridLayout(self.frame_diaries_main)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame_diaries = QFrame(self.frame_diaries_main)
        self.frame_diaries.setObjectName(u"frame_diaries")
        self.frame_diaries.setMaximumSize(QSize(300, 80))
        self.frame_diaries.setFont(font3)
        self.frame_diaries.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: transparent;")
        self.verticalLayout_4 = QVBoxLayout(self.frame_diaries)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButton_everyday = QRadioButton(self.frame_diaries)
        self.radioButton_everyday.setObjectName(u"radioButton_everyday")
        self.radioButton_everyday.setFont(font3)
        self.radioButton_everyday.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.verticalLayout_4.addWidget(self.radioButton_everyday)

        self.radioButton_3_times_in_week = QRadioButton(self.frame_diaries)
        self.radioButton_3_times_in_week.setObjectName(u"radioButton_3_times_in_week")
        self.radioButton_3_times_in_week.setFont(font3)
        self.radioButton_3_times_in_week.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.radioButton_3_times_in_week)

        self.radioButton_twice_in_day = QRadioButton(self.frame_diaries)
        self.radioButton_twice_in_day.setObjectName(u"radioButton_twice_in_day")
        self.radioButton_twice_in_day.setFont(font3)
        self.radioButton_twice_in_day.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.verticalLayout_4.addWidget(self.radioButton_twice_in_day)


        self.gridLayout_3.addWidget(self.frame_diaries, 1, 1, 1, 1)

        self.pushButton_create_diaries = QPushButton(self.frame_diaries_main)
        self.pushButton_create_diaries.setObjectName(u"pushButton_create_diaries")
        self.pushButton_create_diaries.setEnabled(False)
        self.pushButton_create_diaries.setMinimumSize(QSize(0, 0))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButton_create_diaries.setPalette(palette17)
        self.pushButton_create_diaries.setFont(font1)
        self.pushButton_create_diaries.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_create_diaries.setStyleSheet(u"QPushButton {\n"
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
        icon15 = QIcon()
        icon15.addFile(u":/icon/icons/edit_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_create_diaries.setIcon(icon15)
        self.pushButton_create_diaries.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.pushButton_create_diaries, 2, 1, 1, 1)

        self.tableWidget_diaries = QTableWidget(self.frame_diaries_main)
        if (self.tableWidget_diaries.columnCount() < 1):
            self.tableWidget_diaries.setColumnCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_diaries.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        self.tableWidget_diaries.setObjectName(u"tableWidget_diaries")
        self.tableWidget_diaries.setMinimumSize(QSize(300, 0))
        self.tableWidget_diaries.setMaximumSize(QSize(300, 16777215))
        self.tableWidget_diaries.setFont(font1)
        self.tableWidget_diaries.setStyleSheet(u"QTableWidget {\n"
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

        self.gridLayout_3.addWidget(self.tableWidget_diaries, 3, 1, 3, 1)

        self.label_diaries = QLabel(self.frame_diaries_main)
        self.label_diaries.setObjectName(u"label_diaries")
        self.label_diaries.setMinimumSize(QSize(0, 0))
        self.label_diaries.setMaximumSize(QSize(16777215, 50))
        self.label_diaries.setFont(font4)
        self.label_diaries.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_diaries.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_diaries, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_diaries_main, 0, 0, 3, 1)

        self.pushButton_save_diary = QPushButton(self.Page_diaries)
        self.pushButton_save_diary.setObjectName(u"pushButton_save_diary")
        self.pushButton_save_diary.setEnabled(False)
        self.pushButton_save_diary.setMinimumSize(QSize(0, 0))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButton_save_diary.setPalette(palette18)
        self.pushButton_save_diary.setFont(font1)
        self.pushButton_save_diary.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_save_diary.setStyleSheet(u"QPushButton {\n"
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
        icon16 = QIcon()
        icon16.addFile(u":/icon/icons/save_as_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save_diary.setIcon(icon16)
        self.pushButton_save_diary.setIconSize(QSize(32, 32))

        self.gridLayout_8.addWidget(self.pushButton_save_diary, 2, 3, 1, 2)

        self.pushButton_close_diary = QPushButton(self.Page_diaries)
        self.pushButton_close_diary.setObjectName(u"pushButton_close_diary")
        self.pushButton_close_diary.setEnabled(False)
        self.pushButton_close_diary.setMinimumSize(QSize(0, 0))
        self.pushButton_close_diary.setMaximumSize(QSize(90, 30))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush16 = QBrush(QColor(112, 38, 50, 190))
        brush16.setStyle(Qt.SolidPattern)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette19.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette19.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButton_close_diary.setPalette(palette19)
        self.pushButton_close_diary.setFont(font1)
        self.pushButton_close_diary.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_close_diary.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(112, 38, 50, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(112, 38, 50, 255);\n"
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
        icon17 = QIcon()
        icon17.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close_diary.setIcon(icon17)
        self.pushButton_close_diary.setIconSize(QSize(26, 26))

        self.gridLayout_8.addWidget(self.pushButton_close_diary, 0, 4, 1, 1)

        self.label_diary_index = QLabel(self.Page_diaries)
        self.label_diary_index.setObjectName(u"label_diary_index")
        self.label_diary_index.setMinimumSize(QSize(30, 30))
        self.label_diary_index.setMaximumSize(QSize(30, 30))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(9)
        font7.setBold(True)
        font7.setItalic(False)
        self.label_diary_index.setFont(font7)
        self.label_diary_index.setStyleSheet(u"color: White;\n"
"font-size: 9pt;\n"
"background-color: rgba(50, 98, 115, 120);\n"
"border: none;\n"
"")
        self.label_diary_index.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_diary_index, 0, 1, 1, 1)

        self.plainTextEdit_diary = QPlainTextEdit(self.Page_diaries)
        self.plainTextEdit_diary.setObjectName(u"plainTextEdit_diary")
        self.plainTextEdit_diary.setEnabled(False)
        self.plainTextEdit_diary.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 7pt;\n"
"")

        self.gridLayout_8.addWidget(self.plainTextEdit_diary, 1, 1, 1, 4)

        self.horizontalSpacer = QSpacerItem(155, 29, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 2, 1, 1, 2)

        icon18 = QIcon()
        icon18.addFile(u":/icon/icons/auto_stories_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPtCard.addTab(self.Page_diaries, icon18, "")
        self.Page_creating_docs = QWidget()
        self.Page_creating_docs.setObjectName(u"Page_creating_docs")
        self.gridLayout_6 = QGridLayout(self.Page_creating_docs)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.frame_creating_docs = QFrame(self.Page_creating_docs)
        self.frame_creating_docs.setObjectName(u"frame_creating_docs")
        self.frame_creating_docs.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_4 = QGridLayout(self.frame_creating_docs)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(3)
        self.gridLayout_4.setVerticalSpacing(1)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.checkBox_doc_scale = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_scale.setObjectName(u"checkBox_doc_scale")
        palette20 = QPalette()
        brush17 = QBrush(QColor(50, 98, 115, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(238, 238, 238, 255))
        gradient.setColorAt(1, QColor(190, 190, 190, 255))
        brush18 = QBrush(gradient)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush18)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush)
        brush19 = QBrush(QColor(236, 236, 236, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        brush20 = QBrush(QColor(108, 108, 108, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush20)
        brush21 = QBrush(QColor(145, 145, 145, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient1 = QLinearGradient(0, 0, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(238, 238, 238, 255))
        gradient1.setColorAt(1, QColor(190, 190, 190, 255))
        brush22 = QBrush(gradient1)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush22)
        gradient2 = QLinearGradient(0, 0, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(238, 238, 238, 255))
        gradient2.setColorAt(1, QColor(190, 190, 190, 255))
        brush23 = QBrush(gradient2)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush23)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
        brush24 = QBrush(QColor(50, 98, 115, 128))
        brush24.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient3 = QLinearGradient(0, 0, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(238, 238, 238, 255))
        gradient3.setColorAt(1, QColor(190, 190, 190, 255))
        brush25 = QBrush(gradient3)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush25)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient4 = QLinearGradient(0, 0, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(238, 238, 238, 255))
        gradient4.setColorAt(1, QColor(190, 190, 190, 255))
        brush26 = QBrush(gradient4)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush26)
        gradient5 = QLinearGradient(0, 0, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(238, 238, 238, 255))
        gradient5.setColorAt(1, QColor(190, 190, 190, 255))
        brush27 = QBrush(gradient5)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush27)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        brush28 = QBrush(QColor(155, 155, 155, 255))
        brush28.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient6 = QLinearGradient(0, 0, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(238, 238, 238, 255))
        gradient6.setColorAt(1, QColor(190, 190, 190, 255))
        brush29 = QBrush(gradient6)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush29)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient7 = QLinearGradient(0, 0, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(238, 238, 238, 255))
        gradient7.setColorAt(1, QColor(190, 190, 190, 255))
        brush30 = QBrush(gradient7)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush30)
        gradient8 = QLinearGradient(0, 0, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(238, 238, 238, 255))
        gradient8.setColorAt(1, QColor(190, 190, 190, 255))
        brush31 = QBrush(gradient8)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush31)
        brush32 = QBrush(QColor(217, 217, 217, 255))
        brush32.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
        brush33 = QBrush(QColor(238, 238, 238, 128))
        brush33.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_scale.setPalette(palette20)
        self.checkBox_doc_scale.setFont(font3)
        self.checkBox_doc_scale.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_scale, 9, 1, 1, 1)

        self.checkBox_doc_additional_recommendations = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_additional_recommendations.setObjectName(u"checkBox_doc_additional_recommendations")
        self.checkBox_doc_additional_recommendations.setEnabled(False)
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient9 = QLinearGradient(0, 0, 1, 0)
        gradient9.setSpread(QGradient.PadSpread)
        gradient9.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient9.setColorAt(0, QColor(238, 238, 238, 255))
        gradient9.setColorAt(1, QColor(190, 190, 190, 255))
        brush34 = QBrush(gradient9)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush34)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient10 = QLinearGradient(0, 0, 1, 0)
        gradient10.setSpread(QGradient.PadSpread)
        gradient10.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient10.setColorAt(0, QColor(238, 238, 238, 255))
        gradient10.setColorAt(1, QColor(190, 190, 190, 255))
        brush35 = QBrush(gradient10)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush35)
        gradient11 = QLinearGradient(0, 0, 1, 0)
        gradient11.setSpread(QGradient.PadSpread)
        gradient11.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient11.setColorAt(0, QColor(238, 238, 238, 255))
        gradient11.setColorAt(1, QColor(190, 190, 190, 255))
        brush36 = QBrush(gradient11)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush36)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient12 = QLinearGradient(0, 0, 1, 0)
        gradient12.setSpread(QGradient.PadSpread)
        gradient12.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient12.setColorAt(0, QColor(238, 238, 238, 255))
        gradient12.setColorAt(1, QColor(190, 190, 190, 255))
        brush37 = QBrush(gradient12)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush37)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient13 = QLinearGradient(0, 0, 1, 0)
        gradient13.setSpread(QGradient.PadSpread)
        gradient13.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient13.setColorAt(0, QColor(238, 238, 238, 255))
        gradient13.setColorAt(1, QColor(190, 190, 190, 255))
        brush38 = QBrush(gradient13)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush38)
        gradient14 = QLinearGradient(0, 0, 1, 0)
        gradient14.setSpread(QGradient.PadSpread)
        gradient14.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient14.setColorAt(0, QColor(238, 238, 238, 255))
        gradient14.setColorAt(1, QColor(190, 190, 190, 255))
        brush39 = QBrush(gradient14)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush39)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient15 = QLinearGradient(0, 0, 1, 0)
        gradient15.setSpread(QGradient.PadSpread)
        gradient15.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient15.setColorAt(0, QColor(238, 238, 238, 255))
        gradient15.setColorAt(1, QColor(190, 190, 190, 255))
        brush40 = QBrush(gradient15)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush40)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient16 = QLinearGradient(0, 0, 1, 0)
        gradient16.setSpread(QGradient.PadSpread)
        gradient16.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient16.setColorAt(0, QColor(238, 238, 238, 255))
        gradient16.setColorAt(1, QColor(190, 190, 190, 255))
        brush41 = QBrush(gradient16)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush41)
        gradient17 = QLinearGradient(0, 0, 1, 0)
        gradient17.setSpread(QGradient.PadSpread)
        gradient17.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient17.setColorAt(0, QColor(238, 238, 238, 255))
        gradient17.setColorAt(1, QColor(190, 190, 190, 255))
        brush42 = QBrush(gradient17)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush42)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_additional_recommendations.setPalette(palette21)
        self.checkBox_doc_additional_recommendations.setFont(font3)
        self.checkBox_doc_additional_recommendations.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_additional_recommendations, 18, 3, 1, 1)

        self.checkBox_doc_initial_inspection = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_initial_inspection.setObjectName(u"checkBox_doc_initial_inspection")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient18 = QLinearGradient(0, 0, 1, 0)
        gradient18.setSpread(QGradient.PadSpread)
        gradient18.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient18.setColorAt(0, QColor(238, 238, 238, 255))
        gradient18.setColorAt(1, QColor(190, 190, 190, 255))
        brush43 = QBrush(gradient18)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush43)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient19 = QLinearGradient(0, 0, 1, 0)
        gradient19.setSpread(QGradient.PadSpread)
        gradient19.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient19.setColorAt(0, QColor(238, 238, 238, 255))
        gradient19.setColorAt(1, QColor(190, 190, 190, 255))
        brush44 = QBrush(gradient19)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush44)
        gradient20 = QLinearGradient(0, 0, 1, 0)
        gradient20.setSpread(QGradient.PadSpread)
        gradient20.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient20.setColorAt(0, QColor(238, 238, 238, 255))
        gradient20.setColorAt(1, QColor(190, 190, 190, 255))
        brush45 = QBrush(gradient20)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush45)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient21 = QLinearGradient(0, 0, 1, 0)
        gradient21.setSpread(QGradient.PadSpread)
        gradient21.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient21.setColorAt(0, QColor(238, 238, 238, 255))
        gradient21.setColorAt(1, QColor(190, 190, 190, 255))
        brush46 = QBrush(gradient21)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush46)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient22 = QLinearGradient(0, 0, 1, 0)
        gradient22.setSpread(QGradient.PadSpread)
        gradient22.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient22.setColorAt(0, QColor(238, 238, 238, 255))
        gradient22.setColorAt(1, QColor(190, 190, 190, 255))
        brush47 = QBrush(gradient22)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush47)
        gradient23 = QLinearGradient(0, 0, 1, 0)
        gradient23.setSpread(QGradient.PadSpread)
        gradient23.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient23.setColorAt(0, QColor(238, 238, 238, 255))
        gradient23.setColorAt(1, QColor(190, 190, 190, 255))
        brush48 = QBrush(gradient23)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush48)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient24 = QLinearGradient(0, 0, 1, 0)
        gradient24.setSpread(QGradient.PadSpread)
        gradient24.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient24.setColorAt(0, QColor(238, 238, 238, 255))
        gradient24.setColorAt(1, QColor(190, 190, 190, 255))
        brush49 = QBrush(gradient24)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush49)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient25 = QLinearGradient(0, 0, 1, 0)
        gradient25.setSpread(QGradient.PadSpread)
        gradient25.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient25.setColorAt(0, QColor(238, 238, 238, 255))
        gradient25.setColorAt(1, QColor(190, 190, 190, 255))
        brush50 = QBrush(gradient25)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush50)
        gradient26 = QLinearGradient(0, 0, 1, 0)
        gradient26.setSpread(QGradient.PadSpread)
        gradient26.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient26.setColorAt(0, QColor(238, 238, 238, 255))
        gradient26.setColorAt(1, QColor(190, 190, 190, 255))
        brush51 = QBrush(gradient26)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush51)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_initial_inspection.setPalette(palette22)
        self.checkBox_doc_initial_inspection.setFont(font3)
        self.checkBox_doc_initial_inspection.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_initial_inspection, 2, 1, 1, 2)

        self.checkBox_doc_med_commission_1 = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_med_commission_1.setObjectName(u"checkBox_doc_med_commission_1")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient27 = QLinearGradient(0, 0, 1, 0)
        gradient27.setSpread(QGradient.PadSpread)
        gradient27.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient27.setColorAt(0, QColor(238, 238, 238, 255))
        gradient27.setColorAt(1, QColor(190, 190, 190, 255))
        brush52 = QBrush(gradient27)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush52)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient28 = QLinearGradient(0, 0, 1, 0)
        gradient28.setSpread(QGradient.PadSpread)
        gradient28.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient28.setColorAt(0, QColor(238, 238, 238, 255))
        gradient28.setColorAt(1, QColor(190, 190, 190, 255))
        brush53 = QBrush(gradient28)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush53)
        gradient29 = QLinearGradient(0, 0, 1, 0)
        gradient29.setSpread(QGradient.PadSpread)
        gradient29.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient29.setColorAt(0, QColor(238, 238, 238, 255))
        gradient29.setColorAt(1, QColor(190, 190, 190, 255))
        brush54 = QBrush(gradient29)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush54)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient30 = QLinearGradient(0, 0, 1, 0)
        gradient30.setSpread(QGradient.PadSpread)
        gradient30.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient30.setColorAt(0, QColor(238, 238, 238, 255))
        gradient30.setColorAt(1, QColor(190, 190, 190, 255))
        brush55 = QBrush(gradient30)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush55)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient31 = QLinearGradient(0, 0, 1, 0)
        gradient31.setSpread(QGradient.PadSpread)
        gradient31.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient31.setColorAt(0, QColor(238, 238, 238, 255))
        gradient31.setColorAt(1, QColor(190, 190, 190, 255))
        brush56 = QBrush(gradient31)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush56)
        gradient32 = QLinearGradient(0, 0, 1, 0)
        gradient32.setSpread(QGradient.PadSpread)
        gradient32.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient32.setColorAt(0, QColor(238, 238, 238, 255))
        gradient32.setColorAt(1, QColor(190, 190, 190, 255))
        brush57 = QBrush(gradient32)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush57)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient33 = QLinearGradient(0, 0, 1, 0)
        gradient33.setSpread(QGradient.PadSpread)
        gradient33.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient33.setColorAt(0, QColor(238, 238, 238, 255))
        gradient33.setColorAt(1, QColor(190, 190, 190, 255))
        brush58 = QBrush(gradient33)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush58)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient34 = QLinearGradient(0, 0, 1, 0)
        gradient34.setSpread(QGradient.PadSpread)
        gradient34.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient34.setColorAt(0, QColor(238, 238, 238, 255))
        gradient34.setColorAt(1, QColor(190, 190, 190, 255))
        brush59 = QBrush(gradient34)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush59)
        gradient35 = QLinearGradient(0, 0, 1, 0)
        gradient35.setSpread(QGradient.PadSpread)
        gradient35.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient35.setColorAt(0, QColor(238, 238, 238, 255))
        gradient35.setColorAt(1, QColor(190, 190, 190, 255))
        brush60 = QBrush(gradient35)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush60)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_med_commission_1.setPalette(palette23)
        self.checkBox_doc_med_commission_1.setFont(font3)
        self.checkBox_doc_med_commission_1.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_med_commission_1, 2, 3, 1, 1)

        self.checkBox_doc_statistic_talon = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_statistic_talon.setObjectName(u"checkBox_doc_statistic_talon")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient36 = QLinearGradient(0, 0, 1, 0)
        gradient36.setSpread(QGradient.PadSpread)
        gradient36.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient36.setColorAt(0, QColor(238, 238, 238, 255))
        gradient36.setColorAt(1, QColor(190, 190, 190, 255))
        brush61 = QBrush(gradient36)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush61)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient37 = QLinearGradient(0, 0, 1, 0)
        gradient37.setSpread(QGradient.PadSpread)
        gradient37.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient37.setColorAt(0, QColor(238, 238, 238, 255))
        gradient37.setColorAt(1, QColor(190, 190, 190, 255))
        brush62 = QBrush(gradient37)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush62)
        gradient38 = QLinearGradient(0, 0, 1, 0)
        gradient38.setSpread(QGradient.PadSpread)
        gradient38.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient38.setColorAt(0, QColor(238, 238, 238, 255))
        gradient38.setColorAt(1, QColor(190, 190, 190, 255))
        brush63 = QBrush(gradient38)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush63)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient39 = QLinearGradient(0, 0, 1, 0)
        gradient39.setSpread(QGradient.PadSpread)
        gradient39.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient39.setColorAt(0, QColor(238, 238, 238, 255))
        gradient39.setColorAt(1, QColor(190, 190, 190, 255))
        brush64 = QBrush(gradient39)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush64)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient40 = QLinearGradient(0, 0, 1, 0)
        gradient40.setSpread(QGradient.PadSpread)
        gradient40.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient40.setColorAt(0, QColor(238, 238, 238, 255))
        gradient40.setColorAt(1, QColor(190, 190, 190, 255))
        brush65 = QBrush(gradient40)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush65)
        gradient41 = QLinearGradient(0, 0, 1, 0)
        gradient41.setSpread(QGradient.PadSpread)
        gradient41.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient41.setColorAt(0, QColor(238, 238, 238, 255))
        gradient41.setColorAt(1, QColor(190, 190, 190, 255))
        brush66 = QBrush(gradient41)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush66)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient42 = QLinearGradient(0, 0, 1, 0)
        gradient42.setSpread(QGradient.PadSpread)
        gradient42.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient42.setColorAt(0, QColor(238, 238, 238, 255))
        gradient42.setColorAt(1, QColor(190, 190, 190, 255))
        brush67 = QBrush(gradient42)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush67)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient43 = QLinearGradient(0, 0, 1, 0)
        gradient43.setSpread(QGradient.PadSpread)
        gradient43.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient43.setColorAt(0, QColor(238, 238, 238, 255))
        gradient43.setColorAt(1, QColor(190, 190, 190, 255))
        brush68 = QBrush(gradient43)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush68)
        gradient44 = QLinearGradient(0, 0, 1, 0)
        gradient44.setSpread(QGradient.PadSpread)
        gradient44.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient44.setColorAt(0, QColor(238, 238, 238, 255))
        gradient44.setColorAt(1, QColor(190, 190, 190, 255))
        brush69 = QBrush(gradient44)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush69)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_statistic_talon.setPalette(palette24)
        self.checkBox_doc_statistic_talon.setFont(font3)
        self.checkBox_doc_statistic_talon.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_statistic_talon, 5, 1, 1, 1)

        self.checkBox_doc_med_commission_2 = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_med_commission_2.setObjectName(u"checkBox_doc_med_commission_2")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient45 = QLinearGradient(0, 0, 1, 0)
        gradient45.setSpread(QGradient.PadSpread)
        gradient45.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient45.setColorAt(0, QColor(238, 238, 238, 255))
        gradient45.setColorAt(1, QColor(190, 190, 190, 255))
        brush70 = QBrush(gradient45)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush70)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient46 = QLinearGradient(0, 0, 1, 0)
        gradient46.setSpread(QGradient.PadSpread)
        gradient46.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient46.setColorAt(0, QColor(238, 238, 238, 255))
        gradient46.setColorAt(1, QColor(190, 190, 190, 255))
        brush71 = QBrush(gradient46)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush71)
        gradient47 = QLinearGradient(0, 0, 1, 0)
        gradient47.setSpread(QGradient.PadSpread)
        gradient47.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient47.setColorAt(0, QColor(238, 238, 238, 255))
        gradient47.setColorAt(1, QColor(190, 190, 190, 255))
        brush72 = QBrush(gradient47)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush72)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient48 = QLinearGradient(0, 0, 1, 0)
        gradient48.setSpread(QGradient.PadSpread)
        gradient48.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient48.setColorAt(0, QColor(238, 238, 238, 255))
        gradient48.setColorAt(1, QColor(190, 190, 190, 255))
        brush73 = QBrush(gradient48)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush73)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient49 = QLinearGradient(0, 0, 1, 0)
        gradient49.setSpread(QGradient.PadSpread)
        gradient49.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient49.setColorAt(0, QColor(238, 238, 238, 255))
        gradient49.setColorAt(1, QColor(190, 190, 190, 255))
        brush74 = QBrush(gradient49)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush74)
        gradient50 = QLinearGradient(0, 0, 1, 0)
        gradient50.setSpread(QGradient.PadSpread)
        gradient50.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient50.setColorAt(0, QColor(238, 238, 238, 255))
        gradient50.setColorAt(1, QColor(190, 190, 190, 255))
        brush75 = QBrush(gradient50)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush75)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient51 = QLinearGradient(0, 0, 1, 0)
        gradient51.setSpread(QGradient.PadSpread)
        gradient51.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient51.setColorAt(0, QColor(238, 238, 238, 255))
        gradient51.setColorAt(1, QColor(190, 190, 190, 255))
        brush76 = QBrush(gradient51)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush76)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient52 = QLinearGradient(0, 0, 1, 0)
        gradient52.setSpread(QGradient.PadSpread)
        gradient52.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient52.setColorAt(0, QColor(238, 238, 238, 255))
        gradient52.setColorAt(1, QColor(190, 190, 190, 255))
        brush77 = QBrush(gradient52)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush77)
        gradient53 = QLinearGradient(0, 0, 1, 0)
        gradient53.setSpread(QGradient.PadSpread)
        gradient53.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient53.setColorAt(0, QColor(238, 238, 238, 255))
        gradient53.setColorAt(1, QColor(190, 190, 190, 255))
        brush78 = QBrush(gradient53)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush78)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_med_commission_2.setPalette(palette25)
        self.checkBox_doc_med_commission_2.setFont(font3)
        self.checkBox_doc_med_commission_2.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_med_commission_2, 3, 3, 1, 1)

        self.checkBox_doc_appointments = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_appointments.setObjectName(u"checkBox_doc_appointments")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient54 = QLinearGradient(0, 0, 1, 0)
        gradient54.setSpread(QGradient.PadSpread)
        gradient54.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient54.setColorAt(0, QColor(238, 238, 238, 255))
        gradient54.setColorAt(1, QColor(190, 190, 190, 255))
        brush79 = QBrush(gradient54)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush79)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient55 = QLinearGradient(0, 0, 1, 0)
        gradient55.setSpread(QGradient.PadSpread)
        gradient55.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient55.setColorAt(0, QColor(238, 238, 238, 255))
        gradient55.setColorAt(1, QColor(190, 190, 190, 255))
        brush80 = QBrush(gradient55)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush80)
        gradient56 = QLinearGradient(0, 0, 1, 0)
        gradient56.setSpread(QGradient.PadSpread)
        gradient56.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient56.setColorAt(0, QColor(238, 238, 238, 255))
        gradient56.setColorAt(1, QColor(190, 190, 190, 255))
        brush81 = QBrush(gradient56)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush81)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient57 = QLinearGradient(0, 0, 1, 0)
        gradient57.setSpread(QGradient.PadSpread)
        gradient57.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient57.setColorAt(0, QColor(238, 238, 238, 255))
        gradient57.setColorAt(1, QColor(190, 190, 190, 255))
        brush82 = QBrush(gradient57)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush82)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient58 = QLinearGradient(0, 0, 1, 0)
        gradient58.setSpread(QGradient.PadSpread)
        gradient58.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient58.setColorAt(0, QColor(238, 238, 238, 255))
        gradient58.setColorAt(1, QColor(190, 190, 190, 255))
        brush83 = QBrush(gradient58)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush83)
        gradient59 = QLinearGradient(0, 0, 1, 0)
        gradient59.setSpread(QGradient.PadSpread)
        gradient59.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient59.setColorAt(0, QColor(238, 238, 238, 255))
        gradient59.setColorAt(1, QColor(190, 190, 190, 255))
        brush84 = QBrush(gradient59)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush84)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient60 = QLinearGradient(0, 0, 1, 0)
        gradient60.setSpread(QGradient.PadSpread)
        gradient60.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient60.setColorAt(0, QColor(238, 238, 238, 255))
        gradient60.setColorAt(1, QColor(190, 190, 190, 255))
        brush85 = QBrush(gradient60)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush85)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient61 = QLinearGradient(0, 0, 1, 0)
        gradient61.setSpread(QGradient.PadSpread)
        gradient61.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient61.setColorAt(0, QColor(238, 238, 238, 255))
        gradient61.setColorAt(1, QColor(190, 190, 190, 255))
        brush86 = QBrush(gradient61)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush86)
        gradient62 = QLinearGradient(0, 0, 1, 0)
        gradient62.setSpread(QGradient.PadSpread)
        gradient62.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient62.setColorAt(0, QColor(238, 238, 238, 255))
        gradient62.setColorAt(1, QColor(190, 190, 190, 255))
        brush87 = QBrush(gradient62)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush87)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_appointments.setPalette(palette26)
        self.checkBox_doc_appointments.setFont(font3)
        self.checkBox_doc_appointments.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_appointments, 3, 1, 1, 1)

        self.checkBox_doc_discharge_summary = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_discharge_summary.setObjectName(u"checkBox_doc_discharge_summary")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient63 = QLinearGradient(0, 0, 1, 0)
        gradient63.setSpread(QGradient.PadSpread)
        gradient63.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient63.setColorAt(0, QColor(238, 238, 238, 255))
        gradient63.setColorAt(1, QColor(190, 190, 190, 255))
        brush88 = QBrush(gradient63)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush88)
        palette27.setBrush(QPalette.Active, QPalette.Light, brush)
        palette27.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette27.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette27.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient64 = QLinearGradient(0, 0, 1, 0)
        gradient64.setSpread(QGradient.PadSpread)
        gradient64.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient64.setColorAt(0, QColor(238, 238, 238, 255))
        gradient64.setColorAt(1, QColor(190, 190, 190, 255))
        brush89 = QBrush(gradient64)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush89)
        gradient65 = QLinearGradient(0, 0, 1, 0)
        gradient65.setSpread(QGradient.PadSpread)
        gradient65.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient65.setColorAt(0, QColor(238, 238, 238, 255))
        gradient65.setColorAt(1, QColor(190, 190, 190, 255))
        brush90 = QBrush(gradient65)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush90)
        palette27.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient66 = QLinearGradient(0, 0, 1, 0)
        gradient66.setSpread(QGradient.PadSpread)
        gradient66.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient66.setColorAt(0, QColor(238, 238, 238, 255))
        gradient66.setColorAt(1, QColor(190, 190, 190, 255))
        brush91 = QBrush(gradient66)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush91)
        palette27.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette27.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette27.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient67 = QLinearGradient(0, 0, 1, 0)
        gradient67.setSpread(QGradient.PadSpread)
        gradient67.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient67.setColorAt(0, QColor(238, 238, 238, 255))
        gradient67.setColorAt(1, QColor(190, 190, 190, 255))
        brush92 = QBrush(gradient67)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush92)
        gradient68 = QLinearGradient(0, 0, 1, 0)
        gradient68.setSpread(QGradient.PadSpread)
        gradient68.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient68.setColorAt(0, QColor(238, 238, 238, 255))
        gradient68.setColorAt(1, QColor(190, 190, 190, 255))
        brush93 = QBrush(gradient68)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush93)
        palette27.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient69 = QLinearGradient(0, 0, 1, 0)
        gradient69.setSpread(QGradient.PadSpread)
        gradient69.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient69.setColorAt(0, QColor(238, 238, 238, 255))
        gradient69.setColorAt(1, QColor(190, 190, 190, 255))
        brush94 = QBrush(gradient69)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush94)
        palette27.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette27.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette27.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient70 = QLinearGradient(0, 0, 1, 0)
        gradient70.setSpread(QGradient.PadSpread)
        gradient70.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient70.setColorAt(0, QColor(238, 238, 238, 255))
        gradient70.setColorAt(1, QColor(190, 190, 190, 255))
        brush95 = QBrush(gradient70)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush95)
        gradient71 = QLinearGradient(0, 0, 1, 0)
        gradient71.setSpread(QGradient.PadSpread)
        gradient71.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient71.setColorAt(0, QColor(238, 238, 238, 255))
        gradient71.setColorAt(1, QColor(190, 190, 190, 255))
        brush96 = QBrush(gradient71)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush96)
        palette27.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_discharge_summary.setPalette(palette27)
        self.checkBox_doc_discharge_summary.setFont(font3)
        self.checkBox_doc_discharge_summary.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_discharge_summary, 13, 1, 1, 1)

        self.checkBox_doc_back_frontpage = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_back_frontpage.setObjectName(u"checkBox_doc_back_frontpage")
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient72 = QLinearGradient(0, 0, 1, 0)
        gradient72.setSpread(QGradient.PadSpread)
        gradient72.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient72.setColorAt(0, QColor(238, 238, 238, 255))
        gradient72.setColorAt(1, QColor(190, 190, 190, 255))
        brush97 = QBrush(gradient72)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush97)
        palette28.setBrush(QPalette.Active, QPalette.Light, brush)
        palette28.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette28.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient73 = QLinearGradient(0, 0, 1, 0)
        gradient73.setSpread(QGradient.PadSpread)
        gradient73.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient73.setColorAt(0, QColor(238, 238, 238, 255))
        gradient73.setColorAt(1, QColor(190, 190, 190, 255))
        brush98 = QBrush(gradient73)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush98)
        gradient74 = QLinearGradient(0, 0, 1, 0)
        gradient74.setSpread(QGradient.PadSpread)
        gradient74.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient74.setColorAt(0, QColor(238, 238, 238, 255))
        gradient74.setColorAt(1, QColor(190, 190, 190, 255))
        brush99 = QBrush(gradient74)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush99)
        palette28.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient75 = QLinearGradient(0, 0, 1, 0)
        gradient75.setSpread(QGradient.PadSpread)
        gradient75.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient75.setColorAt(0, QColor(238, 238, 238, 255))
        gradient75.setColorAt(1, QColor(190, 190, 190, 255))
        brush100 = QBrush(gradient75)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush100)
        palette28.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette28.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient76 = QLinearGradient(0, 0, 1, 0)
        gradient76.setSpread(QGradient.PadSpread)
        gradient76.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient76.setColorAt(0, QColor(238, 238, 238, 255))
        gradient76.setColorAt(1, QColor(190, 190, 190, 255))
        brush101 = QBrush(gradient76)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush101)
        gradient77 = QLinearGradient(0, 0, 1, 0)
        gradient77.setSpread(QGradient.PadSpread)
        gradient77.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient77.setColorAt(0, QColor(238, 238, 238, 255))
        gradient77.setColorAt(1, QColor(190, 190, 190, 255))
        brush102 = QBrush(gradient77)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush102)
        palette28.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient78 = QLinearGradient(0, 0, 1, 0)
        gradient78.setSpread(QGradient.PadSpread)
        gradient78.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient78.setColorAt(0, QColor(238, 238, 238, 255))
        gradient78.setColorAt(1, QColor(190, 190, 190, 255))
        brush103 = QBrush(gradient78)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush103)
        palette28.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette28.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient79 = QLinearGradient(0, 0, 1, 0)
        gradient79.setSpread(QGradient.PadSpread)
        gradient79.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient79.setColorAt(0, QColor(238, 238, 238, 255))
        gradient79.setColorAt(1, QColor(190, 190, 190, 255))
        brush104 = QBrush(gradient79)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush104)
        gradient80 = QLinearGradient(0, 0, 1, 0)
        gradient80.setSpread(QGradient.PadSpread)
        gradient80.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient80.setColorAt(0, QColor(238, 238, 238, 255))
        gradient80.setColorAt(1, QColor(190, 190, 190, 255))
        brush105 = QBrush(gradient80)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush105)
        palette28.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_back_frontpage.setPalette(palette28)
        self.checkBox_doc_back_frontpage.setFont(font3)
        self.checkBox_doc_back_frontpage.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_back_frontpage, 17, 2, 1, 1)

        self.checkBox_doc_complex = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_complex.setObjectName(u"checkBox_doc_complex")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient81 = QLinearGradient(0, 0, 1, 0)
        gradient81.setSpread(QGradient.PadSpread)
        gradient81.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient81.setColorAt(0, QColor(238, 238, 238, 255))
        gradient81.setColorAt(1, QColor(190, 190, 190, 255))
        brush106 = QBrush(gradient81)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush106)
        palette29.setBrush(QPalette.Active, QPalette.Light, brush)
        palette29.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette29.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette29.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient82 = QLinearGradient(0, 0, 1, 0)
        gradient82.setSpread(QGradient.PadSpread)
        gradient82.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient82.setColorAt(0, QColor(238, 238, 238, 255))
        gradient82.setColorAt(1, QColor(190, 190, 190, 255))
        brush107 = QBrush(gradient82)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush107)
        gradient83 = QLinearGradient(0, 0, 1, 0)
        gradient83.setSpread(QGradient.PadSpread)
        gradient83.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient83.setColorAt(0, QColor(238, 238, 238, 255))
        gradient83.setColorAt(1, QColor(190, 190, 190, 255))
        brush108 = QBrush(gradient83)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush108)
        palette29.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient84 = QLinearGradient(0, 0, 1, 0)
        gradient84.setSpread(QGradient.PadSpread)
        gradient84.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient84.setColorAt(0, QColor(238, 238, 238, 255))
        gradient84.setColorAt(1, QColor(190, 190, 190, 255))
        brush109 = QBrush(gradient84)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush109)
        palette29.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette29.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette29.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient85 = QLinearGradient(0, 0, 1, 0)
        gradient85.setSpread(QGradient.PadSpread)
        gradient85.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient85.setColorAt(0, QColor(238, 238, 238, 255))
        gradient85.setColorAt(1, QColor(190, 190, 190, 255))
        brush110 = QBrush(gradient85)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush110)
        gradient86 = QLinearGradient(0, 0, 1, 0)
        gradient86.setSpread(QGradient.PadSpread)
        gradient86.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient86.setColorAt(0, QColor(238, 238, 238, 255))
        gradient86.setColorAt(1, QColor(190, 190, 190, 255))
        brush111 = QBrush(gradient86)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush111)
        palette29.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient87 = QLinearGradient(0, 0, 1, 0)
        gradient87.setSpread(QGradient.PadSpread)
        gradient87.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient87.setColorAt(0, QColor(238, 238, 238, 255))
        gradient87.setColorAt(1, QColor(190, 190, 190, 255))
        brush112 = QBrush(gradient87)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush112)
        palette29.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette29.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette29.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient88 = QLinearGradient(0, 0, 1, 0)
        gradient88.setSpread(QGradient.PadSpread)
        gradient88.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient88.setColorAt(0, QColor(238, 238, 238, 255))
        gradient88.setColorAt(1, QColor(190, 190, 190, 255))
        brush113 = QBrush(gradient88)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush113)
        gradient89 = QLinearGradient(0, 0, 1, 0)
        gradient89.setSpread(QGradient.PadSpread)
        gradient89.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient89.setColorAt(0, QColor(238, 238, 238, 255))
        gradient89.setColorAt(1, QColor(190, 190, 190, 255))
        brush114 = QBrush(gradient89)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush114)
        palette29.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_complex.setPalette(palette29)
        self.checkBox_doc_complex.setFont(font3)
        self.checkBox_doc_complex.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_complex, 9, 2, 2, 2)

        self.frame_buttons_doc = QFrame(self.frame_creating_docs)
        self.frame_buttons_doc.setObjectName(u"frame_buttons_doc")
        self.frame_buttons_doc.setMaximumSize(QSize(16777215, 25))
        self.frame_buttons_doc.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_buttons_doc)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_lecalo = QPushButton(self.frame_buttons_doc)
        self.pushButton_lecalo.setObjectName(u"pushButton_lecalo")
        self.pushButton_lecalo.setMinimumSize(QSize(0, 22))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette30.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush)
        palette30.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette30.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette30.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette30.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette30.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette30.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette30.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette30.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette30.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButton_lecalo.setPalette(palette30)
        self.pushButton_lecalo.setFont(font1)
        self.pushButton_lecalo.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_lecalo)

        self.pushButton_clean_ticks = QPushButton(self.frame_buttons_doc)
        self.pushButton_clean_ticks.setObjectName(u"pushButton_clean_ticks")
        self.pushButton_clean_ticks.setMinimumSize(QSize(0, 22))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette31.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush)
        palette31.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette31.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette31.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette31.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette31.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette31.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButton_clean_ticks.setPalette(palette31)
        self.pushButton_clean_ticks.setFont(font1)
        self.pushButton_clean_ticks.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_clean_ticks)


        self.gridLayout_4.addWidget(self.frame_buttons_doc, 1, 2, 1, 2)

        self.checkBox_doc_frontpage = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_frontpage.setObjectName(u"checkBox_doc_frontpage")
        self.checkBox_doc_frontpage.setEnabled(False)
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient90 = QLinearGradient(0, 0, 1, 0)
        gradient90.setSpread(QGradient.PadSpread)
        gradient90.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient90.setColorAt(0, QColor(238, 238, 238, 255))
        gradient90.setColorAt(1, QColor(190, 190, 190, 255))
        brush115 = QBrush(gradient90)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush115)
        palette32.setBrush(QPalette.Active, QPalette.Light, brush)
        palette32.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette32.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette32.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient91 = QLinearGradient(0, 0, 1, 0)
        gradient91.setSpread(QGradient.PadSpread)
        gradient91.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient91.setColorAt(0, QColor(238, 238, 238, 255))
        gradient91.setColorAt(1, QColor(190, 190, 190, 255))
        brush116 = QBrush(gradient91)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush116)
        gradient92 = QLinearGradient(0, 0, 1, 0)
        gradient92.setSpread(QGradient.PadSpread)
        gradient92.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient92.setColorAt(0, QColor(238, 238, 238, 255))
        gradient92.setColorAt(1, QColor(190, 190, 190, 255))
        brush117 = QBrush(gradient92)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush117)
        palette32.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient93 = QLinearGradient(0, 0, 1, 0)
        gradient93.setSpread(QGradient.PadSpread)
        gradient93.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient93.setColorAt(0, QColor(238, 238, 238, 255))
        gradient93.setColorAt(1, QColor(190, 190, 190, 255))
        brush118 = QBrush(gradient93)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush118)
        palette32.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette32.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette32.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient94 = QLinearGradient(0, 0, 1, 0)
        gradient94.setSpread(QGradient.PadSpread)
        gradient94.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient94.setColorAt(0, QColor(238, 238, 238, 255))
        gradient94.setColorAt(1, QColor(190, 190, 190, 255))
        brush119 = QBrush(gradient94)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush119)
        gradient95 = QLinearGradient(0, 0, 1, 0)
        gradient95.setSpread(QGradient.PadSpread)
        gradient95.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient95.setColorAt(0, QColor(238, 238, 238, 255))
        gradient95.setColorAt(1, QColor(190, 190, 190, 255))
        brush120 = QBrush(gradient95)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush120)
        palette32.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient96 = QLinearGradient(0, 0, 1, 0)
        gradient96.setSpread(QGradient.PadSpread)
        gradient96.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient96.setColorAt(0, QColor(238, 238, 238, 255))
        gradient96.setColorAt(1, QColor(190, 190, 190, 255))
        brush121 = QBrush(gradient96)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush121)
        palette32.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette32.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette32.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient97 = QLinearGradient(0, 0, 1, 0)
        gradient97.setSpread(QGradient.PadSpread)
        gradient97.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient97.setColorAt(0, QColor(238, 238, 238, 255))
        gradient97.setColorAt(1, QColor(190, 190, 190, 255))
        brush122 = QBrush(gradient97)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush122)
        gradient98 = QLinearGradient(0, 0, 1, 0)
        gradient98.setSpread(QGradient.PadSpread)
        gradient98.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient98.setColorAt(0, QColor(238, 238, 238, 255))
        gradient98.setColorAt(1, QColor(190, 190, 190, 255))
        brush123 = QBrush(gradient98)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush123)
        palette32.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_frontpage.setPalette(palette32)
        self.checkBox_doc_frontpage.setFont(font3)
        self.checkBox_doc_frontpage.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_frontpage, 17, 1, 1, 1)

        self.checkBox_doc_statistic_talon_face = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_statistic_talon_face.setObjectName(u"checkBox_doc_statistic_talon_face")
        self.checkBox_doc_statistic_talon_face.setEnabled(False)
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient99 = QLinearGradient(0, 0, 1, 0)
        gradient99.setSpread(QGradient.PadSpread)
        gradient99.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient99.setColorAt(0, QColor(238, 238, 238, 255))
        gradient99.setColorAt(1, QColor(190, 190, 190, 255))
        brush124 = QBrush(gradient99)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush124)
        palette33.setBrush(QPalette.Active, QPalette.Light, brush)
        palette33.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette33.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette33.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient100 = QLinearGradient(0, 0, 1, 0)
        gradient100.setSpread(QGradient.PadSpread)
        gradient100.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient100.setColorAt(0, QColor(238, 238, 238, 255))
        gradient100.setColorAt(1, QColor(190, 190, 190, 255))
        brush125 = QBrush(gradient100)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush125)
        gradient101 = QLinearGradient(0, 0, 1, 0)
        gradient101.setSpread(QGradient.PadSpread)
        gradient101.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient101.setColorAt(0, QColor(238, 238, 238, 255))
        gradient101.setColorAt(1, QColor(190, 190, 190, 255))
        brush126 = QBrush(gradient101)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush126)
        palette33.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient102 = QLinearGradient(0, 0, 1, 0)
        gradient102.setSpread(QGradient.PadSpread)
        gradient102.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient102.setColorAt(0, QColor(238, 238, 238, 255))
        gradient102.setColorAt(1, QColor(190, 190, 190, 255))
        brush127 = QBrush(gradient102)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush127)
        palette33.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette33.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette33.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient103 = QLinearGradient(0, 0, 1, 0)
        gradient103.setSpread(QGradient.PadSpread)
        gradient103.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient103.setColorAt(0, QColor(238, 238, 238, 255))
        gradient103.setColorAt(1, QColor(190, 190, 190, 255))
        brush128 = QBrush(gradient103)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush128)
        gradient104 = QLinearGradient(0, 0, 1, 0)
        gradient104.setSpread(QGradient.PadSpread)
        gradient104.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient104.setColorAt(0, QColor(238, 238, 238, 255))
        gradient104.setColorAt(1, QColor(190, 190, 190, 255))
        brush129 = QBrush(gradient104)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush129)
        palette33.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient105 = QLinearGradient(0, 0, 1, 0)
        gradient105.setSpread(QGradient.PadSpread)
        gradient105.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient105.setColorAt(0, QColor(238, 238, 238, 255))
        gradient105.setColorAt(1, QColor(190, 190, 190, 255))
        brush130 = QBrush(gradient105)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush130)
        palette33.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette33.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette33.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient106 = QLinearGradient(0, 0, 1, 0)
        gradient106.setSpread(QGradient.PadSpread)
        gradient106.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient106.setColorAt(0, QColor(238, 238, 238, 255))
        gradient106.setColorAt(1, QColor(190, 190, 190, 255))
        brush131 = QBrush(gradient106)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush131)
        gradient107 = QLinearGradient(0, 0, 1, 0)
        gradient107.setSpread(QGradient.PadSpread)
        gradient107.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient107.setColorAt(0, QColor(238, 238, 238, 255))
        gradient107.setColorAt(1, QColor(190, 190, 190, 255))
        brush132 = QBrush(gradient107)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush132)
        palette33.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_statistic_talon_face.setPalette(palette33)
        self.checkBox_doc_statistic_talon_face.setFont(font3)
        self.checkBox_doc_statistic_talon_face.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_statistic_talon_face, 4, 1, 1, 1)

        self.checkBox_doc_directions = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_directions.setObjectName(u"checkBox_doc_directions")
        self.checkBox_doc_directions.setEnabled(False)
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient108 = QLinearGradient(0, 0, 1, 0)
        gradient108.setSpread(QGradient.PadSpread)
        gradient108.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient108.setColorAt(0, QColor(238, 238, 238, 255))
        gradient108.setColorAt(1, QColor(190, 190, 190, 255))
        brush133 = QBrush(gradient108)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush133)
        palette34.setBrush(QPalette.Active, QPalette.Light, brush)
        palette34.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette34.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette34.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient109 = QLinearGradient(0, 0, 1, 0)
        gradient109.setSpread(QGradient.PadSpread)
        gradient109.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient109.setColorAt(0, QColor(238, 238, 238, 255))
        gradient109.setColorAt(1, QColor(190, 190, 190, 255))
        brush134 = QBrush(gradient109)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush134)
        gradient110 = QLinearGradient(0, 0, 1, 0)
        gradient110.setSpread(QGradient.PadSpread)
        gradient110.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient110.setColorAt(0, QColor(238, 238, 238, 255))
        gradient110.setColorAt(1, QColor(190, 190, 190, 255))
        brush135 = QBrush(gradient110)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush135)
        palette34.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient111 = QLinearGradient(0, 0, 1, 0)
        gradient111.setSpread(QGradient.PadSpread)
        gradient111.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient111.setColorAt(0, QColor(238, 238, 238, 255))
        gradient111.setColorAt(1, QColor(190, 190, 190, 255))
        brush136 = QBrush(gradient111)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush136)
        palette34.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette34.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette34.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient112 = QLinearGradient(0, 0, 1, 0)
        gradient112.setSpread(QGradient.PadSpread)
        gradient112.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient112.setColorAt(0, QColor(238, 238, 238, 255))
        gradient112.setColorAt(1, QColor(190, 190, 190, 255))
        brush137 = QBrush(gradient112)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush137)
        gradient113 = QLinearGradient(0, 0, 1, 0)
        gradient113.setSpread(QGradient.PadSpread)
        gradient113.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient113.setColorAt(0, QColor(238, 238, 238, 255))
        gradient113.setColorAt(1, QColor(190, 190, 190, 255))
        brush138 = QBrush(gradient113)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush138)
        palette34.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient114 = QLinearGradient(0, 0, 1, 0)
        gradient114.setSpread(QGradient.PadSpread)
        gradient114.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient114.setColorAt(0, QColor(238, 238, 238, 255))
        gradient114.setColorAt(1, QColor(190, 190, 190, 255))
        brush139 = QBrush(gradient114)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush139)
        palette34.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette34.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette34.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient115 = QLinearGradient(0, 0, 1, 0)
        gradient115.setSpread(QGradient.PadSpread)
        gradient115.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient115.setColorAt(0, QColor(238, 238, 238, 255))
        gradient115.setColorAt(1, QColor(190, 190, 190, 255))
        brush140 = QBrush(gradient115)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush140)
        gradient116 = QLinearGradient(0, 0, 1, 0)
        gradient116.setSpread(QGradient.PadSpread)
        gradient116.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient116.setColorAt(0, QColor(238, 238, 238, 255))
        gradient116.setColorAt(1, QColor(190, 190, 190, 255))
        brush141 = QBrush(gradient116)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush141)
        palette34.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_directions.setPalette(palette34)
        self.checkBox_doc_directions.setFont(font3)
        self.checkBox_doc_directions.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_directions, 13, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 7, 1, 1, 1)

        self.checkBox_lfk_report_sheet = QCheckBox(self.frame_creating_docs)
        self.checkBox_lfk_report_sheet.setObjectName(u"checkBox_lfk_report_sheet")
        self.checkBox_lfk_report_sheet.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_lfk_report_sheet, 14, 1, 1, 2)

        self.checkBox_doc_med_commission_drugs = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_med_commission_drugs.setObjectName(u"checkBox_doc_med_commission_drugs")
        self.checkBox_doc_med_commission_drugs.setEnabled(False)
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient117 = QLinearGradient(0, 0, 1, 0)
        gradient117.setSpread(QGradient.PadSpread)
        gradient117.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient117.setColorAt(0, QColor(238, 238, 238, 255))
        gradient117.setColorAt(1, QColor(190, 190, 190, 255))
        brush142 = QBrush(gradient117)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush142)
        palette35.setBrush(QPalette.Active, QPalette.Light, brush)
        palette35.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette35.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette35.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient118 = QLinearGradient(0, 0, 1, 0)
        gradient118.setSpread(QGradient.PadSpread)
        gradient118.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient118.setColorAt(0, QColor(238, 238, 238, 255))
        gradient118.setColorAt(1, QColor(190, 190, 190, 255))
        brush143 = QBrush(gradient118)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush143)
        gradient119 = QLinearGradient(0, 0, 1, 0)
        gradient119.setSpread(QGradient.PadSpread)
        gradient119.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient119.setColorAt(0, QColor(238, 238, 238, 255))
        gradient119.setColorAt(1, QColor(190, 190, 190, 255))
        brush144 = QBrush(gradient119)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush144)
        palette35.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient120 = QLinearGradient(0, 0, 1, 0)
        gradient120.setSpread(QGradient.PadSpread)
        gradient120.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient120.setColorAt(0, QColor(238, 238, 238, 255))
        gradient120.setColorAt(1, QColor(190, 190, 190, 255))
        brush145 = QBrush(gradient120)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush145)
        palette35.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette35.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette35.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient121 = QLinearGradient(0, 0, 1, 0)
        gradient121.setSpread(QGradient.PadSpread)
        gradient121.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient121.setColorAt(0, QColor(238, 238, 238, 255))
        gradient121.setColorAt(1, QColor(190, 190, 190, 255))
        brush146 = QBrush(gradient121)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush146)
        gradient122 = QLinearGradient(0, 0, 1, 0)
        gradient122.setSpread(QGradient.PadSpread)
        gradient122.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient122.setColorAt(0, QColor(238, 238, 238, 255))
        gradient122.setColorAt(1, QColor(190, 190, 190, 255))
        brush147 = QBrush(gradient122)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush147)
        palette35.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient123 = QLinearGradient(0, 0, 1, 0)
        gradient123.setSpread(QGradient.PadSpread)
        gradient123.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient123.setColorAt(0, QColor(238, 238, 238, 255))
        gradient123.setColorAt(1, QColor(190, 190, 190, 255))
        brush148 = QBrush(gradient123)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush148)
        palette35.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette35.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette35.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient124 = QLinearGradient(0, 0, 1, 0)
        gradient124.setSpread(QGradient.PadSpread)
        gradient124.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient124.setColorAt(0, QColor(238, 238, 238, 255))
        gradient124.setColorAt(1, QColor(190, 190, 190, 255))
        brush149 = QBrush(gradient124)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush149)
        gradient125 = QLinearGradient(0, 0, 1, 0)
        gradient125.setSpread(QGradient.PadSpread)
        gradient125.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient125.setColorAt(0, QColor(238, 238, 238, 255))
        gradient125.setColorAt(1, QColor(190, 190, 190, 255))
        brush150 = QBrush(gradient125)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush150)
        palette35.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_med_commission_drugs.setPalette(palette35)
        self.checkBox_doc_med_commission_drugs.setFont(font3)
        self.checkBox_doc_med_commission_drugs.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")
        self.checkBox_doc_med_commission_drugs.setCheckable(True)
        self.checkBox_doc_med_commission_drugs.setChecked(False)

        self.gridLayout_4.addWidget(self.checkBox_doc_med_commission_drugs, 5, 3, 1, 1)

        self.label_creating_docs = QLabel(self.frame_creating_docs)
        self.label_creating_docs.setObjectName(u"label_creating_docs")
        self.label_creating_docs.setMaximumSize(QSize(16777215, 30))
        self.label_creating_docs.setFont(font4)
        self.label_creating_docs.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_creating_docs.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_creating_docs, 0, 0, 1, 5)

        self.checkBox_doc_final_diary = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_final_diary.setObjectName(u"checkBox_doc_final_diary")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient126 = QLinearGradient(0, 0, 1, 0)
        gradient126.setSpread(QGradient.PadSpread)
        gradient126.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient126.setColorAt(0, QColor(238, 238, 238, 255))
        gradient126.setColorAt(1, QColor(190, 190, 190, 255))
        brush151 = QBrush(gradient126)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush151)
        palette36.setBrush(QPalette.Active, QPalette.Light, brush)
        palette36.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette36.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette36.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient127 = QLinearGradient(0, 0, 1, 0)
        gradient127.setSpread(QGradient.PadSpread)
        gradient127.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient127.setColorAt(0, QColor(238, 238, 238, 255))
        gradient127.setColorAt(1, QColor(190, 190, 190, 255))
        brush152 = QBrush(gradient127)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush152)
        gradient128 = QLinearGradient(0, 0, 1, 0)
        gradient128.setSpread(QGradient.PadSpread)
        gradient128.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient128.setColorAt(0, QColor(238, 238, 238, 255))
        gradient128.setColorAt(1, QColor(190, 190, 190, 255))
        brush153 = QBrush(gradient128)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush153)
        palette36.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient129 = QLinearGradient(0, 0, 1, 0)
        gradient129.setSpread(QGradient.PadSpread)
        gradient129.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient129.setColorAt(0, QColor(238, 238, 238, 255))
        gradient129.setColorAt(1, QColor(190, 190, 190, 255))
        brush154 = QBrush(gradient129)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush154)
        palette36.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette36.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette36.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient130 = QLinearGradient(0, 0, 1, 0)
        gradient130.setSpread(QGradient.PadSpread)
        gradient130.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient130.setColorAt(0, QColor(238, 238, 238, 255))
        gradient130.setColorAt(1, QColor(190, 190, 190, 255))
        brush155 = QBrush(gradient130)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush155)
        gradient131 = QLinearGradient(0, 0, 1, 0)
        gradient131.setSpread(QGradient.PadSpread)
        gradient131.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient131.setColorAt(0, QColor(238, 238, 238, 255))
        gradient131.setColorAt(1, QColor(190, 190, 190, 255))
        brush156 = QBrush(gradient131)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush156)
        palette36.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient132 = QLinearGradient(0, 0, 1, 0)
        gradient132.setSpread(QGradient.PadSpread)
        gradient132.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient132.setColorAt(0, QColor(238, 238, 238, 255))
        gradient132.setColorAt(1, QColor(190, 190, 190, 255))
        brush157 = QBrush(gradient132)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush157)
        palette36.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette36.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette36.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient133 = QLinearGradient(0, 0, 1, 0)
        gradient133.setSpread(QGradient.PadSpread)
        gradient133.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient133.setColorAt(0, QColor(238, 238, 238, 255))
        gradient133.setColorAt(1, QColor(190, 190, 190, 255))
        brush158 = QBrush(gradient133)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush158)
        gradient134 = QLinearGradient(0, 0, 1, 0)
        gradient134.setSpread(QGradient.PadSpread)
        gradient134.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient134.setColorAt(0, QColor(238, 238, 238, 255))
        gradient134.setColorAt(1, QColor(190, 190, 190, 255))
        brush159 = QBrush(gradient134)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush159)
        palette36.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_final_diary.setPalette(palette36)
        self.checkBox_doc_final_diary.setFont(font3)
        self.checkBox_doc_final_diary.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_final_diary, 11, 1, 1, 1)

        self.checkBox_doc_diaries = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_diaries.setObjectName(u"checkBox_doc_diaries")
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient135 = QLinearGradient(0, 0, 1, 0)
        gradient135.setSpread(QGradient.PadSpread)
        gradient135.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient135.setColorAt(0, QColor(238, 238, 238, 255))
        gradient135.setColorAt(1, QColor(190, 190, 190, 255))
        brush160 = QBrush(gradient135)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush160)
        palette37.setBrush(QPalette.Active, QPalette.Light, brush)
        palette37.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette37.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette37.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient136 = QLinearGradient(0, 0, 1, 0)
        gradient136.setSpread(QGradient.PadSpread)
        gradient136.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient136.setColorAt(0, QColor(238, 238, 238, 255))
        gradient136.setColorAt(1, QColor(190, 190, 190, 255))
        brush161 = QBrush(gradient136)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush161)
        gradient137 = QLinearGradient(0, 0, 1, 0)
        gradient137.setSpread(QGradient.PadSpread)
        gradient137.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient137.setColorAt(0, QColor(238, 238, 238, 255))
        gradient137.setColorAt(1, QColor(190, 190, 190, 255))
        brush162 = QBrush(gradient137)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush162)
        palette37.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient138 = QLinearGradient(0, 0, 1, 0)
        gradient138.setSpread(QGradient.PadSpread)
        gradient138.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient138.setColorAt(0, QColor(238, 238, 238, 255))
        gradient138.setColorAt(1, QColor(190, 190, 190, 255))
        brush163 = QBrush(gradient138)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush163)
        palette37.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette37.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette37.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient139 = QLinearGradient(0, 0, 1, 0)
        gradient139.setSpread(QGradient.PadSpread)
        gradient139.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient139.setColorAt(0, QColor(238, 238, 238, 255))
        gradient139.setColorAt(1, QColor(190, 190, 190, 255))
        brush164 = QBrush(gradient139)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush164)
        gradient140 = QLinearGradient(0, 0, 1, 0)
        gradient140.setSpread(QGradient.PadSpread)
        gradient140.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient140.setColorAt(0, QColor(238, 238, 238, 255))
        gradient140.setColorAt(1, QColor(190, 190, 190, 255))
        brush165 = QBrush(gradient140)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush165)
        palette37.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient141 = QLinearGradient(0, 0, 1, 0)
        gradient141.setSpread(QGradient.PadSpread)
        gradient141.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient141.setColorAt(0, QColor(238, 238, 238, 255))
        gradient141.setColorAt(1, QColor(190, 190, 190, 255))
        brush166 = QBrush(gradient141)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush166)
        palette37.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette37.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette37.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient142 = QLinearGradient(0, 0, 1, 0)
        gradient142.setSpread(QGradient.PadSpread)
        gradient142.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient142.setColorAt(0, QColor(238, 238, 238, 255))
        gradient142.setColorAt(1, QColor(190, 190, 190, 255))
        brush167 = QBrush(gradient142)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush167)
        gradient143 = QLinearGradient(0, 0, 1, 0)
        gradient143.setSpread(QGradient.PadSpread)
        gradient143.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient143.setColorAt(0, QColor(238, 238, 238, 255))
        gradient143.setColorAt(1, QColor(190, 190, 190, 255))
        brush168 = QBrush(gradient143)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush168)
        palette37.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_diaries.setPalette(palette37)
        self.checkBox_doc_diaries.setFont(font3)
        self.checkBox_doc_diaries.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_diaries, 8, 1, 1, 1)

        self.checkBox_doc_pass = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_pass.setObjectName(u"checkBox_doc_pass")
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient144 = QLinearGradient(0, 0, 1, 0)
        gradient144.setSpread(QGradient.PadSpread)
        gradient144.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient144.setColorAt(0, QColor(238, 238, 238, 255))
        gradient144.setColorAt(1, QColor(190, 190, 190, 255))
        brush169 = QBrush(gradient144)
        palette38.setBrush(QPalette.Active, QPalette.Button, brush169)
        palette38.setBrush(QPalette.Active, QPalette.Light, brush)
        palette38.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette38.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette38.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette38.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient145 = QLinearGradient(0, 0, 1, 0)
        gradient145.setSpread(QGradient.PadSpread)
        gradient145.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient145.setColorAt(0, QColor(238, 238, 238, 255))
        gradient145.setColorAt(1, QColor(190, 190, 190, 255))
        brush170 = QBrush(gradient145)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush170)
        gradient146 = QLinearGradient(0, 0, 1, 0)
        gradient146.setSpread(QGradient.PadSpread)
        gradient146.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient146.setColorAt(0, QColor(238, 238, 238, 255))
        gradient146.setColorAt(1, QColor(190, 190, 190, 255))
        brush171 = QBrush(gradient146)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush171)
        palette38.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient147 = QLinearGradient(0, 0, 1, 0)
        gradient147.setSpread(QGradient.PadSpread)
        gradient147.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient147.setColorAt(0, QColor(238, 238, 238, 255))
        gradient147.setColorAt(1, QColor(190, 190, 190, 255))
        brush172 = QBrush(gradient147)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush172)
        palette38.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette38.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette38.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette38.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient148 = QLinearGradient(0, 0, 1, 0)
        gradient148.setSpread(QGradient.PadSpread)
        gradient148.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient148.setColorAt(0, QColor(238, 238, 238, 255))
        gradient148.setColorAt(1, QColor(190, 190, 190, 255))
        brush173 = QBrush(gradient148)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush173)
        gradient149 = QLinearGradient(0, 0, 1, 0)
        gradient149.setSpread(QGradient.PadSpread)
        gradient149.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient149.setColorAt(0, QColor(238, 238, 238, 255))
        gradient149.setColorAt(1, QColor(190, 190, 190, 255))
        brush174 = QBrush(gradient149)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush174)
        palette38.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette38.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient150 = QLinearGradient(0, 0, 1, 0)
        gradient150.setSpread(QGradient.PadSpread)
        gradient150.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient150.setColorAt(0, QColor(238, 238, 238, 255))
        gradient150.setColorAt(1, QColor(190, 190, 190, 255))
        brush175 = QBrush(gradient150)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush175)
        palette38.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette38.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette38.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette38.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient151 = QLinearGradient(0, 0, 1, 0)
        gradient151.setSpread(QGradient.PadSpread)
        gradient151.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient151.setColorAt(0, QColor(238, 238, 238, 255))
        gradient151.setColorAt(1, QColor(190, 190, 190, 255))
        brush176 = QBrush(gradient151)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush176)
        gradient152 = QLinearGradient(0, 0, 1, 0)
        gradient152.setSpread(QGradient.PadSpread)
        gradient152.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient152.setColorAt(0, QColor(238, 238, 238, 255))
        gradient152.setColorAt(1, QColor(190, 190, 190, 255))
        brush177 = QBrush(gradient152)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush177)
        palette38.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_pass.setPalette(palette38)
        self.checkBox_doc_pass.setFont(font3)
        self.checkBox_doc_pass.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_pass, 16, 1, 1, 1)

        self.checkBox_doc_reference = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_reference.setObjectName(u"checkBox_doc_reference")
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient153 = QLinearGradient(0, 0, 1, 0)
        gradient153.setSpread(QGradient.PadSpread)
        gradient153.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient153.setColorAt(0, QColor(238, 238, 238, 255))
        gradient153.setColorAt(1, QColor(190, 190, 190, 255))
        brush178 = QBrush(gradient153)
        palette39.setBrush(QPalette.Active, QPalette.Button, brush178)
        palette39.setBrush(QPalette.Active, QPalette.Light, brush)
        palette39.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette39.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette39.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette39.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient154 = QLinearGradient(0, 0, 1, 0)
        gradient154.setSpread(QGradient.PadSpread)
        gradient154.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient154.setColorAt(0, QColor(238, 238, 238, 255))
        gradient154.setColorAt(1, QColor(190, 190, 190, 255))
        brush179 = QBrush(gradient154)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush179)
        gradient155 = QLinearGradient(0, 0, 1, 0)
        gradient155.setSpread(QGradient.PadSpread)
        gradient155.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient155.setColorAt(0, QColor(238, 238, 238, 255))
        gradient155.setColorAt(1, QColor(190, 190, 190, 255))
        brush180 = QBrush(gradient155)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush180)
        palette39.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient156 = QLinearGradient(0, 0, 1, 0)
        gradient156.setSpread(QGradient.PadSpread)
        gradient156.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient156.setColorAt(0, QColor(238, 238, 238, 255))
        gradient156.setColorAt(1, QColor(190, 190, 190, 255))
        brush181 = QBrush(gradient156)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush181)
        palette39.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette39.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette39.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette39.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient157 = QLinearGradient(0, 0, 1, 0)
        gradient157.setSpread(QGradient.PadSpread)
        gradient157.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient157.setColorAt(0, QColor(238, 238, 238, 255))
        gradient157.setColorAt(1, QColor(190, 190, 190, 255))
        brush182 = QBrush(gradient157)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush182)
        gradient158 = QLinearGradient(0, 0, 1, 0)
        gradient158.setSpread(QGradient.PadSpread)
        gradient158.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient158.setColorAt(0, QColor(238, 238, 238, 255))
        gradient158.setColorAt(1, QColor(190, 190, 190, 255))
        brush183 = QBrush(gradient158)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush183)
        palette39.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette39.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient159 = QLinearGradient(0, 0, 1, 0)
        gradient159.setSpread(QGradient.PadSpread)
        gradient159.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient159.setColorAt(0, QColor(238, 238, 238, 255))
        gradient159.setColorAt(1, QColor(190, 190, 190, 255))
        brush184 = QBrush(gradient159)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush184)
        palette39.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette39.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette39.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette39.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient160 = QLinearGradient(0, 0, 1, 0)
        gradient160.setSpread(QGradient.PadSpread)
        gradient160.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient160.setColorAt(0, QColor(238, 238, 238, 255))
        gradient160.setColorAt(1, QColor(190, 190, 190, 255))
        brush185 = QBrush(gradient160)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush185)
        gradient161 = QLinearGradient(0, 0, 1, 0)
        gradient161.setSpread(QGradient.PadSpread)
        gradient161.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient161.setColorAt(0, QColor(238, 238, 238, 255))
        gradient161.setColorAt(1, QColor(190, 190, 190, 255))
        brush186 = QBrush(gradient161)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush186)
        palette39.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_reference.setPalette(palette39)
        self.checkBox_doc_reference.setFont(font3)
        self.checkBox_doc_reference.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_reference, 14, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 12, 1, 1, 1)

        self.checkBox_doc_med_commission_dis = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_med_commission_dis.setObjectName(u"checkBox_doc_med_commission_dis")
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient162 = QLinearGradient(0, 0, 1, 0)
        gradient162.setSpread(QGradient.PadSpread)
        gradient162.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient162.setColorAt(0, QColor(238, 238, 238, 255))
        gradient162.setColorAt(1, QColor(190, 190, 190, 255))
        brush187 = QBrush(gradient162)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush187)
        palette40.setBrush(QPalette.Active, QPalette.Light, brush)
        palette40.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette40.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette40.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient163 = QLinearGradient(0, 0, 1, 0)
        gradient163.setSpread(QGradient.PadSpread)
        gradient163.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient163.setColorAt(0, QColor(238, 238, 238, 255))
        gradient163.setColorAt(1, QColor(190, 190, 190, 255))
        brush188 = QBrush(gradient163)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush188)
        gradient164 = QLinearGradient(0, 0, 1, 0)
        gradient164.setSpread(QGradient.PadSpread)
        gradient164.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient164.setColorAt(0, QColor(238, 238, 238, 255))
        gradient164.setColorAt(1, QColor(190, 190, 190, 255))
        brush189 = QBrush(gradient164)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush189)
        palette40.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient165 = QLinearGradient(0, 0, 1, 0)
        gradient165.setSpread(QGradient.PadSpread)
        gradient165.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient165.setColorAt(0, QColor(238, 238, 238, 255))
        gradient165.setColorAt(1, QColor(190, 190, 190, 255))
        brush190 = QBrush(gradient165)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush190)
        palette40.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette40.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette40.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient166 = QLinearGradient(0, 0, 1, 0)
        gradient166.setSpread(QGradient.PadSpread)
        gradient166.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient166.setColorAt(0, QColor(238, 238, 238, 255))
        gradient166.setColorAt(1, QColor(190, 190, 190, 255))
        brush191 = QBrush(gradient166)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush191)
        gradient167 = QLinearGradient(0, 0, 1, 0)
        gradient167.setSpread(QGradient.PadSpread)
        gradient167.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient167.setColorAt(0, QColor(238, 238, 238, 255))
        gradient167.setColorAt(1, QColor(190, 190, 190, 255))
        brush192 = QBrush(gradient167)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush192)
        palette40.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient168 = QLinearGradient(0, 0, 1, 0)
        gradient168.setSpread(QGradient.PadSpread)
        gradient168.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient168.setColorAt(0, QColor(238, 238, 238, 255))
        gradient168.setColorAt(1, QColor(190, 190, 190, 255))
        brush193 = QBrush(gradient168)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush193)
        palette40.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette40.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette40.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient169 = QLinearGradient(0, 0, 1, 0)
        gradient169.setSpread(QGradient.PadSpread)
        gradient169.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient169.setColorAt(0, QColor(238, 238, 238, 255))
        gradient169.setColorAt(1, QColor(190, 190, 190, 255))
        brush194 = QBrush(gradient169)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush194)
        gradient170 = QLinearGradient(0, 0, 1, 0)
        gradient170.setSpread(QGradient.PadSpread)
        gradient170.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient170.setColorAt(0, QColor(238, 238, 238, 255))
        gradient170.setColorAt(1, QColor(190, 190, 190, 255))
        brush195 = QBrush(gradient170)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush195)
        palette40.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_med_commission_dis.setPalette(palette40)
        self.checkBox_doc_med_commission_dis.setFont(font3)
        self.checkBox_doc_med_commission_dis.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")
        self.checkBox_doc_med_commission_dis.setCheckable(True)
        self.checkBox_doc_med_commission_dis.setChecked(False)

        self.gridLayout_4.addWidget(self.checkBox_doc_med_commission_dis, 4, 3, 1, 1)

        self.checkBox_doc_full_history = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_full_history.setObjectName(u"checkBox_doc_full_history")
        self.checkBox_doc_full_history.setEnabled(False)
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient171 = QLinearGradient(0, 0, 1, 0)
        gradient171.setSpread(QGradient.PadSpread)
        gradient171.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient171.setColorAt(0, QColor(238, 238, 238, 255))
        gradient171.setColorAt(1, QColor(190, 190, 190, 255))
        brush196 = QBrush(gradient171)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush196)
        palette41.setBrush(QPalette.Active, QPalette.Light, brush)
        palette41.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette41.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette41.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient172 = QLinearGradient(0, 0, 1, 0)
        gradient172.setSpread(QGradient.PadSpread)
        gradient172.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient172.setColorAt(0, QColor(238, 238, 238, 255))
        gradient172.setColorAt(1, QColor(190, 190, 190, 255))
        brush197 = QBrush(gradient172)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush197)
        gradient173 = QLinearGradient(0, 0, 1, 0)
        gradient173.setSpread(QGradient.PadSpread)
        gradient173.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient173.setColorAt(0, QColor(238, 238, 238, 255))
        gradient173.setColorAt(1, QColor(190, 190, 190, 255))
        brush198 = QBrush(gradient173)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush198)
        palette41.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient174 = QLinearGradient(0, 0, 1, 0)
        gradient174.setSpread(QGradient.PadSpread)
        gradient174.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient174.setColorAt(0, QColor(238, 238, 238, 255))
        gradient174.setColorAt(1, QColor(190, 190, 190, 255))
        brush199 = QBrush(gradient174)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush199)
        palette41.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette41.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette41.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient175 = QLinearGradient(0, 0, 1, 0)
        gradient175.setSpread(QGradient.PadSpread)
        gradient175.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient175.setColorAt(0, QColor(238, 238, 238, 255))
        gradient175.setColorAt(1, QColor(190, 190, 190, 255))
        brush200 = QBrush(gradient175)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush200)
        gradient176 = QLinearGradient(0, 0, 1, 0)
        gradient176.setSpread(QGradient.PadSpread)
        gradient176.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient176.setColorAt(0, QColor(238, 238, 238, 255))
        gradient176.setColorAt(1, QColor(190, 190, 190, 255))
        brush201 = QBrush(gradient176)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush201)
        palette41.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient177 = QLinearGradient(0, 0, 1, 0)
        gradient177.setSpread(QGradient.PadSpread)
        gradient177.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient177.setColorAt(0, QColor(238, 238, 238, 255))
        gradient177.setColorAt(1, QColor(190, 190, 190, 255))
        brush202 = QBrush(gradient177)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush202)
        palette41.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette41.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette41.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient178 = QLinearGradient(0, 0, 1, 0)
        gradient178.setSpread(QGradient.PadSpread)
        gradient178.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient178.setColorAt(0, QColor(238, 238, 238, 255))
        gradient178.setColorAt(1, QColor(190, 190, 190, 255))
        brush203 = QBrush(gradient178)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush203)
        gradient179 = QLinearGradient(0, 0, 1, 0)
        gradient179.setSpread(QGradient.PadSpread)
        gradient179.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient179.setColorAt(0, QColor(238, 238, 238, 255))
        gradient179.setColorAt(1, QColor(190, 190, 190, 255))
        brush204 = QBrush(gradient179)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush204)
        palette41.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_full_history.setPalette(palette41)
        self.checkBox_doc_full_history.setFont(font3)
        self.checkBox_doc_full_history.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_full_history, 19, 1, 1, 2)

        self.checkBox_doc_consents = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_consents.setObjectName(u"checkBox_doc_consents")
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient180 = QLinearGradient(0, 0, 1, 0)
        gradient180.setSpread(QGradient.PadSpread)
        gradient180.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient180.setColorAt(0, QColor(238, 238, 238, 255))
        gradient180.setColorAt(1, QColor(190, 190, 190, 255))
        brush205 = QBrush(gradient180)
        palette42.setBrush(QPalette.Active, QPalette.Button, brush205)
        palette42.setBrush(QPalette.Active, QPalette.Light, brush)
        palette42.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette42.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette42.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient181 = QLinearGradient(0, 0, 1, 0)
        gradient181.setSpread(QGradient.PadSpread)
        gradient181.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient181.setColorAt(0, QColor(238, 238, 238, 255))
        gradient181.setColorAt(1, QColor(190, 190, 190, 255))
        brush206 = QBrush(gradient181)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush206)
        gradient182 = QLinearGradient(0, 0, 1, 0)
        gradient182.setSpread(QGradient.PadSpread)
        gradient182.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient182.setColorAt(0, QColor(238, 238, 238, 255))
        gradient182.setColorAt(1, QColor(190, 190, 190, 255))
        brush207 = QBrush(gradient182)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush207)
        palette42.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient183 = QLinearGradient(0, 0, 1, 0)
        gradient183.setSpread(QGradient.PadSpread)
        gradient183.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient183.setColorAt(0, QColor(238, 238, 238, 255))
        gradient183.setColorAt(1, QColor(190, 190, 190, 255))
        brush208 = QBrush(gradient183)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush208)
        palette42.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette42.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette42.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient184 = QLinearGradient(0, 0, 1, 0)
        gradient184.setSpread(QGradient.PadSpread)
        gradient184.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient184.setColorAt(0, QColor(238, 238, 238, 255))
        gradient184.setColorAt(1, QColor(190, 190, 190, 255))
        brush209 = QBrush(gradient184)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush209)
        gradient185 = QLinearGradient(0, 0, 1, 0)
        gradient185.setSpread(QGradient.PadSpread)
        gradient185.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient185.setColorAt(0, QColor(238, 238, 238, 255))
        gradient185.setColorAt(1, QColor(190, 190, 190, 255))
        brush210 = QBrush(gradient185)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush210)
        palette42.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient186 = QLinearGradient(0, 0, 1, 0)
        gradient186.setSpread(QGradient.PadSpread)
        gradient186.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient186.setColorAt(0, QColor(238, 238, 238, 255))
        gradient186.setColorAt(1, QColor(190, 190, 190, 255))
        brush211 = QBrush(gradient186)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush211)
        palette42.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette42.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette42.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient187 = QLinearGradient(0, 0, 1, 0)
        gradient187.setSpread(QGradient.PadSpread)
        gradient187.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient187.setColorAt(0, QColor(238, 238, 238, 255))
        gradient187.setColorAt(1, QColor(190, 190, 190, 255))
        brush212 = QBrush(gradient187)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush212)
        gradient188 = QLinearGradient(0, 0, 1, 0)
        gradient188.setSpread(QGradient.PadSpread)
        gradient188.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient188.setColorAt(0, QColor(238, 238, 238, 255))
        gradient188.setColorAt(1, QColor(190, 190, 190, 255))
        brush213 = QBrush(gradient188)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush213)
        palette42.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_consents.setPalette(palette42)
        self.checkBox_doc_consents.setFont(font3)
        self.checkBox_doc_consents.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_consents, 3, 2, 1, 1)

        self.checkBox_doc_ICF = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_ICF.setObjectName(u"checkBox_doc_ICF")
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient189 = QLinearGradient(0, 0, 1, 0)
        gradient189.setSpread(QGradient.PadSpread)
        gradient189.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient189.setColorAt(0, QColor(238, 238, 238, 255))
        gradient189.setColorAt(1, QColor(190, 190, 190, 255))
        brush214 = QBrush(gradient189)
        palette43.setBrush(QPalette.Active, QPalette.Button, brush214)
        palette43.setBrush(QPalette.Active, QPalette.Light, brush)
        palette43.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette43.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette43.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient190 = QLinearGradient(0, 0, 1, 0)
        gradient190.setSpread(QGradient.PadSpread)
        gradient190.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient190.setColorAt(0, QColor(238, 238, 238, 255))
        gradient190.setColorAt(1, QColor(190, 190, 190, 255))
        brush215 = QBrush(gradient190)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush215)
        gradient191 = QLinearGradient(0, 0, 1, 0)
        gradient191.setSpread(QGradient.PadSpread)
        gradient191.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient191.setColorAt(0, QColor(238, 238, 238, 255))
        gradient191.setColorAt(1, QColor(190, 190, 190, 255))
        brush216 = QBrush(gradient191)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush216)
        palette43.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient192 = QLinearGradient(0, 0, 1, 0)
        gradient192.setSpread(QGradient.PadSpread)
        gradient192.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient192.setColorAt(0, QColor(238, 238, 238, 255))
        gradient192.setColorAt(1, QColor(190, 190, 190, 255))
        brush217 = QBrush(gradient192)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush217)
        palette43.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette43.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette43.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient193 = QLinearGradient(0, 0, 1, 0)
        gradient193.setSpread(QGradient.PadSpread)
        gradient193.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient193.setColorAt(0, QColor(238, 238, 238, 255))
        gradient193.setColorAt(1, QColor(190, 190, 190, 255))
        brush218 = QBrush(gradient193)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush218)
        gradient194 = QLinearGradient(0, 0, 1, 0)
        gradient194.setSpread(QGradient.PadSpread)
        gradient194.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient194.setColorAt(0, QColor(238, 238, 238, 255))
        gradient194.setColorAt(1, QColor(190, 190, 190, 255))
        brush219 = QBrush(gradient194)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush219)
        palette43.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient195 = QLinearGradient(0, 0, 1, 0)
        gradient195.setSpread(QGradient.PadSpread)
        gradient195.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient195.setColorAt(0, QColor(238, 238, 238, 255))
        gradient195.setColorAt(1, QColor(190, 190, 190, 255))
        brush220 = QBrush(gradient195)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush220)
        palette43.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette43.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette43.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient196 = QLinearGradient(0, 0, 1, 0)
        gradient196.setSpread(QGradient.PadSpread)
        gradient196.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient196.setColorAt(0, QColor(238, 238, 238, 255))
        gradient196.setColorAt(1, QColor(190, 190, 190, 255))
        brush221 = QBrush(gradient196)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush221)
        gradient197 = QLinearGradient(0, 0, 1, 0)
        gradient197.setSpread(QGradient.PadSpread)
        gradient197.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient197.setColorAt(0, QColor(238, 238, 238, 255))
        gradient197.setColorAt(1, QColor(190, 190, 190, 255))
        brush222 = QBrush(gradient197)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush222)
        palette43.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_ICF.setPalette(palette43)
        self.checkBox_doc_ICF.setFont(font3)
        self.checkBox_doc_ICF.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_ICF, 10, 1, 1, 1)

        self.checkBox_doc_consultation = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_consultation.setObjectName(u"checkBox_doc_consultation")
        self.checkBox_doc_consultation.setEnabled(False)
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient198 = QLinearGradient(0, 0, 1, 0)
        gradient198.setSpread(QGradient.PadSpread)
        gradient198.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient198.setColorAt(0, QColor(238, 238, 238, 255))
        gradient198.setColorAt(1, QColor(190, 190, 190, 255))
        brush223 = QBrush(gradient198)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush223)
        palette44.setBrush(QPalette.Active, QPalette.Light, brush)
        palette44.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette44.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette44.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient199 = QLinearGradient(0, 0, 1, 0)
        gradient199.setSpread(QGradient.PadSpread)
        gradient199.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient199.setColorAt(0, QColor(238, 238, 238, 255))
        gradient199.setColorAt(1, QColor(190, 190, 190, 255))
        brush224 = QBrush(gradient199)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush224)
        gradient200 = QLinearGradient(0, 0, 1, 0)
        gradient200.setSpread(QGradient.PadSpread)
        gradient200.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient200.setColorAt(0, QColor(238, 238, 238, 255))
        gradient200.setColorAt(1, QColor(190, 190, 190, 255))
        brush225 = QBrush(gradient200)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush225)
        palette44.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient201 = QLinearGradient(0, 0, 1, 0)
        gradient201.setSpread(QGradient.PadSpread)
        gradient201.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient201.setColorAt(0, QColor(238, 238, 238, 255))
        gradient201.setColorAt(1, QColor(190, 190, 190, 255))
        brush226 = QBrush(gradient201)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush226)
        palette44.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette44.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette44.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient202 = QLinearGradient(0, 0, 1, 0)
        gradient202.setSpread(QGradient.PadSpread)
        gradient202.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient202.setColorAt(0, QColor(238, 238, 238, 255))
        gradient202.setColorAt(1, QColor(190, 190, 190, 255))
        brush227 = QBrush(gradient202)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush227)
        gradient203 = QLinearGradient(0, 0, 1, 0)
        gradient203.setSpread(QGradient.PadSpread)
        gradient203.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient203.setColorAt(0, QColor(238, 238, 238, 255))
        gradient203.setColorAt(1, QColor(190, 190, 190, 255))
        brush228 = QBrush(gradient203)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush228)
        palette44.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient204 = QLinearGradient(0, 0, 1, 0)
        gradient204.setSpread(QGradient.PadSpread)
        gradient204.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient204.setColorAt(0, QColor(238, 238, 238, 255))
        gradient204.setColorAt(1, QColor(190, 190, 190, 255))
        brush229 = QBrush(gradient204)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush229)
        palette44.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette44.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette44.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient205 = QLinearGradient(0, 0, 1, 0)
        gradient205.setSpread(QGradient.PadSpread)
        gradient205.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient205.setColorAt(0, QColor(238, 238, 238, 255))
        gradient205.setColorAt(1, QColor(190, 190, 190, 255))
        brush230 = QBrush(gradient205)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush230)
        gradient206 = QLinearGradient(0, 0, 1, 0)
        gradient206.setSpread(QGradient.PadSpread)
        gradient206.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient206.setColorAt(0, QColor(238, 238, 238, 255))
        gradient206.setColorAt(1, QColor(190, 190, 190, 255))
        brush231 = QBrush(gradient206)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush231)
        palette44.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_consultation.setPalette(palette44)
        self.checkBox_doc_consultation.setFont(font3)
        self.checkBox_doc_consultation.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_consultation, 18, 1, 1, 2)

        self.pushButtonCreateDocument = QPushButton(self.frame_creating_docs)
        self.pushButtonCreateDocument.setObjectName(u"pushButtonCreateDocument")
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette45.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush)
        palette45.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette45.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette45.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette45.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette45.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette45.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette45.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette45.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette45.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette45.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette45.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette45.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette45.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette45.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette45.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette45.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonCreateDocument.setPalette(palette45)
        self.pushButtonCreateDocument.setFont(font1)
        self.pushButtonCreateDocument.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icon/icons/note_add_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCreateDocument.setIcon(icon19)
        self.pushButtonCreateDocument.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.pushButtonCreateDocument, 20, 1, 1, 3)

        self.checkBox_doc_refusal = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_refusal.setObjectName(u"checkBox_doc_refusal")
        self.checkBox_doc_refusal.setEnabled(True)
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient207 = QLinearGradient(0, 0, 1, 0)
        gradient207.setSpread(QGradient.PadSpread)
        gradient207.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient207.setColorAt(0, QColor(238, 238, 238, 255))
        gradient207.setColorAt(1, QColor(190, 190, 190, 255))
        brush232 = QBrush(gradient207)
        palette46.setBrush(QPalette.Active, QPalette.Button, brush232)
        palette46.setBrush(QPalette.Active, QPalette.Light, brush)
        palette46.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette46.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette46.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette46.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette46.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient208 = QLinearGradient(0, 0, 1, 0)
        gradient208.setSpread(QGradient.PadSpread)
        gradient208.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient208.setColorAt(0, QColor(238, 238, 238, 255))
        gradient208.setColorAt(1, QColor(190, 190, 190, 255))
        brush233 = QBrush(gradient208)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush233)
        gradient209 = QLinearGradient(0, 0, 1, 0)
        gradient209.setSpread(QGradient.PadSpread)
        gradient209.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient209.setColorAt(0, QColor(238, 238, 238, 255))
        gradient209.setColorAt(1, QColor(190, 190, 190, 255))
        brush234 = QBrush(gradient209)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush234)
        palette46.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient210 = QLinearGradient(0, 0, 1, 0)
        gradient210.setSpread(QGradient.PadSpread)
        gradient210.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient210.setColorAt(0, QColor(238, 238, 238, 255))
        gradient210.setColorAt(1, QColor(190, 190, 190, 255))
        brush235 = QBrush(gradient210)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush235)
        palette46.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette46.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette46.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette46.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette46.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient211 = QLinearGradient(0, 0, 1, 0)
        gradient211.setSpread(QGradient.PadSpread)
        gradient211.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient211.setColorAt(0, QColor(238, 238, 238, 255))
        gradient211.setColorAt(1, QColor(190, 190, 190, 255))
        brush236 = QBrush(gradient211)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush236)
        gradient212 = QLinearGradient(0, 0, 1, 0)
        gradient212.setSpread(QGradient.PadSpread)
        gradient212.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient212.setColorAt(0, QColor(238, 238, 238, 255))
        gradient212.setColorAt(1, QColor(190, 190, 190, 255))
        brush237 = QBrush(gradient212)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush237)
        palette46.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette46.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient213 = QLinearGradient(0, 0, 1, 0)
        gradient213.setSpread(QGradient.PadSpread)
        gradient213.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient213.setColorAt(0, QColor(238, 238, 238, 255))
        gradient213.setColorAt(1, QColor(190, 190, 190, 255))
        brush238 = QBrush(gradient213)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush238)
        palette46.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette46.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette46.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette46.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette46.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient214 = QLinearGradient(0, 0, 1, 0)
        gradient214.setSpread(QGradient.PadSpread)
        gradient214.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient214.setColorAt(0, QColor(238, 238, 238, 255))
        gradient214.setColorAt(1, QColor(190, 190, 190, 255))
        brush239 = QBrush(gradient214)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush239)
        gradient215 = QLinearGradient(0, 0, 1, 0)
        gradient215.setSpread(QGradient.PadSpread)
        gradient215.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient215.setColorAt(0, QColor(238, 238, 238, 255))
        gradient215.setColorAt(1, QColor(190, 190, 190, 255))
        brush240 = QBrush(gradient215)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush240)
        palette46.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_refusal.setPalette(palette46)
        self.checkBox_doc_refusal.setFont(font3)
        self.checkBox_doc_refusal.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_refusal, 19, 3, 1, 1)

        self.checkBox_doc_statistic_talon_other = QCheckBox(self.frame_creating_docs)
        self.checkBox_doc_statistic_talon_other.setObjectName(u"checkBox_doc_statistic_talon_other")
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient216 = QLinearGradient(0, 0, 1, 0)
        gradient216.setSpread(QGradient.PadSpread)
        gradient216.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient216.setColorAt(0, QColor(238, 238, 238, 255))
        gradient216.setColorAt(1, QColor(190, 190, 190, 255))
        brush241 = QBrush(gradient216)
        palette47.setBrush(QPalette.Active, QPalette.Button, brush241)
        palette47.setBrush(QPalette.Active, QPalette.Light, brush)
        palette47.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette47.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette47.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette47.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient217 = QLinearGradient(0, 0, 1, 0)
        gradient217.setSpread(QGradient.PadSpread)
        gradient217.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient217.setColorAt(0, QColor(238, 238, 238, 255))
        gradient217.setColorAt(1, QColor(190, 190, 190, 255))
        brush242 = QBrush(gradient217)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush242)
        gradient218 = QLinearGradient(0, 0, 1, 0)
        gradient218.setSpread(QGradient.PadSpread)
        gradient218.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient218.setColorAt(0, QColor(238, 238, 238, 255))
        gradient218.setColorAt(1, QColor(190, 190, 190, 255))
        brush243 = QBrush(gradient218)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush243)
        palette47.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient219 = QLinearGradient(0, 0, 1, 0)
        gradient219.setSpread(QGradient.PadSpread)
        gradient219.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient219.setColorAt(0, QColor(238, 238, 238, 255))
        gradient219.setColorAt(1, QColor(190, 190, 190, 255))
        brush244 = QBrush(gradient219)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush244)
        palette47.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette47.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette47.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette47.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient220 = QLinearGradient(0, 0, 1, 0)
        gradient220.setSpread(QGradient.PadSpread)
        gradient220.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient220.setColorAt(0, QColor(238, 238, 238, 255))
        gradient220.setColorAt(1, QColor(190, 190, 190, 255))
        brush245 = QBrush(gradient220)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush245)
        gradient221 = QLinearGradient(0, 0, 1, 0)
        gradient221.setSpread(QGradient.PadSpread)
        gradient221.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient221.setColorAt(0, QColor(238, 238, 238, 255))
        gradient221.setColorAt(1, QColor(190, 190, 190, 255))
        brush246 = QBrush(gradient221)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush246)
        palette47.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush28)
        gradient222 = QLinearGradient(0, 0, 1, 0)
        gradient222.setSpread(QGradient.PadSpread)
        gradient222.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient222.setColorAt(0, QColor(238, 238, 238, 255))
        gradient222.setColorAt(1, QColor(190, 190, 190, 255))
        brush247 = QBrush(gradient222)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush247)
        palette47.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette47.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette47.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush28)
        palette47.setBrush(QPalette.Disabled, QPalette.ButtonText, brush28)
        gradient223 = QLinearGradient(0, 0, 1, 0)
        gradient223.setSpread(QGradient.PadSpread)
        gradient223.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient223.setColorAt(0, QColor(238, 238, 238, 255))
        gradient223.setColorAt(1, QColor(190, 190, 190, 255))
        brush248 = QBrush(gradient223)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush248)
        gradient224 = QLinearGradient(0, 0, 1, 0)
        gradient224.setSpread(QGradient.PadSpread)
        gradient224.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient224.setColorAt(0, QColor(238, 238, 238, 255))
        gradient224.setColorAt(1, QColor(190, 190, 190, 255))
        brush249 = QBrush(gradient224)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush249)
        palette47.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_doc_statistic_talon_other.setPalette(palette47)
        self.checkBox_doc_statistic_talon_other.setFont(font3)
        self.checkBox_doc_statistic_talon_other.setStyleSheet(u"QCheckBox {\n"
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
"   color: #9B9B9B;\n"
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
"	border-color: #9B9B9B;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_doc_statistic_talon_other, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer, 15, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_creating_docs, 0, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 1, 1, 1, 1)

        self.frame_created_docs = QFrame(self.Page_creating_docs)
        self.frame_created_docs.setObjectName(u"frame_created_docs")
        self.frame_created_docs.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_5 = QGridLayout(self.frame_created_docs)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.textBrowser = QTextBrowser(self.frame_created_docs)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(450, 0))
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        font8.setPointSize(10)
        font8.setBold(True)
        self.textBrowser.setFont(font8)
        self.textBrowser.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"")

        self.gridLayout_5.addWidget(self.textBrowser, 1, 1, 1, 1)

        self.pushButtonOpenFolder = QPushButton(self.frame_created_docs)
        self.pushButtonOpenFolder.setObjectName(u"pushButtonOpenFolder")
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette48.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette48.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush)
        palette48.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette48.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette48.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette48.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette48.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette48.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette48.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette48.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette48.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette48.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette48.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette48.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette48.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette48.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette48.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette48.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette48.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenFolder.setPalette(palette48)
        self.pushButtonOpenFolder.setFont(font1)
        self.pushButtonOpenFolder.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon20 = QIcon()
        icon20.addFile(u":/icon/icons/folder_open_FILL1_wght400_GRAD0_opsz48_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenFolder.setIcon(icon20)
        self.pushButtonOpenFolder.setIconSize(QSize(32, 32))

        self.gridLayout_5.addWidget(self.pushButtonOpenFolder, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.label_status_2 = QLabel(self.frame_created_docs)
        self.label_status_2.setObjectName(u"label_status_2")
        self.label_status_2.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamilies([u"Roboto"])
        font9.setPointSize(16)
        font9.setBold(True)
        self.label_status_2.setFont(font9)
        self.label_status_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")

        self.gridLayout_5.addWidget(self.label_status_2, 0, 0, 1, 3)


        self.gridLayout_6.addWidget(self.frame_created_docs, 2, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        icon21 = QIcon()
        icon21.addFile(u":/icon/icons/print_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabPtCard.addTab(self.Page_creating_docs, icon21, "")

        self.verticalLayout_6.addWidget(self.tabPtCard)

        self.frame_6 = QFrame(self.center)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: White;\n"
"font-size: 10pt;")
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.label_status = QLabel(self.frame_6)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMaximumSize(QSize(16777215, 30))
        self.label_status.setFont(font)
        self.label_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_status)

        self.pushButtonOpenLogs = QPushButton(self.frame_6)
        self.pushButtonOpenLogs.setObjectName(u"pushButtonOpenLogs")
        self.pushButtonOpenLogs.setMaximumSize(QSize(50, 30))
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette49.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette49.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush)
        palette49.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette49.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette49.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette49.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette49.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette49.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette49.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette49.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette49.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette49.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette49.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette49.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette49.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette49.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette49.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette49.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenLogs.setPalette(palette49)
        font10 = QFont()
        font10.setFamilies([u"Roboto"])
        font10.setPointSize(14)
        font10.setBold(False)
        self.pushButtonOpenLogs.setFont(font10)
        self.pushButtonOpenLogs.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 14pt;\n"
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

        self.horizontalLayout.addWidget(self.pushButtonOpenLogs)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.center)

        self.frame_right = QFrame(self.main)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_7 = QVBoxLayout(self.frame_right)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 20, 5, 5)
        self.label_dis_check = QLabel(self.frame_right)
        self.label_dis_check.setObjectName(u"label_dis_check")
        self.label_dis_check.setFont(font1)
        self.label_dis_check.setStyleSheet(u"color: White;\n"
"font-size: 11pt;")
        self.label_dis_check.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_dis_check)

        self.pushButtonHelp = QPushButton(self.frame_right)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        self.pushButtonHelp.setEnabled(False)
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette50.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette50.setBrush(QPalette.Active, QPalette.Light, brush)
        palette50.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette50.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette50.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush)
        palette50.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette50.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette50.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette50.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
        palette50.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette50.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette50.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette50.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette50.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette50.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette50.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
        palette50.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette50.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette50.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette50.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette50.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette50.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette50.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette50.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette50.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
        palette50.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette50.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButtonHelp.setPalette(palette50)
        self.pushButtonHelp.setFont(font1)
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
        icon22 = QIcon()
        icon22.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHelp.setIcon(icon22)

        self.verticalLayout_7.addWidget(self.pushButtonHelp)

        self.pushButton_2 = QPushButton(self.frame_right)
        self.pushButton_2.setObjectName(u"pushButton_2")
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette51.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Active, QPalette.Text, brush)
        palette51.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette51.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette51.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette51.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette51.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette51.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette51.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette51.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette51.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette51.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette51.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette51.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette51.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette51.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette51.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette51.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette51.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButton_2.setPalette(palette51)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
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
"}")

        self.verticalLayout_7.addWidget(self.pushButton_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.checkBox_not_save = QCheckBox(self.frame_right)
        self.checkBox_not_save.setObjectName(u"checkBox_not_save")
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        gradient225 = QLinearGradient(0, 0, 1, 0)
        gradient225.setSpread(QGradient.PadSpread)
        gradient225.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient225.setColorAt(0, QColor(238, 238, 238, 255))
        gradient225.setColorAt(1, QColor(190, 190, 190, 255))
        brush250 = QBrush(gradient225)
        palette52.setBrush(QPalette.Active, QPalette.Button, brush250)
        palette52.setBrush(QPalette.Active, QPalette.Light, brush)
        palette52.setBrush(QPalette.Active, QPalette.Midlight, brush19)
        palette52.setBrush(QPalette.Active, QPalette.Dark, brush20)
        palette52.setBrush(QPalette.Active, QPalette.Mid, brush21)
        palette52.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette52.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        gradient226 = QLinearGradient(0, 0, 1, 0)
        gradient226.setSpread(QGradient.PadSpread)
        gradient226.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient226.setColorAt(0, QColor(238, 238, 238, 255))
        gradient226.setColorAt(1, QColor(190, 190, 190, 255))
        brush251 = QBrush(gradient226)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush251)
        gradient227 = QLinearGradient(0, 0, 1, 0)
        gradient227.setSpread(QGradient.PadSpread)
        gradient227.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient227.setColorAt(0, QColor(238, 238, 238, 255))
        gradient227.setColorAt(1, QColor(190, 190, 190, 255))
        brush252 = QBrush(gradient227)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush252)
        palette52.setBrush(QPalette.Active, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        gradient228 = QLinearGradient(0, 0, 1, 0)
        gradient228.setSpread(QGradient.PadSpread)
        gradient228.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient228.setColorAt(0, QColor(238, 238, 238, 255))
        gradient228.setColorAt(1, QColor(190, 190, 190, 255))
        brush253 = QBrush(gradient228)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush253)
        palette52.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Midlight, brush19)
        palette52.setBrush(QPalette.Inactive, QPalette.Dark, brush20)
        palette52.setBrush(QPalette.Inactive, QPalette.Mid, brush21)
        palette52.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette52.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        gradient229 = QLinearGradient(0, 0, 1, 0)
        gradient229.setSpread(QGradient.PadSpread)
        gradient229.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient229.setColorAt(0, QColor(238, 238, 238, 255))
        gradient229.setColorAt(1, QColor(190, 190, 190, 255))
        brush254 = QBrush(gradient229)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush254)
        gradient230 = QLinearGradient(0, 0, 1, 0)
        gradient230.setSpread(QGradient.PadSpread)
        gradient230.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient230.setColorAt(0, QColor(238, 238, 238, 255))
        gradient230.setColorAt(1, QColor(190, 190, 190, 255))
        brush255 = QBrush(gradient230)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush255)
        palette52.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette52.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        gradient231 = QLinearGradient(0, 0, 1, 0)
        gradient231.setSpread(QGradient.PadSpread)
        gradient231.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient231.setColorAt(0, QColor(238, 238, 238, 255))
        gradient231.setColorAt(1, QColor(190, 190, 190, 255))
        brush256 = QBrush(gradient231)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush256)
        palette52.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Midlight, brush19)
        palette52.setBrush(QPalette.Disabled, QPalette.Dark, brush20)
        palette52.setBrush(QPalette.Disabled, QPalette.Mid, brush21)
        palette52.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette52.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        gradient232 = QLinearGradient(0, 0, 1, 0)
        gradient232.setSpread(QGradient.PadSpread)
        gradient232.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient232.setColorAt(0, QColor(238, 238, 238, 255))
        gradient232.setColorAt(1, QColor(190, 190, 190, 255))
        brush257 = QBrush(gradient232)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush257)
        gradient233 = QLinearGradient(0, 0, 1, 0)
        gradient233.setSpread(QGradient.PadSpread)
        gradient233.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient233.setColorAt(0, QColor(238, 238, 238, 255))
        gradient233.setColorAt(1, QColor(190, 190, 190, 255))
        brush258 = QBrush(gradient233)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush258)
        palette52.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.checkBox_not_save.setPalette(palette52)
        font11 = QFont()
        font11.setFamilies([u"Roboto"])
        font11.setPointSize(9)
        font11.setBold(False)
        font11.setItalic(False)
        self.checkBox_not_save.setFont(font11)
        self.checkBox_not_save.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_7.addWidget(self.checkBox_not_save)

        self.pushButtonNotSaveExit = QPushButton(self.frame_right)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        self.pushButtonNotSaveExit.setEnabled(False)
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette53.setBrush(QPalette.Active, QPalette.Light, brush)
        brush259 = QBrush(QColor(237, 237, 237, 255))
        brush259.setStyle(Qt.SolidPattern)
        palette53.setBrush(QPalette.Active, QPalette.Midlight, brush259)
        brush260 = QBrush(QColor(110, 110, 110, 255))
        brush260.setStyle(Qt.SolidPattern)
        palette53.setBrush(QPalette.Active, QPalette.Dark, brush260)
        brush261 = QBrush(QColor(147, 147, 147, 255))
        brush261.setStyle(Qt.SolidPattern)
        palette53.setBrush(QPalette.Active, QPalette.Mid, brush261)
        palette53.setBrush(QPalette.Active, QPalette.Text, brush)
        palette53.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette53.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette53.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette53.setBrush(QPalette.Active, QPalette.AlternateBase, brush259)
        palette53.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette53.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette53.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette53.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Midlight, brush259)
        palette53.setBrush(QPalette.Inactive, QPalette.Dark, brush260)
        palette53.setBrush(QPalette.Inactive, QPalette.Mid, brush261)
        palette53.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette53.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette53.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush259)
        palette53.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette53.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette53.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette53.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Midlight, brush259)
        palette53.setBrush(QPalette.Disabled, QPalette.Dark, brush260)
        palette53.setBrush(QPalette.Disabled, QPalette.Mid, brush261)
        palette53.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette53.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette53.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush262 = QBrush(QColor(220, 220, 220, 255))
        brush262.setStyle(Qt.SolidPattern)
        palette53.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush262)
        palette53.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette53.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButtonNotSaveExit.setPalette(palette53)
        font12 = QFont()
        font12.setFamilies([u"Roboto"])
        font12.setPointSize(12)
        font12.setBold(False)
        self.pushButtonNotSaveExit.setFont(font12)
        self.pushButtonNotSaveExit.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
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
        icon23 = QIcon()
        icon23.addFile(u":/icon/icons/west_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon23)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSave = QPushButton(self.frame_right)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette54.setBrush(QPalette.Active, QPalette.Light, brush)
        palette54.setBrush(QPalette.Active, QPalette.Midlight, brush259)
        palette54.setBrush(QPalette.Active, QPalette.Dark, brush260)
        palette54.setBrush(QPalette.Active, QPalette.Mid, brush261)
        palette54.setBrush(QPalette.Active, QPalette.Text, brush)
        palette54.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette54.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette54.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette54.setBrush(QPalette.Active, QPalette.AlternateBase, brush259)
        palette54.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette54.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette54.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Midlight, brush259)
        palette54.setBrush(QPalette.Inactive, QPalette.Dark, brush260)
        palette54.setBrush(QPalette.Inactive, QPalette.Mid, brush261)
        palette54.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette54.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette54.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush259)
        palette54.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette54.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette54.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette54.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Midlight, brush259)
        palette54.setBrush(QPalette.Disabled, QPalette.Dark, brush260)
        palette54.setBrush(QPalette.Disabled, QPalette.Mid, brush261)
        palette54.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette54.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette54.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette54.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush262)
        palette54.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette54.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButtonSave.setPalette(palette54)
        self.pushButtonSave.setFont(font12)
        self.pushButtonSave.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
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
        self.pushButtonSave.setIcon(icon16)
        self.pushButtonSave.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.pushButtonSave)

        self.pushButtonSaveExit = QPushButton(self.frame_right)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush263 = QBrush(QColor(92, 158, 173, 255))
        brush263.setStyle(Qt.SolidPattern)
        palette55.setBrush(QPalette.Active, QPalette.Button, brush263)
        palette55.setBrush(QPalette.Active, QPalette.Light, brush)
        palette55.setBrush(QPalette.Active, QPalette.Midlight, brush259)
        palette55.setBrush(QPalette.Active, QPalette.Dark, brush260)
        palette55.setBrush(QPalette.Active, QPalette.Mid, brush261)
        palette55.setBrush(QPalette.Active, QPalette.Text, brush)
        palette55.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush263)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush263)
        palette55.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette55.setBrush(QPalette.Active, QPalette.AlternateBase, brush259)
        palette55.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette55.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush263)
        palette55.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Midlight, brush259)
        palette55.setBrush(QPalette.Inactive, QPalette.Dark, brush260)
        palette55.setBrush(QPalette.Inactive, QPalette.Mid, brush261)
        palette55.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush263)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush263)
        palette55.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette55.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush259)
        palette55.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette55.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette55.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette55.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Midlight, brush259)
        palette55.setBrush(QPalette.Disabled, QPalette.Dark, brush260)
        palette55.setBrush(QPalette.Disabled, QPalette.Mid, brush261)
        palette55.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette55.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette55.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette55.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush262)
        palette55.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette55.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButtonSaveExit.setPalette(palette55)
        self.pushButtonSaveExit.setFont(font12)
        self.pushButtonSaveExit.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"font-size: 12pt;\n"
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
        icon24 = QIcon()
        icon24.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveExit.setIcon(icon24)
        self.pushButtonSaveExit.setIconSize(QSize(36, 36))

        self.verticalLayout_7.addWidget(self.pushButtonSaveExit)


        self.horizontalLayout_2.addWidget(self.frame_right)


        self.verticalLayout_3.addWidget(self.main)


        self.retranslateUi(omr_patient_card)

        self.tabPtCard.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(omr_patient_card)
    # setupUi

    def retranslateUi(self, omr_patient_card):
        omr_patient_card.setWindowTitle(QCoreApplication.translate("omr_patient_card", u"Form", None))
        self.label_status_4.setText("")
        self.label_status_3.setText(QCoreApplication.translate("omr_patient_card", u"UIN", None))
        self.label_unic_number.setText("")
        self.ptFullNameCard.setText(QCoreApplication.translate("omr_patient_card", u"< \u0418\u043c\u044f \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430>\n"
"< \u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f > // < \u0412\u043e\u0437\u0440\u0430\u0441\u0442 > \n"
"< \u0414\u0435\u043d\u044c \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f > --- < \u041a\u043e\u0439\u043a\u043e\u0434\u043d\u0438 > \u043a/\u0434", None))
        self.label_type_hospitalisation.setText(QCoreApplication.translate("omr_patient_card", u"< \u0422\u0438\u043f \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 >", None))
        self.label_LN.setText(QCoreApplication.translate("omr_patient_card", u"<\u041b\u041d>", None))
        self.label_b20.setText(QCoreApplication.translate("omr_patient_card", u"<html><head/><body><p/></body></html>", None))
        self.label_hvc.setText(QCoreApplication.translate("omr_patient_card", u"<html><head/><body><p/></body></html>", None))
        self.label_diabet.setText(QCoreApplication.translate("omr_patient_card", u"<html><head/><body><p/></body></html>", None))
        self.label_adm_data.setText(QCoreApplication.translate("omr_patient_card", u" \u041f\u0440\u0438 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0438:", None))
        self.pushButtonOpenPtPassportData.setText(QCoreApplication.translate("omr_patient_card", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonOpenPtObjStatusAdm.setText(QCoreApplication.translate("omr_patient_card", u"\u0416\u0430\u043b\u043e\u0431\u044b, \u0430\u043d\u0430\u043c\u043d\u0435\u0437 \u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.pushButtonOpenPtNeuralStatusAdm.setText(QCoreApplication.translate("omr_patient_card", u"\u041d\u0435\u0432\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.pushButtonOpenPtDiagnosisAdm.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437 \u0438 \u0448\u043a\u0430\u043b\u044b", None))
        self.pushButtonOpen_icf.setText(QCoreApplication.translate("omr_patient_card", u"\u0420\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0434\u0438\u0430\u0433\u043d\u043e\u0437 \u043f\u043e \u041c\u041a\u0424", None))
        self.pushButtonOpenPtAppointments.setText(QCoreApplication.translate("omr_patient_card", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.pushButtonOpen_mdrk.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u043b\u044f \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b\u0430 \u041c\u0414\u0420\u041a", None))
        self.label_instr_data.setText(QCoreApplication.translate("omr_patient_card", u" \u0414\u0430\u043d\u043d\u044b\u0435 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0439:", None))
        self.pushButtonOpenPtLaboratoryData.setText(QCoreApplication.translate("omr_patient_card", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonOpenPtInstrumentalData.setText(QCoreApplication.translate("omr_patient_card", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonOpenPtConsultationData.setText(QCoreApplication.translate("omr_patient_card", u"\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432", None))
        self.label_dis_data.setText(QCoreApplication.translate("omr_patient_card", u" \u041f\u0440\u0438 \u0432\u044b\u043f\u0438\u0441\u043a\u0435:", None))
        self.pushButtonOpenPtObjStatusDischarge.setText(QCoreApplication.translate("omr_patient_card", u"\u041e\u0431\u044a\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.pushButtonOpenPtNeuralStatusDischarge.setText(QCoreApplication.translate("omr_patient_card", u"\u041d\u0435\u0432\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.pushButtonOpenPtDiagnosisDischarge.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437 \u0438 \u0448\u043a\u0430\u043b\u044b", None))
        self.pushButtonOpen_dynamic.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u0438\u043d\u0430\u043c\u0438\u043a\u0430", None))
        self.pushButtonOpenPtStatisticData.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u0438\u0441\u043a\u0438, \u043a\u043e\u0434\u044b, \u0443\u0441\u043b\u0443\u0433\u0438 \u0438 \u0442.\u0434.", None))
        self.pushButtonOpenPtDischargeRecommend.setText(QCoreApplication.translate("omr_patient_card", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438 \u043f\u0440\u0438 \u0432\u044b\u043f\u0438\u0441\u043a\u0435", None))
        ___qtablewidgetitem = self.tableWidget_dynamic.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("omr_patient_card", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget_dynamic.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget_dynamic.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u0438\u043d\u0430\u043c\u0438\u043a\u0430", None));
        self.pushButtonAddEvent.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u043e\u0435", None))
        self.label_events.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.label_sorry.setText(QCoreApplication.translate("omr_patient_card", u"\u0420\u0430\u0437\u0434\u0435\u043b \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0432 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435\n"
"\u043f\u0440\u0438\u043d\u043e\u0441\u0438\u043c \u0438\u0437\u0432\u0438\u043d\u0435\u043d\u0438\u044f \u0437\u0430 \u043d\u0435\u0443\u0434\u043e\u0431\u0441\u0442\u0432\u0430", None))
        self.tabPtCard.setTabText(self.tabPtCard.indexOf(self.Page_events), QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.label_diaries_2.setText(QCoreApplication.translate("omr_patient_card", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0434\u043d\u0435\u0432\u043d\u0438\u043a\u0430", None))
        self.radioButton_everyday.setText(QCoreApplication.translate("omr_patient_card", u"\u0415\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e", None))
        self.radioButton_3_times_in_week.setText(QCoreApplication.translate("omr_patient_card", u"3 \u0440\u0430\u0437\u0430 \u0432 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.radioButton_twice_in_day.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u0432\u0430\u0436\u0434\u044b \u0432 \u0441\u0443\u0442\u043a\u0438", None))
        self.pushButton_create_diaries.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0434\u043d\u0435\u0432\u043d\u0438\u043a\u0438", None))
        ___qtablewidgetitem3 = self.tableWidget_diaries.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("omr_patient_card", u"\u0417\u0430\u043f\u0438\u0441\u044c", None));
        self.label_diaries.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435\n"
"\u0434\u043d\u0435\u0432\u043d\u0438\u043a\u043e\u0432\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.pushButton_save_diary.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u043d\u0435\u0432\u043d\u0438\u043a\u0430", None))
        self.pushButton_close_diary.setText(QCoreApplication.translate("omr_patient_card", u"\u0437\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label_diary_index.setText("")
        self.tabPtCard.setTabText(self.tabPtCard.indexOf(self.Page_diaries), QCoreApplication.translate("omr_patient_card", u"\u0414\u043d\u0435\u0432\u043d\u0438\u043a\u043e\u0432\u044b\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.checkBox_doc_scale.setText(QCoreApplication.translate("omr_patient_card", u"\u0428\u043a\u0430\u043b\u044b", None))
        self.checkBox_doc_additional_recommendations.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u043e\u043f. \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438", None))
        self.checkBox_doc_initial_inspection.setText(QCoreApplication.translate("omr_patient_card", u"\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0439 \u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.checkBox_doc_med_commission_1.setText(QCoreApplication.translate("omr_patient_card", u"\u0412\u041a \u043f\u043e \u043f\u0440\u043e\u0434\u043b\u0435\u043d\u0438\u044e \u041b\u041d", None))
        self.checkBox_doc_statistic_talon.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u0442\u0430\u0442.\u0442\u0430\u043b\u043e\u043d \u043e\u0431\u043e\u0440\u043e\u0442\u043d\u0430\u044f", None))
        self.checkBox_doc_med_commission_2.setText(QCoreApplication.translate("omr_patient_card", u"\u0412\u041a \u043f\u043e \u041b\u041d # 2", None))
        self.checkBox_doc_appointments.setText(QCoreApplication.translate("omr_patient_card", u"\u041b\u0438\u0441\u0442 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439", None))
        self.checkBox_doc_discharge_summary.setText(QCoreApplication.translate("omr_patient_card", u"\u0412\u044b\u043f\u0438\u0441\u043d\u043e\u0439 \u044d\u043f\u0438\u043a\u0440\u0438\u0437", None))
        self.checkBox_doc_back_frontpage.setText(QCoreApplication.translate("omr_patient_card", u"\u041e\u0431\u043e\u0440\u043e\u0442 \u043e\u0431\u043b\u043e\u0436\u043a\u0438", None))
        self.checkBox_doc_complex.setText(QCoreApplication.translate("omr_patient_card", u"\u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u0432 \u043e\u0434\u043d\u043e\u043c \u0444\u0430\u0439\u043b\u0435", None))
        self.pushButton_lecalo.setText(QCoreApplication.translate("omr_patient_card", u"\u043d\u0430 \u0432\u044b\u043f\u0438\u0441\u043a\u0443", None))
        self.pushButton_clean_ticks.setText(QCoreApplication.translate("omr_patient_card", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.checkBox_doc_frontpage.setText(QCoreApplication.translate("omr_patient_card", u"\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u0438\u0441\u0442\u043e\u0440\u0438\u0438 \u0431\u043e\u043b\u0435\u0437\u043d\u0438", None))
        self.checkBox_doc_statistic_talon_face.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u0442\u0430\u0442.\u0442\u0430\u043b\u043e\u043d \u043b\u0438\u0446\u0435\u0432\u0430\u044f", None))
        self.checkBox_doc_directions.setText(QCoreApplication.translate("omr_patient_card", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.checkBox_lfk_report_sheet.setText(QCoreApplication.translate("omr_patient_card", u"\u041b\u0438\u0441\u0442 \u0443\u0447\u0435\u0442\u0430 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439", None))
        self.checkBox_doc_med_commission_drugs.setText(QCoreApplication.translate("omr_patient_card", u"\u0412\u041a \u043d\u0430 \u043b\u0435\u043a.\u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442", None))
        self.label_creating_docs.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432 (.docx)", None))
        self.checkBox_doc_final_diary.setText(QCoreApplication.translate("omr_patient_card", u"\u0418\u0442\u043e\u0433\u043e\u0432\u044b\u0439 \u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.checkBox_doc_diaries.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u043d\u0435\u0432\u043d\u0438\u043a\u0438", None))
        self.checkBox_doc_pass.setText(QCoreApplication.translate("omr_patient_card", u"\u041f\u0440\u043e\u043f\u0443\u0441\u043a \u0434\u043b\u044f \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.checkBox_doc_reference.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e \u043c\u0435\u0441\u0442\u0443 \u0442\u0440\u0435\u0431.", None))
        self.checkBox_doc_med_commission_dis.setText(QCoreApplication.translate("omr_patient_card", u"\u0412\u041a \u043f\u043e \u041b\u041d \u0434\u043b\u044f \u0432\u044b\u043f\u0438\u0441\u043a\u0438", None))
        self.checkBox_doc_full_history.setText(QCoreApplication.translate("omr_patient_card", u"\u0412\u0441\u044f \u0438\u0441\u0442\u043e\u0440\u0438\u044f \u0431\u043e\u043b\u0435\u0437\u043d\u0438 \u043e\u0434\u043d\u0438\u043c \u0444\u0430\u0439\u043b\u043e\u043c", None))
        self.checkBox_doc_consents.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0433\u043b\u0430\u0441\u0438\u044f", None))
        self.checkBox_doc_ICF.setText(QCoreApplication.translate("omr_patient_card", u"\u041c\u041a\u0424", None))
        self.checkBox_doc_consultation.setText(QCoreApplication.translate("omr_patient_card", u"\u0414\u043e\u043f. \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u043f\u0440\u0438 \u0432\u044b\u043f\u0438\u0441\u043a\u0435 \u0434\u043b\u044f \u041c\u0421\u042d", None))
        self.pushButtonCreateDocument.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b (.docx)", None))
        self.checkBox_doc_refusal.setText(QCoreApplication.translate("omr_patient_card", u"\u041e\u0442\u043a\u0430\u0437 \u043e\u0442 \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.checkBox_doc_statistic_talon_other.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u0442\u0430\u0442.\u0442\u0430\u043b\u043e\u043d \u0434\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435", None))
        self.pushButtonOpenFolder.setText(QCoreApplication.translate("omr_patient_card", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 \u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
        self.label_status_2.setText(QCoreApplication.translate("omr_patient_card", u"<html><head/><body><p align=\"center\">\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b</p></body></html>", None))
        self.tabPtCard.setTabText(self.tabPtCard.indexOf(self.Page_creating_docs), QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.label_status.setText(QCoreApplication.translate("omr_patient_card", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButtonOpenLogs.setText(QCoreApplication.translate("omr_patient_card", u"...\n"
" ", None))
        self.label_dis_check.setText(QCoreApplication.translate("omr_patient_card", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("omr_patient_card", u"Help", None))
        self.pushButton_2.setText(QCoreApplication.translate("omr_patient_card", u"print(d.keys())", None))
        self.checkBox_not_save.setText(QCoreApplication.translate("omr_patient_card", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u044e \n"
"\u043d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("omr_patient_card", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c \n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f\n"
"\u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.pushButtonSave.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("omr_patient_card", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435\n"
"\u0438 \u0437\u0430\u043a\u0440\u044b\u0442\u044c \u043a\u0430\u0440\u0442\u0443\n"
"\u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
    # retranslateUi

