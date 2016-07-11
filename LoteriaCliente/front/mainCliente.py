#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from TelaPrincipal import *
from TelaCadastro import *
from TelaLogin import *
from TelaApostar import *
from ConexaoCliente import *
from PyQt4 import QtGui, QtCore


class Person(object):
    def __init__(self, id_pessoa, nome, idade, cpf, endereco, login, senha, email, cartao, conta, acao):
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.login = login
        self.senha = senha
        self.email = email
        self.cartao = cartao
        self.conta = conta
        self.acao = acao


class Aposta(object):
    def __init__(self, id_aposta, campo1, campo2, campo3, campo4, campo5, campo6, id_pessoa, acao):
        self.id_aposta = id_aposta
        self.campo1 = campo1
        self.campo2 = campo2
        self.campo3 = campo3
        self.campo4 = campo4
        self.campo5 = campo5
        self.campo6 = campo6
        self.id_pessoa = id_pessoa
        self.acao = acao


class classePrincipalCliente(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.tela_principal = Ui_TelaPrincipal()
        self.tela_cadastro = Ui_TelaCadastro()
        self.tela_login = Ui_TelaLogin()
        self.tela_apostar = Ui_TelaApostar()

        self.conexao = Conectar()
        self.tcp = self.conexaoTCPCliente()

        self.id_pessoaM = None

        self.tela_principal.setupUi(self)



    def conexaoTCPCliente(self):
        tcp = self.conexao.conectar()
        return tcp



    def logarFormulario(self):
        self.tela_login.setupUi(self)



    def cadastrarFormulario(self):
        self.tela_cadastro.setupUi(self)



    def cadastrar(self):
        nome = self.tela_cadastro.lineEditNome.text()
        idade = self.tela_cadastro.lineEditIdade.text()
        cpf = self.tela_cadastro.lineEditCPF.text()
        endereco = self.tela_cadastro.lineEditEndereco.text()
        login = self.tela_cadastro.lineEditLogin.text()
        senha = self.tela_cadastro.lineEditSenha.text()
        email = self.tela_cadastro.lineEditEmail.text()
        cartao = self.tela_cadastro.comboBoxCartao.currentText()
        conta = self.tela_cadastro.lineEditConta.text()

        if nome == '' or idade == '' or cpf == '' or endereco == '' or login == '' or senha == '' or email == '' or cartao == '' or conta == '':
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Algum campo ficou em branco")
            msg.setInformativeText(self.trUtf8("Entenda melhor:"))
            msg.setWindowTitle("Campo em branco")
            msg.setDetailedText(self.trUtf8("Esteja ciente de que preencheu todos os campos necessários para realizar o Cadastro."))
            msg.exec_()
            self.tela_cadastro.setupUi(self)
        else:
            tcp = self.tcp

            pessoa = Person(None, nome, idade, cpf, endereco, login, senha, email, cartao, conta, 'CADASTRAR')

            resposta = self.conexao.serializarEnviarObjeto(tcp, pessoa)

            if resposta.acao == 'CADASTRADO':
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setText("Cadastro Realizado com Sucesso!")
                msg.setWindowTitle("Cadastro Realizado")
                msg.exec_()
                self.tela_login.setupUi(self)
            else:
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setText("Algum erro inesperado aconteceu, Tente Novamente!")
                msg.setWindowTitle("Aconteceu um Erro")
                msg.exec_()
                self.tela_cadastro.setupUi(self)



    def sairCadastro(self):
        self.tela_principal.setupUi(self)



    def inicio(self):
        self.tela_principal.setupUi(self)


    def sair(self):
        self.close()



    def logar(self):
        senha = self.tela_login.lineEditSenha.text()
        login = self.tela_login.lineEditLogin.text()

        if senha == '' or login == '':
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Login e/ou Senha em branco")
            msg.setInformativeText(self.trUtf8("Entenda melhor:"))
            msg.setWindowTitle("Campo em branco")
            msg.setDetailedText(self.trUtf8("Esteja ciente de que preencheu todos os campos para realizar o login."))
            msg.exec_()
            self.tela_login.setupUi(self)
        else:
            tcp = self.tcp

            pessoa = Person(None, None, None, None, None, login, senha, None, None, None, 'LOGAR')
            resposta = self.conexao.serializarEnviarObjeto(tcp, pessoa)

            if resposta.acao == 'LOGADO':
                self.id_pessoaM = resposta.id_pessoa

                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setText("Login Realizado com Sucesso!")
                msg.setWindowTitle("Login Realizado")
                msg.exec_()
                self.tela_apostar.setupUi(self)
            else:
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setText("Login e/ou Senha incorretos")
                msg.setInformativeText(self.trUtf8("Entenda melhor:"))
                msg.setWindowTitle("Erro no Login")
                msg.setDetailedText(
                    self.trUtf8("Esteja ciente de que os dados informados estão corretos e que já possui um cadastro."))
                msg.exec_()



    def sairLogin(self):
        self.tela_principal.setupUi(self)



    def apostar(self):
        campo1 = self.tela_apostar.lineEdit01.text()
        campo2 = self.tela_apostar.lineEdit02.text()
        campo3 = self.tela_apostar.lineEdit03.text()
        campo4 = self.tela_apostar.lineEdit04.text()
        campo5 = self.tela_apostar.lineEdit05.text()
        campo6 = self.tela_apostar.lineEdit06.text()

        if campo1 == '' or campo2 == '' or campo3 == '' or campo4 == '' or campo5 == '' or campo6 == '':
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Algum campo ficou em branco")
            msg.setInformativeText(self.trUtf8("Entenda melhor:"))
            msg.setWindowTitle("Campo em branco")
            msg.setDetailedText(self.trUtf8("Esteja ciente de que preencheu todos os campos de aposta."))
            msg.exec_()
            self.tela_apostar.setupUi(self)
        else:
            tcp = self.tcp

            aposta = Aposta(None, campo1, campo2, campo3, campo4, campo5, campo6, self.id_pessoaM, 'APOSTAR')
            resposta = self.conexao.serializarEnviarObjeto(tcp, aposta)

            if resposta.acao == 'APOSTADO':
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setText("Aposta Realizada com Sucesso!")
                msg.setWindowTitle("Aposta Realizada")
                msg.exec_()
                self.tela_principal.setupUi(self)
            else:
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setText("Algum erro ocorreu na aposta, Tente Novamente!")
                msg.setInformativeText(self.trUtf8("Entenda melhor:"))
                msg.setWindowTitle("Erro na aposta")
                msg.setDetailedText(self.trUtf8("Algum erro com a conexão pode ter ocorrido, para efetivar sua aposta tente novamente."))
                msg.exec_()
                self.tela_apostar.setupUi(self)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    f = classePrincipalCliente()
    f.show()

    sys.exit(app.exec_())