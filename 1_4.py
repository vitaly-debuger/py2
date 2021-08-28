import random


def rand_char(a, b):
    return chr(random.randint(ord(a), ord(b))) if a < b else chr(random.randint(ord(b), ord(a)))


def rand_int(a, b):
    return random.randint(a, b) if a < b else random.randint(b, a)


def rand_uni(a, b):
    return round(random.uniform(a, b), 3) if a < b else round(random.uniform(b, a), 3)


data_type, start, stop = [
    x for x in
    input('Введите через пробел параметры: тип данных(int float или str) начальный и конечный элементы: ').split()
]

if data_type == 'int':
    a = int(start)
    b = int(stop)
    print(rand_int(a, b))

elif data_type == 'float':
    a = float(start)
    b = float(stop)
    print(rand_uni(a, b))

elif data_type == 'str':
    a = start
    b = stop
    print(rand_char(a, b))

else:
    print('Неправильно задан диапазон')
