while True:
    numb = float(input('Digite um valor: '))
    numb2 = float(input('Digite outro valor: '))

    print('Escolha um número:')
    print(' 1) Soma \n 2) Subtração \n 3) Multiplicação \n 4) Divisão')
    print(' 5) Potência \n 6) Divisão Inteira \n 7) Resto da Divisão')

    print(f'===================')

    opcao = int(input('Digite um número: '))

    print(f'===================')

    if opcao == 1:
        print(f'O resultado deu: {numb + numb2}')
    elif opcao == 2:
        print(f'O resultado deu: {numb - numb2}')
    elif opcao == 3:
        print(f'O resultado deu: {numb * numb2}')
    elif opcao == 4:
        print(f'O resultado deu: {numb / numb2}')
    elif opcao == 5:
        print(f'O resultado deu: {numb ** numb2}')
    elif opcao == 6:
        print(f'O resultado deu: {numb // numb2}')
    elif opcao == 7:
        print(f'O resultado deu: {numb % numb2}')
    else:
        print('O número digitado está fora dos limites.')
        print(f'===================')
    
    print('Deseja realizar outro cálculo? Digite 1 para Sim e 2 para Não.')
    
    repetir = int(input(''))

    if repetir != 1:
        print('Encerrando...')
        break
    else:
        print('Reiniciando o código...')