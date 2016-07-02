#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import thread
import pickle
import random

from Banco import *
from Email import *

HOST = ''              # Endereco IP do Servidor
PORT = 12345           # Porta que o Servidor esta


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


def conectado(con, cliente):
    print 'Conectado por', cliente

    while True:
        serializado = con.recv(1024)
        try:
            msg = pickle.loads(serializado)
        except EOFError:
            desconectar(con, cliente)
        #if not msg: break
        if msg.acao == 'CADASTRAR':
            nome1 = msg.nome
            idade1 = int(msg.idade)
            cpf1 = msg.cpf
            endereco1 = msg.endereco
            login1 = msg.login
            senha1 = msg.senha

            teste = DAO()
            args = (nome1, idade1, cpf1, endereco1, login1, senha1)
            bole = teste.inserir("INSERT INTO pessoa (nome, idade, cpf, endereco, login, senha) VALUES (%s, %s, %s, %s, %s, %s)", args)
            if bole == True:
                print ("CADASTRADO")
                enviar(con, cliente, "CADASTRADO")
            else:
                print ("NÃO CADASTRADO")
                enviar(con, cliente, "NÃO CADASTRADO")


        if msg.acao == 'LOGAR':
            teste = DAO()
            login1 = msg.login
            senha1 = msg.senha
            boli = teste.lerLogin("SELECT login, senha, nome, cpf, endereco FROM pessoa", login1, senha1)
            
            if boli.nome != None:
                print ("ENTROU LOGAR")
                serumano = Person(boli.nome, None, boli.cpf, boli.endereco, boli.login, boli.senha, None)
                serializadoResposta = pickle.dumps(serumano)
                enviar(con, cliente, serializadoResposta)
                #mandar = Email('netodeolino@outlook.com', 'teste no servidor', 'meu texto do servidor')
                #mandar.enviar()
            else:
                print ("NÃO ENTROU MAN, SENHA INCORRETA?!")
                enviar(con, cliente, "NÃO LOGADO")


        if msg.acao == 'APOSTAR':
            campo1 = msg.campo1
            campo2 = msg.campo2
            campo3 = msg.campo3
            campo4 = msg.campo4
            campo5 = msg.campo5
            campo6 = msg.campo6
            nome1 = msg.nome
            cpf1 = msg.cpf
            endereco1 = msg.endereco

            teste = DAO()
            args = (campo1, campo2, campo3, campo4, campo5, campo6, nome1, cpf1, endereco1)
            bole = teste.inserir("INSERT INTO aposta (campo1, campo2, campo3, campo4, campo5, campo6, nome, cpf, endereco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", args)
            if bole == True:
                print ("APOSTADO")
                enviar(con, cliente, "APOSTADO")
            else:
                print ("NÃO APOSTADO")
                enviar(con, cliente, "NÃO APOSTADO")

    #print 'Finalizando conexao do cliente', cliente
    #con.close()
    #thread.exit()


def enviar(con, cliente, sMessage):    
    #while True:
    #sMessage = raw_input(">>")
    #sMessage = "INSERIDO"
    #if not sMessage: break
    con.send(sMessage)

    #print 'Finalizando conexao do cliente', cliente
    #con.close()
    #thread.exit()

def desconectar(con, cliente):
    print 'Finalizando conexão do cliente', cliente
    con.close()
    thread.exit()

def realizarSorteio():
    #MÉTODO ENCONTRADO NA INTERNET QUE PODE ME AJUDAR NAS APOSTAS
    #
    lista = sorted(random.sample(range(1,99), 6))
    #print lista
    teste = DAO()
    campo1 = lista[0]
    campo2 = lista[1]
    campo3 = lista[2]
    campo4 = lista[3]
    campo5 = lista[4]
    campo6 = lista[5]
    ganhaste = teste.lerSorteio("SELECT campo1, campo2, campo3, campo4, campo5, campo6, nome, cpf, endereco FROM aposta", campo1, campo2, campo3, campo4, campo5, campo6)
    if ganhaste.nome != None:
        print 'HOUVE GANHADOR'
        #mandar email para vencedor (ADICIONAR INFORMAÇÕES DE EMAIL NA PESSOA E NA APOSTA)
    else:
        print 'NÃO HOUVE GANHADOR'
    

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

opc = raw_input('Digite 1 para iniciar o SERVIDOR ou 2 para realizar um SORTEIO: ')
if opc == '1':
    while True:
        con, cliente = tcp.accept()
        thread.start_new_thread(conectado, tuple([con, cliente]))
        #thread.start_new_thread(enviar, tuple([con, cliente]))
else:
    realizarSorteio()

tcp.close()
