# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatientPassportData.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc

class Ui_PatientPassportData(object):
    def setupUi(self, PatientPassportData):
        if not PatientPassportData.objectName():
            PatientPassportData.setObjectName(u"PatientPassportData")
        PatientPassportData.resize(1107, 406)
        PatientPassportData.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout = QVBoxLayout(PatientPassportData)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(PatientPassportData)
        self.main.setObjectName(u"main")
        self.gridLayout_2 = QGridLayout(self.main)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.passport_data = QFrame(self.main)
        self.passport_data.setObjectName(u"passport_data")
        self.passport_data.setMinimumSize(QSize(950, 0))
        self.passport_data.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"border: 1px solid  rgba(50, 98, 115, 255);")
        self.gridLayout = QGridLayout(self.passport_data)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.snils = QLineEdit(self.passport_data)
        self.snils.setObjectName(u"snils")
        palette = QPalette()
        brush = QBrush(QColor(19, 36, 43, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(238, 238, 238, 255))
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
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(19, 36, 43, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(217, 217, 217, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.snils.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(True)
        self.snils.setFont(font)
        self.snils.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.snils, 14, 1, 1, 1)

        self.dadname = QLineEdit(self.passport_data)
        self.dadname.setObjectName(u"dadname")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.dadname.setPalette(palette1)
        self.dadname.setFont(font)
        self.dadname.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.dadname, 3, 1, 1, 1)

        self.labelPtBirthDay = QLabel(self.passport_data)
        self.labelPtBirthDay.setObjectName(u"labelPtBirthDay")
        palette2 = QPalette()
        brush8 = QBrush(QColor(50, 98, 115, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        brush9 = QBrush(QColor(0, 0, 0, 0))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush9)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush11 = QBrush(QColor(255, 255, 220, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush12 = QBrush(QColor(50, 98, 115, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtBirthDay.setPalette(palette2)
        self.labelPtBirthDay.setFont(font)
        self.labelPtBirthDay.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtBirthDay, 4, 0, 1, 1)

        self.dateEdit_birthday = QDateEdit(self.passport_data)
        self.dateEdit_birthday.setObjectName(u"dateEdit_birthday")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.dateEdit_birthday.setPalette(palette3)
        self.dateEdit_birthday.setFont(font)
        self.dateEdit_birthday.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.dateEdit_birthday, 4, 1, 1, 1)

        self.name = QLineEdit(self.passport_data)
        self.name.setObjectName(u"name")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.name.setPalette(palette4)
        self.name.setFont(font)
        self.name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.name, 2, 1, 1, 1)

        self.passport = QLineEdit(self.passport_data)
        self.passport.setObjectName(u"passport")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.passport.setPalette(palette5)
        self.passport.setFont(font)
        self.passport.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.passport, 12, 1, 1, 1)

        self.checkBox_signature_cant = QCheckBox(self.passport_data)
        self.checkBox_signature_cant.setObjectName(u"checkBox_signature_cant")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(238, 238, 238, 255))
        gradient.setColorAt(1, QColor(190, 190, 190, 255))
        brush13 = QBrush(gradient)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        gradient1 = QLinearGradient(0, 0, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(238, 238, 238, 255))
        gradient1.setColorAt(1, QColor(190, 190, 190, 255))
        brush14 = QBrush(gradient1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush14)
        gradient2 = QLinearGradient(0, 0, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(238, 238, 238, 255))
        gradient2.setColorAt(1, QColor(190, 190, 190, 255))
        brush15 = QBrush(gradient2)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        gradient3 = QLinearGradient(0, 0, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(238, 238, 238, 255))
        gradient3.setColorAt(1, QColor(190, 190, 190, 255))
        brush16 = QBrush(gradient3)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        gradient4 = QLinearGradient(0, 0, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(238, 238, 238, 255))
        gradient4.setColorAt(1, QColor(190, 190, 190, 255))
        brush17 = QBrush(gradient4)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        gradient5 = QLinearGradient(0, 0, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(238, 238, 238, 255))
        gradient5.setColorAt(1, QColor(190, 190, 190, 255))
        brush18 = QBrush(gradient5)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush18)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        gradient6 = QLinearGradient(0, 0, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(238, 238, 238, 255))
        gradient6.setColorAt(1, QColor(190, 190, 190, 255))
        brush19 = QBrush(gradient6)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        gradient7 = QLinearGradient(0, 0, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(238, 238, 238, 255))
        gradient7.setColorAt(1, QColor(190, 190, 190, 255))
        brush20 = QBrush(gradient7)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        gradient8 = QLinearGradient(0, 0, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(238, 238, 238, 255))
        gradient8.setColorAt(1, QColor(190, 190, 190, 255))
        brush21 = QBrush(gradient8)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush21)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.checkBox_signature_cant.setPalette(palette6)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.checkBox_signature_cant.setFont(font1)
        self.checkBox_signature_cant.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout.addWidget(self.checkBox_signature_cant, 8, 1, 1, 1)

        self.polis_oms = QLineEdit(self.passport_data)
        self.polis_oms.setObjectName(u"polis_oms")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.polis_oms.setPalette(palette7)
        self.polis_oms.setFont(font)
        self.polis_oms.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.polis_oms, 13, 1, 1, 1)

        self.labelPtSurName = QLabel(self.passport_data)
        self.labelPtSurName.setObjectName(u"labelPtSurName")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSurName.setPalette(palette8)
        self.labelPtSurName.setFont(font)
        self.labelPtSurName.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtSurName, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 9, 1, 1, 1)

        self.adress = QLineEdit(self.passport_data)
        self.adress.setObjectName(u"adress")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.adress.setPalette(palette9)
        self.adress.setFont(font)
        self.adress.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.adress, 5, 1, 1, 1)

        self.labelPtAdress = QLabel(self.passport_data)
        self.labelPtAdress.setObjectName(u"labelPtAdress")
        self.labelPtAdress.setMinimumSize(QSize(200, 0))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtAdress.setPalette(palette10)
        self.labelPtAdress.setFont(font)
        self.labelPtAdress.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtAdress, 5, 0, 1, 1)

        self.labelPtOms = QLabel(self.passport_data)
        self.labelPtOms.setObjectName(u"labelPtOms")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtOms.setPalette(palette11)
        self.labelPtOms.setFont(font)
        self.labelPtOms.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtOms, 13, 0, 1, 1)

        self.phone = QLineEdit(self.passport_data)
        self.phone.setObjectName(u"phone")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.phone.setPalette(palette12)
        self.phone.setFont(font)
        self.phone.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.phone, 10, 1, 1, 1)

        self.surname = QLineEdit(self.passport_data)
        self.surname.setObjectName(u"surname")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.surname.setPalette(palette13)
        self.surname.setFont(font)
        self.surname.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.surname, 1, 1, 1, 1)

        self.labelPtEmail = QLabel(self.passport_data)
        self.labelPtEmail.setObjectName(u"labelPtEmail")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtEmail.setPalette(palette14)
        self.labelPtEmail.setFont(font)
        self.labelPtEmail.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtEmail, 11, 0, 1, 1)

        self.labelPtPhone = QLabel(self.passport_data)
        self.labelPtPhone.setObjectName(u"labelPtPhone")
        self.labelPtPhone.setMinimumSize(QSize(200, 0))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtPhone.setPalette(palette15)
        self.labelPtPhone.setFont(font)
        self.labelPtPhone.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtPhone, 10, 0, 1, 1)

        self.email = QLineEdit(self.passport_data)
        self.email.setObjectName(u"email")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.email.setPalette(palette16)
        self.email.setFont(font)
        self.email.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.email, 11, 1, 1, 1)

        self.labelPtName = QLabel(self.passport_data)
        self.labelPtName.setObjectName(u"labelPtName")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtName.setPalette(palette17)
        self.labelPtName.setFont(font)
        self.labelPtName.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtName, 2, 0, 1, 1)

        self.labelPtSNILS = QLabel(self.passport_data)
        self.labelPtSNILS.setObjectName(u"labelPtSNILS")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSNILS.setPalette(palette18)
        self.labelPtSNILS.setFont(font)
        self.labelPtSNILS.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtSNILS, 14, 0, 1, 1)

        self.labelPtPassport = QLabel(self.passport_data)
        self.labelPtPassport.setObjectName(u"labelPtPassport")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette19.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette19.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette19.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette19.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette19.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette19.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtPassport.setPalette(palette19)
        self.labelPtPassport.setFont(font)
        self.labelPtPassport.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtPassport, 12, 0, 1, 1)

        self.labelPtGender = QLabel(self.passport_data)
        self.labelPtGender.setObjectName(u"labelPtGender")
        self.labelPtGender.setMaximumSize(QSize(16777215, 16777215))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette20.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtGender.setPalette(palette20)
        self.labelPtGender.setFont(font)
        self.labelPtGender.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtGender, 6, 0, 1, 1)

        self.labelPtDadName = QLabel(self.passport_data)
        self.labelPtDadName.setObjectName(u"labelPtDadName")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette21.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette21.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette21.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette21.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette21.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette21.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtDadName.setPalette(palette21)
        self.labelPtDadName.setFont(font)
        self.labelPtDadName.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.labelPtDadName, 3, 0, 1, 1)

        self.checkBoxPtLeftHanded = QCheckBox(self.passport_data)
        self.checkBoxPtLeftHanded.setObjectName(u"checkBoxPtLeftHanded")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        brush22 = QBrush(QColor(238, 238, 238, 128))
        brush22.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.checkBoxPtLeftHanded.setPalette(palette22)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(False)
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

        self.gridLayout.addWidget(self.checkBoxPtLeftHanded, 7, 1, 1, 1)

        self.comboBox_gender = QComboBox(self.passport_data)
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.setObjectName(u"comboBox_gender")
        self.comboBox_gender.setMaximumSize(QSize(16777215, 16777215))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush23 = QBrush(QColor(237, 237, 237, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush23)
        brush24 = QBrush(QColor(110, 110, 110, 255))
        brush24.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush24)
        brush25 = QBrush(QColor(147, 147, 147, 255))
        brush25.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush25)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush23)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush23)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush24)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush25)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush23)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush23)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush24)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush25)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush26 = QBrush(QColor(220, 220, 220, 255))
        brush26.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBox_gender.setPalette(palette23)
        self.comboBox_gender.setFont(font)
        self.comboBox_gender.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBox_gender, 6, 1, 1, 1)


        self.gridLayout_2.addWidget(self.passport_data, 1, 1, 1, 1)

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
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush27 = QBrush(QColor(50, 98, 115, 190))
        brush27.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush27)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette24.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush27)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush27)
        palette24.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush28 = QBrush(QColor(255, 255, 255, 128))
        brush28.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush27)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush27)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush27)
        palette24.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        brush29 = QBrush(QColor(50, 98, 115, 150))
        brush29.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush29)
        brush30 = QBrush(QColor(50, 98, 115, 40))
        brush30.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush30)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush29)
        palette24.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush29)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush30)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush30)
        palette24.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
        brush31 = QBrush(QColor(50, 98, 115, 75))
        brush31.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
