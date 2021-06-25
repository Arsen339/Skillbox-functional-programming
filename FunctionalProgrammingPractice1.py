# На основе алгоритма создать класс итерируемых объектов
# распечатать все простые числа до 10000 в столбик
# Сделать генератор

def set_simple_numbers(n):
    """Функция, возвращающая массив простых чисел"""
    simple_numbers = []
    for number in range(2, n+1):
        for simple in simple_numbers:
            if number % simple == 0:
                break
        else:
            simple_numbers.append(number)
    return simple_numbers


class SimpleNumbers:
    """Класс-итератор, возвращающий простые числа"""
    def __init__(self, n):
        self.number, self.i, self.counter, self.n = 1, 0, 0, n

    def __iter__(self):
        self.number, self.i, self.counter = 0, 1, 0
        return self

    def __next__(self):
        self.number += 1
        self.counter = 0
        if self.number > 1:
            if self.number >= self.n+1:
                raise StopIteration()
            for self.i in range(1, self.number+1):
                if self.number % self.i == 0:
                    self.counter += 1
                if self.counter >= 3:
                    return None
            else:
                return self.number


def simple_numbers_generator(n):
    """Функция-генератор, возвращающая массив простых чисел"""
    for number in range(2, n + 1):
        for simple in simple_numbers_generator(number-1):
            if number % simple == 0:
                break
        else:
            yield number


limit = 30  # Число, до которого выводятся простые числа
# Класс:
simple_numbers_list = SimpleNumbers(limit)
for value in simple_numbers_list:
    print(value)
# Функция
print("Результат работы функции ", set_simple_numbers(limit))
# Генератор
for value in simple_numbers_generator(limit):
    print(value)