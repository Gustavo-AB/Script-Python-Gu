print('{:=^40}'.format('VAMOS PINTAR A PAREDE'))
print('Lembrando que cada litro de tinta pinta uma area de dois metros quadrados !')
largura = int(input('Qual a largura da parede ? '))
altura = int(input('Qual a altura ? '))
area = largura * altura
tinta = area / 2
print('A sua parede tem {} metros quadrados, e você precisa de {} litros de tintas !'.format(area, tinta))
