class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_string(cls, date):
        try:
            day, month, year = date.split('-')
            if day.isdigit() and month.isdigit() and year.isdigit():
                return f'Разделили дату на день: {day}, месяц: {month}, год: {year}'
            else:
                raise ValueError(f'"{date}" - не числовое значение')
        except ValueError as err:
            return err

    @staticmethod
    def valid_date(date):
        try:
            day, month, year = map(int, date.split('-'))
            if month == 2 and day > 28:
                return f'В феврале не может быть больше 28 дней, кроме високосного года'
            if 1 <= day <= 31:
                if 1 <= month <= 12:
                    if len(f'{year}') == 4:
                        return f'Корректная дата: {date}'
                    else:
                        return f'Некорректный год: {year}'
                else:
                    return f'Некорректный месяц: {month}'
            else:
                return f'Некорректный день: {day}'
        except ValueError as err:
            return f'{err} - это не числовое значение'


date_1 = Date.date_string('19-03-1995')
print(date_1)
date_2 = Date.valid_date('28-02-2022')
print(date_2)
date_3 = Date.valid_date('31-02-2022')
print(date_3)
date_4 = Date.valid_date('32-03-2022')
print(date_4)
date_5 = Date.valid_date('19-14-1995')
print(date_5)
date_6 = Date.valid_date('04-04-0234')
print(date_6)
date_8 = Date.date_string('so-happy-year')
print(date_8)
date_7 = Date.valid_date('so-happy-year')
print(date_7)
