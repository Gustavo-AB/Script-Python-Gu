print('=' * 40)
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para converção:
[1]-Converter para BÍNARIO
[2]-Converter para OCTAL
[3]-Converter para HEXADECIMAL''')
print('=' * 40)
opçao = int(input('Digite sua opção: '))
if opçao == 1:
    print('O número {} convertido para BINÁRIO é igual a {}!'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('O número {}, convertido em OCTAL é igual a {}!'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('O número {}, convertido para HEXADECIMAL é igual a {}!'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
print('=' * 40)