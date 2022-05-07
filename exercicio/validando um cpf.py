while True:

    #cpf = '35392282504'
    cpf = input('digite um cpf: ')
    novo = cpf [0:-2]                   #elimina os dois ultimos digitos
    reverso = 10                        #contador reverso
    total = 0
    # Loop do CPF
    for index in range(19):
        if index > 8:                       #primeiro indice vai de 0 a 9
            index -= 9                      #sao os 9 primeiros digitos do cpf


        total += int(novo[index]) * reverso    #valor total da mutiplicaçao


        reverso -= 1                    #decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo += str(d)
    print('--'*30)
    print(novo)
    print('--'*30)

    if cpf == novo:
        print('cpf valido')
    else:
        print('cpf invalido')