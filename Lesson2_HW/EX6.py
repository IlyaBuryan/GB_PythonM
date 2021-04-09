# 6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
# на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая
# в первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать
# выполнение каждой из функции тремя способами.


class ItemDiscount:
    _name = 'Computer'
    _price = 9.99

    @staticmethod
    def set_price(new_price):
        ItemDiscount._price = new_price

    def get_info(self):
        return f'{self._name}, {self._price}'


class ItemDiscountReport1(ItemDiscount):

    def get_info(self):
        return self._name


class ItemDiscountReport2(ItemDiscountReport1):

    def get_info(self):
        return self._price


ex = ItemDiscount()
child1 = ItemDiscountReport1()
child2 = ItemDiscountReport2()

print(ex.get_info())
print(child1.get_info())
print(child2.get_info())
