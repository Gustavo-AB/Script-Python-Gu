cid = str(input('Qual cidade você nasceu ? ')).title().strip()
print('Santo' in cid)
est = str(input('Qual estado você nasceu ? ')).strip().title()
print(est[:6].upper() == 'MINAS')

