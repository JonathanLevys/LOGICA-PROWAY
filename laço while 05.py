# Crie um programa que simule as operações básicas de um banco:
# Todas as opções devem funcionar. A conta só é acessada caso
# seja apresentada a senha correta.
# Inicialmente devem ser Solicitado informado nº da Conta e Senha;
# Caso a conta e senha estejam corretos, redireciona para o seguinte menu:
# a.  	Consultar saldo
# b.  	Pagar conta
# c.   	Depositar na conta
# d.  	Saque
# e.  	Sair
# 	O programa só deve se encerrar quando for selecionada  a opção SAIR.

conta = '123123'
senha = '123456'
conta_digitada = ''
senha_digitada = ''
saldo = 150.95
cheque_especial = 1000.00

# conferir login e senha
while True:
    conta_digitada = input('Conta: ')
    senha_digitada = input('Senha: ')
    if conta_digitada == conta and senha_digitada == senha:
        break

while True:
    print('Banco Central da Proway')
    print('[1] Consultar Saldo')
    print('[2] Pagar Conta')
    print('[3] Depósito em conta')
    print('[4] Saque')
    print('[5] Sair')
    opcao = input('Opção: ')

    if opcao == '1':
        print('Seu saldo Atual é de: R$ ', saldo)

    elif opcao == '2':
        valor = float(input('Qual o valor da fatura: '))
        if valor < 0:
            print('Não é possível valor negativo')
        elif valor < saldo + cheque_especial:
            saldo -= valor
        else:
            print('não há saldo disponível')
        print('Seu saldo Atual é de: R$ ', saldo)

    elif opcao == '3':
        valor = float(input('Qual o valor do depósito: '))
        if valor < 0:
            print('Não é possível valor negativo')
        else:
            saldo += valor
            print('Seu saldo Atual é de: R$ ', saldo)

    elif opcao == '4':
        valor = float(input('Qual o valor do saque: '))
        if valor < 0:
            print('Não é possível valor negativo')
        elif valor < saldo + cheque_especial:
            saldo -= valor
        else:
            print('não há saldo disponível')
        print('Seu saldo Atual é de: R$ ', saldo)

    elif opcao == '5':
        break
    else:
        print('Opção Inválida')

# adicionar as condições para:
# não permitir sacar além do limite (considerar 1.000,00 de cheque especial)
# não permitir lançamento de valores negativos
# após qualquer operação, mostrar o saldo atualizado

