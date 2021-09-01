rand_symb_a = input('Первая буква a - z: ')
rand_symb_b = input('Вторая буква a - z: ')
rand_symb_a = ord(rand_symb_a)
position_a = rand_symb_a - 96
rand_symb_b = ord(rand_symb_b)
position_b = rand_symb_b - 96
distance = position_b - position_a
print(f'Позиция в алфавите первой буквы: {position_a}\n'
      f'Позиция в алфавите второй буквы: {position_b}\n'
      f'Между ними {distance - 1} букв')

