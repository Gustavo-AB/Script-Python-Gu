from math import trunc
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
qdc = co**2 + ca**2
hip = qdc**(1/2)
print('A soma dos quadrados dos catetos vale {} entao a hipotenusa vale {}.'.format(qdc, int(hip)))
