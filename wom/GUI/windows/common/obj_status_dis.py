from PySide6 import QtWidgets

from wom.GUI.PY.common import StObj_discharge
from wom.app_logic.db_func\
    .bucket_func import upload_history_to_yandex_cloud_bucket
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta


class Ui_StPrObjectivus_discharge(QtWidgets.QWidget,
                                  StObj_discharge.Ui_StObj):
    def __init__(self, user_info, windows, main_win, dictionary, case_type):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.case_type = case_type

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Соматический статус при выписке"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.insert_data_from_dictionary()
        self.set_patient_info()
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
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def insert_data_from_dictionary(self):
        # заполнение
        if 'Соматический_статус_выписка' in self.d:
            self.plainTextEdit_status.setPlainText(
                self.d['Соматический_статус_выписка'])
        else:
            if 'Соматический_статус_для_дневников' in self.d:
                self.plainTextEdit_status.setPlainText(
                    self.d['Соматический_статус_для_дневников'])

    def write_to_dictionary(self):
        self.d['Соматический_статус_выписка'] = self.plainTextEdit_status.toPlainText()  # noqa: E501

    def set_styles(self):
        pass
