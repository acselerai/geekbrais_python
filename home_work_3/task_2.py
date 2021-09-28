def user_info(**kwargs):
    result = [f'{key}: {value}' for key, value in kwargs.items()]
    print(' | '.join(result))


user_info(
    **{
        'first_name': 'Foo',
        'last_name': 'Bar',
        'year_of_birth': 2000,
        'city': 'City',
        'email': 'test@test.com',
        'phone_number': '+100000000000'
    }

)
