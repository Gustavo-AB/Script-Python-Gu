valor = int(input('Digite um valor: '))
razao = int(input('Qual a razão? '))
cont = 1
termo = valor
total = 0
ntermo = 10
while ntermo != 0:
    total = total + ntermo
    while cont <= total:
        print('{}-'.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    ntermo = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termo mostrados'.format(total))



