from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import (QAbstractItemView, QPushButton,
                               QTableWidgetItem as QTW_Item)
from wom.GUI.PY.bta import bta_Protocol
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.writing.postprocessing.protocol_bta import update_after_bta_protocol  # noqa: E501
from wom.settings.bta_muscles import muscles
from wom.styles_qss.main_styles import (
    button_del,
    lineEdit_style_error,
    lineEdit_style,
)


# Окно протокола ботулинотерапии
class Ui_Protocol_BTA(QtWidgets.QWidget,
                      bta_Protocol.Ui_Form):
    def __init__(self, user_info, windows, main_win, dictionary):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.d = dictionary
        self.user_info = user_info
        self.main_win = main_win
        self.muscles = []

        msg = "World of Medicine - Кабинет ботулинотерапевта "\
              "- Протокол ботулинотерапии"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_patient_info()
        self.set_connections()
        self.add_values_to_popup_lists()
        self.insert_data_from_dictionary()
        self.set_table_params()
        self.refresh_table_bta()

    def onButtonMy(self):
        # self.textEdit.append("Нажата `Своя Кнопка`!")
        pass

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def set_connections(self):
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonHelp.clicked.connect(self.open_help)
        self.pushButton_add_muscle.clicked.connect(self.add_muscle)

    def exit_and_save(self):
        self.write_to_dictionary()
        write_all_data_to_db_bta(self.d)
        self.exit()

    def exit(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['bta']['patient_card'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win,
                dictionary=self.d))
        win.show()
        self.main_win.close()

    def add_values_to_popup_lists(self):
        self.comboBox_muscle.clear()
        self.comboBox_muscle.addItems(muscles)
        # дописывание произвольных значений в comboBox
        self.comboBox_muscle.setEditable(True)

    def set_table_params(self):
        self.label_summary.setText('')
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setMinimumWidth(850)
        self.tableWidget.setColumnWidth(0, 650)
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(2, 55)

    def open_help(self):
        pass

    def insert_data_from_dictionary(self):
        self.comboBox_bta_preparat.setCurrentText(self.d['препарат_БТА'])
        if 'БТА_мышцы_мишени' in self.d:
            # lineEdit's
            self.lineEdit_series.setText(self.d['бта_серия_препарата'])
            self.lineEdit_when_made.setText(self.d['бта_дата_изготовления'])
            self.lineEdit_best_before.setText(self.d['бта_годен_до'])
            # comboBox's
            self.comboBox_bta_solvent.setCurrentText(self.d['бта_растворитель'])  # noqa: E501
            # список мышц-мишеней
            self.muscles = self.d['бта_мышцы'].copy()

    def write_to_dictionary(self):
        # lineEdit's
        self.d['бта_серия_препарата'] = self.lineEdit_series.text()
        self.d['бта_дата_изготовления'] = self.lineEdit_when_made.text()
        self.d['бта_годен_до'] = self.lineEdit_best_before.text()
        # comboBox's
        self.d['препарат_БТА'] = self.comboBox_bta_preparat.currentText()
        self.d['бта_растворитель'] = self.comboBox_bta_solvent.currentText()
        # список мышц-мишеней
        self.d['бта_мышцы'] = self.muscles
        # суммарная доза БТА
        self.d['бта_суммарная_доза'] = self.label_summary.text()
        # постобработка значений
        update_after_bta_protocol(self.d)

    def add_muscle(self):
        muscle = self.comboBox_muscle.currentText()
        side = self.comboBox_side.currentText()
        dose = self.lineEdit_dose.text()

        try:
            dose = int(dose)
            if all((muscle, dose)) != '':
                d_muscle = {
                    'muscle': muscle,
                    'side': side,
                    'dose': str(dose),
                }
                self.comboBox_muscle.setCurrentText('')
                self.comboBox_side.setCurrentText('')
                self.lineEdit_dose.setText('')
                self.lineEdit_dose.setStyleSheet(lineEdit_style)

                self.muscles.append(d_muscle)
                self.refresh_table_bta()
        except ValueError:
            self.lineEdit_dose.setStyleSheet(lineEdit_style_error)

    def refresh_table_bta(self):
        if (n := len(self.muscles)) != 0:
            # устанавливаем количество строк
            self.tableWidget.setRowCount(n)
            # сумма всех доз БТА
            summary = 0
            # проходим циклом по списку инъецированных мышц
            for i in range(n):
                muscle = f"{self.muscles[i]['muscle']} - "\
                         f"{self.muscles[i]['side']}"
                dose = self.muscles[i]['dose']
                # суммируем дозы
                dose_int = int(dose)
                summary += dose_int
                # создаем кнопку
                button = QPushButton('')
                icon = QtGui.QIcon()
                icon.addPixmap(
                    QtGui.QPixmap(":/icon/icons/block_white_36dp.svg"),
                    QtGui.QIcon.Normal, QtGui.QIcon.Off)
                button.setIcon(icon)
                button.setIconSize(QtCore.QSize(24, 24))
                button.setStyleSheet(button_del)
                button.clicked.connect(self.del_muscle)
                # вставляем значения в таблицу
                self.tableWidget.setItem(i, 0, QTW_Item(muscle))
                self.tableWidget.setItem(i, 1, QTW_Item(dose))
                self.tableWidget.setCellWidget(i, 2, button)
            self.label_summary.setText(str(summary))
        else:
            text = '\tПока не добавлена ни одна точка инъекции БТ-А'
            self.label_summary.setText('')
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QTW_Item(text))

    def del_muscle(self):
        # Определяем из какой строки была кнопка вызвавшая функцию
        button = self.sender()
        i = self.tableWidget.indexAt(button.pos()).row()
        # удаляем элемент списка
        self.muscles.pop(i)
        # обновляем таблицу
        self.refresh_table_bta()
