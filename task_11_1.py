class Date:
    def __init__(self, date: str):
        self.date = date


    @classmethod
    def type_int(cls, date):
        cls.date = date
        day, month, year = date.split('-')
        print(f'Мы разделили дату на числа: {day}, {month}, {year}')
        s = f'{day} {month} {year}'
        return s


    @staticmethod
    def valid_date(s: str):
        day, month, year = s.split(' ')
        day, month = int(day), int(month)
        if day < 1 or day > 31:
            raise ValueError(f'Неверное значение: {day}')
        elif month < 1 or month > 12:
            raise ValueError(f'Неверное значение: {month}')
        elif month == 2 and day > 28:
            raise ValueError(f'Неверное значение: {day}')
        elif len(year) < 4 or len(year) > 4:
            raise ValueError(f'Неверное значение: {year}')
        else:
            print('Все хорошо, дата правильная :)')


if __name__ == '__main__':
    try:
        d = Date.type_int('28-02-2022')
        Date.valid_date(d)
    except ValueError as err:
        print(err)
