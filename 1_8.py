year = int(input('Введите год '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Високосный год')
        else:
            print('Невисокосный год')
    else:
        print('Високосный год')
else:
    print('Невисокосный год')