# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drugs_dictionary.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Almanac_drugs(object):
    def setupUi(self, Almanac_drugs):
        if not Almanac_drugs.objectName():
            Almanac_drugs.setObjectName(u"Almanac_drugs")
        Almanac_drugs.resize(631, 726)
        Almanac_drugs.setMinimumSize(QSize(631, 726))
        Almanac_drugs.setMaximumSize(QSize(631, 726))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        Almanac_drugs.setFont(font)
        self.centralwidget = QWidget(Almanac_drugs)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 611, 719))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_Pt_info = QLabel(self.layoutWidget)
        self.label_Pt_info.setObjectName(u"label_Pt_info")
        self.label_Pt_info.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_Pt_info)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.labelAlmanac = QLabel(self.layoutWidget)
        self.labelAlmanac.setObjectName(u"labelAlmanac")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.labelAlmanac.setFont(font1)

        self.verticalLayout_4.addWidget(self.labelAlmanac)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plainTextEdit_ds = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit_ds.setObjectName(u"plainTextEdit_ds")
        self.plainTextEdit_ds.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_3.addWidget(self.plainTextEdit_ds, 7, 1, 1, 2)

        self.label_name_latin = QLabel(self.layoutWidget)
        self.label_name_latin.setObjectName(u"label_name_latin")

        self.gridLayout_3.addWidget(self.label_name_latin, 5, 0, 1, 1)

        self.lineEdit_name_latin = QLineEdit(self.layoutWidget)
        self.lineEdit_name_latin.setObjectName(u"lineEdit_name_latin")

        self.gridLayout_3.addWidget(self.lineEdit_name_latin, 5, 1, 1, 2)

        self.lineEdit_doses = QLineEdit(self.layoutWidget)
        self.lineEdit_doses.setObjectName(u"lineEdit_doses")

        self.gridLayout_3.addWidget(self.lineEdit_doses, 6, 1, 1, 2)

        self.plainTextEdit_name_torg = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit_name_torg.setObjectName(u"plainTextEdit_name_torg")
        self.plainTextEdit_name_torg.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_3.addWidget(self.plainTextEdit_name_torg, 8, 1, 1, 2)

        self.pushButton_add_drug = QPushButton(self.layoutWidget)
        self.pushButton_add_drug.setObjectName(u"pushButton_add_drug")

        self.gridLayout_3.addWidget(self.pushButton_add_drug, 9, 0, 1, 3)

        self.lineEdit_name = QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.gridLayout_3.addWidget(self.lineEdit_name, 4, 1, 1, 2)

        self.label_ds = QLabel(self.layoutWidget)
        self.label_ds.setObjectName(u"label_ds")

        self.gridLayout_3.addWidget(self.label_ds, 7, 0, 1, 1)

        self.label_doses = QLabel(self.layoutWidget)
        self.label_doses.setObjectName(u"label_doses")

        self.gridLayout_3.addWidget(self.label_doses, 6, 0, 1, 1)

        self.comboBox_group = QComboBox(self.layoutWidget)
        self.comboBox_group.addItem("")
        self.comboBox_group.setObjectName(u"comboBox_group")
        self.comboBox_group.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox_group, 1, 1, 1, 2)

        self.label_name = QLabel(self.layoutWidget)
        self.label_name.setObjectName(u"label_name")

        self.gridLayout_3.addWidget(self.label_name, 4, 0, 1, 1)

        self.label_group = QLabel(self.layoutWidget)
        self.label_group.setObjectName(u"label_group")

        self.gridLayout_3.addWidget(self.label_group, 1, 0, 1, 1)

        self.label_name_torg = QLabel(self.layoutWidget)
        self.label_name_torg.setObjectName(u"label_name_torg")

        self.gridLayout_3.addWidget(self.label_name_torg, 8, 0, 1, 1)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 78))
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 10, 291, 68))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_tab = QRadioButton(self.layoutWidget1)
        self.radioButton_tab.setObjectName(u"radioButton_tab")

        self.gridLayout_2.addWidget(self.radioButton_tab, 0, 0, 1, 1)

        self.radioButton_susp = QRadioButton(self.layoutWidget1)
        self.radioButton_susp.setObjectName(u"radioButton_susp")

        self.gridLayout_2.addWidget(self.radioButton_susp, 0, 1, 1, 1)

        self.radioButton_caps = QRadioButton(self.layoutWidget1)
        self.radioButton_caps.setObjectName(u"radioButton_caps")

        self.gridLayout_2.addWidget(self.radioButton_caps, 1, 0, 1, 1)

        self.radioButton_pulv = QRadioButton(self.layoutWidget1)
        self.radioButton_pulv.setObjectName(u"radioButton_pulv")

        self.gridLayout_2.addWidget(self.radioButton_pulv, 1, 1, 1, 1)

        self.radioButton_sol = QRadioButton(self.layoutWidget1)
        self.radioButton_sol.setObjectName(u"radioButton_sol")

        self.gridLayout_2.addWidget(self.radioButton_sol, 2, 0, 1, 1)

        self.radioButton_supp = QRadioButton(self.layoutWidget1)
        self.radioButton_supp.setObjectName(u"radioButton_supp")

        self.gridLayout_2.addWidget(self.radioButton_supp, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 2, 3)

        self.labelAddDrug = QLabel(self.layoutWidget)
        self.labelAddDrug.setObjectName(u"labelAddDrug")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.labelAddDrug.setFont(font2)

        self.gridLayout_3.addWidget(self.labelAddDrug, 0, 0, 1, 3)


        self.gridLayout.addLayout(self.gridLayout_3, 6, 0, 1, 2)

        self.tableWidget = QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 250))
        self.tableWidget.setFont(font)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 5, 1)

        self.pushButton_start_almanac = QPushButton(self.layoutWidget)
        self.pushButton_start_almanac.setObjectName(u"pushButton_start_almanac")

        self.gridLayout.addWidget(self.pushButton_start_almanac, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.pushButton_statistic = QPushButton(self.layoutWidget)
        self.pushButton_statistic.setObjectName(u"pushButton_statistic")

        self.gridLayout.addWidget(self.pushButton_statistic, 2, 1, 1, 1)

        self.pushButton_send = QPushButton(self.layoutWidget)
        self.pushButton_send.setObjectName(u"pushButton_send")

        self.gridLayout.addWidget(self.pushButton_send, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textBrowser = QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_2.addWidget(self.textBrowser)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButtonSaveExit = QPushButton(self.layoutWidget)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(217, 217, 217, 255))
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
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
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
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButtonSaveExit.setPalette(palette)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.pushButtonSaveExit.setFont(font3)

        self.horizontalLayout_2.addWidget(self.pushButtonSaveExit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        Almanac_drugs.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.comboBox_group, self.lineEdit_name)
        QWidget.setTabOrder(self.lineEdit_name, self.lineEdit_name_latin)
        QWidget.setTabOrder(self.lineEdit_name_latin, self.lineEdit_doses)
        QWidget.setTabOrder(self.lineEdit_doses, self.plainTextEdit_ds)
        QWidget.setTabOrder(self.plainTextEdit_ds, self.plainTextEdit_name_torg)
        QWidget.setTabOrder(self.plainTextEdit_name_torg, self.pushButton_add_drug)
        QWidget.setTabOrder(self.pushButton_add_drug, self.radioButton_sol)
        QWidget.setTabOrder(self.radioButton_sol, self.radioButton_tab)
        QWidget.setTabOrder(self.radioButton_tab, self.pushButtonSaveExit)
        QWidget.setTabOrder(self.pushButtonSaveExit, self.radioButton_pulv)
        QWidget.setTabOrder(self.radioButton_pulv, self.radioButton_susp)
        QWidget.setTabOrder(self.radioButton_susp, self.radioButton_caps)
        QWidget.setTabOrder(self.radioButton_caps, self.radioButton_supp)
        QWidget.setTabOrder(self.radioButton_supp, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.pushButton_start_almanac)
        QWidget.setTabOrder(self.pushButton_start_almanac, self.pushButton_statistic)
        QWidget.setTabOrder(self.pushButton_statistic, self.pushButton_send)
        QWidget.setTabOrder(self.pushButton_send, self.textBrowser)

        self.retranslateUi(Almanac_drugs)

        QMetaObject.connectSlotsByName(Almanac_drugs)
    # setupUi

    def retranslateUi(self, Almanac_drugs):
        Almanac_drugs.setWindowTitle(QCoreApplication.translate("Almanac_drugs", u"\u041b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430", None))
        self.label_Pt_info.setText(QCoreApplication.translate("Almanac_drugs", u"World of Medicine", None))
        self.labelAlmanac.setText(QCoreApplication.translate("Almanac_drugs", u"<html><head/><body><p align=\"center\">\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432</p></body></html>", None))
        self.plainTextEdit_ds.setPlaceholderText(QCoreApplication.translate("Almanac_drugs", u"\u041d-\u0440: \u0432\u043d\u0443\u0442\u0440\u044c \u043d\u0430 \u043d\u043e\u0447\u044c \u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e; \u0432\u043d\u0443\u0442\u0440\u044c \u043e\u0434\u043d\u043e\u043a\u0440\u0430\u0442\u043d\u043e \u21161; \u0432\u043d\u0443\u0442\u0440\u044c \u043f\u043e 1 \u0442\u0430\u0431\u043b\u0435\u0442\u043a\u0435 3 \u0440\u0430\u0437\u0430 \u0432 \u0434\u0435\u043d\u044c", None))
        self.label_name_latin.setText(QCoreApplication.translate("Almanac_drugs", u"\u043f\u043e-\u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438:", None))
        self.lineEdit_name_latin.setPlaceholderText(QCoreApplication.translate("Almanac_drugs", u"\u041d-\u0440: Carbamasepini", None))
        self.lineEdit_doses.setPlaceholderText(QCoreApplication.translate("Almanac_drugs", u"\u041d-\u0440: 200mg; 400mg", None))
        self.plainTextEdit_name_torg.setPlaceholderText(QCoreApplication.translate("Almanac_drugs", u"\u041d-\u0440: \u0424\u0438\u043d\u043b\u0435\u043f\u0441\u0438\u043d; \u0417\u0435\u043f\u0442\u043e\u043b", None))
        self.pushButton_add_drug.setText(QCoreApplication.translate("Almanac_drugs", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0435\u043a.\u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e \u0432 \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("Almanac_drugs", u"\u041d-\u0440: \u041a\u0430\u0440\u0431\u0430\u043c\u0430\u0437\u0435\u043f\u0438\u043d", None))
        self.label_ds.setText(QCoreApplication.translate("Almanac_drugs", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435:", None))
        self.label_doses.setText(QCoreApplication.translate("Almanac_drugs", u"\u0414\u043e\u0437\u0438\u0440\u043e\u0432\u043a\u0438:", None))
        self.comboBox_group.setItemText(0, "")

        self.label_name.setText(QCoreApplication.translate("Almanac_drugs", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_group.setText(QCoreApplication.translate("Almanac_drugs", u"\u0424\u0430\u0440\u043c.\u0433\u0440\u0443\u043f\u043f\u0430:", None))
        self.label_name_torg.setText(QCoreApplication.translate("Almanac_drugs", u"\u0422\u043e\u0440\u0433.\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Almanac_drugs", u"\u041b\u0435\u043a.\u0444\u043e\u0440\u043c\u0430", None))
        self.radioButton_tab.setText(QCoreApplication.translate("Almanac_drugs", u"\u0422\u0430\u0431\u043b\u0435\u0442\u043a\u0438", None))
        self.radioButton_susp.setText(QCoreApplication.translate("Almanac_drugs", u"\u0421\u0443\u0441\u043f\u0435\u043d\u0437\u0438\u044f", None))
        self.radioButton_caps.setText(QCoreApplication.translate("Almanac_drugs", u"\u041a\u0430\u043f\u0441\u0443\u043b\u044b", None))
        self.radioButton_pulv.setText(QCoreApplication.translate("Almanac_drugs", u"\u041f\u043e\u0440\u043e\u0448\u043e\u043a", None))
        self.radioButton_sol.setText(QCoreApplication.translate("Almanac_drugs", u"\u0420\u0430\u0441\u0442\u0432\u043e\u0440", None))
        self.radioButton_supp.setText(QCoreApplication.translate("Almanac_drugs", u"\u0421\u0443\u043f\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0438\u0439", None))
        self.labelAddDrug.setText(QCoreApplication.translate("Almanac_drugs", u"<html><head/><body><p align=\"center\">\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043b\u0435\u043a.\u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442\u0430 \u0432 \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a</p></body></html>", None))
        self.pushButton_start_almanac.setText(QCoreApplication.translate("Almanac_drugs", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c\n"
"\u043c\u0435\u043d\u044e", None))
        self.pushButton_statistic.setText(QCoreApplication.translate("Almanac_drugs", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.pushButton_send.setText(QCoreApplication.translate("Almanac_drugs", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c\n"
"\u0434\u0440\u0443\u0433\u0443", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Almanac_drugs", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto';\"><br /></span></p></body></html>", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("Almanac_drugs", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