#endif
        self.pushButtonHelp.setPalette(palette24)
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

        self.pushButtonPrintConsent = QPushButton(self.groupBox_wom)
        self.pushButtonPrintConsent.setObjectName(u"pushButtonPrintConsent")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush27)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette25.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush27)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush27)
        palette25.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush27)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush27)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush27)
        palette25.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush29)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush30)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush29)
        palette25.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush29)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush30)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush30)
        palette25.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
#endif
        self.pushButtonPrintConsent.setPalette(palette25)
        self.pushButtonPrintConsent.setFont(font2)
        self.pushButtonPrintConsent.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_6.addWidget(self.pushButtonPrintConsent)

        self.pushButtonAddRelative = QPushButton(self.groupBox_wom)
        self.pushButtonAddRelative.setObjectName(u"pushButtonAddRelative")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush27)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette26.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush27)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush27)
        palette26.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush27)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush27)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush27)
        palette26.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush29)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush30)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush29)
        palette26.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush29)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush30)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush30)
        palette26.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
#endif
        self.pushButtonAddRelative.setPalette(palette26)
        self.pushButtonAddRelative.setFont(font2)
        self.pushButtonAddRelative.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_6.addWidget(self.pushButtonAddRelative)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.pushButtonNotSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush27)
        palette27.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Midlight, brush23)
        palette27.setBrush(QPalette.Active, QPalette.Dark, brush24)
        palette27.setBrush(QPalette.Active, QPalette.Mid, brush25)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette27.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush27)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush27)
        palette27.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette27.setBrush(QPalette.Active, QPalette.AlternateBase, brush23)
        palette27.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette27.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush27)
        palette27.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Midlight, brush23)
        palette27.setBrush(QPalette.Inactive, QPalette.Dark, brush24)
        palette27.setBrush(QPalette.Inactive, QPalette.Mid, brush25)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush27)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush27)
        palette27.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette27.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush23)
        palette27.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette27.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Midlight, brush23)
        palette27.setBrush(QPalette.Disabled, QPalette.Dark, brush24)
        palette27.setBrush(QPalette.Disabled, QPalette.Mid, brush25)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette27.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
        palette27.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette27.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
