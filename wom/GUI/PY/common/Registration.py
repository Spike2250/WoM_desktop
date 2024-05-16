# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registration.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from wom.GUI.widgets.my_pushButton import PushButton

class Ui_Registration(object):
    def setupUi(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(810, 523)
        Registration.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_5 = QVBoxLayout(Registration)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(Registration)
        self.main.setObjectName(u"main")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main_frame = QFrame(self.main)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_frame = QFrame(self.main_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMaximumSize(QSize(16777215, 100))
        self.logo_frame.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_3 = QGridLayout(self.logo_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(0)
        self.labelLogo = QLabel(self.logo_frame)
        self.labelLogo.setObjectName(u"labelLogo")
        palette = QPalette()
        brush = QBrush(QColor(112, 38, 50, 190))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(12, 94, 200, 255))
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
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(133, 174, 227, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush10 = QBrush(QColor(112, 38, 50, 95))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.labelLogo.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        font.setBold(False)
        self.labelLogo.setFont(font)
        self.labelLogo.setStyleSheet(u"background-color: none;\n"
"color: rgba(112, 38, 50, 190);")

        self.gridLayout_3.addWidget(self.labelLogo, 0, 0, 2, 1)


        self.verticalLayout.addWidget(self.logo_frame)

        self.frame_user_data = QFrame(self.main_frame)
        self.frame_user_data.setObjectName(u"frame_user_data")
        self.frame_user_data.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.frame_user_data)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_user_data)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(800, 0))
        self.frame.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.checkBox_login_same_email = QCheckBox(self.frame)
        self.checkBox_login_same_email.setObjectName(u"checkBox_login_same_email")
        self.checkBox_login_same_email.setEnabled(True)
        palette1 = QPalette()
        brush11 = QBrush(QColor(50, 98, 115, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        brush12 = QBrush(QColor(217, 217, 217, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush6)
        brush13 = QBrush(QColor(236, 236, 236, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(108, 108, 108, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(145, 145, 145, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        brush16 = QBrush(QColor(50, 98, 115, 128))
        brush16.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        brush17 = QBrush(QColor(238, 238, 238, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        brush18 = QBrush(QColor(238, 238, 238, 128))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.checkBox_login_same_email.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(8)
        font1.setBold(False)
        self.checkBox_login_same_email.setFont(font1)
        self.checkBox_login_same_email.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"	font-size: 8pt;\n"
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
        self.checkBox_login_same_email.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox_login_same_email)

        self.user_login = QLineEdit(self.frame)
        self.user_login.setObjectName(u"user_login")
        self.user_login.setEnabled(False)
        self.user_login.setMinimumSize(QSize(0, 0))
        self.user_login.setStyleSheet(u"QLineEdit {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"}\n"
"QLineEdit::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.verticalLayout_4.addWidget(self.user_login)


        self.gridLayout.addLayout(self.verticalLayout_4, 5, 1, 1, 1)

        self.label_check_email = QLabel(self.frame)
        self.label_check_email.setObjectName(u"label_check_email")
        self.label_check_email.setMinimumSize(QSize(22, 0))
        self.label_check_email.setMaximumSize(QSize(22, 16777215))
        self.label_check_email.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")
        self.label_check_email.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_check_email, 2, 2, 1, 1)

        self.pushButton_verify_phone_2 = PushButton(self.frame)
        self.pushButton_verify_phone_2.setObjectName(u"pushButton_verify_phone_2")
        self.pushButton_verify_phone_2.setEnabled(False)
        self.pushButton_verify_phone_2.setMinimumSize(QSize(0, 0))
        self.pushButton_verify_phone_2.setMaximumSize(QSize(120, 20))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush19 = QBrush(QColor(50, 98, 115, 190))
        brush19.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush20 = QBrush(QColor(255, 255, 255, 128))
        brush20.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        brush21 = QBrush(QColor(50, 98, 115, 150))
        brush21.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        brush22 = QBrush(QColor(50, 98, 115, 40))
        brush22.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        brush23 = QBrush(QColor(50, 98, 115, 75))
        brush23.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush23)
#endif
        self.pushButton_verify_phone_2.setPalette(palette2)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(7)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton_verify_phone_2.setFont(font2)
        self.pushButton_verify_phone_2.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_verify_phone_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 7pt;\n"
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

        self.gridLayout.addWidget(self.pushButton_verify_phone_2, 4, 3, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 4)

        self.pushButton_verify_phone = PushButton(self.frame)
        self.pushButton_verify_phone.setObjectName(u"pushButton_verify_phone")
        self.pushButton_verify_phone.setEnabled(False)
        self.pushButton_verify_phone.setMinimumSize(QSize(0, 0))
        self.pushButton_verify_phone.setMaximumSize(QSize(16777215, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush22)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush22)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush22)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush23)
#endif
        self.pushButton_verify_phone.setPalette(palette3)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.pushButton_verify_phone.setFont(font3)
        self.pushButton_verify_phone.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_verify_phone.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_verify_phone, 4, 1, 1, 1)

        self.user_surname = QLineEdit(self.frame)
        self.user_surname.setObjectName(u"user_surname")
        self.user_surname.setMinimumSize(QSize(0, 0))
        self.user_surname.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_surname, 10, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)

        self.label_check_login = QLabel(self.frame)
        self.label_check_login.setObjectName(u"label_check_login")
        self.label_check_login.setMinimumSize(QSize(22, 0))
        self.label_check_login.setMaximumSize(QSize(22, 22))
        self.label_check_login.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")
        self.label_check_login.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_check_login, 5, 2, 1, 1)

        self.label_check_password = QLabel(self.frame)
        self.label_check_password.setObjectName(u"label_check_password")
        self.label_check_password.setMinimumSize(QSize(22, 0))
        self.label_check_password.setMaximumSize(QSize(22, 16777215))
        self.label_check_password.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")
        self.label_check_password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_check_password, 7, 2, 1, 1)

        self.label_check_password_repeat = QLabel(self.frame)
        self.label_check_password_repeat.setObjectName(u"label_check_password_repeat")
        self.label_check_password_repeat.setMinimumSize(QSize(22, 0))
        self.label_check_password_repeat.setMaximumSize(QSize(22, 16777215))
        self.label_check_password_repeat.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")
        self.label_check_password_repeat.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_check_password_repeat, 8, 2, 1, 1)

        self.user_password = QLineEdit(self.frame)
        self.user_password.setObjectName(u"user_password")
        self.user_password.setMinimumSize(QSize(0, 0))
        self.user_password.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_password, 7, 1, 1, 1)

        self.user_password_2 = QLineEdit(self.frame)
        self.user_password_2.setObjectName(u"user_password_2")
        self.user_password_2.setMinimumSize(QSize(0, 0))
        self.user_password_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_password_2, 8, 1, 1, 1)

        self.user_name = QLineEdit(self.frame)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setMinimumSize(QSize(0, 0))
        self.user_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_name, 11, 1, 1, 1)

        self.label_check_name = QLabel(self.frame)
        self.label_check_name.setObjectName(u"label_check_name")
        self.label_check_name.setMinimumSize(QSize(22, 0))
        self.label_check_name.setMaximumSize(QSize(22, 16777215))
        self.label_check_name.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")
        self.label_check_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_check_name, 11, 2, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)

        self.pushButton_reg = QPushButton(self.frame)
        self.pushButton_reg.setObjectName(u"pushButton_reg")
        self.pushButton_reg.setMinimumSize(QSize(0, 26))
        self.pushButton_reg.setMaximumSize(QSize(16777215, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush19)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush19)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush19)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush20)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush19)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush19)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush22)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush21)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush22)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush22)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush23)
