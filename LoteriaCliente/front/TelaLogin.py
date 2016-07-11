# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaLogin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName(_fromUtf8("TelaLogin"))
        TelaLogin.resize(800, 312)
        self.centralwidget = QtGui.QWidget(TelaLogin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 10, 211, 281))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Downloads/PARA REDES/login.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditLogin = QtGui.QLineEdit(self.centralwidget)
        self.lineEditLogin.setGeometry(QtCore.QRect(130, 60, 291, 27))
        self.lineEditLogin.setObjectName(_fromUtf8("lineEditLogin"))
        self.lineEditSenha = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSenha.setGeometry(QtCore.QRect(130, 130, 291, 27))
        self.lineEditSenha.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditSenha.setObjectName(_fromUtf8("lineEditSenha"))
        self.pushButtonLogar = QtGui.QPushButton(self.centralwidget)
        self.pushButtonLogar.setGeometry(QtCore.QRect(60, 200, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogar.setFont(font)
        self.pushButtonLogar.setObjectName(_fromUtf8("pushButtonLogar"))
        self.pushButtonSairLogin = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSairLogin.setGeometry(QtCore.QRect(330, 200, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSairLogin.setFont(font)
        self.pushButtonSairLogin.setObjectName(_fromUtf8("pushButtonSairLogin"))
        self.pushButtonInicio = QtGui.QPushButton(self.centralwidget)
        self.pushButtonInicio.setGeometry(QtCore.QRect(0, 0, 98, 27))
        self.pushButtonInicio.setObjectName(_fromUtf8("pushButtonInicio"))
        TelaLogin.setCentralWidget(self.centralwidget)
        self.actionInicio = QtGui.QAction(TelaLogin)
        self.actionInicio.setObjectName(_fromUtf8("actionInicio"))
        self.actionSair = QtGui.QAction(TelaLogin)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionCadastro = QtGui.QAction(TelaLogin)
        self.actionCadastro.setObjectName(_fromUtf8("actionCadastro"))

        self.retranslateUi(TelaLogin)
        QtCore.QObject.connect(self.pushButtonLogar, QtCore.SIGNAL(_fromUtf8("clicked()")), TelaLogin.logar)
        QtCore.QObject.connect(self.pushButtonSairLogin, QtCore.SIGNAL(_fromUtf8("clicked()")), TelaLogin.sairLogin)
        QtCore.QObject.connect(self.pushButtonInicio, QtCore.SIGNAL(_fromUtf8("clicked()")), TelaLogin.inicio)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

    def retranslateUi(self, TelaLogin):
        TelaLogin.setWindowTitle(_translate("TelaLogin", "Login", None))
        self.label_2.setText(_translate("TelaLogin", "Login:", None))
        self.label_3.setText(_translate("TelaLogin", "Senha:", None))
        self.pushButtonLogar.setText(_translate("TelaLogin", "Logar", None))
        self.pushButtonSairLogin.setText(_translate("TelaLogin", "Sair", None))
        self.pushButtonInicio.setText(_translate("TelaLogin", "Início", None))
        self.actionInicio.setText(_translate("TelaLogin", "Início", None))
        self.actionSair.setText(_translate("TelaLogin", "Sair", None))
        self.actionCadastro.setText(_translate("TelaLogin", "Cadastro", None))

