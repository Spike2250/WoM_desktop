from PySide6 import QtWidgets

from wom.GUI.PY.common import Login
# from wom.app_logic.db_func.users import login_check


class Ui_Login(QtWidgets.QWidget, Login.Ui_Login):
    def __init__(self, windows, main_win):
        super().__init__()
        self.setupUi(self)
        self.windows = windows
        self.main_win = main_win

        main_win.setWindowTitle('')
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        msg = 'Приветственное слово'
        self.textBrowser.setPlainText(msg)

        self.set_connections()

    def onButtonMy(self):
        pass

    def set_connections(self):
        self.pushButton_login\
            .clicked.connect(self.enter_to_programme)
        self.pushButton_registation\
            .clicked.connect(self.registration)
        self.pushButton_forget_password\
            .clicked.connect(self.forget_password)

    def registration(self):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['common']['registration'](
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def open_main_user_menu(self, user_info):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['common']['main_user_menu'](
                user_info=user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def enter_to_programme(self):
        # enter = login_check(login=self.user_name.text(),
        #                     password=self.user_password.text())
        if enter['result'] == 'success':
            self.open_main_user_menu(
                user_info=enter['user_info']
            )
        elif enter['result'] == 'wrong login':
            msg = 'Пользователя с таким логином не существует!'
            self.label_status.setText(msg)

        elif enter['result'] == 'wrong password':
            msg = 'Неверный пароль!'
            self.label_status.setText(msg)

        elif enter['result'] == 'not full data':
            msg = 'Логин и/или пароль не могут быть пустым!'
            self.label_status.setText(msg)

    def forget_password(self):
        pass
