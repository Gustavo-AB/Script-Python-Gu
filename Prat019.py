print('=-=' *13)
print('{:=^39}'.format('LOJA ONLINE'))
print('=-=' * 13)
cel = 1200
tv = 2000
som = 1500
print('[1]-Celular R$ 1200\n[2]-Televisão R$ 2000\n[3]-Aparelho de Som R$ 1500')
continuar = 'Ss'
soma = 0
while continuar not in 'Nn':
    print('-' * 40)
    escolha = int(input('O que deseja comprar? '))
    if escolha == 1:
        print('Celular R$ 1200')
        escolha = cel
    if escolha == 2:
        print('Televisão R$ 2000')
        escolha = tv
    if escolha == 3:
        print('Aparelho de som R$ 1500')
        escolha = som
    soma += escolha 
    continuar = str(input('Deseja continuar comprando? [S/N] ')).upper().strip()
print('-' * 40)
print('Formas de Pagamento:\n[1]-A vista com 10% de desconto\n[2]-Parcelado com 5% de juros')
print('-' * 40)
pag = int(input('Qual a forma de pagamento? '))
if pag == 1:
    desc = soma - (soma * 10) / 100 
    print('-' * 40)
    print('O total de suas compras é de R${:.2f}\nCom 10% de desconto no total R${:.2f}'.format(soma, desc))
else:
    vez = int(input('Em quantas vezes? '))
    juros = (soma * 5) / 100
    parc = soma / vez 
    print('O total de suas compras é de R${:.2f} parcelado em {}x de R${:.2f} com 5% de juros!'.format(soma, vez, parc+juros))
print('=-=' * 13)
print('{:=^39}'.format('OBRIGADO E VOLTE SEMPRE!'))
print('=-=' * 13)
