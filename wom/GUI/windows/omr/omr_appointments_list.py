from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QWidget,
    QTableWidgetItem as QTW_Item,
    QAbstractItemView,
    QPushButton,
    QPlainTextEdit,
)
from datetime import datetime
from copy import deepcopy

from wom.GUI.PY.omr import omr_Appointments
from wom.app_logic.db_func\
    .bucket_func import (upload_history_to_yandex_cloud_bucket,
                         download_templates_json_from_yandex_cloud_bucket,
                         upload_templates_json_from_yandex_cloud_bucket)
from wom.app_logic.db_func\
    .json_templates import (read_templates,
                            templates_json_recording)
from wom.app_logic.db_func.drugs_almanac import read_almanac
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.writing.postprocessing\
    .appointments import update_after_appointments
from wom.styles_qss.main_styles import button_own, button_other
from wom.settings.config import mdrk_members
from wom.settings.appointment_lists import lfk
from wom.styles_qss.main_styles import pTE_drugs


class Ui_Appointments(QWidget, omr_Appointments.Ui_Appointments):
    def __init__(self, user_info, windows, main_win, dictionary):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary

        self.initial_func()

    def initial_func(self):
        self.d_temp = {}
        self.list_sol = []
        self.list_tab = []
        self.list_lfk = []
        self.list_physio = []

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Листы назначений"
        self.main_win.setWindowTitle(msg)
        objectTitleBar = self.main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.create_tables()
        self.set_connections()
        self.set_patient_info()
        self.set_styles()
        self.read_almanac_json()
        self.set_templates()
        self.insert_lfk_physio_md_lists()
        self.add_values_to_lfk_comboboxes()

        self.insert_data_from_dictionary()
        self.refresh_all_tables()

    def onButtonMy(self):
        pass

    def insert_lfk_physio_md_lists(self):
        # списки для членов МДРК
        self.comboBox_lfk_name.clear()
        self.comboBox_physio_name.clear()
        self.comboBox_lfk_name.addItems(mdrk_members['lfk'])
        self.comboBox_physio_name.addItems(mdrk_members['physio'])

    def add_values_to_lfk_comboboxes(self):
        self.comboBox_lfk.clear()
        self.comboBox_lfk_duration.clear()
        self.comboBox_lfk_ed.clear()

        self.comboBox_lfk.addItems(list(lfk['procedure'].keys()))
        self.comboBox_lfk_duration.addItems(lfk['regimen'])
        self.comboBox_lfk_ed.addItems(lfk['ed'])

    def open_patient_card(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['omr']['patient_card'](
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

    # @upload_history_to_yandex_cloud_bucket('omr')
    def save_history(self):
        self.write_to_dictionary()
        write_all_data_to_db_omr(self.d)

    def write_to_dictionary(self):
        '''
        '''
        self.d['стол'] = self.comboBox_diet.currentText()
        self.d['режим'] = self.comboBox_functional_mode.currentText()

        self.write_drugs_appointments()
        self.write_lfk_appointments()
        self.write_physiotherapy_appointments()

        self.d['ФИО_ЛФК'] = self.comboBox_lfk_name.currentText()
        self.d['ФИО_Физиотерапевт'] = self.comboBox_physio_name.currentText()

        update_after_appointments(self.d)

    def insert_data_from_dictionary(self):
        '''
        '''
        self.comboBox_functional_mode.setCurrentText(self.d['режим'])
        if 'стол' in self.d:
            self.comboBox_diet.setCurrentText(self.d['стол'])
        self.insert_drugs_data()
        self.insert_lfk_data()
        self.insert_physio_data()

    def refresh_all_tables(self):
        self.refresh_tables_drugs_appointment()
        self.refresh_lfk_table()
        self.refresh_physio_table()

    def set_templates(self):
        self.set_templates_list_lfk()
        self.set_templates_list_physio()

    def create_tables(self):
        # делаем значения таблицы неизменяемыми
        self.tableWidget_sol.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_peros.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_lfk.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_physio.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)

        self.tableWidget_sol.setColumnWidth(0, 95)  # ширина колонок
        self.tableWidget_sol.setColumnWidth(1, 200)  # по номеру колонки
        self.tableWidget_sol.setColumnWidth(2, 80)
        self.tableWidget_sol.setColumnWidth(3, 235)
        self.tableWidget_sol.setColumnWidth(4, 35)

        self.tableWidget_peros.setColumnWidth(0, 95)
        self.tableWidget_peros.setColumnWidth(1, 200)
        self.tableWidget_peros.setColumnWidth(2, 80)
        self.tableWidget_peros.setColumnWidth(3, 235)
        self.tableWidget_peros.setColumnWidth(4, 35)

        self.tableWidget_lfk.setColumnWidth(0, 648)
        self.tableWidget_lfk.setColumnWidth(1, 100)
        self.tableWidget_lfk.setColumnWidth(2, 90)
        self.tableWidget_lfk.setColumnWidth(3, 35)

        self.tableWidget_physio.setColumnWidth(0, 374)
        self.tableWidget_physio.setColumnWidth(1, 374)
        self.tableWidget_physio.setColumnWidth(2, 90)
        self.tableWidget_physio.setColumnWidth(3, 35)

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonNotSaveExit\
            .clicked.connect(self.exit)
        self.pushButtonSaveExit\
            .clicked.connect(self.exit_and_save)
        self.pushButton_add_and_continue\
            .clicked.connect(self.add_drug_to_appointments)
        self.pushButton_set_adm_date\
            .clicked.connect(self.set_adm_date)
        self.pushButton_set_today_date\
            .clicked.connect(self.set_today_date)
        self.pushButton_clean\
            .clicked.connect(self.clean_forms)

        self.pushButton_add_lfk\
            .clicked.connect(self.add_lfk_appointment)
        self.pushButton_lfk_push_temp\
            .clicked.connect(self.push_active_template_lfk)
        self.pushButton_lfk_add_new_template\
            .clicked.connect(self.add_new_template_lfk)

        self.pushButton_add_physio\
            .clicked.connect(self.add_physio_appointment)
        self.pushButton_push_temp_physio\
            .clicked.connect(self.push_active_template_physio)
        self.pushButton_add_new_template_physio\
            .clicked.connect(self.add_new_template_physio)

        # коннекты чекбоксов
        self.checkBox_lfk_same.stateChanged.connect(self.set_lfk_md)
        self.checkBox_physio_same.stateChanged.connect(self.set_physio_md)

    """==========================
    Drugs appointments functions
    =========================="""

    def write_drugs_appointments(self):
        self.rewrite_app_DS(
            list_=self.list_sol,
            table=self.tableWidget_sol)
        self.rewrite_app_DS(
            list_=self.list_tab,
            table=self.tableWidget_peros)
        self.d['d_sol'] = deepcopy(self.list_sol)
        self.d['d_tab'] = deepcopy(self.list_tab)

    def rewrite_app_DS(self, list_, table):
        for index, app in enumerate(list_):
            app['DS'] = table.cellWidget(index, 3).toPlainText()

    def insert_drugs_data(self):
        if 'd_sol' in self.d and 'd_tab' in self.d:
            self.list_sol = deepcopy(self.d['d_sol'])
            self.list_tab = deepcopy(self.d['d_tab'])

    def refresh_tables_drugs_appointment(self):
        self.refresh_drugs_table('per_os')
        self.refresh_drugs_table('sol')

    def define_drugs_key_and_table(self, table_name):
        if table_name == 'per_os':
            list_ = self.list_tab
            table = self.tableWidget_peros
            del_func = self.delete_drug_tab
        elif table_name == 'sol':
            list_ = self.list_sol
            table = self.tableWidget_sol
            del_func = self.delete_drug_sol
        return list_, table, del_func

    def refresh_drugs_table(self, table_name):
        list_, table, del_func = self.define_drugs_key_and_table(table_name)

        if (len_ := len(list_)) != 0:
            table.setRowCount(len_)
            for i in range(len_):
                table.setRowHeight(i, 40)

                table.setItem(i, 0, QTW_Item(list_[i]['date']))
                table.setItem(i, 1, QTW_Item(list_[i]['drug']))
                table.setItem(i, 2, QTW_Item(list_[i]['dose']))

                pTE = QPlainTextEdit(list_[i]['DS'])
                pTE.setStyleSheet(pTE_drugs)
                table.setCellWidget(i, 3, pTE)
                # table.setItem(i, 3, QTW_Item(list_[i]['DS']))

                button_delete = QPushButton()
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(":/icon/icons/block_white_36dp.svg"),
                    QtGui.QIcon.Mode.Normal,
                    QtGui.QIcon.State.Off)
                button_delete.setIcon(icon)
                button_delete.setIconSize(QtCore.QSize(25, 25))
                button_delete.setStyleSheet(button_own)
                button_delete.clicked.connect(del_func)
                table.setCellWidget(i, 4, button_delete)
        else:
            table.setRowCount(0)
            table.setRowCount(1)
            table.setItem(0, 1, QTW_Item('Назначения отсутствуют'))

    def delete_drug(self, table_name):
        list_ = self.define_drugs_key_and_table(table_name)[0]
        table = self.define_drugs_key_and_table(table_name)[1]

        button = self.sender()
        i = table.indexAt(button.pos()).row()
        list_.pop(i)

        self.refresh_drugs_table(table_name)

    def delete_drug_tab(self):
        self.delete_drug('per_os')

    def delete_drug_sol(self):
        self.delete_drug('sol')

    def read_almanac_json(self):
        table = self.tableWidget_drugs

        self.almanac = read_almanac()
        if self.almanac is None:
            text = 'Отсутствует справочник лек.средств!'
            table.setColumnCount(1)
            table.setRowCount(1)
            table.setColumnWidth(0, 350)
            table.setHorizontalHeaderLabels(['Ошибка'])
            table.setVerticalHeaderLabels([''])
            table.setItem(0, 0, QTW_Item(text))
        else:
            self.pushButton_restart.clicked.connect(self.start)
            self.start()

    def start(self):
        table = self.tableWidget_drugs

        self.clean_forms()

        table.setColumnCount(0)
        table.setColumnCount(1)
        table.setColumnWidth(0, 360)
        label = 'Выберите дату назначения лек.средства'
        table.setHorizontalHeaderLabels([label])
        table.setRowCount(3)
        table.setVerticalHeaderLabels(['', '', ''])
        button_adm_day = QPushButton('Дата поступления')
        button_today = QPushButton('Сегодня')
        button_latter = QPushButton('пропустить')
        button_adm_day.setStyleSheet(button_other)
        button_today.setStyleSheet(button_other)
        button_latter.setStyleSheet(button_other)
        button_adm_day.clicked.connect(self.step_group)
        button_today.clicked.connect(self.step_group)
        button_latter.clicked.connect(self.step_group)
        table.setCellWidget(0, 0, button_adm_day)
        table.setCellWidget(1, 0, button_today)
        table.setCellWidget(2, 0, button_latter)

    def step_group(self):
        table = self.tableWidget_drugs

        button_day = self.sender()
        name_button_day = button_day.text()
        if name_button_day == 'Дата поступления':
            self.d_temp['date'] = self.d['дата_поступления']
        elif name_button_day == 'Сегодня':
            self.d_temp['date'] = datetime.today().strftime('%d.%m.%Y')
        else:
            self.d_temp['date'] = '01.01.2000'
        n = len(self.almanac)
        table.setColumnCount(0)
        table.setColumnCount(1)
        table.setColumnWidth(0, 360)
        header = 'Выберите фармакологическую группу'
        table.setHorizontalHeaderLabels([header])
        table.setRowCount(n)
        vertical_labels = []
        for k in range(n):
            vertical_labels.append(' ')
        table.setVerticalHeaderLabels(vertical_labels)
        i = 0
        for group in sorted(self.almanac):
            button = QPushButton(group)
            button.setStyleSheet(button_other)
            button.clicked.connect(self.step_drug)
            table.setCellWidget(i, 0, button)
            i += 1

    def step_drug(self):
        table = self.tableWidget_drugs

        button_group = self.sender()
        group = button_group.text()
        self.d_temp['group'] = group
        table.setHorizontalHeaderLabels(['Выберите лек.средство'])
        table.setRowCount(0)
        n = len(self.almanac[group])
        table.setRowCount(n)
        vertical_labels = []
        for k in range(n):
            vertical_labels.append(' ')
        table.setVerticalHeaderLabels(vertical_labels)
        i = 0
        for drug in sorted(self.almanac[group]):
            button = QPushButton(drug)
            button.setStyleSheet(button_other)
            button.clicked.connect(self.step_dose)
            table.setCellWidget(i, 0, button)
            i += 1

    def step_dose(self):
        table = self.tableWidget_drugs

        button_drug = self.sender()
        drug = button_drug.text()
        group = self.d_temp['group']
        self.d_temp['drug'] = drug

        table.setHorizontalHeaderLabels(['Выберите дозировку'])
        table.setRowCount(0)

        doses_n = len(doses := self.almanac[group][drug]['doses'].split('; '))
        table.setRowCount(doses_n)
        vertical_labels = []
        for k in range(doses_n):
            vertical_labels.append(' ')
        table.setVerticalHeaderLabels(vertical_labels)
        i = 0
        for dose in doses:
            button = QPushButton(dose)
            button.setStyleSheet(button_other)
            button.clicked.connect(self.step_DS)
            table.setCellWidget(i, 0, button)
            i += 1

    def step_DS(self):
        table = self.tableWidget_drugs

        button_dose = self.sender()
        dose = button_dose.text()
        group = self.d_temp['group']
        drug = self.d_temp['drug']
        self.d_temp['dose'] = dose

        table.setHorizontalHeaderLabels(['Выберите назначение'])
        table.setRowCount(0)

        ds_n = len(DS := self.almanac[group][drug]['DS'].split('; '))
        table.setRowCount(ds_n)
        vertical_labels = []
        for k in range(ds_n):
            vertical_labels.append(' ')
        table.setVerticalHeaderLabels(vertical_labels)
        i = 0
        for ds in DS:
            button = QPushButton(ds)
            button.setStyleSheet(button_other)
            button.clicked.connect(self.step_final)
            table.setCellWidget(i, 0, button)
            i += 1

    def step_final(self):
        table = self.tableWidget_drugs

        button_ds = self.sender()
        ds = button_ds.text()
        self.d_temp['DS'] = ds

        group = self.d_temp['group']
        drug = self.d_temp['drug']

        if self.checkBox.isChecked():
            latin_drug = f'{self.almanac[group][drug]["form"].split("; ")[1]}'\
                         f'{self.almanac[group][drug]["latin_name"]}'
            self.d_temp['drug'] = latin_drug

        self.dateEdit.setDate(
            QtCore.QDate.fromString(self.d_temp['date'], "dd.MM.yyyy"))
        self.lineEdit_drug.setText(self.d_temp['drug'])
        self.lineEdit_dose.setText(self.d_temp['dose'])
        self.lineEdit_DS.setText(self.d_temp['DS'])

        table.setColumnCount(0)
        table.setRowCount(0)

        self.d_temp = {}

    def add_drug_to_appointments(self):
        '''
        '''

        d_drug = {
            'date': self.dateEdit.dateTime().toString('dd.MM.yyyy'),
            'drug': self.lineEdit_drug.text(),
            'dose': self.lineEdit_dose.text(),
            'DS': self.lineEdit_DS.text()
        }

        check_fullness = True
        for i in d_drug:
            if d_drug[i] == '':
                check_fullness = False

        if check_fullness:
            if d_drug['date'] != '01.01.2000':
                if self.comboBox.currentText() == 'в инъекционный л/н':
                    self.list_sol.append(d_drug)
                    self.refresh_drugs_table('sol')
                elif self.comboBox.currentText() == 'в энтеральный л/н':
                    self.list_tab.append(d_drug)
                    self.refresh_drugs_table('per_os')
                self.start()
            else:
                self.label_status.setText('Дата не введена!')
        else:
            self.label_status.setText('Данные препарата не полные!')

    def set_adm_date(self):
        self.dateEdit.setDate(
            QtCore.QDate.fromString(self.d['дата_поступления'], "dd.MM.yyyy"))

    def set_today_date(self):
        today = datetime.now().strftime('%d.%m.%Y')
        self.dateEdit.setDate(QtCore.QDate.fromString(today, "dd.MM.yyyy"))

    def clean_forms(self):
        self.dateEdit.setDate(
            QtCore.QDate.fromString('01.01.2000', "dd.MM.yyyy"))
        self.lineEdit_drug.setText('')
        self.lineEdit_dose.setText('')
        self.lineEdit_DS.setText('')

    """==========================
    LFK appointments functions
    =========================="""

    def write_lfk_appointments(self):
        self.d['d_lfk'] = deepcopy(self.list_lfk)

    def insert_lfk_data(self):
        if 'd_lfk' in self.d:
            self.list_lfk = deepcopy(self.d['d_lfk'])

    def refresh_lfk_table(self):
        table = self.tableWidget_lfk

        if (len_ := len(self.list_lfk)) != 0:
            table.setRowCount(len_)
            for i in range(len_):
                table.setItem(i, 0, QTW_Item(self.list_lfk[i]['procedure']))
                table.setItem(i, 1, QTW_Item(self.list_lfk[i]['regimen']))
                table.setItem(i, 2, QTW_Item(self.list_lfk[i]['ed']))
                button_delete = QPushButton()
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(":/icon/icons/block_white_36dp.svg"),
                    QtGui.QIcon.Mode.Normal,
                    QtGui.QIcon.State.Off)
                button_delete.setIcon(icon)
                button_delete.setIconSize(QtCore.QSize(25, 25))
                button_delete.setStyleSheet(button_own)
                button_delete.clicked.connect(self.delete_lfk)
                table.setCellWidget(i, 3, button_delete)
        # для обратной совместимости со старыми назначениями
        elif 'лфк_1' in self.d:
            self.d['d_lfk'] = []
            for i in range(1, 11):
                lfk = {'procedure': self.d[f'лфк_{i}'],
                       'regimen': self.d[f'лфк_прдлж_{i}'],
                       'ed': ''}
                if lfk['procedure'] != '':
                    self.d['d_lfk'].append(lfk)
            self.insert_lfk_data()
            self.refresh_lfk_table()
        # назначений нет
        else:
            table.setRowCount(0)
            table.setRowCount(1)
            table.setItem(0, 1, QTW_Item('Назначения отсутствуют'))

    def delete_lfk(self):
        button = self.sender()
        i = self.tableWidget_lfk.indexAt(button.pos()).row()
        self.list_lfk.pop(i)
        self.refresh_lfk_table()

    # @download_templates_json_from_yandex_cloud_bucket('lfk_appointments')
    def set_templates_list_lfk(self):
        self.lfk_templates = read_templates('lfk_appointments')
        if self.lfk_templates is not None:
            templates_list = sorted(list(self.lfk_templates))
            self.comboBox_lfk_template.clear()
            self.comboBox_lfk_template.addItem('')
            self.comboBox_lfk_template.addItems(templates_list)
        else:
            self.lfk_templates = {}
            self.comboBox_lfk_template.clear()

    def add_new_template_lfk(self):
        name = self.lineEdit_lfk_new_template_name.text()

        if name != '':
            self.lfk_templates[name] = self.list_lfk
            templates_file = 'lfk_appointments'
            templates_json_recording(templates=self.lfk_templates,
                                     templates_name=templates_file)
            # загружаем в бакет
            # upload_templates_json_from_yandex_cloud_bucket(templates_file)
            # обновляем список шаблонов
            self.lineEdit_lfk_new_template_name.setText('')
            self.set_templates_list_lfk()

    def push_active_template_lfk(self):
        name = self.comboBox_lfk_template.currentText()
        if name in self.lfk_templates:
            self.list_lfk = []
            for row in self.lfk_templates[name]:
                self.list_lfk.append(row)
            self.refresh_lfk_table()
        self.comboBox_lfk_template.setCurrentText('')

    def add_lfk_appointment(self):
        if self.comboBox_lfk_duration.currentText() != '' and \
                self.comboBox_lfk.currentText() != '' and \
                self.comboBox_lfk_ed.currentText() != '':
            lfk = {
                'procedure': self.comboBox_lfk.currentText(),
                'regimen': self.comboBox_lfk_duration.currentText(),
                'ed': self.comboBox_lfk_ed.currentText(),
            }
            self.list_lfk.append(lfk)
            self.refresh_lfk_table()

            self.comboBox_lfk.setCurrentText("")
            self.comboBox_lfk_duration.setCurrentText("")
            self.comboBox_lfk_ed.setCurrentText("")
        else:
            msg = 'Данные заполнены не в полном объеме!'
            self.label_status_lfk.setText(msg)

    def set_lfk_md(self):
        if self.checkBox_lfk_same.isChecked():
            self.lfk_md = self.comboBox_lfk_name.currentText()
            self.comboBox_lfk_name.setCurrentText(self.d['ФИО_врача'])
            self.comboBox_lfk_name.setEnabled(False)
        else:
            self.comboBox_lfk_name.setCurrentText(self.lfk_md)
            self.comboBox_lfk_name.setEnabled(True)

    """==========================
    Physiotherapy appointments functions
    =========================="""

    def write_physiotherapy_appointments(self):
        self.d['d_physio'] = deepcopy(self.list_physio)

    def insert_physio_data(self):
        if 'd_physio' in self.d:
            self.list_physio = deepcopy(self.d['d_physio'])

    def refresh_physio_table(self):
        table = self.tableWidget_physio

        if (len_ := len(self.list_physio)) != 0:
            table.setRowCount(len_)
            for i in range(len_):
                table.setItem(i, 0, QTW_Item(self.list_physio[i]['procedure']))
                table.setItem(i, 1, QTW_Item(self.list_physio[i]['place']))
                table.setItem(i, 2, QTW_Item(self.list_physio[i]['regimen']))
                button_delete = QPushButton()
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(":/icon/icons/block_white_36dp.svg"),
                    QtGui.QIcon.Mode.Normal,
                    QtGui.QIcon.State.Off)
                button_delete.setIcon(icon)
                button_delete.setIconSize(QtCore.QSize(25, 25))
                button_delete.setStyleSheet(button_own)
                button_delete.clicked.connect(self.delete_physio)
                table.setCellWidget(i, 3, button_delete)
        # для обратной совместимости со старыми назначениями
        elif 'физио_1' in self.d:
            self.d['d_physio'] = []
            for i in range(1, 5):
                physio = {'procedure': self.d[f'физио_{i}'],
                          'place': self.d[f'физио_место_{i}'],
                          'regimen': self.d[f'физио_прдлж_{i}']}
                if physio['procedure'] != '':
                    self.d['d_physio'].append(physio)
            self.insert_physio_data()
            self.refresh_physio_table()
        # назначений нет
        else:
            table.setRowCount(0)
            table.setRowCount(1)
            table.setItem(0, 1, QTW_Item('Назначения отсутствуют'))

    def delete_physio(self):
        button = self.sender()
        i = self.tableWidget_physio.indexAt(button.pos()).row()
        self.list_physio.pop(i)
        self.refresh_physio_table()

    # @download_templates_json_from_yandex_cloud_bucket('physio_appointments')
    def set_templates_list_physio(self):
        self.physio_templates = read_templates('physio_appointments')
        if self.physio_templates is not None:
            templates_list = sorted(list(self.physio_templates))
            self.comboBox_template_physio.clear()
            self.comboBox_template_physio.addItem('')
            self.comboBox_template_physio.addItems(templates_list)
        else:
            self.physio_templates = {}
            self.comboBox_template_physio.clear()

    def add_new_template_physio(self):
        name = self.lineEdit_new_template_name_physio.text()

        if name != '':
            self.physio_templates[name] = self.list_physio
            templates_file = 'physio_appointments'
            templates_json_recording(templates=self.physio_templates,
                                     templates_name=templates_file)
            # загружаем в бакет
            # upload_templates_json_from_yandex_cloud_bucket(templates_file)
            # обновляем список шаблонов
            self.lineEdit_new_template_name_physio.setText('')
            self.set_templates_list_physio()

    def push_active_template_physio(self):
        name = self.comboBox_template_physio.currentText()
        if name in self.physio_templates:
            self.list_physio = []
            for row in self.physio_templates[name]:
                self.list_physio.append(row)
            self.refresh_physio_table()
        self.comboBox_template_physio.setCurrentText('')

    def add_physio_appointment(self):
        if self.comboBox_physio.currentText() != ''\
                and self.comboBox_physio_place.currentText() != ''\
                and self.comboBox_physio_duration.currentText() != '':

            physio = {
                'procedure': self.comboBox_physio.currentText(),
                'place': self.comboBox_physio_place.currentText(),
                'regimen': self.comboBox_physio_duration.currentText(),
            }
            self.list_physio.append(physio)
            self.refresh_physio_table()

            self.comboBox_physio.setCurrentText("")
            self.comboBox_physio_place.setCurrentText("")
            self.comboBox_physio_duration.setCurrentText("")
        else:
            msg = 'Данные заполнены не в полном объеме!'
            self.label_status_physio.setText(msg)

    def set_physio_md(self):
        if self.checkBox_physio_same.isChecked():
            self.physio_md = self.comboBox_physio_name.currentText()
            self.comboBox_physio_name.setCurrentText(self.d['ФИО_врача'])
            self.comboBox_physio_name.setEnabled(False)
        else:
            self.comboBox_physio_name.setCurrentText(self.physio_md)
            self.comboBox_physio_name.setEnabled(True)

    """==========================
    Other
    =========================="""

    def set_styles(self):
        pass
