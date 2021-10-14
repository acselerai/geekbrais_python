from re import findall

DIGIT_REGEX = r'\d+'
SUBJECT_LESSONS_SEPARATOR = ': '


def calculate_subject_lessons(parsed_line):
    return sum(
        [int(token) for token in findall(DIGIT_REGEX, parsed_line)]
    )


with open('task_6.txt', 'r') as file:
    subject_lessons = [line.split(SUBJECT_LESSONS_SEPARATOR) for line in file]

result = {
    subject_lesson[0]: calculate_subject_lessons(subject_lesson[1])
    for subject_lesson in subject_lessons
}

print(result)
