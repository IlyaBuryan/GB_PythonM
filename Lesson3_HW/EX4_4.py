# 4. Написать программу, в которой реализовать две функции.
# В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить
# два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам
# функцию zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы
# каждая строка файла содержала текстовое и числовое значение.

# Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
# Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
# Вся программа должна запускаться по вызову первой функции.
import random
import os


# Для тренировки реализовал на ООП
class WorkWithFiles:

    def fileread(self, filedir):
        try:
            with open(f'{filedir}', 'r', encoding='utf-8') as file:
                for i in file.readlines():
                    print(i, end='')
        except FileNotFoundError:
            print('Файла НЕ существует!')

    def filecreation(self, filename):
        try:
            with open(f'{filename}', 'x', encoding='utf-8') as file:
                list1 = [i for i in range(20)]
                list2 = [random.choice('abc') for i in range(20)]
                zipped_list = list(zip(list1, list2))
                for i in zipped_list:
                    print(*i, file=file)
            print(os.path.abspath(filename))
            self.fileread(os.path.abspath(filename))
        except FileExistsError:
            print('Файл уже существует!')


ex = WorkWithFiles()
ex.filecreation('somefile.txt')
