from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys


class p10_cln_uf1(QMainWindow):
    abecedario = "abcçdefghijklmnñopqrstuvwxyz"

    def __init__(self, title):
        super().__init__()
        uic.loadUi('ui/p10_cln_uf1.ui', self)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle(titol)
        self.bt_xifrar.clicked.connect(self.xifrar)
        self.bt_desxifrar.clicked.connect(self.desxifrar)
        self.sb_clau.setValue(11)
        self.show()

    def xifrar(self):
        clave = self.sb_clau.value()
        textoDes = self.te_desxifrat.toPlainText()
        if textoDes == "":
            return
        cifrado = ''

        for i in textoDes:
            if i in self.abecedario:
                pos_letra = self.abecedario.index(i)
                nueva_pos = (pos_letra + clave) % len(self.abecedario)
                cifrado += self.abecedario[nueva_pos]

            else:
                if i.isupper():
                    pos_letra = self.abecedario.index(i.lower())
                    nueva_pos = (pos_letra + clave) % len(self.abecedario)
                    nueva_letra = self.abecedario[nueva_pos].upper()
                    cifrado += nueva_letra
                else:
                    cifrado += i

        if self.cb_majuscules.isChecked():
            cifrado = cifrado.upper()
        self.te_xifrat.clear()
        self.te_xifrat.insertPlainText(cifrado)

    def desxifrar(self):
        clave = self.sb_clau.value()
        textCod = self.te_xifrat.toPlainText()
        if textCod == "":
            return

        descifrado = ''
        claveNegativa = -clave

        for i in textCod:
            if i in self.abecedario:
                pos_letra = self.abecedario.index(i)
                nueva_pos = (pos_letra + claveNegativa) % len(self.abecedario)
                descifrado += self.abecedario[nueva_pos]
            else:
                if i.isupper():
                    pos_letra = self.abecedario.index(i.lower())
                    nueva_pos = (pos_letra + claveNegativa) % len(self.abecedario)
                    nueva_letra = self.abecedario[nueva_pos].upper()
                    descifrado += nueva_letra
                else:
                    descifrado += i

        if self.cb_majuscules.isChecked():
            descifrado = descifrado.upper()
        self.te_desxifrat.clear()
        self.te_desxifrat.insertPlainText(descifrado)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


app = QApplication(sys.argv)
titol = "El Xifrador/Desxifrador"
win = p10_cln_uf1(titol)
app.exec_()