#endif
        self.pushButtonNotSaveExit.setPalette(palette27)
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
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush32 = QBrush(QColor(92, 158, 173, 255))
        brush32.setStyle(Qt.SolidPattern)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush32)
        palette28.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Active, QPalette.Midlight, brush23)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush24)
        palette28.setBrush(QPalette.Active, QPalette.Mid, brush25)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette28.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush32)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush32)
        palette28.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Active, QPalette.AlternateBase, brush23)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush32)
        palette28.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.Midlight, brush23)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush24)
        palette28.setBrush(QPalette.Inactive, QPalette.Mid, brush25)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush32)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush32)
        palette28.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush23)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette28.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.Midlight, brush23)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush24)
        palette28.setBrush(QPalette.Disabled, QPalette.Mid, brush25)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette28.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush26)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
#endif
        self.pushButtonSaveExit.setPalette(palette28)
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


        self.gridLayout_2.addWidget(self.groupBox_wom, 0, 3, 3, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelPassportData_2 = QLabel(self.main)
        self.labelPassportData_2.setObjectName(u"labelPassportData_2")
        self.labelPassportData_2.setMaximumSize(QSize(50, 50))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush33 = QBrush(QColor(92, 158, 173, 200))
        brush33.setStyle(Qt.SolidPattern)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush33)
        palette29.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette29.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush33)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush33)
        palette29.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette29.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette29.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette29.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush33)
        palette29.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush33)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush33)
        palette29.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette29.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette29.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush33)
        palette29.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush33)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush33)
        palette29.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette29.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette29.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette29.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
