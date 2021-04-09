# 1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
# должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
# должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.

class ItemDiscount:
    name = 'Computer'
    price = 9.99


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.name} стоит {self.price}'


ex = ItemDiscountReport()
print(ex.get_parent_data())
