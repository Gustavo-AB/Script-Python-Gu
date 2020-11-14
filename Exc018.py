import math
ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O SENO de {:.2f} vale {:.2f}\nO COSSENO vale {:.2f}\nE a TANGENTE {:.2f}'.format(ang, seno, coss, tan))
