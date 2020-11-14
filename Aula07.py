n = input('qual é o seu nome ? ')
print('Prazer em conhece-lo {:=^20} !'.format(n))
print('Agora {} digite um numero para fazer-mos operações matematicas !'.format(n))
n1 = int(input('Digite um numero > '))
n2 = int(input('Mais um '))
s = n1 + n2
mu = n1 * n2
d = n1 / n2
po = n1 ** n2
di = n1 // n2
re = n1 % n2
print('A soma é {}  o produto é {}'.format(s, mu),end = ' e tembém ')
print('a divisão é {} a potencia é {:.2f} a divisão inteira é {} e o resto {} !'.format(d, po, di, re))



