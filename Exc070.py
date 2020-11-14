mdm = mb = total = cont = 0
ndmb  = '' 
while True:
    print('-' * 30)
    nome = str(input('Nome do Produto: ')).strip().upper()
    preço = float(input('Preço do Produto R$: '))
    esco = ' '
    while esco not in 'SsNn':
        esco = str(input('Deseja Continuar [S/N]? ')).strip().upper()
    cont += 1
    total += preço

    if cont == 1:
        mb = preço
    else:
        if preço < mb:
            mb = preço
            ndmb = nome
    if esco == 'N':
        break

    if preço >= 1000:
        mdm += 1

print('-' * 30)
print(f'O total da compra é de R${total:.2f}!')
print(f'{mdm} Produtos Custam Mais de R$1000 Reais!')
print(f'O Produto Mais Barato é o {ndmb} Que Custa R${mb:.2f}')
    