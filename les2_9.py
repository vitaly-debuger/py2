def sum_of_digits(num):
    sum_u = 0
    while num > 0:
        sum_u += num % 10
        num //= 10
    return sum_u
sub = input('Введите последовательность натуральных чисел через пробел').split()
total_sum = 0
for i in sub:
    a = int(i)
    b = sum_of_digits(a)
    if b > total_sum:
        total_sum = b

print(total_sum)
