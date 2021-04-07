"""
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os


def print_directory_contents(sPath):
    for i in os.listdir(sPath):
        link = os.path.join(sPath, i)
        if os.path.isfile(link):
            print(os.path.split(link))
        else:
            print_directory_contents(os.path.join(sPath, i))
