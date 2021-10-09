with open('task_2.txt', 'r') as file:
    words_in_line = [len(line.split()) for line in file]
    print(f'Lines in the file: {len(words_in_line)}')
    for index, words in enumerate(words_in_line):
        print(f'{index + 1} line contains {words} words')
