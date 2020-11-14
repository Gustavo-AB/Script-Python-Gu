
#num = int(input('Digite um valor: '))
#opcao = str(input('Deseja continuar [S/N]? ')).upper()
num = 0
opcao = 'Ss'
cont = 0
soma = 0
maior = 0
menor = 0
while opcao not in 'Nn':
    num = int(input('Digite um valor: '))
    opcao = str(input('Deseja continuar [S/N]? ')).upper()
    cont += 1
    soma += num
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A média entre os {} números é {}'.format(cont, media))
print('O maior número é o {} e o menor {}!'.format(maior, menor))
