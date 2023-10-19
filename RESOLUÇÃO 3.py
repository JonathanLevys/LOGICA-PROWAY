# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#  para homens: (50 * altura)         1,85 * 50 =
# para mulheres: (40 * altura)       1,60 * 40 =

altura = float(input('Digite a sua altura(m)'))
sexo = input('sexo: [M]asculino ou [F]eminino'). upper()

if sexo == "M":
    print('Peso ideal:', altura*50)
elif sexo == "F":
    print('Peso ideal:', altura*40)
else:
    print('Sexo não disponivel na lista')

