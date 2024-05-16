from PySide6 import QtWidgets, QtCore

from wom.GUI.PY.common import Discharge_details
from wom.app_logic.service_func import create_mkb_nmu_dict, add_mkb10_nmu
from wom.app_logic.writing.postprocessing\
    .passport import update_patient_info
from wom.app_logic.writing.postprocessing\
    .dis_details import update_after_dis_details
from wom.app_logic.writing.postprocessing import scale_description
from wom.app_logic.db_func\
    .bucket_func import upload_history_to_yandex_cloud_bucket
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta

from wom.settings.config import (
    bed_profiles,
    doc_dict,
    head_department,
    head_department_bta,
)


class Ui_Discharge_details(QtWidgets.QWidget,
                           Discharge_details.Ui_Dis_details):
    def __init__(self, user_info, windows, main_win, dictionary, case_type):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.case_type = case_type

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Данные для выписки"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.add_values_to_popup_lists()
        self.set_patient_info()
        self.insert_data_from_dictionary()
        self.set_styles()

    def onButtonMy(self):
        pass

    def add_values_to_popup_lists(self):
        self.mkb10, self.nmu = create_mkb_nmu_dict()
        # добавление значений в выплывающие списки
        self.comboBoxPtMKB10_main.clear()
        self.comboBoxPtMKB10_main.addItems(list(self.mkb10))
        self.comboBoxPtNMU_code.clear()
        self.comboBoxPtNMU_code.addItems(list(self.nmu))

        self.comboBoxTherapist.clear()
        self.comboBoxTherapist.addItems(list(doc_dict.keys()))

        self.comboBox_department_head.clear()
        if self.case_type == 'bta':
            self.comboBox_department_head.addItems(head_department_bta)
        else:
            self.comboBox_department_head.addItems(head_department)

        self.comboBox_bedprofile.clear()
        self.comboBox_bedprofile.addItems(bed_profiles)

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonNotSaveExit.clicked\
            .connect(self.exit)
        self.pushButtonSaveExit.clicked\
            .connect(self.exit_and_save)
        self.pushButtonDischarge_and_close_history.clicked\
            .connect(self.close_history)
        self.comboBoxPtMKB10_main.currentTextChanged\
            .connect(self.change_mkb_label)
        self.comboBoxPtNMU_code.currentTextChanged\
            .connect(self.change_nmu_label)

    def change_mkb_label(self):
        try:
            self.label_mkb.setText(
                self.mkb10[self.comboBoxPtMKB10_main.currentText()])
        except KeyError:
            self.label_mkb.setText('Не найден такой код МКБ-10')

    def change_nmu_label(self):
        try:
            self.label_nmu.setText(
                self.nmu[self.comboBoxPtNMU_code.currentText()])
        except KeyError:
            self.label_nmu.setText('Не найден такой код НМУ')

    def insert_data_from_dictionary(self):
        self.dateEditDischargeDate\
            .setDate(QtCore.QDate.fromString(
                self.d['дата_выписки_план'], "dd.MM.yyyy"))
        self.dateEditDischargeDate_plan\
            .setDate(QtCore.QDate.fromString(
                self.d['дата_выписки_план'], "dd.MM.yyyy"))
        self.comboBoxPtMKB10_main\
            .setCurrentText(self.d['МКБ'])
        self.comboBoxPtNMU_code\
            .setCurrentText(self.d['услуга'])
        self.dateEditPtAdmissionDay\
            .setDate(QtCore.QDate.fromString(
                self.d['дата_поступления'], "dd.MM.yyyy"))
        self.timeEditPtAdmissionTime\
            .setTime(QtCore.QTime.fromString(
                self.d['время_поступления'], "hh:mm"))
        self.comboBoxPtHoptitalisationType\
            .setCurrentText(self.d['тип_стационара'])
        self.comboBoxTherapist\
            .setCurrentText(self.d['ФИО_врача'])
        self.lineEdit_history_number\
            .setText(self.d['номер_истории'])
        self.comboBox_department_head\
            .setCurrentText(self.d['зав_отделением'])
        self.comboBox_referring_health_facility\
            .setCurrentText(self.d['ЛПУ_кто_направил'])
        self.comboBox_bedprofile\
            .setCurrentText(self.d.get('профиль_коек'))
        self.lineEdit_room_number\
            .setText(self.d['палата'])
        # время выписки по умолчанию
        if self.case_type == 'bta' and \
            self.d['тип_стационара'] in ('БТ - дневной',
                                         'Дневной стационар'):
            time_default = "16:00"
        else:
            time_default = "10:00"
        self.timeEditDischargeTime\
            .setTime(QtCore.QTime.fromString(time_default, "hh:mm"))

        if 'вид_выбытия' in self.d:
            self.dateEditDischargeDate\
                .setDate(QtCore.QDate.fromString(
                    self.d['дата_выписки'], "dd.MM.yyyy"))
            self.timeEditDischargeTime\
                .setTime(QtCore.QTime.fromString(
                    self.d['время_выписки'], "hh:mm"))
            self.comboBoxDischargeData_1\
                .setCurrentText(self.d['вид_выбытия'])
            self.comboBoxDischargeData_2\
                .setCurrentText(self.d['характер_выписки'])
            self.comboBoxDischargeData_3\
                .setCurrentText(self.d['итог_выписки'])

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def write_to_dictionary(self):
        '''
        перезапись в словаре всех значений из виджетов на новые
        '''
        self.d['дата_выписки_план'] = \
            self.dateEditDischargeDate_plan.dateTime().toString('dd.MM.yyyy')
        self.d['дата_выписки'] = \
            self.dateEditDischargeDate.dateTime().toString('dd.MM.yyyy')
        self.d['время_выписки'] = \
            self.timeEditDischargeTime.dateTime().toString('hh:mm')
        self.d['МКБ'] = \
            self.comboBoxPtMKB10_main.currentText()
        self.d['услуга'] = \
            self.comboBoxPtNMU_code.currentText()
        self.d['вид_выбытия'] = \
            self.comboBoxDischargeData_1.currentText()
        self.d['характер_выписки'] = \
            self.comboBoxDischargeData_2.currentText()
        self.d['итог_выписки'] = \
            self.comboBoxDischargeData_3.currentText()
        self.d['дата_поступления'] = \
            self.dateEditPtAdmissionDay.dateTime().toString('dd.MM.yyyy')
        self.d['время_поступления'] = \
            self.timeEditPtAdmissionTime.dateTime().toString('hh:mm')
        self.d['тип_стационара'] = \
            self.comboBoxPtHoptitalisationType.currentText()
        self.d['ФИО_врача'] = \
            self.comboBoxTherapist.currentText()
        self.d['номер_истории'] = \
            self.lineEdit_history_number.text()
        self.d['зав_отделением'] = \
            self.comboBox_department_head.currentText()
        self.d['ЛПУ_кто_направил'] = \
            self.comboBox_referring_health_facility.currentText()
        self.d['профиль_коек'] = \
            self.comboBox_bedprofile.currentText()
        self.d['палата'] = \
            self.lineEdit_room_number.text()
        add_mkb10_nmu(self.d)
        update_patient_info(self.d)
        update_after_dis_details(self.d)
        scale_description.update(self.d)

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

    def open_main_menu(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows[self.case_type]['main_menu'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def exit_and_save(self):
        self.save_history()
        self.open_patient_card()

    def exit(self):
        self.open_patient_card()

    def save_history(self):
        self.write_to_dictionary()
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

    def close_history(self):
        if self.checkBox_dis.isChecked():
            self.d['status_act'] = False  # свидетельство, что пациент выписан
            # записываем новые данные в словарь
            self.save_history()
            self.open_main_menu()
        else:
            pass

    def set_styles(self):
        pass
