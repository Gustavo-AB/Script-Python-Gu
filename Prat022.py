total = mdcem = cont = maisbara = msmvl = 0
baraton = ''

while True:
    nome = str(input('Nome do Produto: ')).strip().upper()
    valor = float(input('Valor do Produto R$: '))
    escolha = ' '
    total += valor
    cont += 1
    
    while escolha not in 'NnSs':
        escolha = str(input('Deseja Continuar [S/N]? ')).strip().upper()
    if valor > 100:
        mdcem += 1

    if cont == 1:
        maisbar = valor
        baraton = nome
    else:

        if valor < maisbar:
            maisbar = valor
            baraton = nome

    #if valor == valor:
        msmvl += 1

    if escolha == 'N':
        break


print(f'O Total da Compra é de R${total:.2f}!')
print(f'{mdcem} Produtos Custam Mais de R$100! ')
print(f'O Produto Mais Barato é o {baraton} que Custa R${maisbar:.2f}')
#print(f'{msmvl} Produtos Tem o Mesmo Valor ')