import sys  # sys нужен для передачи argv в QApplication
from PySide6 import QtWidgets
from wom.GUI.windows.win_aggregator import windows


StyleSheet = """
/* Панель заголовка */
                TitleBar {
                    background-color: rgb(50, 98, 115);
                    font-family: Roboto;
                    font-size: 11pt;
                    color: white;
                }
/* Минимизировать кнопку `Максимальное выключение` Общий фон по умолчанию */
                #buttonMinimum,
                #buttonMaximum,
                #buttonClose,
                #buttonMy {
                    border: none;
                    background-color: transparent;
                }
/* Зависание */
                #buttonMinimum:hover,
                #buttonMaximum:hover,
                #buttonMy:hover {
                    color: white;
                    background-color: rgb(92, 158, 173);
                }
                #buttonClose:hover {
                    color: white;
                    background-color: rgb(232, 17, 35);
                }
/* Мышь удерживать */
                #buttonMinimum:pressed,
                #buttonMaximum:pressed,
                #buttonMy:pressed {
                    background-color: rgb(220, 220, 220);
                }
                #buttonClose:pressed {
                    color: white;
                    background-color: rgb(161, 73, 92);
                }
"""


def show():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    main_win = windows['Frameless']()
    # main_win.setWindowIcon(QIcon('Qt.ico'))\

    user_info = {}  # ВРЕМЕННО ДЛЯ ОТКРЫТИЯ БЕЗ АВТОРИЗАЦИИ
    # добавление своего окна в главное (через FramelessWindow.setWidget)
    main_win.setWidget(
        windows['common']['entry'](
            user_info=user_info,  # ВРЕМЕННО
            windows=windows,
            main_win=main_win))
    main_win.show()
    sys.exit(app.exec())

    # main_win.setWidget(
    #     windows['common']['login'](
    #         windows=windows,
    #         main_win=main_win))
    # main_win.show()
    # sys.exit(app.exec_())
