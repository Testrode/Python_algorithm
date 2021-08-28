A = input('Введите трехзначное число: ')
if len(A) == 3:
    A = int(A)
else: print(f'Вы ввели {len(A)} значное число')

B = input('Введите трехзначное число: ')
if len(B) == 3:
    B = int(B)
else: print(f'Вы ввели {len(B)} значное число')

C = input('Введите трехзначное число: ')
if len(C) == 3:
    C = int(C)
else: print(f'Вы ввели {len(C)} значное число')

print(f'Сумма чисел = {A + B + C}')
print(f'Произведение чисел = {A * B * C}')
