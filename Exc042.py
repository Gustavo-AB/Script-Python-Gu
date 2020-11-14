seg1 = float(input('Qual o primeiro valor? '))
seg2 = float(input('Qual o segundo valor? '))
seg3 = float(input('Qual o terceiro valor? '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('É possivel formar um triangulo ', end='')
    if seg1 == seg2 == seg3:
        print('EQUILATERO!!')
    if seg1 != seg2 != seg3 != seg1:
        print('ESCALENO!!')
    else:
        print('ISÓCELES!!')
else:
    print('NÃO é POSSIVEL formar um triangulo!!')

