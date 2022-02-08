import socket


conexao = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso !!!")

host = 'localhost'
porta = 5433
mensagem = 'Hello Server !!'

try:

    print("cliente : " + mensagem)
    conexao.sendto(mensagem.encode() , (host , 5432))
    dados,servidor = conexao.recvmsg(4096)
    dados = dados.decode()

    print("Cliente : " + dados)

finally:
    print("Cliente : fechando a conexão")

    conexao.close()