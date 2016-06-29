# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaApostar.ui'
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

class Ui_TelaApostar(object):
    def setupUi(self, TelaApostar):
        TelaApostar.setObjectName(_fromUtf8("TelaApostar"))
        TelaApostar.resize(800, 600)
        self.centralwidget = QtGui.QWidget(TelaApostar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 40, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButtonInicio = QtGui.QPushButton(self.centralwidget)
        self.pushButtonInicio.setGeometry(QtCore.QRect(0, 0, 98, 27))
        self.pushButtonInicio.setObjectName(_fromUtf8("pushButtonInicio"))
        TelaApostar.setCentralWidget(self.centralwidget)
        self.actionIn_cio = QtGui.QAction(TelaApostar)
        self.actionIn_cio.setObjectName(_fromUtf8("actionIn_cio"))
        self.actionSair = QtGui.QAction(TelaApostar)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionComo_Apostar = QtGui.QAction(TelaApostar)
        self.actionComo_Apostar.setObjectName(_fromUtf8("actionComo_Apostar"))

        self.retranslateUi(TelaApostar)
        QtCore.QObject.connect(self.pushButtonInicio, QtCore.SIGNAL(_fromUtf8("clicked()")), TelaApostar.inicio)
        QtCore.QMetaObject.connectSlotsByName(TelaApostar)

    def retranslateUi(self, TelaApostar):
        TelaApostar.setWindowTitle(_translate("TelaApostar", "Apostas", None))
        self.label.setText(_translate("TelaApostar", "IDÉIAS?", None))
        self.pushButtonInicio.setText(_translate("TelaApostar", "Início", None))
        self.actionIn_cio.setText(_translate("TelaApostar", "Início", None))
        self.actionSair.setText(_translate("TelaApostar", "Sair", None))
        self.actionComo_Apostar.setText(_translate("TelaApostar", "Como Apostar", None))

