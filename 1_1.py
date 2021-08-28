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

# 2 вариант
a = int(input('Введите целое трехзначное число:'))
b = a // 100
c = (a // 10) % 10
d = a % 10

summa = b + c + d
mult = b * c * d

print(f'Сумма цифр в числе: {summa}')
print(f'Произведение цифр в числе: {mult}')