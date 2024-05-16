# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bta_PatientCard.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import res_main_rc
import res_main_rc

class Ui_PatientCard(object):
    def setupUi(self, PatientCard):
        if not PatientCard.objectName():
            PatientCard.setObjectName(u"PatientCard")
        PatientCard.resize(1223, 606)
        PatientCard.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_6 = QVBoxLayout(PatientCard)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_111 = QFrame(PatientCard)
        self.frame_111.setObjectName(u"frame_111")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.patient_card_block = QFrame(self.frame_111)
        self.patient_card_block.setObjectName(u"patient_card_block")
        self.patient_card_block.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.patient_card_block)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.ptFullNameCard = QLabel(self.patient_card_block)
        self.ptFullNameCard.setObjectName(u"ptFullNameCard")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.ptFullNameCard.setFont(font)
        self.ptFullNameCard.setStyleSheet(u"background-color: rgba(50, 98, 115, 150);\n"
"color: White;\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.ptFullNameCard.setFrameShape(QFrame.NoFrame)
        self.ptFullNameCard.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.ptFullNameCard, 3, 0, 1, 2)

        self.labelCard_2 = QLabel(self.patient_card_block)
        self.labelCard_2.setObjectName(u"labelCard_2")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        self.labelCard_2.setFont(font1)
        self.labelCard_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.labelCard_2.setPixmap(QPixmap(u":/icon/icons/screencast_FILL1_wght400_GRAD0_opsz48.svg"))
        self.labelCard_2.setScaledContents(False)
        self.labelCard_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCard_2, 0, 0, 2, 1)

        self.labelCard = QLabel(self.patient_card_block)
        self.labelCard.setObjectName(u"labelCard")
        self.labelCard.setFont(font1)
        self.labelCard.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(92, 158, 173, 200);\n"
"border: none;\n"
"")
        self.labelCard.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCard, 0, 1, 2, 1)

        self.label_uin = QLabel(self.patient_card_block)
        self.label_uin.setObjectName(u"label_uin")
        self.label_uin.setMaximumSize(QSize(70, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_uin.setFont(font2)
        self.label_uin.setStyleSheet(u"color: #326273;\n"
"font-size: 11pt;\n"
"border: none;\n"
"background-color: transparent;")
        self.label_uin.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_uin, 2, 0, 1, 1)

        self.label_unic_number = QLabel(self.patient_card_block)
        self.label_unic_number.setObjectName(u"label_unic_number")
        self.label_unic_number.setFont(font2)
        self.label_unic_number.setStyleSheet(u"color: White;\n"
"font-size: 11pt;\n"
"border: none;")
        self.label_unic_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_unic_number, 2, 1, 1, 1)

        self.label_type_hospitalisation = QLabel(self.patient_card_block)
        self.label_type_hospitalisation.setObjectName(u"label_type_hospitalisation")
        self.label_type_hospitalisation.setMaximumSize(QSize(16777215, 20))
        self.label_type_hospitalisation.setFont(font)
        self.label_type_hospitalisation.setStyleSheet(u"color: #13242B;;\n"
"font-size: 11pt;\n"
"border: none;")
        self.label_type_hospitalisation.setFrameShape(QFrame.NoFrame)
        self.label_type_hospitalisation.setFrameShadow(QFrame.Plain)
        self.label_type_hospitalisation.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_type_hospitalisation, 4, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.patient_card_block)

        self.frame_pt_data = QFrame(self.frame_111)
        self.frame_pt_data.setObjectName(u"frame_pt_data")
        self.frame_pt_data.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_2 = QVBoxLayout(self.frame_pt_data)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelCard_4 = QLabel(self.frame_pt_data)
        self.labelCard_4.setObjectName(u"labelCard_4")
        self.labelCard_4.setFont(font1)
        self.labelCard_4.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(92, 158, 173, 200);\n"
"border: none;\n"
"")
        self.labelCard_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.labelCard_4)

        self.labelCard_3 = QLabel(self.frame_pt_data)
        self.labelCard_3.setObjectName(u"labelCard_3")
        self.labelCard_3.setMaximumSize(QSize(40, 16777215))
        self.labelCard_3.setFont(font1)
        self.labelCard_3.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(92, 158, 173, 200);\n"
