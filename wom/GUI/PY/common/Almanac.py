# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Almanac.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Almanac(object):
    def setupUi(self, Almanac):
        if not Almanac.objectName():
            Almanac.setObjectName(u"Almanac")
        Almanac.resize(1123, 567)
        Almanac.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout = QVBoxLayout(Almanac)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainframe = QFrame(Almanac)
        self.mainframe.setObjectName(u"mainframe")
        self.gridLayout_5 = QGridLayout(self.mainframe)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(5)
        self.dataframe = QFrame(self.mainframe)
        self.dataframe.setObjectName(u"dataframe")
        self.dataframe.setMinimumSize(QSize(0, 0))
        self.dataframe.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.gridLayout = QGridLayout(self.dataframe)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 2, 1)

        self.pushButton_start_almanac = QPushButton(self.dataframe)
        self.pushButton_start_almanac.setObjectName(u"pushButton_start_almanac")
        self.pushButton_start_almanac.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 7px;\n"
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

        self.gridLayout.addWidget(self.pushButton_start_almanac, 1, 1, 1, 1)

        self.label = QLabel(self.dataframe)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(112, 38, 50, 150);\n"
"border: none;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.tableWidget = QTableWidget(self.dataframe)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(500, 0))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border: 1px solid rgba(50, 98, 115, 255);\n"
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

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 3, 1)


        self.gridLayout_5.addWidget(self.dataframe, 0, 1, 2, 1)

        self.add_drug_frame = QFrame(self.mainframe)
        self.add_drug_frame.setObjectName(u"add_drug_frame")
        self.add_drug_frame.setMinimumSize(QSize(500, 0))
        self.add_drug_frame.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.gridLayout_3 = QGridLayout(self.add_drug_frame)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.plainTextEdit_ds = QPlainTextEdit(self.add_drug_frame)
        self.plainTextEdit_ds.setObjectName(u"plainTextEdit_ds")
        self.plainTextEdit_ds.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_ds.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.gridLayout_3.addWidget(self.plainTextEdit_ds, 7, 1, 1, 2)

        self.label_name_latin = QLabel(self.add_drug_frame)
        self.label_name_latin.setObjectName(u"label_name_latin")
        self.label_name_latin.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_name_latin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_name_latin, 5, 0, 1, 1)

        self.lineEdit_doses = QLineEdit(self.add_drug_frame)
        self.lineEdit_doses.setObjectName(u"lineEdit_doses")
        self.lineEdit_doses.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.gridLayout_3.addWidget(self.lineEdit_doses, 6, 1, 1, 2)

        self.lineEdit_name_latin = QLineEdit(self.add_drug_frame)
        self.lineEdit_name_latin.setObjectName(u"lineEdit_name_latin")
        self.lineEdit_name_latin.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.gridLayout_3.addWidget(self.lineEdit_name_latin, 5, 1, 1, 2)

        self.pushButton_add_drug = QPushButton(self.add_drug_frame)
        self.pushButton_add_drug.setObjectName(u"pushButton_add_drug")
        self.pushButton_add_drug.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 15px;\n"
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

        self.gridLayout_3.addWidget(self.pushButton_add_drug, 9, 0, 1, 3)

        self.label_name_torg = QLabel(self.add_drug_frame)
        self.label_name_torg.setObjectName(u"label_name_torg")
        self.label_name_torg.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_name_torg.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout_3.addWidget(self.label_name_torg, 8, 0, 1, 1)

        self.plainTextEdit_name_torg = QPlainTextEdit(self.add_drug_frame)
        self.plainTextEdit_name_torg.setObjectName(u"plainTextEdit_name_torg")
        self.plainTextEdit_name_torg.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_name_torg.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.gridLayout_3.addWidget(self.plainTextEdit_name_torg, 8, 1, 1, 2)

        self.label_ds = QLabel(self.add_drug_frame)
        self.label_ds.setObjectName(u"label_ds")
        self.label_ds.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_ds.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout_3.addWidget(self.label_ds, 7, 0, 1, 1)

        self.comboBox_group = QComboBox(self.add_drug_frame)
        self.comboBox_group.addItem("")
        self.comboBox_group.setObjectName(u"comboBox_group")
        self.comboBox_group.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBox_group.setEditable(True)
        self.comboBox_group.setModelColumn(0)

        self.gridLayout_3.addWidget(self.comboBox_group, 1, 1, 1, 2)

        self.label_name = QLabel(self.add_drug_frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_name, 4, 0, 1, 1)

        self.labelAddDrug = QLabel(self.add_drug_frame)
        self.labelAddDrug.setObjectName(u"labelAddDrug")
        self.labelAddDrug.setMinimumSize(QSize(0, 20))
        self.labelAddDrug.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.labelAddDrug.setFont(font1)
        self.labelAddDrug.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 150);\n"
