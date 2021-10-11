from time import sleep


class TrafficLight:
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    RED_TIME = 7
    YELLOW_TIME = 2
    GREEN_TIME = 5

    def __init__(self, initial_color=RED):
        self.__color = initial_color

    def running(self):
        print('Press Ctrl+C to exit')
        while True:
            print(f'Trafic light color is: {self.__color}')
            self.__light_processors()[self.__color]()

    def __light_processors(self):
        return {
            self.RED: self.__red,
            self.YELLOW: self.__yellow,
            self.GREEN: self.__green
        }

    def __red(self):
        self.__sleep_for(self.RED_TIME)
        self.__color = self.YELLOW

    def __yellow(self):
        self.__sleep_for(self.YELLOW_TIME)
        self.__color = self.GREEN

    def __green(self):
        self.__sleep_for(self.GREEN_TIME)
        self.__color = self.RED

    def __sleep_for(self, seconds):
        sleep(seconds)
