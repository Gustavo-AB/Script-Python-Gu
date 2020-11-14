num = cont = soma = 0
num = int(input('Digite um valor: '))
while num != 999:
    soma += num 
    cont += 1
    num = int(input('Digite um valor: '))
print('A soma entre os {} números digitados é igual a {}'.format(cont, soma))