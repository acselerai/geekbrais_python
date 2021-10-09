with open('task_1.txt', 'a') as file:
    while True:
        user_input = input(">>>: ")
        if user_input:
            file.write(user_input + '\n')
        else:
            break
