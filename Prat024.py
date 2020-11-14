soma = maior = menor = cont = media = 0

while True:
    num1 = int(input('Digite um número: '))
    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()
    cont += 1
    soma += num1
    media = soma / cont

    if escolha not in 'NnSs':
        while escolha not in 'SsNn':
            print('Opção inválida Digite novamente')
            escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()


    if cont == 1:
        maior = menor = num1
    else:
        if num1 > maior:
            maior = num1

    if num1 < maior:
        menor = num1


    if escolha in  'N':
        break

print(f'Foram digitados {cont} valores!')
print(f'A soma dos valores é de {soma}!')
print(f'A média dos valores é de {media}!')
print(f'O maior número é o {maior}!')
print(f'O menor número é o {menor}!')