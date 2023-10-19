# minimo = 10
# maximo = 20
# valor = 15
#
#
#
# if minimo <= valor <= maximo:
#     print('está entre')
# else:
#     print('não está')
#
# if valor >= minimo and valor <= maximo:
#     print('está entre')
# else:
#     print('não está')
#
# #  abaixo do minimo, no intervalo, acima do maximo
#
# if valor < 11:
#     print('minimo')
# elif valor > 19:
#     print('maximo')
# else:
#     print('intervalo')


# descobrir se o nunero é par ou impar
#
# numero = 10
# if numero % 2 ==0:
#     print('Par')
# else:
#     print('Impar')

media = 7.5
frequencia = 0.6

if media >= 7 and frequencia >= 0.75:
    print('aprovado')
else:
    print('Reprovado')
"""
#  Tabela verdade
# AND - V = Verdadeiro
      - F = Falso
      
      V + V = V
      F + F = V
      V + F = F
      F + V = F
      
# OR
    V + V = V
    V + F = V
"""

media = 7.5
frequencia = 0.6

if media >= 7 or frequencia >= 0.75:
    print('aprovado')
else:
    print('Reprovado')

