num = 200
div = num - (num * 13 / 100)
vezes = int(input('Em quantas vezes deseja parcelar? '))
parcela = div / vezes
print('O total ficou:R${}. Dividido em {} vezes de R${:.2f} !!'.format(div, vezes, parcela))
