#Laço de REPETIÇÃO
for c in range(11, 0, -1):
    print(c)
print('Fim')
for c in range(0, 6):
    print('Olá Mundo!')
for c in range(0, 11):
    print(c)
for c in range(1, 6):
    print('OI')
    print('OLÁ')
    print('TCHAU')
#Contando pulando de 2 em 2
for c in range(0, 11, 2):
    print(c)
num = int(input('Digite um número: '))
for c in range(0, num+1):
    print(c)
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('A soma é {}'.format(s))