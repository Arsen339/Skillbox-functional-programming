class Family:
    def __init__(self):
        self.dad = "Алексей"
        self.son = 'Максим'
        self.mom = 'Мария'
        self.i = 0

    def __iter__(self):
        self.i = 0
        # возвращает ссылку на себя
        return self

    def __next__(self):
        self.i += 1
        if self.i == 1:
            return f"Папа {self.dad}"
        if self.i == 2:
            return f"Мама {self.mom}"
        if self.i == 3:
            return f"Сын {self.son}"
        if self.i == 4:
            return "Счастливая семья"
        raise StopIteration()  # Признак завершения
# Сначала в цикл заходит iter, а потом next, цикл бесконечен


my_family = Family()
# print(my_family)
for value in my_family:
    print(value)

# Последовательность Фиббоначе. Функция создаст в памяти огромный список - нерационально
def fibonacci(n):
    result = []
    a, b = 0, 1
    """_ - значение"""
    for _ in range(n):
        result.append(a)
        a = b
        b = a + b
    return result


fib = fibonacci(n=10)
print(fib)
for value in fib:
    print(value)

# Рациональнее - с помощью итератора
class FibCount:
    def __init__(self, n):
        self.a, self.b, self.i, self.n = 0, 1, 0, n

    def __iter__(self):
        self.a, self.b, self.i = 0, 1, 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b

        return self.a


FI = FibCount(80)
for value in FI:
    print(value)
print(5527939700884757 in FI)

# Оператор yield - возвращать значение - генераторы
def fibonacci2(n):

    a, b = 0, 1
    """_ - значение"""
    for _ in range(n):
        yield a
        a, b = b, a + b


res = fibonacci2(5)
res2 = fibonacci2(5)
# По генератору можно пройти 1 раз! Выведет false
for value in res:
    print(value)
print(1 in res)
print(1 in res2)
# Генератор очереди
def queue(*args):
    data = list(args)
    while data:
        next = data.pop(0)
        new_value = (yield next)
        if new_value is not None:
            data.append(new_value)


shop_queue = queue("Владислав", "Андрей", "Елена")
for name in shop_queue:
    print(f"К кассе приглашается {name}")
    if name == "Андрей":
        print("А кто последний?")
        name = shop_queue.send("Алексей")
        print(f"К кассе приглашается {name}")

import time
# Напишем функцию, которая берет на вход другую функцию
def time_track(func, *args, **kwargs):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f"Функция работает {elapsed} секунд")
        return result
    return surrogate

# Декоратор передает функцию в другую функцию
@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


# засечем время выполнения


"""
started_at = time.time()
result = digits(3141, 5926, 2718, 2818)
print(result)
ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f"Функция работает {elapsed} секунд")"""

result = digits(3141, 5926, 2718, 2818)
print(result)



