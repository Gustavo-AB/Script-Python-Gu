soma = 0
cont = 0
for con in range(1, 501, 2):
    if con % 3 == 0:
        soma += con
        cont += 1
print('A soma é {}!\nE esse {} é o número total de valores impares multiplos de 3!'.format(soma, cont))