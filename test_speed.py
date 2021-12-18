from fractions import Fraction
from functions import find_min, find_max, find_sum, find_product, find_sum_of_min_and_max
from math import factorial

# я здесь задавала 5 файлов, в которых лежали 10, 100, 1000, 10000 и 100000 чисел. Для каждого делала отдельно тесты
# и смотрела время выполнения, прикреплю файл пдф с скринами выполнения (там где-то микросекунды, а где-то даже
# минуты) так как тесты делала отдельно, то здесь идёт проверка на file_4 как пример (я абсолютно аналогично делала
# для остальных)

file_1 = []
file_2 = []
file_3 = []
file_4 = []
file_5 = []
for i in range(10):
    file_1.append(Fraction(str(i + 1)))

for i in range(100):
    file_2.append(Fraction(str(i + 1)))

for i in range(1000):
    file_3.append(Fraction(str(i + 1)))

for i in range(10000):
    file_4.append(Fraction(str(i + 1)))

for i in range(100000):
    file_5.append(Fraction(str(i + 1)))


def test_find_min():  # 1 1 1 1 1 - ответы на файлы 1-5
    assert find_min(file_4) == '1'


def test_find_max():  # 10 100 1000 10000 100000 ответы на файлы 1-5
    assert find_max(file_4) == '10000'


def test_find_sum():  # 55 5050 500500 50005000 5000050000 ответы на файлы 1-5
    assert find_sum(file_4) == '50005000'


def test_find_product():  # факториал 10 100 1000 10000 100000 ответы на файлы 1-5
    assert find_product(file_4) == str(factorial(10000))


def test_find_sum_of_min_and_max():  # 11 101 1001 10001 100001 ответы на файлы 1-5
    assert find_sum_of_min_and_max(file_4) == '10001'
