#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb


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


class DAO(object):
    def __init__(self):
        """
        Inits MySQL connection
        """
        self.conecao()
        return

    def conecao(self):
        """
        Creates connection
        """
        self.db = mdb.connect(host="localhost", \
                                          user="root", \
                                          passwd="mysql", \
                                          db="loteria")
        return


    def inserir(self, sql, args):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        try:
            # Execute the SQL command
            cursor.execute(sql, args)
            # Commit your changes in the database
            self.db.commit()
            return True
        except:
            # Rollback in case there is any error
            self.db.rollback()
            return False

        # disconnect from server
        self.db.close()


    def inserirAposta(self, sql, args):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        try:
            # Execute the SQL command
            cursor.execute(sql, args)
            # Commit your changes in the database
            self.db.commit()
            return True
        except:
            # Rollback in case there is any error
            self.db.rollback()
            return False

        # disconnect from server
        self.db.close()


    def lerLogin(self, sql, login, senha):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                if login == row[1] and senha == row[2]:
                    person = Person(row[0], row[3], None, row[4], row[5], row[1], row[2], row[6], row[7], row[8], None)
                    return person
            person = Person(None, None, None, None, None, None, None, None, None, None, None)
            return person
        except:
            # Error in the SQL command
            print "Error: unable to fecth data"
            person = Person(None, None, None, None, None, None, None, None, None, None, None)
            return person

        # disconnect from server
        self.db.close()


    def lerSorteio(self, sql, campo1, campo2, campo3, campo4, campo5, campo6):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            lista = [] #GAMBIAARRA DE MAIS DE UM GANHADOR
            for row in results:
                if campo1 == row[1] and campo2 == row[2] and campo3 == row[3] and campo4 == row[4] and campo5 == row[5] and campo6 == row[6]:
                    person = Person(row[7], None, None, None, None, None, None, None, None, None, 'GANHOU')
                    lista.append(person)
                    #return person
            return lista
        except:
            # Error in the SQL command
            print "Error: unable to fecth data"
            return None

        # disconnect from server
        self.db.close()


    def atualizar(self, sql):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to UPDATE required records
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()

        # disconnect from server
        self.db.close()


    def apagar(self, sql):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to DELETE required records
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()

        # disconnect from server
        self.db.close()


    def buscarPessoa(self, id):
        resposta = ("SELECT id_pessoa, nome, idade, cpf, endereco, login, senha, email, cartao, conta FROM pessoa")
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        try:
            # Execute the SQL command
            cursor.execute(resposta)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                if id == row[0]:
                    person = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], None)
                    return person
            person = Person(None, None, None, None, None, None, None, 'padrao@email.com', None, None, None)
            return person
        except:
            # Error in the SQL command
            print "Error: unable to fecth data"
            return None

        # disconnect from server
        self.db.close()
