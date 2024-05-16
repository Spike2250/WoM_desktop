# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StObj_admition.ui'
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
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import res_main_rc
import res_main_rc

class Ui_StObj(object):
    def setupUi(self, StObj):
        if not StObj.objectName():
            StObj.setObjectName(u"StObj")
        StObj.resize(1119, 803)
        StObj.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout = QVBoxLayout(StObj)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(StObj)
        self.main.setObjectName(u"main")
        self.horizontalLayout_4 = QHBoxLayout(self.main)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pt_info_block = QFrame(self.main)
        self.pt_info_block.setObjectName(u"pt_info_block")
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
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/stethoscope_FILL0_wght400_GRAD0_opsz48.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTimeline)


        self.verticalLayout_4.addWidget(self.pt_info_block)

        self.tabWidget = QTabWidget(self.main)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.tabWidget.setFont(font2)
        self.tabWidget.setStyleSheet(u"QTabWidget:pane {\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
"color: White;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
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
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setIconSize(QSize(28, 28))
        self.jaloby_page = QWidget()
        self.jaloby_page.setObjectName(u"jaloby_page")
        self.gridLayout = QGridLayout(self.jaloby_page)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer_7 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 4, 0, 1, 1)

        self.jaloby_2 = QFrame(self.jaloby_page)
        self.jaloby_2.setObjectName(u"jaloby_2")
        self.jaloby_2.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout_2 = QHBoxLayout(self.jaloby_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.jaloby = QFrame(self.jaloby_2)
        self.jaloby.setObjectName(u"jaloby")
        self.jaloby.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_3 = QVBoxLayout(self.jaloby)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.jaloby)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.plainTextEditPtComplaints = QPlainTextEdit(self.jaloby)
        self.plainTextEditPtComplaints.setObjectName(u"plainTextEditPtComplaints")
        self.plainTextEditPtComplaints.setMinimumSize(QSize(0, 0))
        self.plainTextEditPtComplaints.setMaximumSize(QSize(16777215, 200))
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
        brush7 = QBrush(QColor(220, 220, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtComplaints.setPalette(palette)
        self.plainTextEditPtComplaints.setFont(font)
        self.plainTextEditPtComplaints.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.verticalLayout_3.addWidget(self.plainTextEditPtComplaints)


        self.horizontalLayout_2.addWidget(self.jaloby)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.jaloby_2, 2, 1, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 4, 3, 1, 1)

        self.metric_data = QFrame(self.jaloby_page)
        self.metric_data.setObjectName(u"metric_data")
        self.metric_data.setMinimumSize(QSize(800, 0))
        self.metric_data.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_11 = QGridLayout(self.metric_data)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(5)
        self.gridLayout_11.setVerticalSpacing(1)
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.label_imt = QLabel(self.metric_data)
        self.label_imt.setObjectName(u"label_imt")
        palette1 = QPalette()
        brush8 = QBrush(QColor(50, 98, 115, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        brush9 = QBrush(QColor(0, 0, 0, 0))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush9)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush11 = QBrush(QColor(255, 255, 220, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush12 = QBrush(QColor(50, 98, 115, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.label_imt.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_imt.setFont(font3)
        self.label_imt.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.label_imt, 8, 1, 1, 6)

        self.labelPtGrowth = QLabel(self.metric_data)
        self.labelPtGrowth.setObjectName(u"labelPtGrowth")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush8)
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
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
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
        self.labelPtGrowth.setPalette(palette2)
        self.labelPtGrowth.setFont(font)
        self.labelPtGrowth.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtGrowth, 2, 1, 1, 1)

        self.labelPtSaturation = QLabel(self.metric_data)
        self.labelPtSaturation.setObjectName(u"labelPtSaturation")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSaturation.setPalette(palette3)
        self.labelPtSaturation.setFont(font)
        self.labelPtSaturation.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtSaturation, 2, 5, 1, 1)

        self.labelPtPulse = QLabel(self.metric_data)
        self.labelPtPulse.setObjectName(u"labelPtPulse")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtPulse.setPalette(palette4)
        self.labelPtPulse.setFont(font)
        self.labelPtPulse.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtPulse, 4, 5, 1, 1)

        self.lineEditSaturation = QLineEdit(self.metric_data)
        self.lineEditSaturation.setObjectName(u"lineEditSaturation")
        self.lineEditSaturation.setMaximumSize(QSize(110, 16777215))
        self.lineEditSaturation.setFont(font)
        self.lineEditSaturation.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditSaturation, 2, 6, 1, 1)

        self.labelPtTemperatureCelcium = QLabel(self.metric_data)
        self.labelPtTemperatureCelcium.setObjectName(u"labelPtTemperatureCelcium")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtTemperatureCelcium.setPalette(palette5)
        self.labelPtTemperatureCelcium.setFont(font)
        self.labelPtTemperatureCelcium.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtTemperatureCelcium, 3, 5, 1, 1)

        self.labelPtWeight = QLabel(self.metric_data)
        self.labelPtWeight.setObjectName(u"labelPtWeight")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWeight.setPalette(palette6)
        self.labelPtWeight.setFont(font)
        self.labelPtWeight.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtWeight, 1, 1, 1, 1)

        self.lineEditPtTemperature = QLineEdit(self.metric_data)
        self.lineEditPtTemperature.setObjectName(u"lineEditPtTemperature")
        self.lineEditPtTemperature.setMaximumSize(QSize(110, 16777215))
        self.lineEditPtTemperature.setFont(font)
        self.lineEditPtTemperature.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtTemperature, 3, 6, 1, 1)

        self.lineEditPtWeight = QLineEdit(self.metric_data)
        self.lineEditPtWeight.setObjectName(u"lineEditPtWeight")
        self.lineEditPtWeight.setMaximumSize(QSize(110, 16777215))
        self.lineEditPtWeight.setFont(font)
        self.lineEditPtWeight.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtWeight, 1, 2, 1, 3)

        self.lineEditPtBreathingSpeed = QLineEdit(self.metric_data)
        self.lineEditPtBreathingSpeed.setObjectName(u"lineEditPtBreathingSpeed")
        self.lineEditPtBreathingSpeed.setMaximumSize(QSize(110, 16777215))
        self.lineEditPtBreathingSpeed.setFont(font)
        self.lineEditPtBreathingSpeed.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtBreathingSpeed, 1, 6, 1, 1)

        self.labelPtBreathingSpeed = QLabel(self.metric_data)
        self.labelPtBreathingSpeed.setObjectName(u"labelPtBreathingSpeed")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtBreathingSpeed.setPalette(palette7)
        self.labelPtBreathingSpeed.setFont(font)
        self.labelPtBreathingSpeed.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtBreathingSpeed, 1, 5, 1, 1)

        self.label_7 = QLabel(self.metric_data)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_7, 0, 0, 1, 8)

        self.lineEditPtGrowth = QLineEdit(self.metric_data)
        self.lineEditPtGrowth.setObjectName(u"lineEditPtGrowth")
        self.lineEditPtGrowth.setMaximumSize(QSize(110, 16777215))
        self.lineEditPtGrowth.setFont(font)
        self.lineEditPtGrowth.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtGrowth, 2, 2, 1, 3)

        self.lineEditPtPulse = QLineEdit(self.metric_data)
        self.lineEditPtPulse.setObjectName(u"lineEditPtPulse")
        self.lineEditPtPulse.setMaximumSize(QSize(110, 16777215))
        self.lineEditPtPulse.setFont(font)
        self.lineEditPtPulse.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtPulse, 4, 6, 1, 1)

        self.label_2 = QLabel(self.metric_data)
        self.label_2.setObjectName(u"label_2")
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
        self.label_2.setPalette(palette8)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.label_2, 10, 1, 1, 6)

        self.labelPtBloodPreasure = QLabel(self.metric_data)
        self.labelPtBloodPreasure.setObjectName(u"labelPtBloodPreasure")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtBloodPreasure.setPalette(palette9)
        self.labelPtBloodPreasure.setFont(font)
        self.labelPtBloodPreasure.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtBloodPreasure, 4, 1, 1, 1)

        self.labelooo = QLabel(self.metric_data)
        self.labelooo.setObjectName(u"labelooo")
        self.labelooo.setMinimumSize(QSize(5, 0))
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
        self.labelooo.setPalette(palette10)
        self.labelooo.setFont(font)
        self.labelooo.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelooo, 4, 3, 1, 1)

        self.lineEditPtBloodPreasureSist = QLineEdit(self.metric_data)
        self.lineEditPtBloodPreasureSist.setObjectName(u"lineEditPtBloodPreasureSist")
        self.lineEditPtBloodPreasureSist.setMaximumSize(QSize(50, 16777215))
        self.lineEditPtBloodPreasureSist.setFont(font)
        self.lineEditPtBloodPreasureSist.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtBloodPreasureSist, 4, 2, 1, 1)

        self.lineEditPtBloodPreasureDiast = QLineEdit(self.metric_data)
        self.lineEditPtBloodPreasureDiast.setObjectName(u"lineEditPtBloodPreasureDiast")
        self.lineEditPtBloodPreasureDiast.setMaximumSize(QSize(50, 16777215))
        self.lineEditPtBloodPreasureDiast.setFont(font)
        self.lineEditPtBloodPreasureDiast.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtBloodPreasureDiast, 4, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_4, 4, 7, 1, 1)

        self.pushButton_random_values = QPushButton(self.metric_data)
        self.pushButton_random_values.setObjectName(u"pushButton_random_values")
        self.pushButton_random_values.setEnabled(True)
        self.pushButton_random_values.setMinimumSize(QSize(0, 30))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush13 = QBrush(QColor(50, 98, 115, 190))
        brush13.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush14 = QBrush(QColor(236, 236, 236, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        brush15 = QBrush(QColor(108, 108, 108, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush15)
        brush16 = QBrush(QColor(145, 145, 145, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush17 = QBrush(QColor(255, 255, 255, 128))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        brush18 = QBrush(QColor(50, 98, 115, 150))
        brush18.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        brush19 = QBrush(QColor(50, 98, 115, 40))
        brush19.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        brush20 = QBrush(QColor(217, 217, 217, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
        brush21 = QBrush(QColor(50, 98, 115, 75))
        brush21.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.pushButton_random_values.setPalette(palette11)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.pushButton_random_values.setFont(font4)
        self.pushButton_random_values.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_11.addWidget(self.pushButton_random_values, 1, 7, 3, 1)

        self.pushButton_add_to_diag = QPushButton(self.metric_data)
        self.pushButton_add_to_diag.setObjectName(u"pushButton_add_to_diag")
        self.pushButton_add_to_diag.setEnabled(False)
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
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
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
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.pushButton_add_to_diag.setPalette(palette12)
        self.pushButton_add_to_diag.setFont(font4)
        self.pushButton_add_to_diag.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_11.addWidget(self.pushButton_add_to_diag, 9, 1, 1, 6)


        self.gridLayout.addWidget(self.metric_data, 3, 1, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 5, 2, 1, 1)

        self.diseases_block = QFrame(self.jaloby_page)
        self.diseases_block.setObjectName(u"diseases_block")
        self.diseases_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_9 = QGridLayout(self.diseases_block)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(5)
        self.gridLayout_9.setVerticalSpacing(1)
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.checkBox_Fat = QCheckBox(self.diseases_block)
        self.checkBox_Fat.setObjectName(u"checkBox_Fat")
        self.checkBox_Fat.setFont(font4)
        self.checkBox_Fat.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_Fat, 6, 0, 1, 1)

        self.checkBox_Atherosclerosis_legs = QCheckBox(self.diseases_block)
        self.checkBox_Atherosclerosis_legs.setObjectName(u"checkBox_Atherosclerosis_legs")
        self.checkBox_Atherosclerosis_legs.setFont(font4)
        self.checkBox_Atherosclerosis_legs.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_Atherosclerosis_legs, 4, 1, 1, 1)

        self.checkBox_Stroke = QCheckBox(self.diseases_block)
        self.checkBox_Stroke.setObjectName(u"checkBox_Stroke")
        self.checkBox_Stroke.setFont(font4)
        self.checkBox_Stroke.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_Stroke, 5, 0, 1, 1)

        self.label_11 = QLabel(self.diseases_block)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 25))
        self.label_11.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 2)

        self.checkBox_other = QCheckBox(self.diseases_block)
        self.checkBox_other.setObjectName(u"checkBox_other")
        self.checkBox_other.setFont(font4)
        self.checkBox_other.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_other, 9, 0, 1, 1)

        self.checkBox_Hyperthyreosis = QCheckBox(self.diseases_block)
        self.checkBox_Hyperthyreosis.setObjectName(u"checkBox_Hyperthyreosis")
        self.checkBox_Hyperthyreosis.setFont(font4)
        self.checkBox_Hyperthyreosis.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_Hyperthyreosis, 2, 1, 1, 1)

        self.checkBox_Hypothyreosis = QCheckBox(self.diseases_block)
        self.checkBox_Hypothyreosis.setObjectName(u"checkBox_Hypothyreosis")
        self.checkBox_Hypothyreosis.setFont(font4)
        self.checkBox_Hypothyreosis.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_Hypothyreosis, 1, 1, 1, 1)

        self.checkBox_IBS = QCheckBox(self.diseases_block)
        self.checkBox_IBS.setObjectName(u"checkBox_IBS")
        self.checkBox_IBS.setFont(font4)
        self.checkBox_IBS.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_IBS, 4, 0, 1, 1)

        self.checkBox_Gastro = QCheckBox(self.diseases_block)
        self.checkBox_Gastro.setObjectName(u"checkBox_Gastro")
        self.checkBox_Gastro.setFont(font4)
        self.checkBox_Gastro.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_Gastro, 8, 0, 1, 1)

        self.checkBox_B20 = QCheckBox(self.diseases_block)
        self.checkBox_B20.setObjectName(u"checkBox_B20")
        self.checkBox_B20.setFont(font4)
        self.checkBox_B20.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_B20, 8, 1, 1, 1)

        self.checkBox_HBsAg = QCheckBox(self.diseases_block)
        self.checkBox_HBsAg.setObjectName(u"checkBox_HBsAg")
        self.checkBox_HBsAg.setFont(font4)
        self.checkBox_HBsAg.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_HBsAg, 6, 1, 1, 1)

        self.checkBox_Atherosclerosis_BCA = QCheckBox(self.diseases_block)
        self.checkBox_Atherosclerosis_BCA.setObjectName(u"checkBox_Atherosclerosis_BCA")
        self.checkBox_Atherosclerosis_BCA.setFont(font4)
        self.checkBox_Atherosclerosis_BCA.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_Atherosclerosis_BCA, 3, 1, 1, 1)

        self.checkBox_Astma = QCheckBox(self.diseases_block)
        self.checkBox_Astma.setObjectName(u"checkBox_Astma")
        self.checkBox_Astma.setFont(font4)
        self.checkBox_Astma.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_Astma, 7, 0, 1, 1)

        self.checkBox_NRS = QCheckBox(self.diseases_block)
        self.checkBox_NRS.setObjectName(u"checkBox_NRS")
        self.checkBox_NRS.setFont(font4)
        self.checkBox_NRS.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_NRS, 3, 0, 1, 1)

        self.checkBox_GB = QCheckBox(self.diseases_block)
        self.checkBox_GB.setObjectName(u"checkBox_GB")
        self.checkBox_GB.setFont(font4)
        self.checkBox_GB.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_GB, 1, 0, 1, 1)

        self.plainTextEdit_other_chronic_diseases = QPlainTextEdit(self.diseases_block)
        self.plainTextEdit_other_chronic_diseases.setObjectName(u"plainTextEdit_other_chronic_diseases")
        self.plainTextEdit_other_chronic_diseases.setMaximumSize(QSize(16777215, 150))
        self.plainTextEdit_other_chronic_diseases.setFont(font)
        self.plainTextEdit_other_chronic_diseases.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.gridLayout_9.addWidget(self.plainTextEdit_other_chronic_diseases, 10, 0, 1, 2)

        self.checkBox_SD = QCheckBox(self.diseases_block)
        self.checkBox_SD.setObjectName(u"checkBox_SD")
        self.checkBox_SD.setFont(font4)
        self.checkBox_SD.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_SD, 2, 0, 1, 1)

        self.checkBox_HCV = QCheckBox(self.diseases_block)
        self.checkBox_HCV.setObjectName(u"checkBox_HCV")
        self.checkBox_HCV.setFont(font4)
        self.checkBox_HCV.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout_9.addWidget(self.checkBox_HCV, 7, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 11, 0, 1, 1)


        self.gridLayout.addWidget(self.diseases_block, 4, 2, 1, 1)

        self.drugs_block = QFrame(self.jaloby_page)
        self.drugs_block.setObjectName(u"drugs_block")
        self.drugs_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_5 = QGridLayout(self.drugs_block)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setVerticalSpacing(1)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.comboBoxPtDrugs = QComboBox(self.drugs_block)
        self.comboBoxPtDrugs.addItem("")
        self.comboBoxPtDrugs.addItem("")
        self.comboBoxPtDrugs.addItem("")
        self.comboBoxPtDrugs.setObjectName(u"comboBoxPtDrugs")
        self.comboBoxPtDrugs.setMaximumSize(QSize(16777215, 16777215))
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
        self.comboBoxPtDrugs.setPalette(palette13)
        self.comboBoxPtDrugs.setFont(font)
        self.comboBoxPtDrugs.setLayoutDirection(Qt.LeftToRight)
        self.comboBoxPtDrugs.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_5.addWidget(self.comboBoxPtDrugs, 1, 1, 1, 2)

        self.plainTextEditPtDrugs = QPlainTextEdit(self.drugs_block)
        self.plainTextEditPtDrugs.setObjectName(u"plainTextEditPtDrugs")
        self.plainTextEditPtDrugs.setMinimumSize(QSize(0, 60))
        self.plainTextEditPtDrugs.setMaximumSize(QSize(16777215, 16777215))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtDrugs.setPalette(palette14)
        self.plainTextEditPtDrugs.setFont(font)
        self.plainTextEditPtDrugs.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_5.addWidget(self.plainTextEditPtDrugs, 2, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label_8 = QLabel(self.drugs_block)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 4)


        self.gridLayout.addWidget(self.drugs_block, 4, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_21)

        self.frame_templates_2 = QFrame(self.jaloby_page)
        self.frame_templates_2.setObjectName(u"frame_templates_2")
        self.frame_templates_2.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_13 = QGridLayout(self.frame_templates_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(5)
        self.gridLayout_13.setVerticalSpacing(1)
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.comboBox_jaloby_templates = QComboBox(self.frame_templates_2)
        self.comboBox_jaloby_templates.addItem("")
        self.comboBox_jaloby_templates.setObjectName(u"comboBox_jaloby_templates")
        self.comboBox_jaloby_templates.setMaximumSize(QSize(16777215, 16777215))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBox_jaloby_templates.setPalette(palette15)
        self.comboBox_jaloby_templates.setFont(font)
        self.comboBox_jaloby_templates.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_13.addWidget(self.comboBox_jaloby_templates, 2, 0, 1, 1)

        self.pushButtonAddNewTemplate_jaloby = QPushButton(self.frame_templates_2)
        self.pushButtonAddNewTemplate_jaloby.setObjectName(u"pushButtonAddNewTemplate_jaloby")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonAddNewTemplate_jaloby.setPalette(palette16)
        self.pushButtonAddNewTemplate_jaloby.setFont(font4)
        self.pushButtonAddNewTemplate_jaloby.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_13.addWidget(self.pushButtonAddNewTemplate_jaloby, 4, 1, 1, 1)

        self.label_14 = QLabel(self.frame_templates_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_14, 0, 0, 1, 2)

        self.pushButton_push_temp_jaloby = QPushButton(self.frame_templates_2)
        self.pushButton_push_temp_jaloby.setObjectName(u"pushButton_push_temp_jaloby")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButton_push_temp_jaloby.setPalette(palette17)
        self.pushButton_push_temp_jaloby.setFont(font4)
        self.pushButton_push_temp_jaloby.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_13.addWidget(self.pushButton_push_temp_jaloby, 2, 1, 1, 1)

        self.lineEdit_new_template_name_jaloby = QLineEdit(self.frame_templates_2)
        self.lineEdit_new_template_name_jaloby.setObjectName(u"lineEdit_new_template_name_jaloby")
        self.lineEdit_new_template_name_jaloby.setMinimumSize(QSize(350, 0))
        self.lineEdit_new_template_name_jaloby.setFont(font)
        self.lineEdit_new_template_name_jaloby.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_13.addWidget(self.lineEdit_new_template_name_jaloby, 4, 0, 1, 1)

        self.label_15 = QLabel(self.frame_templates_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.frame_templates_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_16, 3, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_templates_2)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_22)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 2)

        icon = QIcon()
        icon.addFile(u":/icon/icons/message_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.jaloby_page, icon, "")
        self.anamnesis_page = QWidget()
        self.anamnesis_page.setObjectName(u"anamnesis_page")
        self.gridLayout_12 = QGridLayout(self.anamnesis_page)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_19, 1, 0, 1, 1)

        self.epid_block = QFrame(self.anamnesis_page)
        self.epid_block.setObjectName(u"epid_block")
        self.epid_block.setMinimumSize(QSize(850, 0))
        self.epid_block.setMaximumSize(QSize(16777215, 170))
        self.epid_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_8 = QGridLayout(self.epid_block)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(5)
        self.gridLayout_8.setVerticalSpacing(1)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.comboBoxPtAnamEpid = QComboBox(self.epid_block)
        self.comboBoxPtAnamEpid.addItem("")
        self.comboBoxPtAnamEpid.addItem("")
        self.comboBoxPtAnamEpid.setObjectName(u"comboBoxPtAnamEpid")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtAnamEpid.setPalette(palette18)
        self.comboBoxPtAnamEpid.setFont(font)
        self.comboBoxPtAnamEpid.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_8.addWidget(self.comboBoxPtAnamEpid, 1, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 1, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_14, 1, 2, 1, 1)

        self.label_10 = QLabel(self.epid_block)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 3)

        self.plainTextEditPtAnamEpid = QPlainTextEdit(self.epid_block)
        self.plainTextEditPtAnamEpid.setObjectName(u"plainTextEditPtAnamEpid")
        self.plainTextEditPtAnamEpid.setMinimumSize(QSize(0, 60))
        self.plainTextEditPtAnamEpid.setMaximumSize(QSize(16777215, 120))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtAnamEpid.setPalette(palette19)
        self.plainTextEditPtAnamEpid.setFont(font)
        self.plainTextEditPtAnamEpid.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_8.addWidget(self.plainTextEditPtAnamEpid, 2, 0, 1, 3)


        self.gridLayout_12.addWidget(self.epid_block, 2, 1, 1, 1)

        self.anamnesis_morbi = QFrame(self.anamnesis_page)
        self.anamnesis_morbi.setObjectName(u"anamnesis_morbi")
        self.anamnesis_morbi.setMinimumSize(QSize(850, 0))
        self.anamnesis_morbi.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_5 = QVBoxLayout(self.anamnesis_morbi)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.anamnesis_morbi)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.plainTextEditPtAnamMorbi = QPlainTextEdit(self.anamnesis_morbi)
        self.plainTextEditPtAnamMorbi.setObjectName(u"plainTextEditPtAnamMorbi")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtAnamMorbi.setPalette(palette20)
        self.plainTextEditPtAnamMorbi.setFont(font)
        self.plainTextEditPtAnamMorbi.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.verticalLayout_5.addWidget(self.plainTextEditPtAnamMorbi)


        self.gridLayout_12.addWidget(self.anamnesis_morbi, 0, 1, 1, 1)

        self.allergo_block = QFrame(self.anamnesis_page)
        self.allergo_block.setObjectName(u"allergo_block")
        self.allergo_block.setMinimumSize(QSize(850, 0))
        self.allergo_block.setMaximumSize(QSize(16777215, 170))
        self.allergo_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_4 = QGridLayout(self.allergo_block)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(1)
        self.label_9 = QLabel(self.allergo_block)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.comboBoxPtAllergStatus = QComboBox(self.allergo_block)
        self.comboBoxPtAllergStatus.addItem("")
        self.comboBoxPtAllergStatus.addItem("")
        self.comboBoxPtAllergStatus.setObjectName(u"comboBoxPtAllergStatus")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtAllergStatus.setPalette(palette21)
        self.comboBoxPtAllergStatus.setFont(font)
        self.comboBoxPtAllergStatus.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.comboBoxPtAllergStatus, 1, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 1, 2, 1, 1)

        self.plainTextEditPtAnamAllerg = QPlainTextEdit(self.allergo_block)
        self.plainTextEditPtAnamAllerg.setObjectName(u"plainTextEditPtAnamAllerg")
        self.plainTextEditPtAnamAllerg.setMinimumSize(QSize(0, 60))
        self.plainTextEditPtAnamAllerg.setMaximumSize(QSize(16777215, 120))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtAnamAllerg.setPalette(palette22)
        self.plainTextEditPtAnamAllerg.setFont(font)
        self.plainTextEditPtAnamAllerg.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.plainTextEditPtAnamAllerg, 2, 0, 1, 3)


        self.gridLayout_12.addWidget(self.allergo_block, 1, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_20, 1, 2, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/auto_stories_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.anamnesis_page, icon1, "")
        self.work_page = QWidget()
        self.work_page.setObjectName(u"work_page")
        self.gridLayout_3 = QGridLayout(self.work_page)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.work_block = QFrame(self.work_page)
        self.work_block.setObjectName(u"work_block")
        self.work_block.setMinimumSize(QSize(700, 0))
        self.work_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_6 = QGridLayout(self.work_block)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.comboBoxWorkList_prognosis = QComboBox(self.work_block)
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.setObjectName(u"comboBoxWorkList_prognosis")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxWorkList_prognosis.setPalette(palette23)
        self.comboBoxWorkList_prognosis.setFont(font)
        self.comboBoxWorkList_prognosis.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.comboBoxWorkList_prognosis, 12, 2, 1, 3)

        self.labelPtSickListInfo = QLabel(self.work_block)
        self.labelPtSickListInfo.setObjectName(u"labelPtSickListInfo")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette24.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette24.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette24.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSickListInfo.setPalette(palette24)
        self.labelPtSickListInfo.setFont(font)
        self.labelPtSickListInfo.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtSickListInfo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtSickListInfo, 3, 1, 1, 1)

        self.label_13 = QLabel(self.work_block)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 25))
        self.label_13.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_13, 0, 1, 1, 4)

        self.dateEditPtWorkListDateOpening = QDateEdit(self.work_block)
        self.dateEditPtWorkListDateOpening.setObjectName(u"dateEditPtWorkListDateOpening")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.dateEditPtWorkListDateOpening.setPalette(palette25)
        self.dateEditPtWorkListDateOpening.setFont(font)
        self.dateEditPtWorkListDateOpening.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.dateEditPtWorkListDateOpening.setTimeSpec(Qt.LocalTime)

        self.gridLayout_6.addWidget(self.dateEditPtWorkListDateOpening, 11, 2, 1, 1)

        self.labelPtWorkListDateOpening = QLabel(self.work_block)
        self.labelPtWorkListDateOpening.setObjectName(u"labelPtWorkListDateOpening")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette26.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette26.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette26.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette26.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette26.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette26.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListDateOpening.setPalette(palette26)
        self.labelPtWorkListDateOpening.setFont(font)
        self.labelPtWorkListDateOpening.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkListDateOpening.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkListDateOpening, 11, 1, 1, 1)

        self.labelPtWorkPlace = QLabel(self.work_block)
        self.labelPtWorkPlace.setObjectName(u"labelPtWorkPlace")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette27.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette27.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette27.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette27.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette27.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette27.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette27.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette27.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette27.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette27.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette27.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette27.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette27.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette27.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette27.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette27.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkPlace.setPalette(palette27)
        self.labelPtWorkPlace.setFont(font)
        self.labelPtWorkPlace.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkPlace.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkPlace, 5, 1, 1, 1)

        self.labelPtWorkListNumber_3 = QLabel(self.work_block)
        self.labelPtWorkListNumber_3.setObjectName(u"labelPtWorkListNumber_3")
        self.labelPtWorkListNumber_3.setMaximumSize(QSize(50, 16777215))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette28.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListNumber_3.setPalette(palette28)
        self.labelPtWorkListNumber_3.setFont(font)
        self.labelPtWorkListNumber_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_6.addWidget(self.labelPtWorkListNumber_3, 10, 3, 1, 1)

        self.comboBoxPtSocialStatus = QComboBox(self.work_block)
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.setObjectName(u"comboBoxPtSocialStatus")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette29.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtSocialStatus.setPalette(palette29)
        self.comboBoxPtSocialStatus.setFont(font)
        self.comboBoxPtSocialStatus.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtSocialStatus.setEditable(True)

        self.gridLayout_6.addWidget(self.comboBoxPtSocialStatus, 1, 2, 1, 3)

        self.labelPtWorkListDateOpening_2 = QLabel(self.work_block)
        self.labelPtWorkListDateOpening_2.setObjectName(u"labelPtWorkListDateOpening_2")
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette30.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette30.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette30.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette30.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette30.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListDateOpening_2.setPalette(palette30)
        self.labelPtWorkListDateOpening_2.setFont(font)
        self.labelPtWorkListDateOpening_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_6.addWidget(self.labelPtWorkListDateOpening_2, 11, 3, 1, 2)

        self.labelPtSickListInfo_2 = QLabel(self.work_block)
        self.labelPtSickListInfo_2.setObjectName(u"labelPtSickListInfo_2")
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette31.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette31.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette31.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette31.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette31.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette31.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette31.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette31.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette31.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette31.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette31.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette31.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSickListInfo_2.setPalette(palette31)
        self.labelPtSickListInfo_2.setFont(font)
        self.labelPtSickListInfo_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtSickListInfo_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtSickListInfo_2, 12, 1, 1, 1)

        self.checkBoxPtNeedSickList_2 = QCheckBox(self.work_block)
        self.checkBoxPtNeedSickList_2.setObjectName(u"checkBoxPtNeedSickList_2")
        self.checkBoxPtNeedSickList_2.setEnabled(False)
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette32.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette32.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette32.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette32.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette32.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette32.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette32.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette32.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette32.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette32.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette32.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette32.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
        brush22 = QBrush(QColor(238, 238, 238, 128))
        brush22.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.checkBoxPtNeedSickList_2.setPalette(palette32)
        self.checkBoxPtNeedSickList_2.setFont(font4)
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

        self.gridLayout_6.addWidget(self.checkBoxPtNeedSickList_2, 2, 3, 1, 2)

        self.lineEditPtWorkPlace = QLineEdit(self.work_block)
        self.lineEditPtWorkPlace.setObjectName(u"lineEditPtWorkPlace")
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lineEditPtWorkPlace.setPalette(palette33)
        self.lineEditPtWorkPlace.setFont(font)
        self.lineEditPtWorkPlace.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.lineEditPtWorkPlace, 5, 2, 1, 3)

        self.labelPtSocialStatus = QLabel(self.work_block)
        self.labelPtSocialStatus.setObjectName(u"labelPtSocialStatus")
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette34.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette34.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette34.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette34.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette34.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette34.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette34.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette34.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette34.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette34.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette34.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette34.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette34.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette34.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette34.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette34.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette34.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette34.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSocialStatus.setPalette(palette34)
        self.labelPtSocialStatus.setFont(font)
        self.labelPtSocialStatus.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtSocialStatus.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtSocialStatus, 1, 1, 1, 1)

        self.lineEditPtWorkListNumber_issued = QLineEdit(self.work_block)
        self.lineEditPtWorkListNumber_issued.setObjectName(u"lineEditPtWorkListNumber_issued")
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette35.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette35.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette35.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette35.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette35.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lineEditPtWorkListNumber_issued.setPalette(palette35)
        self.lineEditPtWorkListNumber_issued.setFont(font)
        self.lineEditPtWorkListNumber_issued.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.lineEditPtWorkListNumber_issued, 9, 2, 1, 3)

        self.labelPtWorkListS = QLabel(self.work_block)
        self.labelPtWorkListS.setObjectName(u"labelPtWorkListS")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette36.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette36.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette36.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette36.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette36.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette36.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette36.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette36.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette36.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette36.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette36.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette36.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette36.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette36.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette36.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette36.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette36.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette36.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListS.setPalette(palette36)
        self.labelPtWorkListS.setFont(font)
        self.labelPtWorkListS.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkListS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkListS, 10, 1, 1, 1)

        self.dateEditPtWorkListDate1_1 = QDateEdit(self.work_block)
        self.dateEditPtWorkListDate1_1.setObjectName(u"dateEditPtWorkListDate1_1")
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette37.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.dateEditPtWorkListDate1_1.setPalette(palette37)
        self.dateEditPtWorkListDate1_1.setFont(font)
        self.dateEditPtWorkListDate1_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.dateEditPtWorkListDate1_1.setTimeSpec(Qt.LocalTime)

        self.gridLayout_6.addWidget(self.dateEditPtWorkListDate1_1, 10, 2, 1, 1)

        self.lineEditPtWorkPosition = QLineEdit(self.work_block)
        self.lineEditPtWorkPosition.setObjectName(u"lineEditPtWorkPosition")
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette38.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette38.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette38.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush)
        palette38.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette38.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette38.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette38.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette38.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette38.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette38.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette38.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette38.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette38.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette38.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lineEditPtWorkPosition.setPalette(palette38)
        self.lineEditPtWorkPosition.setFont(font)
        self.lineEditPtWorkPosition.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.lineEditPtWorkPosition, 6, 2, 1, 3)

        self.labelPtWorkListNumber_2 = QLabel(self.work_block)
        self.labelPtWorkListNumber_2.setObjectName(u"labelPtWorkListNumber_2")
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette39.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette39.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette39.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette39.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette39.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette39.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette39.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette39.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette39.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette39.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette39.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette39.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette39.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette39.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette39.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette39.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette39.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette39.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette39.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette39.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette39.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette39.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette39.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListNumber_2.setPalette(palette39)
        self.labelPtWorkListNumber_2.setFont(font)
        self.labelPtWorkListNumber_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkListNumber_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkListNumber_2, 9, 1, 1, 1)

        self.labelPtWorkPosition = QLabel(self.work_block)
        self.labelPtWorkPosition.setObjectName(u"labelPtWorkPosition")
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette40.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette40.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette40.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette40.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette40.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette40.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette40.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette40.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette40.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette40.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette40.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette40.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette40.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette40.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette40.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette40.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette40.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette40.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette40.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette40.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette40.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette40.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkPosition.setPalette(palette40)
        self.labelPtWorkPosition.setFont(font)
        self.labelPtWorkPosition.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkPosition.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkPosition, 6, 1, 1, 1)

        self.labelPtWorkListNumber = QLabel(self.work_block)
        self.labelPtWorkListNumber.setObjectName(u"labelPtWorkListNumber")
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette41.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette41.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette41.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette41.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette41.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette41.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette41.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette41.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette41.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette41.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette41.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette41.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette41.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette41.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette41.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette41.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette41.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette41.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette41.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListNumber.setPalette(palette41)
        self.labelPtWorkListNumber.setFont(font)
        self.labelPtWorkListNumber.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkListNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkListNumber, 8, 1, 1, 1)

        self.checkBoxPtNeedSickList = QCheckBox(self.work_block)
        self.checkBoxPtNeedSickList.setObjectName(u"checkBoxPtNeedSickList")
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette42.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette42.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette42.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette42.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette42.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette42.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette42.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette42.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette42.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette42.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette42.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette42.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette42.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.checkBoxPtNeedSickList.setPalette(palette42)
        self.checkBoxPtNeedSickList.setFont(font4)
        self.checkBoxPtNeedSickList.setLayoutDirection(Qt.LeftToRight)
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

        self.gridLayout_6.addWidget(self.checkBoxPtNeedSickList, 2, 2, 1, 1)

        self.lineEditPtWorkListNumber1_1 = QLineEdit(self.work_block)
        self.lineEditPtWorkListNumber1_1.setObjectName(u"lineEditPtWorkListNumber1_1")
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette43.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette43.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette43.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette43.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette43.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette43.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lineEditPtWorkListNumber1_1.setPalette(palette43)
        self.lineEditPtWorkListNumber1_1.setFont(font)
        self.lineEditPtWorkListNumber1_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.lineEditPtWorkListNumber1_1, 8, 2, 1, 3)

        self.comboBoxWorkListInfo = QComboBox(self.work_block)
        self.comboBoxWorkListInfo.addItem("")
        self.comboBoxWorkListInfo.addItem("")
        self.comboBoxWorkListInfo.addItem("")
        self.comboBoxWorkListInfo.setObjectName(u"comboBoxWorkListInfo")
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette44.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette44.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette44.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette44.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette44.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette44.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxWorkListInfo.setPalette(palette44)
        self.comboBoxWorkListInfo.setFont(font)
        self.comboBoxWorkListInfo.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.comboBoxWorkListInfo, 3, 2, 1, 3)

        self.dateEditPtWorkListDate1_2 = QDateEdit(self.work_block)
        self.dateEditPtWorkListDate1_2.setObjectName(u"dateEditPtWorkListDate1_2")
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette45.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush)
        palette45.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette45.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette45.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette45.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette45.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette45.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.dateEditPtWorkListDate1_2.setPalette(palette45)
        self.dateEditPtWorkListDate1_2.setFont(font)
        self.dateEditPtWorkListDate1_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.dateEditPtWorkListDate1_2.setTimeSpec(Qt.LocalTime)

        self.gridLayout_6.addWidget(self.dateEditPtWorkListDate1_2, 10, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer, 4, 2, 1, 1)


        self.gridLayout_3.addWidget(self.work_block, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 1, 1, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/personal_injury_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.work_page, icon2, "")
        self.obj_status = QWidget()
        self.obj_status.setObjectName(u"obj_status")
        self.gridLayout_10 = QGridLayout(self.obj_status)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_17, 1, 0, 1, 1)

        self.frame = QFrame(self.obj_status)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.labelPtHearthNoise = QLabel(self.frame)
        self.labelPtHearthNoise.setObjectName(u"labelPtHearthNoise")
        self.labelPtHearthNoise.setMaximumSize(QSize(150, 16777215))
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette46.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette46.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette46.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette46.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette46.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette46.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette46.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette46.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette46.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette46.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette46.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette46.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette46.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette46.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette46.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette46.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette46.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette46.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette46.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette46.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette46.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette46.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette46.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtHearthNoise.setPalette(palette46)
        self.labelPtHearthNoise.setFont(font)
        self.labelPtHearthNoise.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtHearthNoise, 13, 0, 1, 1)

        self.comboBoxPtSkinState_1 = QComboBox(self.frame)
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.setObjectName(u"comboBoxPtSkinState_1")
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette47.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette47.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette47.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush)
        palette47.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette47.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette47.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette47.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette47.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette47.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette47.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette47.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette47.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtSkinState_1.setPalette(palette47)
        self.comboBoxPtSkinState_1.setFont(font)
        self.comboBoxPtSkinState_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtSkinState_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtSkinState_1, 2, 1, 1, 1)

        self.labelPtGeneralState = QLabel(self.frame)
        self.labelPtGeneralState.setObjectName(u"labelPtGeneralState")
        self.labelPtGeneralState.setMaximumSize(QSize(150, 16777215))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette48.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette48.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette48.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette48.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette48.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette48.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette48.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette48.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette48.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette48.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette48.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette48.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette48.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette48.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette48.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette48.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette48.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette48.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette48.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette48.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtGeneralState.setPalette(palette48)
        self.labelPtGeneralState.setFont(font)
        self.labelPtGeneralState.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtGeneralState, 1, 0, 1, 1)

        self.labelPtDyspnea = QLabel(self.frame)
        self.labelPtDyspnea.setObjectName(u"labelPtDyspnea")
        self.labelPtDyspnea.setMaximumSize(QSize(150, 16777215))
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette49.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette49.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette49.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette49.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette49.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette49.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette49.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette49.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette49.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette49.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette49.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette49.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette49.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette49.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette49.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette49.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette49.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette49.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette49.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette49.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette49.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette49.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtDyspnea.setPalette(palette49)
        self.labelPtDyspnea.setFont(font)
        self.labelPtDyspnea.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtDyspnea, 9, 0, 1, 1)

        self.labelPtWheezing = QLabel(self.frame)
        self.labelPtWheezing.setObjectName(u"labelPtWheezing")
        self.labelPtWheezing.setMaximumSize(QSize(150, 16777215))
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette50.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette50.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette50.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette50.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette50.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette50.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette50.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette50.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette50.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette50.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette50.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette50.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette50.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette50.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette50.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette50.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette50.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette50.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette50.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette50.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette50.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette50.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette50.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette50.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette50.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette50.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette50.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette50.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette50.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWheezing.setPalette(palette50)
        self.labelPtWheezing.setFont(font)
        self.labelPtWheezing.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtWheezing, 7, 0, 1, 1)

        self.comboBoxPtStomach_1 = QComboBox(self.frame)
        self.comboBoxPtStomach_1.addItem("")
        self.comboBoxPtStomach_1.addItem("")
        self.comboBoxPtStomach_1.addItem("")
        self.comboBoxPtStomach_1.addItem("")
        self.comboBoxPtStomach_1.setObjectName(u"comboBoxPtStomach_1")
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette51.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Active, QPalette.Text, brush)
        palette51.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette51.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette51.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette51.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette51.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtStomach_1.setPalette(palette51)
        self.comboBoxPtStomach_1.setFont(font)
        self.comboBoxPtStomach_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtStomach_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtStomach_1, 14, 1, 1, 1)

        self.comboBoxPtBreathing_3 = QComboBox(self.frame)
        self.comboBoxPtBreathing_3.addItem("")
        self.comboBoxPtBreathing_3.addItem("")
        self.comboBoxPtBreathing_3.addItem("")
        self.comboBoxPtBreathing_3.setObjectName(u"comboBoxPtBreathing_3")
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette52.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette52.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette52.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette52.setBrush(QPalette.Active, QPalette.Text, brush)
        palette52.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette52.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette52.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette52.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette52.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette52.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette52.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette52.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette52.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette52.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette52.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette52.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette52.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtBreathing_3.setPalette(palette52)
        self.comboBoxPtBreathing_3.setFont(font)
        self.comboBoxPtBreathing_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtBreathing_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtBreathing_3, 6, 1, 1, 2)

        self.comboBoxPtUrination_3 = QComboBox(self.frame)
        self.comboBoxPtUrination_3.addItem("")
        self.comboBoxPtUrination_3.addItem("")
        self.comboBoxPtUrination_3.addItem("")
        self.comboBoxPtUrination_3.addItem("")
        self.comboBoxPtUrination_3.setObjectName(u"comboBoxPtUrination_3")
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette53.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette53.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette53.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette53.setBrush(QPalette.Active, QPalette.Text, brush)
        palette53.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette53.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette53.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette53.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette53.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette53.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette53.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette53.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette53.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette53.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette53.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette53.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette53.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette53.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtUrination_3.setPalette(palette53)
        self.comboBoxPtUrination_3.setFont(font)
        self.comboBoxPtUrination_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtUrination_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtUrination_3, 19, 1, 1, 2)

        self.comboBoxPtBreathing_1 = QComboBox(self.frame)
        self.comboBoxPtBreathing_1.addItem("")
        self.comboBoxPtBreathing_1.addItem("")
        self.comboBoxPtBreathing_1.addItem("")
        self.comboBoxPtBreathing_1.setObjectName(u"comboBoxPtBreathing_1")
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette54.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Text, brush)
        palette54.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette54.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette54.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette54.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette54.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtBreathing_1.setPalette(palette54)
        self.comboBoxPtBreathing_1.setFont(font)
        self.comboBoxPtBreathing_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtBreathing_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtBreathing_1, 5, 1, 1, 1)

        self.comboBoxPtGeneralState = QComboBox(self.frame)
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.setObjectName(u"comboBoxPtGeneralState")
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette55.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Active, QPalette.Text, brush)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette55.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette55.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette55.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette55.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtGeneralState.setPalette(palette55)
        self.comboBoxPtGeneralState.setFont(font)
        self.comboBoxPtGeneralState.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxPtGeneralState, 1, 1, 1, 2)

        self.comboBoxPtHearthTone_3 = QComboBox(self.frame)
        self.comboBoxPtHearthTone_3.addItem("")
        self.comboBoxPtHearthTone_3.addItem("")
        self.comboBoxPtHearthTone_3.addItem("")
        self.comboBoxPtHearthTone_3.addItem("")
        self.comboBoxPtHearthTone_3.setObjectName(u"comboBoxPtHearthTone_3")
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette56.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Active, QPalette.Text, brush)
        palette56.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette56.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette56.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette56.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette56.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette56.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette56.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette56.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette56.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthTone_3.setPalette(palette56)
        self.comboBoxPtHearthTone_3.setFont(font)
        self.comboBoxPtHearthTone_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtHearthTone_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtHearthTone_3, 12, 1, 1, 2)

        self.comboBoxPtDyspnea_2 = QComboBox(self.frame)
        self.comboBoxPtDyspnea_2.addItem("")
        self.comboBoxPtDyspnea_2.addItem("")
        self.comboBoxPtDyspnea_2.addItem("")
        self.comboBoxPtDyspnea_2.addItem("")
        self.comboBoxPtDyspnea_2.setObjectName(u"comboBoxPtDyspnea_2")
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette57.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette57.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Text, brush)
        palette57.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette57.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette57.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette57.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette57.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette57.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette57.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette57.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette57.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette57.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette57.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette57.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette57.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette57.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDyspnea_2.setPalette(palette57)
        self.comboBoxPtDyspnea_2.setFont(font)
        self.comboBoxPtDyspnea_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDyspnea_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDyspnea_2, 10, 1, 1, 1)

        self.labelPtHearthTones = QLabel(self.frame)
        self.labelPtHearthTones.setObjectName(u"labelPtHearthTones")
        self.labelPtHearthTones.setMaximumSize(QSize(150, 16777215))
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette58.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette58.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette58.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette58.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette58.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette58.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette58.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette58.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette58.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette58.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette58.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette58.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette58.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette58.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette58.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette58.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette58.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette58.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette58.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette58.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette58.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette58.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette58.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette58.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette58.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette58.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette58.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette58.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette58.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtHearthTones.setPalette(palette58)
        self.labelPtHearthTones.setFont(font)
        self.labelPtHearthTones.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtHearthTones, 11, 0, 1, 1)

        self.comboBoxPtDefecation_2 = QComboBox(self.frame)
        self.comboBoxPtDefecation_2.addItem("")
        self.comboBoxPtDefecation_2.addItem("")
        self.comboBoxPtDefecation_2.addItem("")
        self.comboBoxPtDefecation_2.addItem("")
        self.comboBoxPtDefecation_2.setObjectName(u"comboBoxPtDefecation_2")
        palette59 = QPalette()
        palette59.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette59.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette59.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette59.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette59.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette59.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette59.setBrush(QPalette.Active, QPalette.Text, brush)
        palette59.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette59.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette59.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette59.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette59.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette59.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette59.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette59.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette59.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette59.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette59.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette59.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette59.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette59.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette59.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette59.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette59.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette59.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette59.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette59.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette59.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette59.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDefecation_2.setPalette(palette59)
        self.comboBoxPtDefecation_2.setFont(font)
        self.comboBoxPtDefecation_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDefecation_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDefecation_2, 16, 2, 1, 1)

        self.labelPtLymphnode = QLabel(self.frame)
        self.labelPtLymphnode.setObjectName(u"labelPtLymphnode")
        self.labelPtLymphnode.setMaximumSize(QSize(150, 16777215))
        palette60 = QPalette()
        palette60.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette60.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette60.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette60.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette60.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette60.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette60.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette60.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette60.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette60.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette60.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette60.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette60.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette60.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette60.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette60.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette60.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette60.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette60.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette60.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette60.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette60.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette60.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette60.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette60.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette60.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette60.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette60.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette60.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette60.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette60.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette60.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette60.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette60.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette60.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette60.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette60.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette60.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette60.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette60.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette60.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette60.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette60.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette60.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette60.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtLymphnode.setPalette(palette60)
        self.labelPtLymphnode.setFont(font)
        self.labelPtLymphnode.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtLymphnode, 3, 0, 1, 1)

        self.labelPtDefecation = QLabel(self.frame)
        self.labelPtDefecation.setObjectName(u"labelPtDefecation")
        self.labelPtDefecation.setMaximumSize(QSize(150, 16777215))
        palette61 = QPalette()
        palette61.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette61.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette61.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette61.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette61.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette61.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette61.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette61.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette61.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette61.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette61.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette61.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette61.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette61.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette61.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette61.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette61.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette61.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette61.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette61.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette61.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette61.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette61.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette61.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette61.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette61.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette61.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette61.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette61.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette61.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette61.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette61.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette61.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette61.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette61.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette61.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette61.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette61.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette61.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette61.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette61.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette61.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette61.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette61.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette61.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtDefecation.setPalette(palette61)
        self.labelPtDefecation.setFont(font)
        self.labelPtDefecation.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtDefecation, 16, 0, 1, 1)

        self.comboBoxPtBreathing_2 = QComboBox(self.frame)
        self.comboBoxPtBreathing_2.addItem("")
        self.comboBoxPtBreathing_2.addItem("")
        self.comboBoxPtBreathing_2.addItem("")
        self.comboBoxPtBreathing_2.setObjectName(u"comboBoxPtBreathing_2")
        palette62 = QPalette()
        palette62.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette62.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette62.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette62.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette62.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette62.setBrush(QPalette.Active, QPalette.Text, brush)
        palette62.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette62.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette62.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette62.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette62.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette62.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette62.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette62.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette62.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette62.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette62.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette62.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette62.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette62.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette62.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette62.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette62.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette62.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette62.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette62.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtBreathing_2.setPalette(palette62)
        self.comboBoxPtBreathing_2.setFont(font)
        self.comboBoxPtBreathing_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtBreathing_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtBreathing_2, 5, 2, 1, 1)

        self.comboBoxPtDyspnea_1 = QComboBox(self.frame)
        self.comboBoxPtDyspnea_1.addItem("")
        self.comboBoxPtDyspnea_1.addItem("")
        self.comboBoxPtDyspnea_1.addItem("")
        self.comboBoxPtDyspnea_1.addItem("")
        self.comboBoxPtDyspnea_1.setObjectName(u"comboBoxPtDyspnea_1")
        palette63 = QPalette()
        palette63.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette63.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette63.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette63.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette63.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette63.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette63.setBrush(QPalette.Active, QPalette.Text, brush)
        palette63.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette63.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette63.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette63.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette63.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette63.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette63.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette63.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette63.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette63.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette63.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette63.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette63.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette63.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette63.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette63.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette63.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette63.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette63.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette63.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette63.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette63.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDyspnea_1.setPalette(palette63)
        self.comboBoxPtDyspnea_1.setFont(font)
        self.comboBoxPtDyspnea_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDyspnea_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDyspnea_1, 9, 2, 1, 1)

        self.labelPtBreathing = QLabel(self.frame)
        self.labelPtBreathing.setObjectName(u"labelPtBreathing")
        self.labelPtBreathing.setMaximumSize(QSize(150, 16777215))
        palette64 = QPalette()
        palette64.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette64.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette64.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette64.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette64.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette64.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette64.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette64.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette64.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette64.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette64.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette64.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette64.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette64.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette64.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette64.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette64.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette64.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette64.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette64.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette64.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette64.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette64.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette64.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette64.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette64.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette64.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette64.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette64.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette64.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette64.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette64.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette64.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette64.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette64.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette64.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette64.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette64.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette64.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette64.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette64.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette64.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette64.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette64.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette64.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtBreathing.setPalette(palette64)
        self.labelPtBreathing.setFont(font)
        self.labelPtBreathing.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtBreathing, 5, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 3)

        self.comboBoxPtUrination_2 = QComboBox(self.frame)
        self.comboBoxPtUrination_2.addItem("")
        self.comboBoxPtUrination_2.addItem("")
        self.comboBoxPtUrination_2.addItem("")
        self.comboBoxPtUrination_2.setObjectName(u"comboBoxPtUrination_2")
        palette65 = QPalette()
        palette65.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette65.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette65.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette65.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette65.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette65.setBrush(QPalette.Active, QPalette.Text, brush)
        palette65.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette65.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette65.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette65.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette65.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette65.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette65.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette65.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette65.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette65.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette65.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette65.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette65.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette65.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette65.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette65.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette65.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette65.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette65.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette65.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtUrination_2.setPalette(palette65)
        self.comboBoxPtUrination_2.setFont(font)
        self.comboBoxPtUrination_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtUrination_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtUrination_2, 18, 2, 1, 1)

        self.comboBoxPtDyspneaChoice = QComboBox(self.frame)
        self.comboBoxPtDyspneaChoice.addItem("")
        self.comboBoxPtDyspneaChoice.addItem("")
        self.comboBoxPtDyspneaChoice.setObjectName(u"comboBoxPtDyspneaChoice")
        palette66 = QPalette()
        palette66.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette66.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette66.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette66.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette66.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette66.setBrush(QPalette.Active, QPalette.Text, brush)
        palette66.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette66.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette66.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette66.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette66.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette66.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette66.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette66.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette66.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette66.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette66.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette66.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette66.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette66.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette66.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette66.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette66.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette66.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette66.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette66.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDyspneaChoice.setPalette(palette66)
        self.comboBoxPtDyspneaChoice.setFont(font)
        self.comboBoxPtDyspneaChoice.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxPtDyspneaChoice, 9, 1, 1, 1)

        self.comboBoxPtDefecation_1 = QComboBox(self.frame)
        self.comboBoxPtDefecation_1.addItem("")
        self.comboBoxPtDefecation_1.addItem("")
        self.comboBoxPtDefecation_1.addItem("")
        self.comboBoxPtDefecation_1.setObjectName(u"comboBoxPtDefecation_1")
        palette67 = QPalette()
        palette67.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette67.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette67.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette67.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette67.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette67.setBrush(QPalette.Active, QPalette.Text, brush)
        palette67.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette67.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette67.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette67.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette67.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette67.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette67.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette67.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette67.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette67.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette67.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette67.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette67.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette67.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette67.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette67.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette67.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette67.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette67.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDefecation_1.setPalette(palette67)
        self.comboBoxPtDefecation_1.setFont(font)
        self.comboBoxPtDefecation_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDefecation_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDefecation_1, 16, 1, 1, 1)

        self.comboBoxPtDyspnea_3 = QComboBox(self.frame)
        self.comboBoxPtDyspnea_3.addItem("")
        self.comboBoxPtDyspnea_3.addItem("")
        self.comboBoxPtDyspnea_3.setObjectName(u"comboBoxPtDyspnea_3")
        palette68 = QPalette()
        palette68.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette68.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette68.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette68.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette68.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette68.setBrush(QPalette.Active, QPalette.Text, brush)
        palette68.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette68.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette68.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette68.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette68.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette68.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette68.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette68.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette68.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette68.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette68.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette68.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette68.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette68.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette68.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette68.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette68.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette68.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette68.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette68.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDyspnea_3.setPalette(palette68)
        self.comboBoxPtDyspnea_3.setFont(font)
        self.comboBoxPtDyspnea_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDyspnea_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDyspnea_3, 10, 2, 1, 1)

        self.comboBoxPtMucousMembr_1 = QComboBox(self.frame)
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.setObjectName(u"comboBoxPtMucousMembr_1")
        palette69 = QPalette()
        palette69.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette69.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette69.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette69.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette69.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette69.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette69.setBrush(QPalette.Active, QPalette.Text, brush)
        palette69.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette69.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette69.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette69.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette69.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette69.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette69.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette69.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette69.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette69.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette69.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette69.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette69.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette69.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette69.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette69.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette69.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette69.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette69.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette69.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette69.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette69.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtMucousMembr_1.setPalette(palette69)
        self.comboBoxPtMucousMembr_1.setFont(font)
        self.comboBoxPtMucousMembr_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtMucousMembr_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtMucousMembr_1, 4, 1, 1, 2)

        self.labelPtUrination = QLabel(self.frame)
        self.labelPtUrination.setObjectName(u"labelPtUrination")
        self.labelPtUrination.setMaximumSize(QSize(150, 16777215))
        palette70 = QPalette()
        palette70.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette70.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette70.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette70.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette70.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette70.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette70.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette70.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette70.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette70.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette70.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette70.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette70.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette70.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette70.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette70.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette70.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette70.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette70.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette70.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette70.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette70.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette70.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette70.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette70.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette70.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette70.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette70.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette70.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette70.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette70.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette70.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette70.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette70.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette70.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette70.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette70.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette70.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette70.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette70.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette70.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette70.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette70.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette70.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette70.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette70.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette70.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette70.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtUrination.setPalette(palette70)
        self.labelPtUrination.setFont(font)
        self.labelPtUrination.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtUrination, 18, 0, 1, 1)

        self.comboBoxPtUrination_1 = QComboBox(self.frame)
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.setObjectName(u"comboBoxPtUrination_1")
        palette71 = QPalette()
        palette71.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette71.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette71.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette71.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette71.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette71.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette71.setBrush(QPalette.Active, QPalette.Text, brush)
        palette71.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette71.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette71.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette71.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette71.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette71.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette71.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette71.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette71.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette71.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette71.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette71.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette71.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette71.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette71.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette71.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette71.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette71.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette71.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette71.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette71.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette71.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette71.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtUrination_1.setPalette(palette71)
        self.comboBoxPtUrination_1.setFont(font)
        self.comboBoxPtUrination_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtUrination_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtUrination_1, 18, 1, 1, 1)

        self.comboBoxPtDefecation_3 = QComboBox(self.frame)
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.setObjectName(u"comboBoxPtDefecation_3")
        palette72 = QPalette()
        palette72.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette72.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette72.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette72.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette72.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette72.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette72.setBrush(QPalette.Active, QPalette.Text, brush)
        palette72.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette72.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette72.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette72.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette72.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette72.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette72.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette72.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette72.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette72.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette72.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette72.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette72.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette72.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette72.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette72.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette72.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette72.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette72.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette72.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette72.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette72.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette72.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette72.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette72.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDefecation_3.setPalette(palette72)
        self.comboBoxPtDefecation_3.setFont(font)
        self.comboBoxPtDefecation_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDefecation_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDefecation_3, 17, 1, 1, 2)

        self.labelPtSkinState = QLabel(self.frame)
        self.labelPtSkinState.setObjectName(u"labelPtSkinState")
        self.labelPtSkinState.setMaximumSize(QSize(150, 16777215))
        palette73 = QPalette()
        palette73.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette73.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette73.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette73.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette73.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette73.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette73.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette73.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette73.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette73.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette73.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette73.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette73.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette73.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette73.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette73.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette73.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette73.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette73.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette73.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette73.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette73.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette73.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette73.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette73.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette73.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette73.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette73.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette73.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette73.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette73.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette73.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette73.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette73.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette73.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette73.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette73.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette73.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette73.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette73.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette73.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette73.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette73.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette73.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette73.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette73.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette73.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette73.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSkinState.setPalette(palette73)
        self.labelPtSkinState.setFont(font)
        self.labelPtSkinState.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtSkinState, 2, 0, 1, 1)

        self.comboBoxPtHearthTone_2 = QComboBox(self.frame)
        self.comboBoxPtHearthTone_2.addItem("")
        self.comboBoxPtHearthTone_2.addItem("")
        self.comboBoxPtHearthTone_2.setObjectName(u"comboBoxPtHearthTone_2")
        palette74 = QPalette()
        palette74.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette74.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette74.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette74.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette74.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette74.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette74.setBrush(QPalette.Active, QPalette.Text, brush)
        palette74.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette74.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette74.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette74.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette74.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette74.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette74.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette74.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette74.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette74.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette74.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette74.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette74.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette74.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette74.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette74.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette74.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette74.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette74.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette74.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthTone_2.setPalette(palette74)
        self.comboBoxPtHearthTone_2.setFont(font)
        self.comboBoxPtHearthTone_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtHearthTone_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtHearthTone_2, 11, 2, 1, 1)

        self.comboBoxPtHearthNoiseChoice = QComboBox(self.frame)
        self.comboBoxPtHearthNoiseChoice.addItem("")
        self.comboBoxPtHearthNoiseChoice.addItem("")
        self.comboBoxPtHearthNoiseChoice.setObjectName(u"comboBoxPtHearthNoiseChoice")
        palette75 = QPalette()
        palette75.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette75.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette75.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette75.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette75.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette75.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette75.setBrush(QPalette.Active, QPalette.Text, brush)
        palette75.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette75.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette75.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette75.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette75.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette75.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette75.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette75.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette75.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette75.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette75.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette75.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette75.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette75.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette75.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette75.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette75.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette75.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette75.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette75.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthNoiseChoice.setPalette(palette75)
        self.comboBoxPtHearthNoiseChoice.setFont(font)
        self.comboBoxPtHearthNoiseChoice.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxPtHearthNoiseChoice, 13, 1, 1, 1)

        self.comboBoxPtWheezing_1 = QComboBox(self.frame)
        self.comboBoxPtWheezing_1.addItem("")
        self.comboBoxPtWheezing_1.addItem("")
        self.comboBoxPtWheezing_1.addItem("")
        self.comboBoxPtWheezing_1.setObjectName(u"comboBoxPtWheezing_1")
        palette76 = QPalette()
        palette76.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette76.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette76.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette76.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette76.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette76.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette76.setBrush(QPalette.Active, QPalette.Text, brush)
        palette76.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette76.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette76.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette76.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette76.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette76.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette76.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette76.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette76.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette76.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette76.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette76.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette76.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette76.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette76.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette76.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette76.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette76.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette76.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette76.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette76.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette76.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette76.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette76.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette76.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtWheezing_1.setPalette(palette76)
        self.comboBoxPtWheezing_1.setFont(font)
        self.comboBoxPtWheezing_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtWheezing_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtWheezing_1, 7, 2, 1, 1)

        self.labelPtStObjOther = QLabel(self.frame)
        self.labelPtStObjOther.setObjectName(u"labelPtStObjOther")
        self.labelPtStObjOther.setMaximumSize(QSize(150, 16777215))
        palette77 = QPalette()
        palette77.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette77.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette77.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette77.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette77.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette77.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette77.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette77.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette77.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette77.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette77.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette77.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette77.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette77.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette77.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette77.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette77.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette77.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette77.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette77.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette77.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette77.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette77.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette77.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette77.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette77.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette77.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette77.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette77.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette77.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette77.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette77.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette77.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette77.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette77.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette77.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette77.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette77.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette77.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette77.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette77.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette77.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette77.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette77.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette77.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette77.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette77.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette77.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtStObjOther.setPalette(palette77)
        self.labelPtStObjOther.setFont(font)
        self.labelPtStObjOther.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtStObjOther, 20, 0, 1, 1)

        self.comboBoxPtWheezing_3 = QComboBox(self.frame)
        self.comboBoxPtWheezing_3.addItem("")
        self.comboBoxPtWheezing_3.addItem("")
        self.comboBoxPtWheezing_3.addItem("")
        self.comboBoxPtWheezing_3.addItem("")
        self.comboBoxPtWheezing_3.setObjectName(u"comboBoxPtWheezing_3")
        palette78 = QPalette()
        palette78.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette78.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette78.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette78.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette78.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette78.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette78.setBrush(QPalette.Active, QPalette.Text, brush)
        palette78.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette78.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette78.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette78.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette78.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette78.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette78.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette78.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette78.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette78.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette78.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette78.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette78.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette78.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette78.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette78.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette78.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette78.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette78.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette78.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette78.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette78.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette78.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtWheezing_3.setPalette(palette78)
        self.comboBoxPtWheezing_3.setFont(font)
        self.comboBoxPtWheezing_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtWheezing_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtWheezing_3, 8, 2, 1, 1)

        self.comboBoxPtHearthTone_1 = QComboBox(self.frame)
        self.comboBoxPtHearthTone_1.addItem("")
        self.comboBoxPtHearthTone_1.addItem("")
        self.comboBoxPtHearthTone_1.addItem("")
        self.comboBoxPtHearthTone_1.setObjectName(u"comboBoxPtHearthTone_1")
        palette79 = QPalette()
        palette79.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette79.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette79.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette79.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette79.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette79.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette79.setBrush(QPalette.Active, QPalette.Text, brush)
        palette79.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette79.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette79.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette79.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette79.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette79.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette79.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette79.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette79.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette79.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette79.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette79.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette79.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette79.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette79.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette79.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette79.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette79.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette79.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette79.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette79.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette79.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette79.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthTone_1.setPalette(palette79)
        self.comboBoxPtHearthTone_1.setFont(font)
        self.comboBoxPtHearthTone_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtHearthTone_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtHearthTone_1, 11, 1, 1, 1)

        self.comboBoxPtWheezingChoice = QComboBox(self.frame)
        self.comboBoxPtWheezingChoice.addItem("")
        self.comboBoxPtWheezingChoice.addItem("")
        self.comboBoxPtWheezingChoice.setObjectName(u"comboBoxPtWheezingChoice")
        palette80 = QPalette()
        palette80.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette80.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette80.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette80.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette80.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette80.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette80.setBrush(QPalette.Active, QPalette.Text, brush)
        palette80.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette80.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette80.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette80.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette80.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette80.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette80.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette80.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette80.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette80.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette80.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette80.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette80.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette80.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette80.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette80.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette80.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette80.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette80.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette80.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette80.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette80.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette80.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtWheezingChoice.setPalette(palette80)
        self.comboBoxPtWheezingChoice.setFont(font)
        self.comboBoxPtWheezingChoice.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxPtWheezingChoice, 7, 1, 1, 1)

        self.comboBoxPtStomach_3 = QComboBox(self.frame)
        self.comboBoxPtStomach_3.addItem("")
        self.comboBoxPtStomach_3.addItem("")
        self.comboBoxPtStomach_3.setObjectName(u"comboBoxPtStomach_3")
        palette81 = QPalette()
        palette81.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette81.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette81.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette81.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette81.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette81.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette81.setBrush(QPalette.Active, QPalette.Text, brush)
        palette81.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette81.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette81.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette81.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette81.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette81.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette81.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette81.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette81.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette81.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette81.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette81.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette81.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette81.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette81.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette81.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette81.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette81.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette81.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette81.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette81.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette81.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette81.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtStomach_3.setPalette(palette81)
        self.comboBoxPtStomach_3.setFont(font)
        self.comboBoxPtStomach_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtStomach_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtStomach_3, 15, 1, 1, 2)

        self.comboBoxPtSkinState_2 = QComboBox(self.frame)
        self.comboBoxPtSkinState_2.addItem("")
        self.comboBoxPtSkinState_2.addItem("")
        self.comboBoxPtSkinState_2.setObjectName(u"comboBoxPtSkinState_2")
        palette82 = QPalette()
        palette82.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette82.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette82.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette82.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette82.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette82.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette82.setBrush(QPalette.Active, QPalette.Text, brush)
        palette82.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette82.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette82.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette82.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette82.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette82.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette82.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette82.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette82.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette82.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette82.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette82.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette82.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette82.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette82.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette82.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette82.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette82.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette82.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette82.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette82.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette82.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette82.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette82.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette82.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette82.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette82.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette82.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette82.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtSkinState_2.setPalette(palette82)
        self.comboBoxPtSkinState_2.setFont(font)
        self.comboBoxPtSkinState_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtSkinState_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtSkinState_2, 2, 2, 1, 1)

        self.labelPtMucousMembr = QLabel(self.frame)
        self.labelPtMucousMembr.setObjectName(u"labelPtMucousMembr")
        self.labelPtMucousMembr.setMaximumSize(QSize(150, 16777215))
        palette83 = QPalette()
        palette83.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette83.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette83.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette83.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette83.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette83.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette83.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette83.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette83.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette83.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette83.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette83.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette83.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette83.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette83.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette83.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette83.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette83.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette83.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette83.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette83.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette83.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette83.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette83.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette83.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette83.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette83.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette83.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette83.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette83.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette83.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette83.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette83.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette83.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette83.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette83.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette83.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette83.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette83.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette83.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette83.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette83.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette83.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette83.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette83.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette83.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette83.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette83.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtMucousMembr.setPalette(palette83)
        self.labelPtMucousMembr.setFont(font)
        self.labelPtMucousMembr.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtMucousMembr, 4, 0, 1, 1)

        self.comboBoxPtWheezing_2 = QComboBox(self.frame)
        self.comboBoxPtWheezing_2.addItem("")
        self.comboBoxPtWheezing_2.addItem("")
        self.comboBoxPtWheezing_2.addItem("")
        self.comboBoxPtWheezing_2.addItem("")
        self.comboBoxPtWheezing_2.setObjectName(u"comboBoxPtWheezing_2")
        palette84 = QPalette()
        palette84.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette84.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette84.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette84.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette84.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette84.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette84.setBrush(QPalette.Active, QPalette.Text, brush)
        palette84.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette84.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette84.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette84.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette84.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette84.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette84.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette84.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette84.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette84.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette84.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette84.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette84.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette84.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette84.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette84.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette84.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette84.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette84.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette84.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette84.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette84.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette84.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette84.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette84.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette84.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette84.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette84.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtWheezing_2.setPalette(palette84)
        self.comboBoxPtWheezing_2.setFont(font)
        self.comboBoxPtWheezing_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtWheezing_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtWheezing_2, 8, 1, 1, 1)

        self.labelPtStomach = QLabel(self.frame)
        self.labelPtStomach.setObjectName(u"labelPtStomach")
        self.labelPtStomach.setMaximumSize(QSize(150, 16777215))
        palette85 = QPalette()
        palette85.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette85.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette85.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette85.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette85.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette85.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette85.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette85.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette85.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette85.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette85.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette85.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette85.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette85.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette85.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette85.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette85.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette85.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette85.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette85.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette85.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette85.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette85.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette85.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette85.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette85.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette85.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette85.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette85.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette85.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette85.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette85.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette85.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette85.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette85.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette85.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette85.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette85.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette85.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette85.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette85.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette85.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette85.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette85.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette85.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette85.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette85.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette85.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtStomach.setPalette(palette85)
        self.labelPtStomach.setFont(font)
        self.labelPtStomach.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtStomach, 14, 0, 1, 1)

        self.comboBoxPtStomach_2 = QComboBox(self.frame)
        self.comboBoxPtStomach_2.addItem("")
        self.comboBoxPtStomach_2.addItem("")
        self.comboBoxPtStomach_2.addItem("")
        self.comboBoxPtStomach_2.setObjectName(u"comboBoxPtStomach_2")
        palette86 = QPalette()
        palette86.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette86.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette86.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette86.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette86.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette86.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette86.setBrush(QPalette.Active, QPalette.Text, brush)
        palette86.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette86.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette86.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette86.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette86.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette86.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette86.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette86.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette86.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette86.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette86.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette86.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette86.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette86.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette86.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette86.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette86.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette86.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette86.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette86.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette86.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette86.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette86.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette86.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette86.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette86.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette86.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette86.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette86.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtStomach_2.setPalette(palette86)
        self.comboBoxPtStomach_2.setFont(font)
        self.comboBoxPtStomach_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtStomach_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtStomach_2, 14, 2, 1, 1)

        self.comboBoxPtHearthNoise = QComboBox(self.frame)
        self.comboBoxPtHearthNoise.addItem("")
        self.comboBoxPtHearthNoise.addItem("")
        self.comboBoxPtHearthNoise.addItem("")
        self.comboBoxPtHearthNoise.setObjectName(u"comboBoxPtHearthNoise")
        palette87 = QPalette()
        palette87.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette87.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette87.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette87.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette87.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette87.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette87.setBrush(QPalette.Active, QPalette.Text, brush)
        palette87.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette87.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette87.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette87.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette87.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette87.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette87.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette87.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette87.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette87.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette87.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette87.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette87.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette87.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette87.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette87.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette87.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette87.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette87.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette87.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette87.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette87.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette87.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette87.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette87.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette87.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette87.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette87.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette87.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthNoise.setPalette(palette87)
        self.comboBoxPtHearthNoise.setFont(font)
        self.comboBoxPtHearthNoise.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtHearthNoise.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtHearthNoise, 13, 2, 1, 1)

        self.comboBoxPtLymphnode = QComboBox(self.frame)
        self.comboBoxPtLymphnode.addItem("")
        self.comboBoxPtLymphnode.addItem("")
        self.comboBoxPtLymphnode.setObjectName(u"comboBoxPtLymphnode")
        palette88 = QPalette()
        palette88.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette88.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette88.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette88.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette88.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette88.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette88.setBrush(QPalette.Active, QPalette.Text, brush)
        palette88.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette88.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette88.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette88.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette88.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette88.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette88.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette88.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette88.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette88.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette88.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette88.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette88.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette88.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette88.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette88.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette88.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette88.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette88.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette88.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette88.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette88.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette88.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette88.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette88.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette88.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette88.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette88.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette88.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtLymphnode.setPalette(palette88)
        self.comboBoxPtLymphnode.setFont(font)
        self.comboBoxPtLymphnode.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtLymphnode.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtLymphnode, 3, 1, 1, 2)

        self.plainTextEditPtStObjOther = QPlainTextEdit(self.frame)
        self.plainTextEditPtStObjOther.setObjectName(u"plainTextEditPtStObjOther")
        self.plainTextEditPtStObjOther.setMinimumSize(QSize(0, 60))
        self.plainTextEditPtStObjOther.setMaximumSize(QSize(16777215, 60))
        self.plainTextEditPtStObjOther.setFont(font)
        self.plainTextEditPtStObjOther.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.plainTextEditPtStObjOther, 20, 1, 1, 2)


        self.gridLayout_10.addWidget(self.frame, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.frame_templates = QFrame(self.obj_status)
        self.frame_templates.setObjectName(u"frame_templates")
        self.frame_templates.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_7 = QGridLayout(self.frame_templates)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setVerticalSpacing(1)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.comboBoxGeneralStTemplate = QComboBox(self.frame_templates)
        self.comboBoxGeneralStTemplate.addItem("")
        self.comboBoxGeneralStTemplate.setObjectName(u"comboBoxGeneralStTemplate")
        self.comboBoxGeneralStTemplate.setMaximumSize(QSize(16777215, 16777215))
        palette89 = QPalette()
        palette89.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette89.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette89.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette89.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette89.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette89.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette89.setBrush(QPalette.Active, QPalette.Text, brush)
        palette89.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette89.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette89.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette89.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette89.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette89.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette89.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette89.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette89.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette89.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette89.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette89.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette89.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette89.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette89.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette89.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette89.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette89.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette89.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette89.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette89.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette89.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette89.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette89.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette89.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette89.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette89.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette89.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette89.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxGeneralStTemplate.setPalette(palette89)
        self.comboBoxGeneralStTemplate.setFont(font)
        self.comboBoxGeneralStTemplate.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.comboBoxGeneralStTemplate, 2, 0, 1, 1)

        self.pushButtonAddNewTemplateGeneralSt = QPushButton(self.frame_templates)
        self.pushButtonAddNewTemplateGeneralSt.setObjectName(u"pushButtonAddNewTemplateGeneralSt")
        palette90 = QPalette()
        palette90.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette90.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette90.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette90.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette90.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette90.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette90.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette90.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette90.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette90.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette90.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette90.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette90.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette90.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette90.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette90.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette90.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette90.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette90.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette90.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette90.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette90.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette90.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette90.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette90.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette90.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette90.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette90.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette90.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette90.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette90.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette90.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette90.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette90.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette90.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette90.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette90.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette90.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonAddNewTemplateGeneralSt.setPalette(palette90)
        self.pushButtonAddNewTemplateGeneralSt.setFont(font4)
        self.pushButtonAddNewTemplateGeneralSt.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_7.addWidget(self.pushButtonAddNewTemplateGeneralSt, 4, 1, 1, 1)

        self.label = QLabel(self.frame_templates)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 2)

        self.pushButton_push_temp = QPushButton(self.frame_templates)
        self.pushButton_push_temp.setObjectName(u"pushButton_push_temp")
        palette91 = QPalette()
        palette91.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette91.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette91.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette91.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette91.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette91.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette91.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette91.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette91.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette91.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette91.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette91.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette91.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette91.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette91.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette91.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette91.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette91.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette91.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette91.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette91.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette91.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette91.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette91.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette91.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette91.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette91.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette91.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette91.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette91.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette91.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette91.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette91.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette91.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette91.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette91.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette91.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette91.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette91.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette91.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette91.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette91.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette91.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette91.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette91.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette91.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette91.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette91.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButton_push_temp.setPalette(palette91)
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

        self.gridLayout_7.addWidget(self.pushButton_push_temp, 2, 1, 1, 1)

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

        self.gridLayout_7.addWidget(self.lineEdit_new_template_name, 4, 0, 1, 1)

        self.label_3 = QLabel(self.frame_templates)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_templates)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_templates)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)


        self.gridLayout_10.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_18, 1, 2, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/stethoscope_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.obj_status, icon3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

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
        palette92 = QPalette()
        palette92.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette92.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette92.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette92.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette92.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette92.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette92.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette92.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette92.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette92.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette92.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette92.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette92.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette92.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette92.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette92.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette92.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette92.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette92.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette92.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette92.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette92.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette92.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette92.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette92.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette92.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette92.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette92.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette92.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette92.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette92.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette92.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette92.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette92.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette92.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette92.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette92.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette92.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette92.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette92.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette92.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette92.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette92.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette92.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette92.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
        palette92.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette92.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette92.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.pushButtonHelp.setPalette(palette92)
        self.pushButtonHelp.setFont(font4)
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
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHelp.setIcon(icon4)

        self.verticalLayout_6.addWidget(self.pushButtonHelp)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.pushButtonNotSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette93 = QPalette()
        palette93.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette93.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette93.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette93.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette93.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette93.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette93.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette93.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette93.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette93.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette93.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette93.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette93.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette93.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette93.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette93.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette93.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette93.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette93.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette93.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette93.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette93.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette93.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette93.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette93.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette93.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette93.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette93.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette93.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette93.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette93.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette93.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette93.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette93.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette93.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette93.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette93.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette93.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette93.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette93.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette93.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette93.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette93.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette93.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette93.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette93.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette93.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette93.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonNotSaveExit.setPalette(palette93)
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
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon5)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette94 = QPalette()
        palette94.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush23 = QBrush(QColor(92, 158, 173, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette94.setBrush(QPalette.Active, QPalette.Button, brush23)
        palette94.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette94.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette94.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette94.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette94.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette94.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette94.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette94.setBrush(QPalette.Active, QPalette.Base, brush23)
        palette94.setBrush(QPalette.Active, QPalette.Window, brush23)
        palette94.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette94.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette94.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette94.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette94.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette94.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette94.setBrush(QPalette.Inactive, QPalette.Button, brush23)
        palette94.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette94.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette94.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette94.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette94.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette94.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette94.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette94.setBrush(QPalette.Inactive, QPalette.Base, brush23)
        palette94.setBrush(QPalette.Inactive, QPalette.Window, brush23)
        palette94.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette94.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette94.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette94.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette94.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette94.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette94.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette94.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette94.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette94.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette94.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette94.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette94.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette94.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette94.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette94.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette94.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette94.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette94.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette94.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette94.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonSaveExit.setPalette(palette94)
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
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveExit.setIcon(icon6)
        self.pushButtonSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonSaveExit)


        self.horizontalLayout_4.addWidget(self.groupBox_wom)


        self.verticalLayout.addWidget(self.main)

        QWidget.setTabOrder(self.comboBox_jaloby_templates, self.pushButton_push_temp_jaloby)
        QWidget.setTabOrder(self.pushButton_push_temp_jaloby, self.lineEdit_new_template_name_jaloby)
        QWidget.setTabOrder(self.lineEdit_new_template_name_jaloby, self.pushButtonAddNewTemplate_jaloby)
        QWidget.setTabOrder(self.pushButtonAddNewTemplate_jaloby, self.plainTextEditPtComplaints)
        QWidget.setTabOrder(self.plainTextEditPtComplaints, self.lineEditPtWeight)
        QWidget.setTabOrder(self.lineEditPtWeight, self.lineEditPtGrowth)
        QWidget.setTabOrder(self.lineEditPtGrowth, self.lineEditPtBloodPreasureSist)
        QWidget.setTabOrder(self.lineEditPtBloodPreasureSist, self.lineEditPtBloodPreasureDiast)
        QWidget.setTabOrder(self.lineEditPtBloodPreasureDiast, self.lineEditPtBreathingSpeed)
        QWidget.setTabOrder(self.lineEditPtBreathingSpeed, self.lineEditSaturation)
        QWidget.setTabOrder(self.lineEditSaturation, self.lineEditPtTemperature)
        QWidget.setTabOrder(self.lineEditPtTemperature, self.lineEditPtPulse)
        QWidget.setTabOrder(self.lineEditPtPulse, self.pushButton_random_values)
        QWidget.setTabOrder(self.pushButton_random_values, self.pushButton_add_to_diag)
        QWidget.setTabOrder(self.pushButton_add_to_diag, self.comboBoxPtDrugs)
        QWidget.setTabOrder(self.comboBoxPtDrugs, self.plainTextEditPtDrugs)
        QWidget.setTabOrder(self.plainTextEditPtDrugs, self.checkBox_GB)
        QWidget.setTabOrder(self.checkBox_GB, self.checkBox_Hyperthyreosis)
        QWidget.setTabOrder(self.checkBox_Hyperthyreosis, self.checkBox_SD)
        QWidget.setTabOrder(self.checkBox_SD, self.checkBox_NRS)
        QWidget.setTabOrder(self.checkBox_NRS, self.checkBox_IBS)
        QWidget.setTabOrder(self.checkBox_IBS, self.checkBox_Stroke)
        QWidget.setTabOrder(self.checkBox_Stroke, self.checkBox_B20)
        QWidget.setTabOrder(self.checkBox_B20, self.checkBox_Fat)
        QWidget.setTabOrder(self.checkBox_Fat, self.checkBox_other)
        QWidget.setTabOrder(self.checkBox_other, self.checkBox_Astma)
        QWidget.setTabOrder(self.checkBox_Astma, self.checkBox_Gastro)
        QWidget.setTabOrder(self.checkBox_Gastro, self.checkBox_HCV)
        QWidget.setTabOrder(self.checkBox_HCV, self.plainTextEdit_other_chronic_diseases)
        QWidget.setTabOrder(self.plainTextEdit_other_chronic_diseases, self.checkBox_Hypothyreosis)
        QWidget.setTabOrder(self.checkBox_Hypothyreosis, self.checkBox_Atherosclerosis_BCA)
        QWidget.setTabOrder(self.checkBox_Atherosclerosis_BCA, self.checkBox_Atherosclerosis_legs)
        QWidget.setTabOrder(self.checkBox_Atherosclerosis_legs, self.checkBox_HBsAg)
        QWidget.setTabOrder(self.checkBox_HBsAg, self.plainTextEditPtAnamMorbi)
        QWidget.setTabOrder(self.plainTextEditPtAnamMorbi, self.comboBoxPtAllergStatus)
        QWidget.setTabOrder(self.comboBoxPtAllergStatus, self.plainTextEditPtAnamAllerg)
        QWidget.setTabOrder(self.plainTextEditPtAnamAllerg, self.comboBoxPtAnamEpid)
        QWidget.setTabOrder(self.comboBoxPtAnamEpid, self.plainTextEditPtAnamEpid)
        QWidget.setTabOrder(self.plainTextEditPtAnamEpid, self.comboBoxPtSocialStatus)
        QWidget.setTabOrder(self.comboBoxPtSocialStatus, self.checkBoxPtNeedSickList)
        QWidget.setTabOrder(self.checkBoxPtNeedSickList, self.checkBoxPtNeedSickList_2)
        QWidget.setTabOrder(self.checkBoxPtNeedSickList_2, self.comboBoxWorkListInfo)
        QWidget.setTabOrder(self.comboBoxWorkListInfo, self.lineEditPtWorkPlace)
        QWidget.setTabOrder(self.lineEditPtWorkPlace, self.lineEditPtWorkPosition)
        QWidget.setTabOrder(self.lineEditPtWorkPosition, self.lineEditPtWorkListNumber1_1)
        QWidget.setTabOrder(self.lineEditPtWorkListNumber1_1, self.lineEditPtWorkListNumber_issued)
        QWidget.setTabOrder(self.lineEditPtWorkListNumber_issued, self.dateEditPtWorkListDate1_1)
        QWidget.setTabOrder(self.dateEditPtWorkListDate1_1, self.dateEditPtWorkListDate1_2)
        QWidget.setTabOrder(self.dateEditPtWorkListDate1_2, self.dateEditPtWorkListDateOpening)
        QWidget.setTabOrder(self.dateEditPtWorkListDateOpening, self.comboBoxWorkList_prognosis)
        QWidget.setTabOrder(self.comboBoxWorkList_prognosis, self.comboBoxGeneralStTemplate)
        QWidget.setTabOrder(self.comboBoxGeneralStTemplate, self.pushButton_push_temp)
        QWidget.setTabOrder(self.pushButton_push_temp, self.lineEdit_new_template_name)
        QWidget.setTabOrder(self.lineEdit_new_template_name, self.pushButtonAddNewTemplateGeneralSt)
        QWidget.setTabOrder(self.pushButtonAddNewTemplateGeneralSt, self.comboBoxPtGeneralState)
        QWidget.setTabOrder(self.comboBoxPtGeneralState, self.comboBoxPtSkinState_1)
        QWidget.setTabOrder(self.comboBoxPtSkinState_1, self.comboBoxPtSkinState_2)
        QWidget.setTabOrder(self.comboBoxPtSkinState_2, self.comboBoxPtLymphnode)
        QWidget.setTabOrder(self.comboBoxPtLymphnode, self.comboBoxPtMucousMembr_1)
        QWidget.setTabOrder(self.comboBoxPtMucousMembr_1, self.comboBoxPtBreathing_1)
        QWidget.setTabOrder(self.comboBoxPtBreathing_1, self.comboBoxPtBreathing_2)
        QWidget.setTabOrder(self.comboBoxPtBreathing_2, self.comboBoxPtBreathing_3)
        QWidget.setTabOrder(self.comboBoxPtBreathing_3, self.comboBoxPtWheezingChoice)
        QWidget.setTabOrder(self.comboBoxPtWheezingChoice, self.comboBoxPtWheezing_1)
        QWidget.setTabOrder(self.comboBoxPtWheezing_1, self.comboBoxPtWheezing_2)
        QWidget.setTabOrder(self.comboBoxPtWheezing_2, self.comboBoxPtWheezing_3)
        QWidget.setTabOrder(self.comboBoxPtWheezing_3, self.comboBoxPtDyspneaChoice)
        QWidget.setTabOrder(self.comboBoxPtDyspneaChoice, self.comboBoxPtDyspnea_1)
        QWidget.setTabOrder(self.comboBoxPtDyspnea_1, self.comboBoxPtDyspnea_2)
        QWidget.setTabOrder(self.comboBoxPtDyspnea_2, self.comboBoxPtDyspnea_3)
        QWidget.setTabOrder(self.comboBoxPtDyspnea_3, self.comboBoxPtHearthTone_1)
        QWidget.setTabOrder(self.comboBoxPtHearthTone_1, self.comboBoxPtHearthTone_2)
        QWidget.setTabOrder(self.comboBoxPtHearthTone_2, self.comboBoxPtHearthTone_3)
        QWidget.setTabOrder(self.comboBoxPtHearthTone_3, self.comboBoxPtHearthNoiseChoice)
        QWidget.setTabOrder(self.comboBoxPtHearthNoiseChoice, self.comboBoxPtHearthNoise)
        QWidget.setTabOrder(self.comboBoxPtHearthNoise, self.comboBoxPtStomach_1)
        QWidget.setTabOrder(self.comboBoxPtStomach_1, self.comboBoxPtStomach_2)
        QWidget.setTabOrder(self.comboBoxPtStomach_2, self.comboBoxPtStomach_3)
        QWidget.setTabOrder(self.comboBoxPtStomach_3, self.comboBoxPtDefecation_1)
        QWidget.setTabOrder(self.comboBoxPtDefecation_1, self.comboBoxPtDefecation_2)
        QWidget.setTabOrder(self.comboBoxPtDefecation_2, self.comboBoxPtDefecation_3)
        QWidget.setTabOrder(self.comboBoxPtDefecation_3, self.comboBoxPtUrination_1)
        QWidget.setTabOrder(self.comboBoxPtUrination_1, self.comboBoxPtUrination_2)
        QWidget.setTabOrder(self.comboBoxPtUrination_2, self.comboBoxPtUrination_3)
        QWidget.setTabOrder(self.comboBoxPtUrination_3, self.plainTextEditPtStObjOther)
        QWidget.setTabOrder(self.plainTextEditPtStObjOther, self.pushButtonHelp)
        QWidget.setTabOrder(self.pushButtonHelp, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.pushButtonNotSaveExit)

        self.retranslateUi(StObj)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StObj)
    # setupUi

    def retranslateUi(self, StObj):
        StObj.setWindowTitle(QCoreApplication.translate("StObj", u"Form", None))
        self.label_Pt_info.setText(QCoreApplication.translate("StObj", u"PatientInfo\n"
"fff", None))
        self.labelTimeline.setText("")
        self.label_5.setText(QCoreApplication.translate("StObj", u"\u0416\u0430\u043b\u043e\u0431\u044b \u043d\u0430:", None))
        self.plainTextEditPtComplaints.setPlaceholderText(QCoreApplication.translate("StObj", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0436\u0430\u043b\u043e\u0431\u044b \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.label_imt.setText("")
        self.labelPtGrowth.setText(QCoreApplication.translate("StObj", u"\u0420\u043e\u0441\u0442, \u0441\u043c", None))
        self.labelPtSaturation.setText(QCoreApplication.translate("StObj", u"\u0421\u0430\u0442\u0443\u0440\u0430\u0446\u0438\u044f, %", None))
        self.labelPtPulse.setText(QCoreApplication.translate("StObj", u"\u0427\u0421\u0421, \u0432 1 \u043c\u0438\u043d", None))
        self.labelPtTemperatureCelcium.setText(QCoreApplication.translate("StObj", u"<html><head/><body><p>t \u0442\u0435\u043b\u0430, <span style=\" vertical-align:super;\">o</span>\u0421</p></body></html>", None))
        self.labelPtWeight.setText(QCoreApplication.translate("StObj", u"\u0412\u0435\u0441, \u043a\u0433", None))
        self.labelPtBreathingSpeed.setText(QCoreApplication.translate("StObj", u"\u0427\u0414\u0414, \u0432 1 \u043c\u0438\u043d", None))
        self.label_7.setText(QCoreApplication.translate("StObj", u"\u0410\u043d\u0442\u0440\u043e\u043f\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_2.setText("")
        self.labelPtBloodPreasure.setText(QCoreApplication.translate("StObj", u"\u0410\u0414, \u043c\u043c.\u0440\u0442.\u0441\u0442.", None))
        self.labelooo.setText(QCoreApplication.translate("StObj", u"/", None))
        self.pushButton_random_values.setText(QCoreApplication.translate("StObj", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.pushButton_add_to_diag.setText(QCoreApplication.translate("StObj", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.checkBox_Fat.setText(QCoreApplication.translate("StObj", u"\u041e\u0436\u0438\u0440\u0435\u043d\u0438\u0435", None))
        self.checkBox_Atherosclerosis_legs.setText(QCoreApplication.translate("StObj", u"\u0410\u0442\u0435\u0440\u043e\u0441\u043a\u043b\u0435\u0440\u043e\u0437 \u0430\u0430 \u043d/\u043a", None))
        self.checkBox_Stroke.setText(QCoreApplication.translate("StObj", u"\u041f\u041e\u041d\u041c\u041a", None))
        self.label_11.setText(QCoreApplication.translate("StObj", u"\u0425\u0440\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u044f", None))
        self.checkBox_other.setText(QCoreApplication.translate("StObj", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))
        self.checkBox_Hyperthyreosis.setText(QCoreApplication.translate("StObj", u"\u0413\u0438\u043f\u0435\u0440\u0442\u0438\u0440\u0435\u043e\u0437", None))
        self.checkBox_Hypothyreosis.setText(QCoreApplication.translate("StObj", u"\u0413\u0438\u043f\u043e\u0442\u0438\u0440\u0435\u043e\u0437", None))
        self.checkBox_IBS.setText(QCoreApplication.translate("StObj", u"\u0418\u0411\u0421 / \u0421\u041d / \u041f\u0418\u041a\u0421 / \u0410\u041a\u0428 / \u0427\u041a\u0412", None))
        self.checkBox_Gastro.setText(QCoreApplication.translate("StObj", u"\u0413\u0430\u0441\u0442\u0440\u0438\u0442 / \u042f\u0411\u0416 / \u042f\u0411\u0414\u041f\u041a", None))
        self.checkBox_B20.setText(QCoreApplication.translate("StObj", u"\u0412\u0418\u0427-\u0438\u043d\u0444\u0435\u043a\u0446\u0438\u044f", None))
        self.checkBox_HBsAg.setText(QCoreApplication.translate("StObj", u"\u0412\u0438\u0440\u0443\u0441\u043d\u044b\u0439 \u0433\u0435\u043f\u0430\u0442\u0438\u0442 \u0412", None))
        self.checkBox_Atherosclerosis_BCA.setText(QCoreApplication.translate("StObj", u"\u0410\u0442\u0435\u0440\u043e\u0441\u043a\u043b\u0435\u0440\u043e\u0437 \u0411\u0426\u0410", None))
        self.checkBox_Astma.setText(QCoreApplication.translate("StObj", u"\u0411\u0440\u043e\u043d\u0445\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0430\u0441\u0442\u043c\u0430", None))
        self.checkBox_NRS.setText(QCoreApplication.translate("StObj", u"\u041d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u044f \u0440\u0438\u0442\u043c\u0430 \u0441\u0435\u0440\u0434\u0446\u0430", None))
        self.checkBox_GB.setText(QCoreApplication.translate("StObj", u"\u0413\u0438\u043f\u0435\u0440\u0442\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0431\u043e\u043b\u0435\u0437\u043d\u044c", None))
        self.plainTextEdit_other_chronic_diseases.setPlaceholderText(QCoreApplication.translate("StObj", u"\u043a\u0440\u0430\u0442\u043a\u043e \u0440\u0430\u0441\u043f\u0438\u0448\u0438\u0442\u0435 \u0434\u0440\u0443\u0433\u0438\u0435 \u0445\u0440\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u044f", None))
        self.checkBox_SD.setText(QCoreApplication.translate("StObj", u"\u0421\u0430\u0445\u0430\u0440\u043d\u044b\u0439 \u0434\u0438\u0430\u0431\u0435\u0442", None))
        self.checkBox_HCV.setText(QCoreApplication.translate("StObj", u"\u0412\u0438\u0440\u0443\u0441\u043d\u044b\u0439 \u0433\u0435\u043f\u0430\u0442\u0438\u0442 \u0421", None))
        self.comboBoxPtDrugs.setItemText(0, QCoreApplication.translate("StObj", u"\u041d\u0435 \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442", None))
        self.comboBoxPtDrugs.setItemText(1, QCoreApplication.translate("StObj", u"\u0421\u0438\u0442\u0443\u0430\u0446\u0438\u043e\u043d\u043d\u043e", None))
        self.comboBoxPtDrugs.setItemText(2, QCoreApplication.translate("StObj", u"\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u043e", None))

        self.plainTextEditPtDrugs.setPlaceholderText(QCoreApplication.translate("StObj", u"\u043f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0438\u0442\u0435 \u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442\u044b \u0441 \u0434\u043e\u0437\u043e\u0439, \u0440\u0435\u0436\u0438\u043c\u043e\u043c \u0438 \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c\u044e \u043f\u0440\u0438\u0435\u043c\u0430", None))
        self.label_8.setText(QCoreApplication.translate("StObj", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u043c\u044b\u0435 \u043c\u0435\u0434\u0438\u043a\u0430\u043c\u0435\u043d\u0442\u044b", None))
        self.comboBox_jaloby_templates.setItemText(0, "")

        self.pushButtonAddNewTemplate_jaloby.setText(QCoreApplication.translate("StObj", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.label_14.setText(QCoreApplication.translate("StObj", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u0436\u0430\u043b\u043e\u0431", None))
        self.pushButton_push_temp_jaloby.setText(QCoreApplication.translate("StObj", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit_new_template_name_jaloby.setText("")
        self.lineEdit_new_template_name_jaloby.setPlaceholderText(QCoreApplication.translate("StObj", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_15.setText(QCoreApplication.translate("StObj", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.label_16.setText(QCoreApplication.translate("StObj", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jaloby_page), QCoreApplication.translate("StObj", u"\u0416\u0430\u043b\u043e\u0431\u044b, \u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442\u044b, \u0447\u0438\u0441\u043b\u043e\u0432\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.comboBoxPtAnamEpid.setItemText(0, QCoreApplication.translate("StObj", u"\u0421\u043f\u043e\u043a\u043e\u0439\u043d\u044b\u0439", None))
        self.comboBoxPtAnamEpid.setItemText(1, QCoreApplication.translate("StObj", u"\u043e\u0442\u044f\u0433\u043e\u0449\u0435\u043d", None))

        self.label_10.setText(QCoreApplication.translate("StObj", u"\u042d\u043f\u0438\u0434\u0435\u043c\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.plainTextEditPtAnamEpid.setPlaceholderText(QCoreApplication.translate("StObj", u"\u041f\u0440\u0438 \u043e\u0442\u044f\u0433\u043e\u0449\u0435\u043d\u043d\u043e\u043c \u044d\u043f\u0438\u0434.\u0430\u043d\u0430\u043c\u043d\u0435\u0437\u0435 - \u0440\u0430\u0441\u043f\u0438\u0448\u0438\u0442\u0435 \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435, \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b \u0438 \u0442.\u0434.", None))
        self.label_6.setText(QCoreApplication.translate("StObj", u"\u0410\u043d\u0430\u043c\u043d\u0435\u0437 \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u044f", None))
        self.plainTextEditPtAnamMorbi.setPlaceholderText(QCoreApplication.translate("StObj", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0430\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.label_9.setText(QCoreApplication.translate("StObj", u"\u0410\u043b\u043b\u0435\u0440\u0433\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.comboBoxPtAllergStatus.setItemText(0, QCoreApplication.translate("StObj", u"\u041e\u0442\u0440\u0438\u0446\u0430\u0435\u0442", None))
        self.comboBoxPtAllergStatus.setItemText(1, QCoreApplication.translate("StObj", u"\u0415\u0421\u0422\u042c", None))

        self.plainTextEditPtAnamAllerg.setPlaceholderText(QCoreApplication.translate("StObj", u"\u041f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438 \u0430\u043b\u043b\u0435\u0440\u0433\u0438\u0438: \u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043b\u0435\u043a.\u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442 \u0438 \u0442\u0438\u043f \u0430\u043b\u043b\u0435\u0440\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0440\u0435\u0430\u043a\u0446\u0438\u0438 \u043d\u0430 \u043d\u0435\u0433\u043e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.anamnesis_page), QCoreApplication.translate("StObj", u"\u0410\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.comboBoxWorkList_prognosis.setItemText(0, "")
        self.comboBoxWorkList_prognosis.setItemText(1, QCoreApplication.translate("StObj", u"\u0411\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439", None))
        self.comboBoxWorkList_prognosis.setItemText(2, QCoreApplication.translate("StObj", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0431\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439", None))
        self.comboBoxWorkList_prognosis.setItemText(3, QCoreApplication.translate("StObj", u"\u0421\u043e\u043c\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439", None))
        self.comboBoxWorkList_prognosis.setItemText(4, QCoreApplication.translate("StObj", u"\u041d\u0435\u0431\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439", None))

        self.labelPtSickListInfo.setText(QCoreApplication.translate("StObj", u"\u041b\u041d:", None))
        self.label_13.setText(QCoreApplication.translate("StObj", u"\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0430\u043d\u0430\u043c\u043d\u0435\u0437 \u0438 \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u0438\u0437\u0430 \u043d\u0435\u0442\u0440\u0443\u0434\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438", None))
        self.dateEditPtWorkListDateOpening.setDisplayFormat(QCoreApplication.translate("StObj", u"dd.MM.yyyy", None))
        self.labelPtWorkListDateOpening.setText(QCoreApplication.translate("StObj", u"\u041d\u0430 \u043b\u0438\u0441\u0442\u0435 \u043d\u0435\u0442\u0440\u0443\u0434\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438 \u0441:", None))
        self.labelPtWorkPlace.setText(QCoreApplication.translate("StObj", u"\u041c\u0435\u0441\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u044b:", None))
        self.labelPtWorkListNumber_3.setText(QCoreApplication.translate("StObj", u"<html><head/><body><p align=\"center\">\u043f\u043e</p></body></html>", None))
        self.comboBoxPtSocialStatus.setItemText(0, QCoreApplication.translate("StObj", u"\u0411\u0435\u0437\u0440\u0430\u0431\u043e\u0442\u043d\u044b\u0439", None))
        self.comboBoxPtSocialStatus.setItemText(1, QCoreApplication.translate("StObj", u"\u041f\u0435\u043d\u0441\u0438\u043e\u043d\u0435\u0440", None))
        self.comboBoxPtSocialStatus.setItemText(2, QCoreApplication.translate("StObj", u"\u0420\u0430\u0431\u043e\u0442\u0430\u0435\u0442, \u0443\u0441\u0442\u0440\u043e\u0435\u043d \u043e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u043e", None))
        self.comboBoxPtSocialStatus.setItemText(3, QCoreApplication.translate("StObj", u"\u041d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0430 \u0443\u0447\u0435\u0442\u0435 \u0432 \u0426\u0417\u041d", None))
        self.comboBoxPtSocialStatus.setItemText(4, QCoreApplication.translate("StObj", u"\u0418\u041f", None))
        self.comboBoxPtSocialStatus.setItemText(5, QCoreApplication.translate("StObj", u"\u0418\u043d\u0432\u0430\u043b\u0438\u0434 I \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.comboBoxPtSocialStatus.setItemText(6, QCoreApplication.translate("StObj", u"\u0418\u043d\u0432\u0430\u043b\u0438\u0434 II \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.comboBoxPtSocialStatus.setItemText(7, QCoreApplication.translate("StObj", u"\u0418\u043d\u0432\u0430\u043b\u0438\u0434 III \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.comboBoxPtSocialStatus.setItemText(8, QCoreApplication.translate("StObj", u"\u0423\u0447\u0430\u0449\u0438\u0439\u0441\u044f \u0448\u043a\u043e\u043b\u044b", None))
        self.comboBoxPtSocialStatus.setItemText(9, QCoreApplication.translate("StObj", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442", None))
        self.comboBoxPtSocialStatus.setItemText(10, QCoreApplication.translate("StObj", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442 \u0412\u0423\u0417", None))

        self.labelPtWorkListDateOpening_2.setText(QCoreApplication.translate("StObj", u"(\u043f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0439 \u041b\u041d)", None))
        self.labelPtSickListInfo_2.setText(QCoreApplication.translate("StObj", u"\u0422\u0440\u0443\u0434\u043e\u0432\u043e\u0439 \u043f\u0440\u043e\u0433\u043d\u043e\u0437:", None))
        self.checkBoxPtNeedSickList_2.setText(QCoreApplication.translate("StObj", u"\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0439", None))
        self.labelPtSocialStatus.setText(QCoreApplication.translate("StObj", u"\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441:", None))
        self.labelPtWorkListS.setText(QCoreApplication.translate("StObj", u"<html><head/><body><p align=\"right\">c</p></body></html>", None))
        self.dateEditPtWorkListDate1_1.setDisplayFormat(QCoreApplication.translate("StObj", u"dd.MM.yyyy", None))
        self.labelPtWorkListNumber_2.setText(QCoreApplication.translate("StObj", u"\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d:", None))
        self.labelPtWorkPosition.setText(QCoreApplication.translate("StObj", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.labelPtWorkListNumber.setText(QCoreApplication.translate("StObj", u"\u041d\u043e\u043c\u0435\u0440 \u041b\u041d:", None))
        self.checkBoxPtNeedSickList.setText(QCoreApplication.translate("StObj", u"\u041d\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u041b\u041d", None))
        self.comboBoxWorkListInfo.setItemText(0, QCoreApplication.translate("StObj", u"\u043d\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f", None))
        self.comboBoxWorkListInfo.setItemText(1, QCoreApplication.translate("StObj", u"\u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0430 \u041b\u041d", None))
        self.comboBoxWorkListInfo.setItemText(2, QCoreApplication.translate("StObj", u"\u043d\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u043f\u0435\u0440\u0432\u0438\u0447\u043d\u043e\u043c \u041b\u041d", None))

        self.dateEditPtWorkListDate1_2.setDisplayFormat(QCoreApplication.translate("StObj", u"dd.MM.yyyy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.work_page), QCoreApplication.translate("StObj", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u043d\u0435\u0441\u0442\u0440\u0443\u0434\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438", None))
        self.labelPtHearthNoise.setText(QCoreApplication.translate("StObj", u"\u0428\u0443\u043c\u044b \u0441\u0435\u0440\u0434\u0446\u0430:", None))
        self.comboBoxPtSkinState_1.setItemText(0, QCoreApplication.translate("StObj", u"\u0444\u0438\u0437\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0435", None))
        self.comboBoxPtSkinState_1.setItemText(1, QCoreApplication.translate("StObj", u"\u0433\u0438\u043f\u0435\u0440\u0435\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u044b", None))
        self.comboBoxPtSkinState_1.setItemText(2, QCoreApplication.translate("StObj", u"\u0431\u043b\u0435\u0434\u043d\u043e\u0432\u0430\u0442\u044b\u0435", None))
        self.comboBoxPtSkinState_1.setItemText(3, QCoreApplication.translate("StObj", u"\u0431\u043b\u0435\u0434\u043d\u044b\u0435", None))
        self.comboBoxPtSkinState_1.setItemText(4, QCoreApplication.translate("StObj", u"\u043c\u0440\u0430\u043c\u043e\u0440\u043d\u044b\u0435", None))
        self.comboBoxPtSkinState_1.setItemText(5, QCoreApplication.translate("StObj", u"\u0438\u043a\u0442\u0435\u0440\u0438\u0447\u043d\u044b\u0435", None))

        self.labelPtGeneralState.setText(QCoreApplication.translate("StObj", u"\u041e\u0431\u0449\u0435\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435:", None))
        self.labelPtDyspnea.setText(QCoreApplication.translate("StObj", u"\u041e\u0434\u044b\u0448\u043a\u0430:", None))
        self.labelPtWheezing.setText(QCoreApplication.translate("StObj", u"\u0425\u0440\u0438\u043f\u044b:", None))
        self.comboBoxPtStomach_1.setItemText(0, QCoreApplication.translate("StObj", u"\u043d\u0435\u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d", None))
        self.comboBoxPtStomach_1.setItemText(1, QCoreApplication.translate("StObj", u"\u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u043d\u044b\u0439, \u0431\u043e\u043b\u044c\u0448\u0435 \u0432 \u044d\u043f\u0438\u0433\u0430\u0441\u0442\u0440\u0438\u0438", None))
        self.comboBoxPtStomach_1.setItemText(2, QCoreApplication.translate("StObj", u"\u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u043d\u044b\u0439, \u0431\u043e\u043b\u044c\u0448\u0435 \u0432 \u043f\u043e\u0434\u0432\u0437\u0434\u043e\u0448\u043d\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438", None))
        self.comboBoxPtStomach_1.setItemText(3, QCoreApplication.translate("StObj", u"\u0434\u043e\u0441\u043a\u043e\u043e\u0431\u0440\u0430\u0437\u043d\u044b\u0439", None))

        self.comboBoxPtBreathing_3.setItemText(0, QCoreApplication.translate("StObj", u"\u043f\u0440\u043e\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0432\u043e \u0432\u0441\u0435 \u043e\u0442\u0434\u0435\u043b\u044b", None))
        self.comboBoxPtBreathing_3.setItemText(1, QCoreApplication.translate("StObj", u"\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d\u043e \u0432 \u043d\u0438\u0436\u043d\u0438\u0445 \u043e\u0442\u0434\u0435\u043b\u0430\u0445", None))
        self.comboBoxPtBreathing_3.setItemText(2, "")

        self.comboBoxPtUrination_3.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtUrination_3.setItemText(1, QCoreApplication.translate("StObj", u"5-6 \u0440\u0430\u0437 \u0432 \u0441\u0443\u0442\u043a\u0438", None))
        self.comboBoxPtUrination_3.setItemText(2, QCoreApplication.translate("StObj", u"8-10 \u0440\u0430\u0437 \u0432 \u0441\u0443\u0442\u043a\u0438", None))
        self.comboBoxPtUrination_3.setItemText(3, QCoreApplication.translate("StObj", u"\u043d\u0438\u043a\u0442\u0443\u0440\u0438\u044f", None))

        self.comboBoxPtBreathing_1.setItemText(0, QCoreApplication.translate("StObj", u"\u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e\u0435, \u0447\u0435\u0440\u0435\u0437 \u043d\u043e\u0441", None))
        self.comboBoxPtBreathing_1.setItemText(1, QCoreApplication.translate("StObj", u"\u0447\u0435\u0440\u0435\u0437 \u0440\u043e\u0442", None))
        self.comboBoxPtBreathing_1.setItemText(2, QCoreApplication.translate("StObj", u"\u0447\u0435\u0440\u0435\u0437 \u0422\u0421\u0422", None))

        self.comboBoxPtGeneralState.setItemText(0, QCoreApplication.translate("StObj", u"\u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435", None))
        self.comboBoxPtGeneralState.setItemText(1, QCoreApplication.translate("StObj", u"\u0431\u043b\u0438\u0436\u0435 \u043a \u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u043c\u0443", None))
        self.comboBoxPtGeneralState.setItemText(2, QCoreApplication.translate("StObj", u"\u0441\u0440\u0435\u0434\u043d\u0435\u0439 \u0441\u0442\u0435\u043f\u0435\u043d\u0438 \u0442\u044f\u0436\u0435\u0441\u0442\u0438", None))
        self.comboBoxPtGeneralState.setItemText(3, QCoreApplication.translate("StObj", u"\u0442\u044f\u0436\u0435\u043b\u043e\u0435", None))
        self.comboBoxPtGeneralState.setItemText(4, QCoreApplication.translate("StObj", u"\u043a\u0440\u0430\u0439\u043d\u0435\u0439 \u0441\u0442\u0435\u043f\u0435\u043d\u0438 \u0442\u044f\u0436\u0435\u0441\u0442\u0438", None))
        self.comboBoxPtGeneralState.setItemText(5, QCoreApplication.translate("StObj", u"\u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435", None))

        self.comboBoxPtHearthTone_3.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtHearthTone_3.setItemText(1, QCoreApplication.translate("StObj", u"\u0430\u043a\u0446\u0435\u043d\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0442\u043e\u043d\u0430 \u043d\u0430\u0434 \u0430\u043e\u0440\u0442\u043e\u0439", None))
        self.comboBoxPtHearthTone_3.setItemText(2, QCoreApplication.translate("StObj", u"\u0430\u043a\u0446\u0435\u043d\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0442\u043e\u043d\u0430 \u043d\u0430\u0434 \u043b\u0435\u0433\u043e\u0447\u043d\u043e\u0439 \u0430\u0440\u0442\u0435\u0440\u0438\u0435\u0439", None))
        self.comboBoxPtHearthTone_3.setItemText(3, QCoreApplication.translate("StObj", u"\u0440\u0438\u0442\u043c \u0433\u0430\u043b\u043e\u043f\u0430", None))

        self.comboBoxPtDyspnea_2.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtDyspnea_2.setItemText(1, QCoreApplication.translate("StObj", u"\u043b\u0435\u0433\u043a\u0430\u044f", None))
        self.comboBoxPtDyspnea_2.setItemText(2, QCoreApplication.translate("StObj", u"\u0443\u043c\u0435\u0440\u0435\u043d\u043d\u0430\u044f", None))
        self.comboBoxPtDyspnea_2.setItemText(3, QCoreApplication.translate("StObj", u"\u0432\u044b\u0440\u0430\u0436\u0435\u043d\u043d\u0430\u044f", None))

        self.labelPtHearthTones.setText(QCoreApplication.translate("StObj", u"\u0422\u043e\u043d\u044b \u0441\u0435\u0440\u0434\u0446\u0430:", None))
        self.comboBoxPtDefecation_2.setItemText(0, QCoreApplication.translate("StObj", u"\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0439", None))
        self.comboBoxPtDefecation_2.setItemText(1, QCoreApplication.translate("StObj", u"\u0441\u043a\u043b\u043e\u043d\u043d\u043e\u0441\u0442\u044c \u043a \u0437\u0430\u043f\u043e\u0440\u0430\u043c", None))
        self.comboBoxPtDefecation_2.setItemText(2, QCoreApplication.translate("StObj", u"\u0437\u0430\u043f\u043e\u0440\u044b", None))
        self.comboBoxPtDefecation_2.setItemText(3, QCoreApplication.translate("StObj", u"\u0443\u0447\u0430\u0449\u0435\u043d\u043d\u044b\u0439", None))

        self.labelPtLymphnode.setText(QCoreApplication.translate("StObj", u"\u041b\u0438\u043c\u0444\u043e\u0443\u0437\u043b\u044b:", None))
        self.labelPtDefecation.setText(QCoreApplication.translate("StObj", u"\u0421\u0442\u0443\u043b:", None))
        self.comboBoxPtBreathing_2.setItemText(0, QCoreApplication.translate("StObj", u"\u0432\u0435\u0437\u0438\u043a\u0443\u043b\u044f\u0440\u043d\u043e\u0435", None))
        self.comboBoxPtBreathing_2.setItemText(1, QCoreApplication.translate("StObj", u"\u0436\u0435\u0441\u0442\u043a\u043e\u0435", None))
        self.comboBoxPtBreathing_2.setItemText(2, QCoreApplication.translate("StObj", u"\u0431\u0440\u043e\u043d\u0445\u0438\u0430\u043b\u044c\u043d\u043e\u0435", None))

        self.comboBoxPtDyspnea_1.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtDyspnea_1.setItemText(1, QCoreApplication.translate("StObj", u"\u0438\u043d\u0441\u043f\u0438\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f", None))
        self.comboBoxPtDyspnea_1.setItemText(2, QCoreApplication.translate("StObj", u"\u044d\u043a\u0441\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f", None))
        self.comboBoxPtDyspnea_1.setItemText(3, QCoreApplication.translate("StObj", u"\u0441\u043c\u0435\u0448\u0430\u043d\u043d\u0430\u044f", None))

        self.labelPtBreathing.setText(QCoreApplication.translate("StObj", u"\u0414\u044b\u0445\u0430\u043d\u0438\u0435:", None))
        self.label_12.setText(QCoreApplication.translate("StObj", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0441\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0441\u0442\u0430\u0442\u0443\u0441\u0430", None))
        self.comboBoxPtUrination_2.setItemText(0, QCoreApplication.translate("StObj", u"\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e\u0435", None))
        self.comboBoxPtUrination_2.setItemText(1, QCoreApplication.translate("StObj", u"\u0434\u0438\u0443\u0440\u0435\u0437 \u0441\u043d\u0438\u0436\u0435\u043d", None))
        self.comboBoxPtUrination_2.setItemText(2, QCoreApplication.translate("StObj", u"\u043f\u043e\u043b\u0438\u0443\u0440\u0438\u044f", None))

        self.comboBoxPtDyspneaChoice.setItemText(0, QCoreApplication.translate("StObj", u"\u043d\u0435\u0442", None))
        self.comboBoxPtDyspneaChoice.setItemText(1, QCoreApplication.translate("StObj", u"\u0415\u0421\u0422\u042c", None))

        self.comboBoxPtDefecation_1.setItemText(0, QCoreApplication.translate("StObj", u"\u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u043d\u044b\u0439", None))
        self.comboBoxPtDefecation_1.setItemText(1, QCoreApplication.translate("StObj", u"\u043a\u0430\u0448\u0438\u0446\u0435\u043e\u0431\u0440\u0430\u0437\u043d\u044b\u0439", None))
        self.comboBoxPtDefecation_1.setItemText(2, QCoreApplication.translate("StObj", u"\u0436\u0438\u0434\u043a\u0438\u0439", None))

        self.comboBoxPtDyspnea_3.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtDyspnea_3.setItemText(1, QCoreApplication.translate("StObj", u"\u0443\u0441\u0438\u043b\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043f\u0440\u0438 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u0438", None))

        self.comboBoxPtMucousMembr_1.setItemText(0, QCoreApplication.translate("StObj", u"\u0444\u0438\u0437\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043e\u043a\u0440\u0430\u0441\u043a\u0438", None))
        self.comboBoxPtMucousMembr_1.setItemText(1, QCoreApplication.translate("StObj", u"\u0433\u0438\u043f\u0435\u0440\u0435\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u044b", None))
        self.comboBoxPtMucousMembr_1.setItemText(2, QCoreApplication.translate("StObj", u"\u0431\u043b\u0435\u0434\u043d\u043e\u0432\u0430\u0442\u044b\u0435", None))
        self.comboBoxPtMucousMembr_1.setItemText(3, QCoreApplication.translate("StObj", u"\u0431\u043b\u0435\u0434\u043d\u044b\u0435", None))
        self.comboBoxPtMucousMembr_1.setItemText(4, QCoreApplication.translate("StObj", u"\u043c\u0440\u0430\u043c\u043e\u0440\u043d\u044b\u0435", None))
        self.comboBoxPtMucousMembr_1.setItemText(5, QCoreApplication.translate("StObj", u"\u0438\u043a\u0442\u0435\u0440\u0438\u0447\u043d\u044b\u0435", None))

        self.labelPtUrination.setText(QCoreApplication.translate("StObj", u"\u041c\u043e\u0447\u0435\u0438\u0441\u043f\u0443\u0441\u043a\u0430\u043d\u0438\u0435:", None))
        self.comboBoxPtUrination_1.setItemText(0, QCoreApplication.translate("StObj", u"\u043a\u043e\u043d\u0442\u0440\u043e\u043b\u0438\u0440\u0443\u0435\u0442", None))
        self.comboBoxPtUrination_1.setItemText(1, QCoreApplication.translate("StObj", u"\u0438\u043c\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u043f\u043e\u0437\u044b\u0432\u044b", None))
        self.comboBoxPtUrination_1.setItemText(2, QCoreApplication.translate("StObj", u"\u043f\u0435\u0440\u0438\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043d\u0435\u0443\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.comboBoxPtUrination_1.setItemText(3, QCoreApplication.translate("StObj", u"\u043d\u0435\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.comboBoxPtUrination_1.setItemText(4, QCoreApplication.translate("StObj", u"\u043f\u0435\u0440\u0438\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043a\u0430\u0442\u0435\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.comboBoxPtUrination_1.setItemText(5, QCoreApplication.translate("StObj", u"\u0447\u0435\u0440\u0435\u0437 \u0446\u0438\u0441\u0442\u043e\u0441\u0442\u043e\u043c\u0443", None))
        self.comboBoxPtUrination_1.setItemText(6, QCoreApplication.translate("StObj", u"\u043f\u043e \u043a\u0430\u0442\u0435\u0442\u0435\u0440\u0443", None))

        self.comboBoxPtDefecation_3.setItemText(0, QCoreApplication.translate("StObj", u"\u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u044b\u0439", None))
        self.comboBoxPtDefecation_3.setItemText(1, QCoreApplication.translate("StObj", u"1 \u0440\u0430\u0437 \u0432 2 \u0434\u043d\u044f", None))
        self.comboBoxPtDefecation_3.setItemText(2, QCoreApplication.translate("StObj", u"1 \u0440\u0430\u0437 \u0432 3-4 \u0434\u043d\u044f", None))
        self.comboBoxPtDefecation_3.setItemText(3, QCoreApplication.translate("StObj", u"\u0434\u043e 1 \u0440\u0430\u0437\u0430 \u0432 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.comboBoxPtDefecation_3.setItemText(4, QCoreApplication.translate("StObj", u"2-3 \u0440\u0430\u0437\u0430 \u0432 \u0434\u0435\u043d\u044c", None))
        self.comboBoxPtDefecation_3.setItemText(5, QCoreApplication.translate("StObj", u"\u0434\u043e 6 \u0440\u0430\u0437 \u0432 \u0434\u0435\u043d\u044c", None))

        self.labelPtSkinState.setText(QCoreApplication.translate("StObj", u"\u041a\u043e\u0436\u043d\u044b\u0435 \u043f\u043e\u043a\u0440\u043e\u0432\u044b:", None))
        self.comboBoxPtHearthTone_2.setItemText(0, QCoreApplication.translate("StObj", u"\u0440\u0438\u0442\u043c\u0438\u0447\u043d\u044b\u0435", None))
        self.comboBoxPtHearthTone_2.setItemText(1, QCoreApplication.translate("StObj", u"\u0430\u0440\u0438\u0442\u043c\u0438\u0447\u043d\u044b\u0435", None))

        self.comboBoxPtHearthNoiseChoice.setItemText(0, QCoreApplication.translate("StObj", u"\u043d\u0435\u0442", None))
        self.comboBoxPtHearthNoiseChoice.setItemText(1, QCoreApplication.translate("StObj", u"\u0415\u0421\u0422\u042c", None))

        self.comboBoxPtWheezing_1.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtWheezing_1.setItemText(1, QCoreApplication.translate("StObj", u"\u0435\u0434\u0438\u043d\u0438\u0447\u043d\u044b\u0435", None))
        self.comboBoxPtWheezing_1.setItemText(2, QCoreApplication.translate("StObj", u"\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435", None))

        self.labelPtStObjOther.setText(QCoreApplication.translate("StObj", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435:", None))
        self.comboBoxPtWheezing_3.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtWheezing_3.setItemText(1, QCoreApplication.translate("StObj", u"\u0432 \u043d\u0438\u0436\u043d\u0438\u0445 \u043e\u0442\u0434\u0435\u043b\u0430\u0445", None))
        self.comboBoxPtWheezing_3.setItemText(2, QCoreApplication.translate("StObj", u"\u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0432\u0435\u0440\u0445\u0443\u0448\u0435\u043a", None))
        self.comboBoxPtWheezing_3.setItemText(3, QCoreApplication.translate("StObj", u"\u043d\u0430\u0434 \u0432\u0441\u0435\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u044c\u044e \u043b\u0435\u0433\u043a\u0438\u0445", None))

        self.comboBoxPtHearthTone_1.setItemText(0, QCoreApplication.translate("StObj", u"\u044f\u0441\u043d\u044b\u0435", None))
        self.comboBoxPtHearthTone_1.setItemText(1, QCoreApplication.translate("StObj", u"\u043f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u044b", None))
        self.comboBoxPtHearthTone_1.setItemText(2, QCoreApplication.translate("StObj", u"\u0433\u043b\u0443\u0445\u0438\u0435", None))

        self.comboBoxPtWheezingChoice.setItemText(0, QCoreApplication.translate("StObj", u"\u043d\u0435\u0442", None))
        self.comboBoxPtWheezingChoice.setItemText(1, QCoreApplication.translate("StObj", u"\u0415\u0421\u0422\u042c", None))

        self.comboBoxPtStomach_3.setItemText(0, QCoreApplication.translate("StObj", u"\u0443\u0447\u0430\u0441\u0442\u0432\u0443\u0435\u0442 \u0432 \u0430\u043a\u0442\u0435 \u0434\u044b\u0445\u0430\u043d\u0438\u044f", None))
        self.comboBoxPtStomach_3.setItemText(1, QCoreApplication.translate("StObj", u"\u0432\u0437\u0434\u0443\u0442", None))

        self.comboBoxPtSkinState_2.setItemText(0, QCoreApplication.translate("StObj", u"\u0432\u044b\u0441\u044b\u043f\u0430\u043d\u0438\u0439 \u043d\u0435\u0442", None))
        self.comboBoxPtSkinState_2.setItemText(1, QCoreApplication.translate("StObj", u"\u043f\u0441\u043e\u0440\u0438\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0432\u044b\u0441\u044b\u043f\u0430\u043d\u0438\u044f \u043d\u0430 \u043b\u043e\u043a\u0442\u044f\u0445 ", None))

        self.labelPtMucousMembr.setText(QCoreApplication.translate("StObj", u"\u0421\u043b\u0438\u0437\u0438\u0441\u0442\u044b\u0435:", None))
        self.comboBoxPtWheezing_2.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtWheezing_2.setItemText(1, QCoreApplication.translate("StObj", u"\u0441\u0443\u0445\u0438\u0435", None))
        self.comboBoxPtWheezing_2.setItemText(2, QCoreApplication.translate("StObj", u"\u0432\u043b\u0430\u0436\u043d\u044b\u0435", None))
        self.comboBoxPtWheezing_2.setItemText(3, "")

        self.labelPtStomach.setText(QCoreApplication.translate("StObj", u"\u0416\u0438\u0432\u043e\u0442:", None))
        self.comboBoxPtStomach_2.setItemText(0, QCoreApplication.translate("StObj", u"\u0431\u0435\u0437\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u044b\u0439", None))
        self.comboBoxPtStomach_2.setItemText(1, QCoreApplication.translate("StObj", u"\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u044b\u0439 \u0432 \u044d\u043f\u0438\u0433\u0430\u0441\u0442\u0440\u0438\u0438", None))
        self.comboBoxPtStomach_2.setItemText(2, QCoreApplication.translate("StObj", u"\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u044b\u0439 \u043f\u0440\u0438 \u0433\u043b\u0443\u0431\u043e\u043a\u043e\u0439 \u043f\u0430\u043b\u044c\u043f\u0430\u0446\u0438\u0438", None))

        self.comboBoxPtHearthNoise.setItemText(0, QCoreApplication.translate("StObj", u"-----", None))
        self.comboBoxPtHearthNoise.setItemText(1, QCoreApplication.translate("StObj", u"\u0421\u0438\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0448\u0443\u043c \u043d\u0430\u0434 \u0430\u043e\u0440\u0442\u043e\u0439", None))
        self.comboBoxPtHearthNoise.setItemText(2, QCoreApplication.translate("StObj", u"\u0414\u0438\u0430\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0448\u0443\u043c \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u043c\u0438\u0442\u0440\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043a\u043b\u0430\u043f\u0430\u043d\u0430", None))

        self.comboBoxPtLymphnode.setItemText(0, QCoreApplication.translate("StObj", u"\u043d\u0435 \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u044b", None))
        self.comboBoxPtLymphnode.setItemText(1, QCoreApplication.translate("StObj", u"\u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d \u043f\u043e\u0434\u043c\u044b\u0448\u0435\u0447\u043d\u044b\u0439 \u043b\u0438\u043c\u0444\u043e\u0443\u0437\u0435\u043b \u0441\u043f\u0440\u0430\u0432\u0430", None))

        self.comboBoxGeneralStTemplate.setItemText(0, QCoreApplication.translate("StObj", u"\u041d\u043e\u0440\u043c\u0430", None))

        self.pushButtonAddNewTemplateGeneralSt.setText(QCoreApplication.translate("StObj", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.label.setText(QCoreApplication.translate("StObj", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u0441\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0441\u0442\u0430\u0442\u0443\u0441\u0430", None))
        self.pushButton_push_temp.setText(QCoreApplication.translate("StObj", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit_new_template_name.setText("")
        self.lineEdit_new_template_name.setPlaceholderText(QCoreApplication.translate("StObj", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("StObj", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("StObj", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.obj_status), QCoreApplication.translate("StObj", u"\u0421\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.groupBox_wom.setTitle(QCoreApplication.translate("StObj", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("StObj", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("StObj", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("StObj", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
    # retranslateUi

