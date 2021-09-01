# coding:utf-8

import random
import string

rand_int_a = int(input('Выберите случайное число от: '))
rand_int_b = int(input('До: '))
print(random.randint(rand_int_a, rand_int_b))
rand_float_a = int(input('Выберите случайное число от: '))
rand_float_b = int(input('До: '))
print(random.uniform(rand_float_a,rand_float_b))
rand_symb_a = input('Выберите начало диапазона от a - z: ')
rand_symb_b = input('Выберите диапозон ДО: ')
rand_symb_a = ord(rand_symb_a)
rand_symb_b = ord(rand_symb_b)
print(chr(random.randint(rand_symb_a,rand_symb_b)))


