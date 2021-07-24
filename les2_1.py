while True:
    try:
        operation = input('Выберете операцию + - * / \nДля выхода введите 0 : ')
        if operation == '0':
            break
        elif operation not in [0, '+', '-', '*', '/']:
            print('Вы ввели недопустимый символ')
            continue
        else:
            numbers = input('Введите 2 числа для вычисления через пробел: ').split()
            if operation == '+':
                s = int(numbers[0]) + int(numbers[1])
                print(f'Сумма = {s}')
            if operation == '-':
                d = int(numbers[0]) - int(numbers[1])
                print(f'Разность = {d}')
            if operation == '*':
                c = int(numbers[0]) * int(numbers[1])
                print(f'Произведение = {c}')
            if operation == '/':
                q = int(numbers[0]) / int(numbers[1])
                print(f'Разность = {q}')
    except ZeroDivisionError:
        print('Ай красава, на ноль делить низя!')
