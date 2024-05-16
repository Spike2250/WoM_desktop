# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'omr_AddNewPatient.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTimeEdit, QVBoxLayout, QWidget)
import res_main_rc

class Ui_PatientPassportData(object):
    def setupUi(self, PatientPassportData):
        if not PatientPassportData.objectName():
            PatientPassportData.setObjectName(u"PatientPassportData")
        PatientPassportData.resize(1290, 736)
        PatientPassportData.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_3 = QVBoxLayout(PatientPassportData)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_common = QFrame(PatientPassportData)
        self.frame_common.setObjectName(u"frame_common")
        self.horizontalLayout = QHBoxLayout(self.frame_common)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.promed_frame = QFrame(self.frame_common)
        self.promed_frame.setObjectName(u"promed_frame")
        self.promed_frame.setMinimumSize(QSize(300, 0))
        self.promed_frame.setMaximumSize(QSize(16777215, 16777215))
        self.promed_frame.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.promed_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.labelPassportData = QLabel(self.promed_frame)
        self.labelPassportData.setObjectName(u"labelPassportData")
        self.labelPassportData.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(50, 98, 115, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(50, 98, 115, 40))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(236, 236, 236, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(108, 108, 108, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(145, 145, 145, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(50, 98, 115, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush9 = QBrush(QColor(217, 217, 217, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPassportData.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(16)
        font.setBold(True)
        self.labelPassportData.setFont(font)
        self.labelPassportData.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: None;\n"
"")
        self.labelPassportData.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelPassportData)

        self.plainTextEdit_promed_data = QPlainTextEdit(self.promed_frame)
        self.plainTextEdit_promed_data.setObjectName(u"plainTextEdit_promed_data")
        self.plainTextEdit_promed_data.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.plainTextEdit_promed_data.setFont(font1)
        self.plainTextEdit_promed_data.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.plainTextEdit_promed_data)

        self.pushButton_add_from_promed = QPushButton(self.promed_frame)
        self.pushButton_add_from_promed.setObjectName(u"pushButton_add_from_promed")
        self.pushButton_add_from_promed.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush10 = QBrush(QColor(50, 98, 115, 190))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(255, 255, 255, 128))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButton_add_from_promed.setPalette(palette1)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.pushButton_add_from_promed.setFont(font2)
        self.pushButton_add_from_promed.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.pushButton_add_from_promed)

        self.plainTextEdit_descriptions_promed = QPlainTextEdit(self.promed_frame)
        self.plainTextEdit_descriptions_promed.setObjectName(u"plainTextEdit_descriptions_promed")
        self.plainTextEdit_descriptions_promed.setEnabled(False)
        self.plainTextEdit_descriptions_promed.setMaximumSize(QSize(16777215, 100))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(8)
        font3.setBold(True)
        self.plainTextEdit_descriptions_promed.setFont(font3)
        self.plainTextEdit_descriptions_promed.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"")

        self.verticalLayout_2.addWidget(self.plainTextEdit_descriptions_promed)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.promed_frame)

        self.main_frame = QFrame(self.frame_common)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMaximumSize(QSize(800, 16777215))
        self.main_frame.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(5, 5, 5, 2)
        self.labelPtHoptitalisationType = QLabel(self.main_frame)
        self.labelPtHoptitalisationType.setObjectName(u"labelPtHoptitalisationType")
        self.labelPtHoptitalisationType.setMaximumSize(QSize(16777215, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 0))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtHoptitalisationType.setPalette(palette2)
        self.labelPtHoptitalisationType.setFont(font1)
        self.labelPtHoptitalisationType.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtHoptitalisationType.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtHoptitalisationType, 4, 0, 1, 1)

        self.labelPtPassport = QLabel(self.main_frame)
        self.labelPtPassport.setObjectName(u"labelPtPassport")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtPassport.setPalette(palette3)
        self.labelPtPassport.setFont(font1)
        self.labelPtPassport.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtPassport.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtPassport, 27, 0, 1, 1)

        self.labelPtName = QLabel(self.main_frame)
        self.labelPtName.setObjectName(u"labelPtName")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtName.setPalette(palette4)
        self.labelPtName.setFont(font1)
        self.labelPtName.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtName, 16, 0, 1, 1)

        self.labelPtRoomNumber = QLabel(self.main_frame)
        self.labelPtRoomNumber.setObjectName(u"labelPtRoomNumber")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtRoomNumber.setPalette(palette5)
        self.labelPtRoomNumber.setFont(font1)
        self.labelPtRoomNumber.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtRoomNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtRoomNumber, 3, 0, 1, 1)

        self.label_department_head = QLabel(self.main_frame)
        self.label_department_head.setObjectName(u"label_department_head")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush13 = QBrush(QColor(237, 237, 237, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(110, 110, 110, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(147, 147, 147, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush16 = QBrush(QColor(220, 220, 220, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_department_head.setPalette(palette6)
        self.label_department_head.setFont(font1)
        self.label_department_head.setLayoutDirection(Qt.LeftToRight)
        self.label_department_head.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.label_department_head.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_department_head, 31, 0, 1, 1)

        self.label_bedprofile_2 = QLabel(self.main_frame)
        self.label_bedprofile_2.setObjectName(u"label_bedprofile_2")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_bedprofile_2.setPalette(palette7)
        self.label_bedprofile_2.setFont(font1)
        self.label_bedprofile_2.setLayoutDirection(Qt.LeftToRight)
        self.label_bedprofile_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.label_bedprofile_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_bedprofile_2, 9, 0, 1, 1)

        self.labelPtPhone = QLabel(self.main_frame)
        self.labelPtPhone.setObjectName(u"labelPtPhone")
        self.labelPtPhone.setMinimumSize(QSize(200, 0))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtPhone.setPalette(palette8)
        self.labelPtPhone.setFont(font1)
        self.labelPtPhone.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtPhone.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtPhone, 25, 0, 1, 1)

        self.labelPtSNILS = QLabel(self.main_frame)
        self.labelPtSNILS.setObjectName(u"labelPtSNILS")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtSNILS.setPalette(palette9)
        self.labelPtSNILS.setFont(font1)
        self.labelPtSNILS.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtSNILS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtSNILS, 29, 0, 1, 1)

        self.checkBoxPtNeedSickList = QCheckBox(self.main_frame)
        self.checkBoxPtNeedSickList.setObjectName(u"checkBoxPtNeedSickList")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        brush17 = QBrush(QColor(238, 238, 238, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        brush18 = QBrush(QColor(238, 238, 238, 128))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.checkBoxPtNeedSickList.setPalette(palette10)
        self.checkBoxPtNeedSickList.setFont(font2)
        self.checkBoxPtNeedSickList.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout.addWidget(self.checkBoxPtNeedSickList, 21, 1, 1, 1)

        self.labelTherapist = QLabel(self.main_frame)
        self.labelTherapist.setObjectName(u"labelTherapist")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelTherapist.setPalette(palette11)
        self.labelTherapist.setFont(font1)
        self.labelTherapist.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelTherapist.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelTherapist, 30, 0, 1, 1)

        self.label_history_number = QLabel(self.main_frame)
        self.label_history_number.setObjectName(u"label_history_number")
        self.label_history_number.setMinimumSize(QSize(200, 0))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_history_number.setPalette(palette12)
        self.label_history_number.setFont(font1)
        self.label_history_number.setLayoutDirection(Qt.LeftToRight)
        self.label_history_number.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.label_history_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_history_number, 2, 0, 1, 1)

        self.labelPtAdmissionTime = QLabel(self.main_frame)
        self.labelPtAdmissionTime.setObjectName(u"labelPtAdmissionTime")
        self.labelPtAdmissionTime.setMaximumSize(QSize(16777215, 16777215))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtAdmissionTime.setPalette(palette13)
        self.labelPtAdmissionTime.setFont(font1)
        self.labelPtAdmissionTime.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtAdmissionTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtAdmissionTime, 11, 0, 1, 1)

        self.labelPtNMU_code = QLabel(self.main_frame)
        self.labelPtNMU_code.setObjectName(u"labelPtNMU_code")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtNMU_code.setPalette(palette14)
        self.labelPtNMU_code.setFont(font1)
        self.labelPtNMU_code.setLayoutDirection(Qt.LeftToRight)
        self.labelPtNMU_code.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtNMU_code.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtNMU_code, 6, 0, 1, 1)

        self.labelPtEmail = QLabel(self.main_frame)
        self.labelPtEmail.setObjectName(u"labelPtEmail")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtEmail.setPalette(palette15)
        self.labelPtEmail.setFont(font1)
        self.labelPtEmail.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtEmail.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtEmail, 26, 0, 1, 1)

        self.labelPtAdress = QLabel(self.main_frame)
        self.labelPtAdress.setObjectName(u"labelPtAdress")
        self.labelPtAdress.setMinimumSize(QSize(200, 0))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtAdress.setPalette(palette16)
        self.labelPtAdress.setFont(font1)
        self.labelPtAdress.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtAdress.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtAdress, 19, 0, 1, 1)

        self.labelPtDadName = QLabel(self.main_frame)
        self.labelPtDadName.setObjectName(u"labelPtDadName")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtDadName.setPalette(palette17)
        self.labelPtDadName.setFont(font1)
        self.labelPtDadName.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtDadName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtDadName, 17, 0, 1, 1)

        self.labelPtAdmissionDay = QLabel(self.main_frame)
        self.labelPtAdmissionDay.setObjectName(u"labelPtAdmissionDay")
        self.labelPtAdmissionDay.setMaximumSize(QSize(16777215, 16777215))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtAdmissionDay.setPalette(palette18)
        self.labelPtAdmissionDay.setFont(font1)
        self.labelPtAdmissionDay.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtAdmissionDay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtAdmissionDay, 10, 0, 1, 1)

        self.label_discharge_info = QLabel(self.main_frame)
        self.label_discharge_info.setObjectName(u"label_discharge_info")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        self.label_discharge_info.setFont(font4)
        self.label_discharge_info.setStyleSheet(u"color: #326273;\n"
"border: None;")
        self.label_discharge_info.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_discharge_info, 12, 2, 1, 1)

        self.pushButton_today = QPushButton(self.main_frame)
        self.pushButton_today.setObjectName(u"pushButton_today")
        self.pushButton_today.setMaximumSize(QSize(16777215, 21))
        self.pushButton_today.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_today, 10, 2, 1, 1)

        self.dateEditPtAdmissionDay = QDateEdit(self.main_frame)
        self.dateEditPtAdmissionDay.setObjectName(u"dateEditPtAdmissionDay")
        palette19 = QPalette()
        brush19 = QBrush(QColor(19, 36, 43, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush20 = QBrush(QColor(19, 36, 43, 128))
        brush20.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.dateEditPtAdmissionDay.setPalette(palette19)
        self.dateEditPtAdmissionDay.setFont(font1)
        self.dateEditPtAdmissionDay.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.dateEditPtAdmissionDay.setTimeSpec(Qt.LocalTime)

        self.gridLayout.addWidget(self.dateEditPtAdmissionDay, 10, 1, 1, 1)

        self.dateEditDischargeDate_plan = QDateEdit(self.main_frame)
        self.dateEditDischargeDate_plan.setObjectName(u"dateEditDischargeDate_plan")
        self.dateEditDischargeDate_plan.setFont(font1)
        self.dateEditDischargeDate_plan.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.dateEditDischargeDate_plan, 12, 1, 1, 1)

        self.checkBoxPtNeedSickList_2 = QCheckBox(self.main_frame)
        self.checkBoxPtNeedSickList_2.setObjectName(u"checkBoxPtNeedSickList_2")
        self.checkBoxPtNeedSickList_2.setEnabled(False)
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.checkBoxPtNeedSickList_2.setPalette(palette20)
        self.checkBoxPtNeedSickList_2.setFont(font2)
        self.checkBoxPtNeedSickList_2.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout.addWidget(self.checkBoxPtNeedSickList_2, 21, 2, 1, 1)

        self.labelPtDischargeDate_plan = QLabel(self.main_frame)
        self.labelPtDischargeDate_plan.setObjectName(u"labelPtDischargeDate_plan")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtDischargeDate_plan.setPalette(palette21)
        self.labelPtDischargeDate_plan.setFont(font1)
        self.labelPtDischargeDate_plan.setLayoutDirection(Qt.LeftToRight)
        self.labelPtDischargeDate_plan.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtDischargeDate_plan.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtDischargeDate_plan, 12, 0, 1, 1)

        self.label_bedprofile = QLabel(self.main_frame)
        self.label_bedprofile.setObjectName(u"label_bedprofile")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette22.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette22.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette22.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette22.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette22.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette22.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette22.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette22.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_bedprofile.setPalette(palette22)
        self.label_bedprofile.setFont(font1)
        self.label_bedprofile.setLayoutDirection(Qt.LeftToRight)
        self.label_bedprofile.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.label_bedprofile.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_bedprofile, 8, 0, 1, 1)

        self.labelPtGender = QLabel(self.main_frame)
        self.labelPtGender.setObjectName(u"labelPtGender")
        self.labelPtGender.setMaximumSize(QSize(16777215, 16777215))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette23.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette23.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette23.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtGender.setPalette(palette23)
        self.labelPtGender.setFont(font1)
        self.labelPtGender.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtGender.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtGender, 20, 0, 1, 1)

        self.pushButton_yesterday = QPushButton(self.main_frame)
        self.pushButton_yesterday.setObjectName(u"pushButton_yesterday")
        self.pushButton_yesterday.setMaximumSize(QSize(16777215, 21))
        self.pushButton_yesterday.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_yesterday, 11, 2, 1, 1)

        self.label_referring_health_facility = QLabel(self.main_frame)
        self.label_referring_health_facility.setObjectName(u"label_referring_health_facility")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush)
        palette24.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette24.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_referring_health_facility.setPalette(palette24)
        self.label_referring_health_facility.setFont(font1)
        self.label_referring_health_facility.setLayoutDirection(Qt.LeftToRight)
        self.label_referring_health_facility.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.label_referring_health_facility.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_referring_health_facility, 13, 0, 1, 1)

        self.labelNeedSickList = QLabel(self.main_frame)
        self.labelNeedSickList.setObjectName(u"labelNeedSickList")
        self.labelNeedSickList.setMinimumSize(QSize(200, 0))
        self.labelNeedSickList.setMaximumSize(QSize(16777215, 16777215))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette25.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelNeedSickList.setPalette(palette25)
        self.labelNeedSickList.setFont(font1)
        self.labelNeedSickList.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelNeedSickList.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelNeedSickList, 21, 0, 1, 1)

        self.labelPtOms = QLabel(self.main_frame)
        self.labelPtOms.setObjectName(u"labelPtOms")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush)
        palette26.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette26.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette26.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette26.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtOms.setPalette(palette26)
        self.labelPtOms.setFont(font1)
        self.labelPtOms.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtOms.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtOms, 28, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 32, 0, 1, 1)

        self.timeEditPtAdmissionTime = QTimeEdit(self.main_frame)
        self.timeEditPtAdmissionTime.setObjectName(u"timeEditPtAdmissionTime")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette27.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette27.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette27.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette27.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette27.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette27.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.timeEditPtAdmissionTime.setPalette(palette27)
        self.timeEditPtAdmissionTime.setFont(font1)
        self.timeEditPtAdmissionTime.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.timeEditPtAdmissionTime, 11, 1, 1, 1)

        self.checkBox_need_psylogo = QCheckBox(self.main_frame)
        self.checkBox_need_psylogo.setObjectName(u"checkBox_need_psylogo")
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.checkBox_need_psylogo.setPalette(palette28)
        self.checkBox_need_psylogo.setFont(font2)
        self.checkBox_need_psylogo.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout.addWidget(self.checkBox_need_psylogo, 9, 1, 1, 1)

        self.labelPtMKB10_main = QLabel(self.main_frame)
        self.labelPtMKB10_main.setObjectName(u"labelPtMKB10_main")
        self.labelPtMKB10_main.setMinimumSize(QSize(0, 0))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette29.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette29.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette29.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette29.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette29.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette29.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette29.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette29.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette29.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette29.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette29.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette29.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette29.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette29.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtMKB10_main.setPalette(palette29)
        self.labelPtMKB10_main.setFont(font1)
        self.labelPtMKB10_main.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtMKB10_main.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtMKB10_main, 5, 0, 1, 1)

        self.labelPtSurName = QLabel(self.main_frame)
        self.labelPtSurName.setObjectName(u"labelPtSurName")
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette30.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush)
        palette30.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette30.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette30.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette30.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette30.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette30.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette30.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette30.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette30.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtSurName.setPalette(palette30)
        self.labelPtSurName.setFont(font1)
        self.labelPtSurName.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtSurName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtSurName, 15, 0, 1, 1)

        self.labelPtBirthDay = QLabel(self.main_frame)
        self.labelPtBirthDay.setObjectName(u"labelPtBirthDay")
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette31.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush)
        palette31.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette31.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette31.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette31.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette31.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette31.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette31.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPtBirthDay.setPalette(palette31)
        self.labelPtBirthDay.setFont(font1)
        self.labelPtBirthDay.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.labelPtBirthDay.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPtBirthDay, 18, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 10, 3, 1, 1)

        self.comboBox_referring_health_facility = QComboBox(self.main_frame)
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
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette32.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette32.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette32.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette32.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette32.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette32.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette32.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette32.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette32.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette32.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette32.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette32.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBox_referring_health_facility.setPalette(palette32)
        self.comboBox_referring_health_facility.setFont(font1)
        self.comboBox_referring_health_facility.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_referring_health_facility.setEditable(True)

        self.gridLayout.addWidget(self.comboBox_referring_health_facility, 13, 1, 1, 3)

        self.labelPassportData_2 = QLabel(self.main_frame)
        self.labelPassportData_2.setObjectName(u"labelPassportData_2")
        self.labelPassportData_2.setMaximumSize(QSize(16777215, 50))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush)
        palette33.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette33.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette33.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette33.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette33.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette33.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette33.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette33.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette33.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPassportData_2.setPalette(palette33)
        self.labelPassportData_2.setFont(font)
        self.labelPassportData_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: None;\n"
