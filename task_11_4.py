class Storage:
    def __init__(self):
        self.storage = []

    # def add_to_storage(self):



class Equipment:
    def __init__(self, name, price, quantity, *args):
        self.our_equipment = set()
        self.name = name
        self.price = price
        self.quantity = quantity
        self.equipment = dict()
    # def __str__(self):
    #     return f'{self.name} цена {self.price} количество {self.quantity}'

    def order(self):
        """Формируем перечень техники для заказа"""
        try:
            eq_name = input(f'Введите название: ')
            eq_price = int(input(f'Введите цену за 1 ед: '))
            eq_quantity = int(input(f'Введите количество: '))
            eq = {'Модель устройства': eq_name, 'Цена за 1 ед': eq_price, 'Количество': eq_quantity}
            self.equipment.update(eq)
            return f'Заказана единица техники - {self.equipment}'
        except:
            return f'Ввели неверные данные'


class Printer(Equipment):
    pass


class Scanner(Equipment):
    pass


class Copier(Equipment):
    pass


eq_1 = Printer('hp', 2000, 5, 10)
eq_2 = Scanner('Canon', 1200, 5, 10)
eq_3 = Copier('Xerox', 1500, 1, 15)
print(eq_1.order())
print(eq_2.order())
print(eq_3.order())
print(eq_1.order())
print(eq_1.order())







#
#
#
# class Office:
#     def __init__(self):
#         self.office: set = set()
#
#
#     def add_to_office(self, *args):
#         """Доставить технику в офис"""
#         count = 0
#         for equipment in args:
#             if not isinstance(equipment, Equipment):
#                 print('Мы поставляем в офис только технику')
#                 continue
#             self.office.add(equipment)
#             count += 1
#         print(f'Достаивли технику в офис в количестве: {count}')
#
#     def __iadd__(self, other):
#         if not isinstance(other, Equipment):
#             raise TypeError('Доставляем только технику')
#         self.office.add(other)
#         print(f'В офис доставлена новая техника')
#
#
#
# class Equipment:
#     def __init__(self, size: float, warehouse: set):
#         self.size = size
#         self.warehouse = warehouse
#         self.warehouse.add(self)
#         print(f'Новая единица орг.техники размера {self.size} куплена в офис')
#         print(office)
#
#     def take_out(self):
#         """Увезти технику из офиса"""
#         self.warehouse.discard(self)
#         print('Увезли 1 единицу техники')
#
#
# thing_1 = Equipment(2, office)
#
# # class Printer(Equipment):
# #
# # class Scanner(Equipment):
# #
# # class Copier(Equipment)