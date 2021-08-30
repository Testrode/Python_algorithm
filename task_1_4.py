import random
import string

lst = ['rand_int','rand_float','rand_sign']
choice = lst[random.randint(0,2)]
if choice == 'rand_int':
    print(random.randint(0,9))
if choice == 'rand_float':
    print(random.random())
if choice == 'rand_sign':
    print(''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(1)]))