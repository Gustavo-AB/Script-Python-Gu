print('CALCULADOR DE AUMENTO DE SALARIO')
vs = int(float(input('Qual o valor do salario ? ')))
vd = int(float(input('Qual o valor do aumento ? ')))
mu = vs * vd
di = mu / 100
ns = vs + di
print('Seu novo salario é de {}R$ \nVocê teve um aumento de {}R$'.format(ns, di))
