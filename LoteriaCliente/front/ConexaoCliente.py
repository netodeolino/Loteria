import socket
import pickle

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


class Conectar():

    def conectar(self):
        HOST = '127.0.0.1'  # Endereco IP do Servidor
        PORT = 12345  # Porta que o Servidor esta
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (HOST, PORT)
        tcp.connect(dest)
        return tcp


    def serializarEnviarObjeto(self, tcp, objeto):
        serializado = pickle.dumps(objeto)
        #while objeto != None:
        tcp.send(serializado)

        resposta = self.receberMensagem(tcp)

        respostaFinal = pickle.loads(resposta)
        return respostaFinal


    def fecharConexao(self, tcp):
        tcp.close()


    def receberMensagem(self, tcp):
        rMessage = tcp.recv(1024)
        return rMessage
