import socket
import sys


def main():
    try:
        conexao = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as erro:
        print("A conexão falhou !!!")
        print("Erro :{}".format(erro))
        sys.exit()

    print("Conexão criada com seucesso")

    try:
        HostAlvo = input("Digite o IP ou Host a ser conectado :")
        PortaAlvo = input("Digite a Porta a ser conectado:")


        conexao.connect((HostAlvo , int(PortaAlvo)))
        print(f'Cliente TCP conectado com sucesso  no host {HostAlvo} e na porta{PortaAlvo} ')
        conexao.shutdown(2)

    except socket.error as erro:
        print("Falha na conexão ")
        print("Erro : {}".format(erro))
        sys.exit()