"border: none;\n"
"")
        self.labelCard_3.setPixmap(QPixmap(u":/icon/icons/create_white_36dp.svg"))
        self.labelCard_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.labelCard_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.pushButtonOpenPtPassportData = QPushButton(self.frame_pt_data)
        self.pushButtonOpenPtPassportData.setObjectName(u"pushButtonOpenPtPassportData")
        self.pushButtonOpenPtPassportData.setMinimumSize(QSize(0, 28))
        self.pushButtonOpenPtPassportData.setMaximumSize(QSize(16777215, 28))
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
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.pushButtonOpenPtPassportData.setFont(font3)
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
        self.pushButtonOpenPtPassportData.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtPassportData)

        self.pushButtonOpenPtObjStatus = QPushButton(self.frame_pt_data)
        self.pushButtonOpenPtObjStatus.setObjectName(u"pushButtonOpenPtObjStatus")
        self.pushButtonOpenPtObjStatus.setMinimumSize(QSize(0, 28))
        self.pushButtonOpenPtObjStatus.setMaximumSize(QSize(16777215, 28))
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
        self.pushButtonOpenPtObjStatus.setPalette(palette1)
        self.pushButtonOpenPtObjStatus.setFont(font3)
        self.pushButtonOpenPtObjStatus.setStyleSheet(u"QPushButton {\n"
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
        self.pushButtonOpenPtObjStatus.setIcon(icon1)
        self.pushButtonOpenPtObjStatus.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtObjStatus)

        self.pushButtonOpenPtNeuralStatus = QPushButton(self.frame_pt_data)
        self.pushButtonOpenPtNeuralStatus.setObjectName(u"pushButtonOpenPtNeuralStatus")
        self.pushButtonOpenPtNeuralStatus.setMinimumSize(QSize(0, 28))
        self.pushButtonOpenPtNeuralStatus.setMaximumSize(QSize(16777215, 28))
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
        self.pushButtonOpenPtNeuralStatus.setPalette(palette2)
        self.pushButtonOpenPtNeuralStatus.setFont(font3)
        self.pushButtonOpenPtNeuralStatus.setStyleSheet(u"QPushButton {\n"
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
        self.pushButtonOpenPtNeuralStatus.setIcon(icon2)
        self.pushButtonOpenPtNeuralStatus.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtNeuralStatus)

        self.pushButtonOpenPtDiagnosis = QPushButton(self.frame_pt_data)
        self.pushButtonOpenPtDiagnosis.setObjectName(u"pushButtonOpenPtDiagnosis")
        self.pushButtonOpenPtDiagnosis.setMinimumSize(QSize(0, 28))
        self.pushButtonOpenPtDiagnosis.setMaximumSize(QSize(16777215, 28))
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
        self.pushButtonOpenPtDiagnosis.setPalette(palette3)
        self.pushButtonOpenPtDiagnosis.setFont(font3)
        self.pushButtonOpenPtDiagnosis.setStyleSheet(u"QPushButton {\n"
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
        self.pushButtonOpenPtDiagnosis.setIcon(icon3)
        self.pushButtonOpenPtDiagnosis.setIconSize(QSize(32, 32))
        self.pushButtonOpenPtDiagnosis.setCheckable(False)
        self.pushButtonOpenPtDiagnosis.setChecked(False)
        self.pushButtonOpenPtDiagnosis.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButtonOpenPtDiagnosis)

        self.pushButtonOpen_bta_protocol = QPushButton(self.frame_pt_data)
        self.pushButtonOpen_bta_protocol.setObjectName(u"pushButtonOpen_bta_protocol")
        self.pushButtonOpen_bta_protocol.setMinimumSize(QSize(0, 28))
        self.pushButtonOpen_bta_protocol.setMaximumSize(QSize(16777215, 28))
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
        self.pushButtonOpen_bta_protocol.setPalette(palette4)
        self.pushButtonOpen_bta_protocol.setFont(font3)
        self.pushButtonOpen_bta_protocol.setStyleSheet(u"QPushButton {\n"
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
        icon4.addFile(u":/icon/icons/vaccines_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpen_bta_protocol.setIcon(icon4)
        self.pushButtonOpen_bta_protocol.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButtonOpen_bta_protocol)

        self.pushButtonOpen_discharge_data = QPushButton(self.frame_pt_data)
        self.pushButtonOpen_discharge_data.setObjectName(u"pushButtonOpen_discharge_data")
        self.pushButtonOpen_discharge_data.setMinimumSize(QSize(0, 28))
        self.pushButtonOpen_discharge_data.setMaximumSize(QSize(16777215, 28))
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
        self.pushButtonOpen_discharge_data.setPalette(palette5)
        self.pushButtonOpen_discharge_data.setFont(font3)
        self.pushButtonOpen_discharge_data.setStyleSheet(u"QPushButton {\n"
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
        icon5.addFile(u":/icon/icons/moving_beds_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpen_discharge_data.setIcon(icon5)
        self.pushButtonOpen_discharge_data.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButtonOpen_discharge_data)

        self.pushButtonOpen_recommends = QPushButton(self.frame_pt_data)
        self.pushButtonOpen_recommends.setObjectName(u"pushButtonOpen_recommends")
        self.pushButtonOpen_recommends.setMinimumSize(QSize(0, 28))
        self.pushButtonOpen_recommends.setMaximumSize(QSize(16777215, 28))
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
        self.pushButtonOpen_recommends.setPalette(palette6)
        self.pushButtonOpen_recommends.setFont(font3)
        self.pushButtonOpen_recommends.setStyleSheet(u"QPushButton {\n"
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
        icon6.addFile(u":/icon/icons/list_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpen_recommends.setIcon(icon6)
        self.pushButtonOpen_recommends.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButtonOpen_recommends)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.frame_pt_data)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.creacting_docs = QFrame(self.frame_111)
        self.creacting_docs.setObjectName(u"creacting_docs")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        self.creacting_docs.setFont(font4)
        self.creacting_docs.setStyleSheet(u"font-size: 12pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_4 = QGridLayout(self.creacting_docs)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(1)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.checkBox_doc_consent_bta = QCheckBox(self.creacting_docs)
        self.checkBox_doc_consent_bta.setObjectName(u"checkBox_doc_consent_bta")
        palette7 = QPalette()
        brush12 = QBrush(QColor(50, 98, 115, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(238, 238, 238, 255))
        gradient.setColorAt(1, QColor(190, 190, 190, 255))
        brush13 = QBrush(gradient)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush)
        brush14 = QBrush(QColor(236, 236, 236, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        brush15 = QBrush(QColor(108, 108, 108, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush15)
        brush16 = QBrush(QColor(145, 145, 145, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        gradient1 = QLinearGradient(0, 0, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(238, 238, 238, 255))
        gradient1.setColorAt(1, QColor(190, 190, 190, 255))
        brush17 = QBrush(gradient1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush17)
        gradient2 = QLinearGradient(0, 0, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(238, 238, 238, 255))
        gradient2.setColorAt(1, QColor(190, 190, 190, 255))
        brush18 = QBrush(gradient2)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush18)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        brush19 = QBrush(QColor(50, 98, 115, 128))
        brush19.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        gradient3 = QLinearGradient(0, 0, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(238, 238, 238, 255))
        gradient3.setColorAt(1, QColor(190, 190, 190, 255))
        brush20 = QBrush(gradient3)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        gradient4 = QLinearGradient(0, 0, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(238, 238, 238, 255))
        gradient4.setColorAt(1, QColor(190, 190, 190, 255))
        brush21 = QBrush(gradient4)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        gradient5 = QLinearGradient(0, 0, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(238, 238, 238, 255))
        gradient5.setColorAt(1, QColor(190, 190, 190, 255))
        brush22 = QBrush(gradient5)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush22)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        gradient6 = QLinearGradient(0, 0, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(238, 238, 238, 255))
        gradient6.setColorAt(1, QColor(190, 190, 190, 255))
        brush23 = QBrush(gradient6)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush23)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        gradient7 = QLinearGradient(0, 0, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(238, 238, 238, 255))
        gradient7.setColorAt(1, QColor(190, 190, 190, 255))
        brush24 = QBrush(gradient7)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush24)
        gradient8 = QLinearGradient(0, 0, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(238, 238, 238, 255))
        gradient8.setColorAt(1, QColor(190, 190, 190, 255))
        brush25 = QBrush(gradient8)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush25)
        brush26 = QBrush(QColor(217, 217, 217, 255))
        brush26.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
        brush27 = QBrush(QColor(238, 238, 238, 128))
        brush27.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_consent_bta.setPalette(palette7)
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.checkBox_doc_consent_bta.setFont(font5)
        self.checkBox_doc_consent_bta.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_4.addWidget(self.checkBox_doc_consent_bta, 3, 0, 1, 2)

        self.checkBox_doc_frontpage = QCheckBox(self.creacting_docs)
        self.checkBox_doc_frontpage.setObjectName(u"checkBox_doc_frontpage")
        self.checkBox_doc_frontpage.setEnabled(False)
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_frontpage.setPalette(palette8)
        self.checkBox_doc_frontpage.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_frontpage, 10, 0, 1, 2)

        self.pushButton_clean_ticks = QPushButton(self.creacting_docs)
        self.pushButton_clean_ticks.setObjectName(u"pushButton_clean_ticks")
        self.pushButton_clean_ticks.setMinimumSize(QSize(0, 22))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush28 = QBrush(QColor(50, 98, 115, 190))
        brush28.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush28)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush28)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush28)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush28)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush28)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush28)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush28)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush28)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush28)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButton_clean_ticks.setPalette(palette9)
        self.pushButton_clean_ticks.setFont(font2)
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

        self.gridLayout_4.addWidget(self.pushButton_clean_ticks, 2, 2, 1, 1)

        self.checkBox_doc_consents = QCheckBox(self.creacting_docs)
        self.checkBox_doc_consents.setObjectName(u"checkBox_doc_consents")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_consents.setPalette(palette10)
        self.checkBox_doc_consents.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_consents, 2, 0, 1, 2)

        self.checkBox_doc_protocol_bta = QCheckBox(self.creacting_docs)
        self.checkBox_doc_protocol_bta.setObjectName(u"checkBox_doc_protocol_bta")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_protocol_bta.setPalette(palette11)
        self.checkBox_doc_protocol_bta.setFont(font5)
        self.checkBox_doc_protocol_bta.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_4.addWidget(self.checkBox_doc_protocol_bta, 6, 0, 1, 2)

        self.checkBox_doc_statistic_talon_face = QCheckBox(self.creacting_docs)
        self.checkBox_doc_statistic_talon_face.setObjectName(u"checkBox_doc_statistic_talon_face")
        self.checkBox_doc_statistic_talon_face.setEnabled(False)
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_statistic_talon_face.setPalette(palette12)
        self.checkBox_doc_statistic_talon_face.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_statistic_talon_face, 8, 0, 1, 1)

        self.pushButtonCreateDocument = QPushButton(self.creacting_docs)
        self.pushButtonCreateDocument.setObjectName(u"pushButtonCreateDocument")
        self.pushButtonCreateDocument.setMinimumSize(QSize(0, 30))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush28)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush28)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush28)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush28)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush28)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush28)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush28)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush28)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush28)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonCreateDocument.setPalette(palette13)
        self.pushButtonCreateDocument.setFont(font2)
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
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/note_add_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCreateDocument.setIcon(icon7)
        self.pushButtonCreateDocument.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.pushButtonCreateDocument, 15, 0, 1, 3)

        self.checkBox_doc_initial_inspection = QCheckBox(self.creacting_docs)
        self.checkBox_doc_initial_inspection.setObjectName(u"checkBox_doc_initial_inspection")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_initial_inspection.setPalette(palette14)
        self.checkBox_doc_initial_inspection.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_initial_inspection, 5, 0, 1, 1)

        self.checkBox_doc_back_frontpage = QCheckBox(self.creacting_docs)
        self.checkBox_doc_back_frontpage.setObjectName(u"checkBox_doc_back_frontpage")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_back_frontpage.setPalette(palette15)
        self.checkBox_doc_back_frontpage.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_back_frontpage, 11, 0, 1, 2)

        self.checkBox_doc_statistic_talon = QCheckBox(self.creacting_docs)
        self.checkBox_doc_statistic_talon.setObjectName(u"checkBox_doc_statistic_talon")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_statistic_talon.setPalette(palette16)
        self.checkBox_doc_statistic_talon.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_statistic_talon, 9, 0, 1, 1)

        self.checkBox_doc_med_commission_bta = QCheckBox(self.creacting_docs)
        self.checkBox_doc_med_commission_bta.setObjectName(u"checkBox_doc_med_commission_bta")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_med_commission_bta.setPalette(palette17)
        self.checkBox_doc_med_commission_bta.setFont(font5)
        self.checkBox_doc_med_commission_bta.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_4.addWidget(self.checkBox_doc_med_commission_bta, 7, 0, 1, 2)

        self.checkBox_doc_full_history = QCheckBox(self.creacting_docs)
        self.checkBox_doc_full_history.setObjectName(u"checkBox_doc_full_history")
        self.checkBox_doc_full_history.setEnabled(False)
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_full_history.setPalette(palette18)
        self.checkBox_doc_full_history.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_full_history, 12, 2, 2, 1)

        self.checkBox_doc_discharge_summary = QCheckBox(self.creacting_docs)
        self.checkBox_doc_discharge_summary.setObjectName(u"checkBox_doc_discharge_summary")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_discharge_summary.setPalette(palette19)
        self.checkBox_doc_discharge_summary.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_discharge_summary, 12, 0, 1, 1)

        self.checkBox_doc_refusal = QCheckBox(self.creacting_docs)
        self.checkBox_doc_refusal.setObjectName(u"checkBox_doc_refusal")
        self.checkBox_doc_refusal.setEnabled(True)
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_refusal.setPalette(palette20)
        self.checkBox_doc_refusal.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_refusal, 13, 0, 1, 2)

        self.checkBox_doc_statistic_talon_other = QCheckBox(self.creacting_docs)
        self.checkBox_doc_statistic_talon_other.setObjectName(u"checkBox_doc_statistic_talon_other")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_statistic_talon_other.setPalette(palette21)
        self.checkBox_doc_statistic_talon_other.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_statistic_talon_other, 8, 1, 2, 1)

        self.label_status_3 = QLabel(self.creacting_docs)
        self.label_status_3.setObjectName(u"label_status_3")
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_status_3.setFont(font6)
        self.label_status_3.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(92, 158, 173, 200);\n"
