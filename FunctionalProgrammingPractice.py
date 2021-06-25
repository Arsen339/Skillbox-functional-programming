# Написать функцию, повторяющую 2 первых символа строки
def simple_stutter(text):
    return text[:2] + '-' + text


# Написать функцию, повторяющую 2 первых символа строки n раз
def stutter_factory(n):
    def stutter(text):
        return (text[:2] + '-') * n + text
    return stutter


print(simple_stutter("Зайка"))

stutter_4 = stutter_factory(n=4)
print(stutter_4("Мишка"))

# Создадим массив функций и применим их поочередно к аргументу
stutters = [stutter_factory(n) for n in range(1, 10)]
for stutter_fun in stutters:
    print(stutter_fun("Мишка"))

# Применим все функции поочередно к массиву аргументов
mass = ["Заяц", "Бегемот", "Медведь"]

for stutter_fun in stutters:
    for i in range(len(mass)):
        print(stutter_fun(str(mass[i])))

# или отсортируем по порядку
mesh = [func(animal) for animal in mass for func in stutters]
print(mesh)