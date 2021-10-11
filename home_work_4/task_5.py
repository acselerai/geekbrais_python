from functools import reduce


print(
    reduce(
        lambda first, second: first * second,
        [element for element in range(100, 1001)[::2]]
    )
)
