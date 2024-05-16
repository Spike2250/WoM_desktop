from PySide6 import QtWidgets, QtCore

from wom.GUI.PY.common import StObj_admition
from wom.app_logic.db_func\
    .db_st_obj_templates import (read_db_obj_template_list,
                                 read_db_obj_template_data,
                                 insert_obj_template_into_db,
                                 update_obj_template_db)
from wom.app_logic.db_func\
    .bucket_func import (upload_history_to_yandex_cloud_bucket,
                         upload_templates_db_from_yandex_cloud_bucket,
                         download_templates_db_from_yandex_cloud_bucket,
                         upload_templates_json_from_yandex_cloud_bucket,
                         download_templates_json_from_yandex_cloud_bucket)
from wom.app_logic.db_func\
    .json_templates import (read_templates,
                            templates_json_recording)
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.service_func import calc_BMI
from wom.app_logic.writing.postprocessing.obj_st import update_after_obj_st
from wom.app_logic.writing.diaries.gen import create_random_set


class Ui_StPrObjectivus_admission(QtWidgets.QWidget,
                                  StObj_admition.Ui_StObj):
    def __init__(self, user_info, windows, main_win, dictionary, case_type):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.case_type = case_type

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Жалобы, анамнез, данные по ЛН, "\
              "соматический статус"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_patient_info()
        self.set_templates_list()
        self.set_templates_list_jaloby()
        self.insert_data_from_dictionary()
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

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonNotSaveExit\
            .clicked.connect(self.exit)
        self.pushButtonSaveExit\
            .clicked.connect(self.exit_and_save)
        self.pushButton_add_to_diag\
            .clicked.connect(self.add_to_diagnosis)
        self.pushButton_random_values\
            .clicked.connect(self.set_random_values)
        self.pushButtonAddNewTemplate_jaloby\
            .clicked.connect(self.add_new_template_jaloby)
        self.pushButton_push_temp_jaloby\
            .clicked.connect(self.push_active_template_jaloby)
        self.pushButtonAddNewTemplateGeneralSt\
            .clicked.connect(self.add_new_template_obj_st)
        self.pushButton_push_temp\
            .clicked.connect(self.push_active_template)
        # коннекты зависимостей
        self.lineEditPtGrowth\
            .textChanged.connect(self.count_imt)
        self.lineEditPtWeight\
            .textChanged.connect(self.count_imt)
        self.plainTextEditPtDrugs\
            .textChanged.connect(self.change_drugs_combobox)
        self.plainTextEditPtAnamEpid\
            .textChanged.connect(self.change_anam_epid_combobox)
        self.plainTextEditPtAnamAllerg\
            .textChanged.connect(self.change_anam_aller_combobox)
        self.checkBoxPtNeedSickList\
            .stateChanged.connect(self.activate_first_ln_box)
        self.checkBoxPtNeedSickList_2\
            .stateChanged.connect(self.form_first_ln_data)

    def activate_first_ln_box(self):
        if self.checkBoxPtNeedSickList.isChecked():
            self.checkBoxPtNeedSickList_2.setEnabled(True)
            self.comboBoxWorkListInfo.setCurrentText('находится на ЛН')
        else:
            self.checkBoxPtNeedSickList_2.setChecked(False)
            self.checkBoxPtNeedSickList_2.setEnabled(False)

    def form_first_ln_data(self):
        if self.checkBoxPtNeedSickList_2.isChecked():
            self.comboBoxWorkListInfo\
                .setCurrentText('нуждается в первичном ЛН')
            self.lineEditPtWorkListNumber1_1\
                .setText('Первичный ЛН')
            self.lineEditPtWorkListNumber_issued\
                .setText('ГБУЗ ПК ПККГВВ')
            self.dateEditPtWorkListDate1_1\
                .setDate(QtCore.QDate.fromString(
                    self.d['дата_поступления'], "dd.MM.yyyy"))
            self.dateEditPtWorkListDate1_2\
                .setDate(QtCore.QDate.fromString(
                    self.d['дата_выписки'], "dd.MM.yyyy"))
            self.dateEditPtWorkListDateOpening\
                .setDate(QtCore.QDate.fromString(
                    self.d['дата_поступления'], "dd.MM.yyyy"))
            self.comboBoxWorkList_prognosis\
                .setCurrentText('Относительно благоприятный')
        else:
            if 'Соматический_статус' in self.d:
                self.comboBoxWorkListInfo\
                    .setCurrentText(self.d['ЛН_инфо_нужда'])
                if 'ЛН_выдан_ЛПУ' in self.d:
                    self.lineEditPtWorkListNumber_issued\
                        .setText(self.d['ЛН_выдан_ЛПУ'])
                    self.comboBoxWorkList_prognosis\
                        .setCurrentText(self.d['трудовой_прогноз'])
                self.lineEditPtWorkListNumber1_1\
                    .setText(self.d['ЛН_номер_1'])
                self.dateEditPtWorkListDate1_1\
                    .setDate(QtCore.QDate.fromString(
                        self.d['С_какого_числа_ЛН_на_руках'], "dd.MM.yyyy"))
                self.dateEditPtWorkListDate1_2\
                    .setDate(QtCore.QDate.fromString(
                        self.d['По_какое_число_продлен_ЛН'], "dd.MM.yyyy"))
                self.dateEditPtWorkListDateOpening\
                    .setDate(QtCore.QDate.fromString(
                        self.d['первичный_лн'], "dd.MM.yyyy"))
            else:
                self.comboBoxWorkListInfo.setCurrentText('находится на ЛН')
                self.lineEditPtWorkListNumber1_1.setText('')
                self.lineEditPtWorkListNumber_issued.setText('')
                self.dateEditPtWorkListDate1_1\
                    .setDate(QtCore.QDate.fromString(
                        "01.01.2000", "dd.MM.yyyy"))
                self.dateEditPtWorkListDate1_2\
                    .setDate(QtCore.QDate.fromString(
                        "01.01.2000", "dd.MM.yyyy"))
                self.dateEditPtWorkListDateOpening\
                    .setDate(QtCore.QDate.fromString(
                        "01.01.2000", "dd.MM.yyyy"))
                self.comboBoxWorkList_prognosis.setCurrentText('')

    # @download_templates_db_from_yandex_cloud_bucket('default_templates')
    def set_templates_list(self):
        self.templates_list = read_db_obj_template_list()
        self.comboBoxGeneralStTemplate.clear()
        if len(self.templates_list) <= 1:
            self.comboBoxGeneralStTemplate.addItem(self.templates_list[0])
        else:
            self.comboBoxGeneralStTemplate.addItems(self.templates_list)

    # @download_templates_json_from_yandex_cloud_bucket('complaints')
    def set_templates_list_jaloby(self):
        self.complaints_templates = read_templates('complaints')
        if self.complaints_templates is not None:
            templates_list = sorted(list(self.complaints_templates))
            self.comboBox_jaloby_templates.clear()
            self.comboBox_jaloby_templates.addItem('')
            self.comboBox_jaloby_templates.addItems(templates_list)
        else:
            self.complaints_templates = {}
            self.comboBox_jaloby_templates.clear()

    def insert_data_from_dictionary(self):
        # Заполнение всех ячеек данными, если они уже есть
        if 'Соматический_статус' in self.d:
            # Анамнез
            self.plainTextEditPtAnamMorbi.setPlainText(self.d['анамнез'])
            self.comboBoxPtSocialStatus\
                .setCurrentText(self.d['социальный_статус'])
            self.checkBoxPtNeedSickList.setChecked(self.d['нужда_в_ЛН'])
            if (x := 'нужда_в_ЛН_первич') in self.d:
                self.checkBoxPtNeedSickList_2.setChecked(self.d[x])
            self.comboBoxWorkListInfo.setCurrentText(self.d['ЛН_инфо_нужда'])
            self.lineEditPtWorkPlace.setText(self.d['место_работы_1'])
            self.lineEditPtWorkPosition.setText(self.d['должность_1'])
            if 'ЛН_выдан_ЛПУ' in self.d:
                self.lineEditPtWorkListNumber_issued\
                    .setText(self.d['ЛН_выдан_ЛПУ'])
                self.comboBoxWorkList_prognosis\
                    .setCurrentText(self.d['трудовой_прогноз'])
            self.lineEditPtWorkListNumber1_1\
                .setText(self.d['ЛН_номер_1'])
            self.dateEditPtWorkListDate1_1.setDate(QtCore.QDate.fromString(
                self.d.get('С_какого_числа_ЛН_на_руках', '01.01.2000'), "dd.MM.yyyy"))  # noqa: E501
            self.dateEditPtWorkListDate1_2.setDate(QtCore.QDate.fromString(
                self.d.get('По_какое_число_продлен_ЛН', '01.01.2000'), "dd.MM.yyyy"))  # noqa: E501
            self.dateEditPtWorkListDateOpening.setDate(QtCore.QDate.fromString(
                self.d.get('первичный_лн', '01.01.2000'), "dd.MM.yyyy"))
            self.comboBoxPtAllergStatus.setCurrentText(self.d['аллергия_чек'])
            self.plainTextEditPtAnamAllerg.setPlainText(self.d['аллергия'])
            self.comboBoxPtAnamEpid.setCurrentText(self.d['эпид_анамнез_чек'])
            self.plainTextEditPtAnamEpid.setPlainText(self.d['эпид_анамнез'])
            self.checkBox_GB.setChecked(self.d['ГБ_чек'])
            self.checkBox_SD.setChecked(self.d['СД_чек'])
            self.checkBox_NRS.setChecked(self.d['НРС_чек'])
            self.checkBox_IBS.setChecked(self.d['ИБС_чек'])
            self.checkBox_Stroke.setChecked(self.d['ПОНМК_чек'])
            self.checkBox_Fat.setChecked(self.d['Ожирение_чек'])
            self.checkBox_Hypothyreosis.setChecked(self.d['Гипотиреоз_чек'])
            self.checkBox_Hyperthyreosis.setChecked(self.d['Гипертиреоз_чек'])
            self.checkBox_Gastro.setChecked(self.d['Гастрит_чек'])
            self.checkBox_B20.setChecked(self.d['ВИЧ_чек'])
            self.checkBox_HCV.setChecked(self.d['ВГС_чек'])
            self.checkBox_HBsAg.setChecked(self.d['ВГБ_чек'])
            self.checkBox_Astma.setChecked(self.d['Астма_чек'])
            self.checkBox_Atherosclerosis_legs.setChecked(self.d['ХАН_чек'])
            self.checkBox_Atherosclerosis_BCA.setChecked(self.d['БЦА_чек'])
            self.checkBox_other.setChecked(self.d['Другие_сопут_чек'])
            self.plainTextEdit_other_chronic_diseases\
                .setPlainText(self.d['Другие_сопут'])
            self.comboBoxPtDrugs\
                .setCurrentText(self.d['принимает_медикаменты_чек'])
            self.plainTextEditPtDrugs\
                .setPlainText(self.d['принимает_медикаменты'])
            # жалобы и числовые данные
            self.plainTextEditPtComplaints.setPlainText(self.d['жалобы'])
            self.lineEditPtGrowth.setText(str(self.d['рост']))
            self.lineEditPtWeight.setText(str(self.d['вес']))
            self.lineEditPtBreathingSpeed.setText(str(self.d['ЧДД']))
            self.lineEditPtBloodPreasureSist.setText(str(self.d['АД_сист']))
            self.lineEditPtBloodPreasureDiast.setText(str(self.d['АД_диаст']))
            self.lineEditPtPulse.setText(str(self.d['ЧСС']))
            self.lineEditPtTemperature.setText(str(self.d['Температура']))
            self.lineEditSaturation.setText(str(self.d['Сатурация']))
            # Общий статус
            self.comboBoxPtGeneralState.setCurrentText(
                self.d['Общее_состояние'])
            self.comboBoxPtSkinState_1.setCurrentText(self.d['кожа'])
            self.comboBoxPtSkinState_2.setCurrentText(self.d['высыпания'])
            self.comboBoxPtLymphnode.setCurrentText(self.d['лимфоузлы'])
            self.comboBoxPtMucousMembr_1.setCurrentText(self.d['слизистые'])
            self.comboBoxPtBreathing_1.setCurrentText(self.d['дыхание_1'])
            self.comboBoxPtBreathing_2.setCurrentText(self.d['дыхание_2'])
            self.comboBoxPtBreathing_3.setCurrentText(self.d['дыхание_3'])
            self.comboBoxPtWheezingChoice.setCurrentText(self.d['хрипы_чек'])
            self.comboBoxPtWheezing_1.setCurrentText(self.d['хрипы_1'])
            self.comboBoxPtWheezing_2.setCurrentText(self.d['хрипы_2'])
            self.comboBoxPtWheezing_3.setCurrentText(self.d['хрипы_3'])
            self.comboBoxPtDyspneaChoice.setCurrentText(self.d['одышка_чек'])
            self.comboBoxPtDyspnea_1.setCurrentText(self.d['одышка_1'])
            self.comboBoxPtDyspnea_2.setCurrentText(self.d['одышка_2'])
            self.comboBoxPtDyspnea_3.setCurrentText(self.d['одышка_3'])
            self.comboBoxPtHearthTone_1.setCurrentText(self.d['тоны_сердца_1'])
            self.comboBoxPtHearthTone_2.setCurrentText(self.d['тоны_сердца_2'])
            self.comboBoxPtHearthTone_3.setCurrentText(self.d['тоны_сердца_3'])
            self.comboBoxPtHearthNoiseChoice.setCurrentText(
                self.d['шумы_сердца_чек'])
            self.comboBoxPtHearthNoise.setCurrentText(self.d['шумы_сердца'])
            self.comboBoxPtStomach_1.setCurrentText(self.d['живот_1'])
            self.comboBoxPtStomach_2.setCurrentText(self.d['живот_2'])
            self.comboBoxPtStomach_3.setCurrentText(self.d['живот_3'])
            self.comboBoxPtDefecation_1.setCurrentText(self.d['стул_1'])
            self.comboBoxPtDefecation_2.setCurrentText(self.d['стул_2'])
            self.comboBoxPtDefecation_3.setCurrentText(self.d['стул_3'])
            self.comboBoxPtUrination_1.setCurrentText(
                self.d['Мочеиспускание_1'])
            self.comboBoxPtUrination_2.setCurrentText(
                self.d['Мочеиспускание_2'])
            self.comboBoxPtUrination_3.setCurrentText(
                self.d['Мочеиспускание_доп'])
            self.plainTextEditPtStObjOther.setPlainText(
                self.d['Общ_статус_дополнение'])
        else:
            if self.d['нужда_в_ЛН']:
                self.checkBoxPtNeedSickList.setChecked(self.d['нужда_в_ЛН'])
                self.comboBoxPtSocialStatus.setCurrentText(
                    'Работает, устроен официально')
                if (x := 'нужда_в_ЛН_первич') in self.d:
                    self.checkBoxPtNeedSickList_2.setChecked(self.d[x])
                    if self.d[x]:
                        self.comboBoxWorkListInfo.setCurrentText(
                            'нуждается в первичном ЛН')
                    else:
                        self.comboBoxWorkListInfo.setCurrentText(
                            'находится на ЛН')

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def write_to_dictionary(self):
        '''
        запись в словарь всех значений из виджетов
        '''
        # Анамнез
        self.d['анамнез'] = self.plainTextEditPtAnamMorbi.toPlainText()
        self.d['социальный_статус'] = self.comboBoxPtSocialStatus.currentText()
        self.d['нужда_в_ЛН'] = self.checkBoxPtNeedSickList.isChecked()
        self.d['нужда_в_ЛН_первич'] = self.checkBoxPtNeedSickList_2.isChecked()
        self.d['ЛН_инфо_нужда'] = self.comboBoxWorkListInfo.currentText()
        self.d['место_работы_1'] = self.lineEditPtWorkPlace.text()
        self.d['должность_1'] = self.lineEditPtWorkPosition.text()
        self.d['ЛН_выдан_ЛПУ'] = self.lineEditPtWorkListNumber_issued.text()
        self.d['ЛН_номер_1'] = self.lineEditPtWorkListNumber1_1.text()
        self.d['С_какого_числа_ЛН_на_руках'] = self.dateEditPtWorkListDate1_1\
            .dateTime().toString('dd.MM.yyyy')
        self.d['По_какое_число_продлен_ЛН'] = self.dateEditPtWorkListDate1_2\
            .dateTime().toString('dd.MM.yyyy')
        self.d['первичный_лн'] = self.dateEditPtWorkListDateOpening\
            .dateTime().toString('dd.MM.yyyy')
        self.d['трудовой_прогноз'] = self.comboBoxWorkList_prognosis\
            .currentText()
        self.d['аллергия_чек'] = self.comboBoxPtAllergStatus.currentText()
        self.d['аллергия'] = self.plainTextEditPtAnamAllerg.toPlainText()
        self.d['эпид_анамнез_чек'] = self.comboBoxPtAnamEpid.currentText()
        self.d['эпид_анамнез'] = self.plainTextEditPtAnamEpid.toPlainText()
        self.d['ГБ_чек'] = self.checkBox_GB.isChecked()
        self.d['СД_чек'] = self.checkBox_SD.isChecked()
        self.d['НРС_чек'] = self.checkBox_NRS.isChecked()
        self.d['ИБС_чек'] = self.checkBox_IBS.isChecked()
        self.d['ПОНМК_чек'] = self.checkBox_Stroke.isChecked()
        self.d['Ожирение_чек'] = self.checkBox_Fat.isChecked()
        self.d['Гипотиреоз_чек'] = self.checkBox_Hypothyreosis.isChecked()
        self.d['Гипертиреоз_чек'] = self.checkBox_Hyperthyreosis.isChecked()
        self.d['Гастрит_чек'] = self.checkBox_Gastro.isChecked()
        self.d['ВИЧ_чек'] = self.checkBox_B20.isChecked()
        self.d['ВГС_чек'] = self.checkBox_HCV.isChecked()
        self.d['ВГБ_чек'] = self.checkBox_HBsAg.isChecked()
        self.d['Астма_чек'] = self.checkBox_Astma.isChecked()
        self.d['ХАН_чек'] = self.checkBox_Atherosclerosis_legs.isChecked()
        self.d['БЦА_чек'] = self.checkBox_Atherosclerosis_BCA.isChecked()
        self.d['Другие_сопут_чек'] = self.checkBox_other.isChecked()
        self.d['Другие_сопут'] = self.plainTextEdit_other_chronic_diseases\
            .toPlainText()
        self.d['принимает_медикаменты_чек'] = self.comboBoxPtDrugs\
            .currentText()
        self.d['принимает_медикаменты'] = self.plainTextEditPtDrugs\
            .toPlainText()
        # жалобы и числовые данные
        self.d['жалобы'] = self.plainTextEditPtComplaints.toPlainText()
        self.d['рост'] = self.lineEditPtGrowth.text()
        self.d['вес'] = self.lineEditPtWeight.text()
        self.d['ЧДД'] = self.lineEditPtBreathingSpeed.text()
        self.d['АД_сист'] = self.lineEditPtBloodPreasureSist.text()
        self.d['АД_диаст'] = self.lineEditPtBloodPreasureDiast.text()
        self.d['ЧСС'] = self.lineEditPtPulse.text()
        self.d['Температура'] = self.lineEditPtTemperature.text()
        self.d['Сатурация'] = self.lineEditSaturation.text()
        # Общий статус
        self.d['Общее_состояние'] = self.comboBoxPtGeneralState.currentText()
        self.d['кожа'] = self.comboBoxPtSkinState_1.currentText()
        self.d['высыпания'] = self.comboBoxPtSkinState_2.currentText()
        self.d['лимфоузлы'] = self.comboBoxPtLymphnode.currentText()
        self.d['слизистые'] = self.comboBoxPtMucousMembr_1.currentText()
        self.d['дыхание_1'] = self.comboBoxPtBreathing_1.currentText()
        self.d['дыхание_2'] = self.comboBoxPtBreathing_2.currentText()
        self.d['дыхание_3'] = self.comboBoxPtBreathing_3.currentText()
        self.d['хрипы_чек'] = self.comboBoxPtWheezingChoice.currentText()
        self.d['хрипы_1'] = self.comboBoxPtWheezing_1.currentText()
        self.d['хрипы_2'] = self.comboBoxPtWheezing_2.currentText()
        self.d['хрипы_3'] = self.comboBoxPtWheezing_3.currentText()
        self.d['одышка_чек'] = self.comboBoxPtDyspneaChoice.currentText()
        self.d['одышка_1'] = self.comboBoxPtDyspnea_1.currentText()
        self.d['одышка_2'] = self.comboBoxPtDyspnea_2.currentText()
        self.d['одышка_3'] = self.comboBoxPtDyspnea_3.currentText()
        self.d['тоны_сердца_1'] = self.comboBoxPtHearthTone_1.currentText()
        self.d['тоны_сердца_2'] = self.comboBoxPtHearthTone_2.currentText()
        self.d['тоны_сердца_3'] = self.comboBoxPtHearthTone_3.currentText()
        self.d['шумы_сердца_чек'] = self.comboBoxPtHearthNoiseChoice\
            .currentText()
        self.d['шумы_сердца'] = self.comboBoxPtHearthNoise.currentText()
        self.d['живот_1'] = self.comboBoxPtStomach_1.currentText()
        self.d['живот_2'] = self.comboBoxPtStomach_2.currentText()
        self.d['живот_3'] = self.comboBoxPtStomach_3.currentText()
        self.d['стул_1'] = self.comboBoxPtDefecation_1.currentText()
        self.d['стул_2'] = self.comboBoxPtDefecation_2.currentText()
        self.d['стул_3'] = self.comboBoxPtDefecation_3.currentText()
        self.d['Мочеиспускание_1'] = self.comboBoxPtUrination_1.currentText()
        self.d['Мочеиспускание_2'] = self.comboBoxPtUrination_2.currentText()
        self.d['Мочеиспускание_доп'] = self.comboBoxPtUrination_3.currentText()
        self.d['Общ_статус_дополнение'] = self.plainTextEditPtStObjOther\
            .toPlainText()

        update_after_obj_st(self.d, 'первичный')

    def count_imt(self):
        growth = self.lineEditPtGrowth.text()
        weight = self.lineEditPtWeight.text()
        if (growth, weight) != '':
            try:
                growth, weight = int(growth), int(weight)
                imt, units, conclusion, questionDS = calc_BMI(growth, weight)
                self.label_imt.setText(conclusion)
                if questionDS:
                    self.pushButton_add_to_diag.setEnabled(True)
                    self.checkBox_Fat.setChecked(True)
                else:
                    self.pushButton_add_to_diag.setEnabled(False)
                    self.checkBox_Fat.setChecked(False)
            except ValueError:
                self.label_imt.setText('# ошибка при расчете ИМТ #')

    def add_to_diagnosis(self):
        if 'Сопутствующий_диагноз' not in self.d:
            self.d['Сопутствующий_диагноз'] = self.label_imt.text()
        else:
            length = len(text := self.label_imt.text())
            if len(self.d['Сопутствующий_диагноз']) >= length:
                if self.d['Сопутствующий_диагноз'][-length:] != text:
                    if self.d['Сопутствующий_диагноз'][-1] == ' ':
                        self.d['Сопутствующий_диагноз'] += text
                    else:
                        self.d['Сопутствующий_диагноз'] += f" {text}"
                    self.label_2.setText(
                        'Заключение добавлено в сопут. диагноз')
                else:
                    self.label_2.setText(
                        'Заключение уже было недавно добавлено')

    def change_drugs_combobox(self):
        if self.plainTextEditPtDrugs.toPlainText() != '':
            if self.comboBoxPtDrugs.currentText() == 'Не принимает':
                self.comboBoxPtDrugs.setCurrentText('Постоянно')
        else:
            if self.comboBoxPtDrugs.currentText() != 'Не принимает':
                self.comboBoxPtDrugs.setCurrentText('Не принимает')

    def change_anam_epid_combobox(self):
        if self.plainTextEditPtAnamEpid.toPlainText() != '':
            if self.comboBoxPtAnamEpid.currentText() == 'Спокойный':
                self.comboBoxPtAnamEpid.setCurrentText('отягощен')
        else:
            if self.comboBoxPtAnamEpid.currentText() != 'Спокойный':
                self.comboBoxPtAnamEpid.setCurrentText('Спокойный')

    def change_anam_aller_combobox(self):
        if self.plainTextEditPtAnamAllerg.toPlainText() != '':
            if self.comboBoxPtAllergStatus.currentText() == 'Отрицает':
                self.comboBoxPtAllergStatus.setCurrentText('ЕСТЬ')
        else:
            if self.comboBoxPtAllergStatus.currentText() != 'Отрицает':
                self.comboBoxPtAllergStatus.setCurrentText('Отрицает')

    # @upload_templates_db_from_yandex_cloud_bucket('default_templates')
    def add_new_template_obj_st(self):
        new_template_name = self.lineEdit_new_template_name.text()
        # проверяем не пустое ли имя нового шаблона
        if new_template_name != '':
            # проверяем есть ли уже шаблон с таким именем
            if new_template_name not in self.templates_list:
                # формируем кортеж с данными нового шаблона
                template_new = (
                    self.lineEdit_new_template_name.text(),
                    self.comboBoxPtGeneralState.currentText(),
                    self.comboBoxPtSkinState_1.currentText(),
                    self.comboBoxPtSkinState_2.currentText(),
                    self.comboBoxPtLymphnode.currentText(),
                    self.comboBoxPtMucousMembr_1.currentText(),
                    self.comboBoxPtBreathing_1.currentText(),
                    self.comboBoxPtBreathing_2.currentText(),
                    self.comboBoxPtBreathing_3.currentText(),
                    self.comboBoxPtWheezingChoice.currentText(),
                    self.comboBoxPtWheezing_1.currentText(),
                    self.comboBoxPtWheezing_2.currentText(),
                    self.comboBoxPtWheezing_3.currentText(),
                    self.comboBoxPtDyspneaChoice.currentText(),
                    self.comboBoxPtDyspnea_1.currentText(),
                    self.comboBoxPtDyspnea_2.currentText(),
                    self.comboBoxPtDyspnea_3.currentText(),
                    self.comboBoxPtHearthTone_1.currentText(),
                    self.comboBoxPtHearthTone_2.currentText(),
                    self.comboBoxPtHearthTone_3.currentText(),
                    self.comboBoxPtHearthNoiseChoice.currentText(),
                    self.comboBoxPtHearthNoise.currentText(),
                    self.comboBoxPtStomach_1.currentText(),
                    self.comboBoxPtStomach_2.currentText(),
                    self.comboBoxPtStomach_3.currentText(),
                    self.comboBoxPtDefecation_1.currentText(),
                    self.comboBoxPtDefecation_2.currentText(),
                    self.comboBoxPtDefecation_3.currentText(),
                    self.comboBoxPtUrination_1.currentText(),
                    self.comboBoxPtUrination_2.currentText(),
                    self.comboBoxPtUrination_3.currentText(),
                    self.plainTextEditPtStObjOther.toPlainText()
                )
                # записываем новый шаблон
                insert_obj_template_into_db(template_new)
            else:
                # такое имя шаблона уже есть
                # уточняем желание перезаписать данные
                ''''''
                # формируем кортеж с данными нового шаблона
                template_new = (
                    self.comboBoxPtGeneralState.currentText(),
                    self.comboBoxPtSkinState_1.currentText(),
                    self.comboBoxPtSkinState_2.currentText(),
                    self.comboBoxPtLymphnode.currentText(),
                    self.comboBoxPtMucousMembr_1.currentText(),
                    self.comboBoxPtBreathing_1.currentText(),
                    self.comboBoxPtBreathing_2.currentText(),
                    self.comboBoxPtBreathing_3.currentText(),
                    self.comboBoxPtWheezingChoice.currentText(),
                    self.comboBoxPtWheezing_1.currentText(),
                    self.comboBoxPtWheezing_2.currentText(),
                    self.comboBoxPtWheezing_3.currentText(),
                    self.comboBoxPtDyspneaChoice.currentText(),
                    self.comboBoxPtDyspnea_1.currentText(),
                    self.comboBoxPtDyspnea_2.currentText(),
                    self.comboBoxPtDyspnea_3.currentText(),
                    self.comboBoxPtHearthTone_1.currentText(),
                    self.comboBoxPtHearthTone_2.currentText(),
                    self.comboBoxPtHearthTone_3.currentText(),
                    self.comboBoxPtHearthNoiseChoice.currentText(),
                    self.comboBoxPtHearthNoise.currentText(),
                    self.comboBoxPtStomach_1.currentText(),
                    self.comboBoxPtStomach_2.currentText(),
                    self.comboBoxPtStomach_3.currentText(),
                    self.comboBoxPtDefecation_1.currentText(),
                    self.comboBoxPtDefecation_2.currentText(),
                    self.comboBoxPtDefecation_3.currentText(),
                    self.comboBoxPtUrination_1.currentText(),
                    self.comboBoxPtUrination_2.currentText(),
                    self.comboBoxPtUrination_3.currentText(),
                    self.plainTextEditPtStObjOther.toPlainText(),
                    self.lineEdit_new_template_name.text()
                )
                # обновляем шаблон
                update_obj_template_db(template_new)
        else:
            # имя шаблона пустое
            pass

        self.lineEdit_new_template_name.setText('')
        self.templates_list = read_db_obj_template_list()
        self.comboBoxGeneralStTemplate.clear()
        if len(self.templates_list) <= 1:
            self.comboBoxGeneralStTemplate.addItem(self.templates_list[0])
        else:
            self.comboBoxGeneralStTemplate.addItems(self.templates_list)

    def push_active_template(self):
        '''
        '''
        template_name = self.comboBoxGeneralStTemplate.currentText()
        # читаем данные шаблона по имени
        tpl = read_db_obj_template_data([template_name])
        if tpl is None:
            pass
        else:
            # вставляем полученные данные в нужные ячейки
            self.comboBoxPtGeneralState.setCurrentText(tpl[0])
            self.comboBoxPtSkinState_1.setCurrentText(tpl[1])
            self.comboBoxPtSkinState_2.setCurrentText(tpl[2])
            self.comboBoxPtLymphnode.setCurrentText(tpl[3])
            self.comboBoxPtMucousMembr_1.setCurrentText(tpl[4])
            self.comboBoxPtBreathing_1.setCurrentText(tpl[5])
            self.comboBoxPtBreathing_2.setCurrentText(tpl[6])
            self.comboBoxPtBreathing_3.setCurrentText(tpl[7])
            self.comboBoxPtWheezingChoice.setCurrentText(tpl[8])
            self.comboBoxPtWheezing_1.setCurrentText(tpl[9])
            self.comboBoxPtWheezing_2.setCurrentText(tpl[10])
            self.comboBoxPtWheezing_3.setCurrentText(tpl[11])
            self.comboBoxPtDyspneaChoice.setCurrentText(tpl[12])
            self.comboBoxPtDyspnea_1.setCurrentText(tpl[13])
            self.comboBoxPtDyspnea_2.setCurrentText(tpl[14])
            self.comboBoxPtDyspnea_3.setCurrentText(tpl[15])
            self.comboBoxPtHearthTone_1.setCurrentText(tpl[16])
            self.comboBoxPtHearthTone_2.setCurrentText(tpl[17])
            self.comboBoxPtHearthTone_3.setCurrentText(tpl[18])
            self.comboBoxPtHearthNoiseChoice.setCurrentText(tpl[19])
            self.comboBoxPtHearthNoise.setCurrentText(tpl[20])
            self.comboBoxPtStomach_1.setCurrentText(tpl[21])
            self.comboBoxPtStomach_2.setCurrentText(tpl[22])
            self.comboBoxPtStomach_3.setCurrentText(tpl[23])
            self.comboBoxPtDefecation_1.setCurrentText(tpl[24])
            self.comboBoxPtDefecation_2.setCurrentText(tpl[25])
            self.comboBoxPtDefecation_3.setCurrentText(tpl[26])
            self.comboBoxPtUrination_1.setCurrentText(tpl[27])
            self.comboBoxPtUrination_2.setCurrentText(tpl[28])
            self.comboBoxPtUrination_3.setCurrentText(tpl[29])
            self.plainTextEditPtStObjOther.setPlainText(tpl[30])

    def set_random_values(self):
        random_set = create_random_set()
        self.lineEditPtBloodPreasureSist.setText(random_set['bp_sist'])
        self.lineEditPtBloodPreasureDiast.setText(random_set['bp_diast'])
        self.lineEditPtPulse.setText(random_set['heart_rate'])
        self.lineEditPtBreathingSpeed.setText(random_set['breath_rate'])
        self.lineEditSaturation.setText(random_set['saturation'])
        self.lineEditPtTemperature.setText(random_set['temperature'])

    def add_new_template_jaloby(self):
        template = {
            'name': self.lineEdit_new_template_name_jaloby.text(),
            'жалобы': self.plainTextEditPtComplaints.toPlainText(),
        }

        if template['name'] != '':
            self.complaints_templates[template['name']] = template
            templates_file = 'complaints'
            templates_json_recording(templates=self.complaints_templates,
                                     templates_name=templates_file)
            # загружаем в бакет
            # upload_templates_json_from_yandex_cloud_bucket(templates_file)
        else:
            pass
        # обновляем список шаблонов
        self.lineEdit_new_template_name_jaloby.setText('')
        self.set_templates_list_jaloby()

    def push_active_template_jaloby(self):
        name = self.comboBox_jaloby_templates.currentText()
        if name in self.complaints_templates:
            self.plainTextEditPtComplaints.setPlainText(
                self.complaints_templates[name]['жалобы'])
        self.comboBox_jaloby_templates.setCurrentText('')

    def set_styles(self):
        pass
