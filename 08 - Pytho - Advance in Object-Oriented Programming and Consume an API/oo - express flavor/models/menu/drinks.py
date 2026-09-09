from models.menu.menu_item import MenuItem


class Drinks(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size
        self._drink = True

    def __str__(self):
        return self._name

    def apply_discount(self):
        self._price -= self._price * 0.05
