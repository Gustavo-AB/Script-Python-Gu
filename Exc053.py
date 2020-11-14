frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = junto[::-1]
print('A frase é de tras para frente fica assim {}!'.format(invertido))
#for letra in range(len(frase)+1):
if junto == invertido:
    print('E temos um PALINDROMO!')
