#Condições aninhadas
nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Gustavo':
    print('Que nome bonito!!')
elif nome == 'Alvarez':
    print('Esse nome é bem legal!!')
elif nome in 'Alvarez' or 'Barboza':
    print('Seu sobrenome é muito bonito!!')
else:
    print('Legal esse nome!!')
novon = nome.split()
print('Tenha um bom dia {}!!'.format(novon[0]))
