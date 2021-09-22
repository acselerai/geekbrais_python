FIRST_DAY = 1
DAY_INCREMENT = 1
DISTANCE_PERCENTAGE_INCREMENT = 0.1

first_day_distance = int(input("Enter first day result: "))
desired_distance = int(input("Enter disared distance: "))

day = FIRST_DAY

while first_day_distance < desired_distance:
    increment = first_day_distance * DISTANCE_PERCENTAGE_INCREMENT
    first_day_distance = first_day_distance + increment
    day += DAY_INCREMENT
else:
    print(f"You will reach your distance on {day} day")