"")
        self.labelPassportData_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPassportData_2, 14, 0, 1, 4)

        self.lineEditPtSurName = QLineEdit(self.main_frame)
        self.lineEditPtSurName.setObjectName(u"lineEditPtSurName")
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette34.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette34.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette34.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette34.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette34.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette34.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtSurName.setPalette(palette34)
        self.lineEditPtSurName.setFont(font1)
        self.lineEditPtSurName.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtSurName, 15, 1, 1, 3)

        self.lineEditPtName = QLineEdit(self.main_frame)
        self.lineEditPtName.setObjectName(u"lineEditPtName")
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette35.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette35.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette35.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette35.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette35.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette35.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtName.setPalette(palette35)
        self.lineEditPtName.setFont(font1)
        self.lineEditPtName.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtName, 16, 1, 1, 3)

        self.lineEditPtDadName = QLineEdit(self.main_frame)
        self.lineEditPtDadName.setObjectName(u"lineEditPtDadName")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette36.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette36.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette36.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette36.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette36.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette36.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtDadName.setPalette(palette36)
        self.lineEditPtDadName.setFont(font1)
        self.lineEditPtDadName.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtDadName, 17, 1, 1, 3)

        self.lineEditPtAdress = QLineEdit(self.main_frame)
        self.lineEditPtAdress.setObjectName(u"lineEditPtAdress")
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette37.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette37.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette37.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette37.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette37.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette37.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtAdress.setPalette(palette37)
        self.lineEditPtAdress.setFont(font1)
        self.lineEditPtAdress.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtAdress, 19, 1, 1, 3)

        self.comboBoxGender = QComboBox(self.main_frame)
        self.comboBoxGender.addItem("")
        self.comboBoxGender.addItem("")
        self.comboBoxGender.setObjectName(u"comboBoxGender")
        self.comboBoxGender.setMaximumSize(QSize(16777215, 16777215))
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette38.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette38.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette38.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette38.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette38.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette38.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette38.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette38.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette38.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette38.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette38.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette38.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette38.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette38.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette38.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette38.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette38.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBoxGender.setPalette(palette38)
        self.comboBoxGender.setFont(font1)
        self.comboBoxGender.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBoxGender, 20, 1, 1, 1)

        self.checkBoxPtLeftHanded = QCheckBox(self.main_frame)
        self.checkBoxPtLeftHanded.setObjectName(u"checkBoxPtLeftHanded")
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette39.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush)
        palette39.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette39.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette39.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette39.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette39.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette39.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette39.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette39.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.checkBoxPtLeftHanded.setPalette(palette39)
        self.checkBoxPtLeftHanded.setFont(font2)
        self.checkBoxPtLeftHanded.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout.addWidget(self.checkBoxPtLeftHanded, 20, 2, 1, 1)

        self.lineEditPtPhone = QLineEdit(self.main_frame)
        self.lineEditPtPhone.setObjectName(u"lineEditPtPhone")
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette40.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette40.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette40.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette40.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette40.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette40.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette40.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette40.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette40.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette40.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette40.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette40.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtPhone.setPalette(palette40)
        self.lineEditPtPhone.setFont(font1)
        self.lineEditPtPhone.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtPhone, 25, 1, 1, 3)

        self.comboBox_department_head = QComboBox(self.main_frame)
        self.comboBox_department_head.setObjectName(u"comboBox_department_head")
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette41.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette41.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette41.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette41.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette41.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette41.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette41.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette41.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette41.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette41.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette41.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette41.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBox_department_head.setPalette(palette41)
        self.comboBox_department_head.setFont(font1)
        self.comboBox_department_head.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_department_head.setEditable(True)

        self.gridLayout.addWidget(self.comboBox_department_head, 31, 1, 1, 3)

        self.comboBoxTherapist = QComboBox(self.main_frame)
        self.comboBoxTherapist.setObjectName(u"comboBoxTherapist")
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette42.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette42.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette42.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette42.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette42.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette42.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette42.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette42.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette42.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette42.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette42.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette42.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette42.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBoxTherapist.setPalette(palette42)
        self.comboBoxTherapist.setFont(font1)
        self.comboBoxTherapist.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxTherapist.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxTherapist, 30, 1, 1, 3)

        self.lineEditPtSNILS = QLineEdit(self.main_frame)
        self.lineEditPtSNILS.setObjectName(u"lineEditPtSNILS")
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette43.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette43.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette43.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette43.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette43.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette43.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette43.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtSNILS.setPalette(palette43)
        self.lineEditPtSNILS.setFont(font1)
        self.lineEditPtSNILS.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtSNILS, 29, 1, 1, 3)

        self.lineEditPtOmsNumber = QLineEdit(self.main_frame)
        self.lineEditPtOmsNumber.setObjectName(u"lineEditPtOmsNumber")
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette44.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette44.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette44.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette44.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette44.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette44.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtOmsNumber.setPalette(palette44)
        self.lineEditPtOmsNumber.setFont(font1)
        self.lineEditPtOmsNumber.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtOmsNumber, 28, 1, 1, 3)

        self.lineEditPtPassportNumber = QLineEdit(self.main_frame)
        self.lineEditPtPassportNumber.setObjectName(u"lineEditPtPassportNumber")
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette45.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette45.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette45.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette45.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette45.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette45.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette45.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette45.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette45.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtPassportNumber.setPalette(palette45)
        self.lineEditPtPassportNumber.setFont(font1)
        self.lineEditPtPassportNumber.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtPassportNumber, 27, 1, 1, 3)

        self.lineEditPtEmail = QLineEdit(self.main_frame)
        self.lineEditPtEmail.setObjectName(u"lineEditPtEmail")
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette46.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette46.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette46.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette46.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette46.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette46.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette46.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette46.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette46.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette46.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette46.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEditPtEmail.setPalette(palette46)
        self.lineEditPtEmail.setFont(font1)
        self.lineEditPtEmail.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEditPtEmail, 26, 1, 1, 3)

        self.comboBox_bedprofile = QComboBox(self.main_frame)
        self.comboBox_bedprofile.setObjectName(u"comboBox_bedprofile")
        self.comboBox_bedprofile.setMaximumSize(QSize(16777215, 16777215))
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette47.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette47.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette47.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette47.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette47.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette47.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette47.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette47.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette47.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette47.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette47.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette47.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette47.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette47.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette47.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette47.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBox_bedprofile.setPalette(palette47)
        self.comboBox_bedprofile.setFont(font1)
        self.comboBox_bedprofile.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_bedprofile.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_bedprofile, 8, 1, 1, 3)

        self.frame_name = QFrame(self.main_frame)
        self.frame_name.setObjectName(u"frame_name")
        self.verticalLayout_123 = QVBoxLayout(self.frame_name)
        self.verticalLayout_123.setSpacing(2)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(2, 2, 2, 2)
        self.labelNewPatient = QLabel(self.frame_name)
        self.labelNewPatient.setObjectName(u"labelNewPatient")
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setItalic(True)
        self.labelNewPatient.setFont(font5)
        self.labelNewPatient.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.labelNewPatient.setAlignment(Qt.AlignCenter)

        self.verticalLayout_123.addWidget(self.labelNewPatient)

        self.label_unic_number = QLabel(self.frame_name)
        self.label_unic_number.setObjectName(u"label_unic_number")
        self.label_unic_number.setFont(font4)
        self.label_unic_number.setStyleSheet(u"border: None;")

        self.verticalLayout_123.addWidget(self.label_unic_number)


        self.gridLayout.addWidget(self.frame_name, 0, 0, 1, 4)

        self.labelPassportData_3 = QLabel(self.main_frame)
        self.labelPassportData_3.setObjectName(u"labelPassportData_3")
        self.labelPassportData_3.setMaximumSize(QSize(16777215, 50))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette48.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette48.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush)
        palette48.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette48.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette48.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette48.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette48.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette48.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette48.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette48.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette48.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette48.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette48.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette48.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette48.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette48.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette48.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette48.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.labelPassportData_3.setPalette(palette48)
        self.labelPassportData_3.setFont(font)
        self.labelPassportData_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: None;\n"
