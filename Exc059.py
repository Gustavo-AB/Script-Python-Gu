from time import sleep
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))
soma = num1 + num2
multi = num1 * num2
opcao = 0
while opcao != 5:
    print('=-=' * 10)
    print('Você deseja:')
    print('[1]-Somar\n[2]-Multiplicar\n[3]-Maior\n[4]-Novos números\n[5]-Sair do programa')
    opcao = int(input('O que deseja fazer? '))
    print('...')
    sleep(1)
    if opcao == 1:
        print('{} somado com {} é igual a {}!'.format(num1, num2, soma))
        print('...')
        sleep(1)
    elif opcao == 2:
        print('{} multiplicado com {} é igual a {}!'.format(num1, num2, multi))
        print('...')
        sleep(1)
    elif opcao == 3:
        if num1 > num2:
            print('O numero {} é o MAIOR!'.format(num1))
            print('...')
            sleep(1)
        else:
            print('O número {} é o MAIOR!'.format(num2))
            print('...')
            sleep(1)
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        soma = num1 + num2
        multi = num1 * num2
        print('...')
        sleep(1)
    elif opcao > 5 or opcao < 1:
        print('Opção inválida tente novamente!')
        sleep(1)
print('=-=' * 10)
print('SAINDO DO PROGRAMA...')
sleep(2)
print('=-=' * 10)
print('PROGRAMA FINALIZADO!\nVOLTE SEMPRE!')
print('=-=' * 10)