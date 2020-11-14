#Listas parte 1
valores = [0, 2, 5, 4, 3]
print(sorted(valores))
valores.append(1)
valores.insert(3, 6)
valores.sort()#Isso é uma maneira de colocar em ordem também
print(sorted(valores))
valores.sort(reverse=True)#Esse metodo mostra em ordem só que de traz para frente
print(valores)

abc = ['a', 'd', 'c', 'b']
abc.append('e')
abc.sort()
print(abc)
abc.pop()
del(abc[3])
abc.remove('c')
print(abc)
print(f'Essa lista tem {len(abc)} elementos!')


nvalor = []
nvalor.append(5)
nvalor.append(9)
nvalor.append(4)
nvalor.append(9)
print(nvalor)
for cont in range(0, 5):
    nvalor.append(int(input('Digite um valor: ')))
for c, v in enumerate(nvalor):
    print(f'Na poosição {c}, encontrei o valor {v}!')
print('Cheguei ao finalda lista!')
