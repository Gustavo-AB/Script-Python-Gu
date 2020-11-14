#criando uma tupla. É possivel criar uma tupla sem os parentese tambem
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche)
for c in lanche:
    print(f'Vou Comer {c}!')
print('Ah Comi BAstante')
for cont in range(0, len(lanche)):
    print(f'Vou Comer {lanche[cont]}!')

for pos, conta in enumerate(lanche):
    print(f'Vou comer {conta} na posição {pos}')

print(sorted(lanche))
#esse comando apaga a tupla
del(lanche)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b+a
print(c)
print(c.count(5))
print(c.index(8))
print(c.index(2, 4))