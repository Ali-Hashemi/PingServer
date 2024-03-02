import typing
import math

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets
from Classes.ClassUtility import *


class MySpinBox(QtWidgets.QSpinBox):
    FIXED_PRICE = 0
    IS_COLORED = 0
    LAST_CALCULATED_PRICE = 0
    LABEL_PRICE_BEFORE = None
    LABEL_PRICE_AFTER = None
    LABEL_PRICE_TOTAL_BEFORE = None
    LABEL_PRICE_TOTAL_AFTER = None
    WHOLE_PARENT = None

    def __init__(self, parent=None, selected_spinBox=None, whole_parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

        self.WHOLE_PARENT = whole_parent

        hidden_element = selected_spinBox[1]

        self.FIXED_PRICE = selected_spinBox[2]

        self.LABEL_PRICE_BEFORE = selected_spinBox[3]

        self.LABEL_PRICE_BEFORE.setText(str(format_int_with_commas(self.FIXED_PRICE)))

        self.LABEL_PRICE_AFTER = selected_spinBox[4]

        self.LABEL_PRICE_TOTAL_BEFORE = selected_spinBox[5]

        self.LABEL_PRICE_TOTAL_AFTER = selected_spinBox[6]

        self.IS_COLORED = selected_spinBox[7]

        self.setMaximum(9999)

        rect = QtCore.QRect(hidden_element.geometry().left(),
                            hidden_element.geometry().top(),
                            hidden_element.geometry().width(),
                            hidden_element.geometry().height())

        self.setGeometry(rect)

        self.setAlignment(QtCore.Qt.AlignCenter)

        self.setFont(CustomStyle.spinbox_font)

        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        self.textChanged.connect(
            lambda: (self.calc()))

    def calc(self):
        number_of_prints = int(self.text())

        final_price = self.FIXED_PRICE

        self.LABEL_PRICE_TOTAL_BEFORE.setText(str(format_int_with_commas(final_price * number_of_prints)))

        percent = int(self.WHOLE_PARENT.PERCENTAGE)

        final_percent = 100 - percent

        # if number_of_prints >= 20:
            # final_percent = 100 - (math.floor(number_of_prints / 20) * percent)

            # if final_percent < 10:
            #     final_percent = 10

            # final_price = math.floor(self.FIXED_PRICE * (final_percent / 100))

        final_price = self.floor(math.floor(self.FIXED_PRICE * (final_percent / 100)), 2)

        self.LAST_CALCULATED_PRICE = final_price * number_of_prints

        self.LABEL_PRICE_AFTER.setText(str(format_int_with_commas(final_price)))

        self.LABEL_PRICE_TOTAL_AFTER.setText(str(format_int_with_commas(self.LAST_CALCULATED_PRICE)))

        if number_of_prints < 1:
            self.LABEL_PRICE_AFTER.setText(str(0))

    def floor(self, value, power):
        digit_to_remove = pow(10, power)
        new_value = (math.floor(value / digit_to_remove)) * digit_to_remove

        return new_value

    def alaki(self):
        print("jamesoooo")
