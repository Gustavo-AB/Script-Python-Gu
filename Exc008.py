m = int(input('Digite um valor numerico em metros ! '))
c = m * 100
mi = m * 1000
km = m / 1000
hc = m / 100
print('{} metro(s)\nÉ equivalente a {} centimetros \nE {} milimetros !'.format(m, c, mi))
print('E {}km\n{}hc'.format(km, hc))