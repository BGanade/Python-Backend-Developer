from models.menu.menu_item import MenuItem


class Dessert(MenuItem):
    def __init__(self, name, price, description, type, size):
        super().__init__(name, price)
        self._description = description
        self._type = type
        self._size = size
        self._dessert = True

    def __str__(self) -> str:
        return self._name

    def apply_discount(self):
        self._price -= self._price * 0.15
