class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} rides'

    def stop(self):
        return f'{self.name} stopped'

    def turn(self, direction):
        return f'{self.name} turned {direction}'

    def show_speed(self):
        return f'{self.name} speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Speed limit is reached: {self.speed}'
        else:
            return super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Speed limit is reached: {self.speed}'
        else:
            return super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass
