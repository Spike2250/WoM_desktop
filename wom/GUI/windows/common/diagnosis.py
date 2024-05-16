from PySide6 import QtWidgets

from wom.GUI.PY.common import Diagnosis
from wom.app_logic.db_func\
    .bucket_func import upload_history_to_yandex_cloud_bucket
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.writing.postprocessing\
    .diagnosis import update_after_diagnosis


class Ui_Diagnosis(QtWidgets.QWidget, Diagnosis.Ui_Diagnosis):
    def __init__(self, user_info, windows, main_win,
                 dictionary, case_type, timeline):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.case_type = case_type
        self.timeline = timeline

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Клинический диагноз"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.define_ending()

        self.set_connections()
        self.set_patient_info()
        self.insert_data_from_dictionary()
        self.activate_VAS_boxes()
        self.set_styles()

    def onButtonMy(self):
        pass

    def define_ending(self):
        if self.timeline == 'adm':
            self.end = ''
            self.label_adm_or_dis.setText('при\nпоступлении')
        elif self.timeline == 'dis':
            self.end = '_вып'
            self.label_adm_or_dis.setText('при\nвыписке')
            self.label_diagnosis.setText('Диагноз при выписке')

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        # коннекты событий
        self.checkBoxPainCheck.stateChanged.connect(self.activate_VAS_boxes)

    def activate_VAS_boxes(self):
        if self.checkBoxPainCheck.isChecked():
            self.comboBoxDiagnosisFS_VAS_1.setEnabled(True)
            self.comboBoxDiagnosisFS_VAS_2.setEnabled(True)
        else:
            self.comboBoxDiagnosisFS_VAS_1.setEnabled(False)
            self.comboBoxDiagnosisFS_VAS_2.setEnabled(False)
            self.comboBoxDiagnosisFS_VAS_1.setCurrentText('0')
            self.comboBoxDiagnosisFS_VAS_2.setCurrentText('0')

    def insert_data_from_dictionary(self):
        def insert_scales():
            self.checkBoxPainCheck.setChecked(self.d['наличие_боли'])
            self.comboBoxDiagnosisFS_RRS_1.setCurrentText(self.d['ШРМ'])
            self.comboBoxDiagnosisFS_mRs_1.setCurrentText(self.d['mRs'])
            self.comboBoxDiagnosisFS_IMR_1.setCurrentText(self.d['IMR'])
            self.comboBoxDiagnosisFS_Hauser_1.setCurrentText(self.d['хаузер'])
            self.comboBoxDiagnosisFS_VAS_1.setCurrentText(self.d['VAS'])
            self.comboBoxDiagnosisFS_RRS_2.setCurrentText(self.d['ШРМ_вып'])
            self.comboBoxDiagnosisFS_mRs_2.setCurrentText(self.d['mRs_вып'])
            self.comboBoxDiagnosisFS_IMR_2.setCurrentText(self.d['IMR_вып'])
            self.comboBoxDiagnosisFS_Hauser_2.setCurrentText(self.d['хаузер_вып'])  # noqa: E501
            self.comboBoxDiagnosisFS_VAS_2.setCurrentText(self.d['VAS_вып'])
            if 'NIHSS' in self.d:
                self.comboBoxDiagnosisFS_NIHSS.setCurrentText(self.d['NIHSS'])

        # заполнение данных, если они уже есть
        if f'Основной_диагноз{self.end}' in self.d:
            self.plainTextEditPtDiagnosisMain\
                .setPlainText(self.d[f'Основной_диагноз{self.end}'])
            self.plainTextEditPtDiagnosisConcomitant\
                .setPlainText(self.d[f'Сопутствующий_диагноз{self.end}'])
            insert_scales()
        elif 'Основной_диагноз' in self.d:
            self.plainTextEditPtDiagnosisMain\
                .setPlainText(self.d['Основной_диагноз'])
            self.plainTextEditPtDiagnosisConcomitant\
                .setPlainText(self.d['Сопутствующий_диагноз'])
            insert_scales()
        elif 'Сопутствующий_диагноз' in self.d:
            self.plainTextEditPtDiagnosisConcomitant\
                .setPlainText(self.d['Сопутствующий_диагноз'])

    def write_to_dictionary(self):
        self.d[f'Основной_диагноз{self.end}'] = self\
            .plainTextEditPtDiagnosisMain.toPlainText()
        self.d[f'Сопутствующий_диагноз{self.end}'] = self\
            .plainTextEditPtDiagnosisConcomitant.toPlainText()
        self.d['ШРМ'] = self.comboBoxDiagnosisFS_RRS_1.currentText()
        self.d['mRs'] = self.comboBoxDiagnosisFS_mRs_1 .currentText()
        self.d['IMR'] = self.comboBoxDiagnosisFS_IMR_1.currentText()
        self.d['хаузер'] = self.comboBoxDiagnosisFS_Hauser_1.currentText()
        self.d['VAS'] = self.comboBoxDiagnosisFS_VAS_1.currentText()
        self.d['наличие_боли'] = self.checkBoxPainCheck.isChecked()
        self.d['ШРМ_вып'] = self.comboBoxDiagnosisFS_RRS_2.currentText()
        self.d['mRs_вып'] = self.comboBoxDiagnosisFS_mRs_2.currentText()
        self.d['IMR_вып'] = self.comboBoxDiagnosisFS_IMR_2.currentText()
        self.d['хаузер_вып'] = self.comboBoxDiagnosisFS_Hauser_2.currentText()
        self.d['VAS_вып'] = self.comboBoxDiagnosisFS_VAS_2.currentText()
        self.d['NIHSS'] = self.comboBoxDiagnosisFS_NIHSS.currentText()
        update_after_diagnosis(self.d)

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

    def set_styles(self):
        pass
