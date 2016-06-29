#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import thread
import pickle

from Banco import *
from Email import *

HOST = ''              # Endereco IP do Servidor
PORT = 12345           # Porta que o Servidor esta


class Person(object):
    def __init__(self, nome, idade, cpf, endereco, login, senha):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.login = login
        self.senha = senha


def conectado(con, cliente):
    print 'Conectado por', cliente

    while True:
        serializado = con.recv(1024)
        try:
            msg = pickle.loads(serializado)
        except EOFError:
            desconectar(con, cliente)
        #if not msg: break
        if msg.nome != None:
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
           

        if msg.nome == None:
            teste = DAO()
            login1 = msg.login
            senha1 = msg.senha
            boli = teste.ler("SELECT login, senha FROM pessoa", login1, senha1)
            if boli == True:
                print ("ENTROU")
                enviar(con, cliente, "LOGADO")
                #mandar = Email('netodeolino@outlook.com', 'teste no servidor', 'meu texto do servidor')
                #mandar.enviar()
            else:
                print ("NÃO ENTROU MAN, SENHA INCORRETA?!")
                enviar(con, cliente, "NÃO LOGADO")

    #print 'Finalizando conexao do cliente', cliente
    #con.close()
    #thread.exit()
    #import random
    #sorted(random.sample(range(1,50), 6))
    #[2, 9, 20, 30, 33, 46]


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

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))
    #thread.start_new_thread(enviar, tuple([con, cliente]))

tcp.close()
