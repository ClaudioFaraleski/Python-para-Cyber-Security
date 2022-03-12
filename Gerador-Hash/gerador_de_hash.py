import hashlib

string = input("Digite o texto : ")



menu = int(input(''' ### Digite a Opção Desejada ####

                     1) MD5
                     2) SHA1
                     3) SHA256
                     4) SHA512
                     Entre com a Opção :    '''))

if menu == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print(f'Texto convertido para MD5 :', resultado.hexdigest())
elif menu == 2 :
        resultado = hashlib.sha1(string.encode('utf-8'))
        print(f'Texto convertido para SHA1 :', resultado.hexdigest())
elif menu == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        print(f'Texto convertido para SHA256 :', resultado.hexdigest())
elif menu == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print(f'Texto convertido para MD5 :', resultado.hexdigest())
else:
        print("Opção Invalida .Precisa digitar uma Opção Valida")