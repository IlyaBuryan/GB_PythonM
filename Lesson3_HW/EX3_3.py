# 3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в
# словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.

list1 = [i for i in range(20)]
list2 = [i for i in range(100, 110)]
list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def concat(first, second):
    a = dict(zip(first, second))

    dif = len(first) - len(second)
    if dif > 0:
        for i in range(dif):
            a[first[len(second) + i]] = None
    print(a)


concat(list3, list1)
