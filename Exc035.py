print('-=' * 20)
print('{:=^40}'.format('ANALISADOR DE TRIANGULOS'))
print('-=' * 20)
seg1 = float(input('Qual o primeiro segmento: '))
print('-' * 40)
seg2 = float(input('Qual o segundo segmento: '))
print('-' * 40)
seg3 = float(input('Qual o terceiro segmento: '))
print('-=' * 20)
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('SIM é possivel formar um triangulo!!')
else:
    print('NÃO é possivel formar um triangulo!!')
print('-=' * 20)
