numbers = int(input('Введите число: '))
revers = []
while numbers:
    revers.append(numbers % 10)
    numbers = numbers // 10
result = int((str(revers)).strip("[]").replace(", ", ""))
print(f'Ваше число наоборот: {result}')