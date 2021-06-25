# отсортируем по убыванию
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers.sort(key=lambda x: -x)
print(my_numbers)
# и по возрастанию
my_numbers.sort(key=lambda x: +x)
print(my_numbers)

# сортировка по 1 элементу
my_pairs = [(1, 5), (4, 2), (6, 11)]
my_pairs.sort(key=lambda x: x[0])
print(my_pairs)

# Функция reduce
# Сжимает список
# 1+2 = 3, 3+3=6...
from functools import reduce
my_list = [1, 2, 3, 4, 5, 6]
print(reduce(lambda x, y: x+y, my_list))
# фактроиал
n = 10
print(reduce(lambda x, y: x*y, range(1, n+1)))
