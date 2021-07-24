number = int(input('Введите число: '))
seq = [1]
sum_n = 0
for i in range(number):
    if i > 0:
        seq.append(1 / 2 ** i)
for j in seq:
    sum_n = sum_n + j
print(f'Сумма числел последовательности {seq}\n : {sum_n}')

