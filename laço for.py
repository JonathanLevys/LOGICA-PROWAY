 # Criar um laço de repetição que vai de 0 ate n.

# n = int(input('Digite um numero: '))
#
# for numero in range(n):
#      print(n)

max = 0
for i in range(5):
    numero = int(input('Digite um número: '))
    if i == 0:
        max = numero

    if numero > max:
        max = numero
print('Maior: ', max)