#endif
        self.pushButton_reg.setPalette(palette4)
        self.pushButton_reg.setFont(font3)
        self.pushButton_reg.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_reg.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_reg, 14, 0, 1, 4)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 12, 0, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_check_phone = QLabel(self.frame)
        self.label_check_phone.setObjectName(u"label_check_phone")
        self.label_check_phone.setMinimumSize(QSize(22, 0))
        self.label_check_phone.setMaximumSize(QSize(22, 16777215))
        self.label_check_phone.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")
        self.label_check_phone.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_check_phone, 3, 2, 1, 1)

        self.user_dadname = QLineEdit(self.frame)
        self.user_dadname.setObjectName(u"user_dadname")
        self.user_dadname.setMinimumSize(QSize(0, 0))
        self.user_dadname.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_dadname, 12, 1, 1, 1)

        self.phone_cheking_code = QLineEdit(self.frame)
        self.phone_cheking_code.setObjectName(u"phone_cheking_code")
        self.phone_cheking_code.setEnabled(False)
        self.phone_cheking_code.setMinimumSize(QSize(0, 0))
        self.phone_cheking_code.setMaximumSize(QSize(120, 16777215))
        self.phone_cheking_code.setStyleSheet(u"QLineEdit {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"}\n"
"QLineEdit::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout.addWidget(self.phone_cheking_code, 3, 3, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 13, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)

        self.label_check_surname = QLabel(self.frame)
        self.label_check_surname.setObjectName(u"label_check_surname")
        self.label_check_surname.setMinimumSize(QSize(22, 0))
        self.label_check_surname.setMaximumSize(QSize(22, 16777215))
        self.label_check_surname.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"border: none;")
        self.label_check_surname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_check_surname, 10, 2, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.dateEdit_user_bday = QDateEdit(self.frame)
        self.dateEdit_user_bday.setObjectName(u"dateEdit_user_bday")
        self.dateEdit_user_bday.setEnabled(True)
        self.dateEdit_user_bday.setMinimumSize(QSize(0, 0))
        self.dateEdit_user_bday.setStyleSheet(u"QDateEdit {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"}\n"
