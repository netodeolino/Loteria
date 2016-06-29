import socket
import pickle


class Conectar():
    #def __init__(self):


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
        return resposta


    def fecharConexao(self, tcp):
        tcp.close()


    def receberMensagem(self, tcp):
        rMessage = tcp.recv(1024)
        return rMessage

"""
def envia(tcp, serializado):
    while neto != None:
        tcp.send(serializado)
        # msg = raw_input()


def recebe(tcp):
    while True:
        rMessage = tcp.recv(1024)
        if not rMessage:
            print "Ending connection"
            break
        print rMessage
"""

#envia(tcp, serializado)

# VAMOS TENTAR DE OUTRA FORMA :) serializarEnviarObjeto(tcp, objeto)

#tcp.close()
