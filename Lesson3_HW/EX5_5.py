# 5. Усовершенствовать первую функцию из предыдущего примера.
# Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
# вывод первого вхождения, вывод всех вхождений.
# Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок, состоящих
# из букв и цифр и имеющих пробелы только в начале и конце — например, example345.


import random
import os
import re


# Надеюсь не запутался в формулировке задачи:) Постарался реализовать каждый пункт
class WorkWithFiles:

    def fileread(self, filedir):
        try:
            with open(f'{filedir}', 'r+', encoding='utf-8') as file:
                # Первое вхождение:
                print('Первое вхождение:')
                for i in file.readlines():
                    if re.search(r'.345', i):
                        print(i, end='')
                        file.seek(0)
                        break

                # Все вхождения: cbynf
                print('Все вхождения:')
                for i in file.readlines():
                    if re.search(r'.345', i):
                        print(i, end='')
                file.seek(0)

                # Все вхождения с заменой:
                print('Все вхождения:')
                for i in file.readlines():
                    if re.search(r'[0-9]+\s[a-z]+345', i):
                        i = random.choice((' example999 ', 'example777'))
                        if re.search(r'\s.+\s', i):
                            print(i, end='\n')
                file.seek(0)

        except FileNotFoundError:
            print('Файла НЕ существует!')

    def filecreation(self, filename):
        try:
            with open(f'{filename}', 'x', encoding='utf-8') as file:
                list1 = [i for i in range(20)]
                list2 = [random.choice(('abc', 'example345')) for i in range(20)]
                zipped_list = list(zip(list1, list2))
                for i in zipped_list:
                    print(*i, file=file)
            print(os.path.abspath(filename))
            self.fileread(os.path.abspath(filename))
        except FileExistsError:
            print('Файл уже существует!')


ex = WorkWithFiles()
ex.filecreation('somefile.txt')
