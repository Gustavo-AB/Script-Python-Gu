from time import sleep
print('-=' * 20)
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
#Numero menor!!!
if n2>n1 and n3>n1:
    menor = n1
if n1>n2 and n3>n2:
    menor = n2
if n1>n3 and n2>n3:
    menor = n3
#Numero maior!!!
if n2<n1 and n3<n1:
    maior = n1
if n1<n2 and n3<n2:
    maior = n2
if n1<n3 and n2<n3:
    maior = n3
print('...')
sleep(1)
print('O menor número é o {}!\nE o maior é o {}!'.format(menor, maior))
print('-=' *20)