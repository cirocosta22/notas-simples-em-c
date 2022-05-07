secret = 'framework'
digitadas = []
chances = 4

while True:
     if chances <= 0:
        print('voce perdeu!!!')
        break

     letra = input('digite uma letra: ')

     if len(letra) > 1:
          print('error , tente novamente , digite apenas uma letra')
          continue

     digitadas.append(letra)

     if letra in secret:
         print(f'muito bem , a letra "{letra}"  digitada existe na palavra secreta ')

     else:
        print(f'a letra" {letra}"nao existe na palavra secreta')
        digitadas.pop()

     secret_temp = ''
     for letra_secreta in secret:
        if letra_secreta in digitadas:
            secret_temp += letra_secreta
        else:
             secret_temp += '*'

        if secret_temp == secret:
            print(f'GENIAL, VOCE GANHOU, a palavra era{secret_temp}')
            break
        else:
            print(f'a palavra secreta esta assim {secret_temp}')

        if letra not in secret:
            chances -= 1

        print(f'voce ainda tem {chances}chances')
        print()






