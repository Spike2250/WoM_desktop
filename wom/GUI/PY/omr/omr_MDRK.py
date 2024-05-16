# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'omr_MDRK.ui'
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
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc

class Ui_MDRK(object):
    def setupUi(self, MDRK):
        if not MDRK.objectName():
            MDRK.setObjectName(u"MDRK")
        MDRK.resize(1136, 648)
        MDRK.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_4 = QVBoxLayout(MDRK)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(MDRK)
        self.main.setObjectName(u"main")
        self.gridLayout_4 = QGridLayout(self.main)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget:pane {\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
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
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(28, 28))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.limits = QWidget()
        self.limits.setObjectName(u"limits")
        self.gridLayout = QGridLayout(self.limits)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_rehab_potentional = QLabel(self.limits)
        self.label_rehab_potentional.setObjectName(u"label_rehab_potentional")
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
        self.label_rehab_potentional.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_rehab_potentional.setFont(font)
        self.label_rehab_potentional.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")

        self.horizontalLayout.addWidget(self.label_rehab_potentional)

        self.comboBox_rehab_potentional = QComboBox(self.limits)
        self.comboBox_rehab_potentional.addItem("")
        self.comboBox_rehab_potentional.addItem("")
        self.comboBox_rehab_potentional.addItem("")
        self.comboBox_rehab_potentional.addItem("")
        self.comboBox_rehab_potentional.addItem("")
        self.comboBox_rehab_potentional.setObjectName(u"comboBox_rehab_potentional")
        palette1 = QPalette()
        brush9 = QBrush(QColor(19, 36, 43, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        brush10 = QBrush(QColor(238, 238, 238, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush11 = QBrush(QColor(19, 36, 43, 128))
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
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
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
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.comboBox_rehab_potentional.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.comboBox_rehab_potentional.setFont(font1)
        self.comboBox_rehab_potentional.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_rehab_potentional.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBox_rehab_potentional)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.frame_limit = QFrame(self.limits)
        self.frame_limit.setObjectName(u"frame_limit")
        self.frame_limit.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout = QVBoxLayout(self.frame_limit)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_factors_limiting_rehab = QLabel(self.frame_limit)
        self.label_factors_limiting_rehab.setObjectName(u"label_factors_limiting_rehab")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_factors_limiting_rehab.setPalette(palette2)
        self.label_factors_limiting_rehab.setFont(font)
        self.label_factors_limiting_rehab.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_factors_limiting_rehab.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_factors_limiting_rehab)

        self.tableWidget_limits = QTableWidget(self.frame_limit)
        self.tableWidget_limits.setObjectName(u"tableWidget_limits")
        self.tableWidget_limits.setStyleSheet(u"QTableWidget {\n"
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

        self.verticalLayout.addWidget(self.tableWidget_limits)


        self.gridLayout.addWidget(self.frame_limit, 1, 0, 1, 1)

        icon = QIcon()
        icon.addFile(u":/icon/icons/personal_injury_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.limits, icon, "")
        self.goals = QWidget()
        self.goals.setObjectName(u"goals")
        self.gridLayout_2 = QGridLayout(self.goals)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.goals_frame = QFrame(self.goals)
        self.goals_frame.setObjectName(u"goals_frame")
        self.goals_frame.setMaximumSize(QSize(16777215, 115))
        self.goals_frame.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_3 = QVBoxLayout(self.goals_frame)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.goals_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.plainTextEdit_goals = QPlainTextEdit(self.goals_frame)
        self.plainTextEdit_goals.setObjectName(u"plainTextEdit_goals")
        self.plainTextEdit_goals.setMinimumSize(QSize(400, 0))
        self.plainTextEdit_goals.setMaximumSize(QSize(16777215, 200))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.plainTextEdit_goals.setPalette(palette3)
        self.plainTextEdit_goals.setFont(font1)
        self.plainTextEdit_goals.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.verticalLayout_3.addWidget(self.plainTextEdit_goals)


        self.gridLayout_2.addWidget(self.goals_frame, 0, 0, 1, 1)

        self.frame_templates = QFrame(self.goals)
        self.frame_templates.setObjectName(u"frame_templates")
        self.frame_templates.setMaximumSize(QSize(16777215, 115))
        self.frame_templates.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_13 = QGridLayout(self.frame_templates)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(5)
        self.gridLayout_13.setVerticalSpacing(1)
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.comboBox_templates = QComboBox(self.frame_templates)
        self.comboBox_templates.addItem("")
        self.comboBox_templates.setObjectName(u"comboBox_templates")
        self.comboBox_templates.setMaximumSize(QSize(16777215, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.comboBox_templates.setPalette(palette4)
        self.comboBox_templates.setFont(font1)
        self.comboBox_templates.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_13.addWidget(self.comboBox_templates, 2, 0, 1, 1)

        self.pushButtonAddNewTemplate = QPushButton(self.frame_templates)
        self.pushButtonAddNewTemplate.setObjectName(u"pushButtonAddNewTemplate")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush12 = QBrush(QColor(50, 98, 115, 190))
        brush12.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonAddNewTemplate.setPalette(palette5)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.pushButtonAddNewTemplate.setFont(font2)
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

        self.gridLayout_13.addWidget(self.pushButtonAddNewTemplate, 4, 1, 1, 1)

        self.label_14 = QLabel(self.frame_templates)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_14, 0, 0, 1, 2)

        self.pushButton_push_temp = QPushButton(self.frame_templates)
        self.pushButton_push_temp.setObjectName(u"pushButton_push_temp")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton_push_temp.setPalette(palette6)
        self.pushButton_push_temp.setFont(font2)
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

        self.gridLayout_13.addWidget(self.pushButton_push_temp, 2, 1, 1, 1)

        self.lineEdit_new_template_name = QLineEdit(self.frame_templates)
        self.lineEdit_new_template_name.setObjectName(u"lineEdit_new_template_name")
        self.lineEdit_new_template_name.setMinimumSize(QSize(350, 0))
        self.lineEdit_new_template_name.setFont(font1)
        self.lineEdit_new_template_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_13.addWidget(self.lineEdit_new_template_name, 4, 0, 1, 1)

        self.label_15 = QLabel(self.frame_templates)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.frame_templates)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_16, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_templates, 0, 1, 1, 1)

        self.frame_goals = QFrame(self.goals)
        self.frame_goals.setObjectName(u"frame_goals")
        self.frame_goals.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_2 = QVBoxLayout(self.frame_goals)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_goals = QLabel(self.frame_goals)
        self.label_goals.setObjectName(u"label_goals")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_goals.setPalette(palette7)
        self.label_goals.setFont(font)
        self.label_goals.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_goals.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_goals)

        self.tableWidget_goals = QTableWidget(self.frame_goals)
        self.tableWidget_goals.setObjectName(u"tableWidget_goals")
        self.tableWidget_goals.setStyleSheet(u"QTableWidget {\n"
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

        self.verticalLayout_2.addWidget(self.tableWidget_goals)


        self.gridLayout_2.addWidget(self.frame_goals, 1, 0, 1, 2)

        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/accessible_forward_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.goals, icon1, "")
        self.mdrk = QWidget()
        self.mdrk.setObjectName(u"mdrk")
        self.gridLayout_3 = QGridLayout(self.mdrk)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_4 = QFrame(self.mdrk)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_16 = QGridLayout(self.frame_4)
        self.gridLayout_16.setSpacing(5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_6 = QSpacerItem(5, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_16.addItem(self.verticalSpacer_6, 2, 0, 1, 3)

        self.label_physio = QLabel(self.frame_4)
        self.label_physio.setObjectName(u"label_physio")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_physio.setPalette(palette8)
        self.label_physio.setFont(font)
        self.label_physio.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_physio.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_physio, 0, 0, 1, 3)

        self.plainTextEdit_physio = QPlainTextEdit(self.frame_4)
        self.plainTextEdit_physio.setObjectName(u"plainTextEdit_physio")
        self.plainTextEdit_physio.setEnabled(False)
        self.plainTextEdit_physio.setMinimumSize(QSize(350, 0))
        self.plainTextEdit_physio.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_physio.setFont(font1)
        self.plainTextEdit_physio.setStyleSheet(u"QPlainTextEdit { background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"QPlainTextEdit::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout_16.addWidget(self.plainTextEdit_physio, 1, 0, 1, 3)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(155, 0))
        palette9 = QPalette()
        brush13 = QBrush(QColor(50, 98, 115, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        brush14 = QBrush(QColor(0, 0, 0, 0))
        brush14.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
        brush15 = QBrush(QColor(50, 98, 115, 128))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_13.setPalette(palette9)
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_16.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_physio_name = QLabel(self.frame_4)
        self.label_physio_name.setObjectName(u"label_physio_name")
        self.label_physio_name.setMinimumSize(QSize(0, 0))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_physio_name.setPalette(palette10)
        self.label_physio_name.setFont(font1)
        self.label_physio_name.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_physio_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_physio_name, 3, 1, 1, 2)


        self.gridLayout_3.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame = QFrame(self.mdrk)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_14 = QGridLayout(self.frame)
        self.gridLayout_14.setSpacing(5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(5, 5, 5, 5)
        self.label_psy_hads_2 = QLabel(self.frame)
        self.label_psy_hads_2.setObjectName(u"label_psy_hads_2")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_psy_hads_2.setPalette(palette11)
        self.label_psy_hads_2.setFont(font1)
        self.label_psy_hads_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_14.addWidget(self.label_psy_hads_2, 2, 3, 1, 1)

        self.comboBox_hads_t = QComboBox(self.frame)
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.addItem("")
        self.comboBox_hads_t.setObjectName(u"comboBox_hads_t")
        self.comboBox_hads_t.setMinimumSize(QSize(80, 0))
        self.comboBox_hads_t.setMaximumSize(QSize(80, 16777215))
        self.comboBox_hads_t.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_14.addWidget(self.comboBox_hads_t, 2, 4, 1, 2)

        self.comboBox_hads_d = QComboBox(self.frame)
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.addItem("")
        self.comboBox_hads_d.setObjectName(u"comboBox_hads_d")
        self.comboBox_hads_d.setMinimumSize(QSize(80, 0))
        self.comboBox_hads_d.setMaximumSize(QSize(80, 16777215))
        self.comboBox_hads_d.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_14.addWidget(self.comboBox_hads_d, 2, 6, 1, 2)

        self.comboBox_moca = QComboBox(self.frame)
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.addItem("")
        self.comboBox_moca.setObjectName(u"comboBox_moca")
        self.comboBox_moca.setMinimumSize(QSize(80, 0))
        self.comboBox_moca.setMaximumSize(QSize(80, 16777215))
        self.comboBox_moca.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_14.addWidget(self.comboBox_moca, 2, 1, 1, 2)

        self.label_psy_moca_2 = QLabel(self.frame)
        self.label_psy_moca_2.setObjectName(u"label_psy_moca_2")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_psy_moca_2.setPalette(palette12)
        self.label_psy_moca_2.setFont(font1)
        self.label_psy_moca_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_14.addWidget(self.label_psy_moca_2, 2, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_25, 2, 8, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(5, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 3, 0, 1, 9)

        self.plainTextEdit_psy_conclusion = QPlainTextEdit(self.frame)
        self.plainTextEdit_psy_conclusion.setObjectName(u"plainTextEdit_psy_conclusion")
        self.plainTextEdit_psy_conclusion.setEnabled(True)
        self.plainTextEdit_psy_conclusion.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_psy_conclusion.setFont(font1)
        self.plainTextEdit_psy_conclusion.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_14.addWidget(self.plainTextEdit_psy_conclusion, 1, 0, 1, 9)

        self.label_psy_conclusion_2 = QLabel(self.frame)
        self.label_psy_conclusion_2.setObjectName(u"label_psy_conclusion_2")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_psy_conclusion_2.setPalette(palette13)
        self.label_psy_conclusion_2.setFont(font)
        self.label_psy_conclusion_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_psy_conclusion_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_psy_conclusion_2, 0, 0, 1, 9)

        self.label_psy_name_2 = QLabel(self.frame)
        self.label_psy_name_2.setObjectName(u"label_psy_name_2")
        self.label_psy_name_2.setMinimumSize(QSize(150, 0))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_psy_name_2.setPalette(palette14)
        self.label_psy_name_2.setFont(font1)
        self.label_psy_name_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_14.addWidget(self.label_psy_name_2, 4, 0, 1, 2)

        self.comboBox_psy_name = QComboBox(self.frame)
        self.comboBox_psy_name.setObjectName(u"comboBox_psy_name")
        self.comboBox_psy_name.setMinimumSize(QSize(0, 0))
        self.comboBox_psy_name.setFont(font1)
        self.comboBox_psy_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_psy_name.setEditable(True)

        self.gridLayout_14.addWidget(self.comboBox_psy_name, 4, 2, 1, 7)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.frame_3 = QFrame(self.mdrk)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_15 = QGridLayout(self.frame_3)
        self.gridLayout_15.setSpacing(5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_5 = QSpacerItem(5, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_15.addItem(self.verticalSpacer_5, 2, 0, 1, 3)

        self.label_lfk = QLabel(self.frame_3)
        self.label_lfk.setObjectName(u"label_lfk")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_lfk.setPalette(palette15)
        self.label_lfk.setFont(font)
        self.label_lfk.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_lfk.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_lfk, 0, 0, 1, 3)

        self.plainTextEdit_lfk = QPlainTextEdit(self.frame_3)
        self.plainTextEdit_lfk.setObjectName(u"plainTextEdit_lfk")
        self.plainTextEdit_lfk.setEnabled(False)
        self.plainTextEdit_lfk.setMinimumSize(QSize(350, 0))
        self.plainTextEdit_lfk.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_lfk.setFont(font1)
        self.plainTextEdit_lfk.setStyleSheet(u"QPlainTextEdit { background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"}\n"
"QPlainTextEdit::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout_15.addWidget(self.plainTextEdit_lfk, 1, 0, 1, 3)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(155, 0))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_12.setPalette(palette16)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_15.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_lfk_name = QLabel(self.frame_3)
        self.label_lfk_name.setObjectName(u"label_lfk_name")
        self.label_lfk_name.setMinimumSize(QSize(0, 0))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_lfk_name.setPalette(palette17)
        self.label_lfk_name.setFont(font1)
        self.label_lfk_name.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_lfk_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_lfk_name, 3, 1, 1, 2)


        self.gridLayout_3.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.mdrk)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_12 = QGridLayout(self.frame_2)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(5, 5, 5, 5)
        self.label_logo_dysphagia_2 = QLabel(self.frame_2)
        self.label_logo_dysphagia_2.setObjectName(u"label_logo_dysphagia_2")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_logo_dysphagia_2.setPalette(palette18)
        self.label_logo_dysphagia_2.setFont(font1)
        self.label_logo_dysphagia_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_12.addWidget(self.label_logo_dysphagia_2, 5, 0, 1, 1)

        self.comboBox_logo_disart = QComboBox(self.frame_2)
        self.comboBox_logo_disart.addItem("")
        self.comboBox_logo_disart.addItem("")
        self.comboBox_logo_disart.setObjectName(u"comboBox_logo_disart")
        self.comboBox_logo_disart.setMinimumSize(QSize(80, 0))
        self.comboBox_logo_disart.setMaximumSize(QSize(80, 16777215))
        self.comboBox_logo_disart.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_disart.setEditable(True)

        self.gridLayout_12.addWidget(self.comboBox_logo_disart, 3, 1, 1, 1)

        self.label_logo_proso_2 = QLabel(self.frame_2)
        self.label_logo_proso_2.setObjectName(u"label_logo_proso_2")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette19.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette19.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette19.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette19.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette19.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette19.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette19.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette19.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_logo_proso_2.setPalette(palette19)
        self.label_logo_proso_2.setFont(font1)
        self.label_logo_proso_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_12.addWidget(self.label_logo_proso_2, 4, 0, 1, 1)

        self.label_logo_wasserman_2 = QLabel(self.frame_2)
        self.label_logo_wasserman_2.setObjectName(u"label_logo_wasserman_2")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette20.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette20.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette20.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette20.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette20.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette20.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_logo_wasserman_2.setPalette(palette20)
        self.label_logo_wasserman_2.setFont(font1)
        self.label_logo_wasserman_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_12.addWidget(self.label_logo_wasserman_2, 2, 0, 1, 1)

        self.comboBox_logo_wasserman = QComboBox(self.frame_2)
        self.comboBox_logo_wasserman.addItem("")
        self.comboBox_logo_wasserman.addItem("")
        self.comboBox_logo_wasserman.setObjectName(u"comboBox_logo_wasserman")
        self.comboBox_logo_wasserman.setMinimumSize(QSize(80, 0))
        self.comboBox_logo_wasserman.setMaximumSize(QSize(80, 16777215))
        self.comboBox_logo_wasserman.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_wasserman.setEditable(True)

        self.gridLayout_12.addWidget(self.comboBox_logo_wasserman, 2, 1, 1, 1)

        self.label_logo_disart_2 = QLabel(self.frame_2)
        self.label_logo_disart_2.setObjectName(u"label_logo_disart_2")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette21.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette21.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette21.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette21.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette21.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette21.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette21.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_logo_disart_2.setPalette(palette21)
        self.label_logo_disart_2.setFont(font1)
        self.label_logo_disart_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_12.addWidget(self.label_logo_disart_2, 3, 0, 1, 1)

        self.comboBox_logo_dysphagia = QComboBox(self.frame_2)
        self.comboBox_logo_dysphagia.addItem("")
        self.comboBox_logo_dysphagia.addItem("")
        self.comboBox_logo_dysphagia.setObjectName(u"comboBox_logo_dysphagia")
        self.comboBox_logo_dysphagia.setMinimumSize(QSize(80, 0))
        self.comboBox_logo_dysphagia.setMaximumSize(QSize(80, 16777215))
        self.comboBox_logo_dysphagia.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_dysphagia.setEditable(True)

        self.gridLayout_12.addWidget(self.comboBox_logo_dysphagia, 5, 1, 1, 1)

        self.label_logo_name_2 = QLabel(self.frame_2)
        self.label_logo_name_2.setObjectName(u"label_logo_name_2")
        self.label_logo_name_2.setMinimumSize(QSize(150, 0))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush13)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush13)
        palette22.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush13)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette22.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette22.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette22.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush13)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush13)
        palette22.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush13)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        palette22.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette22.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush13)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush13)
        palette22.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette22.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette22.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.label_logo_name_2.setPalette(palette22)
        self.label_logo_name_2.setFont(font1)
        self.label_logo_name_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_12.addWidget(self.label_logo_name_2, 7, 0, 1, 1)

        self.comboBox_logo_proso = QComboBox(self.frame_2)
        self.comboBox_logo_proso.addItem("")
        self.comboBox_logo_proso.addItem("")
        self.comboBox_logo_proso.setObjectName(u"comboBox_logo_proso")
        self.comboBox_logo_proso.setMinimumSize(QSize(80, 0))
        self.comboBox_logo_proso.setMaximumSize(QSize(80, 16777215))
        self.comboBox_logo_proso.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_proso.setEditable(True)

        self.gridLayout_12.addWidget(self.comboBox_logo_proso, 4, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(170, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_8, 3, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_3, 6, 0, 1, 3)

        self.plainTextEdit_logo_conclusion = QPlainTextEdit(self.frame_2)
        self.plainTextEdit_logo_conclusion.setObjectName(u"plainTextEdit_logo_conclusion")
        self.plainTextEdit_logo_conclusion.setEnabled(True)
        self.plainTextEdit_logo_conclusion.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_logo_conclusion.setFont(font1)
        self.plainTextEdit_logo_conclusion.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_12.addWidget(self.plainTextEdit_logo_conclusion, 1, 0, 1, 3)

        self.label_logo_conclusion_2 = QLabel(self.frame_2)
        self.label_logo_conclusion_2.setObjectName(u"label_logo_conclusion_2")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.label_logo_conclusion_2.setPalette(palette23)
        self.label_logo_conclusion_2.setFont(font)
        self.label_logo_conclusion_2.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label_logo_conclusion_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_logo_conclusion_2, 0, 0, 1, 3)

        self.comboBox_logo_name = QComboBox(self.frame_2)
        self.comboBox_logo_name.setObjectName(u"comboBox_logo_name")
        self.comboBox_logo_name.setMinimumSize(QSize(150, 0))
        self.comboBox_logo_name.setFont(font1)
        self.comboBox_logo_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_logo_name.setEditable(True)

        self.gridLayout_12.addWidget(self.comboBox_logo_name, 7, 1, 1, 2)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 2, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/manage_accounts_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.mdrk, icon2, "")

        self.gridLayout_4.addWidget(self.tabWidget, 1, 1, 2, 1)

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
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush)
        brush16 = QBrush(QColor(236, 236, 236, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush16)
        brush17 = QBrush(QColor(108, 108, 108, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush17)
        brush18 = QBrush(QColor(145, 145, 145, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush18)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush)
        palette24.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette24.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush16)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush16)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush17)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush18)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette24.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush16)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        brush19 = QBrush(QColor(50, 98, 115, 150))
        brush19.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush19)
        brush20 = QBrush(QColor(50, 98, 115, 40))
        brush20.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush16)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush17)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush18)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush19)
        palette24.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush19)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette24.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        brush21 = QBrush(QColor(217, 217, 217, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush21)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
        brush22 = QBrush(QColor(50, 98, 115, 75))
        brush22.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHelp.setIcon(icon3)

        self.verticalLayout_6.addWidget(self.pushButtonHelp)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.pushButtonNotSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonNotSaveExit.setPalette(palette25)
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
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon4)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush23 = QBrush(QColor(92, 158, 173, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush23)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush)
        palette26.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush23)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush23)
        palette26.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette26.setBrush(QPalette.Active, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush23)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush23)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush23)
        palette26.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette26.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette26.setBrush(QPalette.Disabled, QPalette.Shadow, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette26.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonSaveExit.setPalette(palette26)
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
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveExit.setIcon(icon5)
        self.pushButtonSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonSaveExit)


        self.gridLayout_4.addWidget(self.groupBox_wom, 0, 3, 3, 1)

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
        self.label_Pt_info.setFont(font1)
        self.label_Pt_info.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: 13242B;\n"
