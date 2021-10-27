from date import Date, InvalidDateError


def wrap_validation(func, *args):
    try:
        func(*args)
    except InvalidDateError as err:
        return err


valid_date = Date('12-12-2000')
invalid_day_date = Date('44-12-2000')
invalid_month_date = Date('12-14-2000')
invalid_year_date = Date('12-12-1900')

extracted_valid_date = Date.extract_date(valid_date)
extracted_invalid_day_date = Date.extract_date(invalid_day_date)
extracted_invalid_month_date = Date.extract_date(invalid_month_date)
extracted_invalid_year_date = Date.extract_date(invalid_year_date)

print(f'Extracted date: {extracted_valid_date}')
print(f'Extracted date: {extracted_invalid_day_date}')
print(f'Extracted date: {extracted_invalid_month_date}')
print(f'Extracted date: {extracted_invalid_year_date}')


print(Date.validate_date(*extracted_valid_date))

print(
    wrap_validation(
        Date.validate_date,
        *extracted_invalid_day_date
    )
)

print(
    wrap_validation(
        Date.validate_date,
        *extracted_invalid_month_date
    )
)

print(
    wrap_validation(
        Date.validate_date,
        *extracted_invalid_year_date
    )
)
