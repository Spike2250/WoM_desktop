from PySide6 import QtWidgets

from wom.GUI.PY.omr import omr_Dynamic
from wom.app_logic.db_func\
    .bucket_func import (upload_history_to_yandex_cloud_bucket,
                         download_templates_json_from_yandex_cloud_bucket,
                         upload_templates_json_from_yandex_cloud_bucket)
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func\
    .json_templates import (read_templates,
                            templates_json_recording)


class Ui_Dynamic(QtWidgets.QWidget, omr_Dynamic.Ui_Dynamic):
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
              "реабилитации - Динамика"
        self.main_win.setWindowTitle(msg)
        objectTitleBar = self.main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_patient_info()
        self.set_connections()
        self.set_templates_list()
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
        self.d['динамика_вып'] = self.plainTextEdit_dynamic.toPlainText()
        self.d['MoCA_вып'] = self.comboBox_moca.currentText()
        self.d['HADS_t_вып'] = self.comboBox_hads_t.currentText()
        self.d['HADS_d_вып'] = self.comboBox_hads_d.currentText()
        self.d['ш_вассермана_вып'] = self.comboBox_logo_wasserman.currentText()
        self.d['ш_дизартрии_вып'] = self.comboBox_logo_disart.currentText()
        self.d['ш_прозопареза_вып'] = self.comboBox_logo_proso.currentText()
        self.d['ш_дисфагии_вып'] = self.comboBox_logo_dysphagia.currentText()

    def insert_data_from_dictionary(self):
        if 'динамика_вып' in self.d:
            self.comboBox_moca\
                .setCurrentText(self.d['MoCA_вып'])
            self.plainTextEdit_dynamic\
                .setPlainText(self.d['динамика_вып'])
            self.comboBox_hads_t\
                .setCurrentText(self.d['HADS_t_вып'])
            self.comboBox_hads_d\
                .setCurrentText(self.d['HADS_d_вып'])
            self.comboBox_logo_wasserman\
                .setCurrentText(self.d['ш_вассермана_вып'])
            self.comboBox_logo_disart\
                .setCurrentText(self.d['ш_дизартрии_вып'])
            self.comboBox_logo_proso\
                .setCurrentText(self.d['ш_прозопареза_вып'])
            self.comboBox_logo_dysphagia\
                .setCurrentText(self.d['ш_дисфагии_вып'])
        elif 'MoCA' in self.d:
            self.comboBox_moca\
                .setCurrentText(self.d['MoCA'])
            self.comboBox_hads_t\
                .setCurrentText(self.d['HADS_t'])
            self.comboBox_hads_d\
                .setCurrentText(self.d['HADS_d'])
            self.comboBox_logo_wasserman\
                .setCurrentText(self.d['ш_вассермана'])
            self.comboBox_logo_disart\
                .setCurrentText(self.d['ш_дизартрии'])
            self.comboBox_logo_proso\
                .setCurrentText(self.d['ш_прозопареза'])
            self.comboBox_logo_dysphagia\
                .setCurrentText(self.d['ш_дисфагии'])

    # @download_templates_json_from_yandex_cloud_bucket('dynamic')
    def set_templates_list(self):
        self.templates = read_templates('dynamic')
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
            self.templates[name] = self.plainTextEdit_dynamic.toPlainText()
            templates_file = 'dynamic'
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
            self.plainTextEdit_dynamic.setPlainText(self.templates[name])
        self.comboBox_templates.setCurrentText('')
