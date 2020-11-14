#INTERROMPENDO LAÇOS DE REPETIÇÃO COM O 
num = cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    cont += 1 
    if num == 999:
        break
    soma += num
print(f'Você digitou {cont-1} números e a soma entre eles é igual a {soma}')
nome = 'gustavo'.title()
print(f'Calculadora{nome:=^20}')
