nome = str(input('Olá,seja bem-vindo, por favor digite os seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculo é:{} '.format(nome.upper()))
print('Seu nome em minusculo é:{} '.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
novonome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(novonome[0])))





