import hashlib

try:
    doc1 = input('Digite o Hash1 :')
    doc2 = input('Digite o Hash 2 :')


    doc1 = 'a.txt'
    doc2 = 'b.txt'

    print('Tipos De Criptografia = md5 , ripemd160')
    cripto = input('Digite o Tipo de Criptografia :').capitalize()



    hash1 = hashlib.new(cripto)

    hash1.update(open(doc1 ,'rb').read())

    hash2 = hashlib.new('sha256')

    hash2.update(open(doc2 ,'rb').read())


    if hash1.digest() != hash2.digest():
        print(f'O Hash1 {doc1} é diferente ao Hash2{doc2}')
        print(f'o Hash do arquivo a.txt é  = {hash1.hexdigest()}')
        print(f'o Hash do arquivo b.txt é  = {hash2.hexdigest()}')
    else:
        print(f'O Hash1 {doc1} é igual ao Hash2{doc2}')
        print(f'o Hash do arquivo a.txt é  = {hash1.hexdigest()}')
        print(f'o Hash do arquivo b.txt é  = {hash2.hexdigest()}')
except:
    print('Houve  erro na digitação tente de novo  ')


