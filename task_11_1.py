class Date:
    def __init__(self, date: str):
        self.date = date
        self.type_int = type_int
        self.valid_date = valid_date


        @classmethod
        def type_int(cls, date):
            cls.date = date
            day, month, year = int(date.split('-'))
            print(f'Мы разделили дату на числа: {day}, {month}, {year}')


        @staticmethod
        def valid_date(day: int, month: int, year: int):
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


#????????????????????????
if __name__ == '__main__':
    d = Date('22-12-2022')
    print(Date.type_int)
    print(Date.valid_date)
