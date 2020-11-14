print('-=' * 20)
dis = float(input('Qual é a distancia da viagem? '))
viac = dis * 0.50
vial = dis * 0.45
if dis <= 200:
    print('Você fara uma viagem de {}Km!\nO valor da viagem é R${:.2f}!!'.format(dis, viac))
else:
    print('Você fara uma viagem de {}KM!\nO valor da viagem é R${:.2f}!!'.format(dis, vial))
print('Aproveite a viagem!!\nTenha um bom dia!! ')
print('-=' * 20)