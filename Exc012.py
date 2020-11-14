print('VAMOS CALCULAR 5% DE DESCONTO ')
preço = int(float(input('Qual o valor do produto ? ')))
mu = preço * 5
di = mu / 100
novopreço = preço - di
print('O valor de {}R$ reais com 5% de desconto, agora vale {}R$ reais \nE teve um descoonto de {}R$ reais'.format(preço, novopreço, di))
