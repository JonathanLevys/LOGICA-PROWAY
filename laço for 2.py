# Crie um programa que lista os numeros de 1 a 100
# para os numeros divisiveis por 3, escreva fizz
# para os numeros divisiveis por 5, escreva Buzz
# para os numeros divisiveis por 5 e3, escreva FizzBuzz
# Ex: 1, 2, fizz, 4, buzz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz, 16, 17, fizz

for numero in range(1, 100):

    if numero % 5 == 0 and numero % 3 == 0:
        print('FizzBuzz', end=' ')
    elif numero % 3 == 0:
        print('Fizz', end=' ')
    elif numero % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(numero, end=' ')

