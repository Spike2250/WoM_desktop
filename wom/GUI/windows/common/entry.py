from PySide6 import QtWidgets

from wom.GUI.PY.common import Entry
from wom.styles_qss.main_styles import button_own


class Ui_Entry(QtWidgets.QWidget, Entry.Ui_Entry):
    def __init__(self, user_info, windows, main_win):
        super().__init__()
        self.setupUi(self)
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win

        msg = "World of Medicine - Делаем заполнение "\
              "бумажной рутины легче"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.set_styles()

    def onButtonMy(self):
        # self.textEdit.append("Нажата `Своя Кнопка`!")
        pass

    def set_connections(self):
        self.pushButton_omr.clicked.connect(self.open_omr_main_menu)
        self.pushButton_bta.clicked.connect(self.open_bta_main_menu)
        self.pushButton_almanac.clicked.connect(self.open_almanac)

    def set_styles(self):
        style = """
            QPushButton {
                background-color: rgba(112, 38, 50, 190);
                font-size: 11pt;
                color: White;
                border: None;
                padding-top: 30px;
                padding-bottom: 30px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton::hover {
                background-color: rgba(112, 38, 50, 255);
                border: 2px solid rgba(145, 47, 64, 255);
            }
            QPushButton::pressed {
                background-color: rgba(145, 47, 64, 255);
                border: 1px solid rgba(255, 255, 255, 255);
            }
            QPushButton::disabled {
                background-color: #EEEEEE;
                border: 1px solid rgba(112, 38, 50, 255);
            }
        """
        self.pushButton_omr.setStyleSheet(style)

    def create_main_window(self):
        return self.windows['Frameless']()

    def open_menu(self, case_type):
        win = self.create_main_window()
        win.setWidget(
            self.windows[case_type]['main_menu'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def open_almanac(self):
        win = self.create_main_window()
        win.setWidget(
            self.windows['common']['almanac'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def open_omr_main_menu(self):
        self.open_menu('omr')

    def open_bta_main_menu(self):
        self.open_menu('bta')
