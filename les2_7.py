number = int(input('Введите число: '))
seq = [1]
sum_n = 0
for i in range(number):
    if i > 0:
        seq.append(1 + i)
for j in seq:
    sum_n = sum_n + j
print(f'Сумма последовательности {number} чисел ({seq}) это {sum_n} что равно ({number}*({number+1})/2)')