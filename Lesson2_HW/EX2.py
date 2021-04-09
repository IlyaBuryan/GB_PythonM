# 2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении
# текущей логики работы программы будет сгенерирована ошибка выполнения.


# Выпадает ошибка: AttributeError: 'ItemDiscountReport' object has no attribute 'name'
class ItemDiscount:
    _name = 'Computer'
    _price = 9.99


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.name} стоит {self.price}'


ex = ItemDiscountReport()
print(ex.get_parent_data())
