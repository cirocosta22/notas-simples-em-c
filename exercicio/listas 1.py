
secreto= 'framework'
digitadas = []
chances = 4


while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('error, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'muito bem, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'error: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secret_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secret_temp += letra_secreta
        else:
            secret_temp += '*'

    if secret_temp == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secret_temp}.')
        break
    else:
        print(f'A palavra secreta está assim: {secret_temp}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
