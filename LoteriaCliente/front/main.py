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
    def __init__(self, nome, idade, cpf, endereco, login, senha):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.login = login
        self.senha = senha


class classePrincipalCliente(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.tela_principal = Ui_TelaPrincipal()
        self.tela_cadastro = Ui_TelaCadastro()
        self.tela_login = Ui_TelaLogin()
        self.tela_apostar = Ui_TelaApostar()

        self.conexao = Conectar()
        self.tcp = self.conexaoTCPCliente()

        self.tela_principal.setupUi(self)


    def conexaoTCPCliente(self):
        tcp = self.conexao.conectar()
        return tcp


    def logarFormulario(self):
        self.tela_login.setupUi(self)


    def cadastrarFormulario(self):
        self.tela_cadastro.setupUi(self)


    def cadastrar(self):
        # MANDAR PARA O SERVIDOR OS DADOS, CADASTRAR E RECEBER DE VOLTA O OK
        # INFORMAR AO USUÁRIO QUE O CADASTRO FOI REALIZADO COM SUCESSO E REDIRECIONAR PARA O LOGIN

        nome = self.tela_cadastro.lineEditNome.text()
        idade = self.tela_cadastro.lineEditIdade.text()
        cpf = self.tela_cadastro.lineEditCPF.text()
        endereco = self.tela_cadastro.lineEditEndereco.text()
        login = self.tela_cadastro.lineEditLogin.text()
        senha = self.tela_cadastro.lineEditSenha.text()

        #conectar = Conectar()
        tcp = self.tcp

        pessoa = Person(nome, idade, cpf, endereco, login, senha)

        resposta = self.conexao.serializarEnviarObjeto(tcp, pessoa)

        if resposta == 'CADASTRADO':
            self.tela_login.setupUi(self)
        else:
            self.tela_cadastro.setupUi(self)
            self.tela_cadastro.lineEditNome.setText('Informe os dados novamente')


    def sairCadastro(self):
        self.tela_principal.setupUi(self)


    def inicio(self):
        self.tela_principal.setupUi(self)


    def sair(self):
        self.close()


    def logar(self):

        #MANDAR OS DADOS PARA O SERVIDOR ANALISAR SE ESTÁ OK E RECEBER DE VOLTA A RESPOSTA PARA PROSSEGUIR
        #   COM O LOGIN OU NÃO
        senha = self.tela_login.lineEditSenha.text()
        login = self.tela_login.lineEditLogin.text()

        #conectar = Conectar()
        #tcp = conectar.conectar()

        tcp = self.tcp

        pessoa = Person(None, None, None, None, login, senha)
        resposta = self.conexao.serializarEnviarObjeto(tcp, pessoa)

        if resposta == 'LOGADO':
            self.tela_apostar.setupUi(self)
        else:
            #self.tela_login.window()
            print "NÃO LOGADO, DEPOIS CRIAR MENSAGEM PARA A TELA E NÃO PERMITIR IR PARA TELA DE APOSTAS"


    def sairLogin(self):
        self.tela_principal.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    f = classePrincipalCliente()
    f.show()

    sys.exit(app.exec_())