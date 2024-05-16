from PySide6 import QtWidgets, QtCore
from datetime import timedelta, datetime
from wom.GUI.PY.bta import bta_AddNewPatient
from wom.app_logic.service_func import (datedif, convert_date as c_date,
                                        create_mkb_nmu_dict, add_mkb10_nmu)
from wom.app_logic.db_func.db_bta import (read_d_from_db_bta,
                                          read_db_active_cases_bta,
                                          read_db_archive_cases_bta,
                                          write_all_data_to_db_bta,
                                          write_fullness_table_bta)
from wom.app_logic.create_docs import (creating_documents,
                                       open_folder_with_files)
from wom.app_logic.parsing import parse_promed
from wom.app_logic.writing.postprocessing.passport import update_after_passport_data  # noqa: E501

from wom.settings.dep_bta import doc_dict, head_department, bed_profiles


class Ui_AddNewPatient(QtWidgets.QWidget,
                       bta_AddNewPatient.Ui_AddCase):
    def __init__(self, user_info, windows, main_win, dictionary):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.d = dictionary
        self.user_info = user_info
        self.main_win = main_win

        msg = "World of Medicine - Кабинет ботулинотерапевта "\
              "- Добавление нового пациента"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.add_values_to_popup_lists()
        self.tricks()
        self.show_uin_label()

    def onButtonMy(self):
        # self.textEdit.append("Нажата `Своя Кнопка`!")
        pass

    def open_patient_card(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['bta']['patient_card'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win,
                dictionary=self.d))
        win.show()
        self.main_win.close()

    def back_to_main_menu(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['bta']['main_menu'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def open_load_arch(self, histories, case_type):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['common']['load_arch'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win,
                dictionary=self.d,
                histories=histories,
                case_type=case_type))
        win.show()
        self.main_win.close()

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonCreateHistory.clicked.connect(self.create_history)
        self.pushButtonPrintConsent.clicked.connect(self.create_consent)
        self.pushButton_add_from_promed.clicked.connect(self.parse_promed_data)
        self.pushButtonBackToMenu.clicked.connect(self.back_to_main_menu)
        self.pushButton_today.clicked.connect(self.set_adm_date_today)
        self.pushButton_yesterday.clicked.connect(self.set_adm_date_yesterday)
        #
        self.checkBoxPtNeedSickList.stateChanged.connect(self.activate_first_ln_box)  # noqa: E501

    def activate_first_ln_box(self):
        if self.checkBoxPtNeedSickList.isChecked():
            self.checkBoxPtNeedSickList_2.setEnabled(True)
        else:
            self.checkBoxPtNeedSickList_2.setChecked(False)
            self.checkBoxPtNeedSickList_2.setEnabled(False)

    def add_values_to_popup_lists(self):
        # загружаем словари МКБ10 и НМУ
        self.mkb10, self.nmu = create_mkb_nmu_dict()
        # добавление значений в выплывающие списки
        self.comboBox_mkb.clear()
        self.comboBox_mkb.addItems(list(self.mkb10))
        self.comboBox_nmu.clear()
        self.comboBox_nmu.addItems(list(self.nmu))

        self.comboBox_bedprofile.clear()
        self.comboBox_bedprofile.addItems(bed_profiles)

        self.comboBox_therapist.clear()
        self.comboBox_therapist.addItems(list(doc_dict.keys()))

        self.comboBox_department_head.clear()
        self.comboBox_department_head.addItems(head_department)

    def tricks(self):
        # автозаполнение
        self.dateEdit_adm_date.dateChanged.connect(
            self.change_DischargeDate_plan)
        self.dateEdit_adm_date.dateChanged.connect(
            self.change_dis_info)
        self.comboBox_mkb.currentTextChanged.connect(
            self.change_nmu)
        self.comboBox_mkb.currentTextChanged.connect(
            self.change_mkb_desc)
        self.comboBox_nmu.currentTextChanged.connect(
            self.change_nmu_desc)
        self.dateEdit_dis_date_plan.dateChanged.connect(
            self.change_dis_info)

    def set_adm_date_today(self):
        today = datetime.now().strftime('%d.%m.%Y')
        self.dateEdit_adm_date.setDate(
            QtCore.QDate.fromString(today, "dd.MM.yyyy"))

    def set_adm_date_yesterday(self):
        yesterday = (datetime.now() - timedelta(1)).strftime('%d.%m.%Y')
        self.dateEdit_adm_date.setDate(
            QtCore.QDate.fromString(yesterday, "dd.MM.yyyy"))

    def change_dis_info(self):
        adm_date = self.dateEdit_adm_date.dateTime().toString('dd.MM.yyyy')
        dis_date = self.dateEdit_dis_date_plan.dateTime().toString('dd.MM.yyyy')  # noqa: E501
        typeHosp = self.comboBox_hospit_type.currentText()

        if typeHosp in {'Круглосуточный стационар', 'БТ - круглосуточный'}:
            bed_days = datedif(adm_date, dis_date) - 1
        else:
            bed_days = datedif(adm_date, dis_date)
        dis_date = c_date(dis_date)

        text = f'   {dis_date.strftime("%A")} \t({bed_days} к/д)'
        self.label_discharge_info.setText(text)

    def show_uin_label(self):
        # написание UIN
        uin = f"Клиническому случаю будет присвоен "\
              f"UIN: {self.d['unic_number']}"
        self.label_unic_number.setText(uin)

    def change_nmu(self):
        '''
        '''
        mkb10_code = self.comboBox_mkb.currentText()

        if mkb10_code in {'I69.0', 'I69.1',
                          'I69.2', 'I69.3',
                          'I69.4', 'I69.8',
                          'I69.9'}:
            self.comboBox_nmu.setCurrentText('B05.023.001')
        elif mkb10_code in {'M51.1', 'M51.0',
                            'M50.1', 'M50.0'}:
            self.comboBox_nmu.setCurrentText('B05.024.002')
        elif mkb10_code in {'U09.9'}:
            self.comboBox_nmu.setCurrentText('B05.070.001.011')
        elif mkb10_code in {'T91.3', 'T91.1'}:
            self.comboBox_nmu.setCurrentText('B05.024.001')
        elif mkb10_code in {'T90.5'}:
            self.comboBox_nmu.setCurrentText('B05.024.003')
        elif mkb10_code in {'G81.1', 'G82.1',
                            'G82.4'}:
            self.comboBox_nmu.setCurrentText('A25.24.001.002')
        elif mkb10_code in {'G61.0', 'G20'}:
            self.comboBox_nmu.setCurrentText('B05.023.002.002')
        elif mkb10_code in {'M24.5'}:
            self.comboBox_nmu.setCurrentText('B05.050.005')

    def change_DischargeDate_plan(self):
        '''
        '''
        hospit_type = self.comboBox_hospit_type.currentText()
        day_adm = c_date(
            self.dateEdit_adm_date.dateTime().toString('dd.MM.yyyy'))

        if hospit_type == 'БТ - круглосуточный':
            discharge_date_plan = day_adm + timedelta(1)
        else:
            discharge_date_plan = day_adm
        self.dateEdit_dis_date_plan.setDate(QtCore.QDate.fromString(
            discharge_date_plan.strftime('%d.%m.%Y'), "dd.MM.yyyy"))

    def change_mkb_desc(self):
        cbox_text = self.comboBox_mkb.currentText()
        if (cur_text := self.plainTextEdit_descriptions.toPlainText()) != '':
            cur_nmu = cur_text.split('\n')[1]
            self.plainTextEdit_descriptions.toPlainText()
            try:
                text = f'МКБ-10: {cbox_text} - '\
                       f'{self.mkb10[f"{cbox_text}"]}'\
                       f'\n{cur_nmu}'
                self.plainTextEdit_descriptions.setPlainText(text)
            except KeyError:
                text = f'МКБ-10: не определен'\
                       f'\n{cur_nmu}'
                self.plainTextEdit_descriptions.setPlainText(text)
        else:
            try:
                text = f'МКБ-10: {cbox_text} - {self.mkb10[f"{cbox_text}"]}\n'
                self.plainTextEdit_descriptions.setPlainText(text)
            except KeyError:
                text = f'МКБ-10: не определен\n'
                self.plainTextEdit_descriptions.setPlainText(text)

    def change_nmu_desc(self):
        cbox_text = self.comboBox_nmu.currentText()
        if (cur_text := self.plainTextEdit_descriptions.toPlainText()) != '':
            cur_mkb10 = cur_text.split('\n')[0]
            self.plainTextEdit_descriptions.toPlainText()
            try:
                text = f'{cur_mkb10}\n'\
                       f'НМУ: {cbox_text} - '\
                       f'{self.nmu[f"{cbox_text}"]}'
                self.plainTextEdit_descriptions.setPlainText(text)
            except KeyError:
                text = f'{cur_mkb10}\n'\
                       f'НМУ: не определен'
                self.plainTextEdit_descriptions.setPlainText(text)
        else:
            try:
                text = f'\nНМУ: {cbox_text} - {self.nmu[f"{cbox_text}"]}'
                self.plainTextEdit_descriptions.setPlainText(text)
            except KeyError:
                text = f'\nНМУ: не определен'
                self.plainTextEdit_descriptions.setPlainText(text)

    def create_consent(self):
        self.write_to_dictionary()
        creating_documents(self.d, ['Согласия'])
        open_folder_with_files(self.d)

    def save_history(self):
        # записываем словарь в json-файл и обновляем БД
        write_all_data_to_db_bta(self.d)
        write_fullness_table_bta(self.d)

    def write_to_dictionary(self):
        self.d['status_act'] = True  # Статус пациента
        # создаем чек-лайн для БД наполненности
        self.d['check_line'] = '1000000'

        # записываем остальные данные
        # lineEdit's
        self.d['фамилия'] = self.surname.text()
        self.d['имя'] = self.name.text()
        self.d['отчество'] = self.dadname.text()
        self.d['адрес'] = self.adress.text()
        self.d['телефон'] = self.phone.text()
        self.d['электронная_почта'] = self.email.text()
        self.d['паспорт'] = self.passport.text()
        self.d['полис_ОМС'] = self.polis_oms.text()
        self.d['СНИЛС'] = self.snils.text()
        self.d['номер_истории'] = self.history_number.text()
        self.d['палата'] = self.room_number.text()
        # comboBox's
        self.d['профиль_коек'] = self.comboBox_bedprofile.currentText()
        self.d['препарат_БТА'] = self.comboBox_bta_preparat.currentText()
        self.d['тип_стационара'] = self.comboBox_hospit_type.currentText()
        self.d['МКБ'] = self.comboBox_mkb.currentText()
        self.d['услуга'] = self.comboBox_nmu.currentText()
        self.d['ЛПУ_кто_направил'] = self.comboBox_referring_health_facility.currentText()  # noqa: E501
        self.d['пол'] = self.comboBox_gender.currentText()
        self.d['ФИО_врача'] = self.comboBox_therapist.currentText()
        self.d['зав_отделением'] = self.comboBox_department_head.currentText()
        # dateEdit's
        self.d['дата_поступления'] = self.dateEdit_adm_date.dateTime().toString('dd.MM.yyyy')  # noqa: E501
        self.d['дата_выписки_план'] = self.dateEdit_dis_date_plan.dateTime().toString('dd.MM.yyyy')  # noqa: E501
        self.d['дата_рождения'] = self.dateEdit_birthday.dateTime().toString('dd.MM.yyyy')  # noqa: E501
        # timeEdit's
        self.d['время_поступления'] = self.timeEdit_adm_time.dateTime().toString('hh:mm')  # noqa: E501
        # checkBox's
        self.d['нужда_в_ЛН'] = self.checkBoxPtNeedSickList.isChecked()
        self.d['нужда_в_ЛН_первич'] = self.checkBoxPtNeedSickList_2.isChecked()
        self.d['не_может_подписаться'] = self.checkBox_signature_cant.isChecked()  # noqa: E501

        # добавление надписей, при невозможнссти пациента поставить подпись
        if self.d['не_может_подписаться']:
            self.d['нмпп'] = 'не может подписаться'
            self.d['нмпп_дата_поступления'] = self.d['дата_поступления']
            self.d['нмпп_дата_выписки'] = self.d['дата_выписки_план']
            self.d['нмпп_ФИО_врача'] = self.d['ФИО_врача']
            self.d['нмпп_зав_отделением'] = self.d['зав_отделением']

        add_mkb10_nmu(self.d)

        update_after_passport_data(self.d)

    def check_not_empty(self):
        main_data_list = [
            self.lineEditPtSurName.text(),
            self.lineEditPtName.text(),
            self.lineEditPtDadName.text(),
            self.dateEditPtBirthDay.dateTime().toString('dd.MM.yyyy'),
            self.dateEditPtAdmissionDay.dateTime().toString('dd.MM.yyyy'),
            self.timeEditPtAdmissionTime.dateTime().toString('hh:mm'),
            self.comboBoxPtRoomNumber.currentText(),
        ]
        check_list_empty = []

        for i in main_data_list:
            if i in ('', '01.01.2000', '00:00'):
                check_list_empty.append(False)
            else:
                check_list_empty.append(True)

        return check_list_empty

    def check_unique_person(self):
        active_data = read_db_active_cases_bta()
        archive_data = read_db_archive_cases_bta()

        try_d = {
            'фамилия': self.surname.text(),
            'имя': self.name.text(),
            'отчество': self.dadname.text(),
        }

        fullname = f"{try_d['фамилия']} {try_d['имя']} {try_d['отчество']}"
        birthday = self.dateEdit_birthday.dateTime().toString('dd.MM.yyyy')

        for case in active_data:
            if case['fullname'] == fullname:
                # получаем uin
                uin = case['case_id']
                # записываем словарь из БД в словарь
                archive_d = read_d_from_db_bta(uin)
                if birthday == archive_d['дата_рождения']:
                    text = f'В активных случаях уже есть '\
                           f'идентичный пациент! '\
                           f'Добавление истории болезни отменено!'
                    return text
        for case in archive_data:
            if case['fullname'] == fullname:
                # получаем uin
                uin = case['case_id']
                # записываем словарь из БД в словарь
                archive_d = read_d_from_db_bta(uin)
                if birthday == archive_d['дата_рождения']:
                    return uin  # Для использования истории как новой основы
        return True

    def create_history(self):
        uin = self.check_unique_person()
        # если пациент уникальный
        if uin is True:
            # проверяем что данные заполнены
            if all((self.check_not_empty())):
                # записываем новые данные в словарь
                self.write_to_dictionary()
                # загружаем в бакет YandexCloud
                self.save_history()
                # открываем карту пациента
                self.open_patient_card()
            else:
                text = f'      Данные заполнены не полном объеме!\n'\
                       f'Создание истории болезни отменено!\n'\
                       f'Поля фамилия, имя, отчество, дата рождения, '\
                       f'дата поступления, время поступления и '\
                       f'номер палаты не должны быть пустыми!'
                self.plainTextEdit_descriptions_promed.setPlainText(text)
        # если вернули список uin
        elif isinstance(uin, list):
            histories = []
            for i in uin:
                # считываем архивные истории
                histories.append(read_d_from_db_bta(i))
            # записываем новые данные в словарь
            self.write_to_dictionary()
            self.open_load_arch(histories, 'omr')
        # если такая история уже есть в активных
        elif isinstance(uin, str):
            # очищаем все поля
            # lineEdit's
            self.surname.setText('')
            self.name.setText('')
            self.dadname.setText('')
            self.adress.setText('')
            self.phone.setText('')
            self.email.setText('')
            self.passport.setText('')
            self.polis_oms.setText('')
            self.snils.setText('')
            self.history_number.setText('')
            self.room_number.setText('')
            # comboBox's
            self.comboBox_bta_preparat.setCurrentText('')
            self.comboBox_hospit_type.setCurrentText('')
            self.comboBox_mkb.setCurrentText('')
            self.comboBox_nmu.setCurrentText('')
            self.comboBox_referring_health_facility.setCurrentText('')
            self.comboBox_gender.setCurrentText('')
            self.comboBox_therapist.setCurrentText('')
            self.comboBox_department_head.setCurrentText('')
            # dateEdit's
            self.dateEdit_adm_date.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            self.dateEdit_dis_date_plan.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            self.dateEdit_birthday.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            # timeEdit's
            self.timeEdit_adm_time.setTime(
                QtCore.QTime.fromString("00:00", "hh:mm"))
            # checkBox's
            self.checkBoxPtNeedSickList.setChecked(False)
            self.checkBoxPtNeedSickList_2.setChecked(False)
            self.checkBox_signature_cant.setChecked(False)

            # выводим сообщение об отмене добавления истории
            # style = "QPlainTextEdit {font-family: Roboto;font-size: 15px;background-color:#AF830B;}"  # noqa: E501
            # self.plainTextEdit_descriptions.setStyleSheet(style)
            self.plainTextEdit_descriptions.setPlainText(f"{uin}\n")

    def parse_promed_data(self):
        if (x := self.plainTextEdit_promed_data.toPlainText()) != '':
            try:
                promed_data = parse_promed(x)
                self.surname.setText(promed_data['surname'])
                self.name.setText(promed_data['name'])
                self.dadname.setText(promed_data['dadname'])
                self.dateEdit_birthday.setDate(QtCore.QDate.fromString(
                    promed_data['birthday'], "dd.MM.yyyy"))
                self.adress.setText(promed_data['adress'])
                self.phone.setText(promed_data['phone_number'])
                self.passport.setText(promed_data['passport'])
                self.polis_oms.setText(promed_data['oms_polis'])
                self.snils.setText(promed_data['snils'])
                self.comboBox_gender.setCurrentText(promed_data['sex'])
                msg = f"Парсинг прошел успешно! :)"
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
            except IndexError:
                msg = f"Вводимая строка НЕ соответствует\n"\
                      f"формату ЕИСЗ ПК (Промед) и\n"\
                      f"непригодна для парсинга"
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
                self.plainTextEdit_promed_data.setPlainText('')
            except UnboundLocalError:
                msg = f"Вводимая строка НЕ соответствует\n"\
                      f"формату ЕИСЗ ПК (Промед) и\n"\
                      f"непригодна для парсинга"
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
                self.plainTextEdit_promed_data.setPlainText('')
        else:
            msg = f"Строка пуста!\nПарсинг не возможен!"
            self.plainTextEdit_descriptions_promed.setPlainText(msg)
