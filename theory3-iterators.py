def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x ** 3
    else:
        raise Exception("Я могу делать множители только 2 и 3")
    return multiplier


# вызов
my_numbers = [1, 2, 3, 4, 5]
by_2 = get_multiplier_v1(2)
result = map(by_2, my_numbers)
print(list(result))

def get_multiplier_v2(n):

    def multiplier(x):
        return x * n
    return multiplier


my_numbers = [1, 2, 3, 4, 5]
by_2 = get_multiplier_v2(10)
result = map(by_2, my_numbers)
print(list(result))

# лямбда-функция - одноразовая функция. return перед x+10

print(list(map(lambda x:  x+10, my_numbers)))
my_func = lambda x: x + 10
print(my_func(42))