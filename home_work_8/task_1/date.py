class InvalidDateError(Exception):
    pass


class Date():
    def __init__(self, date_str):
        self._date_str = date_str

    @classmethod
    def extract_date(cls, date):
        return [int(str) for str in date._date_str.split('-')]

    @staticmethod
    def validate_date(day, month, year):
        if not 1 <= day <= 31:
            raise InvalidDateError(
                'Day should be between 1 and 31'
            )
        elif not 1 <= month <= 12:
            raise InvalidDateError(
                'Month should be between 1 and 12'
            )
        elif not 1960 <= year <= 9999:
            raise InvalidDateError(
                f'{year} year is not supported'
            )
        return 'Date is valid'
