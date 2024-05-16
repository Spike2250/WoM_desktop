from PySide6 import QtWidgets
import ast
from wom.GUI.PY.bta import bta_PatientCard
from wom.app_logic.writing.postprocessing.passport import (list_created_docs,
                                                           update_patient_info)
from wom.app_logic.create_docs import (creating_documents,
                                       open_folder_with_files)
from wom.app_logic.worklist_data_processing import refresh_worklist_data
from wom.app_logic.db_func.db_bta import (write_all_data_to_db_bta,
                                          write_fullness_table_bta)
from wom.app_logic.writing.diaries.bta import add_diaries_for_bta
from wom.styles_qss.main_styles import (
    style_true_button,
    label_style_act,
    label_style_dis,
)


class Ui_PatientCard(QtWidgets.QWidget,
                     bta_PatientCard.Ui_PatientCard):
    def __init__(self, user_info, windows, main_win, dictionary):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.d = dictionary
        self.user_info = user_info
        self.main_win = main_win

        msg = "World of Medicine - Кабинет ботулинотерапевта "\
              "- Медицинская карта пациента"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.update_descriptions()

        self.check_data_label()

        self.check_data_blocks()
        self.check_created_docs()

        # проверяем возможности словаря
        # - полноту для создания документов
        self.check_possible()

    def onButtonMy(self):
        # self.textEdit.append("Нажата `Своя Кнопка`!")
        pass

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonOpenPtPassportData.clicked.connect(self.open_passport_data)  # noqa: E501
        self.pushButtonOpenPtObjStatus.clicked.connect(self.open_obj_status)
        self.pushButtonOpenPtNeuralStatus.clicked.connect(self.open_neural_status)  # noqa: E501
        self.pushButtonOpenPtDiagnosis.clicked.connect(self.open_diagnosis)
        self.pushButtonOpen_bta_protocol.clicked.connect(self.open_protocol_bta)  # noqa: E501
        self.pushButtonOpen_discharge_data.clicked.connect(self.open_discharge_details)  # noqa: E501
        self.pushButtonOpen_recommends.clicked.connect(self.open_recommends)
        self.pushButtonCreateDocument.clicked.connect(self.create_docs)
        self.pushButtonSaveExit.clicked.connect(self.save_and_close_card)
        self.pushButtonNotSaveExit.clicked.connect(self.close_card)
        self.pushButtonSave.clicked.connect(self.save_history)
        self.pushButton_clean_ticks.clicked.connect(self.clean_ticks)
        self.pushButtonOpenFolder.clicked.connect(self.open_folder)
        self.pushButtonHelp.clicked.connect(self.open_help)
        self.pushButton_2.clicked.connect(self.print_keys_from_d)

    def update_descriptions(self):
        # обновляем "Лого_ИБ" и "patient_info"
        update_patient_info(self.d)
        # меняем подпись истории болезни данными из словаря
        self.ptFullNameCard.setText(self.d['Лого_ИБ'])
        self.label_unic_number.setText(self.d['unic_number'])
        # меняем надпись стационара
        if (x := self.d['тип_стационара']) == 'БТ - круглосуточный':
            h_type = 'Круглосуточный стационар'
        elif x == 'БТ - дневной':
            h_type = 'Дневной стационар'
        self.label_type_hospitalisation.setText(h_type)

    def check_data_label(self):
        # обозначаем в истории, если пациент выписан
        if self.d['status_act']:
            text = f"Активный случай"
            self.label_dis_check.setText(text)
            self.label_dis_check.setStyleSheet(label_style_act)
        else:
            text = f"Пациент выписан {self.d['дата_выписки']}.\n"\
                   f"История находится в архиве."
            self.label_dis_check.setText(text)
            self.label_dis_check.setStyleSheet(label_style_dis)

    def create_main_window(self):
        return self.windows['Frameless']()

    def create_window(self, main_win, folder_name, win_name, timeline):
        if folder_name == 'common':
            if timeline is not None:
                w = self.windows[folder_name][win_name](
                    user_info=self.user_info,
                    windows=self.windows,
                    main_win=main_win,
                    dictionary=self.d,
                    case_type='bta',
                    timeline=timeline)
            else:
                w = self.windows[folder_name][win_name](
                    user_info=self.user_info,
                    windows=self.windows,
                    main_win=main_win,
                    dictionary=self.d,
                    case_type='bta')
        elif folder_name == 'bta':
            if timeline is not None:
                w = self.windows[folder_name][win_name](
                    user_info=self.user_info,
                    windows=self.windows,
                    main_win=main_win,
                    dictionary=self.d,
                    timeline=timeline)
            else:
                w = self.windows[folder_name][win_name](
                    user_info=self.user_info,
                    windows=self.windows,
                    main_win=main_win,
                    dictionary=self.d)
        return w

    def close_card(self):
        win = self.create_main_window()
        win.setWidget(
            self.windows['bta']['main_menu'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def open_window(self, folder_name, win_name, timeline=None):
        win = self.create_main_window()
        win.setWidget(self.create_window(win, folder_name, win_name, timeline))
        win.show()
        self.main_win.close()

    def open_passport_data(self):
        self.open_window(folder_name='common',
                         win_name='passport')

    def open_obj_status(self):
        self.open_window(folder_name='common',
                         win_name='obj_status_adm')

    def open_neural_status(self):
        self.open_window(folder_name='common',
                         win_name='neur_status',
                         timeline='adm')

    def open_diagnosis(self):
        self.open_window(folder_name='common',
                         win_name='diagnosis',
                         timeline='adm')

    def open_discharge_details(self):
        self.open_window(folder_name='common',
                         win_name='dis_details')

    def open_protocol_bta(self):
        win = self.create_main_window()
        win.setWidget(
            self.windows['bta']['protocol'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win,
                dictionary=self.d))
        win.show()
        self.main_win.close()

    def open_recommends(self):
        # self.w = self.windows['bta']['recommeds'](self.windows, self.d)
        # self.w.show()
        # self.hide()
        status_message = f'Раздел "Рекомендации для выписки" '\
                         f'находится в разработке. '
        self.label_status.setText(status_message)

    def open_help(self):
        pass

    def clean_ticks(self):
        '''снятие всех галочек для создания документов'''
        self.checkBox_doc_consents.setChecked(False)
        self.checkBox_doc_consent_bta.setChecked(False)
        self.checkBox_doc_initial_inspection.setChecked(False)
        self.checkBox_doc_appointments.setChecked(False)
        self.checkBox_doc_protocol_bta.setChecked(False)
        self.checkBox_doc_med_commission_bta.setChecked(False)
        self.checkBox_doc_statistic_talon_face.setChecked(False)
        self.checkBox_doc_statistic_talon.setChecked(False)
        self.checkBox_doc_statistic_talon_other.setChecked(False)
        self.checkBox_doc_med_commission_1.setChecked(False)
        self.checkBox_doc_med_commission_drugs.setChecked(False)
        self.checkBox_doc_frontpage.setChecked(False)
        self.checkBox_doc_back_frontpage.setChecked(False)
        self.checkBox_doc_discharge_summary.setChecked(False)
        self.checkBox_doc_refusal.setChecked(False)
        self.checkBox_doc_full_history.setChecked(False)
        self.checkBox_complex.setChecked(False)

    def check_possible(self):
        '''
        self.check_list[0] - 'ФИО_пациента'
        self.check_list[1] - 'Соматический_статус'
        self.check_list[2] - 'Неврологический_статус'
        self.check_list[3] - 'Основной_диагноз'
        self.check_list[4] - 'БТА_мышцы_мишени'
        self.check_list[5] - 'вид_выбытия'
        self.check_list[6] - 'рекомендации_выписка'
        '''
        # Выключаем все чек-боксы
        self.checkBox_doc_consents.setEnabled(False)
        self.checkBox_doc_consent_bta.setEnabled(False)
        self.checkBox_doc_initial_inspection.setEnabled(False)
        self.checkBox_doc_protocol_bta.setEnabled(False)
        self.checkBox_doc_med_commission_bta.setEnabled(False)
        self.checkBox_doc_statistic_talon_face.setEnabled(False)
        self.checkBox_doc_statistic_talon.setEnabled(False)
        self.checkBox_doc_statistic_talon_other.setEnabled(False)
        self.checkBox_doc_frontpage.setEnabled(False)
        self.checkBox_doc_back_frontpage.setEnabled(False)
        self.checkBox_doc_discharge_summary.setEnabled(False)
        self.checkBox_doc_refusal.setEnabled(False)
        self.checkBox_doc_check_list.setEnabled(False)
        self.checkBox_doc_appointments.setEnabled(False)
        self.checkBox_doc_med_commission_1.setEnabled(False)
        self.checkBox_doc_med_commission_drugs.setEnabled(False)
        self.checkBox_doc_full_history.setEnabled(False)
        self.checkBox_complex.setEnabled(False)

        # Проводим проверки для выборочного включения чек-боксов
        # в зависимости от полноты заполнения ИБ

        # Согласия, чек-лист, обложка, 1стр.стат.талона, ВК на препарат
        if self.check_list[0]:
            self.checkBox_doc_consents.setEnabled(True)
            self.checkBox_doc_consent_bta.setEnabled(True)
            self.checkBox_doc_check_list.setEnabled(True)
            # self.checkBox_doc_frontpage.setEnabled(True)
            # self.checkBox_doc_statistic_talon_face.setEnabled(True)
            # self.checkBox_doc_med_commission_drugs.setEnabled(True)

        # Первичный осмотр
        if all((self.check_list[0],
                self.check_list[1],
                self.check_list[2],
                self.check_list[3])):
            self.checkBox_doc_initial_inspection.setEnabled(True)
            # ВК по продлению ЛН
            if self.d['нужда_в_ЛН']:
                self.checkBox_doc_med_commission_1.setEnabled(True)

        # Лист назначений, протокол БТ, ВК для БТА
        if all((self.check_list[0],
                self.check_list[4])):
            self.checkBox_doc_appointments.setEnabled(True)
            self.checkBox_doc_protocol_bta.setEnabled(True)
            self.checkBox_doc_med_commission_bta.setEnabled(True)

        # Стат.талон 2 стр
        if all((self.check_list[0],
                self.check_list[5])):
            self.checkBox_doc_statistic_talon.setEnabled(True)
            # Дополнение к стат.талону, оборот обложки, отказ от госпитализации
            if self.check_list[3]:
                self.checkBox_doc_statistic_talon_other.setEnabled(True)
                self.checkBox_doc_back_frontpage.setEnabled(True)
                self.checkBox_doc_refusal.setEnabled(True)

        # Выписной эпикриз и вся ИБ целиком
        if all((self.check_list[0],
                self.check_list[1],
                self.check_list[2],
                self.check_list[3],
                self.check_list[4],
                self.check_list[5],
                # self.check_list[6],  # блок рекомендаций (пока отсутствует)
                )):
            self.checkBox_doc_discharge_summary.setEnabled(True)
            self.checkBox_doc_full_history.setEnabled(True)
            self.checkBox_complex.setEnabled(True)

    # открытие папки с созданными файлами
    def open_folder(self):
        if 'созданные_документы' not in self.d:
            self.textBrowser.setText('Не создано ни одного документа!')
        else:
            self.textBrowser.setText(
                list_created_docs(self.d['созданные_документы']))
            try:
                open_folder_with_files(self.d)
            except FileNotFoundError:
                status_message = f'Созданные документы не обнаружены. '\
                                 f'Скорее всего они были созданы '\
                                 f'на другом компьютере и хранятся локально.'
                self.label_status.setText(status_message)

    def create_a_list_of_templates(self):
        # создаем список шаблонов для создания документов
        templates = []
        if self.checkBox_doc_consents.isChecked():
            templates.append('Согласия')
        if self.checkBox_doc_consent_bta.isChecked():
            templates.append('Согласие_БТА')
        if self.checkBox_doc_initial_inspection.isChecked():
            templates.append('Первичный_осмотр')
        if self.checkBox_doc_appointments.isChecked():
            templates.append('Лист_назначений')
        if self.checkBox_doc_protocol_bta.isChecked():
            templates.append('Протокол_БТА')
        if self.checkBox_doc_med_commission_bta.isChecked():
            templates.append('ВК_БТА')
        if self.checkBox_doc_statistic_talon.isChecked():
            templates.append('Стат.талон - 2стр (530н)')
        if self.checkBox_doc_statistic_talon_other.isChecked():
            templates.append('Стат_талон_дополнение')
        if self.checkBox_doc_med_commission_1.isChecked():
            templates.append('ВК_продление_ЛН')
        if self.checkBox_doc_back_frontpage.isChecked():
            templates.append('Титульный - 2стр (530н)')
        if self.checkBox_doc_discharge_summary.isChecked():
            templates.append('Выписной_эпикриз')
        if self.checkBox_doc_refusal.isChecked():
            templates.append('Отказ_от_госпитализации')
        if self.checkBox_doc_full_history.isChecked():
            templates.append('История_болезни_полная')
            templates.append('История_болезни_без_согласий')
            templates.append('Лист_назначений')
            templates.append('Стат.талон - 2стр (530н)')
            templates.append('Стат_талон_дополнение')
        if self.checkBox_doc_check_list.isChecked():
            templates.append('чек_лист_covid19')
        if self.checkBox_complex.isChecked():
            templates.append('Complex_doc')
            templates.append('Лист_назначений')

        # if self.checkBox_doc_statistic_talon_face.isChecked():
        #     templates.append('Стат.талон - 1стр (530н)')
        # if self.checkBox_doc_med_commission_drugs.isChecked():
        #     templates.append('ВК_на_препарат')
        # if self.checkBox_doc_frontpage.isChecked():
        #     templates.append('Титульный - 1стр (530н)')

        if templates == []:
            return None
        else:
            return templates

    def create_docs(self):
        if all((self.check_list[0],
                self.check_list[1],
                self.check_list[4])):
            # добавляем бта-дневники (после инъекции и для выписки)
            add_diaries_for_bta(self.d)

        # создаем список шаблоном для создания документов
        # по отмеченным checkBox's
        templates = self.create_a_list_of_templates()

        # проверяем что список не пустой
        if templates is not None:
            # проводим продление ЛН при необходимости
            w = ('ВК_продление_ЛН',
                 'ВК_продление_ЛН_2',
                 'ВК_продление_ЛН_выписка')
            for i in w:
                if i in templates:
                    refresh_worklist_data(self.d)

            # создаем выбранные документы
            creating_documents(self.d, templates)
            self.textBrowser.setText(
                list_created_docs(self.d['созданные_документы']))
        else:
            text = 'Не выбран ни один из шаблонов для '\
                   'создания документов! Действие отменено.'
            self.label_status.setText(text)

    def save_history(self):
        # записываем словарь в json-файл и обновляем БД
        write_all_data_to_db_bta(self.d)
        write_fullness_table_bta(self.d)
        # выводим сообщение об успехе сохранения
        text = '\tИстория болезни успешно сохранена!'
        self.label_status.setText(text)

    def save_and_close_card(self):
        self.save_history()
        self.close_card()

    def check_data_blocks(self):
        '''
        проверяет наличие блоков данных в словаре(d)
        при успешной проверке меняет цвет соответсвующей
        кнопки в карте пациента
        '''
        # формируем словарь с проверочными ключами и
        # присваиваем им соответвующие кнопки
        buttons_dict = {
            'ФИО_пациента': self.pushButtonOpenPtPassportData,
            'Соматический_статус': self.pushButtonOpenPtObjStatus,
            'Неврологический_статус': self.pushButtonOpenPtNeuralStatus,
            'Основной_диагноз': self.pushButtonOpenPtDiagnosis,
            'БТА_мышцы_мишени': self.pushButtonOpen_bta_protocol,
            'вид_выбытия': self.pushButtonOpen_discharge_data,
            'рекомендации_выписка': self.pushButtonOpen_recommends
        }

        # Собираем чек лист для "галочек" и валидности создания документов
        self.check_list = []
        # проверяем наличие блоков данных по соответствующих ключам в словаре d
        for key in buttons_dict:
            if key in self.d:
                # меняем стиль соответствующей кнопки
                if self.d[key] != '':
                    buttons_dict[key].setStyleSheet(style_true_button)
                    self.check_list.append(True)
                else:
                    # buttons_dict[key].setStyleSheet(style_False)
                    self.check_list.append(False)
            else:
                # buttons_dict[key].setStyleSheet(style_False)
                self.check_list.append(False)

        self.create_check_line()

    def create_check_line(self):
        check_line = ''
        for check in self.check_list:
            if check:
                check_line += '1'
            else:
                check_line += '0'
        self.d['check_line'] = check_line

    def check_created_docs(self):
        if 'созданные_документы' in self.d:
            if isinstance(self.d['созданные_документы'], str):
                self.d['созданные_документы'] = ast.literal_eval(
                    self.d['созданные_документы'])
            self.textBrowser.setText(
                list_created_docs(self.d['созданные_документы']))
        else:
            self.textBrowser.setText('Пока не создано ни одного документа :(')

    def print_keys_from_d(self):
        n = 0
        print('Ключи актуального словаря')
        for i in self.d:
            n += 1
            print(f'{n}) {i}')
        print(f'    Всего: {n}')
