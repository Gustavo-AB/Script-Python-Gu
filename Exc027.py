nome = str(input('Qual é o seu nome completo ? ')).strip().title()
nodi = nome.split()
print('Primeiro nome: {}'.format(nodi[0]))
print('Ultimo: {}'.format(nodi[-1]))

