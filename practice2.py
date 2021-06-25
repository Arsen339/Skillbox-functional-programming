ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "//": lambda x, y: x // y,
    "%": lambda x, y: x % y

}

total = 0
def calc(line):
        print(f"Read line {line}", flush=True)  # flush-вывод сразу после команды print без буферизации
        operand1, operation, operand2 = line.split(" ")  # разбиение на пробелы
        if operation in ops:
            func = ops[operation]
            value = func(int(operand1), int(operand2))
        else:
            print(f"Unknown operand {operation}")
            value = None
        print("value is ", value)
        return value

# Упростим код используя генератор
def get_lines(file_name):
    with open(file_name, 'r') as ff:
        for line in ff:
            line = line[:-1]
            yield line


for line in get_lines(file_name="calc.txt"):
    try:
        total += calc(line)
    except ZeroDivisionError as zde:
        print(f"На ноль делить запрещено! {zde}")
    except ValueError as exc:
        if 'unpack' in exc.args[0]:
            print(f"Не хватает операндов {exc}")
        else:
            print(f"Не могу преобразовать к целому {exc}")
    except TypeError as tex:
        print(f"Ошибка типа {tex}")


print(f"Total {total}")