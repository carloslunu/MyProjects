import locale

from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys

locale.setlocale(locale.LC_ALL, "")


class Exercici11(QMainWindow):
    locale.setlocale(locale.LC_ALL, "")

    def __init__(self):
        super().__init__()
        uic.loadUi('ejercicios/ui/p11clnuf1.ui', self)
        self.show()
        self.setWindowTitle("Calculadora")
        self.bt_calcular.clicked.connect(self.resultado)
        self.validator()
        self.rb_enter.toggled.connect(self.boton)


    def resultado(self):
        self.le_num3.setValidator(self.decimal)
        if self.rb_suma.isChecked():
            t1 = self.le_num1.text()
            t2 = self.le_num2.text()
            if self.rb_decimal.isChecked():
                s1 = locale.atof(t1)
                s2 = locale.atof(t2)
                r = s1 + s2
                rs = str(r)
                self.le_num3.setText(rs)
            elif self.rb_enter.isChecked():
                s1 = locale.atoi(t1)
                s2 = locale.atoi(t2)
                r = s1 + s2
                rs = str(r)
                self.le_num3.setText(rs)

        if self.rb_resta.isChecked():
            t1 = self.le_num1.text()
            t2 = self.le_num2.text()
            if self.rb_decimal.isChecked():
                s1 = locale.atof(t1)
                s2 = locale.atof(t2)
                r = s1 - s2
                rs = str(r)
                self.le_num3.setText(rs)
            elif self.rb_enter.isChecked():
                s1 = locale.atoi(t1)
                s2 = locale.atoi(t2)
                r = s1 - s2
                rs = str(r)
                self.le_num3.setText(rs)

        if self.rb_producte.isChecked():
            t1 = self.le_num1.text()
            t2 = self.le_num2.text()
            if self.rb_decimal.isChecked():
                s1 = locale.atof(t1)
                s2 = locale.atof(t2)
                r = s1 * s2
                rs = str(r)
                self.le_num3.setText(rs)
            elif self.rb_enter.isChecked():
                s1 = locale.atoi(t1)
                s2 = locale.atoi(t2)
                r = s1 * s2
                rs = str(r)
                self.le_num3.setText(rs)

        if self.rb_divisio.isChecked():
            t1 = self.le_num1.text()
            t2 = self.le_num2.text()
            s1 = locale.atoi(t1)
            s2 = locale.atoi(t2)
            r = s1 / s2
            rs = str(r)
            self.le_num3.setText(rs)
            if self.rb_decimal.isChecked():
                s1 = locale.atof(t1)
                s2 = locale.atof(t2)
                r = s1 / s2
                rs = str(r)
                self.le_num3.setText(rs)
            elif self.rb_enter.isChecked():
                s1 = locale.atoi(t1)
                s2 = locale.atoi(t2)
                r = s1 / s2
                rs = str(r)
                self.le_num3.setText(rs)

    def validator(self):
        self.entero = QIntValidator()
        self.decimal = QDoubleValidator()
        self.le_num1.setValidator(self.decimal)
        self.le_num2.setValidator(self.decimal)
        self.le_num3.setValidator(self.decimal)

    def boton(self):
        if self.rb_decimal.isChecked():
            self.decimal = QDoubleValidator()
            self.le_num1.setValidator(self.decimal)
            self.le_num2.setValidator(self.decimal)
            self.le_num3.setValidator(self.decimal)
            t1 = self.le_num1.text()
            t2 = self.le_num2.text()
            s1 = locale.atof(t1)
            s2 = locale.atof(t2)
            s1s = str(s1)
            s2s = str(s2)
            self.le_num1.setText(s1s)
            self.le_num2.setText(s2s)

            if self.rb_enter.isChecked():
                self.entero = QIntValidator()
                self.le_num1.setValidator(self.entero)
                self.le_num2.setValidator(self.entero)
                self.le_num3.setValidator(self.entero)
                t1 = self.le_num1.text()
                t2 = self.le_num2.text()
                s1 = locale.atoi(t1)
                s2 = locale.atoi (t2)
                s1s = str(s1)
                s2s = str(s2)
                self.le_num1.setText(s1s)
                self.le_num2.setText(s2s)
                self.le_num1.setText(s1)
                self.le_num2.setText(s2)

app = QApplication(sys.argv)
win = Exercici11()
app.exec_()
