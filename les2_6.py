import random
answer = random.randint(0, 100)
tryCount = 0;
maxTryCount = 10;
while tryCount < maxTryCount:
    user_answer = int(input('Введите число, которые мы загадали, от 0 до 100 : '))
    tryCount += 1
    if user_answer < answer:
        print(f'Вы ввели число меньше загаданного\nсталось {10 - tryCount} попыток')
    elif user_answer > answer:
        print(f'Вы ввели число больше загаданного\nсталось {10 - tryCount} попыток')
    else:
        print(f'Вы угадали, число {answer} !')
        break
print(f'равильное число было {answer}')


