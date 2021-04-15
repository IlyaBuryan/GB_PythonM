# 1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
# При вызове функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо
# реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).


import os


# Basedir - пришлось добавить базовую дирректорию поиска, чтобы функция знала где рекурсивно искать, можно задать диск
# filename - имя файла, который функция будет искать рекурсивно во всех вложенных папках

def print_directory_contents(filename, baseDir):
    for i in os.listdir(baseDir):
        link = os.path.join(baseDir, i)
        if not os.path.isdir(link):
            if i == filename:
                print('Полный путь: ', link)
                print('Имя файла: ', os.path.basename(i)[:i.find('.')])
        else:
            print_directory_contents(filename, os.path.join(baseDir, i))


print_directory_contents('97.psd', r'C:\GeekBrains\usefull')
