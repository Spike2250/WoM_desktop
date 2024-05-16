from PySide6 import QtWidgets

from wom.GUI.PY.common import St_Neurology
from wom.app_logic.db_func\
    .db_st_neur_templates import (read_db_neur_template_list,
                                  read_db_neur_template_data,
                                  insert_neur_template_into_db,
                                  update_neur_template_db)
from wom.app_logic.db_func\
    .bucket_func import (upload_history_to_yandex_cloud_bucket,
                         upload_templates_db_from_yandex_cloud_bucket,
                         download_templates_db_from_yandex_cloud_bucket)
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.writing.postprocessing.neur_st import update_after_neur_st


class Ui_StNeurology(QtWidgets.QWidget,
                     St_Neurology.Ui_Neurology_status):
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
              "реабилитации - Неврологический и "\
              "функциональный статусы"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.define_ending()
        self.create_dict_of_widgets()

        self.set_connections()
        self.set_templates_list()
        self.set_patient_info()
        self.insert_data_from_dictionary()
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

    def create_dict_of_widgets(self):
        self.ns = {
            'Сознание': self.comboBoxNS_Conscious,
            'ШКГ': self.comboBoxNS_GCS,
            'RASS': self.comboBoxNS_RASS,
            'Контакт': self.comboBoxNS_Contact,
            'Ориентирование': self.comboBoxNS_Orientation,
            'Менингеальные_1': self.comboBoxNS_MeningealSymp_1,
            'Менингеальные_2': self.comboBoxNS_MeningealSymp_2,
            'Менингеальные_3': self.comboBoxNS_MeningealSymp_3,
            'Речь_1': self.comboBoxNS_Speech_1,
            'Речь_2': self.comboBoxNS_Speech_2,
            'Речь_3': self.comboBoxNS_Speech_3,
            'ФТО': self.comboBoxNS_PelvicFuntion,
            'обоняние': self.comboBoxNS_4MN_1_Smell,
            'острота_зрения': self.comboBoxNS_4MN_2_VisualAcuity,
            'поля_зрения': self.comboBoxNS_4MN_2_Fields,
            'зрачки': self.comboBoxNS_4MN_2_Pupils,
            'аккомодация': self.comboBoxNS_4MN_2_Accomodation,
            'фотореакция': self.comboBoxNS_4MN_2_Photoreaction,
            'конвергенция': self.comboBoxNS_4MN_2_Convergension,
            'движения_гл_яблок': self.comboBoxNS_4MN_346_EyeballMove,
            'парез_глазодвиг': self.comboBoxNS_4MN_346_EyeballParesis,
            'птоз': self.comboBoxNS_4MN_346_Ptosis,
            'нистагм': self.comboBoxNS_4MN_346_Nystagmus,
            'V_пара': self.comboBoxNS_4MN_5_FaceSensitivity,
            'V_пара_Ветви': self.comboBoxNS_4MN_5_Branches,
            'V_пара_Зельдер': self.comboBoxNS_4MN_5_Zelder,
            'VII_пара': self.comboBoxNS_4MN_7_Symmetry,
            'VII_пара_дополнение': self.comboBoxNS_4MN_7_Other,
            'слух': self.comboBoxNS_4MN_8_Hearing,
            'центр_головокружение': self.comboBoxNS_4MN_8_CentralVertigo,
            'фонация': self.comboBoxNS_4MN_910_Phonation,
            'мягкое_небо': self.comboBoxNS_4MN_910_SoftPalate,
            'глотание': self.comboBoxNS_4MN_910_Swallowing,
            'питание': self.comboBoxNS_4MN_910_Food,
            'дизартрия': self.comboBoxNS_4MN_910_Dysarthria,
            'дизартрия_степень': self.comboBoxNS_4MN_910_Dysarthria_power,
            'XI_пара': self.comboBoxNS_4MN_11,
            'XII_пара': self.comboBoxNS_4MN_12,
            'движ_конечности': self.comboBoxNS_Moving_limbs,
            'движ_суставы': self.comboBoxNS_Moving_joints,
            'движ_позвоночник': self.comboBoxNS_Moving_spine,
            'MRC_R_A_P': self.comboBoxNS_MRC_R_A_P,
            'MRC_R_A_D': self.comboBoxNS_MRC_R_A_D,
            'MRC_R_L_P': self.comboBoxNS_MRC_R_L_P,
            'MRC_R_L_D': self.comboBoxNS_MRC_R_L_D,
            'MRC_L_A_P': self.comboBoxNS_MRC_L_A_P,
            'MRC_L_A_D': self.comboBoxNS_MRC_L_A_D,
            'MRC_L_L_P': self.comboBoxNS_MRC_L_L_P,
            'MRC_L_L_D': self.comboBoxNS_MRC_L_L_D,
            'мышечный_тонус_1': self.comboBoxNS_MuscleTonus_1,
            'мышечный_тонус_2': self.comboBoxNS_MuscleTonus_2,
            'Ash_R_A_P': self.comboBoxNS_Ash_R_A_P,
            'Ash_R_A_D': self.comboBoxNS_Ash_R_A_D,
            'Ash_R_L_P': self.comboBoxNS_Ash_R_L_P,
            'Ash_R_L_D': self.comboBoxNS_Ash_R_L_D,
            'Ash_L_A_P': self.comboBoxNS_Ash_L_A_P,
            'Ash_L_A_D': self.comboBoxNS_Ash_L_A_D,
            'Ash_L_L_P': self.comboBoxNS_Ash_L_L_P,
            'Ash_L_L_D': self.comboBoxNS_Ash_L_L_D,
            'рефлексы_руки_1': self.comboBoxNS_Arms_reflex_1,
            'рефлексы_руки_2': self.comboBoxNS_Arms_reflex_2,
            'рефлексы_ноги_1': self.comboBoxNS_Legs_reflex_1,
            'рефлексы_ноги_2': self.comboBoxNS_Legs_reflex_2,
            'патологические_рефлексы': self.comboBoxNS_Pathology_reflex,
            'трофика_мышц': self.comboBoxNS_MuscleTrofic,
            'чувствительность_1': self.comboBoxNS_Sensitivity_1,
            'чувствительность_2': self.comboBoxNS_Sensitivity_2,
            'координация_1': self.comboBoxNS_Coordination_1,
            'координация_2': self.comboBoxNS_Coordination_2,
            'экстрапирамидные_1': self.comboBoxNS_Extrapyramid_1,
            'экстрапирамидные_2': self.comboBoxNS_Extrapyramid_2,
            'экстрапирамидные_3': self.comboBoxNS_Extrapyramid_3,
            'эпилептический_статус': self.comboBoxNS_EpilepticStatus,
            'функциональный_статус': self.comboBoxNS_FuncStatus_common,
            'ходьба': self.comboBoxNS_FuncStatus_walking,
            'походка': self.comboBoxNS_FuncStatus_walking_type,
            'мелкая_моторика': self.comboBoxNS_FuncStatus_motorics,
            'одевание': self.comboBoxNS_FuncStatus_dressing,
            'подъем_по_лестнице': self.comboBoxNS_FuncStatus_stairway,
            'прием_пищи': self.comboBoxNS_FuncStatus_eating,
            'письмо': self.comboBoxNS_FuncStatus_writing,
            'чтение': self.comboBoxNS_FuncStatus_reading,
            'чувствительность_текст': self.plainTextEditNS_Sensitivity,
            'координация_текст': self.plainTextEditNS_Coordination,
            'функциональный_статус_дополнение': self.plainTextEditNS_FuncStatus,  # noqa: E501
            'NS_дополнение': self.plainTextEditNS_other,
        }

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        self.pushButtonAddNewTemplate.clicked.connect(
            self.add_new_template_neur_st)
        self.pushButton_push_temp.clicked.connect(
            self.push_active_template)

    # @download_templates_db_from_yandex_cloud_bucket('default_templates')
    def set_templates_list(self):
        # список шаблонов
        self.templates_list = read_db_neur_template_list()
        self.comboBoxNeuralStTemplate.clear()
        if len(self.templates_list) <= 1:
            self.comboBoxNeuralStTemplate.addItem(self.templates_list[0])
        else:
            self.comboBoxNeuralStTemplate.addItems(self.templates_list)

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def insert_data_from_dictionary(self):
        # заполнение данных, если они уже есть
        if f'Неврологический_статус{self.end}' in self.d:
            for key in self.ns:
                try:
                    self.ns[key].setCurrentText(self.d[f"{key}{self.end}"])
                except AttributeError:
                    self.ns[key].setPlainText(self.d[f"{key}{self.end}"])
        # заполнение данных для выписки - данными при поступлении
        elif self.timeline == 'dis' and\
                'Неврологический_статус' in self.d:
            for key in self.ns:
                try:
                    self.ns[key].setCurrentText(self.d[f"{key}"])
                except AttributeError:
                    self.ns[key].setPlainText(self.d[f"{key}"])

    def write_to_dictionary(self):
        for key in self.ns:
            try:
                self.d[f"{key}{self.end}"] = self.ns[key].currentText()
            except AttributeError:
                self.d[f"{key}{self.end}"] = self.ns[key].toPlainText()
        update_after_neur_st(self.d, self.timeline)

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

    # @upload_templates_db_from_yandex_cloud_bucket('default_templates')
    def add_new_template_neur_st(self):
        new_template_name = self.lineEdit_new_template_name.text()
        # проверяем не пустое ли имя нового шаблона
        if new_template_name != '':
            # проверяем есть ли уже шаблон с таким именем
            if new_template_name not in self.templates_list:
                # формируем кортеж с данными нового шаблона
                template_new = (
                    self.lineEdit_new_template_name.text(),
                    self.comboBoxNS_Conscious.currentText(),
                    self.comboBoxNS_GCS.currentText(),
                    self.comboBoxNS_RASS.currentText(),
                    self.comboBoxNS_Contact.currentText(),
                    self.comboBoxNS_Orientation.currentText(),
                    self.comboBoxNS_MeningealSymp_1.currentText(),
                    self.comboBoxNS_MeningealSymp_2.currentText(),
                    self.comboBoxNS_MeningealSymp_3.currentText(),
                    self.comboBoxNS_Speech_1.currentText(),
                    self.comboBoxNS_Speech_2.currentText(),
                    self.comboBoxNS_Speech_3.currentText(),
                    self.comboBoxNS_PelvicFuntion.currentText(),
                    self.comboBoxNS_4MN_1_Smell.currentText(),
                    self.comboBoxNS_4MN_2_VisualAcuity.currentText(),
                    self.comboBoxNS_4MN_2_Fields.currentText(),
                    self.comboBoxNS_4MN_2_Pupils.currentText(),
                    self.comboBoxNS_4MN_2_Accomodation.currentText(),
                    self.comboBoxNS_4MN_2_Photoreaction.currentText(),
                    self.comboBoxNS_4MN_2_Convergension.currentText(),
                    self.comboBoxNS_4MN_346_EyeballMove.currentText(),
                    self.comboBoxNS_4MN_346_EyeballParesis.currentText(),
                    self.comboBoxNS_4MN_346_Ptosis.currentText(),
                    self.comboBoxNS_4MN_346_Nystagmus.currentText(),
                    self.comboBoxNS_4MN_5_FaceSensitivity.currentText(),
                    self.comboBoxNS_4MN_5_Branches.currentText(),
                    self.comboBoxNS_4MN_5_Zelder.currentText(),
                    self.comboBoxNS_4MN_7_Symmetry.currentText(),
                    self.comboBoxNS_4MN_7_Other.currentText(),
                    self.comboBoxNS_4MN_8_Hearing.currentText(),
                    self.comboBoxNS_4MN_8_CentralVertigo.currentText(),
                    self.comboBoxNS_4MN_910_Phonation.currentText(),
                    self.comboBoxNS_4MN_910_SoftPalate.currentText(),
                    self.comboBoxNS_4MN_910_Swallowing.currentText(),
                    self.comboBoxNS_4MN_910_Food.currentText(),
                    self.comboBoxNS_4MN_910_Dysarthria.currentText(),
                    self.comboBoxNS_4MN_910_Dysarthria_power.currentText(),
                    self.comboBoxNS_4MN_11.currentText(),
                    self.comboBoxNS_4MN_12.currentText(),
                    self.comboBoxNS_Moving_limbs.currentText(),
                    self.comboBoxNS_Moving_joints.currentText(),
                    self.comboBoxNS_Moving_spine.currentText(),
                    self.comboBoxNS_MRC_R_A_P.currentText(),
                    self.comboBoxNS_MRC_R_A_D.currentText(),
                    self.comboBoxNS_MRC_R_L_P.currentText(),
                    self.comboBoxNS_MRC_R_L_D.currentText(),
                    self.comboBoxNS_MRC_L_A_P.currentText(),
                    self.comboBoxNS_MRC_L_A_D.currentText(),
                    self.comboBoxNS_MRC_L_L_P.currentText(),
                    self.comboBoxNS_MRC_L_L_D.currentText(),
                    self.comboBoxNS_MuscleTonus_1.currentText(),
                    self.comboBoxNS_MuscleTonus_2.currentText(),
                    self.comboBoxNS_Ash_R_A_P.currentText(),
                    self.comboBoxNS_Ash_R_A_D.currentText(),
                    self.comboBoxNS_Ash_R_L_P.currentText(),
                    self.comboBoxNS_Ash_R_L_D.currentText(),
                    self.comboBoxNS_Ash_L_A_P.currentText(),
                    self.comboBoxNS_Ash_L_A_D.currentText(),
                    self.comboBoxNS_Ash_L_L_P.currentText(),
                    self.comboBoxNS_Ash_L_L_D.currentText(),
                    self.comboBoxNS_Arms_reflex_1.currentText(),
                    self.comboBoxNS_Arms_reflex_2.currentText(),
                    self.comboBoxNS_Legs_reflex_1.currentText(),
                    self.comboBoxNS_Legs_reflex_2.currentText(),
                    self.comboBoxNS_Pathology_reflex.currentText(),
                    self.comboBoxNS_MuscleTrofic.currentText(),
                    self.comboBoxNS_Sensitivity_1.currentText(),
                    self.comboBoxNS_Sensitivity_2.currentText(),
                    self.plainTextEditNS_Sensitivity.toPlainText(),
                    self.comboBoxNS_Coordination_1.currentText(),
                    self.comboBoxNS_Coordination_2.currentText(),
                    self.plainTextEditNS_Coordination.toPlainText(),
                    self.comboBoxNS_Extrapyramid_1.currentText(),
                    self.comboBoxNS_Extrapyramid_2.currentText(),
                    self.comboBoxNS_Extrapyramid_3.currentText(),
                    self.comboBoxNS_EpilepticStatus.currentText(),
                    self.comboBoxNS_FuncStatus_common.currentText(),
                    self.comboBoxNS_FuncStatus_walking.currentText(),
                    self.comboBoxNS_FuncStatus_walking_type.currentText(),
                    self.comboBoxNS_FuncStatus_motorics.currentText(),
                    self.comboBoxNS_FuncStatus_dressing.currentText(),
                    self.comboBoxNS_FuncStatus_stairway.currentText(),
                    self.comboBoxNS_FuncStatus_eating.currentText(),
                    self.comboBoxNS_FuncStatus_writing.currentText(),
                    self.comboBoxNS_FuncStatus_reading.currentText(),
                    self.plainTextEditNS_FuncStatus.toPlainText(),
                    self.plainTextEditNS_other.toPlainText()
                )
                # записываем новый шаблон
                insert_neur_template_into_db(template_new)
            else:
                # такое имя шаблона уже есть
                # уточняем желание перезаписать данные
                ''''''
                # формируем кортеж с данными нового шаблона
                template_new = (
                    self.comboBoxNS_Conscious.currentText(),
                    self.comboBoxNS_GCS.currentText(),
                    self.comboBoxNS_RASS.currentText(),
                    self.comboBoxNS_Contact.currentText(),
                    self.comboBoxNS_Orientation.currentText(),
                    self.comboBoxNS_MeningealSymp_1.currentText(),
                    self.comboBoxNS_MeningealSymp_2.currentText(),
                    self.comboBoxNS_MeningealSymp_3.currentText(),
                    self.comboBoxNS_Speech_1.currentText(),
                    self.comboBoxNS_Speech_2.currentText(),
                    self.comboBoxNS_Speech_3.currentText(),
                    self.comboBoxNS_PelvicFuntion.currentText(),
                    self.comboBoxNS_4MN_1_Smell.currentText(),
                    self.comboBoxNS_4MN_2_VisualAcuity.currentText(),
                    self.comboBoxNS_4MN_2_Fields.currentText(),
                    self.comboBoxNS_4MN_2_Pupils.currentText(),
                    self.comboBoxNS_4MN_2_Accomodation.currentText(),
                    self.comboBoxNS_4MN_2_Photoreaction.currentText(),
                    self.comboBoxNS_4MN_2_Convergension.currentText(),
                    self.comboBoxNS_4MN_346_EyeballMove.currentText(),
                    self.comboBoxNS_4MN_346_EyeballParesis.currentText(),
                    self.comboBoxNS_4MN_346_Ptosis.currentText(),
                    self.comboBoxNS_4MN_346_Nystagmus.currentText(),
                    self.comboBoxNS_4MN_5_FaceSensitivity.currentText(),
                    self.comboBoxNS_4MN_5_Branches.currentText(),
                    self.comboBoxNS_4MN_5_Zelder.currentText(),
                    self.comboBoxNS_4MN_7_Symmetry.currentText(),
                    self.comboBoxNS_4MN_7_Other.currentText(),
                    self.comboBoxNS_4MN_8_Hearing.currentText(),
                    self.comboBoxNS_4MN_8_CentralVertigo.currentText(),
                    self.comboBoxNS_4MN_910_Phonation.currentText(),
                    self.comboBoxNS_4MN_910_SoftPalate.currentText(),
                    self.comboBoxNS_4MN_910_Swallowing.currentText(),
                    self.comboBoxNS_4MN_910_Food.currentText(),
                    self.comboBoxNS_4MN_910_Dysarthria.currentText(),
                    self.comboBoxNS_4MN_910_Dysarthria_power.currentText(),
                    self.comboBoxNS_4MN_11.currentText(),
                    self.comboBoxNS_4MN_12.currentText(),
                    self.comboBoxNS_Moving_limbs.currentText(),
                    self.comboBoxNS_Moving_joints.currentText(),
                    self.comboBoxNS_Moving_spine.currentText(),
                    self.comboBoxNS_MRC_R_A_P.currentText(),
                    self.comboBoxNS_MRC_R_A_D.currentText(),
                    self.comboBoxNS_MRC_R_L_P.currentText(),
                    self.comboBoxNS_MRC_R_L_D.currentText(),
                    self.comboBoxNS_MRC_L_A_P.currentText(),
                    self.comboBoxNS_MRC_L_A_D.currentText(),
                    self.comboBoxNS_MRC_L_L_P.currentText(),
                    self.comboBoxNS_MRC_L_L_D.currentText(),
                    self.comboBoxNS_MuscleTonus_1.currentText(),
                    self.comboBoxNS_MuscleTonus_2.currentText(),
                    self.comboBoxNS_Ash_R_A_P.currentText(),
                    self.comboBoxNS_Ash_R_A_D.currentText(),
                    self.comboBoxNS_Ash_R_L_P.currentText(),
                    self.comboBoxNS_Ash_R_L_D.currentText(),
                    self.comboBoxNS_Ash_L_A_P.currentText(),
                    self.comboBoxNS_Ash_L_A_D.currentText(),
                    self.comboBoxNS_Ash_L_L_P.currentText(),
                    self.comboBoxNS_Ash_L_L_D.currentText(),
                    self.comboBoxNS_Arms_reflex_1.currentText(),
                    self.comboBoxNS_Arms_reflex_2.currentText(),
                    self.comboBoxNS_Legs_reflex_1.currentText(),
                    self.comboBoxNS_Legs_reflex_2.currentText(),
                    self.comboBoxNS_Pathology_reflex.currentText(),
                    self.comboBoxNS_MuscleTrofic.currentText(),
                    self.comboBoxNS_Sensitivity_1.currentText(),
                    self.comboBoxNS_Sensitivity_2.currentText(),
                    self.plainTextEditNS_Sensitivity.toPlainText(),
                    self.comboBoxNS_Coordination_1.currentText(),
                    self.comboBoxNS_Coordination_2.currentText(),
                    self.plainTextEditNS_Coordination.toPlainText(),
                    self.comboBoxNS_Extrapyramid_1.currentText(),
                    self.comboBoxNS_Extrapyramid_2.currentText(),
                    self.comboBoxNS_Extrapyramid_3.currentText(),
                    self.comboBoxNS_EpilepticStatus.currentText(),
                    self.comboBoxNS_FuncStatus_common.currentText(),
                    self.comboBoxNS_FuncStatus_walking.currentText(),
                    self.comboBoxNS_FuncStatus_walking_type.currentText(),
                    self.comboBoxNS_FuncStatus_motorics.currentText(),
                    self.comboBoxNS_FuncStatus_dressing.currentText(),
                    self.comboBoxNS_FuncStatus_stairway.currentText(),
                    self.comboBoxNS_FuncStatus_eating.currentText(),
                    self.comboBoxNS_FuncStatus_writing.currentText(),
                    self.comboBoxNS_FuncStatus_reading.currentText(),
                    self.plainTextEditNS_FuncStatus.toPlainText(),
                    self.plainTextEditNS_other.toPlainText(),
                    self.lineEdit_new_template_name.text()
                )
                # обновляем шаблон
                update_neur_template_db(template_new)
        else:
            # имя шаблона пустое
            pass

        self.lineEdit_new_template_name.setText('')
        self.templates_list = read_db_neur_template_list()
        self.comboBoxNeuralStTemplate.clear()
        if len(self.templates_list) <= 1:
            self.comboBoxNeuralStTemplate.addItem(self.templates_list[0])
        else:
            self.comboBoxNeuralStTemplate.addItems(self.templates_list)

    def push_active_template(self):
        '''
        '''
        template_name = self.comboBoxNeuralStTemplate.currentText()
        # читаем данные шаблона по имени
        tpl = read_db_neur_template_data([template_name])
        if tpl is None:
            pass
        else:
            # вставляем полученные данные в нужные ячейки
            self.comboBoxNS_Conscious.setCurrentText(tpl[0])
            self.comboBoxNS_GCS.setCurrentText(tpl[1])
            self.comboBoxNS_RASS.setCurrentText(tpl[2])
            self.comboBoxNS_Contact.setCurrentText(tpl[3])
            self.comboBoxNS_Orientation.setCurrentText(tpl[4])
            self.comboBoxNS_MeningealSymp_1.setCurrentText(tpl[5])
            self.comboBoxNS_MeningealSymp_2.setCurrentText(tpl[6])
            self.comboBoxNS_MeningealSymp_3.setCurrentText(tpl[7])
            self.comboBoxNS_Speech_1.setCurrentText(tpl[8])
            self.comboBoxNS_Speech_2.setCurrentText(tpl[9])
            self.comboBoxNS_Speech_3.setCurrentText(tpl[10])
            self.comboBoxNS_PelvicFuntion.setCurrentText(tpl[11])
            self.comboBoxNS_4MN_1_Smell.setCurrentText(tpl[12])
            self.comboBoxNS_4MN_2_VisualAcuity.setCurrentText(tpl[13])
            self.comboBoxNS_4MN_2_Fields.setCurrentText(tpl[14])
            self.comboBoxNS_4MN_2_Pupils.setCurrentText(tpl[15])
            self.comboBoxNS_4MN_2_Accomodation.setCurrentText(tpl[16])
            self.comboBoxNS_4MN_2_Photoreaction.setCurrentText(tpl[17])
            self.comboBoxNS_4MN_2_Convergension.setCurrentText(tpl[18])
            self.comboBoxNS_4MN_346_EyeballMove.setCurrentText(tpl[19])
            self.comboBoxNS_4MN_346_EyeballParesis.setCurrentText(tpl[20])
            self.comboBoxNS_4MN_346_Ptosis.setCurrentText(tpl[21])
            self.comboBoxNS_4MN_346_Nystagmus.setCurrentText(tpl[22])
            self.comboBoxNS_4MN_5_FaceSensitivity.setCurrentText(tpl[23])
            self.comboBoxNS_4MN_5_Branches.setCurrentText(tpl[24])
            self.comboBoxNS_4MN_5_Zelder.setCurrentText(tpl[25])
            self.comboBoxNS_4MN_7_Symmetry.setCurrentText(tpl[26])
            self.comboBoxNS_4MN_7_Other.setCurrentText(tpl[27])
            self.comboBoxNS_4MN_8_Hearing.setCurrentText(tpl[28])
            self.comboBoxNS_4MN_8_CentralVertigo.setCurrentText(tpl[29])
            self.comboBoxNS_4MN_910_Phonation.setCurrentText(tpl[30])
            self.comboBoxNS_4MN_910_SoftPalate.setCurrentText(tpl[31])
            self.comboBoxNS_4MN_910_Swallowing.setCurrentText(tpl[32])
            self.comboBoxNS_4MN_910_Food.setCurrentText(tpl[33])
            self.comboBoxNS_4MN_910_Dysarthria.setCurrentText(tpl[34])
            self.comboBoxNS_4MN_910_Dysarthria_power.setCurrentText(tpl[35])
            self.comboBoxNS_4MN_11.setCurrentText(tpl[36])
            self.comboBoxNS_4MN_12.setCurrentText(tpl[37])
            self.comboBoxNS_Moving_limbs.setCurrentText(tpl[38])
            self.comboBoxNS_Moving_joints.setCurrentText(tpl[39])
            self.comboBoxNS_Moving_spine.setCurrentText(tpl[40])
            self.comboBoxNS_MRC_R_A_P.setCurrentText(tpl[41])
            self.comboBoxNS_MRC_R_A_D.setCurrentText(tpl[42])
            self.comboBoxNS_MRC_R_L_P.setCurrentText(tpl[43])
            self.comboBoxNS_MRC_R_L_D.setCurrentText(tpl[44])
            self.comboBoxNS_MRC_L_A_P.setCurrentText(tpl[45])
            self.comboBoxNS_MRC_L_A_D.setCurrentText(tpl[46])
            self.comboBoxNS_MRC_L_L_P.setCurrentText(tpl[47])
            self.comboBoxNS_MRC_L_L_D.setCurrentText(tpl[48])
            self.comboBoxNS_MuscleTonus_1.setCurrentText(tpl[49])
            self.comboBoxNS_MuscleTonus_2.setCurrentText(tpl[50])
            self.comboBoxNS_Ash_R_A_P.setCurrentText(tpl[51])
            self.comboBoxNS_Ash_R_A_D.setCurrentText(tpl[52])
            self.comboBoxNS_Ash_R_L_P.setCurrentText(tpl[53])
            self.comboBoxNS_Ash_R_L_D.setCurrentText(tpl[54])
            self.comboBoxNS_Ash_L_A_P.setCurrentText(tpl[55])
            self.comboBoxNS_Ash_L_A_D.setCurrentText(tpl[56])
            self.comboBoxNS_Ash_L_L_P.setCurrentText(tpl[57])
            self.comboBoxNS_Ash_L_L_D.setCurrentText(tpl[58])
            self.comboBoxNS_Arms_reflex_1.setCurrentText(tpl[59])
            self.comboBoxNS_Arms_reflex_2.setCurrentText(tpl[60])
            self.comboBoxNS_Legs_reflex_1.setCurrentText(tpl[61])
            self.comboBoxNS_Legs_reflex_2.setCurrentText(tpl[62])
            self.comboBoxNS_Pathology_reflex.setCurrentText(tpl[63])
            self.comboBoxNS_MuscleTrofic.setCurrentText(tpl[64])
            self.comboBoxNS_Sensitivity_1.setCurrentText(tpl[65])
            self.comboBoxNS_Sensitivity_2.setCurrentText(tpl[66])
            self.plainTextEditNS_Sensitivity.setPlainText(tpl[67])
            self.comboBoxNS_Coordination_1.setCurrentText(tpl[68])
            self.comboBoxNS_Coordination_2.setCurrentText(tpl[69])
            self.plainTextEditNS_Coordination.setPlainText(tpl[70])
            self.comboBoxNS_Extrapyramid_1.setCurrentText(tpl[71])
            self.comboBoxNS_Extrapyramid_2.setCurrentText(tpl[72])
            self.comboBoxNS_Extrapyramid_3.setCurrentText(tpl[73])
            self.comboBoxNS_EpilepticStatus.setCurrentText(tpl[74])
            self.comboBoxNS_FuncStatus_common.setCurrentText(tpl[75])
            self.comboBoxNS_FuncStatus_walking.setCurrentText(tpl[76])
            self.comboBoxNS_FuncStatus_walking_type.setCurrentText(tpl[77])
            self.comboBoxNS_FuncStatus_motorics.setCurrentText(tpl[78])
            self.comboBoxNS_FuncStatus_dressing.setCurrentText(tpl[79])
            self.comboBoxNS_FuncStatus_stairway.setCurrentText(tpl[80])
            self.comboBoxNS_FuncStatus_eating.setCurrentText(tpl[81])
            self.comboBoxNS_FuncStatus_writing.setCurrentText(tpl[82])
            self.comboBoxNS_FuncStatus_reading.setCurrentText(tpl[83])
            self.plainTextEditNS_FuncStatus.setPlainText(tpl[84])
            self.plainTextEditNS_other.setPlainText(tpl[85])

    def set_styles(self):
        pass
