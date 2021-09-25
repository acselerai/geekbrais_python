input_seconds = int(input("Enter seconds: "))

HOUR_IN_SECONDS = 3600
HOURS_IN_A_DAY = 24
MINUTE_IN_SECONDS = 60

hours = (input_seconds // HOUR_IN_SECONDS) % HOURS_IN_A_DAY
minutes = (input_seconds % HOUR_IN_SECONDS) // MINUTE_IN_SECONDS
seconds = (input_seconds % HOUR_IN_SECONDS) % MINUTE_IN_SECONDS

formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

print(formatted_time)
