from random import randint

valor = (randint(0,10), randint(0,10), randint(0,10), 
randint(0,10), randint(0,10))

print('Os valores sorteados foram: ', end='')
for n in valor:
    print(f'{n} ', end='')


print(f'\nO MAIOR número é o {max(valor)}')
print(f'O MENOR número é o {min(valor)}')