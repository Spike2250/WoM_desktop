
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
# from PySide6.QtCore import Signal

from wom.GUI.windows.FramelessWindow import FramelessWindow


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        objectTitleBar = args[0].titleBar

        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QPushButton('Кнопка', self))
        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)

        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

    def onButtonMy(self):
        # self.textEdit.append("Нажата `Своя Кнопка`!")
        pass


# стиль
StyleSheet = """
/* Панель заголовка */
                TitleBar {
                    background-color: rgb(54, 157, 180);
                }
/* Минимизировать кнопку `Максимальное выключение` Общий фон по умолчанию */
                #buttonMinimum,#buttonMaximum,#buttonClose, #buttonMy {
                    border: none;
                    background-color: rgb(54, 157, 180);
                }
/* Зависание */
                #buttonMinimum:hover,#buttonMaximum:hover {
                    background-color: rgb(48, 141, 162);
                }
                #buttonClose:hover {
                    color: white;
                    background-color: rgb(232, 17, 35);
                }
                #buttonMy:hover {
                    color: white;
                    background-color: green;   /* rgb(232, 17, 35) */
                }
/* Мышь удерживать */
                #buttonMinimum:pressed,#buttonMaximum:pressed {
                    background-color: rgb(44, 125, 144);
                }
                #buttonClose:pressed {
                    color: white;
                    background-color: rgb(161, 73, 92);
                }
                """

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    w = FramelessWindow()
    w.setWindowTitle('Тестовая строка заголовка')
    w.setWindowIcon(QIcon('Qt.ico'))
    w.setWidget(MainWindow(w))          # Добавить свое окно
    w.show()
    sys.exit(app.exec_())
