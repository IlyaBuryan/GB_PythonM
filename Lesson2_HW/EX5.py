# 5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента
# в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод init, в который
# должна передаваться переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна
# пересчитываться цена и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не
# забудьте инициализировать дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).


class ItemDiscount:
    _name = 'Computer'
    _price = 9.99

    @staticmethod
    def set_price(new_price):
        ItemDiscount._price = new_price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount):
        self.discount = discount

    def __str__(self):
        return f'Цена со скидкой: {self._price * (self.discount / 100)}'

    def get_parent_data(self):
        return f'{self._name} стоит {self._price}'


ex = ItemDiscount()
print(ex._price)
ex.set_price(123)
print(ex._price)

ex2 = ItemDiscountReport(50)
print(ex2.get_parent_data())
print(ex2)