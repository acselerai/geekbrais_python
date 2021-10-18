class InvalidAmount(Exception):
    pass


class Warehouse():
    def __init__(self):
        self.items = {}

    def add_item(self, item, amount=1):
        self.validate_amount(amount)
        item_id = item.brand + item.model
        if self.items.get(item_id):
            self.items[item_id] += amount
        else:
            self.items[item_id] = 1

    def obtain_item(self, item, amount=1):
        item_id = item.brand + item.model
        warehouse_amount = self.items.get(item_id)
        self.validate_obtain_amount(amount, warehouse_amount)
        if warehouse_amount:
            self.items[item_id] -= amount
        else:
            self.items[item_id] = 0

    def validate_amount(self, amount):
        if not isinstance(amount, int):
            raise InvalidAmount('Amount should be an integer')

    def validate_obtain_amount(self, amount, warehouse_amount):
        self.validate_amount(amount)
        if warehouse_amount < amount:
            raise InvalidAmount('Not enough amount at warehouse')


class OfficeEquipment():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, dpi):
        super().__init__(brand, model)
        self.dpi = dpi


class Printer(OfficeEquipment):
    def __init__(self, brend, model, type):
        super().__init__(brend, model)
        self.type = type


class Xerox(OfficeEquipment):
    def __init__(self, brend, model, speed):
        super().__init__(brend, model)
        self.speed = speed