"border: none;")

        self.gridLayout_4.addWidget(self.label_status_3, 1, 0, 1, 3)

        self.checkBox_doc_med_commission_drugs = QCheckBox(self.creacting_docs)
        self.checkBox_doc_med_commission_drugs.setObjectName(u"checkBox_doc_med_commission_drugs")
        self.checkBox_doc_med_commission_drugs.setEnabled(False)
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_med_commission_drugs.setPalette(palette22)
        self.checkBox_doc_med_commission_drugs.setFont(font5)
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
        self.checkBox_doc_med_commission_drugs.setCheckable(True)
        self.checkBox_doc_med_commission_drugs.setChecked(False)

        self.gridLayout_4.addWidget(self.checkBox_doc_med_commission_drugs, 10, 2, 1, 1)

        self.checkBox_doc_med_commission_1 = QCheckBox(self.creacting_docs)
        self.checkBox_doc_med_commission_1.setObjectName(u"checkBox_doc_med_commission_1")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_med_commission_1.setPalette(palette23)
        self.checkBox_doc_med_commission_1.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_med_commission_1, 9, 2, 1, 1)

        self.checkBox_doc_check_list = QCheckBox(self.creacting_docs)
        self.checkBox_doc_check_list.setObjectName(u"checkBox_doc_check_list")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_check_list.setPalette(palette24)
        self.checkBox_doc_check_list.setFont(font5)
        self.checkBox_doc_check_list.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_4.addWidget(self.checkBox_doc_check_list, 5, 2, 1, 1)

        self.checkBox_doc_appointments = QCheckBox(self.creacting_docs)
        self.checkBox_doc_appointments.setObjectName(u"checkBox_doc_appointments")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush26)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush26)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush26)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush26)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush26)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush26)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush26)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush27)
