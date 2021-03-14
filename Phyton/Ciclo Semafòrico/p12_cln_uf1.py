from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic, QtGui
import sys
import random

class p12_cln_uf1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/p12_cln_uf1.ui', self)
        self.setWindowTitle('Laberint')
        self.bt_nord_oest.setText("")
        self.bt_nord.setText("")
        self.bt_nord_est.setText("")
        self.bt_oest.setText("")
        self.bt_centre.setText("")
        self.bt_est.setText("")
        self.bt_sud_oest.setText("")
        self.bt_sud.setText("")
        self.bt_sud_est.setText("")
        self.fila = 3
        self.columna = 7
        self.posicio = (self.fila, self.columna)
        self.mapa= [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', 'X', '*', '*', '*', '*', '*', '*', '*']
            , ['*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*']
            , ['*', ' ', '*', '*', '*', ' ', '*', ' ', '*', '*', '*', '*', '*', ' ', '*', ' ', '*']
            , ['*', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', '*']
            , ['*', ' ', '*', ' ', '*', '*', '*', '*', '*', '*', '*', ' ', '*', ' ', '*', '*', '*']
            , ['*', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*']
            , ['*', '*', '*', ' ', '*', ' ', '*', '*', '*', '*', '*', ' ', '*', '*', '*', '*', '*']
            , ['*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*']
            , ['*', ' ', '*', '*', '*', '*', '*', ' ', '*', ' ', '*', '*', '*', ' ', '*', ' ', '*']
            , ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*']
            , ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        ]
        self.dicc_posicionbut = {'bt_nord_oest': (-1, -1), 'bt_nord': (-1, 0), 'bt_nord_est': (-1, 1), 'bt_oest': (0, -1),
                      'bt_centre': (0, 0), 'bt_est': (0, 1), 'bt_sud_oest': (1, -1), 'bt_sud': (1, 0),
                      'bt_sud_est': (1, 1)}
        self.dicc_posicionact = {(-1, -1): self.bt_nord_oest, (-1, 0): self.bt_nord, (-1, 1): self.bt_nord_est, (0, -1): self.bt_oest,
                               (0, 0): self.bt_centre, (0, 1): self.bt_est, (1, -1): self.bt_sud_oest, (1, 0): self.bt_sud,
                               (1, 1): self.bt_sud_est}
        self.preparar()
        for i in self.dicc_posicionact:
            self.dicc_posicionact[i].clicked.connect(self.click)
        self.show()

    def click(self):
        send = self.sender()
        bt_click =send.objectName()
        self.movimento(bt_click)

    def movimento(self,bt_click):
        if bt_click in self.dicc_posicionbut:
            self.fila = self.fila + self.dicc_posicionbut[bt_click][0]
            self.columna = self.columna + self.dicc_posicionbut[bt_click][1]
            if self.mapa[self.fila][self.columna] == 'X':
                self.ganar()
            self.posicio = (self.fila, self.columna)
            self.preparar()

    def preparar(self):
        icona_serpent = QIcon()
        icona_serpent.addPixmap(QPixmap("ui/snake-tongue.png"), QIcon.Disabled, QIcon.On)
        for i in range(-1, 2):
            for j in range(-1, 2):
                pos_bt_fila = self.fila + i
                pos_bt_columna = self.columna + j
                if self.mapa[pos_bt_fila][pos_bt_columna] == '*':
                    self.dicc_posicionact[(i, j)].setIcon(icona_serpent)
                    self.dicc_posicionact[(i, j)].setEnabled(False)
                elif self.mapa[pos_bt_fila][pos_bt_columna] == 'X':
                    self.dicc_posicionact[(i, j)].setIcon(QIcon(QPixmap("ui/dungeon-gate.png")))
                    self.dicc_posicionact[(i, j)].setEnabled(True)
                else:
                    self.dicc_posicionact[(i, j)].setIcon(QIcon(QPixmap()))
                    self.dicc_posicionact[(i, j)].setEnabled(True)
                self.dicc_posicionact[(i, j)].setIconSize(QSize(120, 120))

    def ganar(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.dicc_posicionact[(i, j)].setIcon(QIcon(QPixmap("ui/dungeon-gate.png")))
                self.dicc_posicionact[(i, j)].setEnabled(True)
        win_msg = QMessageBox()
        win_msg.setIcon(QMessageBox.Information)
        win_msg.setText("Has sortit del laberint!")
        win_msg.setWindowTitle("Felicitats")
        win_msg.setStandardButtons(QMessageBox.Ok)
        close = win_msg.exec()
        if close == QMessageBox.Ok:
            win_msg.close()
        self.new()

    def new(self):
        messagegame = QMessageBox()
        messagegame.setIcon(QMessageBox.Warning)
        messagegame.setText("Vols tornar a jugar una altre partida?")
        messagegame.setWindowTitle("Començar partida")
        messagegame.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        newgame = messagegame.exec()
        if newgame == QMessageBox.Yes:
            self.fila = random.randint(0, len(self.mapa)-1)
            self.columna = random.randint(0, len(self.mapa[0])-1)
            mapa = self.mapa[self.fila][self.columna];
            while mapa == "X" or mapa == "*":
                self.fila = random.randint(0, len(self.mapa)-1)
                self.columna = random.randint(0, len(self.mapa[0])-1)
                mapa = self.mapa[self.fila][self.columna];
            self.posicio = (self.fila, self.columna)
            self.preparar()
        else:
            self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setText("Vols sortir del joc?")
        mensaje.setWindowTitle("Sortir")
        mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        close = mensaje.exec()
        if close == QMessageBox.Yes:
            a0.accept()
        else:
            self.new()


app = QApplication(sys.argv)
win = p12_cln_uf1()
app.exec_()
