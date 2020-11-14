#pont = '.' * 30
#produtos = (f'Televisão{pont}R$ 2000.00', f'Rádio{pont}R$ 899.00', f'Celular{pont}R$ 789.00',)
#for p in produtos:
 #   print(f'{p}')




listagem = ('Lápis', 1.75,
'Borracha', 2.00,
'Caderno', 15.90,
'Estojo', 25.00,
'Transferidor', 4.20,
'Compasso', 9.99,
'Mochila', 120.32,
'Canetas', 22.30,
'Livros', 34.90)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<60}', end='')
    elif pos % 2 == 1:
        print(f'R$ {listagem[pos]:>6.2f}')