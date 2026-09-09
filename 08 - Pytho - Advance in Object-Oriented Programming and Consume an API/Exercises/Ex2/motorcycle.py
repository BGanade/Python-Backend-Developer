from vehicle import Vehicle
# 5


class Motorcycle(Vehicle):
    def __init__(self, brand, model, motorcycle_type) -> None:
        super().__init__(brand, model)
        self._type = motorcycle_type  # Sport or Casual

    # 6
    def __str__(self) -> str:
        return f'{super().__str__()}, Type: {self._type}'