#endif
        self.checkBox_doc_appointments.setPalette(palette25)
        self.checkBox_doc_appointments.setFont(font5)
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

        self.gridLayout_4.addWidget(self.checkBox_doc_appointments, 6, 2, 2, 1)

        self.checkBox_complex = QCheckBox(self.creacting_docs)
        self.checkBox_complex.setObjectName(u"checkBox_complex")
        self.checkBox_complex.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"	padding-left: 40px;\n"
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
"}\n"
"")

        self.gridLayout_4.addWidget(self.checkBox_complex, 14, 0, 1, 3)


        self.verticalLayout_4.addWidget(self.creacting_docs)

        self.frame = QFrame(self.frame_111)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_status_2 = QLabel(self.frame)
        self.label_status_2.setObjectName(u"label_status_2")
        self.label_status_2.setFont(font6)
        self.label_status_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(92, 158, 173, 200);\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_status_2)

        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.textBrowser.setFont(font7)
        self.textBrowser.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"")

        self.verticalLayout.addWidget(self.textBrowser)

        self.pushButtonOpenFolder = QPushButton(self.frame)
        self.pushButtonOpenFolder.setObjectName(u"pushButtonOpenFolder")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush28)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush)
        palette26.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush28)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush28)
        palette26.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush28)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush28)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush28)
        palette26.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush28)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush28)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush28)
        palette26.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenFolder.setPalette(palette26)
        self.pushButtonOpenFolder.setFont(font2)
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
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/folder_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonOpenFolder.setIcon(icon8)
        self.pushButtonOpenFolder.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.pushButtonOpenFolder)


        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.frame_6 = QFrame(self.frame_111)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: White")
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_status = QLabel(self.frame_6)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMaximumSize(QSize(16777215, 30))
        self.label_status.setFont(font2)

        self.horizontalLayout.addWidget(self.label_status)

        self.pushButtonOpenLogs = QPushButton(self.frame_6)
        self.pushButtonOpenLogs.setObjectName(u"pushButtonOpenLogs")
        self.pushButtonOpenLogs.setMaximumSize(QSize(50, 30))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush28)
        palette27.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush)
        palette27.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush28)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush28)
        palette27.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette27.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette27.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette27.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush28)
        palette27.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush28)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush28)
        palette27.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette27.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette27.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette27.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette27.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette27.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette27.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette27.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonOpenLogs.setPalette(palette27)
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        font8.setPointSize(14)
        font8.setBold(False)
        self.pushButtonOpenLogs.setFont(font8)
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


        self.verticalLayout_5.addWidget(self.frame_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.groupBox_7 = QGroupBox(self.frame_111)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 20, 5, 5)
        self.label_dis_check = QLabel(self.groupBox_7)
        self.label_dis_check.setObjectName(u"label_dis_check")
        self.label_dis_check.setFont(font2)
        self.label_dis_check.setStyleSheet(u"color: White;\n"
"font-size: 11pt;")
        self.label_dis_check.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_dis_check)

        self.pushButtonHelp = QPushButton(self.groupBox_7)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        self.pushButtonHelp.setEnabled(False)
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush28)
        palette28.setBrush(QPalette.Active, QPalette.Light, brush)
        palette28.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette28.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush)
        palette28.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush28)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush28)
        palette28.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette28.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush28)
        palette28.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette28.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush28)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush28)
        palette28.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette28.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        brush29 = QBrush(QColor(50, 98, 115, 150))
        brush29.setStyle(Qt.SolidPattern)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush29)
        brush30 = QBrush(QColor(50, 98, 115, 40))
        brush30.setStyle(Qt.SolidPattern)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush30)
        palette28.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette28.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush29)
        palette28.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush29)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush30)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush30)
        palette28.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette28.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush31 = QBrush(QColor(50, 98, 115, 75))
        brush31.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
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
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHelp.setIcon(icon9)

        self.verticalLayout_7.addWidget(self.pushButtonHelp)

        self.pushButton_2 = QPushButton(self.groupBox_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush28)
        palette29.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush28)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush28)
        palette29.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette29.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette29.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette29.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush28)
        palette29.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush28)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush28)
        palette29.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette29.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette29.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette29.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush28)
        palette29.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush28)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush28)
        palette29.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette29.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette29.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette29.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButton_2.setPalette(palette29)
        self.pushButton_2.setFont(font2)
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

        self.pushButtonNotSaveExit = QPushButton(self.groupBox_7)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush28)
        palette30.setBrush(QPalette.Active, QPalette.Light, brush)
        brush32 = QBrush(QColor(237, 237, 237, 255))
        brush32.setStyle(Qt.SolidPattern)
        palette30.setBrush(QPalette.Active, QPalette.Midlight, brush32)
        brush33 = QBrush(QColor(110, 110, 110, 255))
        brush33.setStyle(Qt.SolidPattern)
        palette30.setBrush(QPalette.Active, QPalette.Dark, brush33)
        brush34 = QBrush(QColor(147, 147, 147, 255))
        brush34.setStyle(Qt.SolidPattern)
        palette30.setBrush(QPalette.Active, QPalette.Mid, brush34)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush)
        palette30.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush28)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush28)
        palette30.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette30.setBrush(QPalette.Active, QPalette.AlternateBase, brush32)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush28)
        palette30.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Midlight, brush32)
        palette30.setBrush(QPalette.Inactive, QPalette.Dark, brush33)
        palette30.setBrush(QPalette.Inactive, QPalette.Mid, brush34)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush28)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush28)
        palette30.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette30.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush32)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Midlight, brush32)
        palette30.setBrush(QPalette.Disabled, QPalette.Dark, brush33)
        palette30.setBrush(QPalette.Disabled, QPalette.Mid, brush34)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush35 = QBrush(QColor(220, 220, 220, 255))
        brush35.setStyle(Qt.SolidPattern)
        palette30.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush35)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonNotSaveExit.setPalette(palette30)
        self.pushButtonNotSaveExit.setFont(font8)
        self.pushButtonNotSaveExit.setStyleSheet(u"QPushButton {\n"
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
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon10)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSave = QPushButton(self.groupBox_7)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush28)
        palette31.setBrush(QPalette.Active, QPalette.Light, brush)
        palette31.setBrush(QPalette.Active, QPalette.Midlight, brush32)
        palette31.setBrush(QPalette.Active, QPalette.Dark, brush33)
        palette31.setBrush(QPalette.Active, QPalette.Mid, brush34)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush)
        palette31.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush28)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush28)
        palette31.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Active, QPalette.AlternateBase, brush32)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush28)
        palette31.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Midlight, brush32)
        palette31.setBrush(QPalette.Inactive, QPalette.Dark, brush33)
        palette31.setBrush(QPalette.Inactive, QPalette.Mid, brush34)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush28)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush28)
        palette31.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush32)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette31.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Midlight, brush32)
        palette31.setBrush(QPalette.Disabled, QPalette.Dark, brush33)
        palette31.setBrush(QPalette.Disabled, QPalette.Mid, brush34)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette31.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush35)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonSave.setPalette(palette31)
        self.pushButtonSave.setFont(font8)
        self.pushButtonSave.setStyleSheet(u"QPushButton {\n"
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
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSave.setIcon(icon11)
        self.pushButtonSave.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.pushButtonSave)

        self.pushButtonSaveExit = QPushButton(self.groupBox_7)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush36 = QBrush(QColor(92, 158, 173, 255))
        brush36.setStyle(Qt.SolidPattern)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush36)
        palette32.setBrush(QPalette.Active, QPalette.Light, brush)
        palette32.setBrush(QPalette.Active, QPalette.Midlight, brush32)
        palette32.setBrush(QPalette.Active, QPalette.Dark, brush33)
        palette32.setBrush(QPalette.Active, QPalette.Mid, brush34)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush)
        palette32.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush36)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush36)
        palette32.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette32.setBrush(QPalette.Active, QPalette.AlternateBase, brush32)
        palette32.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette32.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush36)
        palette32.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Midlight, brush32)
        palette32.setBrush(QPalette.Inactive, QPalette.Dark, brush33)
        palette32.setBrush(QPalette.Inactive, QPalette.Mid, brush34)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush36)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush36)
        palette32.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette32.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush32)
        palette32.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette32.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Midlight, brush32)
        palette32.setBrush(QPalette.Disabled, QPalette.Dark, brush33)
        palette32.setBrush(QPalette.Disabled, QPalette.Mid, brush34)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette32.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette32.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush35)
        palette32.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette32.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.pushButtonSaveExit.setPalette(palette32)
        self.pushButtonSaveExit.setFont(font8)
        self.pushButtonSaveExit.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(92, 158, 173, 255);\n"
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
"}")
        self.pushButtonSaveExit.setIcon(icon11)
        self.pushButtonSaveExit.setIconSize(QSize(36, 36))

        self.verticalLayout_7.addWidget(self.pushButtonSaveExit)


        self.horizontalLayout_3.addWidget(self.groupBox_7)


        self.verticalLayout_6.addWidget(self.frame_111)


        self.retranslateUi(PatientCard)

        self.pushButtonOpenPtDiagnosis.setDefault(False)


        QMetaObject.connectSlotsByName(PatientCard)
    # setupUi

    def retranslateUi(self, PatientCard):
        PatientCard.setWindowTitle(QCoreApplication.translate("PatientCard", u"Form", None))
        self.ptFullNameCard.setText(QCoreApplication.translate("PatientCard", u"< \u0418\u043c\u044f \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430>\n"
"< \u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f > // < \u0412\u043e\u0437\u0440\u0430\u0441\u0442 > \n"
"< \u0414\u0435\u043d\u044c \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f > --- < \u041a\u043e\u0439\u043a\u043e\u0434\u043d\u0438 > \u043a/\u0434", None))
#if QT_CONFIG(statustip)
        self.labelCard_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.labelCard_2.setText("")
        self.labelCard.setText(QCoreApplication.translate("PatientCard", u"\u041a\u0410\u0420\u0422\u0410 \u041f\u0410\u0426\u0418\u0415\u041d\u0422\u0410", None))
        self.label_uin.setText(QCoreApplication.translate("PatientCard", u"Card-UIN:", None))
        self.label_unic_number.setText("")
        self.labelCard_4.setText(QCoreApplication.translate("PatientCard", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.labelCard_3.setText("")
        self.pushButtonOpenPtPassportData.setText(QCoreApplication.translate("PatientCard", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonOpenPtObjStatus.setText(QCoreApplication.translate("PatientCard", u"\u0416\u0430\u043b\u043e\u0431\u044b, \u0430\u043d\u0430\u043c\u043d\u0435\u0437 \u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.pushButtonOpenPtNeuralStatus.setText(QCoreApplication.translate("PatientCard", u"\u041d\u0435\u0432\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.pushButtonOpenPtDiagnosis.setText(QCoreApplication.translate("PatientCard", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437 \u0438 \u0448\u043a\u0430\u043b\u044b", None))
        self.pushButtonOpen_bta_protocol.setText(QCoreApplication.translate("PatientCard", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u0431\u043e\u0442\u0443\u043b\u0438\u043d\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u0438", None))
        self.pushButtonOpen_discharge_data.setText(QCoreApplication.translate("PatientCard", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0432\u044b\u043f\u0438\u0441\u043a\u0438", None))
        self.pushButtonOpen_recommends.setText(QCoreApplication.translate("PatientCard", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438 \u0434\u043b\u044f \u0432\u044b\u043f\u0438\u0441\u043a\u0438", None))
        self.checkBox_doc_consent_bta.setText(QCoreApplication.translate("PatientCard", u"\u0421\u043e\u0433\u043b\u0430\u0441\u0438\u0435 \u043d\u0430 \u0431\u043e\u0442\u0443\u043b\u0438\u043d\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044e", None))
        self.checkBox_doc_frontpage.setText(QCoreApplication.translate("PatientCard", u"\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u0438\u0441\u0442\u043e\u0440\u0438\u0438 \u0431\u043e\u043b\u0435\u0437\u043d\u0438", None))
        self.pushButton_clean_ticks.setText(QCoreApplication.translate("PatientCard", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440", None))
        self.checkBox_doc_consents.setText(QCoreApplication.translate("PatientCard", u"\u0421\u043e\u0433\u043b\u0430\u0441\u0438\u044f (\u043f\u0435\u0440\u0441.\u0434\u0430\u043d\u043d\u044b\u0435, \u043d\u0430 \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044e)", None))
        self.checkBox_doc_protocol_bta.setText(QCoreApplication.translate("PatientCard", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u0431\u043e\u0442\u0443\u043b\u0438\u043d\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u0438", None))
        self.checkBox_doc_statistic_talon_face.setText(QCoreApplication.translate("PatientCard", u"\u0421\u0442\u0430\u0442.\u0442\u0430\u043b\u043e\u043d 1 \u0441\u0442\u0440.", None))
        self.pushButtonCreateDocument.setText(QCoreApplication.translate("PatientCard", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.checkBox_doc_initial_inspection.setText(QCoreApplication.translate("PatientCard", u"\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0439 \u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.checkBox_doc_back_frontpage.setText(QCoreApplication.translate("PatientCard", u"\u041e\u0431\u043e\u0440\u043e\u0442\u043d\u0430\u044f \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043e\u0431\u043b\u043e\u0436\u043a\u0438", None))
        self.checkBox_doc_statistic_talon.setText(QCoreApplication.translate("PatientCard", u"\u0421\u0442\u0430\u0442.\u0442\u0430\u043b\u043e\u043d 2 \u0441\u0442\u0440.", None))
        self.checkBox_doc_med_commission_bta.setText(QCoreApplication.translate("PatientCard", u"\u0412\u041a \u0434\u043b\u044f \u0431\u043e\u0442\u0443\u043b\u0438\u043d\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u0438", None))
        self.checkBox_doc_full_history.setText(QCoreApplication.translate("PatientCard", u"\u0412\u0441\u044f \u0438\u0441\u0442\u043e\u0440\u0438\u044f \u0431\u043e\u043b\u0435\u0437\u043d\u0438\n"
"\u043e\u0434\u043d\u0438\u043c \u0444\u0430\u0439\u043b\u043e\u043c", None))
        self.checkBox_doc_discharge_summary.setText(QCoreApplication.translate("PatientCard", u"\u0412\u044b\u043f\u0438\u0441\u043d\u043e\u0439 \u044d\u043f\u0438\u043a\u0440\u0438\u0437", None))
        self.checkBox_doc_refusal.setText(QCoreApplication.translate("PatientCard", u"\u041e\u0442\u043a\u0430\u0437 \u043e\u0442 \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.checkBox_doc_statistic_talon_other.setText(QCoreApplication.translate("PatientCard", u"\u0421\u0442\u0430\u0442.\u0442\u0430\u043b\u043e\u043d\n"
"\u0434\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 + Ds", None))
        self.label_status_3.setText(QCoreApplication.translate("PatientCard", u"<html><head/><body><p align=\"center\">\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432 (.docx)</p></body></html>", None))
        self.checkBox_doc_med_commission_drugs.setText(QCoreApplication.translate("PatientCard", u"\u0412\u041a \u043d\u0430 \u043b\u0435\u043a.\u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442", None))
        self.checkBox_doc_med_commission_1.setText(QCoreApplication.translate("PatientCard", u"\u0412\u041a \u043f\u043e \u043f\u0440\u043e\u0434\u043b\u0435\u043d\u0438\u044e \u041b\u041d", None))
        self.checkBox_doc_check_list.setText(QCoreApplication.translate("PatientCard", u"\u0447\u0435\u043a-\u043b\u0438\u0441\u0442 (covid19)", None))
        self.checkBox_doc_appointments.setText(QCoreApplication.translate("PatientCard", u"\u041b\u0438\u0441\u0442 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 +\n"
"\u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u043d\u044b\u0439 \u043b\u0438\u0441\u0442", None))
        self.checkBox_complex.setText(QCoreApplication.translate("PatientCard", u"\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0439 + \u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b + \u0412\u044b\u043f\u0438\u0441\u043a\u0430", None))
        self.label_status_2.setText(QCoreApplication.translate("PatientCard", u"<html><head/><body><p align=\"center\">\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b</p></body></html>", None))
        self.pushButtonOpenFolder.setText(QCoreApplication.translate("PatientCard", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 \u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
        self.label_status.setText(QCoreApplication.translate("PatientCard", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButtonOpenLogs.setText(QCoreApplication.translate("PatientCard", u"...\n"
" ", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("PatientCard", u"World of Medicine", None))
        self.label_dis_check.setText(QCoreApplication.translate("PatientCard", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("PatientCard", u"Help", None))
        self.pushButton_2.setText(QCoreApplication.translate("PatientCard", u"print(d.keys())", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("PatientCard", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c \n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f\n"
"\u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.pushButtonSave.setText(QCoreApplication.translate("PatientCard", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("PatientCard", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438 \u0437\u0430\u043a\u0440\u044b\u0442\u044c\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
    # retranslateUi

