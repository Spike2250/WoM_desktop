from PySide6 import QtCore, QtWidgets


class PushButton(QtWidgets.QPushButton):
    hover = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        pass

    def enterEvent(self, event):
        self.hover.emit("enterEvent")

    def leaveEvent(self, event):
        self.hover.emit("leaveEvent")
