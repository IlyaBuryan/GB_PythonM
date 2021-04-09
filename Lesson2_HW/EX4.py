# 4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний
# классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса
# и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).


class ItemDiscount:
    _name = 'Computer'
    _price = 9.99

    @staticmethod
    def set_price(new_price):
        ItemDiscount._price = new_price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self._name} стоит {self._price}'


ex = ItemDiscount()
ex2 = ItemDiscountReport()
print(ex._price)
ex.set_price(123)
print(ex._price)

print(ex2.get_parent_data())
