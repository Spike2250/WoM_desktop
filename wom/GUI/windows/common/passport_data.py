from PySide6 import QtWidgets, QtCore

from wom.GUI.PY.common import PatientPassportData
from wom.app_logic.create_docs import (creating_documents,
                                       open_folder_with_files)
from wom.app_logic.db_func\
    .bucket_func import upload_history_to_yandex_cloud_bucket
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.writing.postprocessing\
    .passport import update_after_passport_data


# Окно паспортных данных пациента
class Ui_PatientPassportData(QtWidgets.QWidget,
                             PatientPassportData.Ui_PatientPassportData):
    def __init__(self, user_info, windows, main_win, dictionary, case_type):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.case_type = case_type

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Паспортные данные пациента"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.insert_data_from_dictionary()
        self.set_styles()

    def onButtonMy(self):
        pass

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonPrintConsent.clicked.connect(self.create_consent)
        self.pushButtonAddRelative.clicked.connect(self.add_patient_relative)
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)

    def insert_data_from_dictionary(self):
        self.surname.setText(self.d['фамилия'])
        self.name.setText(self.d['имя'])
        self.dadname.setText(self.d['отчество'])
        self.adress.setText(self.d['адрес'])
        self.phone.setText(self.d['телефон'])
        self.email.setText(self.d['электронная_почта'])
        self.passport.setText(self.d['паспорт'])
        self.polis_oms.setText(self.d['полис_ОМС'])
        self.snils.setText(self.d['СНИЛС'])
        self.dateEdit_birthday.setDate(QtCore.QDate.fromString(
            self.d['дата_рождения'], "dd.MM.yyyy"))
        self.comboBox_gender.setCurrentText(self.d['пол'])
        self.checkBox_signature_cant.setChecked(
            self.d.get('не_может_подписаться', False))
        if self.d.get('Правша', True):
            self.checkBoxPtLeftHanded.setChecked(False)  # инверсия
        else:
            self.checkBoxPtLeftHanded.setChecked(True)  # инверсия
        update_after_passport_data(self.d)

    # функции для кнопок
    def create_consent(self):
        '''
        функция создает и открывает файл (.docx)
            с различными согласиями пациента
            с возможностью их редактирования
            и вывода на печать

        '''
        self.write_to_dictionary()

        self.templates_consent = ['Согласие_перс_данные',
                                  'Согласие',
                                  'Уведомление']

        self.templates_consent_bta = ['Согласие_перс_данные',
                                      'Согласие',
                                      'Уведомление',
                                      'Согласие_БТА']

        if self.case_type == 'bta':
            creating_documents(self.d, self.templates_consent_bta)
        else:
            creating_documents(self.d, self.templates_consent)

        open_folder_with_files(self.d)

    def write_to_dictionary(self):
        '''
        перезапись в словаре всех значений из виджетов на новые
        '''
        self.d['фамилия'] = self.surname.text()
        self.d['имя'] = self.name.text()
        self.d['отчество'] = self.dadname.text()
        self.d['адрес'] = self.adress.text()
        self.d['телефон'] = self.phone.text()
        self.d['электронная_почта'] = self.email.text()
        self.d['паспорт'] = self.passport.text()
        self.d['полис_ОМС'] = self.polis_oms.text()
        self.d['СНИЛС'] = self.snils.text()
        self.d['дата_рождения'] = self.dateEdit_birthday\
            .dateTime().toString('dd.MM.yyyy')
        self.d['пол'] = self.comboBox_gender.currentText()
        self.d['не_может_подписаться'] = self\
            .checkBox_signature_cant.isChecked()
        if self.checkBoxPtLeftHanded.isChecked():
            self.d['Правша'] = False  # инверсия
        else:
            self.d['Правша'] = True

    def set_styles(self):
        pass

    def open_window(self, name):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['common'][name](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win,
                dictionary=self.d,
                case_type=self.case_type))
        win.show()

    def add_patient_relative(self):
        self.write_to_dictionary()
        self.open_window('add_relative')
        self.main_win.close()

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
