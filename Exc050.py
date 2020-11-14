soma = 0
cont = 0
for p in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(p)))
    soma += num
    cont += 1
if num % 2 == 0:
    print('Você informaou {} números pares!\nA soma dos números pares é {}!'.format(cont, soma))