"QDateEdit::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout.addWidget(self.dateEdit_user_bday, 13, 1, 1, 1)

        self.user_phone = QLineEdit(self.frame)
        self.user_phone.setObjectName(u"user_phone")
        self.user_phone.setMinimumSize(QSize(0, 0))
        self.user_phone.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_phone, 3, 1, 1, 1)

        self.user_email = QLineEdit(self.frame)
        self.user_email.setObjectName(u"user_email")
        self.user_email.setMinimumSize(QSize(0, 0))
        self.user_email.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_email, 2, 1, 1, 1)

        self.labelLogo_3 = QLabel(self.frame)
        self.labelLogo_3.setObjectName(u"labelLogo_3")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush24 = QBrush(QColor(112, 38, 50, 40))
        brush24.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush24)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush24)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush24)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush24)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush24)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush24)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush24)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush24)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush24)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.labelLogo_3.setPalette(palette5)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.labelLogo_3.setFont(font4)
        self.labelLogo_3.setStyleSheet(u"background-color: rgba(112, 38, 50, 40);\n"
"border: none;\n"
"color: rgba(112, 38, 50, 190);\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.labelLogo_3, 0, 0, 1, 4)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 9, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_user_data)

        self.logs_frame = QFrame(self.main_frame)
        self.logs_frame.setObjectName(u"logs_frame")
        self.logs_frame.setMaximumSize(QSize(16777215, 70))
        self.logs_frame.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.logs_frame.setFrameShape(QFrame.HLine)
        self.horizontalLayout_6 = QHBoxLayout(self.logs_frame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_status = QLabel(self.logs_frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(0, 50))
        self.label_status.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_status.setFont(font5)
        self.label_status.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"")
        self.label_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_status)


        self.verticalLayout.addWidget(self.logs_frame)


        self.horizontalLayout.addWidget(self.main_frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.main)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Form", None))
        self.labelLogo.setText(QCoreApplication.translate("Registration", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">World of Medicine</span></p></body></html>", None))
        self.checkBox_login_same_email.setText(QCoreApplication.translate("Registration", u"\u0441\u043e\u0432\u043f\u0430\u0434\u0430\u0435\u0442 \u0441 e-mail", None))
        self.label_check_email.setText("")
        self.pushButton_verify_phone_2.setText(QCoreApplication.translate("Registration", u"\u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u0434\n"
"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Registration", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_9.setText(QCoreApplication.translate("Registration", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.pushButton_verify_phone.setText(QCoreApplication.translate("Registration", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.label_11.setText(QCoreApplication.translate("Registration", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_check_login.setText("")
        self.label_check_password.setText("")
        self.label_check_password_repeat.setText("")
        self.label_check_name.setText("")
        self.label_12.setText(QCoreApplication.translate("Registration", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_reg.setText(QCoreApplication.translate("Registration", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.label_8.setText(QCoreApplication.translate("Registration", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_14.setText(QCoreApplication.translate("Registration", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_13.setText(QCoreApplication.translate("Registration", u"E-mail", None))
        self.label_check_phone.setText("")
        self.label_15.setText(QCoreApplication.translate("Registration", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Registration", u"\u0418\u043c\u044f", None))
        self.label_check_surname.setText("")
        self.label.setText(QCoreApplication.translate("Registration", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.labelLogo_3.setText(QCoreApplication.translate("Registration", u"<html><head/><body><p align=\"center\">\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</p></body></html>", None))
        self.label_status.setText(QCoreApplication.translate("Registration", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

