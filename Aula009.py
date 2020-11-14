print('FATIAMNETO')
frase = 'Programação'
#Função len() para contar as letras e espaços
resul = len(frase)
print('A palavra {} tem {} letras'.format(frase, resul))
#Método [] para mostrar somente a letra desejada.[:] começa antes dos postos e termina no final.[::]começa e termina pulando tantas casas
print(frase[6])
print(frase[6:10])
print(frase[6:])
print(frase[4:6])
print(frase[:10])
print(frase[0::2])
#Método .count('x') para contar quantas letras tem na palavra 
print(frase.count('a'))
print('TRANSFORMAÇÃO DE STR')
#Método .replace para colocar em cima uma nova frase
print(frase.replace('ção',' de tv'))
print(frase.find('gra'))
#Método upper() para colocar em maiusculo, e lower() em minusculo(mantendo o que ja esta)
print(frase.upper())
print(frase.lower())
frase = frase.replace('ção',' de tv')
print(frase)
print('de'in frase)
nf = '   Novo Teste de Python'
print(nf.strip())
print(nf.split())
dividido = nf.split()
print(dividido[0])
print(dividido[3][3])








