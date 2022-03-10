import random
import string

tamanho = int(input("Digite o Tamanho da senha a ser Gerada :"))

char = string.ascii_letters + string.digits + '!@#$%*()_+*-/:><;ç'

rnd = random.SystemRandom()

print(''.join(rnd.choice(char) for i in range(tamanho)))