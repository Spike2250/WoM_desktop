from PySide6 import QtWidgets
from PySide6.QtWidgets import QAbstractItemView, QCheckBox, QPlainTextEdit

from wom.GUI.PY.omr import omr_MDRK
from wom.app_logic.handbooks.mdrk_data import rehab_goals, rehab_limits
from wom.app_logic.db_func\
    .bucket_func import (upload_history_to_yandex_cloud_bucket,
                         download_templates_json_from_yandex_cloud_bucket,
                         upload_templates_json_from_yandex_cloud_bucket)
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func\
    .json_templates import (read_templates,
                            templates_json_recording)
from wom.app_logic.writing.postprocessing\
    .mdrk import update_after_mdrk
from wom.styles_qss.main_styles import check_main, pTE_main
from wom.settings.dep_omr import mdrk_members


class Ui_Mdrk(QtWidgets.QWidget, omr_MDRK.Ui_MDRK):
    def __init__(self, user_info, windows, main_win, dictionary):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary

        self.initial_func()

    def initial_func(self):
        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Данные для протокола МДРК"
        self.main_win.setWindowTitle(msg)
        objectTitleBar = self.main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.comboBox_logo_name.clear()
        self.comboBox_psy_name.clear()
        self.comboBox_logo_name.addItems(mdrk_members['logo'])
        self.comboBox_psy_name.addItems(mdrk_members['psy'])

        self.set_patient_info()
        self.set_connections()
        self.set_templates_list()
        self.create_tables()
        self.insert_data_from_dictionary()

    def onButtonMy(self):
        pass

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText(
                'Ошибка! Нет "patient_info" в словаре!')

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonNotSaveExit\
            .clicked.connect(self.exit)
        self.pushButtonSaveExit\
            .clicked.connect(self.exit_and_save)
        self.pushButton_push_temp\
            .clicked.connect(self.push_active_template)
        self.pushButtonAddNewTemplate\
            .clicked.connect(self.add_new_template)

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
        self.d['реаб_потенциал'] =\
            self.comboBox_rehab_potentional.currentText()
        self.write_to_d_rehab_limits()
        self.write_to_d_rehab_goals()
        self.write_to_d_mdrk()
        update_after_mdrk(self.d)

    def create_tables(self):
        self.create_table('limits')
        self.create_table('goals')

    def create_table(self, type_):
        if type_ == 'limits':
            table = self.tableWidget_limits
            list_ = rehab_limits
        elif type_ == 'goals':
            table = self.tableWidget_goals
            list_ = rehab_goals

        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.setColumnCount(1)
        table.setColumnWidth(0, 947)
        table.horizontalHeader().hide()

        table.setRowCount((n := len(list_)) + 1)
        table.verticalHeader().hide()

        for index, elem in enumerate(list_):
            check_box = QCheckBox(elem)
            check_box.setStyleSheet(check_main)
            table.setCellWidget(index, 0, check_box)
        pTE = QPlainTextEdit()
        pTE.setPlaceholderText('допишите, при необходимости')
        pTE.setStyleSheet(pTE_main)
        table.setRowHeight(n, 50)
        table.setCellWidget(n, 0, pTE)

    def insert_data_from_dictionary(self):
        self.insert_from_d_rehab_limits()
        self.insert_from_d_rehab_goals()
        self.insert_from_d_mdrk()

    def insert_from_d_rehab_limits(self):
        if 'list_limits' in self.d:
            for index in range((n := len(rehab_limits))):
                checkBox = self.tableWidget_limits.cellWidget(index, 0)
                if checkBox.text() in self.d['list_limits']:
                    checkBox.setChecked(True)
            self.tableWidget_limits\
                .cellWidget(n, 0)\
                .setPlainText(self.d['limits_other'])
        # для совместимости со старыми версиями
        elif 'огран_1' in self.d:
            self.d['list_limits'] = []
            for index, elem in enumerate(rehab_limits):
                if self.d.get(f"огран_{index + 1}"):
                    self.d['list_limits'].append(elem)
            self.d['limits_other'] = self.d['огран_другое']
            self.insert_from_d_rehab_limits()

    def insert_from_d_rehab_goals(self):
        if 'list_goals' in self.d:
            self.plainTextEdit_goals.setPlainText(self.d.get('rehab_goal'))
            for index in range((n := len(rehab_goals))):
                checkBox = self.tableWidget_goals.cellWidget(index, 0)
                if checkBox.text() in self.d['list_goals']:
                    checkBox.setChecked(True)
            self.tableWidget_goals\
                .cellWidget(n, 0)\
                .setPlainText(self.d['goals_other'])
        # для совместимости со старыми версиями
        elif 'цель_1' in self.d:
            self.d['list_goals'] = []
            for index, elem in enumerate(rehab_goals):
                if self.d.get(f"цель_{index + 1}"):
                    self.d['list_goals'].append(elem)
            self.d['goals_other'] = self.d['цель_другое']
            self.insert_from_d_rehab_goals()

    def insert_from_d_mdrk(self):
        if 'закл_психолога' in self.d:
            self.plainTextEdit_psy_conclusion\
                .setPlainText(self.d['закл_психолога'])
            self.comboBox_moca.setCurrentText(self.d['MoCA'])
            self.comboBox_hads_t.setCurrentText(self.d['HADS_t'])
            self.comboBox_hads_d.setCurrentText(self.d['HADS_d'])
            self.comboBox_psy_name.setCurrentText(self.d['ФИО_психолог'])

        if 'закл_логопеда' in self.d:
            self.plainTextEdit_logo_conclusion\
                .setPlainText(self.d['закл_логопеда'])
            self.comboBox_logo_wasserman.setCurrentText(self.d['ш_вассермана'])
            self.comboBox_logo_disart.setCurrentText(self.d['ш_дизартрии'])
            self.comboBox_logo_proso.setCurrentText(self.d['ш_прозопареза'])
            self.comboBox_logo_dysphagia.setCurrentText(self.d['ш_дисфагии'])
            self.comboBox_logo_name.setCurrentText(self.d['ФИО_логопед'])

        if 'ФИО_ЛФК' in self.d:
            self.plainTextEdit_lfk.setPlainText(self.d['лфк'])
            self.plainTextEdit_physio.setPlainText(self.d['физиотерапия'])

            self.label_lfk_name.setText(self.d['ФИО_ЛФК'])
            self.label_physio_name.setText(self.d['ФИО_Физиотерапевт'])

    def write_to_d_rehab_limits(self):
        self.d['list_limits'] = []
        for index, elem in enumerate(rehab_limits):
            if self.tableWidget_limits.cellWidget(index, 0).isChecked():
                self.d['list_limits'].append(elem)
        self.d['limits_other'] = self.tableWidget_limits\
            .cellWidget(len(rehab_limits), 0).toPlainText()

    def write_to_d_rehab_goals(self):
        self.d['rehab_goal'] = self.plainTextEdit_goals.toPlainText()
        self.d['list_goals'] = []
        for index, elem in enumerate(rehab_goals):
            if self.tableWidget_goals.cellWidget(index, 0).isChecked():
                self.d['list_goals'].append(elem)
        self.d['goals_other'] = self.tableWidget_goals\
            .cellWidget(len(rehab_goals), 0).toPlainText()

    def write_to_d_mdrk(self):
        self.d['закл_психолога'] =\
            self.plainTextEdit_psy_conclusion.toPlainText()
        self.d['MoCA'] = self.comboBox_moca.currentText()
        self.d['HADS'] = f'{self.comboBox_hads_t.currentText()}' \
                         f'/{self.comboBox_hads_d.currentText()}'
        self.d['HADS_t'] = self.comboBox_hads_t.currentText()
        self.d['HADS_d'] = self.comboBox_hads_d.currentText()
        self.d['ФИО_психолог'] = self.comboBox_psy_name.currentText()

        self.d['закл_логопеда'] =\
            self.plainTextEdit_logo_conclusion.toPlainText()
        self.d['ш_вассермана'] = self.comboBox_logo_wasserman.currentText()
        self.d['ш_дизартрии'] = self.comboBox_logo_disart.currentText()
        self.d['ш_прозопареза'] = self.comboBox_logo_proso.currentText()
        self.d['ш_дисфагии'] = self.comboBox_logo_dysphagia.currentText()
        self.d['ФИО_логопед'] = self.comboBox_logo_name.currentText()

    # @download_templates_json_from_yandex_cloud_bucket('rehab_goal')
    def set_templates_list(self):
        self.templates = read_templates('rehab_goal')
        if self.templates is not None:
            templates_list = sorted(list(self.templates))
            self.comboBox_templates.clear()
            self.comboBox_templates.addItem('')
            self.comboBox_templates.addItems(templates_list)
        else:
            self.templates = {}
            self.comboBox_templates.clear()

    def add_new_template(self):
        name = self.lineEdit_new_template_name.text()

        if name != '':
            self.templates[name] = self.plainTextEdit_goals.toPlainText()
            templates_file = 'rehab_goal'
            templates_json_recording(templates=self.templates,
                                     templates_name=templates_file)
            # загружаем в бакет
            # upload_templates_json_from_yandex_cloud_bucket(templates_file)
            # обновляем список шаблонов
            self.lineEdit_new_template_name.setText('')
            self.set_templates_list()

    def push_active_template(self):
        name = self.comboBox_templates.currentText()
        if name in self.templates:
            self.plainTextEdit_goals.setPlainText(self.templates[name])
        self.comboBox_templates.setCurrentText('')
