nome = 'Jonathan'
num_caract = len(nome)

tamanho pequeno até 5 caracteres
tamanho médio até 7 caracteres
tamanho grande até 10 caracteres
tamanho gigante acima 10 caracteres


if num_caract < 6:
    print('pequeno')
elif num_caract < 8:
    print('medio')
elif num_caract < 11:
    print('grande')
else:
    print('gigante')