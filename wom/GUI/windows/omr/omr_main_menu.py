
import uuid  # генератор случайных UIN
from datetime import timedelta, datetime
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import (
    QTableWidgetItem as QTW_Item,
    QAbstractItemView,
    QPushButton,
    QProgressBar,
)

from wom.GUI.PY.omr import omr_MainMenu
from wom.app_logic.service_func import (convert_date as c_date,
                                        calc_percent_fullness)
from wom.app_logic.db_func.db_omr import (read_d_from_db,
                                          read_db_active_cases,
                                          read_db_archive_cases,
                                          read_db_active_cases_for_discharge,
                                          read_fullness_db)
from wom.app_logic.writing.lists import (open_folder_patients_lists,
                                         create_patients_list,
                                         create_patients_list_for_discharge,
                                         create_doc_lists,
                                         creating_file_pt_list,
                                         creating_file_doc_lists)
from wom.app_logic.db_func.bucket_func import (download_case_from_yandex_cloud_bucket,  # noqa: E501
                                               download_db_from_yandex_cloud_bucket)  # noqa: E501
from wom.styles_qss.main_styles import (progress_style_other,
                                        button_del)


# Окно основного меню
class Ui_MainMenu(QtWidgets.QWidget,
                  omr_MainMenu.Ui_omr_main_menu):
    def __init__(self, user_info, windows, main_win):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = {}

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # окно без рамки

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Рабочее место врача-ФРМ"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.create_tables()
        self.show_active_cases()
        self.set_styles()

    def onButtonMy(self):
        pass

    def set_connections(self):
        # коннекты кнопок
        self.add_new_patient\
            .clicked.connect(self.create_new_case)
        self.refresh_pt_list\
            .clicked.connect(self.show_active_cases)
        self.find_patient\
            .clicked.connect(self.show_active_cases)
        self.pushButtonOpenArchive\
            .clicked.connect(self.show_archive_cases)
        self.pushButton_month\
            .clicked.connect(self.set_current_month_dates)
        self.pushButton_previous_month\
            .clicked.connect(self.set_previous_month_dates)
        self.pushButton_year\
            .clicked.connect(self.set_current_year_dates)
        self.pushButton_report_manager\
            .clicked.connect(self.open_report_manager)
        self.pushButton_print_patient_list\
            .clicked.connect(self.print_patients_list)
        self.pushButton_print_patient_list_2\
            .clicked.connect(self.print_patients_list_for_discharge)
        self.pushButton_print_lists\
            .clicked.connect(self.print_docs_lists)
        self.pushButton_back.clicked.connect(self.return_to_entry)
        # HotKeys
        self.refresh_pt_list.setShortcut('Return')
        self.pushButtonOpenArchive.setShortcut('Return')

    def create_tables(self):
        # делаем значения таблицы неизменяемыми
        self.tableWidget_db.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_archive_bd.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)
        # таблица
        self.tableWidget_db.setColumnWidth(0, 120)  # ширина колонок
        self.tableWidget_db.setColumnWidth(1, 75)  # по номеру колонки
        self.tableWidget_db.setColumnWidth(2, 40)
        self.tableWidget_db.setColumnWidth(3, 85)
        self.tableWidget_db.setColumnWidth(4, 58)
        self.tableWidget_db.setColumnWidth(5, 280)
        self.tableWidget_db.setColumnWidth(6, 55)
        self.tableWidget_db.setColumnWidth(7, 150)
        self.tableWidget_db.setColumnWidth(8, 45)
        self.tableWidget_db.setColumnWidth(9, 45)
        self.tableWidget_db.setColumnWidth(10, 280)
        # таблица архивных случаев
        self.tableWidget_archive_bd.setColumnWidth(0, 75)  # ширина колонок
        self.tableWidget_archive_bd.setColumnWidth(1, 40)  # по номеру колонки
        self.tableWidget_archive_bd.setColumnWidth(2, 85)
        self.tableWidget_archive_bd.setColumnWidth(3, 85)
        self.tableWidget_archive_bd.setColumnWidth(4, 280)
        self.tableWidget_archive_bd.setColumnWidth(5, 55)
        self.tableWidget_archive_bd.setColumnWidth(6, 150)
        self.tableWidget_archive_bd.setColumnWidth(7, 45)
        self.tableWidget_archive_bd.setColumnWidth(8, 280)
        # устанавливаем стандартные даты поиска
        self.today = datetime.now().strftime('%d.%m.%Y')
        self.dateEdit_find_1.setDate(
            QtCore.QDate.fromString('01.01.2022', "dd.MM.yyyy"))
        self.dateEdit_find_2.setDate(
            QtCore.QDate.fromString(self.today, "dd.MM.yyyy"))
        # устанавливаем placeholdertext
        find_text = 'введите поисковой запрос'
        self.lineEdit.setPlaceholderText(find_text)
        self.lineEdit_find_active.setPlaceholderText(find_text)

    def set_current_month_dates(self):
        date = f'01.{self.today[-7:]}'
        self.dateEdit_find_1.setDate(
            QtCore.QDate.fromString(date, "dd.MM.yyyy"))
        self.dateEdit_find_2.setDate(
            QtCore.QDate.fromString(self.today, "dd.MM.yyyy"))

    def set_current_year_dates(self):
        date = f'01.01.{self.today[-4:]}'
        self.dateEdit_find_1.setDate(
            QtCore.QDate.fromString(date, "dd.MM.yyyy"))
        self.dateEdit_find_2.setDate(
            QtCore.QDate.fromString(self.today, "dd.MM.yyyy"))

    def set_previous_month_dates(self):
        date2 = (c_date(f'01.{self.today[-7:]}') - timedelta(1))
        date2 = date2.strftime('%d.%m.%Y')
        date1 = f'01.{date2[-7:]}'
        self.dateEdit_find_1.setDate(
            QtCore.QDate.fromString(date1, "dd.MM.yyyy"))
        self.dateEdit_find_2.setDate(
            QtCore.QDate.fromString(date2, "dd.MM.yyyy"))

    def create_new_case(self):
        # создаем уникальный индентификатор случая
        self.d['unic_number'] = str(uuid.uuid4())  # УНИКАЛЬНЫЙ ID ДЛЯ БД
        self.open_window('add_new_patient')

    def open_patient_card(self):
        button = self.sender()
        self.open_card(type_='active', button=button)

    def open_patient_card_from_archive(self):
        button = self.sender()
        self.open_card(type_='archive', button=button)

    def open_card(self, type_, button):
        if type_ == 'active':
            table = self.tableWidget_db
            uin_pos = 10  # номер колонки с uin
        elif type_ == 'archive':
            table = self.tableWidget_archive_bd
            uin_pos = 8  # номер колонки с uin
        # Определяем из какой строки была кнопка вызвавшая функцию
        index = table.indexAt(button.pos()).row()
        # получаем uin из таблицы
        uin = table.item(index, uin_pos).text()
        self.reading_dict_and_open_card(uin)

    # @download_case_from_yandex_cloud_bucket('omr')
    def reading_dict_and_open_card(self, uin):
        # загружаем данные в словарь
        self.d = read_d_from_db(uin)
        self.open_window('patient_card')

    # @download_db_from_yandex_cloud_bucket('omr')
    def show_active_cases(self):
        # определяем критерии поиска
        find = self.lineEdit_find_active.text().lower()
        # читаем БД и получаем список кортежей активных случаев
        data = read_db_active_cases()
        # проверяем, что данные есть
        if data is not None:
            # сортируем все по алфавиту
            data.sort(
                key=lambda case: case["full_name"],
                reverse=False)
            # по чек-боксам сортируем дополнительно
            # по дате поступления
            if self.radioButton_date.isChecked():
                data.sort(
                    key=lambda case: c_date(case["adm_date"]),
                    reverse=False)
            elif self.radioButton_doc.isChecked():
                data.sort(
                    key=lambda case: case["doctor_name"],
                    reverse=False)
            elif self.radioButton_room.isChecked():
                data.sort(
                    key=lambda case: case["room_number"],
                    reverse=False)
            # собираем новый список кортежей по критериям поиска
            new_data = []
            for case in data:
                if find in case["full_name"].lower():
                    new_data.append(case)
            data = new_data
            # устанавливаем количество строк в таблице равное
            # количеству найденных случаев
            table = self.tableWidget_db
            table.setRowCount(len(data))
            # формируем подпись о полученных данных
            self.label_act_pt.setText(f'Найдено {len(data)} активных случаев')

            # формируем "Item"s для каждой клетки таблицы
            for i in range(len(data)):
                # создаем кнопку
                button = QPushButton('Открыть')
                # создаем иконку
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(":/icon/icons/sticky_note_2_white_36dp.svg"),
                    QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(icon)
                button.clicked.connect(self.open_patient_card)
                button.setStyleSheet(button_del)
                # определяем полноту истории
                fullness = read_fullness_db(data[i]["case_id"])
                percent = calc_percent_fullness(fullness)
                progress = QProgressBar()
                progress.setValue(percent)
                progress.setTextVisible(False)
                progress.setStyleSheet(progress_style_other)

                # заполняем ячейки
                table.setCellWidget(i, 0, progress)
                table.setCellWidget(i, 1, button)
                if data[i]["type_hosp"] == 'Круглосуточный стационар':
                    table.setItem(i, 2, QTW_Item('КС'))
                elif data[i]["type_hosp"] == 'Дневной стационар':
                    table.setItem(i, 2, QTW_Item('ДС'))
                else:
                    table.setItem(i, 2, QTW_Item('UN'))
                table.setItem(i, 3, QTW_Item(data[i]["adm_date"]))
                table.setItem(i, 4, QTW_Item(data[i]["room_number"]))
                table.setItem(i, 5, QTW_Item(data[i]["full_name"]))
                table.setItem(i, 6, QTW_Item(data[i]["mkb10_ds"]))
                table.setItem(i, 7, QTW_Item(data[i]["doctor_name"]))
                if data[i]["sicklist_check"] == '1':
                    table.setItem(i, 8, QTW_Item('+'))
                else:
                    table.setItem(i, 8, QTW_Item(' '))
                table.setItem(i, 9, QTW_Item(data[i]["diet"]))
                table.setItem(i, 10, QTW_Item(data[i]["case_id"]))
        else:
            self.label_act_pt.setText('Не найден ни один активный случай')

    # @download_db_from_yandex_cloud_bucket('omr')
    def show_archive_cases(self):
        # определяем критерии поиска
        dates = (
            c_date(self.dateEdit_find_1.dateTime().toString('dd.MM.yyyy')),
            c_date(self.dateEdit_find_2.dateTime().toString('dd.MM.yyyy'))
        )
        find = self.lineEdit.text().lower()
        # читаем БД и получаем список кортежей случаев
        data = read_db_archive_cases()
        # сортируем список
        # проверяем, что данные есть
        if data is not None:
            # сортируем все по алфавиту
            data.sort(
                key=lambda case: case["full_name"],
                reverse=False)
            # и по дате выписки
            data.sort(
                key=lambda case: c_date(case["dis_date"]),
                reverse=False)
            # корректируем список кортежей
            new_data = []
            # определяем критерий поиска по датам
            if self.radioButton_admission.isChecked():
                date = 'adm_date'
            elif self.radioButton_discharge.isChecked():
                date = 'dis_date'
            # собираем новый список кортежей по критериям поиска
            for case in data:
                if dates[0] <= c_date(case[date]) <= dates[1]:
                    if find in case["full_name"].lower():
                        new_data.append(case)
            data = new_data

            # устанавливаем количество строк в таблице равное
            # количеству найденных случаев
            table = self.tableWidget_archive_bd
            table.setRowCount(len(data))
            # формируем подпись о полученных данных
            self.label_archive_pt.setText(
                f'Найдено {len(data)} историй болезни')

            # формируем "Item"s для каждой клетки таблицы
            for i in range(len(data)):
                # создаем кнопку
                button = QPushButton('Открыть')
                # создаем иконку
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(":/icon/icons/sticky_note_2_white_36dp.svg"),
                    QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(icon)
                button.clicked.connect(self.open_patient_card_from_archive)
                button.setStyleSheet(button_del)
                # заполняем ячейки
                table.setCellWidget(i, 0, button)
                if data[i]["type_hosp"] == 'Круглосуточный стационар':
                    table.setItem(i, 1, QTW_Item('КС'))
                elif data[i]["type_hosp"] == 'Дневной стационар':
                    table.setItem(i, 1, QTW_Item('ДС'))
                else:
                    table.setItem(i, 1, QTW_Item('UN'))
                table.setItem(i, 2, QTW_Item(data[i]["adm_date"]))
                table.setItem(i, 3, QTW_Item(data[i]["dis_date"]))
                table.setItem(i, 4, QTW_Item(data[i]["full_name"]))
                table.setItem(i, 5, QTW_Item(data[i]["mkb10_ds"]))
                table.setItem(i, 6, QTW_Item(data[i]["doctor_name"]))
                if data[i]["sicklist_check"] == '1':
                    table.setItem(i, 7, QTW_Item('+'))
                else:
                    table.setItem(i, 7, QTW_Item(' '))
                table.setItem(i, 8, QTW_Item(data[i]["case_id"]))
        else:
            self.label_act_pt.setText('Не найден ни один случай')

    def print_patients_list(self):
        # читаем БД и получаем список кортежей случаев
        data = read_db_active_cases()
        # проверяем, что данные есть
        if data is not None:
            d_to_print = {
                'список_пациентов': create_patients_list(data)
            }
            creating_file_pt_list(d_to_print, 'today_list')
            open_folder_patients_lists()

    def print_patients_list_for_discharge(self):
        # читаем БД и получаем список кортежей случаев
        data = read_db_active_cases_for_discharge()
        if data is not None:
            table = create_patients_list_for_discharge(data)
            d_to_print = {
                'список_пациентов': table['simple'],
                'список_по_врачам': table['docs']
            }
            creating_file_pt_list(d_to_print, 'discharge')
            open_folder_patients_lists()

    def print_docs_lists(self):
        # читаем БД и получаем список кортежей случаев
        data = read_db_active_cases()
        # проверяем, что данные есть
        if data is not None:
            d_to_print = {
                'списки_для_обхода': create_doc_lists(data)
            }
            creating_file_doc_lists(d_to_print)
            open_folder_patients_lists()

    def open_window(self, name):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['omr'][name](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win,
                dictionary=self.d,
            )
        )
        win.show()
        self.main_win.close()

    def return_to_entry(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['common']['entry'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def set_styles(self):
        pass

    def open_report_manager(self):
        pass
