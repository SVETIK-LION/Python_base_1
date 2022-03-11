class Warehouse:
    def __init__(self):
        self.dict = {'Принтеры': [], 'Сканеры': [], 'Копиры': []}


class OfficeEquipment:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f'Бренд: {self.brand}, модель: {self.model}, год выпуска: {self.year}'


    def adding(self, quantity):
        """Добавить технику на склад"""





class Printer(OfficeEquipment):
    def __init__(self, brand, model, year, print_speed):
        super().__init__(brand, model, year)
        self.print_speed = print_speed

    def action(self):
        return f'Печатает'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, year, scan_quality):
        super().__init__(brand, model, year)
        self.scan_quality = scan_quality

    def action(self):
        return f'Сканирует'


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, year, copy_speed):
        super().__init__(brand, model, year)
        self.copy_speed = copy_speed

    def action(self):
        return f'Копирует'


eq_1 = Printer('hp', 2000, 2014, 10)
eq_2 = Scanner('Canon', 1200, 2020, 10)
eq_3 = Xerox('Xerox', 1500, 2019, 15)
print(eq_1)
print(eq_1.action())
print()
print(eq_2)
print(eq_2.action())
print()
print(eq_3)
print(eq_3.action())
