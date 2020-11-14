print('-=' * 20)
print('{:=^40}'.format('COMPRAS ONLINE'))
print('-=' * 20)
cel = 2000
tv = 2300
print('(1)-Celular R$2000\n(2)-Televisão R$2300')
print('-=' * 20)
esc = int(input('Olá, o que deseja comprar? Digite um dos numeros acima: '))
if esc == 2:
    print('A TELEVISÃO custa R${}'.format(tv))
if esc == 1:
    print('O CELULAR custa R${}'.format(cel))
print('-=' * 20)
print('Aceitamos pagamentos:\n(3)-A vista (com 10% de desconto)\n(4)-Parcelado em 5 vezes sem juros')
pag = int(input('Digite um dos numeros acima para informar a forma de pagamento:'))
#Pag a vista
if pag == 3 and esc == 1:
    mult = cel * 10 / 100
    npag = cel - mult
    print('O preço final agora é R${:.2f}!'.format(npag))
if pag == 3 and esc == 2:
    mult = tv * 10 / 100
    npag = tv - mult
    print('O preço final agora é R${:.2f}'.format(npag))
#pag parcelado
if pag == 4 and esc == 1:
    npag = cel / 5
    print('O celular ficou em 5 parcelas de R${}!!'.format(npag))
if pag == 4 and esc == 2:
    npag = tv / 5
    print('A televisão ficou parcelada em 5 vezes de R${}'.format(npag))

