# Написать функцию (несколько функций), реализующую вывод таблицы умножения размерностью AｘB.
# Первый и второй множитель должны задаваться в виде аргументов функции.


def validate_value(x):
    """
    Функция валидации значения
    Выкинет исключение, если тип данных не int
    """
    if type(x) == int and x > 0:
        return x
    raise ValueError('Введенное значение имеет тип не Int > 0')


# Первый вариант с while
def multiplication_table1(a, b):
    """Функция вывода таблицы умножения AxB"""
    validate_value(a)
    validate_value(b)

    i = 1
    while i <= a:
        j = 1
        while j <= b:
            print(f'{i} x {j} = {i * j}')
            j += 1
        i += 1


# Вариант 2 сделан как просилось в методичке (просто для тренировки)
def multiplication_table2(a, b):
    """Функция вывода таблицы умножения AxB"""
    validate_value(a)
    validate_value(b)

    result = []
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            result.append(f'{i} x {j} = {i * j}')

    print_result = lambda x: print(*x, sep='\n')
    print_result(result)


multiplication_table1(3, 3)
print()
multiplication_table2(3, 3)
