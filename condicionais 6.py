#Criar um programa que solicita o sexo e a idade, e no final traz:
# Sexo: masculino - idade :31

sexo = input('Digite o sexo [M]ascilino ou [F]eminino')
idade = input('Digita a idade')

tipo_sexo = ''

if sexo.upper() == "M":
    tipo_sexo = 'Masculino'
elif sexo.upper() == "F":
    tipo_sexo = 'Feminino'

else:
    print('Não foi possível confirmar dados')

if int(idade) <18:
    faixa_etaria = 'Menor'
else:
    faixa_etaria = 'Maior'

print('Sexo:', tipo_sexo, '-idade:', idade, '- é de', faixa_etaria)
