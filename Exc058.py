from random import randint
from time import sleep
pc = randint(0, 10)
cont = 0
acertou = False
while not acertou:
    num = int(input('Em qual numero eu estou pensando entre 1 e 10? '))
    sleep(1)
    cont += 1
    if num == pc:
        acertou = True
    else:
        if num < pc:
            print('Mais...Tente novamente: ')
        elif num > pc:
            print('Menos...Tente novamente: ')
    sleep(1)
print('Parabéns você acertou!\nVocê precisou de {} tentativas!'.format(cont))