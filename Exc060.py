num = int(input('Digite um número: '))
cont = num
fac = 1
print('Calculando o fatorial de {}'.format(num))
while cont > 0:
    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else ' = ', end='')
    fac *= cont
    cont -= 1
print('{}'.format(fac), end='')
