# https://drive.google.com/drive/folders/1hVRupnZyLS3J3dAwc7_2QmpEq0vb7C-P?usp=sharing

from time import sleep

texto = r"""
 _____ ____________   _   _  ___   _     ___________  ___ _____ ___________   _____  _____ 
/  __ \| ___ \  ___| | | | |/ _ \ | |   |_   _|  _  \/ _ \_   _|  _  | ___ \ / __  \|  _  |
| /  \/| |_/ / |_    | | | / /_\ \| |     | | | | | / /_\ \| | | | | | |_/ / `' / /'| |/' |
| |    |  __/|  _|   | | | |  _  || |     | | | | | |  _  || | | | | |    /    / /  |  /| |
| \__/\| |   | |     \ \_/ / | | || |_____| |_| |/ /| | | || | \ \_/ / |\ \  ./ /___\ |_/ /
 \____/\_|   \_|      \___/\_| |_/\_____/\___/|___/ \_| |_/\_/  \___/\_| \_| \_____(_)___/                                                                              
"""
valido = """

██    ██  █████  ██      ██ ██████   ██████  
██    ██ ██   ██ ██      ██ ██   ██ ██    ██ 
██    ██ ███████ ██      ██ ██   ██ ██    ██ 
 ██  ██  ██   ██ ██      ██ ██   ██ ██    ██ 
  ████   ██   ██ ███████ ██ ██████   ██████  


"""
print(texto)
cpf = input('Digite seu CPF:')
cpf_sem_verificador = cpf[:-2]
tamanho = len(cpf_sem_verificador)
contador = 0
multiplicador = 10
total = 0

# 1º Verificador
while contador < tamanho:
    total += multiplicador * int(cpf_sem_verificador[contador])
    multiplicador -= 1
    contador += 1

primeiro_verificador = 11 - total % 11

if primeiro_verificador > 9:
    primeiro_verificador = 0

# 2º Verificador
cpf_sem_verificador = cpf[:-1]
tamanho = len(cpf_sem_verificador)
contador = 0
multiplicador = 11
total = 0

# 1º Verificador
while contador < tamanho:
    total += multiplicador * int(cpf_sem_verificador[contador])
    multiplicador -= 1
    contador += 1

segundo_verificador = 11 - total % 11

if segundo_verificador > 9:
    segundo_verificador = 0

for i in range(50):
    print('||', end='')
    sleep(0.1)

if primeiro_verificador == int(cpf[-2]) and segundo_verificador == int(cpf[-1]):
    print(valido)
else:
    print('CPF Inválido')

input()
