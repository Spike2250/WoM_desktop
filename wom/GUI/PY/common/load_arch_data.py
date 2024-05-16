# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_arch_data.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Load_Arch(object):
    def setupUi(self, Load_Arch):
        if not Load_Arch.objectName():
            Load_Arch.setObjectName(u"Load_Arch")
        Load_Arch.setEnabled(True)
        Load_Arch.resize(736, 564)
        Load_Arch.setMinimumSize(QSize(0, 0))
        Load_Arch.setMaximumSize(QSize(10000, 10000))
        font = QFont()
        font.setFamilies([u"Roboto"])
        Load_Arch.setFont(font)
        Load_Arch.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout = QVBoxLayout(Load_Arch)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main = QFrame(Load_Arch)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")
        self.gridLayout = QGridLayout(self.main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 2, 1, 2)

        self.label_status = QLabel(self.main)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(0, 50))
        self.label_status.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_status.setFont(font1)
        self.label_status.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"")
        self.label_status.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_status, 6, 0, 1, 4)

        self.pushButton_yes = QPushButton(self.main)
        self.pushButton_yes.setObjectName(u"pushButton_yes")
        self.pushButton_yes.setMinimumSize(QSize(0, 70))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(14)
        self.pushButton_yes.setFont(font2)
        self.pushButton_yes.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_yes, 3, 3, 2, 1)

        self.checkBox = QCheckBox(self.main)
        self.checkBox.setObjectName(u"checkBox")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(11)
        self.checkBox.setFont(font3)
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
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

        self.gridLayout.addWidget(self.checkBox, 3, 2, 1, 1)

        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.copy_frame = QFrame(self.main)
        self.copy_frame.setObjectName(u"copy_frame")
        self.copy_frame.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.copy_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.copy_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.fullcopy = QRadioButton(self.copy_frame)
        self.fullcopy.setObjectName(u"fullcopy")
        self.fullcopy.setStyleSheet(u"QRadioButton {\n"
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
        self.fullcopy.setChecked(True)

        self.verticalLayout_2.addWidget(self.fullcopy)

        self.adm_copy = QRadioButton(self.copy_frame)
        self.adm_copy.setObjectName(u"adm_copy")
        self.adm_copy.setStyleSheet(u"QRadioButton {\n"
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

        self.verticalLayout_2.addWidget(self.adm_copy)

        self.dis_to_adm_copy = QRadioButton(self.copy_frame)
        self.dis_to_adm_copy.setObjectName(u"dis_to_adm_copy")
        self.dis_to_adm_copy.setStyleSheet(u"QRadioButton {\n"
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

        self.verticalLayout_2.addWidget(self.dis_to_adm_copy)


        self.gridLayout.addWidget(self.copy_frame, 2, 0, 4, 1)

        self.tableWidget = QTableWidget(self.main)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
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

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 4)

        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: None;")

        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 2)

        self.pushButton_no = QPushButton(self.main)
        self.pushButton_no.setObjectName(u"pushButton_no")
        self.pushButton_no.setMinimumSize(QSize(0, 30))
        self.pushButton_no.setFont(font2)
        self.pushButton_no.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_no, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.main)


        self.retranslateUi(Load_Arch)

        QMetaObject.connectSlotsByName(Load_Arch)
    # setupUi

    def retranslateUi(self, Load_Arch):
        Load_Arch.setWindowTitle(QCoreApplication.translate("Load_Arch", u"Form", None))
        self.label_status.setText(QCoreApplication.translate("Load_Arch", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton_yes.setText(QCoreApplication.translate("Load_Arch", u"\u0414\u0430, \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e\n"
"\u0438\u0441\u0442\u043e\u0440\u0438\u044e \u0431\u043e\u043b\u0435\u0437\u043d\u0438 \u043d\u0430\n"
"\u043e\u0441\u043d\u043e\u0432\u0435 \u0430\u0440\u0445\u0438\u0432\u043d\u043e\u0439", None))
        self.checkBox.setText(QCoreApplication.translate("Load_Arch", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u044e \u043e\u0442\u043a\u0430\u0437\n"
"\u043e\u0442 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Load_Arch", u"<html><head/><body><p align=\"center\">\u041e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u044b \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u044b \u0432 \u0430\u0440\u0445\u0438\u0432\u0435 \u0438\u0441\u0442\u043e\u0440\u0438\u0439 \u0431\u043e\u043b\u0435\u0437\u043d\u0435\u0439, <br/><span style=\" font-weight:600;\">\u0441 \u0438\u0434\u0435\u043d\u0442\u0438\u0447\u043d\u044b\u043c\u0438 \u0424\u0418\u041e \u0438 \u0434\u0430\u0442\u043e\u0439 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Load_Arch", u"\u0420\u0435\u0436\u0438\u043c \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.fullcopy.setText(QCoreApplication.translate("Load_Arch", u"\u043f\u043e\u043b\u043d\u043e\u0435", None))
        self.adm_copy.setText(QCoreApplication.translate("Load_Arch", u"\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0440\u0438 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0438", None))
        self.dis_to_adm_copy.setText(QCoreApplication.translate("Load_Arch", u"\u0432\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0440\u0438 \u0432\u044b\u043f\u0438\u0441\u043a\u0435\n"
"\u043a\u0430\u043a \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0440\u0438 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0438", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Load_Arch", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Load_Arch", u"\u041c\u041a\u0411-10", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Load_Arch", u"\u0414\u0430\u0442\u044b", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Load_Arch", u"uin", None));
        self.label_2.setText(QCoreApplication.translate("Load_Arch", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0430\u0440\u0445\u0438\u0432\u0430 \u043a\u0430\u043a<br/>\u043e\u0441\u043d\u043e\u0432\u0443 \u043d\u043e\u0432\u043e\u0439 \u0438\u0441\u0442\u043e\u0440\u0438\u0438 \u0431\u043e\u043b\u0435\u0437\u043d\u0438?</span></p></body></html>", None))
        self.pushButton_no.setText(QCoreApplication.translate("Load_Arch", u"\u041d\u0435\u0442", None))
    # retranslateUi

