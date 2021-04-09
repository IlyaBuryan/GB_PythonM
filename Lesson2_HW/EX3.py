# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:
    _name = 'Computer'
    _price = 9.99


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self._name} стоит {self._price}'


ex = ItemDiscountReport()
print(ex.get_parent_data())
