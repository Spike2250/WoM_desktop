# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(512, 560)
        Login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_3 = QVBoxLayout(Login)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.full_frame = QFrame(Login)
        self.full_frame.setObjectName(u"full_frame")
        self.full_frame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.full_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo_frame = QFrame(self.full_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMaximumSize(QSize(16777215, 100))
        self.logo_frame.setStyleSheet(u"")
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


        self.verticalLayout_2.addWidget(self.logo_frame)

        self.frame_login = QFrame(self.full_frame)
        self.frame_login.setObjectName(u"frame_login")
        self.horizontalLayout = QHBoxLayout(self.frame_login)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame_login_wom = QFrame(self.frame_login)
        self.frame_login_wom.setObjectName(u"frame_login_wom")
        self.frame_login_wom.setMaximumSize(QSize(550, 16777215))
        self.frame_login_wom.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.frame_login_wom)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hello_frame = QFrame(self.frame_login_wom)
        self.hello_frame.setObjectName(u"hello_frame")
        self.hello_frame.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.horizontalLayout_7 = QHBoxLayout(self.hello_frame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.textBrowser = QTextBrowser(self.hello_frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(500, 200))
        self.textBrowser.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: White;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.horizontalLayout_7.addWidget(self.textBrowser)


        self.verticalLayout.addWidget(self.hello_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.login_frame = QFrame(self.frame_login_wom)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setMaximumSize(QSize(16777215, 16777215))
        self.login_frame.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.login_frame)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.login_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 13pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.label = QLabel(self.login_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.user_password = QLineEdit(self.login_frame)
        self.user_password.setObjectName(u"user_password")
        self.user_password.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_password, 2, 1, 1, 1)

        self.label_2 = QLabel(self.login_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.user_name = QLineEdit(self.login_frame)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.user_name, 1, 1, 1, 1)

        self.pushButton_forget_password = QPushButton(self.login_frame)
        self.pushButton_forget_password.setObjectName(u"pushButton_forget_password")
        self.pushButton_forget_password.setEnabled(False)
        self.pushButton_forget_password.setMinimumSize(QSize(0, 26))
        self.pushButton_forget_password.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush11 = QBrush(QColor(50, 98, 115, 190))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush12 = QBrush(QColor(255, 255, 255, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        brush13 = QBrush(QColor(50, 98, 115, 150))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        brush14 = QBrush(QColor(50, 98, 115, 40))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        brush15 = QBrush(QColor(50, 98, 115, 75))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButton_forget_password.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_forget_password.setFont(font1)
        self.pushButton_forget_password.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_forget_password.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_forget_password, 5, 0, 1, 1)

        self.pushButton_registation = QPushButton(self.login_frame)
        self.pushButton_registation.setObjectName(u"pushButton_registation")
        self.pushButton_registation.setMinimumSize(QSize(0, 26))
        self.pushButton_registation.setMaximumSize(QSize(16777215, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButton_registation.setPalette(palette2)
        self.pushButton_registation.setFont(font1)
        self.pushButton_registation.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_registation.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_registation, 5, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.pushButton_login = QPushButton(self.login_frame)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setMinimumSize(QSize(0, 26))
        self.pushButton_login.setMaximumSize(QSize(16777215, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.pushButton_login.setPalette(palette3)
        self.pushButton_login.setFont(font1)
        self.pushButton_login.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_login.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_login, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.login_frame)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.logs_frame = QFrame(self.frame_login_wom)
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
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_status.setFont(font2)
        self.label_status.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"")
        self.label_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_status)


        self.verticalLayout.addWidget(self.logs_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_login_wom)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_login)


        self.verticalLayout_3.addWidget(self.full_frame)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.labelLogo.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">World of Medicine</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.label.setText(QCoreApplication.translate("Login", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.pushButton_forget_password.setText(QCoreApplication.translate("Login", u"\u0417\u0430\u0431\u044b\u043b \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_registation.setText(QCoreApplication.translate("Login", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.pushButton_login.setText(QCoreApplication.translate("Login", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_status.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

