from time import sleep
print('-=' * 20)
print('{:=^40}'.format('LOJA ONLINE'))
print('-=' * 20)
um = 800
dois = 2700
esc = int(input('[1]-Celular:R$800\n[2]-Televisão:R$2700\nQual item deseja comprar? '))
print('...')
sleep(1)
print('Escolha a forma de pagamento:\n[1]-Parcelado em 5 vezes!\n[2]-A vista com 10% de desconto!')
pag = int(input('Qual a forma de pagamento? '))
print('...')
sleep(1)
if esc == 1:
    print('Celular de R${:.2f}! '.format(um), end='')
    if pag == 1:
        parc = um / 5
        print('Parcelado em 5 vzes de R${}!!\nTotal:5v R${:.2f}'.format(parc, parc))
    if pag == 2:
        desco = um - (um * 10 / 100)
        print('A vista com 10% de desconto!!\nTotal: R${:.2f}'.format(desco))
if esc == 2:
    print('Televisão de R${:.2f}! '.format(dois), end='')
    if pag == 1:
        parc = dois / 5
        print('Pacelado em 5 vezes de R${:.2f}\nTotal:5x R${:.2f}'.format(parc, parc))
    if pag == 2:
        desco = dois - (dois * 10 / 100)
        print('A vista com 10% de desconto!!\nTotal: R${:.2f}'.format(desco))
print('Confirmando compra...')
sleep(1)
print('COMPRA FINALIZADA')
sleep(1)
print('-=' * 20)
print('{:=^40}'.format('OBRIGADO PELA PREFERÊNCIA. VOLTE SEMPRE!'))
print('-=' * 20)