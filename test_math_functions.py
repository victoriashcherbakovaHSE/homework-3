import pytest
from fractions import Fraction

from functions import find_min, find_max, find_sum, find_product, find_sum_of_min_and_max

file_1 = ['24', '-0.18', '342', '24.244', '100', '-82', '-30.02']
file_2 = ['2341', '583', '-0.234', '502.12', '34', '-12.00000000000000000002', '4000']
file_11 = []
file_22 = []
for i in range(len(file_1)):
    file_11.append(Fraction(file_1[i]))
for i in range(len(file_2)):
    file_22.append(Fraction(file_2[i]))


def test_find_min():
    assert find_min(file_11) == '-82'
    assert find_min(file_22) == '-600000000000000000001/50000000000000000000'


def test_find_max():
    assert find_max(file_11) == '342'
    assert find_max(file_22) == '4000'


def test_find_sum():
    assert find_sum(file_11) == '94511/250'
    assert find_sum(file_22) == '372394299999999999999999/50000000000000000000'


def test_find_product():
    assert find_product(file_11) == '-27554256073872/3125'
    assert find_product(file_22) == '20445772815210600000034076288025351/78125000000000000000'


def test_find_sum_of_min_and_max():
    assert find_sum_of_min_and_max(file_11) == '260'
    assert find_sum_of_min_and_max(file_22) == '199399999999999999999999/50000000000000000000'
