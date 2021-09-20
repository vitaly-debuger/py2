numbers = int(input('Введите число: '))
chet = []
nechet = []
c_chet = 0
c_nechet = 0
while numbers:
    if (numbers % 10) % 2 ==0:
        c_chet += 1
        chet.append(numbers % 10)
    else:
        nechet.append(numbers % 10)
        c_nechet += 1
    numbers = numbers // 10
print(f'Вы ввели {c_chet} четных {chet} и {c_nechet} нечетных {nechet}')

seq = []
number = int(input('Введите число: '))
for i in range(number)):
    seq.append(1 / i**number)
print(seq)
