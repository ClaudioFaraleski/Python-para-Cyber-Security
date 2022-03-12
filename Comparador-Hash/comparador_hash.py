import hashlib


doc1 = 'a.txt'
doc2 = 'b.txt'



hash1 = hashlib.new('ripemd160')

hash1.update(open(doc1 ,'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(doc2 ,'rb').read())


if hash1.digest() != hash2.digest():
        print(f'O Hash1 {doc1} é diferente ao Hash2{doc2}')
        print(f'o Hash do arquivo a.txt é  = {hash1.hexdigest()}')
        print(f'o Hash do arquivo b.txt é  = {hash2.hexdigest()}')
else:
        print(f'O Hash1 {doc1} é igual ao Hash2{doc2}')
        print(f'o Hash do arquivo a.txt é  = {hash1.hexdigest()}')
        print(f'o Hash do arquivo b.txt é  = {hash2.hexdigest()}')