"font-size: 11pt;\n"
"font-weight: bold;\n"
"border: 1px solid rgba(50, 98, 115, 255);")

        self.horizontalLayout_3.addWidget(self.label_Pt_info)

        self.labelTimeline = QLabel(self.pt_info_block)
        self.labelTimeline.setObjectName(u"labelTimeline")
        self.labelTimeline.setMaximumSize(QSize(80, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setItalic(False)
        self.labelTimeline.setFont(font3)
        self.labelTimeline.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(92, 158, 173, 200)\n"
"")
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/conditions_FILL1_wght400_GRAD0_opsz48.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTimeline)


        self.gridLayout_4.addWidget(self.pt_info_block, 0, 0, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 2, 2, 1)

        self.horizontalSpacer_3 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 0, 2, 1)


        self.verticalLayout_4.addWidget(self.main)


        self.retranslateUi(MDRK)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MDRK)
    # setupUi

    def retranslateUi(self, MDRK):
        MDRK.setWindowTitle(QCoreApplication.translate("MDRK", u"Form", None))
        self.label_rehab_potentional.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0420\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b:</p></body></html>", None))
        self.comboBox_rehab_potentional.setItemText(0, QCoreApplication.translate("MDRK", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.comboBox_rehab_potentional.setItemText(1, QCoreApplication.translate("MDRK", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.comboBox_rehab_potentional.setItemText(2, QCoreApplication.translate("MDRK", u"\u041a\u0440\u0430\u0439\u043d\u0435 \u043d\u0438\u0437\u043a\u0438\u0439", None))
        self.comboBox_rehab_potentional.setItemText(3, QCoreApplication.translate("MDRK", u"\u041d\u0438\u0437\u043a\u0438\u0439", None))
        self.comboBox_rehab_potentional.setItemText(4, QCoreApplication.translate("MDRK", u"\u0412\u044b\u0441\u043e\u043a\u0438\u0439", None))

        self.label_factors_limiting_rehab.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0424\u0430\u043a\u0442\u043e\u0440\u044b \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0438\u0432\u0430\u044e\u0449\u0438\u0435 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u044e:</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.limits), QCoreApplication.translate("MDRK", u"\u041f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b, \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MDRK", u"\u0426\u0435\u043b\u0438 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438:", None))
        self.plainTextEdit_goals.setPlaceholderText(QCoreApplication.translate("MDRK", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0446\u0435\u043b\u044c/\u0446\u0435\u043b\u0438", None))
        self.comboBox_templates.setItemText(0, "")

        self.pushButtonAddNewTemplate.setText(QCoreApplication.translate("MDRK", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.label_14.setText(QCoreApplication.translate("MDRK", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u0446\u0435\u043b\u0435\u0439", None))
        self.pushButton_push_temp.setText(QCoreApplication.translate("MDRK", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit_new_template_name.setText("")
        self.lineEdit_new_template_name.setPlaceholderText(QCoreApplication.translate("MDRK", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_15.setText(QCoreApplication.translate("MDRK", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.label_16.setText(QCoreApplication.translate("MDRK", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_goals.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0417\u0430\u0434\u0430\u0447\u0438 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438:</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.goals), QCoreApplication.translate("MDRK", u"\u0426\u0435\u043b\u0438 \u0438 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_physio.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0444\u0438\u0437\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u0438:</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MDRK", u"\u0412\u0440\u0430\u0447-\u0444\u0438\u0437\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442:", None))
        self.label_psy_hads_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>HADS:</p></body></html>", None))
        self.comboBox_hads_t.setItemText(0, "")
        self.comboBox_hads_t.setItemText(1, QCoreApplication.translate("MDRK", u"UN", None))
        self.comboBox_hads_t.setItemText(2, QCoreApplication.translate("MDRK", u"0", None))
        self.comboBox_hads_t.setItemText(3, QCoreApplication.translate("MDRK", u"1", None))
        self.comboBox_hads_t.setItemText(4, QCoreApplication.translate("MDRK", u"2", None))
        self.comboBox_hads_t.setItemText(5, QCoreApplication.translate("MDRK", u"3", None))
        self.comboBox_hads_t.setItemText(6, QCoreApplication.translate("MDRK", u"4", None))
        self.comboBox_hads_t.setItemText(7, QCoreApplication.translate("MDRK", u"5", None))
        self.comboBox_hads_t.setItemText(8, QCoreApplication.translate("MDRK", u"6", None))
        self.comboBox_hads_t.setItemText(9, QCoreApplication.translate("MDRK", u"7", None))
        self.comboBox_hads_t.setItemText(10, QCoreApplication.translate("MDRK", u"8", None))
        self.comboBox_hads_t.setItemText(11, QCoreApplication.translate("MDRK", u"9", None))
        self.comboBox_hads_t.setItemText(12, QCoreApplication.translate("MDRK", u"10", None))
        self.comboBox_hads_t.setItemText(13, QCoreApplication.translate("MDRK", u"11", None))
        self.comboBox_hads_t.setItemText(14, QCoreApplication.translate("MDRK", u"12", None))
        self.comboBox_hads_t.setItemText(15, QCoreApplication.translate("MDRK", u"13", None))
        self.comboBox_hads_t.setItemText(16, QCoreApplication.translate("MDRK", u"14", None))
        self.comboBox_hads_t.setItemText(17, QCoreApplication.translate("MDRK", u"15", None))
        self.comboBox_hads_t.setItemText(18, QCoreApplication.translate("MDRK", u"16", None))
        self.comboBox_hads_t.setItemText(19, QCoreApplication.translate("MDRK", u"17", None))
        self.comboBox_hads_t.setItemText(20, QCoreApplication.translate("MDRK", u"18", None))
        self.comboBox_hads_t.setItemText(21, QCoreApplication.translate("MDRK", u"19", None))
        self.comboBox_hads_t.setItemText(22, QCoreApplication.translate("MDRK", u"20", None))
        self.comboBox_hads_t.setItemText(23, QCoreApplication.translate("MDRK", u"21", None))

        self.comboBox_hads_d.setItemText(0, "")
        self.comboBox_hads_d.setItemText(1, QCoreApplication.translate("MDRK", u"UN", None))
        self.comboBox_hads_d.setItemText(2, QCoreApplication.translate("MDRK", u"0", None))
        self.comboBox_hads_d.setItemText(3, QCoreApplication.translate("MDRK", u"1", None))
        self.comboBox_hads_d.setItemText(4, QCoreApplication.translate("MDRK", u"2", None))
        self.comboBox_hads_d.setItemText(5, QCoreApplication.translate("MDRK", u"3", None))
        self.comboBox_hads_d.setItemText(6, QCoreApplication.translate("MDRK", u"4", None))
        self.comboBox_hads_d.setItemText(7, QCoreApplication.translate("MDRK", u"5", None))
        self.comboBox_hads_d.setItemText(8, QCoreApplication.translate("MDRK", u"6", None))
        self.comboBox_hads_d.setItemText(9, QCoreApplication.translate("MDRK", u"7", None))
        self.comboBox_hads_d.setItemText(10, QCoreApplication.translate("MDRK", u"8", None))
        self.comboBox_hads_d.setItemText(11, QCoreApplication.translate("MDRK", u"9", None))
        self.comboBox_hads_d.setItemText(12, QCoreApplication.translate("MDRK", u"10", None))
        self.comboBox_hads_d.setItemText(13, QCoreApplication.translate("MDRK", u"11", None))
        self.comboBox_hads_d.setItemText(14, QCoreApplication.translate("MDRK", u"12", None))
        self.comboBox_hads_d.setItemText(15, QCoreApplication.translate("MDRK", u"13", None))
        self.comboBox_hads_d.setItemText(16, QCoreApplication.translate("MDRK", u"14", None))
        self.comboBox_hads_d.setItemText(17, QCoreApplication.translate("MDRK", u"15", None))
        self.comboBox_hads_d.setItemText(18, QCoreApplication.translate("MDRK", u"16", None))
        self.comboBox_hads_d.setItemText(19, QCoreApplication.translate("MDRK", u"17", None))
        self.comboBox_hads_d.setItemText(20, QCoreApplication.translate("MDRK", u"18", None))
        self.comboBox_hads_d.setItemText(21, QCoreApplication.translate("MDRK", u"19", None))
        self.comboBox_hads_d.setItemText(22, QCoreApplication.translate("MDRK", u"20", None))
        self.comboBox_hads_d.setItemText(23, QCoreApplication.translate("MDRK", u"21", None))

        self.comboBox_moca.setItemText(0, "")
        self.comboBox_moca.setItemText(1, QCoreApplication.translate("MDRK", u"UN", None))
        self.comboBox_moca.setItemText(2, QCoreApplication.translate("MDRK", u"30", None))
        self.comboBox_moca.setItemText(3, QCoreApplication.translate("MDRK", u"29", None))
        self.comboBox_moca.setItemText(4, QCoreApplication.translate("MDRK", u"28", None))
        self.comboBox_moca.setItemText(5, QCoreApplication.translate("MDRK", u"27", None))
        self.comboBox_moca.setItemText(6, QCoreApplication.translate("MDRK", u"26", None))
        self.comboBox_moca.setItemText(7, QCoreApplication.translate("MDRK", u"25", None))
        self.comboBox_moca.setItemText(8, QCoreApplication.translate("MDRK", u"24", None))
        self.comboBox_moca.setItemText(9, QCoreApplication.translate("MDRK", u"23", None))
        self.comboBox_moca.setItemText(10, QCoreApplication.translate("MDRK", u"22", None))
        self.comboBox_moca.setItemText(11, QCoreApplication.translate("MDRK", u"21", None))
        self.comboBox_moca.setItemText(12, QCoreApplication.translate("MDRK", u"20", None))
        self.comboBox_moca.setItemText(13, QCoreApplication.translate("MDRK", u"19", None))
        self.comboBox_moca.setItemText(14, QCoreApplication.translate("MDRK", u"18", None))
        self.comboBox_moca.setItemText(15, QCoreApplication.translate("MDRK", u"17", None))
        self.comboBox_moca.setItemText(16, QCoreApplication.translate("MDRK", u"16", None))
        self.comboBox_moca.setItemText(17, QCoreApplication.translate("MDRK", u"15", None))
        self.comboBox_moca.setItemText(18, QCoreApplication.translate("MDRK", u"14", None))
        self.comboBox_moca.setItemText(19, QCoreApplication.translate("MDRK", u"13", None))
        self.comboBox_moca.setItemText(20, QCoreApplication.translate("MDRK", u"12", None))
        self.comboBox_moca.setItemText(21, QCoreApplication.translate("MDRK", u"11", None))
        self.comboBox_moca.setItemText(22, QCoreApplication.translate("MDRK", u"10", None))
        self.comboBox_moca.setItemText(23, QCoreApplication.translate("MDRK", u"9", None))
        self.comboBox_moca.setItemText(24, QCoreApplication.translate("MDRK", u"8", None))
        self.comboBox_moca.setItemText(25, QCoreApplication.translate("MDRK", u"7", None))
        self.comboBox_moca.setItemText(26, QCoreApplication.translate("MDRK", u"6", None))
        self.comboBox_moca.setItemText(27, QCoreApplication.translate("MDRK", u"5", None))
        self.comboBox_moca.setItemText(28, QCoreApplication.translate("MDRK", u"4", None))
        self.comboBox_moca.setItemText(29, QCoreApplication.translate("MDRK", u"3", None))
        self.comboBox_moca.setItemText(30, QCoreApplication.translate("MDRK", u"2", None))
        self.comboBox_moca.setItemText(31, QCoreApplication.translate("MDRK", u"1", None))
        self.comboBox_moca.setItemText(32, QCoreApplication.translate("MDRK", u"0", None))

        self.label_psy_moca_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>MoCA:</p></body></html>", None))
        self.label_psy_conclusion_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0417\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433\u0430:</p></body></html>", None))
        self.label_psy_name_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p align=\"right\">\u041f\u0441\u0438\u0445\u043e\u043b\u043e\u0433:</p></body></html>", None))
        self.label_lfk.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u041b\u0424\u041a:</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MDRK", u"\u0412\u0440\u0430\u0447-\u041b\u0424\u041a:", None))
        self.label_logo_dysphagia_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0433\u043b\u043e\u0442\u0430\u043d\u0438\u044f \u041a\u0418\u041c:</p></body></html>", None))
        self.comboBox_logo_disart.setItemText(0, "")
        self.comboBox_logo_disart.setItemText(1, QCoreApplication.translate("MDRK", u"UN", None))

        self.label_logo_proso_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0425\u0430\u0443\u0441-\u0411\u0440\u0430\u0430\u043a\u043c\u0430\u043d:</p></body></html>", None))
        self.label_logo_wasserman_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0412\u0430\u0441\u0441\u0435\u0440\u043c\u0430\u043d\u0430:</p></body></html>", None))
        self.comboBox_logo_wasserman.setItemText(0, "")
        self.comboBox_logo_wasserman.setItemText(1, QCoreApplication.translate("MDRK", u"UN", None))

        self.label_logo_disart_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0428\u043a\u0430\u043b\u0430 \u0414\u0438\u0437\u0430\u0440\u0442\u0440\u0438\u0438:</p></body></html>", None))
        self.comboBox_logo_dysphagia.setItemText(0, "")
        self.comboBox_logo_dysphagia.setItemText(1, QCoreApplication.translate("MDRK", u"UN", None))

        self.label_logo_name_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p align=\"right\">\u041b\u043e\u0433\u043e\u043f\u0435\u0434:</p></body></html>", None))
        self.comboBox_logo_proso.setItemText(0, "")
        self.comboBox_logo_proso.setItemText(1, QCoreApplication.translate("MDRK", u"UN", None))

        self.label_logo_conclusion_2.setText(QCoreApplication.translate("MDRK", u"<html><head/><body><p>\u0417\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043b\u043e\u0433\u043e\u043f\u0435\u0434\u0430:</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mdrk), QCoreApplication.translate("MDRK", u"\u041c\u0414\u0420\u041a", None))
        self.groupBox_wom.setTitle(QCoreApplication.translate("MDRK", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("MDRK", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("MDRK", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("MDRK", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.label_Pt_info.setText(QCoreApplication.translate("MDRK", u"PatientInfo\n"
"fff", None))
        self.labelTimeline.setText("")
    # retranslateUi

