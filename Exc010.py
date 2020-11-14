print('{:=^10}'.format('VAMOS DESCOBRIR QUANTOS DÓLARES VOCÊ PODERIA COMPRAR COM O DINHEIRO QUE VOCÊ TEM!'))
dinheiro = float(input('Quanto dinheiro você tem ? R$'))
print('Você consegue comprar US${:.2f} dolares com R${:.2f} reais'.format(dinheiro/5, dinheiro))