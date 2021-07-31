import cProfile

minDiv = 2
maxDiv = 9


def div_count(max_number):
    div_dict = dict()

    for _ in range(minDiv, maxDiv + 1):
        div_dict[_] = max_number // _

    return div_dict


def div_count_1(max_number):
    div_dict = dict()

    for _ in range(minDiv, maxDiv + 1):
        div_dict[_] = 0

        for num in range(2, max_number + 1):

            if num % _ == 0:
                div_dict[_] += 1

    return div_dict


#total = 99
#print(div_count_1(total))
#print(div_count(total))

def main():
    total = 99*100
    res1 = div_count(total)
    res2 = div_count_1(total)

if __name__ == '__main__':
    cProfile.run('main()')


по первому заданию
1 вариант о(1) тк при увеличении числа время статично
2 вариант имеет линейную сложность o(n) тк при увеличении числа передаваемого в функции на 10 , время тоже увеличивается примерно в 10 раз

