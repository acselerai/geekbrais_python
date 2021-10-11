from car import TownCar, PoliceCar, WorkCar, SportCar

town_car = TownCar(
    speed=100,
    color='white',
    name='town car',
    is_police=False
)
police_car = PoliceCar(
    speed=200,
    color='blue',
    name='police car',
    is_police=True
)
work_car = WorkCar(
    speed=80,
    color='yellow',
    name='work car',
    is_police=False
)
sport_car = SportCar(
    speed=350,
    color='black',
    name='speed car',
    is_police=False
)

cars = [town_car, police_car, work_car, sport_car]

for car in cars:
    print(f'Car name:{car.name}')
    print(f'Car color:{car.color}')
    print(f'Car speed:{car.speed}')
    print(f'Is car a police:{car.is_police}')
    print(f'GO: {car.go()}')
    print(f'Turn: {car.turn("to the north")}')
    print(f'Stop: {car.stop()}')
    print(f'Show speed: {car.show_speed()}')
    print('*' * 100)
