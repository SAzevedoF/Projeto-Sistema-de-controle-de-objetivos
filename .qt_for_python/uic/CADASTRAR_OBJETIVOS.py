# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\projetoSCO\TELAS.PY\CADASTRAR_OBJETIVOS.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(822, 596)
        Dialog.setStyleSheet("background-color: rgb(170, 197, 255);")
        self.B_Conf_Conta = QtWidgets.QPushButton(Dialog)
        self.B_Conf_Conta.setGeometry(QtCore.QRect(0, 510, 161, 23))
        self.B_Conf_Conta.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.B_Conf_Conta.setObjectName("B_Conf_Conta")
        self.B_NovoObjetivo = QtWidgets.QPushButton(Dialog)
        self.B_NovoObjetivo.setEnabled(True)
        self.B_NovoObjetivo.setGeometry(QtCore.QRect(0, 190, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_NovoObjetivo.setFont(font)
        self.B_NovoObjetivo.setToolTipDuration(-1)
        self.B_NovoObjetivo.setStyleSheet("background-color: rgb(198, 255, 253);")
        self.B_NovoObjetivo.setObjectName("B_NovoObjetivo")
        self.Img_User = QtWidgets.QLabel(Dialog)
        self.Img_User.setGeometry(QtCore.QRect(70, 10, 81, 91))
        self.Img_User.setStyleSheet("image: url(:/img/USUARIO.png);\n"
"background-color: rgb(113, 229, 231);")
        self.Img_User.setText("")
        self.Img_User.setObjectName("Img_User")
        self.Back_Lista = QtWidgets.QLabel(Dialog)
        self.Back_Lista.setGeometry(QtCore.QRect(0, 0, 221, 581))
        self.Back_Lista.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.Back_Lista.setText("")
        self.Back_Lista.setObjectName("Back_Lista")
        self.B_Sair = QtWidgets.QPushButton(Dialog)
        self.B_Sair.setGeometry(QtCore.QRect(0, 540, 41, 23))
        self.B_Sair.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.B_Sair.setObjectName("B_Sair")
        self.B_MeusObjetivos = QtWidgets.QPushButton(Dialog)
        self.B_MeusObjetivos.setEnabled(True)
        self.B_MeusObjetivos.setGeometry(QtCore.QRect(0, 150, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_MeusObjetivos.setFont(font)
        self.B_MeusObjetivos.setToolTipDuration(-1)
        self.B_MeusObjetivos.setStyleSheet("background-color: rgb(198, 255, 253);")
        self.B_MeusObjetivos.setObjectName("B_MeusObjetivos")
        self.NomeUsuario = QtWidgets.QLabel(Dialog)
        self.NomeUsuario.setGeometry(QtCore.QRect(60, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.NomeUsuario.setFont(font)
        self.NomeUsuario.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.NomeUsuario.setObjectName("NomeUsuario")
        self.L_CAD_OBJ = QtWidgets.QLabel(Dialog)
        self.L_CAD_OBJ.setGeometry(QtCore.QRect(360, 10, 221, 41))
        self.L_CAD_OBJ.setObjectName("L_CAD_OBJ")
        self.L_back_meio = QtWidgets.QLabel(Dialog)
        self.L_back_meio.setGeometry(QtCore.QRect(290, 50, 391, 461))
        self.L_back_meio.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_back_meio.setText("")
        self.L_back_meio.setObjectName("L_back_meio")
        self.B_cadastrar = QtWidgets.QPushButton(Dialog)
        self.B_cadastrar.setGeometry(QtCore.QRect(420, 530, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.B_cadastrar.setFont(font)
        self.B_cadastrar.setStyleSheet("background-color: rgb(113, 229, 231);\n"
"color: rgb(255, 255, 255);")
        self.B_cadastrar.setObjectName("B_cadastrar")
        self.L_materia = QtWidgets.QLabel(Dialog)
        self.L_materia.setGeometry(QtCore.QRect(330, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.L_materia.setFont(font)
        self.L_materia.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_materia.setObjectName("L_materia")
        self.L_assunto = QtWidgets.QLabel(Dialog)
        self.L_assunto.setGeometry(QtCore.QRect(320, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.L_assunto.setFont(font)
        self.L_assunto.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_assunto.setObjectName("L_assunto")
        self.L_objetivo1 = QtWidgets.QLabel(Dialog)
        self.L_objetivo1.setGeometry(QtCore.QRect(310, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.L_objetivo1.setFont(font)
        self.L_objetivo1.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_objetivo1.setObjectName("L_objetivo1")
        self.C_materia = QtWidgets.QLineEdit(Dialog)
        self.C_materia.setGeometry(QtCore.QRect(400, 79, 261, 31))
        self.C_materia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_materia.setObjectName("C_materia")
        self.C_assunto = QtWidgets.QLineEdit(Dialog)
        self.C_assunto.setGeometry(QtCore.QRect(400, 130, 261, 31))
        self.C_assunto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_assunto.setObjectName("C_assunto")
        self.C_Objetivo1 = QtWidgets.QLineEdit(Dialog)
        self.C_Objetivo1.setGeometry(QtCore.QRect(400, 180, 261, 31))
        self.C_Objetivo1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_Objetivo1.setObjectName("C_Objetivo1")
        self.L_RC_A1 = QtWidgets.QLabel(Dialog)
        self.L_RC_A1.setGeometry(QtCore.QRect(440, 210, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_RC_A1.setFont(font)
        self.L_RC_A1.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_RC_A1.setObjectName("L_RC_A1")
        self.C_RC_A1 = QtWidgets.QLineEdit(Dialog)
        self.C_RC_A1.setGeometry(QtCore.QRect(400, 230, 261, 31))
        self.C_RC_A1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_RC_A1.setObjectName("C_RC_A1")
        self.L_RC_B1 = QtWidgets.QLabel(Dialog)
        self.L_RC_B1.setGeometry(QtCore.QRect(440, 260, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_RC_B1.setFont(font)
        self.L_RC_B1.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_RC_B1.setObjectName("L_RC_B1")
        self.C_RC_B1 = QtWidgets.QLineEdit(Dialog)
        self.C_RC_B1.setGeometry(QtCore.QRect(400, 280, 261, 31))
        self.C_RC_B1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_RC_B1.setObjectName("C_RC_B1")
        self.L_objetivo2 = QtWidgets.QLabel(Dialog)
        self.L_objetivo2.setGeometry(QtCore.QRect(300, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.L_objetivo2.setFont(font)
        self.L_objetivo2.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_objetivo2.setObjectName("L_objetivo2")
        self.C_objetivo2 = QtWidgets.QLineEdit(Dialog)
        self.C_objetivo2.setGeometry(QtCore.QRect(400, 330, 261, 31))
        self.C_objetivo2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_objetivo2.setObjectName("C_objetivo2")
        self.L_RC_A2 = QtWidgets.QLabel(Dialog)
        self.L_RC_A2.setGeometry(QtCore.QRect(430, 370, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_RC_A2.setFont(font)
        self.L_RC_A2.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_RC_A2.setObjectName("L_RC_A2")
        self.C_RC_A2 = QtWidgets.QLineEdit(Dialog)
        self.C_RC_A2.setGeometry(QtCore.QRect(400, 400, 261, 31))
        self.C_RC_A2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_RC_A2.setObjectName("C_RC_A2")
        self.L_RC_B2 = QtWidgets.QLabel(Dialog)
        self.L_RC_B2.setGeometry(QtCore.QRect(430, 440, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_RC_B2.setFont(font)
        self.L_RC_B2.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.L_RC_B2.setObjectName("L_RC_B2")
        self.C_RC_B2 = QtWidgets.QLineEdit(Dialog)
        self.C_RC_B2.setGeometry(QtCore.QRect(400, 460, 261, 31))
        self.C_RC_B2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_RC_B2.setObjectName("C_RC_B2")
        self.Back_Lista.raise_()
        self.B_Conf_Conta.raise_()
        self.B_NovoObjetivo.raise_()
        self.Img_User.raise_()
        self.B_Sair.raise_()
        self.B_MeusObjetivos.raise_()
        self.NomeUsuario.raise_()
        self.L_CAD_OBJ.raise_()
        self.L_back_meio.raise_()
        self.B_cadastrar.raise_()
        self.L_materia.raise_()
        self.L_assunto.raise_()
        self.L_objetivo1.raise_()
        self.C_materia.raise_()
        self.C_assunto.raise_()
        self.C_Objetivo1.raise_()
        self.L_RC_A1.raise_()
        self.C_RC_A1.raise_()
        self.L_RC_B1.raise_()
        self.C_RC_B1.raise_()
        self.L_objetivo2.raise_()
        self.C_objetivo2.raise_()
        self.L_RC_A2.raise_()
        self.C_RC_A2.raise_()
        self.L_RC_B2.raise_()
        self.C_RC_B2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.B_Conf_Conta.setText(_translate("Dialog", "Configurações de conta"))
        self.B_NovoObjetivo.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Meus Objetivos</span></p></body></html>"))
        self.B_NovoObjetivo.setText(_translate("Dialog", "Novo Objetivo"))
        self.B_Sair.setText(_translate("Dialog", "Sair"))
        self.B_MeusObjetivos.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Meus Objetivos</span></p></body></html>"))
        self.B_MeusObjetivos.setText(_translate("Dialog", "Meus Objetivos"))
        self.NomeUsuario.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.L_CAD_OBJ.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Cadastrar Objetivos</span></p></body></html>"))
        self.B_cadastrar.setText(_translate("Dialog", "Cadastrar"))
        self.L_materia.setText(_translate("Dialog", "Matéria:"))
        self.L_assunto.setText(_translate("Dialog", "Assunto:"))
        self.L_objetivo1.setText(_translate("Dialog", "Objetivo1:"))
        self.L_RC_A1.setText(_translate("Dialog", "Resultado-Chave a"))
        self.L_RC_B1.setText(_translate("Dialog", "Resultado-Chave b"))
        self.L_objetivo2.setText(_translate("Dialog", "Objetivo2:"))
        self.L_RC_A2.setText(_translate("Dialog", "Resultado-Chave a"))
        self.L_RC_B2.setText(_translate("Dialog", "Resultado-Chave b"))
import sourcee_rc
