print('=' * 20, 'Testador de Calculo', '=' * 20)
print('-' * 60)
print('vamos utilizar apenas 2 valores!')
print('-' * 60)



print('-' * 60)
while True:
    val1 = float(input('Digite o Primeiro valor: '))
    val2 = float(input('Digite o Segundo valor: '))
    print('-' * 60)

    print('Escolha uma das Operações abaixo:')
    print('Adição=[A]\nSubtração=[S]\nMultiplicação=[M]\nDivisão=[D]')

    escolha = str(input('--> ')).strip().upper()

    if escolha == 'A':
        print(f'Agora digite o resultado da Soma entre {val1} e {val2} ')
        resultado = float(input('-->'))
        if resultado == val1 + val2:
            print('Parabéns Você Acertou!')
        else:
            while True:
                print('Você Errou! Tente Novamente')
                resultado = float(input('-->'))
                if resultado == val1 + val2:
                    print('Parabéns Você Acertou!')
                    break
    
    

    if escolha == 'S':
        resultado = float(input(f'Agora digite o resultado da Subtração entre {val1} e {val2}\n-->'))
        if resultado == val1 - val2:
            print('Parabéns Você Acertou!')
        else:
            while True:
                print('Você Errou! Tente Novamente')
                resultado = float(input('-->'))
                if resultado == val1 - val2:
                    print('Parabéns Você Acertou!')
                    break

    

    if escolha == 'M':
        resultado = float(input(f'Agora digite o resultado da Multiplicação entre {val1} e {val2}\n-->'))
        if resultado == val1 * val2:
            print('Parabéns Você Acertou!')
        else:
            while True:
                print('Você Errou! Tente Novamente')
                resultado = float(input('-->'))
                if resultado == val1 * val2:
                    print('Parabéns Você Acertou!')
                    break 

    if escolha == 'D':
        resultado = float(input(f'Agora digite o resultado da Divisão entre {val1} e {val2}\n-->'))
        if resultado == val1 / val2:
            print('Parabéns Você Acertou!')
        else:
            while True:
                print('Você Errou! Tente Novamente ')
                resultado = float(input('-->'))
                if resultado == val1 / val2:
                    print('Parabéns Você Acertou!')
                    break

    continuar = str(input('Deseja Continuar [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
    
print('=' * 45)
print('=' * 20, 'FIM', '=' * 20)
print('=' * 45)
#00FF00