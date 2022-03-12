import  re
import json
from urllib.request import urlopen


url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados =json.load(resposta)

ip = dados['ip']
host = dados['hostname']
cid = dados['city']
rg = dados['region']
pais = dados['country']

print(f'O IP :{ip} \n O Hostname :{host}\n a Cidade : {cid}\n A Região : {rg}\n O Pais : {pais}')