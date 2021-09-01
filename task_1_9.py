first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

lst = []
lst.append(first_number)
lst.append(second_number)
lst.append(third_number)

lst.remove(min(lst))
lst.remove(max(lst))

print(f'Среднее число: {lst}')
