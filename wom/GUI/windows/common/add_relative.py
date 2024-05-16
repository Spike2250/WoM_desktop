from PySide6 import QtWidgets

from wom.GUI.PY.common import AddRelative
from wom.app_logic.create_docs import (open_folder_with_files,
                                       creating_documents)
from wom.app_logic.db_func\
    .bucket_func import upload_history_to_yandex_cloud_bucket
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.writing.postprocessing\
    .add_relative import update_after_add_relative


# Окно добавления родственников
class Ui_AddRelative(QtWidgets.QWidget,
                     AddRelative.Ui_AddRelative):
    def __init__(self, user_info, windows, main_win,
                 dictionary, case_type, from_add_patient=False):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.case_type = case_type
        self.from_add_patient = from_add_patient

        self.set_connections()
        self.insert_data_from_dictionary()

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonPrintRelativePass\
            .clicked.connect(self.create_relative_pass)
        self.pushButtonNotSaveExit\
            .clicked.connect(self.exit)
        self.pushButtonSaveExit\
            .clicked.connect(self.exit_and_save)

    def insert_data_from_dictionary(self):
        self.labelPassportData.setText(self.d['patient_info'])
        # заполнение ячеек окна данными из словаря
        if 'родс_фио' in self.d:
            self.lineEditPtRelativeFullName\
                .setText(self.d['родс_фио'])
            self.lineEditPtRelativePhone\
                .setText(self.d['родс_телефон'])
            self.lineEditPtRelativePassportNumber\
                .setText(self.d['родс_паспорт'])
            self.lineEditPtRelativeKinship\
                .setText(self.d['родс_родство'])

            self.lineEditPtRelativeFullName_2\
                .setText(self.d['родс_фио_2'])
            self.lineEditPtRelativePhone_2\
                .setText(self.d['родс_телефон_2'])
            self.lineEditPtRelativePassportNumber_2\
                .setText(self.d['родс_паспорт_2'])
            self.lineEditPtRelativeKinship_2\
                .setText(self.d['родс_родство_2'])

            self.lineEditPtRelativeFullName_3\
                .setText(self.d['родс_фио_3'])
            self.lineEditPtRelativePhone_3\
                .setText(self.d['родс_телефон_3'])
            self.lineEditPtRelativePassportNumber_3\
                .setText(self.d['родс_паспорт_3'])
            self.lineEditPtRelativeKinship_3\
                .setText(self.d['родс_родство_3'])

            self.lineEditPtRelativeFullName_4\
                .setText(self.d['родс_фио_4'])
            self.lineEditPtRelativePhone_4\
                .setText(self.d['родс_телефон_4'])
            self.lineEditPtRelativePassportNumber_4\
                .setText(self.d['родс_паспорт_4'])
            self.lineEditPtRelativeKinship_4\
                .setText(self.d['родс_родство_4'])

    # функции для кнопок
    def create_relative_pass(self):
        '''
        '''
        self.write_to_dictionary()
        creating_documents(self.d, ['Пропуск_для_посещения'])
        open_folder_with_files(self.d)

    def write_to_dictionary(self):
        '''
        перезапись в словаре всех значений из виджетов на новые
        '''
        self.d['родс_фио'] = self\
            .lineEditPtRelativeFullName.text()
        self.d['родс_телефон'] = self\
            .lineEditPtRelativePhone.text()
        self.d['родс_паспорт'] = self\
            .lineEditPtRelativePassportNumber.text()
        self.d['родс_родство'] = self\
            .lineEditPtRelativeKinship.text()

        self.d['родс_фио_2'] = self\
            .lineEditPtRelativeFullName_2.text()
        self.d['родс_телефон_2'] = self\
            .lineEditPtRelativePhone_2.text()
        self.d['родс_паспорт_2'] = self\
            .lineEditPtRelativePassportNumber_2.text()
        self.d['родс_родство_2'] = self\
            .lineEditPtRelativeKinship_2.text()

        self.d['родс_фио_3'] = self\
            .lineEditPtRelativeFullName_3.text()
        self.d['родс_телефон_3'] = self\
            .lineEditPtRelativePhone_3.text()
        self.d['родс_паспорт_3'] = self\
            .lineEditPtRelativePassportNumber_3.text()
        self.d['родс_родство_3'] = self\
            .lineEditPtRelativeKinship_3.text()

        self.d['родс_фио_4'] = self\
            .lineEditPtRelativeFullName_4.text()
        self.d['родс_телефон_4'] = self\
            .lineEditPtRelativePhone_4.text()
        self.d['родс_паспорт_4'] = self\
            .lineEditPtRelativePassportNumber_4.text()
        self.d['родс_родство_4'] = self\
            .lineEditPtRelativeKinship_4.text()

        update_after_add_relative(self.d)

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

    def exit_and_save(self):
        self.save_history()
        self.exit()

    def create_window(self, main_win):
        if self.from_add_patient:
            w = self.windows[self.case_type]['add_new_patient'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=main_win,
                dictionary=self.d)
        else:
            w = self.windows['common']['passport'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=main_win,
                dictionary=self.d,
                case_type=self.case_type)
        return w

    def exit(self):
        win = self.windows['Frameless']()
        win.setWidget(self.create_window(win))
        win.show()
        self.main_win.close()
