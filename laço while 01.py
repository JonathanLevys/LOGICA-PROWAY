# Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Dada a massa inicial, em gramas, fazer um programa em que calcule o tempo necessário
# para que essa massa se torne menor que 0,5 grama. O programa deve escrever a massa inicial,
# a massa final e o tempo calculado em segundos.


massa_inicial = float(input("Digite a massa inicial em gramas: "))


tempo = 0

while massa_inicial >= 0.5:
    massa_inicial /= 2
    tempo += 50


print('Massa inicial: ', massa_inicial, 'gramas')
print('Massa final: ', 0.5, 'gramas')
print('Tempo necessário: ', tempo//60, 'min: ', tempo%60, 'segundos')