class Warehouse:
    """Склад, на котором хранится вся техника"""
    dict_eq = {'Принтеры': [], 'Сканеры': [], 'Копиры': []}


class OfficeEquipment:
    """Класс, описывающий общие параметры офисной техники"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def __str__(self):
        if not isinstance(self.model, int) or not isinstance(self.year, int):
            print('Не числовое значение')
        else:
            return f'Бренд: {self.brand}, модель: {self.model}, год выпуска: {self.year}'


    def adding(self):
        """Добавить технику на склад"""
        if isinstance(self, Printer):
            Warehouse.dict_eq['Принтеры'].append((self.brand, self.model, self.year, self.print_speed))
        elif isinstance(self, Scanner):
            Warehouse.dict_eq['Сканеры'].append((self.brand, self.model, self.year, self.scan_quality))
        elif isinstance(self, Copier):
            Warehouse.dict_eq['Копиры'].append((self.brand, self.model, self.year, self.copy_speed))


    @classmethod
    def count(cls):
        cls.num += 1


    def show(self):
        print(f'Весь склад: {Warehouse.dict_eq}')
        self.count()

    @staticmethod
    def warehouse_count():
        return f'Принтеров: {Printer.num}, Сканеров: {Scanner.num}, Копиров: {Copier.num}'

class Printer(OfficeEquipment):
    num = 0
    def __init__(self, brand, model, year, print_speed):
        super().__init__(brand, model, year)
        self.print_speed = print_speed
    def __str__(self):
        if not isinstance(self.model, int) or not isinstance(self.year, int) or not isinstance(self.print_speed, int):
            return f'{self.model} или {self.year}, или {self.print_speed} - не числовое значение'
        else:
            return f'Бренд: {self.brand}, модель: {self.model}, год выпуска: {self.year}, скорость печати: {self.print_speed}'

    def action(self):
        return f'Печатает'


class Scanner(OfficeEquipment):
    num = 0
    def __init__(self, brand, model, year, scan_quality):
        super().__init__(brand, model, year)
        self.scan_quality = scan_quality

    def __str__(self):
        return f'Бренд: {self.brand}, модель: {self.model}, год выпуска: {self.year}, качество сканирования: {self.scan_quality}'

    def action(self):
        return f'Сканирует'


class Copier(OfficeEquipment):
    num = 0
    def __init__(self, brand, model, year, copy_speed):
        super().__init__(brand, model, year)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'Бренд: {self.brand}, модель: {self.model}, год выпуска: {self.year}, скорость копирования: {self.copy_speed}'

    def action(self):
        return f'Копирует'


eq_1 = Printer('hp', '2000', 2014, 10)
eq_2 = Scanner('Canon', 1200, 2020, 10)
eq_3 = Copier('Xerox', 1500, 2019, 15)
eq_4 = Copier('Marusya', 4939, 2022, 25)


print(eq_1)
print(eq_1.action())
eq_1.adding()
eq_1.show()
print(eq_1.warehouse_count())
print()
print(eq_2)
print(eq_2.action())
eq_2.adding()
eq_2.show()
print(eq_2.warehouse_count())
print()
print(eq_3)
print(eq_3.action())
eq_3.adding()
eq_3.show()
print(eq_3.warehouse_count())
print()
print(eq_4)
print(eq_4.action())
eq_4.adding()
eq_4.show()
print(eq_4.warehouse_count())
