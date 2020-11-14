from random import shuffle
print('APRESENTAÇÃO DOS TRABALHOS-POR SORTEIO')
al1 = str(input('Primeio aluno: '))
al2 = str(input('Segundo aluno:'))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A órdem de apresentação será')
print(lista)
