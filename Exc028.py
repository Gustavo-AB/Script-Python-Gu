from random import randint
from time import sleep
print('-=' * 20)
print('{:=^40}'.format('ADIVINHANDO O NÚMERO'))
print('-=' * 20)
print('Olá, eu sou o PC, e seja BEM-VINDO ao Adivinhando o Numero.')
print('Neste joguinho, eu vou pensar em um numero inteiro, de 0 a 5.')
print('E a sua missão, é tentar adivinhar qual numero eu pensei.')
ns = randint(0, 5)
num = int(input('Acabei de pensar em um numero, qual você acha que é? '))
print('PROCESSANDO...')
sleep(2)
print('-=' * 20)
if num == ns:
    print('Uau, PARABÉNS você conseguiu vencer.\nVocê GANHOU!!')
else:
    print('HAHA eu pensei no numero {} e não no {}\nVocê PERDEU!!'.format(ns, num))
print('-=' * 20)


