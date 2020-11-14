from random import choice
print('SROTEIO DE ALUNOS')
al1 = input('Nome do primeiro aluno: ')
al2 = input('Nome do segundo aluno: ')
al3 = input('Nome do terceiro açuno: ')
al4 = input('Nome do quarto aluno: ')
lista = [al1, al2, al3, al4]
res = choice(lista)
print('O aluno sorteado foi {}'.format(res))
