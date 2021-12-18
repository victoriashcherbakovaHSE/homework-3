from fractions import Fraction

file_name = input('Введите название файла(если Вы уже поместили его в папку с кодом) или абсолютный путь к файлу: ')
file = open(file_name, "r")
values = file.read().split("\n")
data = []
for i in range(len(values)):
    data.append(values[i].split())

data_new = []
for i in range(len(data)):
    a = data[i]
    for j in range(len(a)):
        data_new.append(Fraction(a[j]))

# вывод в виде дроби для максимальной точности (если вещественное число больщое с точки зрения памяти)


def find_min(l1):
    p = sorted(l1)
    return str(p[0])


def find_max(l2):
    b = sorted(l2)
    return str(b[len(b) - 1])


def find_sum(l3):
    sum = Fraction(0)
    for i in l3:
        sum = sum + i
    return str(sum)


def find_product(l4):
    product = Fraction(1)
    for i in l4:
        product = product * i
    return str(product)


def find_sum_of_min_and_max(l5):       # Для получения оценки "4": реализуйте любой другой тест на ваше усмотрение
    r = sorted(l5)
    return str(r[0] + r[len(r) - 1])


print('Результат любой функции может быть выведен в виде дроби для максимальной точности вычислений')
print('Минимальное число:', find_min(data_new))
print('Максимальное число:', find_max(data_new))
print('Сумма:', find_sum(data_new))
print('Произведение:', find_product(data_new))
print('Сумма минимального и максимального числа:', find_sum_of_min_and_max(data_new))
