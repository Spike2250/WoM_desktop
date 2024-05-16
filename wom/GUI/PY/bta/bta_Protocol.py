# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bta_Protocol.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1277, 652)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(Form)
        self.main_frame.setObjectName(u"main_frame")
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pt_info_block = QFrame(self.main_frame)
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
        font.setBold(False)
        self.label_Pt_info.setFont(font)
        self.label_Pt_info.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: 13242B;\n"
"font-size: 11pt;\n"
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
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/vaccines_FILL1_wght400_GRAD0_opsz48.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTimeline)


        self.verticalLayout.addWidget(self.pt_info_block)

        self.label_2 = QLabel(self.main_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(92, 158, 173, 200);\n"
"border: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.frame_medicine_info = QFrame(self.main_frame)
        self.frame_medicine_info.setObjectName(u"frame_medicine_info")
        self.frame_medicine_info.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.frame_medicine_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.lineEdit_series = QLineEdit(self.frame_medicine_info)
        self.lineEdit_series.setObjectName(u"lineEdit_series")
        self.lineEdit_series.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_series, 3, 1, 1, 1)

        self.label_solvent = QLabel(self.frame_medicine_info)
        self.label_solvent.setObjectName(u"label_solvent")
        self.label_solvent.setMinimumSize(QSize(200, 0))
        palette = QPalette()
        brush = QBrush(QColor(50, 98, 115, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(237, 237, 237, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(110, 110, 110, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(147, 147, 147, 255))
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
        brush9 = QBrush(QColor(220, 220, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_solvent.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_solvent.setFont(font2)
        self.label_solvent.setLayoutDirection(Qt.LeftToRight)
        self.label_solvent.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_solvent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_solvent, 6, 0, 1, 1)

        self.lineEdit_when_made = QLineEdit(self.frame_medicine_info)
        self.lineEdit_when_made.setObjectName(u"lineEdit_when_made")
        self.lineEdit_when_made.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_when_made, 4, 1, 1, 1)

        self.label_best_before = QLabel(self.frame_medicine_info)
        self.label_best_before.setObjectName(u"label_best_before")
        self.label_best_before.setMinimumSize(QSize(200, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_best_before.setPalette(palette1)
        self.label_best_before.setFont(font2)
        self.label_best_before.setLayoutDirection(Qt.LeftToRight)
        self.label_best_before.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_best_before.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_best_before, 5, 0, 1, 1)

        self.lineEdit_best_before = QLineEdit(self.frame_medicine_info)
        self.lineEdit_best_before.setObjectName(u"lineEdit_best_before")
        self.lineEdit_best_before.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_best_before, 5, 1, 1, 1)

        self.label_bta = QLabel(self.frame_medicine_info)
        self.label_bta.setObjectName(u"label_bta")
        self.label_bta.setMinimumSize(QSize(200, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_bta.setPalette(palette2)
        self.label_bta.setFont(font2)
        self.label_bta.setLayoutDirection(Qt.LeftToRight)
        self.label_bta.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout.addWidget(self.label_bta, 2, 0, 1, 1)

        self.comboBox_bta_solvent = QComboBox(self.frame_medicine_info)
        self.comboBox_bta_solvent.addItem("")
        self.comboBox_bta_solvent.addItem("")
        self.comboBox_bta_solvent.addItem("")
        self.comboBox_bta_solvent.addItem("")
        self.comboBox_bta_solvent.addItem("")
        self.comboBox_bta_solvent.setObjectName(u"comboBox_bta_solvent")
        palette3 = QPalette()
        brush10 = QBrush(QColor(19, 36, 43, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        brush11 = QBrush(QColor(238, 238, 238, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush12 = QBrush(QColor(19, 36, 43, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.comboBox_bta_solvent.setPalette(palette3)
        self.comboBox_bta_solvent.setFont(font2)
        self.comboBox_bta_solvent.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_bta_solvent.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_bta_solvent, 6, 1, 1, 1)

        self.label_series = QLabel(self.frame_medicine_info)
        self.label_series.setObjectName(u"label_series")
        self.label_series.setMinimumSize(QSize(200, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_series.setPalette(palette4)
        self.label_series.setFont(font2)
        self.label_series.setLayoutDirection(Qt.LeftToRight)
        self.label_series.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_series.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_series, 3, 0, 1, 1)

        self.comboBox_bta_preparat = QComboBox(self.frame_medicine_info)
        self.comboBox_bta_preparat.addItem("")
        self.comboBox_bta_preparat.addItem("")
        self.comboBox_bta_preparat.addItem("")
        self.comboBox_bta_preparat.setObjectName(u"comboBox_bta_preparat")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.comboBox_bta_preparat.setPalette(palette5)
        self.comboBox_bta_preparat.setFont(font2)
        self.comboBox_bta_preparat.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_bta_preparat.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_bta_preparat, 2, 1, 1, 1)

        self.label_date_from = QLabel(self.frame_medicine_info)
        self.label_date_from.setObjectName(u"label_date_from")
        self.label_date_from.setMinimumSize(QSize(200, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_date_from.setPalette(palette6)
        self.label_date_from.setFont(font2)
        self.label_date_from.setLayoutDirection(Qt.LeftToRight)
        self.label_date_from.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_date_from.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_date_from, 4, 0, 1, 1)

        self.label_3 = QLabel(self.frame_medicine_info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_medicine_info)

        self.frame_add_point = QFrame(self.main_frame)
        self.frame_add_point.setObjectName(u"frame_add_point")
        self.frame_add_point.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_2 = QVBoxLayout(self.frame_add_point)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.frame_add_point)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 25))
        self.label_4.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.frame_point = QFrame(self.frame_add_point)
        self.frame_point.setObjectName(u"frame_point")
        self.gridLayout_2 = QGridLayout(self.frame_point)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_dose = QFrame(self.frame_point)
        self.frame_dose.setObjectName(u"frame_dose")
        self.frame_dose.setMaximumSize(QSize(380, 16777215))
        self.frame_dose.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_dose)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_dose = QLineEdit(self.frame_dose)
        self.lineEdit_dose.setObjectName(u"lineEdit_dose")
        self.lineEdit_dose.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_dose.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.horizontalLayout_5.addWidget(self.lineEdit_dose)

        self.label_6 = QLabel(self.frame_dose)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)


        self.gridLayout_2.addWidget(self.frame_dose, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_point)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 2)

        self.comboBox_muscle = QComboBox(self.frame_point)
        self.comboBox_muscle.addItem("")
        self.comboBox_muscle.setObjectName(u"comboBox_muscle")
        self.comboBox_muscle.setMinimumSize(QSize(500, 0))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.comboBox_muscle.setPalette(palette7)
        self.comboBox_muscle.setFont(font2)
        self.comboBox_muscle.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_muscle.setEditable(False)

        self.gridLayout_2.addWidget(self.comboBox_muscle, 2, 0, 1, 2)

        self.label_7 = QLabel(self.frame_point)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 30);\n"
"border: none;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 2)

        self.frame_side = QFrame(self.frame_point)
        self.frame_side.setObjectName(u"frame_side")
        self.frame_side.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_side)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_side)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.comboBox_side = QComboBox(self.frame_side)
        self.comboBox_side.addItem("")
        self.comboBox_side.addItem("")
        self.comboBox_side.addItem("")
        self.comboBox_side.setObjectName(u"comboBox_side")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.comboBox_side.setPalette(palette8)
        self.comboBox_side.setFont(font2)
        self.comboBox_side.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_side.setEditable(False)

        self.horizontalLayout_4.addWidget(self.comboBox_side)


        self.gridLayout_2.addWidget(self.frame_side, 3, 0, 1, 1)

        self.frame_add_button = QFrame(self.frame_point)
        self.frame_add_button.setObjectName(u"frame_add_button")
        self.frame_add_button.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_add_button)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pushButton_add_muscle = QPushButton(self.frame_add_button)
        self.pushButton_add_muscle.setObjectName(u"pushButton_add_muscle")
        self.pushButton_add_muscle.setEnabled(True)
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush13 = QBrush(QColor(50, 98, 115, 190))
        brush13.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush14 = QBrush(QColor(236, 236, 236, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        brush15 = QBrush(QColor(108, 108, 108, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush15)
        brush16 = QBrush(QColor(145, 145, 145, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush17 = QBrush(QColor(255, 255, 255, 128))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush18 = QBrush(QColor(217, 217, 217, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush18)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButton_add_muscle.setPalette(palette9)
        self.pushButton_add_muscle.setFont(font)
        self.pushButton_add_muscle.setStyleSheet(u"QPushButton {\n"
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
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/add_circle_outline_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_muscle.setIcon(icon)
        self.pushButton_add_muscle.setIconSize(QSize(26, 26))

        self.horizontalLayout_6.addWidget(self.pushButton_add_muscle)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.frame_add_button, 4, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_point)

        self.tableWidget = QTableWidget(self.frame_add_point)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: rgba(50, 98, 115, 255);\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"   border-color: 1px solid  rgba(50, 98, 115, 255);\n"
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

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_solvent_2 = QLabel(self.frame_add_point)
        self.label_solvent_2.setObjectName(u"label_solvent_2")
        self.label_solvent_2.setMinimumSize(QSize(200, 0))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_solvent_2.setPalette(palette10)
        self.label_solvent_2.setFont(font2)
        self.label_solvent_2.setLayoutDirection(Qt.LeftToRight)
        self.label_solvent_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_solvent_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_solvent_2)

        self.label_summary = QLabel(self.frame_add_point)
        self.label_summary.setObjectName(u"label_summary")
        self.label_summary.setMinimumSize(QSize(0, 0))
        self.label_summary.setMaximumSize(QSize(150, 16777215))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label_summary.setPalette(palette11)
        self.label_summary.setFont(font2)
        self.label_summary.setLayoutDirection(Qt.LeftToRight)
        self.label_summary.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_summary.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_summary)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_add_point)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.groupBox_wom = QGroupBox(self.main_frame)
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
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        brush19 = QBrush(QColor(50, 98, 115, 150))
        brush19.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        brush20 = QBrush(QColor(50, 98, 115, 40))
        brush20.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush18)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush21 = QBrush(QColor(50, 98, 115, 75))
        brush21.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.pushButtonHelp.setPalette(palette12)
        self.pushButtonHelp.setFont(font)
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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHelp.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.pushButtonHelp)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.pushButtonNotSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonNotSaveExit.setPalette(palette13)
        self.pushButtonNotSaveExit.setFont(font)
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon2)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush22 = QBrush(QColor(92, 158, 173, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush22)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush22)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush22)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush22)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush22)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush22)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonSaveExit.setPalette(palette14)
        self.pushButtonSaveExit.setFont(font)
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveExit.setIcon(icon3)
        self.pushButtonSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonSaveExit)


        self.horizontalLayout.addWidget(self.groupBox_wom)


        self.verticalLayout_3.addWidget(self.main_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_Pt_info.setText(QCoreApplication.translate("Form", u"PatientInfo\n"
"fff", None))
        self.labelTimeline.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u0438\u043d\u044a\u0435\u043a\u0446\u0438\u0438 \u0431\u043e\u0442\u0443\u043b\u043e\u0442\u043e\u043a\u0441\u0438\u043d\u0430", None))
        self.label_solvent.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0420\u0430\u0441\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c:</p></body></html>", None))
        self.label_best_before.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0413\u043e\u0434\u0435\u043d \u0434\u043e:</p></body></html>", None))
        self.label_bta.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0439 \u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442 \u0411\u0422-\u0410:</p></body></html>", None))
        self.comboBox_bta_solvent.setItemText(0, QCoreApplication.translate("Form", u"Sol.NaCl 0,9%-2ml", None))
        self.comboBox_bta_solvent.setItemText(1, QCoreApplication.translate("Form", u"Sol.NaCl 0,9%-2.5ml", None))
        self.comboBox_bta_solvent.setItemText(2, QCoreApplication.translate("Form", u"Sol.NaCl 0,9%-3ml", None))
        self.comboBox_bta_solvent.setItemText(3, QCoreApplication.translate("Form", u"Sol.NaCl 0,9%-5ml", None))
        self.comboBox_bta_solvent.setItemText(4, QCoreApplication.translate("Form", u"Sol.NaCl 0,9%", None))

        self.label_series.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0421\u0435\u0440\u0438\u044f:</p></body></html>", None))
        self.comboBox_bta_preparat.setItemText(0, QCoreApplication.translate("Form", u"\u0420\u0435\u043b\u0430\u0442\u043e\u043a\u0441 (Relatox)", None))
        self.comboBox_bta_preparat.setItemText(1, QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u043f\u043e\u0440\u0442 (Dysport)", None))
        self.comboBox_bta_preparat.setItemText(2, QCoreApplication.translate("Form", u"\u041a\u0441\u0435\u043e\u043c\u0438\u043d (Xeomin)", None))

        self.label_date_from.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0418\u0437\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041c\u044b\u0448\u0446\u044b \u043c\u0438\u0448\u0435\u043d\u0438 \u0438 \u0434\u043e\u0437\u0438\u0440\u043e\u0432\u043a\u0438", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0437\u0430 \u0411\u0422\u0410, \u0415\u0434", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u044b\u0448\u0446\u0443", None))
        self.comboBox_muscle.setItemText(0, "")

        self.label_7.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0447\u043a\u0438 \u0438\u043d\u044a\u0435\u043a\u0446\u0438\u0438", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u043e\u0440\u043e\u043d\u0443", None))
        self.comboBox_side.setItemText(0, "")
        self.comboBox_side.setItemText(1, QCoreApplication.translate("Form", u"\u0441\u043f\u0440\u0430\u0432\u0430", None))
        self.comboBox_side.setItemText(2, QCoreApplication.translate("Form", u"\u0441\u043b\u0435\u0432\u0430", None))

        self.pushButton_add_muscle.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u044b\u0448\u0446\u044b", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0437\u0430 \u0411\u0422-\u0410, \u0415\u0434", None));
        self.label_solvent_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0412\u0441\u0435\u0433\u043e, \u0415\u0434:</p></body></html>", None))
        self.label_summary.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0441\u0443\u043c\u043c\u0430</p></body></html>", None))
        self.groupBox_wom.setTitle(QCoreApplication.translate("Form", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("Form", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("Form", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
    # retranslateUi

