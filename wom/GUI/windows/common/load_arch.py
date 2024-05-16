from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QTableWidgetItem as QTW_Item,
    QCheckBox,
    QAbstractItemView,
)

from wom.GUI.PY.common import load_arch_data
from wom.app_logic.db_func\
    .bucket_func import upload_history_to_yandex_cloud_bucket
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.copy_archive_case import arch_import


# Окно подтверждения
class Ui_load_arch_data(QtWidgets.QWidget,
                        load_arch_data.Ui_Load_Arch):
    def __init__(self, user_info, windows, main_win,
                 dictionary, histories, case_type):

        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.histories = histories
        self.case_type = case_type

        self.pushButton_yes.setEnabled(False)
        self.pushButton_yes.clicked.connect(self.yes)
        self.pushButton_no.setEnabled(False)
        self.pushButton_no.clicked.connect(self.change_buttons)
        self.checkBox.stateChanged.connect(self.change_buttons)
        self.refresh_table()

    def go_to_patient_card(self):
        self.save_history()
        self.open_patient_card()

    def open_patient_card(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows[self.case_type]['patient_card'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win,
                dictionary=self.d))
        win.show()
        self.main_win.close()

    def yes(self):
        index = self.is_alone_check_box()[1]
        copy_style = self.define_copy_style()
        self.d = arch_import(d=self.d,
                             d_arch=self.histories[index],
                             copy_style=copy_style)
        self.go_to_patient_card()

    def no(self):
        self.go_to_patient_card()

    def save_history(self):
        if self.case_type == 'omr':
            self.save_history_omr()
        elif self.case_type == 'bta':
            self.save_history_bta()
        else:
            raise ValueError

    # @upload_history_to_yandex_cloud_bucket('omr')
    def save_history_omr(self):
        write_all_data_to_db_omr(self.d)

    # @upload_history_to_yandex_cloud_bucket('bta')
    def save_history_bta(self):
        write_all_data_to_db_bta(self.d)

    def define_copy_style(self):
        if self.fullcopy.isChecked():
            style = 'full'
        elif self.adm_copy.isChecked():
            style = 'only_adm'
        elif self.dis_to_adm_copy.isChecked():
            style = 'dynamic'
        return style

    def change_buttons(self):
        if self.checkBox.isChecked():
            self.pushButton_no.setEnabled(True)
            self.pushButton_yes.setEnabled(False)
        else:
            self.pushButton_no.setEnabled(False)
            if self.is_alone_check_box()[0]:
                self.pushButton_yes.setEnabled(True)

    def refresh_table(self):
        self.tableWidget.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 160)
        self.tableWidget.setColumnWidth(2, 70)
        self.tableWidget.setColumnWidth(3, 170)
        self.tableWidget.setColumnWidth(4, 300)
        self.fill_table()

    def fill_table(self):
        self.tableWidget.setRowCount(len(self.histories))
        for i, case in enumerate(self.histories):
            check = QCheckBox('выбрать')
            check.stateChanged.connect(self.activate_button)
            style = '''
                QCheckBox {
                    color: #326273;
                    border: none;
                    background-color: none;
                }
                QCheckBox:checked {
                   color: #702632;
                }
                QCheckBox:disabled {
                   color: #EEEEEE;
                }
                QCheckBox::indicator:checked {
                    border-style:solid;
                    border-width: 1px;
                    border-color: #702632;
                    color: #FFFFFF;
                    background-color: #702632;
                }
                QCheckBox::indicator:!checked {
                    border-style:solid;
                    border-width: 1px;
                    border-color: #702632;
                    color: #FFFFFF;
                    background-color: none;
                }
                QCheckBox::indicator:disabled {
                    border-style:solid;
                    border-width: 1px;
                    border-color: #EEEEEE;
                    color: #FFFFFF;
                    background-color: transparent;
                }'''
            check.setStyleSheet(style)

            name = f"{case['фамилия']} {case['имя'][0]}{case['отчество'][0]}"
            mkb10 = f"{case['МКБ']}"
            dates = f"{case['дата_поступления']} - {case['дата_выписки']}"
            uin = f"{case['unic_number']}"

            self.tableWidget.setCellWidget(i, 0, check)
            self.tableWidget.setItem(i, 1, QTW_Item(name))
            self.tableWidget.setItem(i, 2, QTW_Item(mkb10))
            self.tableWidget.setItem(i, 3, QTW_Item(dates))
            self.tableWidget.setItem(i, 4, QTW_Item(uin))

    def is_alone_check_box(self):
        check_list = []
        for i in range(len(self.histories)):
            if self.tableWidget.cellWidget(i, 0).isChecked():
                check_list.append(i)
        if len(check_list) == 1:
            return (True, check_list[0])
        return (False, 0)

    def activate_button(self):
        if self.is_alone_check_box()[0] and not self.checkBox.isChecked():
            self.pushButton_yes.setEnabled(True)
        else:
            self.pushButton_yes.setEnabled(False)
