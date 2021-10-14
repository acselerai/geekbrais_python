TRANSLATIONS = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
SEPARATOR = ' - '


with open('task_4.txt', 'r') as file:
    parsed_dict = dict(
        [line.split(SEPARATOR) for line in file]
    )


translated_dict = {
    TRANSLATIONS[key]: value for (key, value) in parsed_dict.items()
}

with open('task_4_translated.txt', 'w') as file:
    for key, value in translated_dict.items():
        file.write(f'{key}{SEPARATOR}{value}')
