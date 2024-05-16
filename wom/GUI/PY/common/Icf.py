# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'icf.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPlainTextEdit, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

from wom.GUI.widgets.my_pushButton import PushButton
import res_main_rc
import res_main_rc

class Ui_icf(object):
    def setupUi(self, icf):
        if not icf.objectName():
            icf.setObjectName(u"icf")
        icf.resize(1281, 792)
        icf.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_3 = QVBoxLayout(icf)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(icf)
        self.main.setObjectName(u"main")
        self.horizontalLayout_4 = QHBoxLayout(self.main)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.info_frame = QFrame(self.main)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 40))
        self.info_frame.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.info_frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_Pt_info = QLabel(self.info_frame)
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

        self.horizontalLayout_2.addWidget(self.label_Pt_info)

        self.label_who_call = QLabel(self.info_frame)
        self.label_who_call.setObjectName(u"label_who_call")
        self.label_who_call.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_who_call.setFont(font1)
        self.label_who_call.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"background-color: rgba(92, 158, 173, 200);\n"
"border: none;")
        self.label_who_call.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_who_call)

        self.labelTimeline = QLabel(self.info_frame)
        self.labelTimeline.setObjectName(u"labelTimeline")
        self.labelTimeline.setMaximumSize(QSize(80, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(False)
        self.labelTimeline.setFont(font2)
        self.labelTimeline.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(92, 158, 173, 200)\n"
"")
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/personal_injury_FILL1_wght400_GRAD0_opsz48.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelTimeline)


        self.verticalLayout_2.addWidget(self.info_frame)

        self.labelZZZPtStNeur = QLabel(self.main)
        self.labelZZZPtStNeur.setObjectName(u"labelZZZPtStNeur")
        self.labelZZZPtStNeur.setMaximumSize(QSize(16777215, 26))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(112, 38, 50, 150))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush2 = QBrush(QColor(237, 237, 237, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(110, 110, 110, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(147, 147, 147, 255))
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
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        brush8 = QBrush(QColor(220, 220, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.labelZZZPtStNeur.setPalette(palette)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.labelZZZPtStNeur.setFont(font3)
        self.labelZZZPtStNeur.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")

        self.verticalLayout_2.addWidget(self.labelZZZPtStNeur)

        self.frame = QFrame(self.main)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.templates_icf = QFrame(self.frame)
        self.templates_icf.setObjectName(u"templates_icf")
        self.templates_icf.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.templates_icf)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.labelZZZ_template = QLabel(self.templates_icf)
        self.labelZZZ_template.setObjectName(u"labelZZZ_template")
        palette1 = QPalette()
        brush9 = QBrush(QColor(50, 98, 115, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        brush10 = QBrush(QColor(50, 98, 115, 40))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
        brush11 = QBrush(QColor(50, 98, 115, 128))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.labelZZZ_template.setPalette(palette1)
        self.labelZZZ_template.setFont(font)
        self.labelZZZ_template.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.labelZZZ_template.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelZZZ_template, 0, 0, 1, 2)

        self.label_3 = QLabel(self.templates_icf)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.comboBox_template = QComboBox(self.templates_icf)
        self.comboBox_template.addItem("")
        self.comboBox_template.setObjectName(u"comboBox_template")
        self.comboBox_template.setMinimumSize(QSize(300, 0))
        palette2 = QPalette()
        brush12 = QBrush(QColor(19, 36, 43, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        brush13 = QBrush(QColor(238, 238, 238, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush14 = QBrush(QColor(19, 36, 43, 128))
        brush14.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.comboBox_template.setPalette(palette2)
        self.comboBox_template.setFont(font)
        self.comboBox_template.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.comboBox_template, 2, 0, 1, 1)

        self.label_4 = QLabel(self.templates_icf)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_new_template_name = QLineEdit(self.templates_icf)
        self.lineEdit_new_template_name.setObjectName(u"lineEdit_new_template_name")
        self.lineEdit_new_template_name.setMinimumSize(QSize(300, 0))
        self.lineEdit_new_template_name.setFont(font)
        self.lineEdit_new_template_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_new_template_name, 4, 0, 1, 1)

        self.pushButtonAddNewTemplate = PushButton(self.templates_icf)
        self.pushButtonAddNewTemplate.setObjectName(u"pushButtonAddNewTemplate")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush15 = QBrush(QColor(50, 98, 115, 190))
        brush15.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonAddNewTemplate.setPalette(palette3)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.pushButtonAddNewTemplate.setFont(font4)
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

        self.gridLayout.addWidget(self.pushButtonAddNewTemplate, 4, 1, 1, 1)

        self.pushButton_push_temp = PushButton(self.templates_icf)
        self.pushButton_push_temp.setObjectName(u"pushButton_push_temp")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_push_temp.setPalette(palette4)
        self.pushButton_push_temp.setFont(font4)
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

        self.gridLayout.addWidget(self.pushButton_push_temp, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.templates_icf)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.add_new_domain = QFrame(self.main)
        self.add_new_domain.setObjectName(u"add_new_domain")
        self.add_new_domain.setMaximumSize(QSize(16777215, 160))
        self.add_new_domain.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout = QVBoxLayout(self.add_new_domain)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.labelZZZ_template_2 = QLabel(self.add_new_domain)
        self.labelZZZ_template_2.setObjectName(u"labelZZZ_template_2")
        self.labelZZZ_template_2.setMaximumSize(QSize(16777215, 35))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.labelZZZ_template_2.setPalette(palette5)
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.labelZZZ_template_2.setFont(font5)
        self.labelZZZ_template_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.labelZZZ_template_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelZZZ_template_2)

        self.find_line = QFrame(self.add_new_domain)
        self.find_line.setObjectName(u"find_line")
        self.find_line.setMaximumSize(QSize(16777215, 40))
        self.find_line.setStyleSheet(u"background-color: transparent;\n"
"border: None;")
        self.horizontalLayout_3 = QHBoxLayout(self.find_line)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelZZZ_template_24 = QLabel(self.find_line)
        self.labelZZZ_template_24.setObjectName(u"labelZZZ_template_24")
        self.labelZZZ_template_24.setMaximumSize(QSize(70, 16777215))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        brush16 = QBrush(QColor(0, 0, 0, 0))
        brush16.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.labelZZZ_template_24.setPalette(palette6)
        self.labelZZZ_template_24.setFont(font)
        self.labelZZZ_template_24.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelZZZ_template_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.labelZZZ_template_24)

        self.comboBox_find_domen = QComboBox(self.find_line)
        self.comboBox_find_domen.addItem("")
        self.comboBox_find_domen.setObjectName(u"comboBox_find_domen")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.comboBox_find_domen.setPalette(palette7)
        self.comboBox_find_domen.setFont(font)
        self.comboBox_find_domen.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.horizontalLayout_3.addWidget(self.comboBox_find_domen)

        self.pushButton_push_domen = PushButton(self.find_line)
        self.pushButton_push_domen.setObjectName(u"pushButton_push_domen")
        self.pushButton_push_domen.setMaximumSize(QSize(100, 16777215))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_push_domen.setPalette(palette8)
        self.pushButton_push_domen.setFont(font4)
        self.pushButton_push_domen.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.pushButton_push_domen)


        self.verticalLayout.addWidget(self.find_line)

        self.frame_2 = QFrame(self.add_new_domain)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 90))
        self.frame_2.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: None;\n"
"background-color: transparent;")
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 10)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 15))
        self.label_6.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lineEdit_new_domen_numbers_dynamic = QLineEdit(self.frame_3)
        self.lineEdit_new_domen_numbers_dynamic.setObjectName(u"lineEdit_new_domen_numbers_dynamic")
        self.lineEdit_new_domen_numbers_dynamic.setEnabled(False)
        self.lineEdit_new_domen_numbers_dynamic.setMaximumSize(QSize(65, 16777215))
        self.lineEdit_new_domen_numbers_dynamic.setFont(font)
        self.lineEdit_new_domen_numbers_dynamic.setStyleSheet(u"QLineEdit {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"color: #DDDDDD;\n"
"font-weight: normal;\n"
"font-size: 10pt;\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_new_domen_numbers_dynamic, 2, 1, 1, 1)

        self.lineEdit_new_domen_numbers = QLineEdit(self.frame_3)
        self.lineEdit_new_domen_numbers.setObjectName(u"lineEdit_new_domen_numbers")
        self.lineEdit_new_domen_numbers.setEnabled(False)
        self.lineEdit_new_domen_numbers.setMaximumSize(QSize(65, 16777215))
        self.lineEdit_new_domen_numbers.setFont(font)
        self.lineEdit_new_domen_numbers.setStyleSheet(u"QLineEdit {\n"
"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"color: #DDDDDD;\n"
"font-weight: normal;\n"
"font-size: 10pt;\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_new_domen_numbers, 1, 1, 1, 1)

        self.label_check_correct_dynamic = QLabel(self.frame_3)
        self.label_check_correct_dynamic.setObjectName(u"label_check_correct_dynamic")
        self.label_check_correct_dynamic.setMinimumSize(QSize(50, 0))
        self.label_check_correct_dynamic.setMaximumSize(QSize(50, 24))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.label_check_correct_dynamic.setPalette(palette9)
        self.label_check_correct_dynamic.setFont(font5)
        self.label_check_correct_dynamic.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_check_correct_dynamic, 2, 2, 1, 1)

        self.label_check_correct = QLabel(self.frame_3)
        self.label_check_correct.setObjectName(u"label_check_correct")
        self.label_check_correct.setMinimumSize(QSize(50, 0))
        self.label_check_correct.setMaximumSize(QSize(50, 24))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.label_check_correct.setPalette(palette10)
        self.label_check_correct.setFont(font5)
        self.label_check_correct.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_check_correct, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(80, 16777215))
        self.label_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.labelZZZ_template_22 = QLabel(self.frame_3)
        self.labelZZZ_template_22.setObjectName(u"labelZZZ_template_22")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.labelZZZ_template_22.setPalette(palette11)
        self.labelZZZ_template_22.setFont(font)
        self.labelZZZ_template_22.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.labelZZZ_template_22.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.labelZZZ_template_22, 0, 0, 1, 3)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(80, 16777215))
        self.label_5.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 2, 2, 1)

        self.pushButton_add_domen = PushButton(self.frame_2)
        self.pushButton_add_domen.setObjectName(u"pushButton_add_domen")
        self.pushButton_add_domen.setEnabled(False)
        self.pushButton_add_domen.setMinimumSize(QSize(85, 40))
        self.pushButton_add_domen.setMaximumSize(QSize(16777215, 16777215))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush17 = QBrush(QColor(145, 47, 64, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        brush18 = QBrush(QColor(50, 98, 115, 150))
        brush18.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
        brush19 = QBrush(QColor(50, 98, 115, 75))
        brush19.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.pushButton_add_domen.setPalette(palette12)
        self.pushButton_add_domen.setFont(font4)
        self.pushButton_add_domen.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(145, 47, 64, 255);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(145, 47, 64, 150);\n"
"border: 1px solid rgba(145, 47, 64, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(145, 47, 64, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.pushButton_add_domen, 0, 3, 2, 1)

        self.pushButton_push_domen_2 = PushButton(self.frame_2)
        self.pushButton_push_domen_2.setObjectName(u"pushButton_push_domen_2")
        self.pushButton_push_domen_2.setMaximumSize(QSize(100, 16777215))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_push_domen_2.setPalette(palette13)
        self.pushButton_push_domen_2.setFont(font4)
        self.pushButton_push_domen_2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.pushButton_push_domen_2, 0, 1, 1, 1)

        self.plainTextEdit_new_domen = QPlainTextEdit(self.frame_2)
        self.plainTextEdit_new_domen.setObjectName(u"plainTextEdit_new_domen")
        self.plainTextEdit_new_domen.setEnabled(False)
        self.plainTextEdit_new_domen.setMinimumSize(QSize(600, 0))
        self.plainTextEdit_new_domen.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_new_domen.setFont(font)
        self.plainTextEdit_new_domen.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.plainTextEdit_new_domen, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.add_new_domain)

        self.table_frame = QFrame(self.main)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_4 = QGridLayout(self.table_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.textBrowser_description = QTextBrowser(self.table_frame)
        self.textBrowser_description.setObjectName(u"textBrowser_description")
        self.textBrowser_description.setMinimumSize(QSize(350, 0))
        self.textBrowser_description.setMaximumSize(QSize(350, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(8)
        font6.setBold(True)
        self.textBrowser_description.setFont(font6)
        self.textBrowser_description.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"")

        self.gridLayout_4.addWidget(self.textBrowser_description, 1, 0, 1, 1)

        self.labelZZZ_template_23 = QLabel(self.table_frame)
        self.labelZZZ_template_23.setObjectName(u"labelZZZ_template_23")
        self.labelZZZ_template_23.setMaximumSize(QSize(16777215, 25))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.labelZZZ_template_23.setPalette(palette14)
        self.labelZZZ_template_23.setFont(font)
        self.labelZZZ_template_23.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.labelZZZ_template_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelZZZ_template_23, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.table_frame)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(750, 350))
        self.tableWidget.setFont(font4)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: #000000;\n"
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

        self.gridLayout_4.addWidget(self.tableWidget, 1, 1, 1, 1)

        self.labelZZZ_template_25 = QLabel(self.table_frame)
        self.labelZZZ_template_25.setObjectName(u"labelZZZ_template_25")
        self.labelZZZ_template_25.setMaximumSize(QSize(16777215, 25))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.labelZZZ_template_25.setPalette(palette15)
        self.labelZZZ_template_25.setFont(font)
        self.labelZZZ_template_25.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.labelZZZ_template_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelZZZ_template_25, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.table_frame)

        self.logs_frame = QFrame(self.main)
        self.logs_frame.setObjectName(u"logs_frame")
        self.logs_frame.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.horizontalLayout_5 = QHBoxLayout(self.logs_frame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_status = QLabel(self.logs_frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(0, 50))
        self.label_status.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.label_status.setFont(font7)
        self.label_status.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"")
        self.label_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_status)


        self.verticalLayout_2.addWidget(self.logs_frame)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

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
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.pushButtonNotSaveExit = PushButton(self.groupBox_wom)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush15)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonNotSaveExit.setPalette(palette16)
        self.pushButtonNotSaveExit.setFont(font4)
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
        icon = QIcon()
        icon.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSaveExit = PushButton(self.groupBox_wom)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush20 = QBrush(QColor(92, 158, 173, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonSaveExit.setPalette(palette17)
        self.pushButtonSaveExit.setFont(font4)
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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveExit.setIcon(icon1)
        self.pushButtonSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonSaveExit)


        self.horizontalLayout_4.addWidget(self.groupBox_wom)


        self.verticalLayout_3.addWidget(self.main)

        QWidget.setTabOrder(self.comboBox_template, self.pushButton_push_temp)
        QWidget.setTabOrder(self.pushButton_push_temp, self.lineEdit_new_template_name)
        QWidget.setTabOrder(self.lineEdit_new_template_name, self.pushButtonAddNewTemplate)
        QWidget.setTabOrder(self.pushButtonAddNewTemplate, self.comboBox_find_domen)
        QWidget.setTabOrder(self.comboBox_find_domen, self.pushButton_push_domen)
        QWidget.setTabOrder(self.pushButton_push_domen, self.lineEdit_new_domen_numbers)
        QWidget.setTabOrder(self.lineEdit_new_domen_numbers, self.lineEdit_new_domen_numbers_dynamic)
        QWidget.setTabOrder(self.lineEdit_new_domen_numbers_dynamic, self.pushButton_add_domen)
        QWidget.setTabOrder(self.pushButton_add_domen, self.pushButton_push_domen_2)
        QWidget.setTabOrder(self.pushButton_push_domen_2, self.pushButtonNotSaveExit)
        QWidget.setTabOrder(self.pushButtonNotSaveExit, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.plainTextEdit_new_domen)
        QWidget.setTabOrder(self.plainTextEdit_new_domen, self.textBrowser_description)
        QWidget.setTabOrder(self.textBrowser_description, self.tableWidget)

        self.retranslateUi(icf)

        QMetaObject.connectSlotsByName(icf)
    # setupUi

    def retranslateUi(self, icf):
        icf.setWindowTitle(QCoreApplication.translate("icf", u"Form", None))
        self.label_Pt_info.setText(QCoreApplication.translate("icf", u"PatientInfo\n"
"fff", None))
        self.label_who_call.setText(QCoreApplication.translate("icf", u"whocall", None))
        self.labelTimeline.setText("")
        self.labelZZZPtStNeur.setText(QCoreApplication.translate("icf", u"<html><head/><body><p align=\"center\">\u0420\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0434\u0438\u0430\u0433\u043d\u043e\u0437 \u043f\u043e \u041c\u041a\u0424</p></body></html>", None))
        self.labelZZZ_template.setText(QCoreApplication.translate("icf", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u041c\u041a\u0424", None))
        self.label_3.setText(QCoreApplication.translate("icf", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.comboBox_template.setItemText(0, "")

        self.label_4.setText(QCoreApplication.translate("icf", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.lineEdit_new_template_name.setPlaceholderText(QCoreApplication.translate("icf", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.pushButtonAddNewTemplate.setText(QCoreApplication.translate("icf", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.pushButton_push_temp.setText(QCoreApplication.translate("icf", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.labelZZZ_template_2.setText(QCoreApplication.translate("icf", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0434\u043e\u043c\u0435\u043d\u0430", None))
        self.labelZZZ_template_24.setText(QCoreApplication.translate("icf", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBox_find_domen.setItemText(0, "")

        self.pushButton_push_domen.setText(QCoreApplication.translate("icf", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("icf", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0434\u043e\u043c\u0435\u043d", None))
        self.label_check_correct_dynamic.setText(QCoreApplication.translate("icf", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_check_correct.setText(QCoreApplication.translate("icf", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("icf", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.labelZZZ_template_22.setText(QCoreApplication.translate("icf", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0438", None))
        self.label_5.setText(QCoreApplication.translate("icf", u"\u0412\u044b\u043f\u0438\u0441\u043a\u0430", None))
        self.pushButton_add_domen.setText(QCoreApplication.translate("icf", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_push_domen_2.setText(QCoreApplication.translate("icf", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.labelZZZ_template_23.setText(QCoreApplication.translate("icf", u"<html><head/><body><p align=\"center\">\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0435\u0439 \u0434\u043e\u043c\u0435\u043d\u0430</p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("icf", u"\u0414\u043e\u043c\u0435\u043d \u0441 \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u043e\u0439", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("icf", u"\u043f\u043e\u0441\u0442.", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("icf", u"\u0432\u044b\u043f.", None));
        self.labelZZZ_template_25.setText(QCoreApplication.translate("icf", u"<html><head/><body><p align=\"center\">\u0414\u043e\u043c\u0435\u043d\u044b, \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0432 \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u0431\u043e\u043b\u0435\u0437\u043d\u0438</p></body></html>", None))
        self.label_status.setText(QCoreApplication.translate("icf", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.groupBox_wom.setTitle(QCoreApplication.translate("icf", u"World of Medicine", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("icf", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("icf", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
    # retranslateUi

