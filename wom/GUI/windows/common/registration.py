from PySide6 import QtWidgets

from wom.GUI.PY.common import Registration
from wom.app_logic.checking_data import check_registation_data


class Ui_Registration(QtWidgets.QWidget, Registration.Ui_Registration):
    def __init__(self, windows, main_win):
        super().__init__()
        self.setupUi(self)
        self.windows = windows
        self.main_win = main_win

        main_win.setWindowTitle('')
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()

    def onButtonMy(self):
        pass

    def set_connections(self):
        self.pushButton_reg\
            .clicked.connect(self.registration)
        self.pushButton_verify_phone\
            .clicked.connect(self.verify_phone)
        self.pushButton_verify_phone_2\
            .clicked.connect(self.verify_phone)

        self.user_email\
            .textChanged.connect(self.set_login_as_email)
        self.checkBox_login_same_email\
            .stateChanged.connect(self.activate_login)

    def registration(self):
        data = {
            'email': self.user_email.text(),
            'phone': self.user_phone.text(),
            'login': self.user_login.text(),
            'password': self.user_password.text(),
            'password_2': self.user_password_2.text(),
            'surname': self.user_surname.text(),
            'name': self.user_name.text(),
            'dadname': self.user_dadname.text(),
            'b_day': self.dateEdit_user_bday.dateTime().toString('dd.MM.yyyy')
        }
        check_result = check_registation_data(data)

    def verify_phone(self):
        pass

    def set_login_as_email(self):
        if self.checkBox_login_same_email.isChecked():
            self.user_login.setText(
                self.user_email.text()
            )

    def activate_login(self):
        if self.checkBox_login_same_email.isChecked():
            self.user_login.setEnabled(False)
            self.set_login_as_email()
        else:
            self.user_login.setEnabled(True)
            self.user_login.setText('')
