valor = (int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')))


print('-' * 30)
print('Você digitou os seguintes valores:', end='')
for v in valor:
    print(f' {v}', end='')
print('!', end='')

print(f'\nO número 9 apareceu {valor.count(9)} vezes!')


if 3 in valor:
    print(f'O primeiro número 3, apareceu na posição {valor.index(3)+1}!')
else:
    print('O valor 3 não foi digitado!')


print(f'Os valores PARES digitados foram: ', end='')

for n in valor:
    if n % 2 == 0:
        print(f'{n} ', end='')
