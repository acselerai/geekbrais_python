from abc import ABC, abstractclassmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractclassmethod
    def material_amount(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__('Coat')
        self.size = size

    @property
    def material_amount(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        super().__init__('Suit')
        self.height = height

    @property
    def material_amount(self):
        return 2 * self.height + 0.3
