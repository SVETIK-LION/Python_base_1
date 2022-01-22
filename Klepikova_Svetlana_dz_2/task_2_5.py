from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    for i in range(len(list_in)):
        list_in[i] = f'{int(list_in[i])} руб {(list_in[i] % 1) * 100:.0f} коп'
    return list_in


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
print(id(my_list))
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(id(result_2))
print(f'Отсортированный по возрастанию исходный список: {result_2}')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    return list_out


print(id(my_list))
result_3 = sort_price_adv(my_list)
print(id(result_3))
print(f'Отсортированный по убыванию новый список: {result_3}')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    largest_5 = []
    for i in range(5):
        largest = max(list_in)
        largest_5.append(largest)
        list_in.remove(largest)
    return largest_5


result_4 = check_five_max_elements(my_list)
print(result_4)
