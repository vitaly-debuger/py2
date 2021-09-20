
def sieve_without_eratosthenes(i):
    '''Функция поиска i-го простого числа,
    без использования алгоритма «Решето Эратосфена»
    '''

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]





user_number = int(input('Введите номер по счету простого числа: '))

print('Алгоритм  без использования алгоритма «Решето Эратосфена»')
print(
    f'{sieve_without_eratosthenes(user_number)} - {user_number} \
по счёту простое число'
)