"border: none;\n"
"")
        self.labelAddDrug.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.labelAddDrug, 0, 0, 1, 3)

        self.label_doses = QLabel(self.add_drug_frame)
        self.label_doses.setObjectName(u"label_doses")
        self.label_doses.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_doses.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_doses, 6, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.add_drug_frame)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.gridLayout_3.addWidget(self.lineEdit_name, 4, 1, 1, 2)

        self.label_group = QLabel(self.add_drug_frame)
        self.label_group.setObjectName(u"label_group")
        self.label_group.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_group.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_group, 1, 0, 1, 1)

        self.drugform_frame_1 = QFrame(self.add_drug_frame)
        self.drugform_frame_1.setObjectName(u"drugform_frame_1")
        self.drugform_frame_1.setMinimumSize(QSize(0, 0))
        self.drugform_frame_1.setStyleSheet(u"border: None;\n"
"background-color: transparent;")
        self.gridLayout_4 = QGridLayout(self.drugform_frame_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label_group_2 = QLabel(self.drugform_frame_1)
        self.label_group_2.setObjectName(u"label_group_2")
        self.label_group_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_4.addWidget(self.label_group_2, 0, 0, 1, 2)

        self.drugform_frame_2 = QFrame(self.drugform_frame_1)
        self.drugform_frame_2.setObjectName(u"drugform_frame_2")
        self.gridLayout_2 = QGridLayout(self.drugform_frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_tab = QRadioButton(self.drugform_frame_2)
        self.radioButton_tab.setObjectName(u"radioButton_tab")
        self.radioButton_tab.setStyleSheet(u"QRadioButton {\n"
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

        self.gridLayout_2.addWidget(self.radioButton_tab, 0, 0, 1, 1)

        self.radioButton_susp = QRadioButton(self.drugform_frame_2)
        self.radioButton_susp.setObjectName(u"radioButton_susp")
        self.radioButton_susp.setStyleSheet(u"QRadioButton {\n"
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

        self.gridLayout_2.addWidget(self.radioButton_susp, 0, 1, 1, 1)

        self.radioButton_caps = QRadioButton(self.drugform_frame_2)
        self.radioButton_caps.setObjectName(u"radioButton_caps")
        self.radioButton_caps.setStyleSheet(u"QRadioButton {\n"
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

        self.gridLayout_2.addWidget(self.radioButton_caps, 1, 0, 1, 1)

        self.radioButton_pulv = QRadioButton(self.drugform_frame_2)
        self.radioButton_pulv.setObjectName(u"radioButton_pulv")
        self.radioButton_pulv.setStyleSheet(u"QRadioButton {\n"
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

        self.gridLayout_2.addWidget(self.radioButton_pulv, 1, 1, 1, 1)

        self.radioButton_sol = QRadioButton(self.drugform_frame_2)
        self.radioButton_sol.setObjectName(u"radioButton_sol")
        self.radioButton_sol.setStyleSheet(u"QRadioButton {\n"
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

        self.gridLayout_2.addWidget(self.radioButton_sol, 2, 0, 1, 1)

        self.radioButton_supp = QRadioButton(self.drugform_frame_2)
        self.radioButton_supp.setObjectName(u"radioButton_supp")
        self.radioButton_supp.setStyleSheet(u"QRadioButton {\n"
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

        self.gridLayout_2.addWidget(self.radioButton_supp, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.drugform_frame_2, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.drugform_frame_1, 2, 0, 2, 3)


        self.gridLayout_5.addWidget(self.add_drug_frame, 0, 2, 2, 1)

        self.horizontalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.bot_frame = QFrame(self.mainframe)
        self.bot_frame.setObjectName(u"bot_frame")
        self.bot_frame.setMaximumSize(QSize(16777215, 80))
        self.bot_frame.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.horizontalLayout_2 = QHBoxLayout(self.bot_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.textBrowser = QTextBrowser(self.bot_frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.textBrowser)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButtonSaveExit = QPushButton(self.bot_frame)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(50, 98, 115, 190))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush2 = QBrush(QColor(236, 236, 236, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(108, 108, 108, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(145, 145, 145, 255))
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
        brush7 = QBrush(QColor(0, 0, 0, 128))
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
        brush8 = QBrush(QColor(217, 217, 217, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonSaveExit.setPalette(palette)
        self.pushButtonSaveExit.setFont(font)
        self.pushButtonSaveExit.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 7px;\n"
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

        self.horizontalLayout_2.addWidget(self.pushButtonSaveExit)


        self.gridLayout_5.addWidget(self.bot_frame, 2, 1, 1, 2)


        self.verticalLayout.addWidget(self.mainframe)

        QWidget.setTabOrder(self.comboBox_group, self.radioButton_tab)
        QWidget.setTabOrder(self.radioButton_tab, self.radioButton_caps)
        QWidget.setTabOrder(self.radioButton_caps, self.radioButton_sol)
        QWidget.setTabOrder(self.radioButton_sol, self.radioButton_susp)
        QWidget.setTabOrder(self.radioButton_susp, self.radioButton_pulv)
        QWidget.setTabOrder(self.radioButton_pulv, self.radioButton_supp)
        QWidget.setTabOrder(self.radioButton_supp, self.lineEdit_name)
        QWidget.setTabOrder(self.lineEdit_name, self.lineEdit_name_latin)
        QWidget.setTabOrder(self.lineEdit_name_latin, self.lineEdit_doses)
        QWidget.setTabOrder(self.lineEdit_doses, self.plainTextEdit_ds)
        QWidget.setTabOrder(self.plainTextEdit_ds, self.plainTextEdit_name_torg)
        QWidget.setTabOrder(self.plainTextEdit_name_torg, self.pushButton_add_drug)
        QWidget.setTabOrder(self.pushButton_add_drug, self.pushButton_start_almanac)
        QWidget.setTabOrder(self.pushButton_start_almanac, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.textBrowser)

        self.retranslateUi(Almanac)

        QMetaObject.connectSlotsByName(Almanac)
    # setupUi

    def retranslateUi(self, Almanac):
        Almanac.setWindowTitle(QCoreApplication.translate("Almanac", u"Form", None))
        self.pushButton_start_almanac.setText(QCoreApplication.translate("Almanac", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c\n"
"\u043c\u0435\u043d\u044e", None))
        self.label.setText(QCoreApplication.translate("Almanac", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432", None))
        self.plainTextEdit_ds.setPlaceholderText(QCoreApplication.translate("Almanac", u"\u041d-\u0440: \u0432\u043d\u0443\u0442\u0440\u044c \u043d\u0430 \u043d\u043e\u0447\u044c \u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e; \u0432\u043d\u0443\u0442\u0440\u044c \u043e\u0434\u043d\u043e\u043a\u0440\u0430\u0442\u043d\u043e \u21161; \u0432\u043d\u0443\u0442\u0440\u044c \u043f\u043e 1 \u0442\u0430\u0431\u043b\u0435\u0442\u043a\u0435 3 \u0440\u0430\u0437\u0430 \u0432 \u0434\u0435\u043d\u044c", None))
        self.label_name_latin.setText(QCoreApplication.translate("Almanac", u"\u043f\u043e-\u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438:", None))
        self.lineEdit_doses.setPlaceholderText(QCoreApplication.translate("Almanac", u"\u041d-\u0440: 200mg; 400mg", None))
        self.lineEdit_name_latin.setPlaceholderText(QCoreApplication.translate("Almanac", u"\u041d-\u0440: Carbamasepini", None))
        self.pushButton_add_drug.setText(QCoreApplication.translate("Almanac", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a", None))
        self.label_name_torg.setText(QCoreApplication.translate("Almanac", u"\u0422\u043e\u0440\u0433\u043e\u0432\u044b\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f:", None))
        self.plainTextEdit_name_torg.setPlaceholderText(QCoreApplication.translate("Almanac", u"\u041d-\u0440: \u0424\u0438\u043d\u043b\u0435\u043f\u0441\u0438\u043d; \u0417\u0435\u043f\u0442\u043e\u043b", None))
        self.label_ds.setText(QCoreApplication.translate("Almanac", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435:", None))
        self.comboBox_group.setItemText(0, "")

        self.comboBox_group.setPlaceholderText(QCoreApplication.translate("Almanac", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0438\u043b\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u0443\u044e", None))
        self.label_name.setText(QCoreApplication.translate("Almanac", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 (\u041c\u041d\u041d):", None))
        self.labelAddDrug.setText(QCoreApplication.translate("Almanac", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430", None))
        self.label_doses.setText(QCoreApplication.translate("Almanac", u"\u0414\u043e\u0437\u0438\u0440\u043e\u0432\u043a\u0438:", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("Almanac", u"\u041d-\u0440: \u041a\u0430\u0440\u0431\u0430\u043c\u0430\u0437\u0435\u043f\u0438\u043d", None))
        self.label_group.setText(QCoreApplication.translate("Almanac", u"\u0424\u0430\u0440\u043c.\u0433\u0440\u0443\u043f\u043f\u0430:", None))
        self.label_group_2.setText(QCoreApplication.translate("Almanac", u"\u041b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0430:", None))
        self.radioButton_tab.setText(QCoreApplication.translate("Almanac", u"\u0422\u0430\u0431\u043b\u0435\u0442\u043a\u0438", None))
        self.radioButton_susp.setText(QCoreApplication.translate("Almanac", u"\u0421\u0443\u0441\u043f\u0435\u043d\u0437\u0438\u044f", None))
        self.radioButton_caps.setText(QCoreApplication.translate("Almanac", u"\u041a\u0430\u043f\u0441\u0443\u043b\u044b", None))
        self.radioButton_pulv.setText(QCoreApplication.translate("Almanac", u"\u041f\u043e\u0440\u043e\u0448\u043e\u043a", None))
        self.radioButton_sol.setText(QCoreApplication.translate("Almanac", u"\u0420\u0430\u0441\u0442\u0432\u043e\u0440", None))
        self.radioButton_supp.setText(QCoreApplication.translate("Almanac", u"\u0421\u0443\u043f\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0438\u0439", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Almanac", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("Almanac", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

