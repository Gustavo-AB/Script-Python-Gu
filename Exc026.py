frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posção {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A')+1-frase.count(' ')))
