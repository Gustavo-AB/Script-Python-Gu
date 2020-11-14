n = int(input('Digite um numero dentro de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n //1000 % 10
print('O numero {} tem:'.format(n))
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))