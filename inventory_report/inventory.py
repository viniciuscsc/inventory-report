from inventory_report.product import Product


class Inventory:
    def __init__(self, data: list[Product] | None = None):
        if data is None:
            data = []
        self._data = data

    @property
    def data(self):
        return self._data

    def add_data(self, data: list[Product]) -> None:
        self._data.extend(data)
