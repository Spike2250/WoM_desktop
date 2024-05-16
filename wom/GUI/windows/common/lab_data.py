from PySide6 import QtWidgets, QtCore

from wom.GUI.PY.common import Laboratory_data
from wom.app_logic.db_func\
    .bucket_func import (upload_history_to_yandex_cloud_bucket,
                         download_templates_json_from_yandex_cloud_bucket,
                         upload_templates_json_from_yandex_cloud_bucket)
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.db_func\
    .json_templates import (read_templates,
                            templates_json_recording)
from wom.app_logic.writing.postprocessing.lab_data import forming


# Окно лабораторных данных
class Ui_Laboratory_data(QtWidgets.QWidget,
                         Laboratory_data.Ui_Lab_data):
    def __init__(self, user_info, windows, main_win, dictionary, case_type):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.case_type = case_type

        self.d_temp = {}

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Лабораторные данные"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_templates_list()
        self.insert_data_from_dictionary()
        self.create_dict_of_widgets()
        self.set_patient_info()
        self.set_connections()
        self.set_styles()

    def onButtonMy(self):
        pass

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

    # @download_templates_json_from_yandex_cloud_bucket('lab_templates')
    def set_templates_list(self):
        # список шаблонов
        self.templates = read_templates('lab_templates')

        if self.templates is not None:
            self.templates_list = list(self.templates)
            self.comboBox_mylab_template.clear()
            self.comboBox_mylab_template.addItem('')
            if len(self.templates_list) <= 1:
                self.comboBox_mylab_template.addItem(self.templates_list[0])
            else:
                self.comboBox_mylab_template.addItems(self.templates_list)
        else:
            self.templates = {}
            self.comboBox_mylab_template.clear()

    def create_dict_of_widgets(self):
        self.widget = {
            "label_Er": self.label_Er,
            "label_Hb": self.label_Hb,
            "label_Ht": self.label_Ht,
            "label_Le": self.label_Le,
            "label_Le_B": self.label_Le_B,
            "label_Le_Eoz": self.label_Le_Eoz,
            "label_Le_Lym": self.label_Le_Lym,
            "label_Le_M": self.label_Le_M,
            "label_Le_N": self.label_Le_N,
            "label_Le_N_p": self.label_Le_N_p,
            "label_Le_N_yu": self.label_Le_N_yu,
            "label_Le_N_s": self.label_Le_N_s,
            "label_OAK_report": self.label_OAK_report,
            "label_Tr": self.label_Tr,
            "label_color": self.label_color,
            "label_soe": self.label_soe,
            "lineEdit_Er": self.lineEdit_Er,
            "lineEdit_Hb": self.lineEdit_Hb,
            "lineEdit_Ht": self.lineEdit_Ht,
            "lineEdit_Le": self.lineEdit_Le,
            "lineEdit_Le_B": self.lineEdit_Le_B,
            "lineEdit_Le_Eoz": self.lineEdit_Le_Eoz,
            "lineEdit_Le_Lym": self.lineEdit_Le_Lym,
            "lineEdit_Le_M": self.lineEdit_Le_M,
            "lineEdit_Le_N_p": self.lineEdit_Le_N_p,
            "lineEdit_Le_N_s": self.lineEdit_Le_N_s,
            "lineEdit_Le_N_yu": self.lineEdit_Le_N_yu,
            "lineEdit_OAK_other": self.lineEdit_OAK_other,
            "lineEdit_OAK_other_r": self.lineEdit_OAK_other_r,
            "lineEdit_Tr": self.lineEdit_Tr,
            "lineEdit_color": self.lineEdit_color,
            "lineEdit_soe": self.lineEdit_soe,
            "label_OAM_report": self.label_OAM_report,
            "label_udel_ves": self.label_udel_ves,
            "label_urine_Bacteria": self.label_urine_Bacteria,
            "label_urine_Er": self.label_urine_Er,
            "label_urine_Le": self.label_urine_Le,
            "label_urine_aceton": self.label_urine_aceton,
            "label_urine_cilindr": self.label_urine_cilindr,
            "label_urine_color": self.label_urine_color,
            "label_urine_epit_pl": self.label_urine_epit_pl,
            "label_urine_epit_ren": self.label_urine_epit_ren,
            "label_urine_epit_zern": self.label_urine_epit_zern,
            "label_urine_gluc": self.label_urine_gluc,
            "label_urine_light": self.label_urine_light,
            "label_urine_protein": self.label_urine_protein,
            "label_urine_salt": self.label_urine_salt,
            "label_urine_slime": self.label_urine_slime,
            "lineEdit_udel_ves": self.lineEdit_udel_ves,
            "lineEdit_urine_Bacteria": self.lineEdit_urine_Bacteria,
            "lineEdit_urine_Er": self.lineEdit_urine_Er,
            "lineEdit_urine_Le": self.lineEdit_urine_Le,
            "lineEdit_urine_aceton": self.lineEdit_urine_aceton,
            "lineEdit_urine_cilindr": self.lineEdit_urine_cilindr,
            "lineEdit_urine_color": self.lineEdit_urine_color,
            "lineEdit_urine_epit_pl": self.lineEdit_urine_epit_pl,
            "lineEdit_urine_epit_ren": self.lineEdit_urine_epit_ren,
            "lineEdit_urine_epit_zern": self.lineEdit_urine_epit_zern,
            "lineEdit_urine_gluc": self.lineEdit_urine_gluc,
            "lineEdit_urine_light": self.lineEdit_urine_light,
            "lineEdit_urine_other": self.lineEdit_urine_other,
            "lineEdit_urine_other_r": self.lineEdit_urine_other_r,
            "lineEdit_urine_protein": self.lineEdit_urine_protein,
            "lineEdit_urine_salt": self.lineEdit_urine_salt,
            "lineEdit_urine_slime": self.lineEdit_urine_slime,
            "dateEdit_OAK": self.dateEdit_OAK,
            "dateEdit_OAM": self.dateEdit_OAM,
            "pushButton_add_OAK": self.pushButton_add_OAK,
            "pushButton_add_OAM": self.pushButton_add_OAM,
            "dateEdit_BhAK": self.dateEdit_BhAK,
            "label_BhAK_report": self.label_BhAK_report,
            "label_LSp_lpnp": self.label_LSp_lpnp,
            "label_LSp_lponp": self.label_LSp_lponp,
            "label_LSp_lpvp": self.label_LSp_lpvp,
            "label_LSp_triglic": self.label_LSp_triglic,
            "label_bh_Bilirubin_main": self.label_bh_Bilirubin_main,
            "label_bh_Bilirubin_svyaz": self.label_bh_Bilirubin_svyaz,
            "label_bh_alt": self.label_bh_alt,
            "label_bh_ast": self.label_bh_ast,
            "label_bh_creatinin": self.label_bh_creatinin,
            "label_bh_gluc": self.label_bh_gluc,
            "label_bh_holesterin": self.label_bh_holesterin,
            "label_bh_mochevina": self.label_bh_mochevina,
            "label_bh_protein": self.label_bh_protein,
            "label_lipid_spectr": self.label_lipid_spectr,
            "lineEdit_LSp_lpnp": self.lineEdit_LSp_lpnp,
            "lineEdit_LSp_lponp": self.lineEdit_LSp_lponp,
            "lineEdit_LSp_lpvp": self.lineEdit_LSp_lpvp,
            "lineEdit_LSp_triglic": self.lineEdit_LSp_triglic,
            "lineEdit_bh_Bilirubin_main": self.lineEdit_bh_Bilirubin_main,
            "lineEdit_bh_Bilirubin_svyaz": self.lineEdit_bh_Bilirubin_svyaz,
            "lineEdit_bh_alt": self.lineEdit_bh_alt,
            "lineEdit_bh_ast": self.lineEdit_bh_ast,
            "lineEdit_bh_creatinin": self.lineEdit_bh_creatinin,
            "lineEdit_bh_gluc": self.lineEdit_bh_gluc,
            "lineEdit_bh_holesterin": self.lineEdit_bh_holesterin,
            "lineEdit_bh_mochevina": self.lineEdit_bh_mochevina,
            "lineEdit_bh_other_1": self.lineEdit_bh_other_1,
            "lineEdit_bh_other_2": self.lineEdit_bh_other_2,
            "lineEdit_bh_other_3": self.lineEdit_bh_other_3,
            "lineEdit_bh_other_r_1": self.lineEdit_bh_other_r_1,
            "lineEdit_bh_other_r_2": self.lineEdit_bh_other_r_2,
            "lineEdit_bh_other_r_3": self.lineEdit_bh_other_r_3,
            "lineEdit_bh_protein": self.lineEdit_bh_protein,
            "pushButton_add_BhAK": self.pushButton_add_BhAK,
            "dateEdit_GlucPr": self.dateEdit_GlucPr,
            "label_GlucPr_report": self.label_GlucPr_report,
            "label_glucprof_08_00": self.label_glucprof_08_00,
            "label_glucprof_13_30": self.label_glucprof_13_30,
            "label_glucprof_17_30": self.label_glucprof_17_30,
            "label_glucprof_21_00": self.label_glucprof_21_00,
            "lineEdit_glucprof_08_00": self.lineEdit_glucprof_08_00,
            "lineEdit_glucprof_13_30": self.lineEdit_glucprof_13_30,
            "lineEdit_glucprof_17_30": self.lineEdit_glucprof_17_30,
            "lineEdit_glucprof_21_00": self.lineEdit_glucprof_21_00,
            "pushButton_add_GlucPr": self.pushButton_add_GlucPr,
            "comboBox_mylab_template": self.comboBox_mylab_template,
            "dateEdit_my_lab": self.dateEdit_my_lab,
            "label_my_lab_report": self.label_my_lab_report,
            "label_my_lab_template": self.label_my_lab_template,
            "lineEdit_my_lab_1": self.lineEdit_my_lab_1,
            "lineEdit_my_lab_2": self.lineEdit_my_lab_2,
            "lineEdit_my_lab_3": self.lineEdit_my_lab_3,
            "lineEdit_my_lab_4": self.lineEdit_my_lab_4,
            "lineEdit_my_lab_5": self.lineEdit_my_lab_5,
            "lineEdit_my_lab_6": self.lineEdit_my_lab_6,
            "lineEdit_my_lab_7": self.lineEdit_my_lab_7,
            "lineEdit_my_lab_8": self.lineEdit_my_lab_8,
            "lineEdit_my_lab_name": self.lineEdit_my_lab_name,
            "lineEdit_my_lab_r_1": self.lineEdit_my_lab_r_1,
            "lineEdit_my_lab_r_2": self.lineEdit_my_lab_r_2,
            "lineEdit_my_lab_r_3": self.lineEdit_my_lab_r_3,
            "lineEdit_my_lab_r_4": self.lineEdit_my_lab_r_4,
            "lineEdit_my_lab_r_5": self.lineEdit_my_lab_r_5,
            "lineEdit_my_lab_r_6": self.lineEdit_my_lab_r_6,
            "lineEdit_my_lab_r_7": self.lineEdit_my_lab_r_7,
            "lineEdit_my_lab_r_8": self.lineEdit_my_lab_r_8,
            "lineEdit_mylab_template": self.lineEdit_mylab_template,
            "pushButton_add_mylab": self.pushButton_add_mylab,
            "pushButton_insert_mylab_template": self.pushButton_insert_mylab_template,
            "pushButton_mylab_clean": self.pushButton_mylab_clean,
            "pushButton_save_mylab_template": self.pushButton_save_mylab_template,
            "textEdit_lab_result": self.textEdit_lab_result
        }

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonNotSaveExit\
            .clicked.connect(self.exit)
        self.pushButtonSaveExit\
            .clicked.connect(self.exit_and_save)
        self.pushButton_add_OAK\
            .clicked.connect(self.write_OAK)
        self.pushButton_add_OAM\
            .clicked.connect(self.write_OAM)
        self.pushButton_add_BhAK\
            .clicked.connect(self.write_BhAK)
        self.pushButton_add_GlucPr\
            .clicked.connect(self.write_GlucPr)
        self.pushButton_add_mylab\
            .clicked.connect(self.write_mylab)
        self.pushButton_mylab_clean\
            .clicked.connect(self.clean_mylab)
        self.pushButton_insert_mylab_template\
            .clicked.connect(self.insert_mylab_template)
        self.pushButton_save_mylab_template\
            .clicked.connect(self.save_my_lab_template)

        self.checkBox_mylab.stateChanged.connect(self.set_new_tmpl_name)
        self.lineEdit_my_lab_name.textChanged.connect(self.set_new_tmpl_name)

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def insert_data_from_dictionary(self):
        if 'лабораторные_данные' in self.d:
            self.textEdit_lab_result.setText(self.d['лабораторные_данные'])

    def write_to_dictionary(self):
        '''
        '''
        text = self.textEdit_lab_result.toPlainText()
        if text:
            self.d['лабораторные_данные'] = text.strip()

    def set_styles(self):
        pass

    def write_OAK(self):
        '''
        '''
        empty = True
        check_list = (
            "lineEdit_Er",
            "lineEdit_Hb",
            "lineEdit_color",
            "lineEdit_Ht",
            "lineEdit_Le",
            "lineEdit_Le_B",
            "lineEdit_Le_Eoz",
            "lineEdit_Le_N_yu",
            "lineEdit_Le_N_p",
            "lineEdit_Le_N_s",
            "lineEdit_Le_M",
            "lineEdit_Le_Lym",
            "lineEdit_Tr",
            "lineEdit_soe",
            "lineEdit_OAK_other")

        for i in check_list:
            if i != "lineEdit_OAK_other":
                if self.widget[i].text() != '':
                    empty = False
                    self.d_temp[f'label{i[8:]}'] =\
                        self.widget[f'label{i[8:]}'].text()
                    self.d_temp[i] = self.widget[i].text()
                    self.widget[i].setText('')
            else:
                if self.widget[i].text() != '':
                    empty = False
                    self.d_temp[i] = self.widget[i].text()
                    self.d_temp[f'{i}_r'] = self.widget[f'{i}_r'].text()
                    self.widget[i].setText('')
                    self.widget[f'{i}_r'].setText('')

        if not empty:
            self.d_temp['dateEdit_OAK'] =\
                self.widget['dateEdit_OAK'].dateTime().toString('dd.MM.yyyy')

            if 'лабораторные_данные' not in self.d:
                self.d['лабораторные_данные'] = forming('oak', self.d_temp)
                self.widget['textEdit_lab_result']\
                    .setText(self.d['лабораторные_данные'])
            else:
                result = f"{self.textEdit_lab_result.toPlainText()}"\
                         f"{forming('oak', self.d_temp)}"
                self.widget['textEdit_lab_result'].setText(result)
                self.d['лабораторные_данные'] = result

            self.label_OAK_report.setText(
                f"ОАК от {self.d_temp['dateEdit_OAK']} добавлен.")

        self.d_temp = {}

    def write_OAM(self):
        '''
        '''
        empty = True
        check_list = (
            "lineEdit_urine_color",
            "lineEdit_urine_light",
            "lineEdit_udel_ves",
            "lineEdit_urine_protein",
            "lineEdit_urine_gluc",
            "lineEdit_urine_aceton",
            "lineEdit_urine_Le",
            "lineEdit_urine_Er",
            "lineEdit_urine_epit_pl",
            "lineEdit_urine_epit_zern",
            "lineEdit_urine_epit_ren",
            "lineEdit_urine_cilindr",
            "lineEdit_urine_salt",
            "lineEdit_urine_slime",
            "lineEdit_urine_Bacteria",
            "lineEdit_urine_other")

        for i in check_list:
            if i != "lineEdit_urine_other":
                if self.widget[i].text() != '':
                    empty = False
                    self.d_temp[f'label{i[8:]}'] =\
                        self.widget[f'label{i[8:]}'].text()
                    self.d_temp[i] = self.widget[i].text()
                    self.widget[i].setText('')
            else:
                if self.widget[i].text() != '':
                    empty = False
                    self.d_temp[i] = self.widget[i].text()
                    self.d_temp[f'{i}_r'] = self.widget[f"{i}_r"].text()
                    self.widget[i].setText('')
                    self.widget[f'{i}_r'].setText('')

        if not empty:
            self.d_temp['dateEdit_OAM'] =\
                self.widget['dateEdit_OAM'].dateTime().toString('dd.MM.yyyy')

            if 'лабораторные_данные' not in self.d:
                self.d['лабораторные_данные'] = forming('oam', self.d_temp)
                self.widget['textEdit_lab_result']\
                    .setText(self.d['лабораторные_данные'])
            else:
                result = f"{self.textEdit_lab_result.toPlainText()}"\
                         f"{forming('oam', self.d_temp)}"
                self.widget['textEdit_lab_result'].setText(result)
                self.d['лабораторные_данные'] = result

            self.label_OAM_report.setText(
                f"ОАМ от {self.d_temp['dateEdit_OAM']} добавлен.")

        self.d_temp = {}

    def write_BhAK(self):
        empty = True
        check_list = (
            "lineEdit_bh_gluc",
            "lineEdit_bh_protein",
            "lineEdit_bh_alt",
            "lineEdit_bh_ast",
            "lineEdit_bh_Bilirubin_main",
            "lineEdit_bh_Bilirubin_svyaz",
            "lineEdit_bh_creatinin",
            "lineEdit_bh_mochevina",
            "lineEdit_bh_other_1",
            "lineEdit_bh_other_2",
            "lineEdit_bh_other_3",
            "lineEdit_bh_holesterin",
            "lineEdit_LSp_lpnp",
            "lineEdit_LSp_lponp",
            "lineEdit_LSp_lpvp",
            "lineEdit_LSp_triglic",)

        for i in check_list:
            if i not in ("lineEdit_bh_other_1",
                         "lineEdit_bh_other_2",
                         "lineEdit_bh_other_3"):
                if self.widget[i].text() != '':
                    empty = False
                    self.d_temp[f'label{i[8:]}'] =\
                        self.widget[f'label{i[8:]}'].text()
                    self.d_temp[i] = self.widget[i].text()
                    self.widget[i].setText('')
            else:
                if self.widget[i].text() != '':
                    empty = False
                    self.d_temp[i] = self.widget[i].text()
                    self.d_temp[f'{i[:-1]}r_{i[-1]}'] =\
                        self.widget[f'{i[:-1]}r_{i[-1]}'].text()
                    self.widget[i].setText('')
                    self.widget[f'{i[:-1]}r_{i[-1]}'].setText('')

        if not empty:
            self.d_temp['dateEdit_BhAK'] =\
                self.widget['dateEdit_BhAK'].dateTime().toString('dd.MM.yyyy')

            if 'лабораторные_данные' not in self.d:
                self.d['лабораторные_данные'] = forming('bh', self.d_temp)
                self.widget['textEdit_lab_result']\
                    .setText(self.d['лабораторные_данные'])
            else:
                result = f"{self.textEdit_lab_result.toPlainText()}"\
                         f"{forming('bh', self.d_temp)}"
                self.widget['textEdit_lab_result'].setText(result)
                self.d['лабораторные_данные'] = result

            msg = f"Б/х анализ крови от "\
                  f"{self.d_temp['dateEdit_BhAK']} добавлен."
            self.label_BhAK_report.setText(msg)

        self.d_temp = {}

    def write_GlucPr(self):
        empty = True
        check_list = (
            "lineEdit_glucprof_08_00",
            "lineEdit_glucprof_17_30",
            "lineEdit_glucprof_13_30",
            "lineEdit_glucprof_21_00")

        for i in check_list:
            if self.widget[i].text() != '':
                empty = False
                self.d_temp[f'label{i[8:]}'] =\
                    self.widget[f'label{i[8:]}'].text()
                self.d_temp[i] = self.widget[i].text()
                self.widget[i].setText('')

        if not empty:
            self.d_temp['dateEdit_GlucPr'] =\
                self.widget['dateEdit_GlucPr']\
                    .dateTime().toString('dd.MM.yyyy')
            self.d_temp['plainTextEdit_glucprof'] =\
                self.plainTextEdit_glucprof.toPlainText()
            self.plainTextEdit_glucprof.setPlainText('')

            if 'лабораторные_данные' not in self.d:
                self.d['лабораторные_данные'] =\
                    forming('glucprof', self.d_temp)
                self.widget['textEdit_lab_result']\
                    .setText(self.d['лабораторные_данные'])
            else:
                result = f"{self.textEdit_lab_result.toPlainText()}"\
                         f"{forming('glucprof', self.d_temp)}"
                self.widget['textEdit_lab_result'].setText(result)
                self.d['лабораторные_данные'] = result

            msg = f"Гликемический профиль от "\
                  f"{self.d_temp['dateEdit_GlucPr']} добавлен."
            self.label_GlucPr_report.setText(msg)

        self.d_temp = {}

    def write_mylab(self):
        empty = True

        for i in range(1, 9):
            if (a := self.widget[f'lineEdit_my_lab_{i}'].text()) != '':
                if (b := self.widget[f'lineEdit_my_lab_r_{i}'].text()) != '':
                    empty = False
                    self.d_temp[f'mylab_{i}'] = a
                    self.d_temp[f'mylab_r_{i}'] = b

        if not empty:
            self.d_temp["mylab_date"] =\
                self.widget["dateEdit_my_lab"]\
                    .dateTime().toString('dd.MM.yyyy')
            self.d_temp["mylab_name"] =\
                self.widget["lineEdit_my_lab_name"].text()

            if 'лабораторные_данные' not in self.d:
                self.d['лабораторные_данные'] = forming('my_lab', self.d_temp)
                self.widget['textEdit_lab_result']\
                    .setText(self.d['лабораторные_данные'])
            else:
                result = f"{self.textEdit_lab_result.toPlainText()}"\
                         f"{forming('my_lab', self.d_temp)}"
                self.widget['textEdit_lab_result'].setText(result)
                self.d['лабораторные_данные'] = result
            msg = f'{self.d_temp["mylab_name"]} от '\
                  f'{self.d_temp["mylab_date"]} добавлен.'
            self.label_my_lab_report.setText(msg)

        self.clean_mylab()
        self.d_temp = {}

    def clean_mylab(self):
        self.widget["lineEdit_my_lab_name"].setText('')
        self.widget["dateEdit_my_lab"].setDate(
            QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
        for i in range(1, 9):
            self.widget[f'lineEdit_my_lab_{i}'].setText('')
            self.widget[f'lineEdit_my_lab_r_{i}'].setText('')

    def insert_mylab_template(self):
        self.clean_mylab()
        name = self.comboBox_mylab_template.currentText()

        if name != '':
            lab_name = self.templates[name]['mylab_name']
            self.widget["lineEdit_my_lab_name"].setText(lab_name)
            for i in range(1, 9):
                self.widget[f'lineEdit_my_lab_{i}']\
                    .setText(self.templates[name][f'mylab_{i}'])

    def save_my_lab_template(self):
        if (name_tpl := self.lineEdit_mylab_template.text()) != '':
            dict_ = {}
            dict_['mylab_name'] = self.widget["lineEdit_my_lab_name"].text()
            for i in range(1, 9):
                dict_[f'mylab_{i}'] =\
                    self.widget[f'lineEdit_my_lab_{i}'].text()
            self.templates[f'{name_tpl}'] = dict_
            templates_file = 'lab_templates'
            templates_json_recording(templates=self.templates,
                                     templates_name=templates_file)
            # загружаем в бакет
            upload_templates_json_from_yandex_cloud_bucket(templates_file)
            self.set_templates_list()
            self.lineEdit_mylab_template.setText('')
            self.clean_mylab()

    def set_new_tmpl_name(self):
        if self.checkBox_mylab.isChecked():
            self.lineEdit_mylab_template\
                .setText(self.lineEdit_my_lab_name.text())
            self.lineEdit_mylab_template.setEnabled(False)
        else:
            self.lineEdit_mylab_template.setText('')
            self.lineEdit_mylab_template.setEnabled(True)