"")
        self.labelPassportData_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPassportData_3, 1, 0, 1, 4)

        self.dateEditPtBirthDay = QDateEdit(self.main_frame)
        self.dateEditPtBirthDay.setObjectName(u"dateEditPtBirthDay")
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette49.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette49.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette49.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette49.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette49.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette49.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette49.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette49.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette49.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette49.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.dateEditPtBirthDay.setPalette(palette49)
        self.dateEditPtBirthDay.setFont(font1)
        self.dateEditPtBirthDay.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.dateEditPtBirthDay, 18, 1, 1, 1)

        self.comboBoxPtNMU_code = QComboBox(self.main_frame)
        self.comboBoxPtNMU_code.setObjectName(u"comboBoxPtNMU_code")
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette50.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette50.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette50.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette50.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette50.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette50.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette50.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette50.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette50.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette50.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette50.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette50.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette50.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette50.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette50.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette50.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette50.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBoxPtNMU_code.setPalette(palette50)
        self.comboBoxPtNMU_code.setFont(font1)
        self.comboBoxPtNMU_code.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtNMU_code.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxPtNMU_code, 6, 1, 1, 3)

        self.comboBoxPtMKB10_main = QComboBox(self.main_frame)
        self.comboBoxPtMKB10_main.setObjectName(u"comboBoxPtMKB10_main")
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette51.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette51.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette51.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette51.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette51.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette51.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette51.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette51.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette51.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette51.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette51.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette51.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette51.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette51.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette51.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette51.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette51.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette51.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette51.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette51.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBoxPtMKB10_main.setPalette(palette51)
        self.comboBoxPtMKB10_main.setFont(font1)
        self.comboBoxPtMKB10_main.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtMKB10_main.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxPtMKB10_main, 5, 1, 1, 3)

        self.comboBoxPtHoptitalisationType = QComboBox(self.main_frame)
        self.comboBoxPtHoptitalisationType.addItem("")
        self.comboBoxPtHoptitalisationType.addItem("")
        self.comboBoxPtHoptitalisationType.setObjectName(u"comboBoxPtHoptitalisationType")
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette52.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette52.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette52.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette52.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette52.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette52.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette52.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette52.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette52.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette52.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette52.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette52.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette52.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette52.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette52.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette52.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette52.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette52.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette52.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette52.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBoxPtHoptitalisationType.setPalette(palette52)
        self.comboBoxPtHoptitalisationType.setFont(font1)
        self.comboBoxPtHoptitalisationType.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBoxPtHoptitalisationType, 4, 1, 1, 3)

        self.comboBoxPtRoomNumber = QComboBox(self.main_frame)
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.addItem("")
        self.comboBoxPtRoomNumber.setObjectName(u"comboBoxPtRoomNumber")
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette53.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette53.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette53.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette53.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette53.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette53.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette53.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette53.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette53.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette53.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette53.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette53.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette53.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette53.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette53.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette53.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette53.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette53.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette53.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette53.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette53.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.comboBoxPtRoomNumber.setPalette(palette53)
        self.comboBoxPtRoomNumber.setFont(font1)
        self.comboBoxPtRoomNumber.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtRoomNumber.setEditable(False)

        self.gridLayout.addWidget(self.comboBoxPtRoomNumber, 3, 1, 1, 3)

        self.lineEdit_history_number = QLineEdit(self.main_frame)
        self.lineEdit_history_number.setObjectName(u"lineEdit_history_number")
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush19)
        palette54.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette54.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Text, brush19)
        palette54.setBrush(QPalette.Active, QPalette.ButtonText, brush19)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette54.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush19)
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette54.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Text, brush19)
        palette54.setBrush(QPalette.Inactive, QPalette.ButtonText, brush19)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette54.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette54.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette54.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette54.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette54.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.lineEdit_history_number.setPalette(palette54)
        self.lineEdit_history_number.setFont(font1)
        self.lineEdit_history_number.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_history_number, 2, 1, 1, 3)

        self.plainTextEdit_descriptions = QPlainTextEdit(self.main_frame)
        self.plainTextEdit_descriptions.setObjectName(u"plainTextEdit_descriptions")
        self.plainTextEdit_descriptions.setEnabled(True)
        self.plainTextEdit_descriptions.setMaximumSize(QSize(16777215, 55))
        self.plainTextEdit_descriptions.setFont(font3)
        self.plainTextEdit_descriptions.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"")

        self.gridLayout.addWidget(self.plainTextEdit_descriptions, 7, 0, 1, 4)


        self.horizontalLayout.addWidget(self.main_frame)

        self.wom_panel = QFrame(self.frame_common)
        self.wom_panel.setObjectName(u"wom_panel")
        self.wom_panel.setMaximumSize(QSize(200, 16777215))
        self.wom_panel.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.wom_panel)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.wom_panel)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #326273;\n"
