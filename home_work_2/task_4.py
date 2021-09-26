user_input = input('Enter the sentece: ')

words_list = user_input.split()

for index, word in enumerate(words_list):
    print(f'{index + 1}. {word[0:10]}')
