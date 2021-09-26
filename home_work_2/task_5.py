rating_list = [7, 5, 3, 3, 2]

user_input = int(input('Enter the new ratiny value: '))

rating_list.append(user_input)
rating_list.sort(reverse=True)

print(rating_list)
