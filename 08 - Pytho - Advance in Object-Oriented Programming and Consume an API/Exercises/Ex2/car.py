# 3
from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, doors) -> None:
        super().__init__(brand, model)
        self._doors = doors

    # 4
    def __str__(self) -> str:
        return f'{super().__str__()}, Doors: {self._doors}'