"border: none;\n"
"background-color: transparent;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.help_page = QPushButton(self.wom_panel)
        self.help_page.setObjectName(u"help_page")
        self.help_page.setEnabled(False)
        self.help_page.setFont(font4)
        self.help_page.setStyleSheet(u"QPushButton {\n"
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
        self.help_page.setIcon(icon)
        self.help_page.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.help_page)

        self.pushButtonBackToMenu = QPushButton(self.wom_panel)
        self.pushButtonBackToMenu.setObjectName(u"pushButtonBackToMenu")
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette55.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette55.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette55.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette55.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette55.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette55.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette55.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette55.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette55.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette55.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette55.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette55.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette55.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette55.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette55.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette55.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette55.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette55.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette55.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette55.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette55.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButtonBackToMenu.setPalette(palette55)
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(14)
        font6.setBold(False)
        self.pushButtonBackToMenu.setFont(font6)
        self.pushButtonBackToMenu.setStyleSheet(u"QPushButton {\n"
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
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/west_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonBackToMenu.setIcon(icon1)
        self.pushButtonBackToMenu.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.pushButtonBackToMenu)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButtonAddRelative = QPushButton(self.wom_panel)
        self.pushButtonAddRelative.setObjectName(u"pushButtonAddRelative")
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette56.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette56.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette56.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette56.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette56.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette56.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette56.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette56.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette56.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette56.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette56.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette56.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette56.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette56.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette56.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette56.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette56.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette56.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette56.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette56.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette56.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette56.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette56.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette56.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette56.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette56.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette56.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette56.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette56.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette56.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette56.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette56.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButtonAddRelative.setPalette(palette56)
        self.pushButtonAddRelative.setFont(font6)
        self.pushButtonAddRelative.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_4.addWidget(self.pushButtonAddRelative)

        self.pushButtonPrintConsent = QPushButton(self.wom_panel)
        self.pushButtonPrintConsent.setObjectName(u"pushButtonPrintConsent")
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette57.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette57.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette57.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette57.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette57.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette57.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette57.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette57.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette57.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette57.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette57.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette57.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette57.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette57.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette57.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette57.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette57.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette57.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette57.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette57.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette57.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette57.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette57.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette57.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButtonPrintConsent.setPalette(palette57)
        self.pushButtonPrintConsent.setFont(font6)
        self.pushButtonPrintConsent.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/print_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPrintConsent.setIcon(icon2)
        self.pushButtonPrintConsent.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.pushButtonPrintConsent)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.pushButtonCreateHistory = QPushButton(self.wom_panel)
        self.pushButtonCreateHistory.setObjectName(u"pushButtonCreateHistory")
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush21 = QBrush(QColor(92, 158, 173, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette58.setBrush(QPalette.Active, QPalette.Button, brush21)
        palette58.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette58.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette58.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette58.setBrush(QPalette.Active, QPalette.Base, brush21)
        palette58.setBrush(QPalette.Active, QPalette.Window, brush21)
        palette58.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette58.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette58.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette58.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.Button, brush21)
        palette58.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        palette58.setBrush(QPalette.Inactive, QPalette.Window, brush21)
        palette58.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette58.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette58.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette58.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette58.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette58.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette58.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette58.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette58.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette58.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette58.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.pushButtonCreateHistory.setPalette(palette58)
        self.pushButtonCreateHistory.setFont(font6)
        self.pushButtonCreateHistory.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/person_add_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCreateHistory.setIcon(icon3)
        self.pushButtonCreateHistory.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.pushButtonCreateHistory)

        self.verticalSpacer_7 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)


        self.horizontalLayout.addWidget(self.wom_panel)


        self.verticalLayout_3.addWidget(self.frame_common)

        QWidget.setTabOrder(self.plainTextEdit_promed_data, self.pushButton_add_from_promed)
        QWidget.setTabOrder(self.pushButton_add_from_promed, self.lineEdit_history_number)
        QWidget.setTabOrder(self.lineEdit_history_number, self.comboBoxPtRoomNumber)
        QWidget.setTabOrder(self.comboBoxPtRoomNumber, self.comboBoxPtHoptitalisationType)
        QWidget.setTabOrder(self.comboBoxPtHoptitalisationType, self.comboBoxPtMKB10_main)
        QWidget.setTabOrder(self.comboBoxPtMKB10_main, self.comboBoxPtNMU_code)
        QWidget.setTabOrder(self.comboBoxPtNMU_code, self.comboBox_bedprofile)
        QWidget.setTabOrder(self.comboBox_bedprofile, self.checkBox_need_psylogo)
        QWidget.setTabOrder(self.checkBox_need_psylogo, self.pushButton_today)
        QWidget.setTabOrder(self.pushButton_today, self.pushButton_yesterday)
        QWidget.setTabOrder(self.pushButton_yesterday, self.dateEditPtAdmissionDay)
        QWidget.setTabOrder(self.dateEditPtAdmissionDay, self.timeEditPtAdmissionTime)
        QWidget.setTabOrder(self.timeEditPtAdmissionTime, self.dateEditDischargeDate_plan)
        QWidget.setTabOrder(self.dateEditDischargeDate_plan, self.comboBox_referring_health_facility)
        QWidget.setTabOrder(self.comboBox_referring_health_facility, self.plainTextEdit_descriptions)
        QWidget.setTabOrder(self.plainTextEdit_descriptions, self.plainTextEdit_descriptions_promed)
        QWidget.setTabOrder(self.plainTextEdit_descriptions_promed, self.lineEditPtSurName)
        QWidget.setTabOrder(self.lineEditPtSurName, self.lineEditPtName)
        QWidget.setTabOrder(self.lineEditPtName, self.lineEditPtDadName)
        QWidget.setTabOrder(self.lineEditPtDadName, self.dateEditPtBirthDay)
        QWidget.setTabOrder(self.dateEditPtBirthDay, self.lineEditPtAdress)
        QWidget.setTabOrder(self.lineEditPtAdress, self.comboBoxGender)
        QWidget.setTabOrder(self.comboBoxGender, self.checkBoxPtNeedSickList)
        QWidget.setTabOrder(self.checkBoxPtNeedSickList, self.checkBoxPtNeedSickList_2)
        QWidget.setTabOrder(self.checkBoxPtNeedSickList_2, self.lineEditPtPhone)
        QWidget.setTabOrder(self.lineEditPtPhone, self.lineEditPtEmail)
        QWidget.setTabOrder(self.lineEditPtEmail, self.lineEditPtPassportNumber)
        QWidget.setTabOrder(self.lineEditPtPassportNumber, self.lineEditPtOmsNumber)
        QWidget.setTabOrder(self.lineEditPtOmsNumber, self.lineEditPtSNILS)
        QWidget.setTabOrder(self.lineEditPtSNILS, self.comboBoxTherapist)
        QWidget.setTabOrder(self.comboBoxTherapist, self.comboBox_department_head)
        QWidget.setTabOrder(self.comboBox_department_head, self.pushButtonAddRelative)
        QWidget.setTabOrder(self.pushButtonAddRelative, self.pushButtonPrintConsent)
        QWidget.setTabOrder(self.pushButtonPrintConsent, self.help_page)

        self.retranslateUi(PatientPassportData)

        QMetaObject.connectSlotsByName(PatientPassportData)
    # setupUi

    def retranslateUi(self, PatientPassportData):
        PatientPassportData.setWindowTitle(QCoreApplication.translate("PatientPassportData", u"Form", None))
        self.labelPassportData.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u0411\u044b\u0441\u0442\u0440\u043e\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435</p></body></html>", None))
        self.plainTextEdit_promed_data.setPlaceholderText(QCoreApplication.translate("PatientPassportData", u"\u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0441\u044e\u0434\u0430 \u0441\u0442\u0440\u043e\u043a\u0443 \u0434\u043b\u044f \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.pushButton_add_from_promed.setText(QCoreApplication.translate("PatientPassportData", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u041f\u0440\u043e\u043c\u0435\u0434", None))
        self.labelPtHoptitalisationType.setText(QCoreApplication.translate("PatientPassportData", u"\u0422\u0438\u043f \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438:", None))
        self.labelPtPassport.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442 (\u0441\u0435\u0440\u0438\u044f, \u043d\u043e\u043c\u0435\u0440): ", None))
        self.labelPtName.setText(QCoreApplication.translate("PatientPassportData", u"\u0418\u043c\u044f:", None))
        self.labelPtRoomNumber.setText(QCoreApplication.translate("PatientPassportData", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u043b\u0430\u0442\u044b:", None))
        self.label_department_head.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u0417\u0430\u0432.\u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435\u043c:</p></body></html>", None))
        self.label_bedprofile_2.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0441\u043c\u043e\u0442\u0440\u0430:</p></body></html>", None))
        self.labelPtPhone.setText(QCoreApplication.translate("PatientPassportData", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.labelPtSNILS.setText(QCoreApplication.translate("PatientPassportData", u"\u0421\u041d\u0418\u041b\u0421 (\u043d\u043e\u043c\u0435\u0440):", None))
        self.checkBoxPtNeedSickList.setText(QCoreApplication.translate("PatientPassportData", u"\u041d\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u041b\u041d", None))
        self.labelTherapist.setText(QCoreApplication.translate("PatientPassportData", u"\u041b\u0435\u0447\u0430\u0449\u0438\u0439 \u0432\u0440\u0430\u0447:", None))
        self.label_history_number.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u041d\u043e\u043c\u0435\u0440 \u0438\u0441\u0442\u043e\u0440\u0438\u0438 \u0431\u043e\u043b\u0435\u0437\u043d\u0438:</p></body></html>", None))
        self.labelPtAdmissionTime.setText(QCoreApplication.translate("PatientPassportData", u"\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f:", None))
        self.labelPtNMU_code.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u041a\u043e\u0434 \u043c\u0435\u0434.\u0443\u0441\u043b\u0443\u0433\u0438:</p></body></html>", None))
        self.labelPtEmail.setText(QCoreApplication.translate("PatientPassportData", u"E-mail:", None))
        self.labelPtAdress.setText(QCoreApplication.translate("PatientPassportData", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u0430\u0434\u0440\u0435\u0441:", None))
        self.labelPtDadName.setText(QCoreApplication.translate("PatientPassportData", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.labelPtAdmissionDay.setText(QCoreApplication.translate("PatientPassportData", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_discharge_info.setText("")
        self.pushButton_today.setText(QCoreApplication.translate("PatientPassportData", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.dateEditPtAdmissionDay.setDisplayFormat(QCoreApplication.translate("PatientPassportData", u"dd.MM.yyyy", None))
        self.checkBoxPtNeedSickList_2.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0439", None))
        self.labelPtDischargeDate_plan.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u0438\u0441\u043a\u0438 (\u043f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u043c\u0430\u044f):</p></body></html>", None))
        self.label_bedprofile.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u043a\u043e\u0439\u043a\u0438:</p></body></html>", None))
        self.labelPtGender.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u043e\u043b:", None))
        self.pushButton_yesterday.setText(QCoreApplication.translate("PatientPassportData", u"\u0412\u0447\u0435\u0440\u0430", None))
        self.label_referring_health_facility.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u041d\u0430\u043f\u0440\u0430\u0432\u0438\u0432\u0448\u0435\u0435 \u041b\u041f\u0423:</p></body></html>", None))
        self.labelNeedSickList.setText(QCoreApplication.translate("PatientPassportData", u"\u041b\u0438\u0441\u0442 \u043d\u0435\u0442\u0440\u0443\u0434\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438:", None))
        self.labelPtOms.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u043e\u043b\u0438\u0441 \u041e\u041c\u0421 (\u043d\u043e\u043c\u0435\u0440):", None))
        self.checkBox_need_psylogo.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u0441\u0438\u0445\u043e\u043b\u043e\u0433\u0430 \u0438 \u043b\u043e\u0433\u043e\u043f\u0435\u0434\u0430", None))
        self.labelPtMKB10_main.setText(QCoreApplication.translate("PatientPassportData", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437 \u043f\u043e \u041c\u041a\u0411-10, \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439:", None))
        self.labelPtSurName.setText(QCoreApplication.translate("PatientPassportData", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.labelPtBirthDay.setText(QCoreApplication.translate("PatientPassportData", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.comboBox_referring_health_facility.setItemText(0, "")
        self.comboBox_referring_health_facility.setItemText(1, QCoreApplication.translate("PatientPassportData", u"\u043f\u043e\u043b\u0438\u043a\u043b\u0438\u043d\u0438\u043a\u0430 \u0413\u041a\u0411 \u0438\u043c.\u0421.\u041d.\u0413\u0440\u0438\u043d\u0431\u0435\u0440\u0433\u0430", None))
        self.comboBox_referring_health_facility.setItemText(2, QCoreApplication.translate("PatientPassportData", u"\u0413\u041a\u041f 2", None))
        self.comboBox_referring_health_facility.setItemText(3, QCoreApplication.translate("PatientPassportData", u"\u043d\u0435\u0432\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0413\u041a\u0411 \u0438\u043c.\u0421.\u041d.\u0413\u0440\u0438\u043d\u0431\u0435\u0440\u0433\u0430", None))
        self.comboBox_referring_health_facility.setItemText(4, QCoreApplication.translate("PatientPassportData", u"\u043d\u0435\u0432\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0413\u041a\u0411 \u0438\u043c.\u041c.\u0410.\u0422\u0432\u0435\u0440\u044c\u0435", None))
        self.comboBox_referring_health_facility.setItemText(5, QCoreApplication.translate("PatientPassportData", u"\u041a\u0440\u0430\u0441\u043d\u043e\u043a\u0430\u043c\u0441\u043a\u0430\u044f \u0413\u0411", None))
        self.comboBox_referring_health_facility.setItemText(6, QCoreApplication.translate("PatientPassportData", u"\u041d\u044b\u0442\u0432\u0435\u043d\u0441\u043a\u0430\u044f \u0420\u0411", None))
        self.comboBox_referring_health_facility.setItemText(7, QCoreApplication.translate("PatientPassportData", u"\u0411\u043e\u043b\u044c\u0448\u0435\u0441\u043e\u0441\u043d\u043e\u0432\u0441\u043a\u0430\u044f \u0426\u0420\u0411", None))
        self.comboBox_referring_health_facility.setItemText(8, QCoreApplication.translate("PatientPassportData", u"\u041e\u0441\u0438\u043d\u0441\u043a\u0430\u044f \u0426\u0420\u0411", None))
        self.comboBox_referring_health_facility.setItemText(9, QCoreApplication.translate("PatientPassportData", u"\u0411\u0430\u0440\u0434\u044b\u043c\u0441\u043a\u0430\u044f \u0426\u0420\u0411", None))
        self.comboBox_referring_health_facility.setItemText(10, QCoreApplication.translate("PatientPassportData", u"\u041e\u0440\u0434\u0438\u043d\u0441\u043a\u0430\u044f \u0426\u0420\u0411", None))

        self.labelPassportData_2.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430</p></body></html>", None))
        self.comboBoxGender.setItemText(0, QCoreApplication.translate("PatientPassportData", u"\u041c\u0443\u0436\u0441\u043a\u043e\u0439", None))
        self.comboBoxGender.setItemText(1, QCoreApplication.translate("PatientPassportData", u"\u0416\u0435\u043d\u0441\u043a\u0438\u0439", None))

        self.checkBoxPtLeftHanded.setText(QCoreApplication.translate("PatientPassportData", u"\u041b\u0435\u0432\u0448\u0430", None))
        self.labelNewPatient.setText(QCoreApplication.translate("PatientPassportData", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u0438\u0441\u0442\u043e\u0440\u0438\u0438 \u0431\u043e\u043b\u0435\u0437\u043d\u0438", None))
        self.label_unic_number.setText("")
        self.labelPassportData_3.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438</p></body></html>", None))
        self.dateEditPtBirthDay.setDisplayFormat(QCoreApplication.translate("PatientPassportData", u"dd.MM.yyyy", None))
        self.comboBoxPtHoptitalisationType.setItemText(0, QCoreApplication.translate("PatientPassportData", u"\u041a\u0440\u0443\u0433\u043b\u043e\u0441\u0443\u0442\u043e\u0447\u043d\u044b\u0439 \u0441\u0442\u0430\u0446\u0438\u043e\u043d\u0430\u0440", None))
        self.comboBoxPtHoptitalisationType.setItemText(1, QCoreApplication.translate("PatientPassportData", u"\u0414\u043d\u0435\u0432\u043d\u043e\u0439 \u0441\u0442\u0430\u0446\u0438\u043e\u043d\u0430\u0440", None))

        self.comboBoxPtRoomNumber.setItemText(0, "")
        self.comboBoxPtRoomNumber.setItemText(1, QCoreApplication.translate("PatientPassportData", u"201", None))
        self.comboBoxPtRoomNumber.setItemText(2, QCoreApplication.translate("PatientPassportData", u"202", None))
        self.comboBoxPtRoomNumber.setItemText(3, QCoreApplication.translate("PatientPassportData", u"204", None))
        self.comboBoxPtRoomNumber.setItemText(4, QCoreApplication.translate("PatientPassportData", u"205", None))
        self.comboBoxPtRoomNumber.setItemText(5, QCoreApplication.translate("PatientPassportData", u"206", None))
        self.comboBoxPtRoomNumber.setItemText(6, QCoreApplication.translate("PatientPassportData", u"208", None))
        self.comboBoxPtRoomNumber.setItemText(7, QCoreApplication.translate("PatientPassportData", u"209", None))
        self.comboBoxPtRoomNumber.setItemText(8, QCoreApplication.translate("PatientPassportData", u"210", None))
        self.comboBoxPtRoomNumber.setItemText(9, QCoreApplication.translate("PatientPassportData", u"211", None))
        self.comboBoxPtRoomNumber.setItemText(10, QCoreApplication.translate("PatientPassportData", u"212", None))
        self.comboBoxPtRoomNumber.setItemText(11, QCoreApplication.translate("PatientPassportData", u"213", None))
        self.comboBoxPtRoomNumber.setItemText(12, QCoreApplication.translate("PatientPassportData", u"301", None))
        self.comboBoxPtRoomNumber.setItemText(13, QCoreApplication.translate("PatientPassportData", u"302", None))
        self.comboBoxPtRoomNumber.setItemText(14, QCoreApplication.translate("PatientPassportData", u"303", None))
        self.comboBoxPtRoomNumber.setItemText(15, QCoreApplication.translate("PatientPassportData", u"304", None))
        self.comboBoxPtRoomNumber.setItemText(16, QCoreApplication.translate("PatientPassportData", u"305", None))
        self.comboBoxPtRoomNumber.setItemText(17, QCoreApplication.translate("PatientPassportData", u"306", None))
        self.comboBoxPtRoomNumber.setItemText(18, QCoreApplication.translate("PatientPassportData", u"307", None))
        self.comboBoxPtRoomNumber.setItemText(19, QCoreApplication.translate("PatientPassportData", u"308", None))
        self.comboBoxPtRoomNumber.setItemText(20, QCoreApplication.translate("PatientPassportData", u"308A", None))
        self.comboBoxPtRoomNumber.setItemText(21, QCoreApplication.translate("PatientPassportData", u"309", None))
        self.comboBoxPtRoomNumber.setItemText(22, QCoreApplication.translate("PatientPassportData", u"310", None))
        self.comboBoxPtRoomNumber.setItemText(23, QCoreApplication.translate("PatientPassportData", u"311", None))
        self.comboBoxPtRoomNumber.setItemText(24, QCoreApplication.translate("PatientPassportData", u"312", None))
        self.comboBoxPtRoomNumber.setItemText(25, QCoreApplication.translate("PatientPassportData", u"313", None))
        self.comboBoxPtRoomNumber.setItemText(26, QCoreApplication.translate("PatientPassportData", u"315", None))

        self.plainTextEdit_descriptions.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("PatientPassportData", u"World\n"
"of\n"
"Medicine", None))
        self.help_page.setText(QCoreApplication.translate("PatientPassportData", u"help", None))
        self.pushButtonBackToMenu.setText(QCoreApplication.translate("PatientPassportData", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.pushButtonAddRelative.setText(QCoreApplication.translate("PatientPassportData", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c\n"
"\u0440\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u043e\u0432", None))
        self.pushButtonPrintConsent.setText(QCoreApplication.translate("PatientPassportData", u"\u041d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c\n"
"\u0432\u0441\u0435 \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u044f", None))
        self.pushButtonCreateHistory.setText(QCoreApplication.translate("PatientPassportData", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c\n"
"\u0438\u0441\u0442\u043e\u0440\u0438\u044e\n"
"\u0431\u043e\u043b\u0435\u0437\u043d\u0438", None))
    # retranslateUi

