import  os

host_ip = input("Digite o Ip ou Host que deseja consultar :")


os.system('ping -c 6 {}'.format(host_ip))