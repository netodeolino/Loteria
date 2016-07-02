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
    def __init__(self, nome, idade, cpf, endereco, login, senha, acao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.login = login
        self.senha = senha
        self.acao = acao


class Aposta(object):
    def __init__(self, campo1, campo2, campo3, campo4, campo5, campo6, nome, cpf, endereco, acao):
        self.campo1 = campo1
        self.campo2 = campo2
        self.campo3 = campo3
        self.campo4 = campo4
        self.campo5 = campo5
        self.campo6 = campo6
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
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

        self.nomeM = None
        self.cpfM = None
        self.enderecoM = None

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

        pessoa = Person(nome, idade, cpf, endereco, login, senha, 'CADASTRAR')

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

        pessoa = Person(None, None, None, None, login, senha, 'LOGAR')
        resposta = self.conexao.serializarEnviarObjeto(tcp, pessoa)

        if resposta.nome != None:
            print 'CHEGOU UMA PESSOA AQUI'
            #print resposta.nome, resposta.cpf, resposta.endereco
            self.nomeM = resposta.nome
            self.cpfM = resposta.cpf
            self.enderecoM = resposta.endereco
            self.tela_apostar.setupUi(self)
        else:
            print 'NÃO CHEGOU NINGUÉM'
            print "NÃO LOGADO, DEPOIS CRIAR MENSAGEM PARA A TELA E NÃO PERMITIR IR PARA TELA DE APOSTAS"

        """
        if resposta == 'LOGADO':
            self.tela_apostar.setupUi(self)
        else:
            #self.tela_login.window()
            print "NÃO LOGADO, DEPOIS CRIAR MENSAGEM PARA A TELA E NÃO PERMITIR IR PARA TELA DE APOSTAS"
        """


    def sairLogin(self):
        self.tela_principal.setupUi(self)


    def comoJogar(self):
        pass


    def apostar(self):
        campo1 = self.tela_apostar.lineEdit01.text()
        campo2 = self.tela_apostar.lineEdit02.text()
        campo3 = self.tela_apostar.lineEdit03.text()
        campo4 = self.tela_apostar.lineEdit04.text()
        campo5 = self.tela_apostar.lineEdit05.text()
        campo6 = self.tela_apostar.lineEdit06.text()

        if campo1 == None or campo2 == None or campo3 == None or campo4 == None or campo5 == None or campo6 == None:
            #CRIAR MENSAGEM DE TELA, TIPO O JOPTIONPANE DO JAVA
            print 'NÃO PODE CONTER CAMPOS EM BRANCO'
        else:
            tcp = self.tcp
            aposta = Aposta(campo1, campo2, campo3, campo4, campo5, campo6, self.nomeM, self.cpfM, self.enderecoM, 'APOSTAR')
            resposta = self.conexao.serializarEnviarObjeto(tcp, aposta)

        if resposta == 'APOSTADO':
            print 'MENSAGEM TIPO JOPTIONPANE QUE DEU CERTO A APOSTA'
            self.tela_principal.setupUi(self)
        else:
            print 'NAO APOSTOU, OCORREU ERRO MENSAGEM'
            self.tela_apostar.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    f = classePrincipalCliente()
    f.show()

    sys.exit(app.exec_())