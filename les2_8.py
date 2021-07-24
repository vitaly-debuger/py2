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
