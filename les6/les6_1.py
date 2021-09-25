import sys
# number = input('Введите трехзначное число: ')
#
# sum_number = 0
# prod = 1
#
# for f in number:
#     sum_number += int(f)
#     prod *= int(f)
# print(f"Сумма цифр числа {number}: {sum_number}")
# print(f"Произведение цифр: {number}: {prod}")
#
# sum_size = 0
# sum_size += sys.getsizeof(number)
# sum_size += sys.getsizeof(sum_number)
# sum_size += sys.getsizeof(prod)
# sum_size += sys.getsizeof(f)
#
# print('Переменные занимают', sum_size)
# сумма переменных 158

# a = int(input('Введите целое трехзначное число:'))
#
# print(f'Сумма цифр в числе: {(a // 100) + ((a // 10) % 10) + (a % 10)}')
# print(f'Произведение цифр в числе: {(a // 100) * ((a // 10) % 10) * (a % 10)}')
#
#
# print('Переменные занимают', sys.getsizeof(a))

# сумма переменных 28, меньше переменных меньше проблем =)

import random
n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
sub = []
count = 0
for i in range(1, n + 1):
    m = random.randint(0, 100)
    sub.append(m)
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10
print(f'В последовательности {sub} было найдено {count} цифр {d}')

sum_size = 0
sum_size += sys.getsizeof(n)
sum_size += sys.getsizeof(d)
sum_size += sys.getsizeof(sub)
sum_size += sys.getsizeof(count)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(m)

print(sys.getsizeof(sub))
print('Переменные занимают', sum_size)
# сумма переменных 320
# python v3.9 win_x64