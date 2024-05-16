from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QTableWidgetItem as QTW_Item,
    QAbstractItemView,
    QPushButton,
    QLineEdit,
)

from wom.GUI.PY.common import Almanac

from wom.app_logic.db_func\
    .drugs_almanac import read_almanac, almanac_json_recording
from wom.app_logic.service_func import get_value_between_brackets

from wom.styles_qss\
    .main_styles import button_own, button_other, lineEdit_style


class Ui_Almanac(QtWidgets.QWidget,
                 Almanac.Ui_Almanac):
    def __init__(self, user_info, windows, main_win):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win

        msg = "World of Medicine - Справочник "\
              "лекарственных средств"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.read_actual_json()
        self.refresh_group_list()
        self.set_connections()

    def onButtonMy(self):
        pass

    def refresh_group_list(self):
        self.comboBox_group.clear()
        self.comboBox_group.addItem('')
        group_list = list(self.almanac)
        self.comboBox_group.addItems(group_list)

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        self.pushButton_add_drug.clicked.connect(self.add_new_drug)
        self.pushButton_start_almanac.clicked.connect(self.show_almanac)

    def read_actual_json(self):
        '''
        '''
        self.almanac = read_almanac()
        if self.almanac is None:
            self.almanac = {}

    def add_new_drug(self):
        '''
        '''
        group = self.comboBox_group.currentText()
        if group != '':
            drug_name = self.lineEdit_name.text()
            if drug_name != '':
                if self.radioButton_tab.isChecked():
                    drug_type = 'Табл.; Tab.'
                elif self.radioButton_caps.isChecked():
                    drug_type = 'Капс.; Caps.'
                elif self.radioButton_sol.isChecked():
                    drug_type = 'Р-р.; Sol.'
                elif self.radioButton_susp.isChecked():
                    drug_type = 'Сусп.; Susp.'
                elif self.radioButton_pulv.isChecked():
                    drug_type = 'Пор.; Pulv.'
                elif self.radioButton_supp.isChecked():
                    drug_type = 'Супп.; Supp.'
                else:
                    drug_type = '; '
                doses = self.lineEdit_doses.text()
                latin_name = self.lineEdit_name_latin.text()
                ds = self.plainTextEdit_ds.toPlainText()
                name_torg = self.plainTextEdit_name_torg.toPlainText()

                drug = {
                    'name': drug_name,
                    'form': drug_type,
                    'latin_name': latin_name,
                    'doses': doses,
                    'DS': ds,
                    'torg_name': name_torg
                }

                drugs_dict = {
                    f'{drug_type.split("; ")[0]}{drug_name}': drug
                }
                if group not in self.almanac:
                    self.almanac[group] = drugs_dict
                    text = f"Препарат '{drug_name}' успешно "\
                           f"добавлен в справочник!\n"\
                           f"Создана новая фарм.группа '{group}'."
                    self.textBrowser.setText(text)
                    self.refresh_group_list()
                else:
                    self.almanac[group][f'{drug_type.split("; ")[0]}{drug_name}'] = drug  # noqa: E501
                    text = f"Препарат '{drug_name}' "\
                           f"успешно добавлен в справочник!"
                    self.textBrowser.setText(text)

                self.clear_inputs()

            else:
                text = f"Не указано название препарата! Препарат не добавлен!"
                self.textBrowser.setText(text)

        else:
            text = f"Не указана фармакологическая "\
                   f"группа! Препарат не добавлен!"
            self.textBrowser.setText(text)

    def clear_inputs(self):
        self.lineEdit_name.setText('')
        self.lineEdit_name_latin.setText('')
        self.plainTextEdit_name_torg.setPlaceholderText('')
        # self.lineEdit_doses.setText('')
        # self.plainTextEdit_ds.setPlaceholderText('')

    def show_almanac(self):
        '''
        '''
        n = len(self.almanac)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setColumnWidth(0, 495)
        self.tableWidget.setHorizontalHeaderLabels(['Фармакологическая группа'])  # noqa: E501
        self.tableWidget.setRowCount(n)
        self.tableWidget.verticalHeader().hide()
        i = 0
        for group in sorted(self.almanac):
            button = QPushButton(group)
            button.setStyleSheet(button_other)
            button.clicked.connect(self.open_group)
            self.tableWidget.setCellWidget(i, 0, button)
            i += 1

    def open_group(self):
        button_group = self.sender()
        group = button_group.text()
        self.tableWidget.setHorizontalHeaderLabels([group])
        self.tableWidget.setRowCount(0)
        n = len(self.almanac[group])
        self.tableWidget.setRowCount(n)
        self.tableWidget.verticalHeader().hide()
        i = 0
        for drug in sorted(self.almanac[group]):
            button = QPushButton(drug)
            button.setStyleSheet(button_other)
            button.clicked.connect(self.open_drug)
            self.tableWidget.setCellWidget(i, 0, button)
            i += 1

    def open_drug(self):
        button_drug = self.sender()
        drug = button_drug.text()
        group = self.tableWidget.horizontalHeaderItem(0).text()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, 135)
        self.tableWidget.setColumnWidth(1, 290)
        self.tableWidget.setColumnWidth(2, 70)
        self.tableWidget.setHorizontalHeaderLabels(
            ['', f'{self.almanac[group][drug]["name"]}', ''])

        doses_n = len(doses := self.almanac[group][drug]['doses'].split('; '))
        ds_n = len(DS := self.almanac[group][drug]['DS'].split('; '))
        dj_n = len(torg := self.almanac[group][drug]['torg_name'].split('; '))
        n = 3 + doses_n + ds_n + dj_n + 2
        self.tableWidget.setRowCount(n)
        self.tableWidget.verticalHeader().hide()

        form_rus, form_latin = self.almanac[group][drug]['form'].split('; ')
        rus_name = f"{form_rus}{self.almanac[group][drug]['name']}"
        latin_name = f"{form_latin}{self.almanac[group][drug]['latin_name']}"

        button_resave = QPushButton('переcохранить лек.препарат')
        button_resave.clicked.connect(self.resave_drug)
        button_resave.setStyleSheet(button_other)
        button_del = QPushButton('удалить')
        button_del.clicked.connect(self.del_drug)
        button_del.setStyleSheet(button_own)
        lineEdit_check = QLineEdit()
        lineEdit_check.setStyleSheet(lineEdit_style)
        lineEdit_check.setPlaceholderText(
            'Введите "удалить" для подтверждения')

        i = 0
        self.tableWidget.setItem(i, 0, QTW_Item('Название:'))
        self.tableWidget.setItem(i, 1, QTW_Item(rus_name))
        self.tableWidget.setItem(i, 2, QTW_Item(''))
        i += 1
        self.tableWidget.setItem(i, 0, QTW_Item('по-латински:'))
        latin_name_lineEdit = QLineEdit(latin_name)
        latin_name_lineEdit.setStyleSheet(lineEdit_style)
        self.tableWidget.setCellWidget(i, 1, latin_name_lineEdit)
        self.tableWidget.setItem(i, 2, QTW_Item(''))
        i += 1
        self.tableWidget.setItem(i, 0, QTW_Item('Фарм.группа:'))
        self.tableWidget.setItem(i, 1, QTW_Item(group))
        self.tableWidget.setItem(i, 2, QTW_Item(''))
        i += 1
        for j in range(doses_n):
            if j == 0:
                self.tableWidget.setItem(
                    i, 0, QTW_Item(f'Дозировки({doses_n}):'))
            dose_lineEdit = QLineEdit(doses[j])
            dose_lineEdit.setStyleSheet(lineEdit_style)
            self.tableWidget.setCellWidget(i, 1, dose_lineEdit)
            self.tableWidget.setItem(i, 2, QTW_Item(''))
            i += 1
        for j in range(ds_n):
            if j == 0:
                self.tableWidget.setItem(
                    i, 0, QTW_Item(f'Назначения({ds_n}):'))
            app_lineEdit = QLineEdit(DS[j])
            app_lineEdit.setStyleSheet(lineEdit_style)
            self.tableWidget.setCellWidget(i, 1, app_lineEdit)
            self.tableWidget.setItem(i, 2, QTW_Item(''))
            i += 1
        for j in range(dj_n):
            if j == 0:
                self.tableWidget.setItem(
                    i, 0, QTW_Item(f'Торг.названия({dj_n}):'))
            torg_lineEdit = QLineEdit(torg[j])
            torg_lineEdit.setStyleSheet(lineEdit_style)
            self.tableWidget.setCellWidget(i, 1, torg_lineEdit)
            self.tableWidget.setItem(i, 2, QTW_Item(''))
            i += 1
        self.tableWidget.setItem(i, 0, QTW_Item(''))
        self.tableWidget.setCellWidget(i, 1, button_resave)
        self.tableWidget.setItem(i, 2, QTW_Item(''))
        i += 1
        self.tableWidget.setItem(i, 0, QTW_Item(''))
        self.tableWidget.setCellWidget(i, 1, lineEdit_check)
        self.tableWidget.setCellWidget(i, 2, button_del)

    def resave_drug(self):
        # получаем из таблицы названия препарата и фарм.группы
        drug = self.tableWidget.item(0, 1).text()
        drug_latin = self.tableWidget.cellWidget(1, 1).text()
        group = self.tableWidget.item(2, 1).text()
        # позиция начала дозировок
        row_doses = 3  # дозировки всегда начинаются на 4й(3) строке
        # получаем значение количества вариантов доз лек.средства
        doses_n = int(get_value_between_brackets(
            self.tableWidget.item(row_doses, 0).text()))
        # вычисляем позицию начала назначений
        row_ds = row_doses + doses_n
        # и получаем значение количества вариантов назначений
        ds_n = int(get_value_between_brackets(
            self.tableWidget.item(row_ds, 0).text()))
        # вычисляем позицию начала торг.названий
        row_dj = row_ds + ds_n
        # и получаем значение количества вариантов торг.названий
        dj_n = int(get_value_between_brackets(
            self.tableWidget.item(row_dj, 0).text()))
        # собираем строку дозировок
        doses = ''
        for i in range(doses_n):
            doses += self.tableWidget.cellWidget(row_doses + i, 1).text()
            if i + 1 != doses_n:
                doses += '; '
        # собираем строку назначений
        DS = ''
        for i in range(ds_n):
            DS += self.tableWidget.cellWidget(row_ds + i, 1).text()
            if i + 1 != ds_n:
                DS += '; '
        # собираем строку торг.названий
        torg_name = ''
        for i in range(dj_n):
            torg_name += self.tableWidget.cellWidget(row_dj + i, 1).text()
            if i + 1 != dj_n:
                torg_name += '; '

        try:
            # перезаписываем соответствующие значения на новые
            self.almanac[group][drug]['latin_name'] = drug_latin
            self.almanac[group][drug]['doses'] = doses
            self.almanac[group][drug]['DS'] = DS
            self.almanac[group][drug]['torg_name'] = torg_name
            # выводим сообщение об успешной перезаписи
            text = f"Дозировки, назначения и торг.названия препарата '{drug}'"\
                   f"были успешно обновлены в справочнике!"
            self.textBrowser.setText(text)
            # обновляем таблицу со справочником на главное меню
            self.show_almanac()
        except KeyError as error:
            print(error)
            # выводим сообщение об ошибке
            text = f"(!) Ошибка при перезаписи лек.препарата!!!"
            self.textBrowser.setText(text)

    def del_drug(self):
        # получаем номер строки, где расположена кнопка удаления
        button = self.sender()
        i = self.tableWidget.indexAt(button.pos()).row()
        # получаем из таблицы названия препарата и фарм.группы
        drug = self.tableWidget.item(0, 1).text()
        group = self.tableWidget.item(2, 1).text()
        # получаем значения из подтверждающей строки lineEdit
        check = self.tableWidget.cellWidget(i, 1).text()
        # удаляем из справочника словарь с данным препаратом
        if check in ('удалить', 'Удалить', 'УДАЛИТЬ'):
            try:
                del self.almanac[group][drug]
                # выводим сообщение об успешном удалении
                text = f"Препарат {drug} был успешно удален из справочника!"
                self.textBrowser.setText(text)
                # обновляем таблицу со справочником на главное меню
                self.show_almanac()
            except KeyError as error:
                print(error)
                # выводим сообщение об ошибке
                text = f"(!) Ошибка при удалении лек.препарата!!!"
                self.textBrowser.setText(text)
        else:
            # выводим сообщение о провале проверки
            text = f"(!) Удаление остановлено! \n"\
                   f"Пересмотрите строку подтверждения и попробуйте снова."
            self.textBrowser.setText(text)

    def exit_and_save(self):
        self.save_almanac()
        self.close_almanac()

    def save_almanac(self):
        almanac_json_recording(self.almanac)

    def close_almanac(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['common']['entry'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()
