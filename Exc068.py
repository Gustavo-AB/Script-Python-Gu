from random import randint
from time import sleep

vit = 0
print('=-' * 20)
print('{:=^40}'.format('PAR OU ÍMPAR!'))


while True:
    numpc = randint(0, 10)
    print('=-' * 20)
    num = int(input('Digite Um Valor: '))
    poui = str(input('Pra ou Impár [I/P]? ')).strip().upper()
    print('=-' * 20)

    if poui == 'P':
        result = num + numpc 
        print(f'Você Digitou o Número {num} e Escolheu PAR!')
        sleep(1)
        print(f'O Pc Escolheu o Número {numpc} e Escolheu IMPAR Totalizando {result}!')
        print('=-' * 20)

        if result %  2 == 0:
            sleep(1)
            print('Você Ganhou PARABÉNS!')
            vit += 1
        else:
            sleep(1)
            print('Que Pena Você PERDEU!')
            sleep(1)
            print(f'Você Teve um Total de {vit} Vitórias!')
            break

    if poui not in 'PpIi':
        print('Erro\nTente novamente')


    if poui == 'I':
        result = num + numpc
        print(f'Você Digitou o Número {num} e Escolheu IMPAR!')
        sleep(1)
        print(f'O Pc Escolheu o Número {numpc} e Escolheu PAR Totalizando {result}!')

        if result % 2 == 1:
            sleep(1)
            print('Você Ganhou PARABÉNS!')
            vit += 1
        else:
            print('Que Pena Você PERDEU!')
            sleep(1)
            print(f'Você Teve um Total de {vit} Vitórias!')
            break

print('=-' * 20)