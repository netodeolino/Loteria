# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaPrincipal.ui'
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

class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName(_fromUtf8("TelaPrincipal"))
        TelaPrincipal.resize(800, 600)
        self.centralwidget = QtGui.QWidget(TelaPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 271, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButtonLoginFormulario = QtGui.QPushButton(self.centralwidget)
        self.pushButtonLoginFormulario.setGeometry(QtCore.QRect(30, 480, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLoginFormulario.setFont(font)
        self.pushButtonLoginFormulario.setObjectName(_fromUtf8("pushButtonLoginFormulario"))
        self.pushButtonCadastrarFormulario = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCadastrarFormulario.setGeometry(QtCore.QRect(300, 480, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCadastrarFormulario.setFont(font)
        self.pushButtonCadastrarFormulario.setObjectName(_fromUtf8("pushButtonCadastrarFormulario"))
        self.pushButtonSair = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSair.setGeometry(QtCore.QRect(560, 480, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSair.setFont(font)
        self.pushButtonSair.setObjectName(_fromUtf8("pushButtonSair"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 330, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 50, 241, 241))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Downloads/PARA REDES/loteria.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2.raise_()
        self.pushButtonCadastrarFormulario.raise_()
        self.pushButtonLoginFormulario.raise_()
        self.pushButtonSair.raise_()
        self.label_3.raise_()
        self.label.raise_()
        TelaPrincipal.setCentralWidget(self.centralwidget)
        self.actionInicio = QtGui.QAction(TelaPrincipal)
        self.actionInicio.setObjectName(_fromUtf8("actionInicio"))
        self.actionSair = QtGui.QAction(TelaPrincipal)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionSair_2 = QtGui.QAction(TelaPrincipal)
        self.actionSair_2.setObjectName(_fromUtf8("actionSair_2"))
        self.actionCadastre_se = QtGui.QAction(TelaPrincipal)
        self.actionCadastre_se.setObjectName(_fromUtf8("actionCadastre_se"))
        self.actionLogin = QtGui.QAction(TelaPrincipal)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))

        self.retranslateUi(TelaPrincipal)
        QtCore.QObject.connect(self.pushButtonLoginFormulario, QtCore.SIGNAL(_fromUtf8("clicked()")), TelaPrincipal.logarFormulario)
        QtCore.QObject.connect(self.pushButtonCadastrarFormulario, QtCore.SIGNAL(_fromUtf8("clicked()")), TelaPrincipal.cadastrarFormulario)
        QtCore.QObject.connect(self.pushButtonSair, QtCore.SIGNAL(_fromUtf8("clicked()")), TelaPrincipal.sair)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)

    def retranslateUi(self, TelaPrincipal):
        TelaPrincipal.setWindowTitle(_translate("TelaPrincipal", "Loteria", None))
        self.label_2.setText(_translate("TelaPrincipal", "Loteria", None))
        self.pushButtonLoginFormulario.setText(_translate("TelaPrincipal", "Login", None))
        self.pushButtonCadastrarFormulario.setText(_translate("TelaPrincipal", "Cadastre-se", None))
        self.pushButtonSair.setText(_translate("TelaPrincipal", "Sair", None))
        self.label_3.setText(_translate("TelaPrincipal", "Bem vindo!", None))
        self.actionInicio.setText(_translate("TelaPrincipal", "Inicio", None))
        self.actionSair.setText(_translate("TelaPrincipal", "Sair", None))
        self.actionSair_2.setText(_translate("TelaPrincipal", "Sair", None))
        self.actionCadastre_se.setText(_translate("TelaPrincipal", "Cadastro", None))
        self.actionLogin.setText(_translate("TelaPrincipal", "Login", None))


