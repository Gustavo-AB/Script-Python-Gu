valor1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = valor1 + (10 - 1) * razao
for q in range(valor1, decimo+razao, razao):
    print('{}'.format(q), end='-')
print('Acabou!')