#endif
        self.labelPassportData_2.setPalette(palette29)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.labelPassportData_2.setFont(font3)
        self.labelPassportData_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(92, 158, 173, 200);\n"
"border: none;")
        self.labelPassportData_2.setPixmap(QPixmap(u":/icon/icons/account_box_white_36dp.svg"))
        self.labelPassportData_2.setScaledContents(False)
        self.labelPassportData_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelPassportData_2)

        self.labelPassportData = QLabel(self.main)
        self.labelPassportData.setObjectName(u"labelPassportData")
        self.labelPassportData.setMinimumSize(QSize(650, 0))
        self.labelPassportData.setMaximumSize(QSize(16777215, 50))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush34 = QBrush(QColor(112, 38, 50, 150))
        brush34.setStyle(Qt.SolidPattern)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush34)
        palette30.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette30.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush34)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush34)
        palette30.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush28)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush34)
        palette30.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush34)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush34)
        palette30.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush34)
        palette30.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush34)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush34)
        palette30.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
#endif
        self.labelPassportData.setPalette(palette30)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.labelPassportData.setFont(font4)
        self.labelPassportData.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.labelPassportData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelPassportData)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 3)


        self.verticalLayout.addWidget(self.main)

        QWidget.setTabOrder(self.surname, self.name)
        QWidget.setTabOrder(self.name, self.dadname)
        QWidget.setTabOrder(self.dadname, self.dateEdit_birthday)
        QWidget.setTabOrder(self.dateEdit_birthday, self.adress)
        QWidget.setTabOrder(self.adress, self.comboBox_gender)
        QWidget.setTabOrder(self.comboBox_gender, self.checkBoxPtLeftHanded)
        QWidget.setTabOrder(self.checkBoxPtLeftHanded, self.checkBox_signature_cant)
        QWidget.setTabOrder(self.checkBox_signature_cant, self.phone)
        QWidget.setTabOrder(self.phone, self.email)
        QWidget.setTabOrder(self.email, self.passport)
        QWidget.setTabOrder(self.passport, self.polis_oms)
        QWidget.setTabOrder(self.polis_oms, self.snils)
        QWidget.setTabOrder(self.snils, self.pushButtonPrintConsent)
        QWidget.setTabOrder(self.pushButtonPrintConsent, self.pushButtonAddRelative)
        QWidget.setTabOrder(self.pushButtonAddRelative, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.pushButtonNotSaveExit)
        QWidget.setTabOrder(self.pushButtonNotSaveExit, self.pushButtonHelp)

        self.retranslateUi(PatientPassportData)

        QMetaObject.connectSlotsByName(PatientPassportData)
    # setupUi

    def retranslateUi(self, PatientPassportData):
        PatientPassportData.setWindowTitle(QCoreApplication.translate("PatientPassportData", u"Form", None))
        self.labelPtBirthDay.setText(QCoreApplication.translate("PatientPassportData", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.dateEdit_birthday.setDisplayFormat(QCoreApplication.translate("PatientPassportData", u"dd.MM.yyyy", None))
        self.checkBox_signature_cant.setText(QCoreApplication.translate("PatientPassportData", u"\u043f\u0430\u0446\u0438\u0435\u043d\u0442 \u041d\u0415 \u041c\u041e\u0416\u0415\u0422 \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0434\u043f\u0438\u0441\u044c", None))
        self.labelPtSurName.setText(QCoreApplication.translate("PatientPassportData", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.labelPtAdress.setText(QCoreApplication.translate("PatientPassportData", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u0430\u0434\u0440\u0435\u0441:", None))
        self.labelPtOms.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u043e\u043b\u0438\u0441 \u041e\u041c\u0421 (\u043d\u043e\u043c\u0435\u0440):", None))
        self.labelPtEmail.setText(QCoreApplication.translate("PatientPassportData", u"E-mail:", None))
        self.labelPtPhone.setText(QCoreApplication.translate("PatientPassportData", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.labelPtName.setText(QCoreApplication.translate("PatientPassportData", u"\u0418\u043c\u044f:", None))
        self.labelPtSNILS.setText(QCoreApplication.translate("PatientPassportData", u"\u0421\u041d\u0418\u041b\u0421 (\u043d\u043e\u043c\u0435\u0440):", None))
        self.labelPtPassport.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442 (\u0441\u0435\u0440\u0438\u044f, \u043d\u043e\u043c\u0435\u0440): ", None))
        self.labelPtGender.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u043e\u043b:", None))
        self.labelPtDadName.setText(QCoreApplication.translate("PatientPassportData", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.checkBoxPtLeftHanded.setText(QCoreApplication.translate("PatientPassportData", u"\u041b\u0435\u0432\u0448\u0430", None))
        self.comboBox_gender.setItemText(0, QCoreApplication.translate("PatientPassportData", u"\u041c\u0443\u0436\u0441\u043a\u043e\u0439", None))
        self.comboBox_gender.setItemText(1, QCoreApplication.translate("PatientPassportData", u"\u0416\u0435\u043d\u0441\u043a\u0438\u0439", None))

        self.groupBox_wom.setTitle(QCoreApplication.translate("PatientPassportData", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("PatientPassportData", u"Help", None))
        self.pushButtonPrintConsent.setText(QCoreApplication.translate("PatientPassportData", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0432\u0441\u0435\u0445\n"
"\u0441\u043e\u0433\u043b\u0430\u0441\u0438\u0439", None))
        self.pushButtonAddRelative.setText(QCoreApplication.translate("PatientPassportData", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c\n"
"\u0440\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u043e\u0432", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("PatientPassportData", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("PatientPassportData", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.labelPassportData_2.setText("")
        self.labelPassportData.setText(QCoreApplication.translate("PatientPassportData", u"<html><head/><body><p>\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430</p></body></html>", None))
    # retranslateUi

