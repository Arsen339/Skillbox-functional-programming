def get_russian_names():
    return ['Ваня', 'Коля', 'Маша']


# Имя функции указывает на объект функции
print(type(get_russian_names))
# Можно узнать название функции
print(get_russian_names.__name__)
my_func = get_russian_names
print(my_func)
print(my_func.__name__)


# Функция как объект
def get_british_names():
    return ['Garry', 'Oliver', 'Harry']


name_get = [get_british_names, get_russian_names]
for name in name_get:
    print(name())


# Передача функции в функцию
def print_names(message, name_getting):
    print(message, name_getting())


print_names(message='Русские имена', name_getting=get_russian_names)

# Словарь из функций
print('              ')
names = {'Русские имена': get_russian_names, "Английские имена": get_british_names}
for message, name_getter in names.items():
    print_names(message, name_getter)


def adder(*args):
    res = 0
    for number in args:
        res += number
    return res

def multiplier(*args):
    res = 0
    for number in args:
        res *= number
    return res

def process_numbers(numbers, handler):
    result = handler(*numbers)
    print(f"Получилось  {result}")


my_numbers = [1, 2, 3, 4, 5]

process_numbers(numbers=my_numbers,handler=adder)


def mul_by_2(x):
    return x * 2


# вернет нечетные
def is_odd(x):
    return x % 2


# map - прогон по списку, list - формирование массива
print(list(map(mul_by_2, my_numbers)))
# filter - если True, сатавляет элемент в список
my_numbers = [1, 2, 0, 4, 5]
print(list(filter(is_odd, my_numbers)))

# выведем сумму от нечетных чисел умноженных на 2
print(sum(list(map(mul_by_2, filter(is_odd, my_numbers)))))

# Списковая сборка
result = [x * 3 for x in my_numbers]
print(result)
print("Выведем все числа не кратные 2")
print([x for x in my_numbers if x % 2])
# умножение каждого элемента с каждым
my_numbers = [1, 2, 3, 4, 5]
they_numbers = [5, 4, 3, 2, 1]
print([x * y for x in my_numbers for y in they_numbers])