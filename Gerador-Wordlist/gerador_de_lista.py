import itertools

tamanho = input("Digite a Palavra  :")
resultado = itertools.permutations(tamanho , len(tamanho))


for i in resultado:

    print(''.join(i))