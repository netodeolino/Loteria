#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb


class Person(object):
    def __init__(self, nome, idade, cpf, endereco, login, senha, acao):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.login = login
        self.senha = senha
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
        #sql = """INSERT INTO venda (VENDA_ID, PEDIDO_ID, PRODUTO_ID) VALUES (2, 1, 1)"""
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
        #sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                if login == row[0] and senha == row[1]:
                    person = Person(row[2], None, row[3], row[4], row[0], row[1], None)
                    return person
            return None
                #print row
                #cpf = row[0]
                
                # Now print fetched result VENDA_ID, PEDIDO_ID, PRODUTO_ID
                #print "cpf=%s" % \
                      #(cpf)
        except:
            print "Error: unable to fecth data"
            return False

        # disconnect from server
        self.db.close()


    def lerSorteio(self, sql, campo1, campo2, campo3, campo4, campo5, campo6):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        #sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                if campo1 == row[0] and campo2 == row[1] and campo3 == row[2] and campo4 == row[3] and campo5 == row[4] and campo6 == row[5]:
                    person = Person(row[6], None, row[7], row[8], None, None, None)
                    return person
                else:
                    person = Person(None, None, None, None, None, None, None)
                    return person
            return None
                #print row
                #cpf = row[0]
                
                # Now print fetched result VENDA_ID, PEDIDO_ID, PRODUTO_ID
                #print "cpf=%s" % \
                      #(cpf)
        except:
            print "Error: unable to fecth data"
            return False

        # disconnect from server
        self.db.close()


    def atualizar(self, sql):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        # Prepare SQL query to UPDATE required records
        #sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

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
        #sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
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