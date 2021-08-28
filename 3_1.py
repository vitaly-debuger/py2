MAX_NUMBER = 99
MIN_DIV = 2
MAX_DIV = 9

print('Делитель    Чисел на него делится')

for div in range(MIN_DIV, MAX_DIV + 1):
    print(f'{div:>6} {MAX_NUMBER // div:>16}')