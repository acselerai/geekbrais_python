def int_func(words):
    return ' '.join(
        [word.title() for word in words.split()]
    )


print(
    int_func('one two three four')
)
