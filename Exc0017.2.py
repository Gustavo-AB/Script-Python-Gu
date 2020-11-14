from math import hypot 
print('{:=^60}'.format('CALCULO DA HIPOTENUSA'))
co = float(input('Digite quanto vale o cateto oposto: '))
ca = float(input('Digite quanto vale o cateto adjacente: '))
print('A hipotenusa vale {:.2f}'.format(hypot(co, ca)))
