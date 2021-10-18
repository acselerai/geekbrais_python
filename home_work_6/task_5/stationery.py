class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Start drawing'


class Pen(Stationery):
    def draw(self):
        return 'Pen drawing'


class Pencil(Stationery):
    def draw(self):
        return 'Pencil drawing'


class Handle(Stationery):
    def draw(self):
        return 'Handle drawing'
