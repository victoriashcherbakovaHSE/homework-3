from fractions import Fraction


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
