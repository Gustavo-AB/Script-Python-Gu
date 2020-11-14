valor = int(input('Digite um valor: '))
razao = int(input('Qual a razão? '))
cont = 1
termo = valor
while cont <= 10:
    print('{}-'.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
