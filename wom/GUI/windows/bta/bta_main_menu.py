
import uuid  # генератор случайных UIN
from datetime import timedelta, datetime
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import (QTableWidgetItem as QTW_Item,
                               QAbstractItemView,
                               QPushButton,
                               QProgressBar)

from wom.GUI.PY.bta import bta_MainMenu
from wom.app_logic.service_func import (convert_date as c_date,
                                        calc_percent_fullness)
from wom.app_logic.db_func.db_bta import (read_d_from_db_bta,
                                          read_db_active_cases_bta,
                                          read_db_archive_cases_bta,
                                          read_fullness_db_bta)
from wom.styles_qss import main_styles


class Ui_MainMenu(QtWidgets.QWidget,
                  bta_MainMenu.Ui_MainMenu):
    def __init__(self, user_info, windows, main_win):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.user_info = user_info
        self.main_win = main_win
        self.d = {}

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Кабинет ботулинотерапевта"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.create_tables()
        self.show_active_cases()

    def onButtonMy(self):
        # self.textEdit.append("Нажата `Своя Кнопка`!")
        pass

    def set_connections(self):
        # коннекты кнопок
        self.add_new_patient.clicked.connect(
            self.create_new_case)
        self.refresh_pt_list.clicked.connect(
            self.show_active_cases)
        self.find_patient.clicked.connect(
            self.show_active_cases)
        self.pushButtonOpenArchive.clicked.connect(
            self.show_archive_cases)
        self.pushButton_month.clicked.connect(
            self.set_current_month_dates)
        self.pushButton_previous_month.clicked.connect(
            self.set_previous_month_dates)
        self.pushButton_year.clicked.connect(
            self.set_current_year_dates)
        self.pushButton_report_manager.clicked.connect(
            self.open_report_manager)
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
        # таблица активных случаев
        self.tableWidget_db.setColumnWidth(0, 100)  # ширина колонок
        self.tableWidget_db.setColumnWidth(1, 75)  # по номеру колонки
        self.tableWidget_db.setColumnWidth(2, 40)
        self.tableWidget_db.setColumnWidth(3, 85)
        self.tableWidget_db.setColumnWidth(4, 280)
        self.tableWidget_db.setColumnWidth(5, 85)
        self.tableWidget_db.setColumnWidth(6, 150)
        self.tableWidget_db.setColumnWidth(7, 55)
        self.tableWidget_db.setColumnWidth(8, 280)
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

    def return_to_entry(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['common']['entry'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def open_window(self, name):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['bta'][name](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win,
                dictionary=self.d))
        win.show()
        self.main_win.close()

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
        self.d = read_d_from_db_bta(uin)
        self.open_window('patient_card')

    def show_active_cases(self):
        # определяем критерии поиска
        find = self.lineEdit_find_active.text().lower()
        # читаем БД и получаем список кортежей активных случаев
        data = read_db_active_cases_bta()
        # проверяем, что данные есть
        if data is not None:
            # сортируем все по алфавиту
            data = sorted(
                data,
                key=lambda case: case['full_name'],
                reverse=False
            )
            # по чек-боксам сортируем дополнительно
            # по дате поступления
            if self.radioButton_date.isChecked():
                data = sorted(
                    data,
                    key=lambda case: c_date(case['adm_date']),
                    reverse=False
                )
            # по врачу
            elif self.radioButton_doc.isChecked():
                data.sort(
                    key=lambda case: case['doctor_name'],
                    reverse=False
                )
            # собираем новый список кортежей по критериям поиска
            new_data = []
            for case in data:
                if find in case['full_name'].lower():
                    new_data.append(case)
            data = new_data

            table = self.tableWidget_db
            # устанавливаем количество строк в таблице равное
            # количеству найденных случаев
            table.setRowCount(len(data))
            # формируем подпись о полученных данных
            self.label_act_pt.setText(f'Найдено активных случаев: {len(data)}')

            for i in range(len(data)):
                # создаем кнопку
                button = QPushButton('Открыть')
                # создаем иконку
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(":/icon/icons/sticky_note_2_white_36dp.svg"),
                    QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(icon)
                button.setStyleSheet(main_styles.button_del)
                # соединяем кнопку с функцией открытия истории болезни
                button.clicked.connect(self.open_patient_card)
                # определяем полноту истории
                fullness = read_fullness_db_bta(data[i]['case_id'])
                percent = calc_percent_fullness(fullness, bta=True)
                progress = QProgressBar()
                progress.setValue(percent)
                progress.setTextVisible(False)
                progress.setStyleSheet(main_styles.progress)

                # заполняем ячейки
                table.setCellWidget(i, 0, progress)
                table.setCellWidget(i, 1, button)
                if data[i]['type_hosp'] == 'БТ - круглосуточный':
                    table.setItem(i, 2, QTW_Item('КС'))
                elif data[i]['type_hosp'] == 'БТ - дневной':
                    table.setItem(i, 2, QTW_Item('ДС'))
                else:
                    table.setItem(i, 2, QTW_Item('UN'))
                table.setItem(i, 3, QTW_Item(data[i]['adm_date']))
                table.setItem(i, 4, QTW_Item(data[i]['full_name']))
                table.setItem(i, 5, QTW_Item(data[i]['mkb10_ds']))
                table.setItem(i, 6, QTW_Item(data[i]['doctor_name']))
                if data[i]['sicklist_check'] == '1':
                    table.setItem(i, 7, QTW_Item('+'))
                else:
                    table.setItem(i, 7, QTW_Item(' '))
                table.setItem(i, 8, QTW_Item(data[i]['case_id']))
        else:
            self.label_act_pt.setText('Не найден ни один активный случай')

    def show_archive_cases(self):
        # определяем критерии поиска
        dates = (
            c_date(self.dateEdit_find_1.dateTime().toString('dd.MM.yyyy')),
            c_date(self.dateEdit_find_2.dateTime().toString('dd.MM.yyyy')))
        find = self.lineEdit.text().lower()
        # читаем БД и получаем список кортежей случаев
        data = read_db_archive_cases_bta()
        # сортируем список
        # проверяем, что данные есть
        if data is not None:
            # сортируем все по алфавиту
            data = sorted(
                data,
                key=lambda case: case['full_name'],
                reverse=False)
            # и по дате выписки
            data = sorted(
                data,
                key=lambda case: c_date(case['dis_date']),
                reverse=False)

            # корректируем список кортежей
            new_data = []
            # определяем критерий поиска по датам
            if self.radioButton_admission.isChecked():
                date = 'adm_date'
            elif self.radioButton_discharge.isChecked():
                date = 'dis_date'
            # собираем новый список по критериям поиска
            for case in data:
                if dates[0] <= c_date(case[date]) <= dates[1]:
                    if find in case['full_name'].lower():
                        new_data.append(case)
            data = new_data

            table = self.tableWidget_archive_bd
            # устанавливаем количество строк в таблице равное
            # количеству найденных случаев
            table.setRowCount(len(data))
            # формируем подпись о полученных данных
            self.label_archive_pt.setText(f'Найдено историй болезни: {len(data)}')  # noqa: E501

            for i in range(len(data)):
                # создаем кнопку
                button = QPushButton('открыть')
                # создаем иконку
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(":/icon/icons/sticky_note_2_white_36dp.svg"),
                    QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(icon)
                button.setStyleSheet(main_styles.button_del)
                # соединяем кнопку с функцией открытия истории болезни
                button.clicked.connect(self.open_patient_card_from_archive)

                # заполняем ячейки
                table.setCellWidget(i, 0, button)
                if data[i]['type_hosp'] == 'БТ - круглосуточный':
                    table.setItem(i, 1, QTW_Item('КС'))
                elif data[i]['type_hosp'] == 'БТ - дневной':
                    table.setItem(i, 1, QTW_Item('ДС'))
                else:
                    table.setItem(i, 1, QTW_Item('UN'))
                table.setItem(i, 2, QTW_Item(data[i]['adm_date']))
                table.setItem(i, 3, QTW_Item(data[i]['dis_date']))
                table.setItem(i, 4, QTW_Item(data[i]['full_name']))
                table.setItem(i, 5, QTW_Item(data[i]['mkb10_ds']))
                table.setItem(i, 6, QTW_Item(data[i]['doctor_name']))
                if data[i]['sicklist_check'] == '1':
                    table.setItem(i, 7, QTW_Item('+'))
                else:
                    table.setItem(i, 7, QTW_Item(' '))
                table.setItem(i, 8, QTW_Item(data[i]['case_id']))
        else:
            self.label_act_pt.setText('Не найден ни один случай')

    def open_report_manager(self):
        pass
