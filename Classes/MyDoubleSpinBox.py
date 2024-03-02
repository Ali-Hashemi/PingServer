import typing
import math
from msvcrt import getch

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets
from Classes.ClassUtility import *


class MyDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    def __init__(self, parent=None, hidden_element: QtWidgets.QSpinBox = None):
        super().__init__(parent)
        self.setAcceptDrops(True)

        self.setMaximum(999)

        rect = QtCore.QRect(hidden_element.geometry().left(),
                            hidden_element.geometry().top(),
                            hidden_element.geometry().width(),
                            hidden_element.geometry().height())

        self.setDecimals(1)

        self.setGeometry(rect)

        self.setAlignment(QtCore.Qt.AlignCenter)

        self.setFont(CustomStyle.spinbox_font)

        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(e)

        key = e.key()
        if key == Qt.Key_Backspace:
            text = self.text()

            if not text:
                self.setValue(0)
