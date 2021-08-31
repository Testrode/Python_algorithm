select_year = int(input('Выберите год: '))
definition = select_year % 4
if definition == 0:
    print(f'{select_year} високосный год')
else: print(f'{select_year} обычный год')