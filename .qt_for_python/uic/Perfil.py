# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\projetoSCO\TELAS.PY\Perfil.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 489)
        Dialog.setStyleSheet("background-color: rgb(170, 197, 255);")
        self.Back_Lista = QtWidgets.QLabel(Dialog)
        self.Back_Lista.setGeometry(QtCore.QRect(-10, -10, 211, 501))
        self.Back_Lista.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.Back_Lista.setText("")
        self.Back_Lista.setObjectName("Back_Lista")
        self.Img_User = QtWidgets.QLabel(Dialog)
        self.Img_User.setGeometry(QtCore.QRect(50, 0, 81, 91))
        self.Img_User.setStyleSheet("image: url(:/img/USUARIO.png);\n"
"background-color: rgb(113, 229, 231);")
        self.Img_User.setText("")
        self.Img_User.setObjectName("Img_User")
        self.NomeUsuario = QtWidgets.QLabel(Dialog)
        self.NomeUsuario.setGeometry(QtCore.QRect(10, 90, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.NomeUsuario.setFont(font)
        self.NomeUsuario.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.NomeUsuario.setAlignment(QtCore.Qt.AlignCenter)
        self.NomeUsuario.setObjectName("NomeUsuario")
        self.l_sejabemvindo = QtWidgets.QLabel(Dialog)
        self.l_sejabemvindo.setGeometry(QtCore.QRect(330, 20, 291, 41))
        self.l_sejabemvindo.setObjectName("l_sejabemvindo")
        self.NomeUsuario_Meio = QtWidgets.QLabel(Dialog)
        self.NomeUsuario_Meio.setGeometry(QtCore.QRect(310, 60, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.NomeUsuario_Meio.setFont(font)
        self.NomeUsuario_Meio.setAlignment(QtCore.Qt.AlignCenter)
        self.NomeUsuario_Meio.setObjectName("NomeUsuario_Meio")
        self.B_MeusObjetivos = QtWidgets.QPushButton(Dialog)
        self.B_MeusObjetivos.setEnabled(True)
        self.B_MeusObjetivos.setGeometry(QtCore.QRect(0, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_MeusObjetivos.setFont(font)
        self.B_MeusObjetivos.setToolTipDuration(-1)
        self.B_MeusObjetivos.setStyleSheet("background-color: rgb(198, 255, 253);")
        self.B_MeusObjetivos.setObjectName("B_MeusObjetivos")
        self.B_NovoObjetivo = QtWidgets.QPushButton(Dialog)
        self.B_NovoObjetivo.setEnabled(True)
        self.B_NovoObjetivo.setGeometry(QtCore.QRect(0, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_NovoObjetivo.setFont(font)
        self.B_NovoObjetivo.setToolTipDuration(-1)
        self.B_NovoObjetivo.setStyleSheet("background-color: rgb(198, 255, 253);")
        self.B_NovoObjetivo.setObjectName("B_NovoObjetivo")
        self.B_Sair = QtWidgets.QPushButton(Dialog)
        self.B_Sair.setGeometry(QtCore.QRect(10, 440, 41, 23))
        self.B_Sair.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.B_Sair.setObjectName("B_Sair")
        self.B_Conf_Conta = QtWidgets.QPushButton(Dialog)
        self.B_Conf_Conta.setGeometry(QtCore.QRect(10, 420, 131, 23))
        self.B_Conf_Conta.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.B_Conf_Conta.setObjectName("B_Conf_Conta")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.NomeUsuario.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.l_sejabemvindo.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt;\">SEJA BEM-VINDO</span></p><p><br/></p></body></html>"))
        self.NomeUsuario_Meio.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.B_MeusObjetivos.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Meus Objetivos</span></p></body></html>"))
        self.B_MeusObjetivos.setText(_translate("Dialog", "Meus Objetivos"))
        self.B_NovoObjetivo.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Meus Objetivos</span></p></body></html>"))
        self.B_NovoObjetivo.setText(_translate("Dialog", "Novo Objetivo"))
        self.B_Sair.setText(_translate("Dialog", "Sair"))
        self.B_Conf_Conta.setText(_translate("Dialog", "Configurações de conta"))
import sourcee_rc
